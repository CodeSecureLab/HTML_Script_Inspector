import os
import glob
import re
from  src.models.module import module
from src.connections.cdnjs import get_latest_version_cdnjs
from bs4 import BeautifulSoup
from src.configs.regex_config import ImportPatterns
from prettytable import PrettyTable
import asyncio


def html_files(path, recursive=False):
    if recursive:
        for file in glob.iglob(os.path.join(path, '**', '*.html'), recursive=True):
            yield file
    else:
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith(".html"):
                    yield os.path.join(root, file)

def output_sbom(modules):
    table = PrettyTable()
    table.title = "SBOM Results"
    table.field_names = ["Path", "Module", "Version", "Latest Version"]
    for module in modules:
        table.add_row([module.path, module.module, module.version, module.latest_version])
    print(table)

def gather_latest_versions(modules):
    loop = asyncio.get_event_loop()
    tasks = [get_latest_version_cdnjs(module.module) for module in modules]
    latest_versions = loop.run_until_complete(asyncio.gather(*tasks))
    for module, latest_version in zip(modules, latest_versions):
        module.latest_version = latest_version

def inspect_files(file_list):
    modules = []
    cdn_patterns = ImportPatterns().get_patterns()

    for file in file_list:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            soup = BeautifulSoup(content, 'html.parser')
            script_tags = soup.find_all('script')

            for script in script_tags:
                src = script.get('src')
                if src:
                    module_name = None
                    version = None
                    for cdn, pattern in cdn_patterns.items():
                        match = pattern.search(src)
                        if match:
                            module_name = match.group(1)
                            version = match.group(2) if len(match.groups()) > 1 else None
                            break
                    if not module_name:
                        # Fallback to extract module name without version
                        module_name = src.split('/')[-1].split('.')[0]
                    # Ensure version is only numbers and periods
                    if version and not re.match(r'^[\d\.]+$', version):
                        version = None
                    # Get the line number of the script tag
                    if re.match(r'^[\d\.]+$', module_name):
                        print(f"issue parsing {src}")
                        continue
                    module_obj = module(path=file, script=src, module=module_name, version=version)
                    modules.append(module_obj)
    gather_latest_versions(modules)
    output_sbom(modules)
    return modules
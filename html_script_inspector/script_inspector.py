import os
import glob
import re
from  src.models.module import module
from bs4 import BeautifulSoup
from src.regex_config import ImportPatterns
from prettytable import PrettyTable

def html_files(path, recursive=False):
    if recursive:
        for file in glob.iglob(os.path.join(path, '**', '*.html'), recursive=True):
            yield file
    else:
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith(".html"):
                    yield os.path.join(root, file)

def pretty_table(modules):
    table = PrettyTable()
    table.field_names = ["Path", "Module", "Version", "Line"]
    for module in modules:
        table.add_row([module.path, module.module, module.version if module.version else "None", module.line])
    print(table)

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
                    # Get the line number of the script tag
                    line_number = content[:content.find(src)].count('\n') + 1
                    module_obj = module(path=file, module=module_name, version=version, line=line_number)
                    modules.append(module_obj)
    pretty_table(modules)
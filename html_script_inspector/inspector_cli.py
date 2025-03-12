"""command line interface for http_script_inspector"""
import argparse
import logging
import json
from src.script_inspector import html_files, inspect_files
from src.script_vulnerabilities import get_script_vulns


def inspector_cli():
    parser = argparse.ArgumentParser(description="Inspect http scripts")
    parser.add_argument("--path", help="path to inspect")
    parser.add_argument("-R", "--recursive", action="store_true", help="recursively inspect directories", default=False)
    parser.add_argument("--oss", action="store_true", help="inspect for open source vulnerabilities", default=False)
    parser.add_argument("--sbom_output", help="sbom output file(json)", default=None)
    parser.add_argument("--vuln_output", help="vulnerability output file(json)", default=None)
    parser.add_argument("--user", help="oss index username", default=None)
    parser.add_argument("--key", help="oss index key", default=None)

    args = parser.parse_args()
    #function to get all html files
    html_file_list = html_files(args.path, recursive=args.recursive)
    #main function for inspection
    modules = inspect_files(html_file_list)
    if args.oss:
        #inspect for open source vulnerabilities
        if args.user is None or args.key is None:
            logging.error("Must provide oss username and key")
            exit(1)
        vulnerabilities = get_script_vulns(modules, args.user, args.key)
        if args.vuln_output:
            # output vulnerabilities to file
            with open(args.vuln_output, 'w') as f:
                json.dump(vulnerabilities, f, indent=4)
    if args.sbom_output:
        # output sbom to file
        with open(args.sbom_output, 'w') as f:
            json.dump([module.__dict__ for module in modules], f, indent=4)

        



if __name__ == "__main__":
    inspector_cli()

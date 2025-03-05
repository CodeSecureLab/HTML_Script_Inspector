"""command line interface for http_script_inspector"""
import argparse
import logging
from src.script_inspector import html_files, inspect_files
from src.script_vulnerabilities import get_script_vulns
import dotenv

def main():
    dotenv.load_dotenv()
    parser = argparse.ArgumentParser(description="Inspect http scripts")
    parser.add_argument("--path", help="path to inspect")
    parser.add_argument("-R", "--recursive", action="store_true", help="recursively inspect directories", default=False)
    parser.add_argument("--oss", action="store_true", help="inspect for open source vulnerabilities", default=False)
    parser.add_argument("--output", help="output file", default=None)

    args = parser.parse_args()
    #function to get all html files
    html_file_list = html_files(args.path, recursive=args.recursive)
    #main function for inspection
    modules = inspect_files(html_file_list)
    if args.oss:
        #inspect for open source vulnerabilities
        get_script_vulns(modules)
        



if __name__ == "__main__":
    main()

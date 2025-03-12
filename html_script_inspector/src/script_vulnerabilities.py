
from src.connections.oss import get_vulnerabilities_oss
from prettytable import PrettyTable
from dotenv import load_dotenv

def get_script_vulns(modules, user, key):
    vulnerabilities = get_vulnerabilities_oss(modules, user, key)
    display_vulnerabilities(vulnerabilities)
    return vulnerabilities
    
def display_vulnerabilities(vulnerabilities):
    table = PrettyTable()
    table.title = "Vulnerabilities"
    table.field_names = ["Module", "Vulnerability", "CVSS Score"]
    for module, vulns in vulnerabilities.items():
        for vuln in vulns:
            table.add_row([module, vuln['vulnerability'], vuln['cvssScore']])
    print(table)
    
    
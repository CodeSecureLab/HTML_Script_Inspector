
from src.connections.oss import get_vulnerabilities_oss
from prettytable import PrettyTable

def get_script_vulns(modules):
    vulnerabilities = get_vulnerabilities_oss(modules)
    display_vulnerabilities(vulnerabilities)
    
def display_vulnerabilities(vulnerabilities):
    table = PrettyTable()
    table.title = "Vulnerabilities"
    table.field_names = ["Module", "Vulnerability", "CVSS Score"]
    for module, vulns in vulnerabilities.items():
        for vuln in vulns:
            table.add_row([module, vuln['vulnerability'], vuln['cvssScore']])
    print(table)
    
    
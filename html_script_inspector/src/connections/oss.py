import requests
from requests.auth import HTTPBasicAuth
from os import environ
from dotenv import load_dotenv

def get_vulnerabilities_oss(modules, email, api_token):
    url = "https://ossindex.sonatype.org/api/v3/component-report"
    coordinates = [f"pkg:npm/{module.module}@{module.version}" for module in modules if module.version is not None]
    payload = {
        "coordinates": coordinates
    }
    auth = HTTPBasicAuth(email, api_token)
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers, auth=auth)
    if response.status_code == 200:
        vulnerabilities = {}
        data = response.json()
        for vulnerability in data:
            vulnerabilities[vulnerability['coordinates']] = []
            for vuln in vulnerability['vulnerabilities']:
                vulnerabilities[vulnerability['coordinates']].append({"vulnerability": vuln['displayName'], "cvssScore": vuln['cvssScore']})
        return vulnerabilities
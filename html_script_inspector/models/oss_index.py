from dataclasses import dataclass
from typing import Optional, List

@dataclass
class OssIndex:
    id: str
    title: str
    description: str
    severity: str
    cvss_score: Optional[float]
    cwe_ids: Optional[List[str]]
    cve_ids: Optional[List[str]]
    references: Optional[List[str]]
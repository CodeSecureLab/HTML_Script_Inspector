from dataclasses import dataclass
from typing import Optional
from src.connections.cdnjs import get_latest_version_cdnjs


@dataclass
class module:
    path: str
    script: str
    module: str
    version: str
    latest_version: str = "Not Found"

    @property
    def cdn(self):
        if self.path.startswith("http"):
            return self.path.split("/")[2]
        return None

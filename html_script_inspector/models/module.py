from dataclasses import dataclass
from typing import Optional


@dataclass
class module:
    path: str
    module: str
    line: str
    version: str = "None"

    @property
    def cdn(self):
        if self.path.startswith("http"):
            return self.path.split("/")[2]
        return None
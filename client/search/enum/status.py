from dataclasses import dataclass
from enum import Enum

@dataclass
class Status(Enum):
    GOOD = "good"
    RENEW = "renew"

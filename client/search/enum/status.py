from dataclasses import dataclass
from enum import Enum

@dataclass
class Status(str, Enum):
    GOOD = "good"
    RENEW = "renew"
    NEW_DEVELOPMENT = "newdevelopment"

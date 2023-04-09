from dataclasses import dataclass
from enum import Enum


@dataclass
class TenantGender(Enum):
    MIXED = "mixed"
    MALE = "male"
    FEMALE = "female"
from enum import Enum


class SinceDate(Enum):
    LAST_WEEK = "W"
    LAST_MONTH= "M"
    LAST_DAY = "T"
    LAST_TWO_DAYS = "Y"

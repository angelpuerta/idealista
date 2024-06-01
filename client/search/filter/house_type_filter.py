from dataclasses import dataclass


@dataclass
class HouseTypeFilter:
    flat: bool
    penthouse: bool
    duplex: bool
    studio: bool
    chalet: bool
    countryHouse: bool

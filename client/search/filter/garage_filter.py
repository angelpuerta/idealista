from dataclasses import dataclass


@dataclass
class GarageFilter:
    bankOffer: bool
    automaticDoor: bool
    motorcycleParking: bool
    security: bool

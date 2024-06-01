from dataclasses import dataclass
from typing import List

from client.search.enum.building_type import BuildingType


@dataclass
class PremiseFilter:
    virtualTour: bool
    location: str
    corner: bool
    airConditioning: bool
    smokeVentilation: bool
    heating: bool
    transfer: bool
    buildingTypes: List[BuildingType]
    bankOffer: bool

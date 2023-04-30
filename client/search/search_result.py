from dataclasses import dataclass
from typing import List

from client.search.enum.operation import Operation
from client.search.enum.status import Status


@dataclass
class ParkingSpace:
    hasParkingSpace: bool
    isParkingSpaceIncludedInPrice: bool
    parkingSpacePrice: float


@dataclass
class DetailedType:
    typology: str
    subtipology: str


@dataclass
class Property:
    address: str
    bathrooms: int
    country: str
    distance: str
    district: str
    exterior: bool
    hasVideo: bool
    latitude: float
    longitude: float
    municipality: str
    neighborhood: str
    numPhotos: int
    operation: Operation
    price: float
    propertyCode: str
    province: str
    rooms: int
    showAddress: bool
    size: float
    url: str
    status: Status
    newDevelopment: bool
    priceByArea: float
    detailedType: DetailedType
    hasPlan: bool
    propertyType: dict | str
    detailedType: dict
    suggestedTexts: dict
    has3DTour: bool
    has360: bool
    hasStaging: bool
    topNewDevelopment: bool
    superTopHighlight: bool
    description: str = ""
    thumbnail: str = ""
    externalReference: str = None
    floor: str = None
    hasLift: bool = None
    tenantGender: str = None
    garageType: str = None
    hasLift: bool = None
    newDevelopmentFinished: bool = None
    isSmokingAllowed: bool = None


@dataclass
class SearchPage():
    actualPage: int
    itemsPerPage: int
    lowerRangePosition: int
    paginable: bool
    summary: List[str]
    total: int
    totalPages: int
    upperRangePosition: int
    elementList: List[Property]
    numPaginations: int
    alertName: str
    totalAppliedFilters: int

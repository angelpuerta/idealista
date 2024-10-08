from dataclasses import dataclass, field
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
    priceByArea: float
    detailedType: DetailedType
    size: float
    url: str
    propertyType: dict | str
    detailedType: dict
    suggestedTexts: dict
    status: Status = field(default_factory=lambda: Status.UNKNOWN)  
    showAddress: bool = False
    newDevelopment: bool = False
    hasPlan: bool = False
    has3DTour: bool = False
    has360: bool = False
    hasStaging: bool = False
    topNewDevelopment: bool = False
    superTopHighlight: bool = False
    description: str = ""
    thumbnail: str = ""
    exterior: bool = False
    externalReference: str = None
    floor: str = None
    hasLift: bool = None
    tenantGender: str = None
    garageType: str = None
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

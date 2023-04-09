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
    floor: str
    hasVideo: bool
    latitude: float
    longitude: float
    municipality: str
    neighborhood: str
    numPhotos: int
    operation:  Operation
    price: int
    propertyCode: int
    province: str
    region: str
    rooms: int
    showAddress: bool
    size: int
    subregion: str
    thumbnail: str
    url: str
    status: Status
    newDevelopment: bool
    tenantGender: str
    garageType: str
    parkingSpace: ParkingSpace
    hasLift: bool
    newDevelopmentFinished: bool
    isSmokingAllowed: bool
    priceByArea: float
    detailedType: DetailedType
    externalReference: str

@dataclass
class SearchPage:
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
    alertName:str
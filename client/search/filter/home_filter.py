from client.search.enum.bathroom import BathRoom
from client.search.enum.bedroom import BedRoom
from client.search.enum.furnised import Furnished
from client.search.enum.status import Status


class HomeFilter:
    virtualTour: bool
    bedrooms: BedRoom
    bathrooms: BathRoom
    preservation: Status
    newDevelopment: bool
    furnished: Furnished
    bankOffer: bool
    garage: bool
    terrace: bool
    exterior: bool
    elevator: bool
    swimmingPool: bool
    airConditioning: bool
    storeRoom: bool
    builtinWardrobes: bool

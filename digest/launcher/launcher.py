import logging

from client.search.enum.operation import Operation
from client.search.enum.status import Status
from client.search.search_result import Property, ParkingSpace
from digest.pipeline.pipeline_reader import pipelines
from digest.search.search import search
from digest.store.store_service import store_service


def launch(name: str):
    logging.debug(f'Executing pipe {name}')
    if name not in pipelines:
        raise Exception(f'Pipeline {name} not in pipelines.yaml')
    pipeline = pipelines[name]
    #result = search.query(pipeline)
    result = [
        Property(
            address="123 Main Street",
            bathrooms=2,
            country="United States",
            distance="10 miles",
            district="Downtown",
            exterior=True,
            floor="4th",
            hasVideo=True,
            latitude=37.7749,
            longitude=-122.4194,
            municipality="San Francisco",
            neighborhood="South of Market",
            numPhotos=8,
            operation=Operation.RENT,
            price=3000,
            propertyCode=1234567,
            province="California",
            region="West",
            rooms=3,
            showAddress=True,
            size=1000,
            subregion="San Francisco Bay Area",
            thumbnail="https://example.com/thumbnail.jpg",
            url="https://example.com/property/1234567",
            status=Status.GOOD,
            newDevelopment=False,
            tenantGender="Any",
            garageType=None,
            parkingSpace=None,
            hasLift=True,
            newDevelopmentFinished=False,
            isSmokingAllowed=True,
            priceByArea=3,
            detailedType=None,
            externalReference="ABCD1234"
        ),
        Property(
            address="123 Main Street",
            bathrooms=2,
            country="United States",
            distance="10 miles",
            district="Downtown",
            exterior=True,
            floor="4th",
            hasVideo=True,
            latitude=37.7749,
            longitude=-122.4194,
            municipality="San Francisco",
            neighborhood="South of Market",
            numPhotos=8,
            operation=Operation.RENT,
            price=3000,
            propertyCode=1234567,
            province="California",
            region="West",
            rooms=3,
            showAddress=True,
            size=1000,
            subregion="San Francisco Bay Area",
            thumbnail="https://example.com/thumbnail.jpg",
            url="https://example.com/property/1234567",
            status=Status.GOOD,
            newDevelopment=False,
            tenantGender="Any",
            garageType=None,
            parkingSpace=None,
            hasLift=True,
            newDevelopmentFinished=False,
            isSmokingAllowed=True,
            priceByArea=3,
            detailedType=None,
            externalReference="ABCD1234"
        )

    ]
    store_service.store(pipeline, result)

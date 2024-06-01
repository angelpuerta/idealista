from client.search.defaults.load_cities import city_coordinates
from client.search.query.geo_coordinates import GeoCoordinates
from client.search.query.geo_query import GeoQuery


def from_city(city: str, distance: int = 1000) -> GeoQuery:
    if city not in city_coordinates:
        raise ValueError("City not found in defaults/cities.csv")
    latitude = city_coordinates[city]['latitude']
    longitude = city_coordinates[city]['longitude']
    return GeoQuery(distance=distance, center=GeoCoordinates(latitude, longitude))


def from_location(latitude, longitude, distance: int = 1000) -> GeoQuery:
    return GeoQuery(distance=distance, center=GeoCoordinates(latitude, longitude))

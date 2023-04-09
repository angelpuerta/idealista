from dataclasses import dataclass

from client.search.query.geo_coordinates import GeoCoordinates


@dataclass
class GeoQuery:
    center: GeoCoordinates
    distance: float

    def to_dict(self):
        return {
            'distance': self.distance,
            'center': f'{self.center.latitude},{self.center.longitude}'
        }

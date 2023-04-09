from dataclasses import dataclass

from client.search.enum.since_date import SinceDate


@dataclass
class BasicFilter:
    minSize: float | None
    maxSize: float | None
    maxPrice: float | None
    minPrice: float | None
    sinceDate: SinceDate

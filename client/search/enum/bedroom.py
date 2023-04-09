from typing import List

MAX_BEDROOM_SIZE = 4


class BedRoom:
    bedrooms_combinations: List[int] = []

    def __init__(self, *numbers):
        for val in numbers:
            if int(val) <= MAX_BEDROOM_SIZE:
                self.bedrooms_combinations.append(int(val))

    @property
    def value(self):
        return ','.join(map(lambda x: str(x), self.bedrooms_combinations))


ZERO_BEDROOM = BedRoom(0)
ONE_BEDROOM = BedRoom(1)
TWO_BEDROOM = BedRoom(2)
THREE_BEDROOM = BedRoom(3)
FOUR_OR_MORE_BEDROOM = BedRoom(4)
ONE_OR_TWO = BedRoom(1, 2)
TWO_OR_THREE = BedRoom(2, 3)

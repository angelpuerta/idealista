from typing import List

MAX_BATHROOM_SIZE = 3


class BathRoom:
    bathroom_combinations: List[int] = []

    def __init__(self, *numbers):
        for val in numbers:
            if int(val) <= MAX_BATHROOM_SIZE:
                self.bathroom_combinations.append(int(val))

    @property
    def value(self):
        return ','.join(map(lambda x: str(x), self.bathroom_combinations))

ZERO_BATHROOM = BathRoom(0)
ONE_BATHROOM = BathRoom(1)
TWO_BATHROOM = BathRoom(2)
ONE_OR_TWO_BATHROOM = BathRoom(1,2)
THREE_OR_MORE_BATHROOM = BathRoom(3)
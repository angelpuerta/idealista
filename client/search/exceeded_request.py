from dataclasses import dataclass


@dataclass
class ExceededRequest:

    def __bool__(self):
        return False
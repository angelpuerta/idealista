from dataclasses import dataclass


@dataclass
class SearchError:
    status: str
    message: str

    def __bool__(self):
        return False

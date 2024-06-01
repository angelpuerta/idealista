from dataclasses import dataclass


@dataclass
class ExceededRequest:

    def __str__(self):
        return "The number of requests have exceeded the token"

    def __bool__(self):
        return False
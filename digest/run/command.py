from dataclasses import dataclass


@dataclass
class Command:
    function: str
    arg: str
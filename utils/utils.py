from dataclasses import asdict
from enum import Enum


def map_values(v):
    if isinstance(v, Enum):
        return v.value
    return v


def parse_dict(values: dict) -> dict:
    return {k: map_values(v) for k, v in filter(lambda items: items[1], values.items())}


def to_dict(object) -> dict:
    return {k: map_values(v) for k, v in filter(lambda items: items[1], asdict(object).items())}

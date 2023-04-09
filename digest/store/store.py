from dataclasses import dataclass

from digest.store.store_type import StoreType


@dataclass
class Store:
    type: StoreType
    output: str
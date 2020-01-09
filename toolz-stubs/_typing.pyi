from typing_extensions import Protocol
from typing import Any, Generic, Mapping, TypeVar

M = TypeVar("M", bound=Mapping)

P = TypeVar("P")
T = TypeVar("T")
U = TypeVar("U")
V = TypeVar("V")

HTU_ = HasGetItem[T, U]
HVU_ = HasGetItem[V, U]

HTU = TypeVar("HTU", bound=HTU_)
HVU = TypeVar("HVU", bound=HVU_)

CT = TypeVar("CT", contravariant=True)
OU = TypeVar("OU", covariant=True)

class RandomLike(Protocol):
    def random(self) -> float: ...

class HasGetItem(Protocol, Generic[CT, OU]):
    def __getitem__(self, item: CT) -> OU: ...

class MappingFactory(Generic[T, U]):
    def __call__(self) -> Mapping[T, U]: ...

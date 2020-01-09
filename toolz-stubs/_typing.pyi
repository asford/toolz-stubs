from typing_extensions import Protocol
from typing import Any, Generic, TypeVar

T = TypeVar("T")
U = TypeVar("U")
CT = TypeVar("CT", contravariant=True)
OU = TypeVar("OU", covariant=True)

class RandomLike(Protocol):
    def random(self) -> float: ...

class HasGetItem(Protocol, Generic[CT, OU]):
    def __getitem__(self, item: CT) -> OU: ...

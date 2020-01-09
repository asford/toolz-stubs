from typing import overload, Any, Callable, Iterable, Iterator, Mapping, List, Optional, Tuple, TypeVar, Union
from ._typing import MappingFactory
from ._typing import P, T, U, V

def merge(*dicts: Mapping[T, U], **kwargs: Any) -> Mapping[T, U]: ...
def merge_with(func: Any, *dicts: Any, **kwargs: Any): ...
def valmap(func: Callable[[U], V], d: Mapping[T, U], factory: MappingFactory[T, V] = ...) -> Mapping[T, V]: ...
def keymap(func: Callable[[T], V], d: Mapping[T, U], factory: MappingFactory[V, U] = ...) -> Mapping[V, U]: ...
def itemmap(func: Callable[[Tuple[P, T]], Tuple[V, U]], d: Mapping[P, T], factory: MappingFactory[V, U] = ...) -> Mapping[V, U]: ...
def valfilter(predicate: Callable[[U], Any], d: Mapping[T, U], factory: MappingFactory[T, U] = ...) -> Mapping[T, U]: ...
def keyfilter(predicate: Callable[[T], Any], d: Mapping[T, U], factory: MappingFactory[T, U] = ...) -> Mapping[T, U]: ...
def itemfilter(predicate: Callable[[Tuple[T, U]], Any], d: Mapping[T, U], factory: MappingFactory[T, U] = ...) -> Mapping[T, U]: ...
def assoc(d: Mapping[T, U], key: T, value: U, factory: MappingFactory[T, U] = ...) -> Mapping[T, U]: ...
def dissoc(d: Mapping[T, U], *keys: T, **kwargs: Any) -> Mapping[T, U]: ...
def assoc_in(d: Any, keys: Any, value: Any, factory: Any = ...): ...
def update_in(d: Any, keys: Any, func: Any, default: Optional[Any] = ..., factory: Any = ...): ...
def get_in(keys: Any, coll: Any, default: Optional[Any] = ..., no_default: bool = ...): ...

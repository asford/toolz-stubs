from toolz.compatibility import map as map, reduce as reduce
from toolz.itertoolz import partition_all as partition_all
from toolz.utils import no_default as no_default
from typing import Any, Optional

def fold(binop: Any, seq: Any, default: Any = ..., map: Any = ..., chunksize: int = ..., combine: Optional[Any] = ...): ...

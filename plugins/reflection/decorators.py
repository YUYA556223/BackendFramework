from enum import Enum
from inspect import getattr_static
import inspect
from plugins.collections.generic import DictionaryC, KeyValuePair, ListC
from typing import Any, Callable, Optional, Tuple, Type, TypeVar


class AttributeType(Enum):
    STATIC = 1


_T = TypeVar("_T")


class static(object):
    __func__: Callable[..., Any]
    subs = ListC[Tuple[str, str, str, AttributeType]]()

    def __init__(self, fn: Callable[..., Any]) -> None:
        fnname = fn.__name__
        tname = fn.__qualname__.replace("." + fn.__name__, "")
        mname = fn.__module__
        static.subs.Add((mname, tname, fnname, AttributeType.STATIC))
        self.__func__ = fn
        pass

    def __get__(self, obj: _T,
                type: Optional[Type[_T]] = ...) -> Callable[..., Any]:
        return self.__func__

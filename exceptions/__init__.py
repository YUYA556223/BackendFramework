from abc import ABCMeta, abstractmethod
from plugins.reflection.decorators import static


class RequestException(metaclass=ABCMeta):
    """Basic Exception
    """

    @static
    @abstractmethod
    def id():
        return -1

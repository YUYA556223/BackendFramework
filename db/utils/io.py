from sqlalchemy.orm.attributes import InstrumentedAttribute
from sqlalchemy.orm.query import Query
from plugins.collections.generic import ListC
from plugins.reflection.property import PropertyInfo
from typing import Any, Generic, Type, TypeVar

from db.models import DB
from plugins.reflection.type import TypeC, typeof

T = TypeVar("T")


class IOHelper:
    """
    Provides a set of codes for managing database input and output.\n
    @Usage: IOHelper(type).push(instance)
    """
    targetType: TypeC
    __instrumented_attribute_type = typeof(InstrumentedAttribute).TypeInfo

    def __init__(self, t: type) -> None:
        """ Defines database manager
        """
        self.targetType = typeof(t).TypeInfo
        self.__query = DB.session.query(t)

    @staticmethod
    def __build_criterion(instance: T, propinfos: ListC[PropertyInfo]):
        prime_key_cnt = 0
        for prop in propinfos:
            if prop.PropertyType.__name__ == IOHelper.__instrumented_attribute_type.Name:
                static = prop.GetValue()
                instance_val = prop.GetValue(instance)
                if static.primary_key:
                    prime_key_cnt += 1
                    return static == instance_val
        if prime_key_cnt == 0:
            raise KeyError("[Database Error]: Primary key does not exists.")

    @ staticmethod
    def __update_internal(target, value, propinfos: ListC[PropertyInfo]):
        for prop in propinfos:
            if prop.PropertyType.__name__ == IOHelper.__instrumented_attribute_type.Name:
                value = prop.GetValue(value)
                prop.SetValue(value, target)
        return

    __property_info_cache = ListC[PropertyInfo]()
    __property_is_constructed = False

    def write(self, data: Any):
        """
        Writes the given data to the database.\n
        If the data already exists, it will be updated.
        (If it does not exist, it will be created.)\n
        @exception: KeyError: Primary key does not exist. Define Primary Key in model class
        """
        if self.__property_is_constructed == False:
            self.__property_info_cache = self.targetType.GetProperties()
        first = self.__query.filter(
            IOHelper.__build_criterion(data, self.__property_info_cache)).first()
        if first is None:
            DB.session.add(data)
            print("[Database]: the instance of <" + self.targetType.Name +
                  "> was newly added to database")
        else:
            IOHelper.__update_internal(first, data, self.__property_info_cache)
            print("[Database]: the instance of <" + self.targetType.Name +
                  "> was updated")
        DB.session.commit()

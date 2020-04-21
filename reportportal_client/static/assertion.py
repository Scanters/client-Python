# -*- coding: utf-8 -*-
from .exception import RPError

__all__ = [
    "assertion"
]


class Assertion(object):
    def __check_and_raise(self, value, exception_type=RPError, message=""):
        assert issubclass(exception_type, Exception)

        if not value:
            raise exception_type(message)

    def is_true(self, value, message=""):
        self.__check_and_raise(bool(value), message=message)

    def is_false(self, value, message=""):
        self.__check_and_raise(not value, message=message)

    def is_instance(self, obj, types):
        types = types if isinstance(types, tuple) else (types,)
        type_matched = isinstance(obj, types)
        self.__check_and_raise(type_matched)


assertion = Assertion()

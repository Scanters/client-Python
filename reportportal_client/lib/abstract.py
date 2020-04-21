from abc import ABCMeta as _ABCMeta, abstractmethod

__all__ = ["AbstractBaseClass", "abstractmethod"]


class AbstractBaseClass(_ABCMeta):
    """
    Metaclass fot pure Interfacing.
    Being set as __metaclass__, forbids direct object creation from this class, allowing only inheritance.

    i.e.
    class Interface(object):
        __metaclass__ = AbstractBaseClass

    i = Interface() -> will raise TypeError

    meanwhile,

    class Implementation(Interface):
        pass

    i = Implementation() -> success
    """

    _abc_registry = []

    def __call__(cls, *args, **kwargs):
        if cls.__name__ in AbstractBaseClass._abc_registry:
            raise TypeError("No instantiation allowed for Interface-Class '{}'. Please inherit.".format(cls.__name__))

        result = super(AbstractBaseClass, cls).__call__(*args, **kwargs)
        return result

    def __new__(mcs, name, bases, namespace):
        class_ = super(AbstractBaseClass, mcs).__new__(mcs, name, bases, namespace)
        if namespace.get("__metaclass__") is AbstractBaseClass:
            mcs._abc_registry.append(name)
        return class_

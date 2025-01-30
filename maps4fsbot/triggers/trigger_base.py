"""This module contains the TriggerBase class, which is a singleton class that is used as a base 
class for all triggers."""


class Singleton(type):
    """Singleton metaclass."""

    _instances: dict[type, object] = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class TriggerBase(metaclass=Singleton):
    """Base class for all triggers."""

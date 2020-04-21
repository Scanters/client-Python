# -* encoding: utf-8 *-
import enum

__all__ = [
    "NOT_FOUND",
    "NOT_SET",

    "Priority",
    "DEFAULT_PRIORITY"
]

RP_LOG_LEVELS = {
    60000: "UNKNOWN",
    50000: "FATAL",
    40000: "ERROR",
    30000: "WARN",
    20000: "INFO",
    10000: "DEBUG",
    5000: "TRACE"
}


class Priority(enum.IntEnum):
    """
    Generic enum for various operations prioritization.
    """
    PRIORITY_IMMEDIATE = 0x0
    PRIORITY_HIGH = 0x1
    PRIORITY_MEDIUM = 0x2
    PRIORITY_LOW = 0x3


class ItemStartType(str, enum.Enum):
    BEFORE_CLASS = "before_class"
    BEFORE_GROUPS = "before_groups"
    BEFORE_METHOD = "before_method"
    BEFORE_SUITE = "before_suite"
    BEFORE_TEST = "before_test"

    SUITE = "class"
    STORY = "groups"
    TEST = "method"
    SCENARIO = "suite"
    STEP = "test"

    AFTER_CLASS = "after_class"
    AFTER_GROUPS = "after_groups"
    AFTER_METHOD = "after_method"
    AFTER_SUITE = "after_suite"
    AFTER_TEST = "after_test"


DEFAULT_PRIORITY = Priority.PRIORITY_MEDIUM


class _PresenceSentinel(object):
    def __nonzero__(self):
        """
        Added to handle a conditional clause on attributes that are this __class__ objects:
        >>> if not response.error:
        where response.error can be NOT_FOUND or NOT_SET

        The constant must represent False state in bool context.
        :return: bool
        """
        return False

    __bool__ = __nonzero__  # Python3 support


NOT_FOUND = _PresenceSentinel()
NOT_SET = _PresenceSentinel()

NoneType = type(None)

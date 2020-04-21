# -* encoding: utf-8 *-

from Queue import PriorityQueue

from reportportal_client.lib.abstract import AbstractBaseClass
from reportportal_client.static.assertion import assertion
from reportportal_client.static.defines import Priority, DEFAULT_PRIORITY, NOT_SET


class ItemBase(object):
    __metaclass__ = AbstractBaseClass

    def __init__(self, priority=DEFAULT_PRIORITY):
        assertion.is_instance(priority, Priority)
        self._priority = priority  # type: Priority
        self._uid = NOT_SET

    def __ge__(self, other):
        # type: ("ItemBase") -> bool
        return self.priority >= other.priority

    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, value):
        assertion.is_instance(value, Priority)
        self._priority = value


class Item(ItemBase):
    pass


class Tracker(object):
    def __init__(self):
        self._queue = PriorityQueue()

    def add_item(self, item):
        # type: (ItemBase) -> None
        self._queue.put(item)


if __name__ == '__main__':
    q = PriorityQueue()
    q.put(Item(priority=Priority.PRIORITY_IMMEDIATE))
    q.put(Item(priority=Priority.PRIORITY_MEDIUM))
    q.put(Item(priority=Priority.PRIORITY_MEDIUM))
    q.put(Item(priority=Priority.PRIORITY_LOW))
    q.put(Item(priority=Priority.PRIORITY_HIGH))

    res = q.get()
    res = q.get()
    res = q.get()
    res = q.get()
    res = q.get()
    res

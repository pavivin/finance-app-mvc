from enum import Enum


class StrEnum(str, Enum):

    def __str__(self):
        return self._value_

    def __eq__(self, other):
        return str(other) == str(self)

    def __hash__(self):
        return super().__hash__()

    @classmethod
    def all(cls):
        # noinspection PyUnresolvedReferences
        return [t.value for t in cls]
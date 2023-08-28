from __future__ import annotations

from functools import total_ordering


@total_ordering
class AbstractMeasure:
    _value: float

    def __str__(self):
        return self.to_string()

    def __add__(self, other: AbstractMeasure):
        if not isinstance(other, type(self)):
            return NotImplemented
        return type(self)(self._value + other._value)

    def __mul__(self, other: AbstractMeasure):
        if not isinstance(other, type(self)):
            return NotImplemented
        return type(self)(self._value * other._value)

    def __sub__(self, other: AbstractMeasure):
        if not isinstance(other, type(self)):
            return NotImplemented
        return type(self)(self._value - other._value)

    def __truediv__(self, other: AbstractMeasure):
        if not isinstance(other, type(self)):
            return NotImplemented
        return type(self)(self._value / other._value)

    def __mod__(self, other: AbstractMeasure):
        if not isinstance(other, type(self)):
            return NotImplemented
        return type(self)(self._value % other._value)

    def __pow__(self, other: AbstractMeasure):
        if not isinstance(other, type(self)):
            return NotImplemented
        return type(self)(self._value ** other._value)

    def __eq__(self, other: AbstractMeasure):
        if not isinstance(other, type(self)):
            return NotImplemented
        return self._value == other._value

    def __lt__(self, other: AbstractMeasure):
        if not isinstance(other, type(self)):
            return NotImplemented
        return self._value < other._value

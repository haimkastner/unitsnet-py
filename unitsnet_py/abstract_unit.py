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
    
    def _truncate_fraction_digits(self, num: float, fractional_digits: int):
        if fractional_digits is None:
            return num
        # Convert the number to a string with the desired precision
        num_string = format(num, f".{fractional_digits}f")
        
        # Parse the string back to a number
        truncated_num = float(num_string)
        
        if truncated_num % 1 == 0:  # Check if num is an integer, if so convert it to int, so the X.0 will be printed as X only
            return int(truncated_num)

        return truncated_num

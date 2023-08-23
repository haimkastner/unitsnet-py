from __future__ import annotations


class AbstractMeasure:
    _value: float

    def __str__(self):
        return self.to_string()

    def __add__(self, other: AbstractMeasure):
        if not isinstance(other, type(self)):
            raise TypeError(_msg('+', self, other))
        return type(self)(self._value + other._value)

    def __mul__(self, other: AbstractMeasure):
        if not isinstance(other, type(self)):
            raise TypeError(_msg('*', self, other))
        return type(self)(self._value * other._value)

    def __sub__(self, other: AbstractMeasure):
        if not isinstance(other, type(self)):
            raise TypeError(_msg('-', self, other))
        return type(self)(self._value - other._value)

    def __truediv__(self, other: AbstractMeasure):
        if not isinstance(other, type(self)):
            raise TypeError(_msg('/', self, other))
        return type(self)(self._value / other._value)

    def __mod__(self, other: AbstractMeasure):
        if not isinstance(other, type(self)):
            raise TypeError(_msg('%', self, other))
        return type(self)(self._value % other._value)

    def __pow__(self, other: AbstractMeasure):
        if not isinstance(other, type(self)):
            raise TypeError(_msg('**', self, other))
        return type(self)(self._value ** other._value)

    def __eq__(self, other: AbstractMeasure):
        if not isinstance(other, type(self)):
            raise TypeError(_msg('==', self, other))
        return self._value == other._value

    def __lt__(self, other: AbstractMeasure):
        if not isinstance(other, type(self)):
            raise TypeError(_msg('<', self, other))
        return self._value < other._value

    def __gt__(self, other: AbstractMeasure):
        if not isinstance(other, type(self)):
            raise TypeError(_msg('>', self, other))
        return self._value > other._value

    def __le__(self, other: AbstractMeasure):
        if not isinstance(other, type(self)):
            raise TypeError(_msg('<=', self, other))
        return self._value <= other._value

    def __ge__(self, other: AbstractMeasure):
        if not isinstance(other, type(self)):
            raise TypeError(_msg('>=', self, other))
        return self._value >= other._value


def _msg(operator, first, second):
    def _name(instance):
        return type(instance).__name__
    return (
        f'unsupported operand type(s) for {operator}: '
        f"'{_name(first)}' and '{_name(second)}'"
    )

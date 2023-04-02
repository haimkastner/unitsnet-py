from enum import Enum
import math
import string


class ElectricCurrentGradientUnits(Enum):
        """
            ElectricCurrentGradientUnits enumeration
        """
        
        AmperePerSecond = 'ampere_per_second'
        """
            
        """
        
        AmperePerMillisecond = 'ampere_per_millisecond'
        """
            
        """
        
        AmperePerMicrosecond = 'ampere_per_microsecond'
        """
            
        """
        
        AmperePerNanosecond = 'ampere_per_nanosecond'
        """
            
        """
        

class ElectricCurrentGradient:
    """
    In electromagnetism, the current gradient describes how the current changes in time.

    Args:
        value (float): The value.
        from_unit (ElectricCurrentGradientUnits): The ElectricCurrentGradient unit to create from, The default unit is AmperePerSecond
    """
    def __init__(self, value: float, from_unit: ElectricCurrentGradientUnits = ElectricCurrentGradientUnits.AmperePerSecond):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__amperes_per_second = None
        
        self.__amperes_per_millisecond = None
        
        self.__amperes_per_microsecond = None
        
        self.__amperes_per_nanosecond = None
        

    def __convert_from_base(self, from_unit: ElectricCurrentGradientUnits) -> float:
        value = self.__value
        
        if from_unit == ElectricCurrentGradientUnits.AmperePerSecond:
            return (value)
        
        if from_unit == ElectricCurrentGradientUnits.AmperePerMillisecond:
            return (value / 1e3)
        
        if from_unit == ElectricCurrentGradientUnits.AmperePerMicrosecond:
            return (value / 1e6)
        
        if from_unit == ElectricCurrentGradientUnits.AmperePerNanosecond:
            return (value / 1e9)
        
        return None


    def __convert_to_base(self, value: float, to_unit: ElectricCurrentGradientUnits) -> float:
        
        if to_unit == ElectricCurrentGradientUnits.AmperePerSecond:
            return (value)
        
        if to_unit == ElectricCurrentGradientUnits.AmperePerMillisecond:
            return (value * 1e3)
        
        if to_unit == ElectricCurrentGradientUnits.AmperePerMicrosecond:
            return (value * 1e6)
        
        if to_unit == ElectricCurrentGradientUnits.AmperePerNanosecond:
            return (value * 1e9)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
    @staticmethod
    def from_amperes_per_second(amperes_per_second: float):
        """
        Create a new instance of ElectricCurrentGradient from a value in amperes_per_second.

        

        :param meters: The ElectricCurrentGradient value in amperes_per_second.
        :type amperes_per_second: float
        :return: A new instance of ElectricCurrentGradient.
        :rtype: ElectricCurrentGradient
        """
        return ElectricCurrentGradient(amperes_per_second, ElectricCurrentGradientUnits.AmperePerSecond)

    
    @staticmethod
    def from_amperes_per_millisecond(amperes_per_millisecond: float):
        """
        Create a new instance of ElectricCurrentGradient from a value in amperes_per_millisecond.

        

        :param meters: The ElectricCurrentGradient value in amperes_per_millisecond.
        :type amperes_per_millisecond: float
        :return: A new instance of ElectricCurrentGradient.
        :rtype: ElectricCurrentGradient
        """
        return ElectricCurrentGradient(amperes_per_millisecond, ElectricCurrentGradientUnits.AmperePerMillisecond)

    
    @staticmethod
    def from_amperes_per_microsecond(amperes_per_microsecond: float):
        """
        Create a new instance of ElectricCurrentGradient from a value in amperes_per_microsecond.

        

        :param meters: The ElectricCurrentGradient value in amperes_per_microsecond.
        :type amperes_per_microsecond: float
        :return: A new instance of ElectricCurrentGradient.
        :rtype: ElectricCurrentGradient
        """
        return ElectricCurrentGradient(amperes_per_microsecond, ElectricCurrentGradientUnits.AmperePerMicrosecond)

    
    @staticmethod
    def from_amperes_per_nanosecond(amperes_per_nanosecond: float):
        """
        Create a new instance of ElectricCurrentGradient from a value in amperes_per_nanosecond.

        

        :param meters: The ElectricCurrentGradient value in amperes_per_nanosecond.
        :type amperes_per_nanosecond: float
        :return: A new instance of ElectricCurrentGradient.
        :rtype: ElectricCurrentGradient
        """
        return ElectricCurrentGradient(amperes_per_nanosecond, ElectricCurrentGradientUnits.AmperePerNanosecond)

    
    @property
    def amperes_per_second(self) -> float:
        """
        
        """
        if self.__amperes_per_second != None:
            return self.__amperes_per_second
        self.__amperes_per_second = self.__convert_from_base(ElectricCurrentGradientUnits.AmperePerSecond)
        return self.__amperes_per_second

    
    @property
    def amperes_per_millisecond(self) -> float:
        """
        
        """
        if self.__amperes_per_millisecond != None:
            return self.__amperes_per_millisecond
        self.__amperes_per_millisecond = self.__convert_from_base(ElectricCurrentGradientUnits.AmperePerMillisecond)
        return self.__amperes_per_millisecond

    
    @property
    def amperes_per_microsecond(self) -> float:
        """
        
        """
        if self.__amperes_per_microsecond != None:
            return self.__amperes_per_microsecond
        self.__amperes_per_microsecond = self.__convert_from_base(ElectricCurrentGradientUnits.AmperePerMicrosecond)
        return self.__amperes_per_microsecond

    
    @property
    def amperes_per_nanosecond(self) -> float:
        """
        
        """
        if self.__amperes_per_nanosecond != None:
            return self.__amperes_per_nanosecond
        self.__amperes_per_nanosecond = self.__convert_from_base(ElectricCurrentGradientUnits.AmperePerNanosecond)
        return self.__amperes_per_nanosecond

    
    def to_string(self, unit: ElectricCurrentGradientUnits = ElectricCurrentGradientUnits.AmperePerSecond) -> string:
        """
        Format the ElectricCurrentGradient to string.
        Note! the default format for ElectricCurrentGradient is AmperePerSecond.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == ElectricCurrentGradientUnits.AmperePerSecond:
            return f"""{self.amperes_per_second} A/s"""
        
        if unit == ElectricCurrentGradientUnits.AmperePerMillisecond:
            return f"""{self.amperes_per_millisecond} A/ms"""
        
        if unit == ElectricCurrentGradientUnits.AmperePerMicrosecond:
            return f"""{self.amperes_per_microsecond} A/μs"""
        
        if unit == ElectricCurrentGradientUnits.AmperePerNanosecond:
            return f"""{self.amperes_per_nanosecond} A/ns"""
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: ElectricCurrentGradientUnits = ElectricCurrentGradientUnits.AmperePerSecond) -> string:
        """
        Get ElectricCurrentGradient unit abbreviation.
        Note! the default abbreviation for ElectricCurrentGradient is AmperePerSecond.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == ElectricCurrentGradientUnits.AmperePerSecond:
            return """A/s"""
        
        if unit_abbreviation == ElectricCurrentGradientUnits.AmperePerMillisecond:
            return """A/ms"""
        
        if unit_abbreviation == ElectricCurrentGradientUnits.AmperePerMicrosecond:
            return """A/μs"""
        
        if unit_abbreviation == ElectricCurrentGradientUnits.AmperePerNanosecond:
            return """A/ns"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, ElectricCurrentGradient):
            raise TypeError("unsupported operand type(s) for +: 'ElectricCurrentGradient' and '{}'".format(type(other).__name__))
        return ElectricCurrentGradient(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, ElectricCurrentGradient):
            raise TypeError("unsupported operand type(s) for *: 'ElectricCurrentGradient' and '{}'".format(type(other).__name__))
        return ElectricCurrentGradient(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, ElectricCurrentGradient):
            raise TypeError("unsupported operand type(s) for -: 'ElectricCurrentGradient' and '{}'".format(type(other).__name__))
        return ElectricCurrentGradient(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, ElectricCurrentGradient):
            raise TypeError("unsupported operand type(s) for /: 'ElectricCurrentGradient' and '{}'".format(type(other).__name__))
        return ElectricCurrentGradient(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, ElectricCurrentGradient):
            raise TypeError("unsupported operand type(s) for %: 'ElectricCurrentGradient' and '{}'".format(type(other).__name__))
        return ElectricCurrentGradient(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, ElectricCurrentGradient):
            raise TypeError("unsupported operand type(s) for **: 'ElectricCurrentGradient' and '{}'".format(type(other).__name__))
        return ElectricCurrentGradient(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, ElectricCurrentGradient):
            raise TypeError("unsupported operand type(s) for ==: 'ElectricCurrentGradient' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, ElectricCurrentGradient):
            raise TypeError("unsupported operand type(s) for <: 'ElectricCurrentGradient' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, ElectricCurrentGradient):
            raise TypeError("unsupported operand type(s) for >: 'ElectricCurrentGradient' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, ElectricCurrentGradient):
            raise TypeError("unsupported operand type(s) for <=: 'ElectricCurrentGradient' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, ElectricCurrentGradient):
            raise TypeError("unsupported operand type(s) for >=: 'ElectricCurrentGradient' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value
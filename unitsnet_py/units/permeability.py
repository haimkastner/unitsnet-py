from enum import Enum
import math
import string


class PermeabilityUnits(Enum):
        """
            PermeabilityUnits enumeration
        """
        
        HenryPerMeter = 'henry_per_meter'
        """
            
        """
        

class Permeability:
    """
    In electromagnetism, permeability is the measure of the ability of a material to support the formation of a magnetic field within itself.

    Args:
        value (float): The value.
        from_unit (PermeabilityUnits): The Permeability unit to create from, The default unit is HenryPerMeter
    """
    def __init__(self, value: float, from_unit: PermeabilityUnits = PermeabilityUnits.HenryPerMeter):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__henries_per_meter = None
        

    def __convert_from_base(self, from_unit: PermeabilityUnits) -> float:
        value = self.__value
        
        if from_unit == PermeabilityUnits.HenryPerMeter:
            return (value)
        
        return None


    def __convert_to_base(self, value: float, to_unit: PermeabilityUnits) -> float:
        
        if to_unit == PermeabilityUnits.HenryPerMeter:
            return (value)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
    @staticmethod
    def from_henries_per_meter(henries_per_meter: float):
        """
        Create a new instance of Permeability from a value in henries_per_meter.

        

        :param meters: The Permeability value in henries_per_meter.
        :type henries_per_meter: float
        :return: A new instance of Permeability.
        :rtype: Permeability
        """
        return Permeability(henries_per_meter, PermeabilityUnits.HenryPerMeter)

    
    @property
    def henries_per_meter(self) -> float:
        """
        
        """
        if self.__henries_per_meter != None:
            return self.__henries_per_meter
        self.__henries_per_meter = self.__convert_from_base(PermeabilityUnits.HenryPerMeter)
        return self.__henries_per_meter

    
    def to_string(self, unit: PermeabilityUnits = PermeabilityUnits.HenryPerMeter) -> string:
        """
        Format the Permeability to string.
        Note! the default format for Permeability is HenryPerMeter.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == PermeabilityUnits.HenryPerMeter:
            return f"""{self.henries_per_meter} H/m"""
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: PermeabilityUnits = PermeabilityUnits.HenryPerMeter) -> string:
        """
        Get Permeability unit abbreviation.
        Note! the default abbreviation for Permeability is HenryPerMeter.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == PermeabilityUnits.HenryPerMeter:
            return """H/m"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, Permeability):
            raise TypeError("unsupported operand type(s) for +: 'Permeability' and '{}'".format(type(other).__name__))
        return Permeability(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, Permeability):
            raise TypeError("unsupported operand type(s) for *: 'Permeability' and '{}'".format(type(other).__name__))
        return Permeability(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, Permeability):
            raise TypeError("unsupported operand type(s) for -: 'Permeability' and '{}'".format(type(other).__name__))
        return Permeability(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, Permeability):
            raise TypeError("unsupported operand type(s) for /: 'Permeability' and '{}'".format(type(other).__name__))
        return Permeability(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, Permeability):
            raise TypeError("unsupported operand type(s) for %: 'Permeability' and '{}'".format(type(other).__name__))
        return Permeability(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, Permeability):
            raise TypeError("unsupported operand type(s) for **: 'Permeability' and '{}'".format(type(other).__name__))
        return Permeability(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, Permeability):
            raise TypeError("unsupported operand type(s) for ==: 'Permeability' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, Permeability):
            raise TypeError("unsupported operand type(s) for <: 'Permeability' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, Permeability):
            raise TypeError("unsupported operand type(s) for >: 'Permeability' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, Permeability):
            raise TypeError("unsupported operand type(s) for <=: 'Permeability' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, Permeability):
            raise TypeError("unsupported operand type(s) for >=: 'Permeability' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value
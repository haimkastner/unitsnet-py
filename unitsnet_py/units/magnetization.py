from enum import Enum
import math
import string


class MagnetizationUnits(Enum):
        """
            MagnetizationUnits enumeration
        """
        
        AmperePerMeter = 'ampere_per_meter'
        """
            
        """
        

class Magnetization:
    """
    In classical electromagnetism, magnetization is the vector field that expresses the density of permanent or induced magnetic dipole moments in a magnetic material.

    Args:
        value (float): The value.
        from_unit (MagnetizationUnits): The Magnetization unit to create from, The default unit is AmperePerMeter
    """
    def __init__(self, value: float, from_unit: MagnetizationUnits = MagnetizationUnits.AmperePerMeter):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__amperes_per_meter = None
        

    def __convert_from_base(self, from_unit: MagnetizationUnits) -> float:
        value = self.__value
        
        if from_unit == MagnetizationUnits.AmperePerMeter:
            return (value)
        
        return None


    def __convert_to_base(self, value: float, to_unit: MagnetizationUnits) -> float:
        
        if to_unit == MagnetizationUnits.AmperePerMeter:
            return (value)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
    @staticmethod
    def from_amperes_per_meter(amperes_per_meter: float):
        """
        Create a new instance of Magnetization from a value in amperes_per_meter.

        

        :param meters: The Magnetization value in amperes_per_meter.
        :type amperes_per_meter: float
        :return: A new instance of Magnetization.
        :rtype: Magnetization
        """
        return Magnetization(amperes_per_meter, MagnetizationUnits.AmperePerMeter)

    
    @property
    def amperes_per_meter(self) -> float:
        """
        
        """
        if self.__amperes_per_meter != None:
            return self.__amperes_per_meter
        self.__amperes_per_meter = self.__convert_from_base(MagnetizationUnits.AmperePerMeter)
        return self.__amperes_per_meter

    
    def to_string(self, unit: MagnetizationUnits = MagnetizationUnits.AmperePerMeter) -> string:
        """
        Format the Magnetization to string.
        Note! the default format for Magnetization is AmperePerMeter.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == MagnetizationUnits.AmperePerMeter:
            return f"""{self.amperes_per_meter} A/m"""
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: MagnetizationUnits = MagnetizationUnits.AmperePerMeter) -> string:
        """
        Get Magnetization unit abbreviation.
        Note! the default abbreviation for Magnetization is AmperePerMeter.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == MagnetizationUnits.AmperePerMeter:
            return """A/m"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, Magnetization):
            raise TypeError("unsupported operand type(s) for +: 'Magnetization' and '{}'".format(type(other).__name__))
        return Magnetization(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, Magnetization):
            raise TypeError("unsupported operand type(s) for *: 'Magnetization' and '{}'".format(type(other).__name__))
        return Magnetization(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, Magnetization):
            raise TypeError("unsupported operand type(s) for -: 'Magnetization' and '{}'".format(type(other).__name__))
        return Magnetization(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, Magnetization):
            raise TypeError("unsupported operand type(s) for /: 'Magnetization' and '{}'".format(type(other).__name__))
        return Magnetization(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, Magnetization):
            raise TypeError("unsupported operand type(s) for %: 'Magnetization' and '{}'".format(type(other).__name__))
        return Magnetization(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, Magnetization):
            raise TypeError("unsupported operand type(s) for **: 'Magnetization' and '{}'".format(type(other).__name__))
        return Magnetization(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, Magnetization):
            raise TypeError("unsupported operand type(s) for ==: 'Magnetization' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, Magnetization):
            raise TypeError("unsupported operand type(s) for <: 'Magnetization' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, Magnetization):
            raise TypeError("unsupported operand type(s) for >: 'Magnetization' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, Magnetization):
            raise TypeError("unsupported operand type(s) for <=: 'Magnetization' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, Magnetization):
            raise TypeError("unsupported operand type(s) for >=: 'Magnetization' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value
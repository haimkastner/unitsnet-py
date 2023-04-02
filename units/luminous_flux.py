from enum import Enum
import math
import string


class LuminousFluxUnits(Enum):
        """
            LuminousFluxUnits enumeration
        """
        
        Lumen = 'lumen'
        """
            
        """
        

class LuminousFlux:
    """
    In photometry, luminous flux or luminous power is the measure of the perceived power of light.

    Args:
        value (float): The value.
        from_unit (LuminousFluxUnits): The LuminousFlux unit to create from, The default unit is Lumen
    """
    def __init__(self, value: float, from_unit: LuminousFluxUnits = LuminousFluxUnits.Lumen):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__lumens = None
        

    def __convert_from_base(self, from_unit: LuminousFluxUnits) -> float:
        value = self.__value
        
        if from_unit == LuminousFluxUnits.Lumen:
            return (value)
        
        return None


    def __convert_to_base(self, value: float, to_unit: LuminousFluxUnits) -> float:
        
        if to_unit == LuminousFluxUnits.Lumen:
            return (value)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
    @staticmethod
    def from_lumens(lumens: float):
        """
        Create a new instance of LuminousFlux from a value in lumens.

        

        :param meters: The LuminousFlux value in lumens.
        :type lumens: float
        :return: A new instance of LuminousFlux.
        :rtype: LuminousFlux
        """
        return LuminousFlux(lumens, LuminousFluxUnits.Lumen)

    
    @property
    def lumens(self) -> float:
        """
        
        """
        if self.__lumens != None:
            return self.__lumens
        self.__lumens = self.__convert_from_base(LuminousFluxUnits.Lumen)
        return self.__lumens

    
    def to_string(self, unit: LuminousFluxUnits = LuminousFluxUnits.Lumen) -> string:
        """
        Format the LuminousFlux to string.
        Note! the default format for LuminousFlux is Lumen.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == LuminousFluxUnits.Lumen:
            return f"""{self.lumens} lm"""
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: LuminousFluxUnits = LuminousFluxUnits.Lumen) -> string:
        """
        Get LuminousFlux unit abbreviation.
        Note! the default abbreviation for LuminousFlux is Lumen.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == LuminousFluxUnits.Lumen:
            return """lm"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, LuminousFlux):
            raise TypeError("unsupported operand type(s) for +: 'LuminousFlux' and '{}'".format(type(other).__name__))
        return LuminousFlux(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, LuminousFlux):
            raise TypeError("unsupported operand type(s) for *: 'LuminousFlux' and '{}'".format(type(other).__name__))
        return LuminousFlux(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, LuminousFlux):
            raise TypeError("unsupported operand type(s) for -: 'LuminousFlux' and '{}'".format(type(other).__name__))
        return LuminousFlux(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, LuminousFlux):
            raise TypeError("unsupported operand type(s) for /: 'LuminousFlux' and '{}'".format(type(other).__name__))
        return LuminousFlux(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, LuminousFlux):
            raise TypeError("unsupported operand type(s) for %: 'LuminousFlux' and '{}'".format(type(other).__name__))
        return LuminousFlux(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, LuminousFlux):
            raise TypeError("unsupported operand type(s) for **: 'LuminousFlux' and '{}'".format(type(other).__name__))
        return LuminousFlux(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, LuminousFlux):
            raise TypeError("unsupported operand type(s) for ==: 'LuminousFlux' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, LuminousFlux):
            raise TypeError("unsupported operand type(s) for <: 'LuminousFlux' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, LuminousFlux):
            raise TypeError("unsupported operand type(s) for >: 'LuminousFlux' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, LuminousFlux):
            raise TypeError("unsupported operand type(s) for <=: 'LuminousFlux' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, LuminousFlux):
            raise TypeError("unsupported operand type(s) for >=: 'LuminousFlux' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value
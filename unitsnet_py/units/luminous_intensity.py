from enum import Enum
import math
import string


class LuminousIntensityUnits(Enum):
        """
            LuminousIntensityUnits enumeration
        """
        
        Candela = 'candela'
        """
            
        """
        

class LuminousIntensity:
    """
    In photometry, luminous intensity is a measure of the wavelength-weighted power emitted by a light source in a particular direction per unit solid angle, based on the luminosity function, a standardized model of the sensitivity of the human eye.

    Args:
        value (float): The value.
        from_unit (LuminousIntensityUnits): The LuminousIntensity unit to create from, The default unit is Candela
    """
    def __init__(self, value: float, from_unit: LuminousIntensityUnits = LuminousIntensityUnits.Candela):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__candela = None
        

    def __convert_from_base(self, from_unit: LuminousIntensityUnits) -> float:
        value = self.__value
        
        if from_unit == LuminousIntensityUnits.Candela:
            return (value)
        
        return None


    def __convert_to_base(self, value: float, to_unit: LuminousIntensityUnits) -> float:
        
        if to_unit == LuminousIntensityUnits.Candela:
            return (value)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
    @staticmethod
    def from_candela(candela: float):
        """
        Create a new instance of LuminousIntensity from a value in candela.

        

        :param meters: The LuminousIntensity value in candela.
        :type candela: float
        :return: A new instance of LuminousIntensity.
        :rtype: LuminousIntensity
        """
        return LuminousIntensity(candela, LuminousIntensityUnits.Candela)

    
    @property
    def candela(self) -> float:
        """
        
        """
        if self.__candela != None:
            return self.__candela
        self.__candela = self.__convert_from_base(LuminousIntensityUnits.Candela)
        return self.__candela

    
    def to_string(self, unit: LuminousIntensityUnits = LuminousIntensityUnits.Candela) -> string:
        """
        Format the LuminousIntensity to string.
        Note! the default format for LuminousIntensity is Candela.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == LuminousIntensityUnits.Candela:
            return f"""{self.candela} cd"""
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: LuminousIntensityUnits = LuminousIntensityUnits.Candela) -> string:
        """
        Get LuminousIntensity unit abbreviation.
        Note! the default abbreviation for LuminousIntensity is Candela.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == LuminousIntensityUnits.Candela:
            return """cd"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, LuminousIntensity):
            raise TypeError("unsupported operand type(s) for +: 'LuminousIntensity' and '{}'".format(type(other).__name__))
        return LuminousIntensity(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, LuminousIntensity):
            raise TypeError("unsupported operand type(s) for *: 'LuminousIntensity' and '{}'".format(type(other).__name__))
        return LuminousIntensity(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, LuminousIntensity):
            raise TypeError("unsupported operand type(s) for -: 'LuminousIntensity' and '{}'".format(type(other).__name__))
        return LuminousIntensity(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, LuminousIntensity):
            raise TypeError("unsupported operand type(s) for /: 'LuminousIntensity' and '{}'".format(type(other).__name__))
        return LuminousIntensity(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, LuminousIntensity):
            raise TypeError("unsupported operand type(s) for %: 'LuminousIntensity' and '{}'".format(type(other).__name__))
        return LuminousIntensity(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, LuminousIntensity):
            raise TypeError("unsupported operand type(s) for **: 'LuminousIntensity' and '{}'".format(type(other).__name__))
        return LuminousIntensity(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, LuminousIntensity):
            raise TypeError("unsupported operand type(s) for ==: 'LuminousIntensity' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, LuminousIntensity):
            raise TypeError("unsupported operand type(s) for <: 'LuminousIntensity' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, LuminousIntensity):
            raise TypeError("unsupported operand type(s) for >: 'LuminousIntensity' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, LuminousIntensity):
            raise TypeError("unsupported operand type(s) for <=: 'LuminousIntensity' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, LuminousIntensity):
            raise TypeError("unsupported operand type(s) for >=: 'LuminousIntensity' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value
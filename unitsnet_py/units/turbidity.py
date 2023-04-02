from enum import Enum
import math
import string


class TurbidityUnits(Enum):
        """
            TurbidityUnits enumeration
        """
        
        NTU = 'ntu'
        """
            
        """
        

class Turbidity:
    """
    Turbidity is the cloudiness or haziness of a fluid caused by large numbers of individual particles that are generally invisible to the naked eye, similar to smoke in air. The measurement of turbidity is a key test of water quality.

    Args:
        value (float): The value.
        from_unit (TurbidityUnits): The Turbidity unit to create from, The default unit is NTU
    """
    def __init__(self, value: float, from_unit: TurbidityUnits = TurbidityUnits.NTU):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__ntu = None
        

    def __convert_from_base(self, from_unit: TurbidityUnits) -> float:
        value = self.__value
        
        if from_unit == TurbidityUnits.NTU:
            return (value)
        
        return None


    def __convert_to_base(self, value: float, to_unit: TurbidityUnits) -> float:
        
        if to_unit == TurbidityUnits.NTU:
            return (value)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
    @staticmethod
    def from_ntu(ntu: float):
        """
        Create a new instance of Turbidity from a value in ntu.

        

        :param meters: The Turbidity value in ntu.
        :type ntu: float
        :return: A new instance of Turbidity.
        :rtype: Turbidity
        """
        return Turbidity(ntu, TurbidityUnits.NTU)

    
    @property
    def ntu(self) -> float:
        """
        
        """
        if self.__ntu != None:
            return self.__ntu
        self.__ntu = self.__convert_from_base(TurbidityUnits.NTU)
        return self.__ntu

    
    def to_string(self, unit: TurbidityUnits = TurbidityUnits.NTU) -> string:
        """
        Format the Turbidity to string.
        Note! the default format for Turbidity is NTU.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == TurbidityUnits.NTU:
            return f"""{self.ntu} NTU"""
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: TurbidityUnits = TurbidityUnits.NTU) -> string:
        """
        Get Turbidity unit abbreviation.
        Note! the default abbreviation for Turbidity is NTU.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == TurbidityUnits.NTU:
            return """NTU"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, Turbidity):
            raise TypeError("unsupported operand type(s) for +: 'Turbidity' and '{}'".format(type(other).__name__))
        return Turbidity(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, Turbidity):
            raise TypeError("unsupported operand type(s) for *: 'Turbidity' and '{}'".format(type(other).__name__))
        return Turbidity(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, Turbidity):
            raise TypeError("unsupported operand type(s) for -: 'Turbidity' and '{}'".format(type(other).__name__))
        return Turbidity(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, Turbidity):
            raise TypeError("unsupported operand type(s) for /: 'Turbidity' and '{}'".format(type(other).__name__))
        return Turbidity(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, Turbidity):
            raise TypeError("unsupported operand type(s) for %: 'Turbidity' and '{}'".format(type(other).__name__))
        return Turbidity(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, Turbidity):
            raise TypeError("unsupported operand type(s) for **: 'Turbidity' and '{}'".format(type(other).__name__))
        return Turbidity(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, Turbidity):
            raise TypeError("unsupported operand type(s) for ==: 'Turbidity' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, Turbidity):
            raise TypeError("unsupported operand type(s) for <: 'Turbidity' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, Turbidity):
            raise TypeError("unsupported operand type(s) for >: 'Turbidity' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, Turbidity):
            raise TypeError("unsupported operand type(s) for <=: 'Turbidity' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, Turbidity):
            raise TypeError("unsupported operand type(s) for >=: 'Turbidity' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value
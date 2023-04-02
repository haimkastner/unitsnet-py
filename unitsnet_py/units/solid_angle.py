from enum import Enum
import math
import string


class SolidAngleUnits(Enum):
        """
            SolidAngleUnits enumeration
        """
        
        Steradian = 'steradian'
        """
            
        """
        

class SolidAngle:
    """
    In geometry, a solid angle is the two-dimensional angle in three-dimensional space that an object subtends at a point.

    Args:
        value (float): The value.
        from_unit (SolidAngleUnits): The SolidAngle unit to create from, The default unit is Steradian
    """
    def __init__(self, value: float, from_unit: SolidAngleUnits = SolidAngleUnits.Steradian):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__steradians = None
        

    def __convert_from_base(self, from_unit: SolidAngleUnits) -> float:
        value = self.__value
        
        if from_unit == SolidAngleUnits.Steradian:
            return (value)
        
        return None


    def __convert_to_base(self, value: float, to_unit: SolidAngleUnits) -> float:
        
        if to_unit == SolidAngleUnits.Steradian:
            return (value)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
    @staticmethod
    def from_steradians(steradians: float):
        """
        Create a new instance of SolidAngle from a value in steradians.

        

        :param meters: The SolidAngle value in steradians.
        :type steradians: float
        :return: A new instance of SolidAngle.
        :rtype: SolidAngle
        """
        return SolidAngle(steradians, SolidAngleUnits.Steradian)

    
    @property
    def steradians(self) -> float:
        """
        
        """
        if self.__steradians != None:
            return self.__steradians
        self.__steradians = self.__convert_from_base(SolidAngleUnits.Steradian)
        return self.__steradians

    
    def to_string(self, unit: SolidAngleUnits = SolidAngleUnits.Steradian) -> string:
        """
        Format the SolidAngle to string.
        Note! the default format for SolidAngle is Steradian.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == SolidAngleUnits.Steradian:
            return f"""{self.steradians} sr"""
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: SolidAngleUnits = SolidAngleUnits.Steradian) -> string:
        """
        Get SolidAngle unit abbreviation.
        Note! the default abbreviation for SolidAngle is Steradian.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == SolidAngleUnits.Steradian:
            return """sr"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, SolidAngle):
            raise TypeError("unsupported operand type(s) for +: 'SolidAngle' and '{}'".format(type(other).__name__))
        return SolidAngle(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, SolidAngle):
            raise TypeError("unsupported operand type(s) for *: 'SolidAngle' and '{}'".format(type(other).__name__))
        return SolidAngle(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, SolidAngle):
            raise TypeError("unsupported operand type(s) for -: 'SolidAngle' and '{}'".format(type(other).__name__))
        return SolidAngle(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, SolidAngle):
            raise TypeError("unsupported operand type(s) for /: 'SolidAngle' and '{}'".format(type(other).__name__))
        return SolidAngle(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, SolidAngle):
            raise TypeError("unsupported operand type(s) for %: 'SolidAngle' and '{}'".format(type(other).__name__))
        return SolidAngle(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, SolidAngle):
            raise TypeError("unsupported operand type(s) for **: 'SolidAngle' and '{}'".format(type(other).__name__))
        return SolidAngle(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, SolidAngle):
            raise TypeError("unsupported operand type(s) for ==: 'SolidAngle' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, SolidAngle):
            raise TypeError("unsupported operand type(s) for <: 'SolidAngle' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, SolidAngle):
            raise TypeError("unsupported operand type(s) for >: 'SolidAngle' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, SolidAngle):
            raise TypeError("unsupported operand type(s) for <=: 'SolidAngle' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, SolidAngle):
            raise TypeError("unsupported operand type(s) for >=: 'SolidAngle' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value
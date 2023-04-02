from enum import Enum
import math
import string


class RelativeHumidityUnits(Enum):
        """
            RelativeHumidityUnits enumeration
        """
        
        Percent = 'percent'
        """
            
        """
        

class RelativeHumidity:
    """
    Relative humidity is a ratio of the actual water vapor present in the air to the maximum water vapor in the air at the given temperature.

    Args:
        value (float): The value.
        from_unit (RelativeHumidityUnits): The RelativeHumidity unit to create from, The default unit is Percent
    """
    def __init__(self, value: float, from_unit: RelativeHumidityUnits = RelativeHumidityUnits.Percent):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__percent = None
        

    def __convert_from_base(self, from_unit: RelativeHumidityUnits) -> float:
        value = self.__value
        
        if from_unit == RelativeHumidityUnits.Percent:
            return (value)
        
        return None


    def __convert_to_base(self, value: float, to_unit: RelativeHumidityUnits) -> float:
        
        if to_unit == RelativeHumidityUnits.Percent:
            return (value)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
    @staticmethod
    def from_percent(percent: float):
        """
        Create a new instance of RelativeHumidity from a value in percent.

        

        :param meters: The RelativeHumidity value in percent.
        :type percent: float
        :return: A new instance of RelativeHumidity.
        :rtype: RelativeHumidity
        """
        return RelativeHumidity(percent, RelativeHumidityUnits.Percent)

    
    @property
    def percent(self) -> float:
        """
        
        """
        if self.__percent != None:
            return self.__percent
        self.__percent = self.__convert_from_base(RelativeHumidityUnits.Percent)
        return self.__percent

    
    def to_string(self, unit: RelativeHumidityUnits = RelativeHumidityUnits.Percent) -> string:
        """
        Format the RelativeHumidity to string.
        Note! the default format for RelativeHumidity is Percent.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == RelativeHumidityUnits.Percent:
            return f"""{self.percent} %RH"""
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: RelativeHumidityUnits = RelativeHumidityUnits.Percent) -> string:
        """
        Get RelativeHumidity unit abbreviation.
        Note! the default abbreviation for RelativeHumidity is Percent.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == RelativeHumidityUnits.Percent:
            return """%RH"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, RelativeHumidity):
            raise TypeError("unsupported operand type(s) for +: 'RelativeHumidity' and '{}'".format(type(other).__name__))
        return RelativeHumidity(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, RelativeHumidity):
            raise TypeError("unsupported operand type(s) for *: 'RelativeHumidity' and '{}'".format(type(other).__name__))
        return RelativeHumidity(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, RelativeHumidity):
            raise TypeError("unsupported operand type(s) for -: 'RelativeHumidity' and '{}'".format(type(other).__name__))
        return RelativeHumidity(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, RelativeHumidity):
            raise TypeError("unsupported operand type(s) for /: 'RelativeHumidity' and '{}'".format(type(other).__name__))
        return RelativeHumidity(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, RelativeHumidity):
            raise TypeError("unsupported operand type(s) for %: 'RelativeHumidity' and '{}'".format(type(other).__name__))
        return RelativeHumidity(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, RelativeHumidity):
            raise TypeError("unsupported operand type(s) for **: 'RelativeHumidity' and '{}'".format(type(other).__name__))
        return RelativeHumidity(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, RelativeHumidity):
            raise TypeError("unsupported operand type(s) for ==: 'RelativeHumidity' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, RelativeHumidity):
            raise TypeError("unsupported operand type(s) for <: 'RelativeHumidity' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, RelativeHumidity):
            raise TypeError("unsupported operand type(s) for >: 'RelativeHumidity' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, RelativeHumidity):
            raise TypeError("unsupported operand type(s) for <=: 'RelativeHumidity' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, RelativeHumidity):
            raise TypeError("unsupported operand type(s) for >=: 'RelativeHumidity' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value
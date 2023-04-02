from enum import Enum
import math
import string


class RatioChangeRateUnits(Enum):
        """
            RatioChangeRateUnits enumeration
        """
        
        PercentPerSecond = 'percent_per_second'
        """
            
        """
        
        DecimalFractionPerSecond = 'decimal_fraction_per_second'
        """
            
        """
        

class RatioChangeRate:
    """
    The change in ratio per unit of time.

    Args:
        value (float): The value.
        from_unit (RatioChangeRateUnits): The RatioChangeRate unit to create from, The default unit is DecimalFractionPerSecond
    """
    def __init__(self, value: float, from_unit: RatioChangeRateUnits = RatioChangeRateUnits.DecimalFractionPerSecond):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__percents_per_second = None
        
        self.__decimal_fractions_per_second = None
        

    def __convert_from_base(self, from_unit: RatioChangeRateUnits) -> float:
        value = self.__value
        
        if from_unit == RatioChangeRateUnits.PercentPerSecond:
            return (value * 1e2)
        
        if from_unit == RatioChangeRateUnits.DecimalFractionPerSecond:
            return (value)
        
        return None


    def __convert_to_base(self, value: float, to_unit: RatioChangeRateUnits) -> float:
        
        if to_unit == RatioChangeRateUnits.PercentPerSecond:
            return (value / 1e2)
        
        if to_unit == RatioChangeRateUnits.DecimalFractionPerSecond:
            return (value)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
    @staticmethod
    def from_percents_per_second(percents_per_second: float):
        """
        Create a new instance of RatioChangeRate from a value in percents_per_second.

        

        :param meters: The RatioChangeRate value in percents_per_second.
        :type percents_per_second: float
        :return: A new instance of RatioChangeRate.
        :rtype: RatioChangeRate
        """
        return RatioChangeRate(percents_per_second, RatioChangeRateUnits.PercentPerSecond)

    
    @staticmethod
    def from_decimal_fractions_per_second(decimal_fractions_per_second: float):
        """
        Create a new instance of RatioChangeRate from a value in decimal_fractions_per_second.

        

        :param meters: The RatioChangeRate value in decimal_fractions_per_second.
        :type decimal_fractions_per_second: float
        :return: A new instance of RatioChangeRate.
        :rtype: RatioChangeRate
        """
        return RatioChangeRate(decimal_fractions_per_second, RatioChangeRateUnits.DecimalFractionPerSecond)

    
    @property
    def percents_per_second(self) -> float:
        """
        
        """
        if self.__percents_per_second != None:
            return self.__percents_per_second
        self.__percents_per_second = self.__convert_from_base(RatioChangeRateUnits.PercentPerSecond)
        return self.__percents_per_second

    
    @property
    def decimal_fractions_per_second(self) -> float:
        """
        
        """
        if self.__decimal_fractions_per_second != None:
            return self.__decimal_fractions_per_second
        self.__decimal_fractions_per_second = self.__convert_from_base(RatioChangeRateUnits.DecimalFractionPerSecond)
        return self.__decimal_fractions_per_second

    
    def to_string(self, unit: RatioChangeRateUnits = RatioChangeRateUnits.DecimalFractionPerSecond) -> string:
        """
        Format the RatioChangeRate to string.
        Note! the default format for RatioChangeRate is DecimalFractionPerSecond.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == RatioChangeRateUnits.PercentPerSecond:
            return f"""{self.percents_per_second} %/s"""
        
        if unit == RatioChangeRateUnits.DecimalFractionPerSecond:
            return f"""{self.decimal_fractions_per_second} /s"""
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: RatioChangeRateUnits = RatioChangeRateUnits.DecimalFractionPerSecond) -> string:
        """
        Get RatioChangeRate unit abbreviation.
        Note! the default abbreviation for RatioChangeRate is DecimalFractionPerSecond.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == RatioChangeRateUnits.PercentPerSecond:
            return """%/s"""
        
        if unit_abbreviation == RatioChangeRateUnits.DecimalFractionPerSecond:
            return """/s"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, RatioChangeRate):
            raise TypeError("unsupported operand type(s) for +: 'RatioChangeRate' and '{}'".format(type(other).__name__))
        return RatioChangeRate(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, RatioChangeRate):
            raise TypeError("unsupported operand type(s) for *: 'RatioChangeRate' and '{}'".format(type(other).__name__))
        return RatioChangeRate(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, RatioChangeRate):
            raise TypeError("unsupported operand type(s) for -: 'RatioChangeRate' and '{}'".format(type(other).__name__))
        return RatioChangeRate(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, RatioChangeRate):
            raise TypeError("unsupported operand type(s) for /: 'RatioChangeRate' and '{}'".format(type(other).__name__))
        return RatioChangeRate(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, RatioChangeRate):
            raise TypeError("unsupported operand type(s) for %: 'RatioChangeRate' and '{}'".format(type(other).__name__))
        return RatioChangeRate(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, RatioChangeRate):
            raise TypeError("unsupported operand type(s) for **: 'RatioChangeRate' and '{}'".format(type(other).__name__))
        return RatioChangeRate(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, RatioChangeRate):
            raise TypeError("unsupported operand type(s) for ==: 'RatioChangeRate' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, RatioChangeRate):
            raise TypeError("unsupported operand type(s) for <: 'RatioChangeRate' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, RatioChangeRate):
            raise TypeError("unsupported operand type(s) for >: 'RatioChangeRate' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, RatioChangeRate):
            raise TypeError("unsupported operand type(s) for <=: 'RatioChangeRate' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, RatioChangeRate):
            raise TypeError("unsupported operand type(s) for >=: 'RatioChangeRate' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value
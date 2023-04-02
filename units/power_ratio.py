from enum import Enum
import math
import string


class PowerRatioUnits(Enum):
        """
            PowerRatioUnits enumeration
        """
        
        DecibelWatt = 'decibel_watt'
        """
            
        """
        
        DecibelMilliwatt = 'decibel_milliwatt'
        """
            
        """
        

class PowerRatio:
    """
    The strength of a signal expressed in decibels (dB) relative to one watt.

    Args:
        value (float): The value.
        from_unit (PowerRatioUnits): The PowerRatio unit to create from, The default unit is DecibelWatt
    """
    def __init__(self, value: float, from_unit: PowerRatioUnits = PowerRatioUnits.DecibelWatt):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__decibel_watts = None
        
        self.__decibel_milliwatts = None
        

    def __convert_from_base(self, from_unit: PowerRatioUnits) -> float:
        value = self.__value
        
        if from_unit == PowerRatioUnits.DecibelWatt:
            return (value)
        
        if from_unit == PowerRatioUnits.DecibelMilliwatt:
            return (value + 30)
        
        return None


    def __convert_to_base(self, value: float, to_unit: PowerRatioUnits) -> float:
        
        if to_unit == PowerRatioUnits.DecibelWatt:
            return (value)
        
        if to_unit == PowerRatioUnits.DecibelMilliwatt:
            return (value - 30)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
    @staticmethod
    def from_decibel_watts(decibel_watts: float):
        """
        Create a new instance of PowerRatio from a value in decibel_watts.

        

        :param meters: The PowerRatio value in decibel_watts.
        :type decibel_watts: float
        :return: A new instance of PowerRatio.
        :rtype: PowerRatio
        """
        return PowerRatio(decibel_watts, PowerRatioUnits.DecibelWatt)

    
    @staticmethod
    def from_decibel_milliwatts(decibel_milliwatts: float):
        """
        Create a new instance of PowerRatio from a value in decibel_milliwatts.

        

        :param meters: The PowerRatio value in decibel_milliwatts.
        :type decibel_milliwatts: float
        :return: A new instance of PowerRatio.
        :rtype: PowerRatio
        """
        return PowerRatio(decibel_milliwatts, PowerRatioUnits.DecibelMilliwatt)

    
    @property
    def decibel_watts(self) -> float:
        """
        
        """
        if self.__decibel_watts != None:
            return self.__decibel_watts
        self.__decibel_watts = self.__convert_from_base(PowerRatioUnits.DecibelWatt)
        return self.__decibel_watts

    
    @property
    def decibel_milliwatts(self) -> float:
        """
        
        """
        if self.__decibel_milliwatts != None:
            return self.__decibel_milliwatts
        self.__decibel_milliwatts = self.__convert_from_base(PowerRatioUnits.DecibelMilliwatt)
        return self.__decibel_milliwatts

    
    def to_string(self, unit: PowerRatioUnits = PowerRatioUnits.DecibelWatt) -> string:
        """
        Format the PowerRatio to string.
        Note! the default format for PowerRatio is DecibelWatt.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == PowerRatioUnits.DecibelWatt:
            return f"""{self.decibel_watts} dBW"""
        
        if unit == PowerRatioUnits.DecibelMilliwatt:
            return f"""{self.decibel_milliwatts} dBmW"""
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: PowerRatioUnits = PowerRatioUnits.DecibelWatt) -> string:
        """
        Get PowerRatio unit abbreviation.
        Note! the default abbreviation for PowerRatio is DecibelWatt.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == PowerRatioUnits.DecibelWatt:
            return """dBW"""
        
        if unit_abbreviation == PowerRatioUnits.DecibelMilliwatt:
            return """dBmW"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, PowerRatio):
            raise TypeError("unsupported operand type(s) for +: 'PowerRatio' and '{}'".format(type(other).__name__))
        return PowerRatio(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, PowerRatio):
            raise TypeError("unsupported operand type(s) for *: 'PowerRatio' and '{}'".format(type(other).__name__))
        return PowerRatio(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, PowerRatio):
            raise TypeError("unsupported operand type(s) for -: 'PowerRatio' and '{}'".format(type(other).__name__))
        return PowerRatio(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, PowerRatio):
            raise TypeError("unsupported operand type(s) for /: 'PowerRatio' and '{}'".format(type(other).__name__))
        return PowerRatio(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, PowerRatio):
            raise TypeError("unsupported operand type(s) for %: 'PowerRatio' and '{}'".format(type(other).__name__))
        return PowerRatio(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, PowerRatio):
            raise TypeError("unsupported operand type(s) for **: 'PowerRatio' and '{}'".format(type(other).__name__))
        return PowerRatio(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, PowerRatio):
            raise TypeError("unsupported operand type(s) for ==: 'PowerRatio' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, PowerRatio):
            raise TypeError("unsupported operand type(s) for <: 'PowerRatio' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, PowerRatio):
            raise TypeError("unsupported operand type(s) for >: 'PowerRatio' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, PowerRatio):
            raise TypeError("unsupported operand type(s) for <=: 'PowerRatio' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, PowerRatio):
            raise TypeError("unsupported operand type(s) for >=: 'PowerRatio' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value
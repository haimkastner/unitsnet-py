from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



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
        

class RatioChangeRate(AbstractMeasure):
    """
    The change in ratio per unit of time.

    Args:
        value (float): The value.
        from_unit (RatioChangeRateUnits): The RatioChangeRate unit to create from, The default unit is DecimalFractionPerSecond
    """
    def __init__(self, value: float, from_unit: RatioChangeRateUnits = RatioChangeRateUnits.DecimalFractionPerSecond):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__percents_per_second = None
        
        self.__decimal_fractions_per_second = None
        

    def convert(self, unit: RatioChangeRateUnits) -> float:
        return self.__convert_from_base(unit)

    def __convert_from_base(self, from_unit: RatioChangeRateUnits) -> float:
        value = self._value
        
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
        return self._value

    
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

    
    def to_string(self, unit: RatioChangeRateUnits = RatioChangeRateUnits.DecimalFractionPerSecond) -> str:
        """
        Format the RatioChangeRate to string.
        Note! the default format for RatioChangeRate is DecimalFractionPerSecond.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == RatioChangeRateUnits.PercentPerSecond:
            return f"""{self.percents_per_second} %/s"""
        
        if unit == RatioChangeRateUnits.DecimalFractionPerSecond:
            return f"""{self.decimal_fractions_per_second} /s"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: RatioChangeRateUnits = RatioChangeRateUnits.DecimalFractionPerSecond) -> str:
        """
        Get RatioChangeRate unit abbreviation.
        Note! the default abbreviation for RatioChangeRate is DecimalFractionPerSecond.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == RatioChangeRateUnits.PercentPerSecond:
            return """%/s"""
        
        if unit_abbreviation == RatioChangeRateUnits.DecimalFractionPerSecond:
            return """/s"""
        
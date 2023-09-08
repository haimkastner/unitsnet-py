from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



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
        

class PowerRatio(AbstractMeasure):
    """
    The strength of a signal expressed in decibels (dB) relative to one watt.

    Args:
        value (float): The value.
        from_unit (PowerRatioUnits): The PowerRatio unit to create from, The default unit is DecibelWatt
    """
    def __init__(self, value: float, from_unit: PowerRatioUnits = PowerRatioUnits.DecibelWatt):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__decibel_watts = None
        
        self.__decibel_milliwatts = None
        

    def convert(self, unit: PowerRatioUnits) -> float:
        return self.__convert_from_base(unit)

    def __convert_from_base(self, from_unit: PowerRatioUnits) -> float:
        value = self._value
        
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
        return self._value

    
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

    
    def to_string(self, unit: PowerRatioUnits = PowerRatioUnits.DecibelWatt) -> str:
        """
        Format the PowerRatio to string.
        Note! the default format for PowerRatio is DecibelWatt.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == PowerRatioUnits.DecibelWatt:
            return f"""{self.decibel_watts} dBW"""
        
        if unit == PowerRatioUnits.DecibelMilliwatt:
            return f"""{self.decibel_milliwatts} dBmW"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: PowerRatioUnits = PowerRatioUnits.DecibelWatt) -> str:
        """
        Get PowerRatio unit abbreviation.
        Note! the default abbreviation for PowerRatio is DecibelWatt.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == PowerRatioUnits.DecibelWatt:
            return """dBW"""
        
        if unit_abbreviation == PowerRatioUnits.DecibelMilliwatt:
            return """dBmW"""
        
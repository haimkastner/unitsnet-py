from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class MagnetizationUnits(Enum):
        """
            MagnetizationUnits enumeration
        """
        
        AmperePerMeter = 'ampere_per_meter'
        """
            
        """
        

class Magnetization(AbstractMeasure):
    """
    In classical electromagnetism, magnetization is the vector field that expresses the density of permanent or induced magnetic dipole moments in a magnetic material.

    Args:
        value (float): The value.
        from_unit (MagnetizationUnits): The Magnetization unit to create from, The default unit is AmperePerMeter
    """
    def __init__(self, value: float, from_unit: MagnetizationUnits = MagnetizationUnits.AmperePerMeter):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__amperes_per_meter = None
        

    def convert(self, unit: MagnetizationUnits) -> float:
        return self.__convert_from_base(unit)

    def __convert_from_base(self, from_unit: MagnetizationUnits) -> float:
        value = self._value
        
        if from_unit == MagnetizationUnits.AmperePerMeter:
            return (value)
        
        return None


    def __convert_to_base(self, value: float, to_unit: MagnetizationUnits) -> float:
        
        if to_unit == MagnetizationUnits.AmperePerMeter:
            return (value)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
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

    
    def to_string(self, unit: MagnetizationUnits = MagnetizationUnits.AmperePerMeter) -> str:
        """
        Format the Magnetization to string.
        Note! the default format for Magnetization is AmperePerMeter.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == MagnetizationUnits.AmperePerMeter:
            return f"""{self.amperes_per_meter} A/m"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: MagnetizationUnits = MagnetizationUnits.AmperePerMeter) -> str:
        """
        Get Magnetization unit abbreviation.
        Note! the default abbreviation for Magnetization is AmperePerMeter.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == MagnetizationUnits.AmperePerMeter:
            return """A/m"""
        
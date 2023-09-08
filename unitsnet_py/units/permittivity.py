from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class PermittivityUnits(Enum):
        """
            PermittivityUnits enumeration
        """
        
        FaradPerMeter = 'farad_per_meter'
        """
            
        """
        

class Permittivity(AbstractMeasure):
    """
    In electromagnetism, permittivity is the measure of resistance that is encountered when forming an electric field in a particular medium.

    Args:
        value (float): The value.
        from_unit (PermittivityUnits): The Permittivity unit to create from, The default unit is FaradPerMeter
    """
    def __init__(self, value: float, from_unit: PermittivityUnits = PermittivityUnits.FaradPerMeter):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__farads_per_meter = None
        

    def convert(self, unit: PermittivityUnits) -> float:
        return self.__convert_from_base(unit)

    def __convert_from_base(self, from_unit: PermittivityUnits) -> float:
        value = self._value
        
        if from_unit == PermittivityUnits.FaradPerMeter:
            return (value)
        
        return None


    def __convert_to_base(self, value: float, to_unit: PermittivityUnits) -> float:
        
        if to_unit == PermittivityUnits.FaradPerMeter:
            return (value)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_farads_per_meter(farads_per_meter: float):
        """
        Create a new instance of Permittivity from a value in farads_per_meter.

        

        :param meters: The Permittivity value in farads_per_meter.
        :type farads_per_meter: float
        :return: A new instance of Permittivity.
        :rtype: Permittivity
        """
        return Permittivity(farads_per_meter, PermittivityUnits.FaradPerMeter)

    
    @property
    def farads_per_meter(self) -> float:
        """
        
        """
        if self.__farads_per_meter != None:
            return self.__farads_per_meter
        self.__farads_per_meter = self.__convert_from_base(PermittivityUnits.FaradPerMeter)
        return self.__farads_per_meter

    
    def to_string(self, unit: PermittivityUnits = PermittivityUnits.FaradPerMeter) -> str:
        """
        Format the Permittivity to string.
        Note! the default format for Permittivity is FaradPerMeter.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == PermittivityUnits.FaradPerMeter:
            return f"""{self.farads_per_meter} F/m"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: PermittivityUnits = PermittivityUnits.FaradPerMeter) -> str:
        """
        Get Permittivity unit abbreviation.
        Note! the default abbreviation for Permittivity is FaradPerMeter.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == PermittivityUnits.FaradPerMeter:
            return """F/m"""
        
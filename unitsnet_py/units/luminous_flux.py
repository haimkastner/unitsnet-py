from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class LuminousFluxUnits(Enum):
        """
            LuminousFluxUnits enumeration
        """
        
        Lumen = 'lumen'
        """
            
        """
        

class LuminousFlux(AbstractMeasure):
    """
    In photometry, luminous flux or luminous power is the measure of the perceived power of light.

    Args:
        value (float): The value.
        from_unit (LuminousFluxUnits): The LuminousFlux unit to create from, The default unit is Lumen
    """
    def __init__(self, value: float, from_unit: LuminousFluxUnits = LuminousFluxUnits.Lumen):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__lumens = None
        

    def convert(self, unit: LuminousFluxUnits) -> float:
        return self.__convert_from_base(unit)

    def __convert_from_base(self, from_unit: LuminousFluxUnits) -> float:
        value = self._value
        
        if from_unit == LuminousFluxUnits.Lumen:
            return (value)
        
        return None


    def __convert_to_base(self, value: float, to_unit: LuminousFluxUnits) -> float:
        
        if to_unit == LuminousFluxUnits.Lumen:
            return (value)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_lumens(lumens: float):
        """
        Create a new instance of LuminousFlux from a value in lumens.

        

        :param meters: The LuminousFlux value in lumens.
        :type lumens: float
        :return: A new instance of LuminousFlux.
        :rtype: LuminousFlux
        """
        return LuminousFlux(lumens, LuminousFluxUnits.Lumen)

    
    @property
    def lumens(self) -> float:
        """
        
        """
        if self.__lumens != None:
            return self.__lumens
        self.__lumens = self.__convert_from_base(LuminousFluxUnits.Lumen)
        return self.__lumens

    
    def to_string(self, unit: LuminousFluxUnits = LuminousFluxUnits.Lumen) -> str:
        """
        Format the LuminousFlux to string.
        Note! the default format for LuminousFlux is Lumen.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == LuminousFluxUnits.Lumen:
            return f"""{self.lumens} lm"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: LuminousFluxUnits = LuminousFluxUnits.Lumen) -> str:
        """
        Get LuminousFlux unit abbreviation.
        Note! the default abbreviation for LuminousFlux is Lumen.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == LuminousFluxUnits.Lumen:
            return """lm"""
        
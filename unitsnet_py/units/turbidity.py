from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class TurbidityUnits(Enum):
        """
            TurbidityUnits enumeration
        """
        
        NTU = 'ntu'
        """
            
        """
        

class Turbidity(AbstractMeasure):
    """
    Turbidity is the cloudiness or haziness of a fluid caused by large numbers of individual particles that are generally invisible to the naked eye, similar to smoke in air. The measurement of turbidity is a key test of water quality.

    Args:
        value (float): The value.
        from_unit (TurbidityUnits): The Turbidity unit to create from, The default unit is NTU
    """
    def __init__(self, value: float, from_unit: TurbidityUnits = TurbidityUnits.NTU):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__ntu = None
        

    def convert(self, unit: TurbidityUnits) -> float:
        return self.__convert_from_base(unit)

    def __convert_from_base(self, from_unit: TurbidityUnits) -> float:
        value = self._value
        
        if from_unit == TurbidityUnits.NTU:
            return (value)
        
        return None


    def __convert_to_base(self, value: float, to_unit: TurbidityUnits) -> float:
        
        if to_unit == TurbidityUnits.NTU:
            return (value)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
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

    
    def to_string(self, unit: TurbidityUnits = TurbidityUnits.NTU) -> str:
        """
        Format the Turbidity to string.
        Note! the default format for Turbidity is NTU.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == TurbidityUnits.NTU:
            return f"""{self.ntu} NTU"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: TurbidityUnits = TurbidityUnits.NTU) -> str:
        """
        Get Turbidity unit abbreviation.
        Note! the default abbreviation for Turbidity is NTU.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == TurbidityUnits.NTU:
            return """NTU"""
        
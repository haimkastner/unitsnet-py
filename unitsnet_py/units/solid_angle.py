from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class SolidAngleUnits(Enum):
        """
            SolidAngleUnits enumeration
        """
        
        Steradian = 'steradian'
        """
            
        """
        

class SolidAngle(AbstractMeasure):
    """
    In geometry, a solid angle is the two-dimensional angle in three-dimensional space that an object subtends at a point.

    Args:
        value (float): The value.
        from_unit (SolidAngleUnits): The SolidAngle unit to create from, The default unit is Steradian
    """
    def __init__(self, value: float, from_unit: SolidAngleUnits = SolidAngleUnits.Steradian):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__steradians = None
        

    def convert(self, unit: SolidAngleUnits) -> float:
        return self.__convert_from_base(unit)

    def __convert_from_base(self, from_unit: SolidAngleUnits) -> float:
        value = self._value
        
        if from_unit == SolidAngleUnits.Steradian:
            return (value)
        
        return None


    def __convert_to_base(self, value: float, to_unit: SolidAngleUnits) -> float:
        
        if to_unit == SolidAngleUnits.Steradian:
            return (value)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
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

    
    def to_string(self, unit: SolidAngleUnits = SolidAngleUnits.Steradian) -> str:
        """
        Format the SolidAngle to string.
        Note! the default format for SolidAngle is Steradian.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == SolidAngleUnits.Steradian:
            return f"""{self.steradians} sr"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: SolidAngleUnits = SolidAngleUnits.Steradian) -> str:
        """
        Get SolidAngle unit abbreviation.
        Note! the default abbreviation for SolidAngle is Steradian.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == SolidAngleUnits.Steradian:
            return """sr"""
        
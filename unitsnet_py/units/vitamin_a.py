from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class VitaminAUnits(Enum):
        """
            VitaminAUnits enumeration
        """
        
        InternationalUnit = 'international_unit'
        """
            
        """
        

class VitaminA(AbstractMeasure):
    """
    Vitamin A: 1 IU is the biological equivalent of 0.3 µg retinol, or of 0.6 µg beta-carotene.

    Args:
        value (float): The value.
        from_unit (VitaminAUnits): The VitaminA unit to create from, The default unit is InternationalUnit
    """
    def __init__(self, value: float, from_unit: VitaminAUnits = VitaminAUnits.InternationalUnit):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__international_units = None
        

    def convert(self, unit: VitaminAUnits) -> float:
        return self.__convert_from_base(unit)

    def __convert_from_base(self, from_unit: VitaminAUnits) -> float:
        value = self._value
        
        if from_unit == VitaminAUnits.InternationalUnit:
            return (value)
        
        return None


    def __convert_to_base(self, value: float, to_unit: VitaminAUnits) -> float:
        
        if to_unit == VitaminAUnits.InternationalUnit:
            return (value)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_international_units(international_units: float):
        """
        Create a new instance of VitaminA from a value in international_units.

        

        :param meters: The VitaminA value in international_units.
        :type international_units: float
        :return: A new instance of VitaminA.
        :rtype: VitaminA
        """
        return VitaminA(international_units, VitaminAUnits.InternationalUnit)

    
    @property
    def international_units(self) -> float:
        """
        
        """
        if self.__international_units != None:
            return self.__international_units
        self.__international_units = self.__convert_from_base(VitaminAUnits.InternationalUnit)
        return self.__international_units

    
    def to_string(self, unit: VitaminAUnits = VitaminAUnits.InternationalUnit) -> str:
        """
        Format the VitaminA to string.
        Note! the default format for VitaminA is InternationalUnit.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == VitaminAUnits.InternationalUnit:
            return f"""{self.international_units} IU"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: VitaminAUnits = VitaminAUnits.InternationalUnit) -> str:
        """
        Get VitaminA unit abbreviation.
        Note! the default abbreviation for VitaminA is InternationalUnit.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == VitaminAUnits.InternationalUnit:
            return """IU"""
        
from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class ElectricFieldUnits(Enum):
        """
            ElectricFieldUnits enumeration
        """
        
        VoltPerMeter = 'volt_per_meter'
        """
            
        """
        

class ElectricField(AbstractMeasure):
    """
    An electric field is a force field that surrounds electric charges that attracts or repels other electric charges.

    Args:
        value (float): The value.
        from_unit (ElectricFieldUnits): The ElectricField unit to create from, The default unit is VoltPerMeter
    """
    def __init__(self, value: float, from_unit: ElectricFieldUnits = ElectricFieldUnits.VoltPerMeter):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__volts_per_meter = None
        

    def convert(self, unit: ElectricFieldUnits) -> float:
        return self.__convert_from_base(unit)

    def __convert_from_base(self, from_unit: ElectricFieldUnits) -> float:
        value = self._value
        
        if from_unit == ElectricFieldUnits.VoltPerMeter:
            return (value)
        
        return None


    def __convert_to_base(self, value: float, to_unit: ElectricFieldUnits) -> float:
        
        if to_unit == ElectricFieldUnits.VoltPerMeter:
            return (value)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_volts_per_meter(volts_per_meter: float):
        """
        Create a new instance of ElectricField from a value in volts_per_meter.

        

        :param meters: The ElectricField value in volts_per_meter.
        :type volts_per_meter: float
        :return: A new instance of ElectricField.
        :rtype: ElectricField
        """
        return ElectricField(volts_per_meter, ElectricFieldUnits.VoltPerMeter)

    
    @property
    def volts_per_meter(self) -> float:
        """
        
        """
        if self.__volts_per_meter != None:
            return self.__volts_per_meter
        self.__volts_per_meter = self.__convert_from_base(ElectricFieldUnits.VoltPerMeter)
        return self.__volts_per_meter

    
    def to_string(self, unit: ElectricFieldUnits = ElectricFieldUnits.VoltPerMeter) -> str:
        """
        Format the ElectricField to string.
        Note! the default format for ElectricField is VoltPerMeter.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == ElectricFieldUnits.VoltPerMeter:
            return f"""{self.volts_per_meter} V/m"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: ElectricFieldUnits = ElectricFieldUnits.VoltPerMeter) -> str:
        """
        Get ElectricField unit abbreviation.
        Note! the default abbreviation for ElectricField is VoltPerMeter.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == ElectricFieldUnits.VoltPerMeter:
            return """V/m"""
        
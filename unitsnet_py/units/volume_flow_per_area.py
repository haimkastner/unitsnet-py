from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class VolumeFlowPerAreaUnits(Enum):
        """
            VolumeFlowPerAreaUnits enumeration
        """
        
        CubicMeterPerSecondPerSquareMeter = 'cubic_meter_per_second_per_square_meter'
        """
            
        """
        
        CubicFootPerMinutePerSquareFoot = 'cubic_foot_per_minute_per_square_foot'
        """
            
        """
        

class VolumeFlowPerArea(AbstractMeasure):
    """
    None

    Args:
        value (float): The value.
        from_unit (VolumeFlowPerAreaUnits): The VolumeFlowPerArea unit to create from, The default unit is CubicMeterPerSecondPerSquareMeter
    """
    def __init__(self, value: float, from_unit: VolumeFlowPerAreaUnits = VolumeFlowPerAreaUnits.CubicMeterPerSecondPerSquareMeter):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__cubic_meters_per_second_per_square_meter = None
        
        self.__cubic_feet_per_minute_per_square_foot = None
        

    def convert(self, unit: VolumeFlowPerAreaUnits) -> float:
        return self.__convert_from_base(unit)

    def __convert_from_base(self, from_unit: VolumeFlowPerAreaUnits) -> float:
        value = self._value
        
        if from_unit == VolumeFlowPerAreaUnits.CubicMeterPerSecondPerSquareMeter:
            return (value)
        
        if from_unit == VolumeFlowPerAreaUnits.CubicFootPerMinutePerSquareFoot:
            return (value * 196.850394)
        
        return None


    def __convert_to_base(self, value: float, to_unit: VolumeFlowPerAreaUnits) -> float:
        
        if to_unit == VolumeFlowPerAreaUnits.CubicMeterPerSecondPerSquareMeter:
            return (value)
        
        if to_unit == VolumeFlowPerAreaUnits.CubicFootPerMinutePerSquareFoot:
            return (value / 196.850394)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_cubic_meters_per_second_per_square_meter(cubic_meters_per_second_per_square_meter: float):
        """
        Create a new instance of VolumeFlowPerArea from a value in cubic_meters_per_second_per_square_meter.

        

        :param meters: The VolumeFlowPerArea value in cubic_meters_per_second_per_square_meter.
        :type cubic_meters_per_second_per_square_meter: float
        :return: A new instance of VolumeFlowPerArea.
        :rtype: VolumeFlowPerArea
        """
        return VolumeFlowPerArea(cubic_meters_per_second_per_square_meter, VolumeFlowPerAreaUnits.CubicMeterPerSecondPerSquareMeter)

    
    @staticmethod
    def from_cubic_feet_per_minute_per_square_foot(cubic_feet_per_minute_per_square_foot: float):
        """
        Create a new instance of VolumeFlowPerArea from a value in cubic_feet_per_minute_per_square_foot.

        

        :param meters: The VolumeFlowPerArea value in cubic_feet_per_minute_per_square_foot.
        :type cubic_feet_per_minute_per_square_foot: float
        :return: A new instance of VolumeFlowPerArea.
        :rtype: VolumeFlowPerArea
        """
        return VolumeFlowPerArea(cubic_feet_per_minute_per_square_foot, VolumeFlowPerAreaUnits.CubicFootPerMinutePerSquareFoot)

    
    @property
    def cubic_meters_per_second_per_square_meter(self) -> float:
        """
        
        """
        if self.__cubic_meters_per_second_per_square_meter != None:
            return self.__cubic_meters_per_second_per_square_meter
        self.__cubic_meters_per_second_per_square_meter = self.__convert_from_base(VolumeFlowPerAreaUnits.CubicMeterPerSecondPerSquareMeter)
        return self.__cubic_meters_per_second_per_square_meter

    
    @property
    def cubic_feet_per_minute_per_square_foot(self) -> float:
        """
        
        """
        if self.__cubic_feet_per_minute_per_square_foot != None:
            return self.__cubic_feet_per_minute_per_square_foot
        self.__cubic_feet_per_minute_per_square_foot = self.__convert_from_base(VolumeFlowPerAreaUnits.CubicFootPerMinutePerSquareFoot)
        return self.__cubic_feet_per_minute_per_square_foot

    
    def to_string(self, unit: VolumeFlowPerAreaUnits = VolumeFlowPerAreaUnits.CubicMeterPerSecondPerSquareMeter) -> str:
        """
        Format the VolumeFlowPerArea to string.
        Note! the default format for VolumeFlowPerArea is CubicMeterPerSecondPerSquareMeter.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == VolumeFlowPerAreaUnits.CubicMeterPerSecondPerSquareMeter:
            return f"""{self.cubic_meters_per_second_per_square_meter} m³/(s·m²)"""
        
        if unit == VolumeFlowPerAreaUnits.CubicFootPerMinutePerSquareFoot:
            return f"""{self.cubic_feet_per_minute_per_square_foot} CFM/ft²"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: VolumeFlowPerAreaUnits = VolumeFlowPerAreaUnits.CubicMeterPerSecondPerSquareMeter) -> str:
        """
        Get VolumeFlowPerArea unit abbreviation.
        Note! the default abbreviation for VolumeFlowPerArea is CubicMeterPerSecondPerSquareMeter.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == VolumeFlowPerAreaUnits.CubicMeterPerSecondPerSquareMeter:
            return """m³/(s·m²)"""
        
        if unit_abbreviation == VolumeFlowPerAreaUnits.CubicFootPerMinutePerSquareFoot:
            return """CFM/ft²"""
        
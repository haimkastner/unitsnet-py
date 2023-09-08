from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class TemperatureGradientUnits(Enum):
        """
            TemperatureGradientUnits enumeration
        """
        
        KelvinPerMeter = 'kelvin_per_meter'
        """
            
        """
        
        DegreeCelsiusPerMeter = 'degree_celsius_per_meter'
        """
            
        """
        
        DegreeFahrenheitPerFoot = 'degree_fahrenheit_per_foot'
        """
            
        """
        
        DegreeCelsiusPerKilometer = 'degree_celsius_per_kilometer'
        """
            
        """
        

class TemperatureGradient(AbstractMeasure):
    """
    None

    Args:
        value (float): The value.
        from_unit (TemperatureGradientUnits): The TemperatureGradient unit to create from, The default unit is KelvinPerMeter
    """
    def __init__(self, value: float, from_unit: TemperatureGradientUnits = TemperatureGradientUnits.KelvinPerMeter):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__kelvins_per_meter = None
        
        self.__degrees_celcius_per_meter = None
        
        self.__degrees_fahrenheit_per_foot = None
        
        self.__degrees_celcius_per_kilometer = None
        

    def convert(self, unit: TemperatureGradientUnits) -> float:
        return self.__convert_from_base(unit)

    def __convert_from_base(self, from_unit: TemperatureGradientUnits) -> float:
        value = self._value
        
        if from_unit == TemperatureGradientUnits.KelvinPerMeter:
            return (value)
        
        if from_unit == TemperatureGradientUnits.DegreeCelsiusPerMeter:
            return (value)
        
        if from_unit == TemperatureGradientUnits.DegreeFahrenheitPerFoot:
            return ((value * 0.3048) * 9 / 5)
        
        if from_unit == TemperatureGradientUnits.DegreeCelsiusPerKilometer:
            return (value * 1e3)
        
        return None


    def __convert_to_base(self, value: float, to_unit: TemperatureGradientUnits) -> float:
        
        if to_unit == TemperatureGradientUnits.KelvinPerMeter:
            return (value)
        
        if to_unit == TemperatureGradientUnits.DegreeCelsiusPerMeter:
            return (value)
        
        if to_unit == TemperatureGradientUnits.DegreeFahrenheitPerFoot:
            return ((value / 0.3048) * 5 / 9)
        
        if to_unit == TemperatureGradientUnits.DegreeCelsiusPerKilometer:
            return (value / 1e3)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_kelvins_per_meter(kelvins_per_meter: float):
        """
        Create a new instance of TemperatureGradient from a value in kelvins_per_meter.

        

        :param meters: The TemperatureGradient value in kelvins_per_meter.
        :type kelvins_per_meter: float
        :return: A new instance of TemperatureGradient.
        :rtype: TemperatureGradient
        """
        return TemperatureGradient(kelvins_per_meter, TemperatureGradientUnits.KelvinPerMeter)

    
    @staticmethod
    def from_degrees_celcius_per_meter(degrees_celcius_per_meter: float):
        """
        Create a new instance of TemperatureGradient from a value in degrees_celcius_per_meter.

        

        :param meters: The TemperatureGradient value in degrees_celcius_per_meter.
        :type degrees_celcius_per_meter: float
        :return: A new instance of TemperatureGradient.
        :rtype: TemperatureGradient
        """
        return TemperatureGradient(degrees_celcius_per_meter, TemperatureGradientUnits.DegreeCelsiusPerMeter)

    
    @staticmethod
    def from_degrees_fahrenheit_per_foot(degrees_fahrenheit_per_foot: float):
        """
        Create a new instance of TemperatureGradient from a value in degrees_fahrenheit_per_foot.

        

        :param meters: The TemperatureGradient value in degrees_fahrenheit_per_foot.
        :type degrees_fahrenheit_per_foot: float
        :return: A new instance of TemperatureGradient.
        :rtype: TemperatureGradient
        """
        return TemperatureGradient(degrees_fahrenheit_per_foot, TemperatureGradientUnits.DegreeFahrenheitPerFoot)

    
    @staticmethod
    def from_degrees_celcius_per_kilometer(degrees_celcius_per_kilometer: float):
        """
        Create a new instance of TemperatureGradient from a value in degrees_celcius_per_kilometer.

        

        :param meters: The TemperatureGradient value in degrees_celcius_per_kilometer.
        :type degrees_celcius_per_kilometer: float
        :return: A new instance of TemperatureGradient.
        :rtype: TemperatureGradient
        """
        return TemperatureGradient(degrees_celcius_per_kilometer, TemperatureGradientUnits.DegreeCelsiusPerKilometer)

    
    @property
    def kelvins_per_meter(self) -> float:
        """
        
        """
        if self.__kelvins_per_meter != None:
            return self.__kelvins_per_meter
        self.__kelvins_per_meter = self.__convert_from_base(TemperatureGradientUnits.KelvinPerMeter)
        return self.__kelvins_per_meter

    
    @property
    def degrees_celcius_per_meter(self) -> float:
        """
        
        """
        if self.__degrees_celcius_per_meter != None:
            return self.__degrees_celcius_per_meter
        self.__degrees_celcius_per_meter = self.__convert_from_base(TemperatureGradientUnits.DegreeCelsiusPerMeter)
        return self.__degrees_celcius_per_meter

    
    @property
    def degrees_fahrenheit_per_foot(self) -> float:
        """
        
        """
        if self.__degrees_fahrenheit_per_foot != None:
            return self.__degrees_fahrenheit_per_foot
        self.__degrees_fahrenheit_per_foot = self.__convert_from_base(TemperatureGradientUnits.DegreeFahrenheitPerFoot)
        return self.__degrees_fahrenheit_per_foot

    
    @property
    def degrees_celcius_per_kilometer(self) -> float:
        """
        
        """
        if self.__degrees_celcius_per_kilometer != None:
            return self.__degrees_celcius_per_kilometer
        self.__degrees_celcius_per_kilometer = self.__convert_from_base(TemperatureGradientUnits.DegreeCelsiusPerKilometer)
        return self.__degrees_celcius_per_kilometer

    
    def to_string(self, unit: TemperatureGradientUnits = TemperatureGradientUnits.KelvinPerMeter) -> str:
        """
        Format the TemperatureGradient to string.
        Note! the default format for TemperatureGradient is KelvinPerMeter.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == TemperatureGradientUnits.KelvinPerMeter:
            return f"""{self.kelvins_per_meter} ∆°K/m"""
        
        if unit == TemperatureGradientUnits.DegreeCelsiusPerMeter:
            return f"""{self.degrees_celcius_per_meter} ∆°C/m"""
        
        if unit == TemperatureGradientUnits.DegreeFahrenheitPerFoot:
            return f"""{self.degrees_fahrenheit_per_foot} ∆°F/ft"""
        
        if unit == TemperatureGradientUnits.DegreeCelsiusPerKilometer:
            return f"""{self.degrees_celcius_per_kilometer} ∆°C/km"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: TemperatureGradientUnits = TemperatureGradientUnits.KelvinPerMeter) -> str:
        """
        Get TemperatureGradient unit abbreviation.
        Note! the default abbreviation for TemperatureGradient is KelvinPerMeter.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == TemperatureGradientUnits.KelvinPerMeter:
            return """∆°K/m"""
        
        if unit_abbreviation == TemperatureGradientUnits.DegreeCelsiusPerMeter:
            return """∆°C/m"""
        
        if unit_abbreviation == TemperatureGradientUnits.DegreeFahrenheitPerFoot:
            return """∆°F/ft"""
        
        if unit_abbreviation == TemperatureGradientUnits.DegreeCelsiusPerKilometer:
            return """∆°C/km"""
        
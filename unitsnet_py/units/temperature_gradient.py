from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class TemperatureGradientUnits(Enum):
        """
            TemperatureGradientUnits enumeration
        """
        
        KelvinPerMeter = 'KelvinPerMeter'
        """
            
        """
        
        DegreeCelsiusPerMeter = 'DegreeCelsiusPerMeter'
        """
            
        """
        
        DegreeFahrenheitPerFoot = 'DegreeFahrenheitPerFoot'
        """
            
        """
        
        DegreeCelsiusPerKilometer = 'DegreeCelsiusPerKilometer'
        """
            
        """
        

class TemperatureGradientDto:
    """
    A DTO representation of a TemperatureGradient

    Attributes:
        value (float): The value of the TemperatureGradient.
        unit (TemperatureGradientUnits): The specific unit that the TemperatureGradient value is representing.
    """

    def __init__(self, value: float, unit: TemperatureGradientUnits):
        """
        Create a new DTO representation of a TemperatureGradient

        Parameters:
            value (float): The value of the TemperatureGradient.
            unit (TemperatureGradientUnits): The specific unit that the TemperatureGradient value is representing.
        """
        self.value: float = value
        """
        The value of the TemperatureGradient
        """
        self.unit: TemperatureGradientUnits = unit
        """
        The specific unit that the TemperatureGradient value is representing
        """

    def to_json(self):
        """
        Get a TemperatureGradient DTO JSON object representing the current unit.

        :return: JSON object represents TemperatureGradient DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "KelvinPerMeter"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of TemperatureGradient DTO from a json representation.

        :param data: The TemperatureGradient DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "KelvinPerMeter"}
        :return: A new instance of TemperatureGradientDto.
        :rtype: TemperatureGradientDto
        """
        return TemperatureGradientDto(value=data["value"], unit=TemperatureGradientUnits(data["unit"]))


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

    def to_dto(self, hold_in_unit: TemperatureGradientUnits = TemperatureGradientUnits.KelvinPerMeter) -> TemperatureGradientDto:
        """
        Get a new instance of TemperatureGradient DTO representing the current unit.

        :param hold_in_unit: The specific TemperatureGradient unit to store the TemperatureGradient value in the DTO representation.
        :type hold_in_unit: TemperatureGradientUnits
        :return: A new instance of TemperatureGradientDto.
        :rtype: TemperatureGradientDto
        """
        return TemperatureGradientDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: TemperatureGradientUnits = TemperatureGradientUnits.KelvinPerMeter):
        """
        Get a TemperatureGradient DTO JSON object representing the current unit.

        :param hold_in_unit: The specific TemperatureGradient unit to store the TemperatureGradient value in the DTO representation.
        :type hold_in_unit: TemperatureGradientUnits
        :return: JSON object represents TemperatureGradient DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "KelvinPerMeter"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(temperature_gradient_dto: TemperatureGradientDto):
        """
        Obtain a new instance of TemperatureGradient from a DTO unit object.

        :param temperature_gradient_dto: The TemperatureGradient DTO representation.
        :type temperature_gradient_dto: TemperatureGradientDto
        :return: A new instance of TemperatureGradient.
        :rtype: TemperatureGradient
        """
        return TemperatureGradient(temperature_gradient_dto.value, temperature_gradient_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of TemperatureGradient from a DTO unit json representation.

        :param data: The TemperatureGradient DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "KelvinPerMeter"}
        :return: A new instance of TemperatureGradient.
        :rtype: TemperatureGradient
        """
        return TemperatureGradient.from_dto(TemperatureGradientDto.from_json(data))

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

    
    def to_string(self, unit: TemperatureGradientUnits = TemperatureGradientUnits.KelvinPerMeter, fractional_digits: int = None) -> str:
        """
        Format the TemperatureGradient to a string.
        
        Note: the default format for TemperatureGradient is KelvinPerMeter.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the TemperatureGradient. Default is 'KelvinPerMeter'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == TemperatureGradientUnits.KelvinPerMeter:
            return f"""{super()._truncate_fraction_digits(self.kelvins_per_meter, fractional_digits)} ∆°K/m"""
        
        if unit == TemperatureGradientUnits.DegreeCelsiusPerMeter:
            return f"""{super()._truncate_fraction_digits(self.degrees_celcius_per_meter, fractional_digits)} ∆°C/m"""
        
        if unit == TemperatureGradientUnits.DegreeFahrenheitPerFoot:
            return f"""{super()._truncate_fraction_digits(self.degrees_fahrenheit_per_foot, fractional_digits)} ∆°F/ft"""
        
        if unit == TemperatureGradientUnits.DegreeCelsiusPerKilometer:
            return f"""{super()._truncate_fraction_digits(self.degrees_celcius_per_kilometer, fractional_digits)} ∆°C/km"""
        
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
        
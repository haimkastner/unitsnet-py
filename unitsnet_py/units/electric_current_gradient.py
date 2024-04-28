from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class ElectricCurrentGradientUnits(Enum):
        """
            ElectricCurrentGradientUnits enumeration
        """
        
        AmperePerSecond = 'AmperePerSecond'
        """
            
        """
        
        AmperePerMinute = 'AmperePerMinute'
        """
            
        """
        
        AmperePerMillisecond = 'AmperePerMillisecond'
        """
            
        """
        
        AmperePerMicrosecond = 'AmperePerMicrosecond'
        """
            
        """
        
        AmperePerNanosecond = 'AmperePerNanosecond'
        """
            
        """
        
        MilliamperePerSecond = 'MilliamperePerSecond'
        """
            
        """
        
        MilliamperePerMinute = 'MilliamperePerMinute'
        """
            
        """
        

class ElectricCurrentGradientDto:
    """
    A DTO representation of a ElectricCurrentGradient

    Attributes:
        value (float): The value of the ElectricCurrentGradient.
        unit (ElectricCurrentGradientUnits): The specific unit that the ElectricCurrentGradient value is representing.
    """

    def __init__(self, value: float, unit: ElectricCurrentGradientUnits):
        """
        Create a new DTO representation of a ElectricCurrentGradient

        Parameters:
            value (float): The value of the ElectricCurrentGradient.
            unit (ElectricCurrentGradientUnits): The specific unit that the ElectricCurrentGradient value is representing.
        """
        self.value: float = value
        """
        The value of the ElectricCurrentGradient
        """
        self.unit: ElectricCurrentGradientUnits = unit
        """
        The specific unit that the ElectricCurrentGradient value is representing
        """

    def to_json(self):
        """
        Get a ElectricCurrentGradient DTO JSON object representing the current unit.

        :return: JSON object represents ElectricCurrentGradient DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "AmperePerSecond"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of ElectricCurrentGradient DTO from a json representation.

        :param data: The ElectricCurrentGradient DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "AmperePerSecond"}
        :return: A new instance of ElectricCurrentGradientDto.
        :rtype: ElectricCurrentGradientDto
        """
        return ElectricCurrentGradientDto(value=data["value"], unit=ElectricCurrentGradientUnits(data["unit"]))


class ElectricCurrentGradient(AbstractMeasure):
    """
    In electromagnetism, the current gradient describes how the current changes in time.

    Args:
        value (float): The value.
        from_unit (ElectricCurrentGradientUnits): The ElectricCurrentGradient unit to create from, The default unit is AmperePerSecond
    """
    def __init__(self, value: float, from_unit: ElectricCurrentGradientUnits = ElectricCurrentGradientUnits.AmperePerSecond):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__amperes_per_second = None
        
        self.__amperes_per_minute = None
        
        self.__amperes_per_millisecond = None
        
        self.__amperes_per_microsecond = None
        
        self.__amperes_per_nanosecond = None
        
        self.__milliamperes_per_second = None
        
        self.__milliamperes_per_minute = None
        

    def convert(self, unit: ElectricCurrentGradientUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: ElectricCurrentGradientUnits = ElectricCurrentGradientUnits.AmperePerSecond) -> ElectricCurrentGradientDto:
        """
        Get a new instance of ElectricCurrentGradient DTO representing the current unit.

        :param hold_in_unit: The specific ElectricCurrentGradient unit to store the ElectricCurrentGradient value in the DTO representation.
        :type hold_in_unit: ElectricCurrentGradientUnits
        :return: A new instance of ElectricCurrentGradientDto.
        :rtype: ElectricCurrentGradientDto
        """
        return ElectricCurrentGradientDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: ElectricCurrentGradientUnits = ElectricCurrentGradientUnits.AmperePerSecond):
        """
        Get a ElectricCurrentGradient DTO JSON object representing the current unit.

        :param hold_in_unit: The specific ElectricCurrentGradient unit to store the ElectricCurrentGradient value in the DTO representation.
        :type hold_in_unit: ElectricCurrentGradientUnits
        :return: JSON object represents ElectricCurrentGradient DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "AmperePerSecond"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(electric_current_gradient_dto: ElectricCurrentGradientDto):
        """
        Obtain a new instance of ElectricCurrentGradient from a DTO unit object.

        :param electric_current_gradient_dto: The ElectricCurrentGradient DTO representation.
        :type electric_current_gradient_dto: ElectricCurrentGradientDto
        :return: A new instance of ElectricCurrentGradient.
        :rtype: ElectricCurrentGradient
        """
        return ElectricCurrentGradient(electric_current_gradient_dto.value, electric_current_gradient_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of ElectricCurrentGradient from a DTO unit json representation.

        :param data: The ElectricCurrentGradient DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "AmperePerSecond"}
        :return: A new instance of ElectricCurrentGradient.
        :rtype: ElectricCurrentGradient
        """
        return ElectricCurrentGradient.from_dto(ElectricCurrentGradientDto.from_json(data))

    def __convert_from_base(self, from_unit: ElectricCurrentGradientUnits) -> float:
        value = self._value
        
        if from_unit == ElectricCurrentGradientUnits.AmperePerSecond:
            return (value)
        
        if from_unit == ElectricCurrentGradientUnits.AmperePerMinute:
            return (value * 60)
        
        if from_unit == ElectricCurrentGradientUnits.AmperePerMillisecond:
            return (value / 1e3)
        
        if from_unit == ElectricCurrentGradientUnits.AmperePerMicrosecond:
            return (value / 1e6)
        
        if from_unit == ElectricCurrentGradientUnits.AmperePerNanosecond:
            return (value / 1e9)
        
        if from_unit == ElectricCurrentGradientUnits.MilliamperePerSecond:
            return ((value) / 0.001)
        
        if from_unit == ElectricCurrentGradientUnits.MilliamperePerMinute:
            return ((value * 60) / 0.001)
        
        return None


    def __convert_to_base(self, value: float, to_unit: ElectricCurrentGradientUnits) -> float:
        
        if to_unit == ElectricCurrentGradientUnits.AmperePerSecond:
            return (value)
        
        if to_unit == ElectricCurrentGradientUnits.AmperePerMinute:
            return (value / 60)
        
        if to_unit == ElectricCurrentGradientUnits.AmperePerMillisecond:
            return (value * 1e3)
        
        if to_unit == ElectricCurrentGradientUnits.AmperePerMicrosecond:
            return (value * 1e6)
        
        if to_unit == ElectricCurrentGradientUnits.AmperePerNanosecond:
            return (value * 1e9)
        
        if to_unit == ElectricCurrentGradientUnits.MilliamperePerSecond:
            return ((value) * 0.001)
        
        if to_unit == ElectricCurrentGradientUnits.MilliamperePerMinute:
            return ((value / 60) * 0.001)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_amperes_per_second(amperes_per_second: float):
        """
        Create a new instance of ElectricCurrentGradient from a value in amperes_per_second.

        

        :param meters: The ElectricCurrentGradient value in amperes_per_second.
        :type amperes_per_second: float
        :return: A new instance of ElectricCurrentGradient.
        :rtype: ElectricCurrentGradient
        """
        return ElectricCurrentGradient(amperes_per_second, ElectricCurrentGradientUnits.AmperePerSecond)

    
    @staticmethod
    def from_amperes_per_minute(amperes_per_minute: float):
        """
        Create a new instance of ElectricCurrentGradient from a value in amperes_per_minute.

        

        :param meters: The ElectricCurrentGradient value in amperes_per_minute.
        :type amperes_per_minute: float
        :return: A new instance of ElectricCurrentGradient.
        :rtype: ElectricCurrentGradient
        """
        return ElectricCurrentGradient(amperes_per_minute, ElectricCurrentGradientUnits.AmperePerMinute)

    
    @staticmethod
    def from_amperes_per_millisecond(amperes_per_millisecond: float):
        """
        Create a new instance of ElectricCurrentGradient from a value in amperes_per_millisecond.

        

        :param meters: The ElectricCurrentGradient value in amperes_per_millisecond.
        :type amperes_per_millisecond: float
        :return: A new instance of ElectricCurrentGradient.
        :rtype: ElectricCurrentGradient
        """
        return ElectricCurrentGradient(amperes_per_millisecond, ElectricCurrentGradientUnits.AmperePerMillisecond)

    
    @staticmethod
    def from_amperes_per_microsecond(amperes_per_microsecond: float):
        """
        Create a new instance of ElectricCurrentGradient from a value in amperes_per_microsecond.

        

        :param meters: The ElectricCurrentGradient value in amperes_per_microsecond.
        :type amperes_per_microsecond: float
        :return: A new instance of ElectricCurrentGradient.
        :rtype: ElectricCurrentGradient
        """
        return ElectricCurrentGradient(amperes_per_microsecond, ElectricCurrentGradientUnits.AmperePerMicrosecond)

    
    @staticmethod
    def from_amperes_per_nanosecond(amperes_per_nanosecond: float):
        """
        Create a new instance of ElectricCurrentGradient from a value in amperes_per_nanosecond.

        

        :param meters: The ElectricCurrentGradient value in amperes_per_nanosecond.
        :type amperes_per_nanosecond: float
        :return: A new instance of ElectricCurrentGradient.
        :rtype: ElectricCurrentGradient
        """
        return ElectricCurrentGradient(amperes_per_nanosecond, ElectricCurrentGradientUnits.AmperePerNanosecond)

    
    @staticmethod
    def from_milliamperes_per_second(milliamperes_per_second: float):
        """
        Create a new instance of ElectricCurrentGradient from a value in milliamperes_per_second.

        

        :param meters: The ElectricCurrentGradient value in milliamperes_per_second.
        :type milliamperes_per_second: float
        :return: A new instance of ElectricCurrentGradient.
        :rtype: ElectricCurrentGradient
        """
        return ElectricCurrentGradient(milliamperes_per_second, ElectricCurrentGradientUnits.MilliamperePerSecond)

    
    @staticmethod
    def from_milliamperes_per_minute(milliamperes_per_minute: float):
        """
        Create a new instance of ElectricCurrentGradient from a value in milliamperes_per_minute.

        

        :param meters: The ElectricCurrentGradient value in milliamperes_per_minute.
        :type milliamperes_per_minute: float
        :return: A new instance of ElectricCurrentGradient.
        :rtype: ElectricCurrentGradient
        """
        return ElectricCurrentGradient(milliamperes_per_minute, ElectricCurrentGradientUnits.MilliamperePerMinute)

    
    @property
    def amperes_per_second(self) -> float:
        """
        
        """
        if self.__amperes_per_second != None:
            return self.__amperes_per_second
        self.__amperes_per_second = self.__convert_from_base(ElectricCurrentGradientUnits.AmperePerSecond)
        return self.__amperes_per_second

    
    @property
    def amperes_per_minute(self) -> float:
        """
        
        """
        if self.__amperes_per_minute != None:
            return self.__amperes_per_minute
        self.__amperes_per_minute = self.__convert_from_base(ElectricCurrentGradientUnits.AmperePerMinute)
        return self.__amperes_per_minute

    
    @property
    def amperes_per_millisecond(self) -> float:
        """
        
        """
        if self.__amperes_per_millisecond != None:
            return self.__amperes_per_millisecond
        self.__amperes_per_millisecond = self.__convert_from_base(ElectricCurrentGradientUnits.AmperePerMillisecond)
        return self.__amperes_per_millisecond

    
    @property
    def amperes_per_microsecond(self) -> float:
        """
        
        """
        if self.__amperes_per_microsecond != None:
            return self.__amperes_per_microsecond
        self.__amperes_per_microsecond = self.__convert_from_base(ElectricCurrentGradientUnits.AmperePerMicrosecond)
        return self.__amperes_per_microsecond

    
    @property
    def amperes_per_nanosecond(self) -> float:
        """
        
        """
        if self.__amperes_per_nanosecond != None:
            return self.__amperes_per_nanosecond
        self.__amperes_per_nanosecond = self.__convert_from_base(ElectricCurrentGradientUnits.AmperePerNanosecond)
        return self.__amperes_per_nanosecond

    
    @property
    def milliamperes_per_second(self) -> float:
        """
        
        """
        if self.__milliamperes_per_second != None:
            return self.__milliamperes_per_second
        self.__milliamperes_per_second = self.__convert_from_base(ElectricCurrentGradientUnits.MilliamperePerSecond)
        return self.__milliamperes_per_second

    
    @property
    def milliamperes_per_minute(self) -> float:
        """
        
        """
        if self.__milliamperes_per_minute != None:
            return self.__milliamperes_per_minute
        self.__milliamperes_per_minute = self.__convert_from_base(ElectricCurrentGradientUnits.MilliamperePerMinute)
        return self.__milliamperes_per_minute

    
    def to_string(self, unit: ElectricCurrentGradientUnits = ElectricCurrentGradientUnits.AmperePerSecond, fractional_digits: int = None) -> str:
        """
        Format the ElectricCurrentGradient to a string.
        
        Note: the default format for ElectricCurrentGradient is AmperePerSecond.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the ElectricCurrentGradient. Default is 'AmperePerSecond'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == ElectricCurrentGradientUnits.AmperePerSecond:
            return f"""{super()._truncate_fraction_digits(self.amperes_per_second, fractional_digits)} A/s"""
        
        if unit == ElectricCurrentGradientUnits.AmperePerMinute:
            return f"""{super()._truncate_fraction_digits(self.amperes_per_minute, fractional_digits)} A/min"""
        
        if unit == ElectricCurrentGradientUnits.AmperePerMillisecond:
            return f"""{super()._truncate_fraction_digits(self.amperes_per_millisecond, fractional_digits)} A/ms"""
        
        if unit == ElectricCurrentGradientUnits.AmperePerMicrosecond:
            return f"""{super()._truncate_fraction_digits(self.amperes_per_microsecond, fractional_digits)} A/μs"""
        
        if unit == ElectricCurrentGradientUnits.AmperePerNanosecond:
            return f"""{super()._truncate_fraction_digits(self.amperes_per_nanosecond, fractional_digits)} A/ns"""
        
        if unit == ElectricCurrentGradientUnits.MilliamperePerSecond:
            return f"""{super()._truncate_fraction_digits(self.milliamperes_per_second, fractional_digits)} mA/s"""
        
        if unit == ElectricCurrentGradientUnits.MilliamperePerMinute:
            return f"""{super()._truncate_fraction_digits(self.milliamperes_per_minute, fractional_digits)} mA/min"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: ElectricCurrentGradientUnits = ElectricCurrentGradientUnits.AmperePerSecond) -> str:
        """
        Get ElectricCurrentGradient unit abbreviation.
        Note! the default abbreviation for ElectricCurrentGradient is AmperePerSecond.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == ElectricCurrentGradientUnits.AmperePerSecond:
            return """A/s"""
        
        if unit_abbreviation == ElectricCurrentGradientUnits.AmperePerMinute:
            return """A/min"""
        
        if unit_abbreviation == ElectricCurrentGradientUnits.AmperePerMillisecond:
            return """A/ms"""
        
        if unit_abbreviation == ElectricCurrentGradientUnits.AmperePerMicrosecond:
            return """A/μs"""
        
        if unit_abbreviation == ElectricCurrentGradientUnits.AmperePerNanosecond:
            return """A/ns"""
        
        if unit_abbreviation == ElectricCurrentGradientUnits.MilliamperePerSecond:
            return """mA/s"""
        
        if unit_abbreviation == ElectricCurrentGradientUnits.MilliamperePerMinute:
            return """mA/min"""
        
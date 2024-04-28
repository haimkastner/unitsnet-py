from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class StandardVolumeFlowUnits(Enum):
        """
            StandardVolumeFlowUnits enumeration
        """
        
        StandardCubicMeterPerSecond = 'StandardCubicMeterPerSecond'
        """
            
        """
        
        StandardCubicMeterPerMinute = 'StandardCubicMeterPerMinute'
        """
            
        """
        
        StandardCubicMeterPerHour = 'StandardCubicMeterPerHour'
        """
            
        """
        
        StandardCubicMeterPerDay = 'StandardCubicMeterPerDay'
        """
            
        """
        
        StandardCubicCentimeterPerMinute = 'StandardCubicCentimeterPerMinute'
        """
            
        """
        
        StandardLiterPerMinute = 'StandardLiterPerMinute'
        """
            
        """
        
        StandardCubicFootPerSecond = 'StandardCubicFootPerSecond'
        """
            
        """
        
        StandardCubicFootPerMinute = 'StandardCubicFootPerMinute'
        """
            
        """
        
        StandardCubicFootPerHour = 'StandardCubicFootPerHour'
        """
            
        """
        

class StandardVolumeFlowDto:
    """
    A DTO representation of a StandardVolumeFlow

    Attributes:
        value (float): The value of the StandardVolumeFlow.
        unit (StandardVolumeFlowUnits): The specific unit that the StandardVolumeFlow value is representing.
    """

    def __init__(self, value: float, unit: StandardVolumeFlowUnits):
        """
        Create a new DTO representation of a StandardVolumeFlow

        Parameters:
            value (float): The value of the StandardVolumeFlow.
            unit (StandardVolumeFlowUnits): The specific unit that the StandardVolumeFlow value is representing.
        """
        self.value: float = value
        """
        The value of the StandardVolumeFlow
        """
        self.unit: StandardVolumeFlowUnits = unit
        """
        The specific unit that the StandardVolumeFlow value is representing
        """

    def to_json(self):
        """
        Get a StandardVolumeFlow DTO JSON object representing the current unit.

        :return: JSON object represents StandardVolumeFlow DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "StandardCubicMeterPerSecond"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of StandardVolumeFlow DTO from a json representation.

        :param data: The StandardVolumeFlow DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "StandardCubicMeterPerSecond"}
        :return: A new instance of StandardVolumeFlowDto.
        :rtype: StandardVolumeFlowDto
        """
        return StandardVolumeFlowDto(value=data["value"], unit=StandardVolumeFlowUnits(data["unit"]))


class StandardVolumeFlow(AbstractMeasure):
    """
    The molar flow rate of a gas corrected to standardized conditions of temperature and pressure thus representing a fixed number of moles of gas regardless of composition and actual flow conditions.

    Args:
        value (float): The value.
        from_unit (StandardVolumeFlowUnits): The StandardVolumeFlow unit to create from, The default unit is StandardCubicMeterPerSecond
    """
    def __init__(self, value: float, from_unit: StandardVolumeFlowUnits = StandardVolumeFlowUnits.StandardCubicMeterPerSecond):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__standard_cubic_meters_per_second = None
        
        self.__standard_cubic_meters_per_minute = None
        
        self.__standard_cubic_meters_per_hour = None
        
        self.__standard_cubic_meters_per_day = None
        
        self.__standard_cubic_centimeters_per_minute = None
        
        self.__standard_liters_per_minute = None
        
        self.__standard_cubic_feet_per_second = None
        
        self.__standard_cubic_feet_per_minute = None
        
        self.__standard_cubic_feet_per_hour = None
        

    def convert(self, unit: StandardVolumeFlowUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: StandardVolumeFlowUnits = StandardVolumeFlowUnits.StandardCubicMeterPerSecond) -> StandardVolumeFlowDto:
        """
        Get a new instance of StandardVolumeFlow DTO representing the current unit.

        :param hold_in_unit: The specific StandardVolumeFlow unit to store the StandardVolumeFlow value in the DTO representation.
        :type hold_in_unit: StandardVolumeFlowUnits
        :return: A new instance of StandardVolumeFlowDto.
        :rtype: StandardVolumeFlowDto
        """
        return StandardVolumeFlowDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: StandardVolumeFlowUnits = StandardVolumeFlowUnits.StandardCubicMeterPerSecond):
        """
        Get a StandardVolumeFlow DTO JSON object representing the current unit.

        :param hold_in_unit: The specific StandardVolumeFlow unit to store the StandardVolumeFlow value in the DTO representation.
        :type hold_in_unit: StandardVolumeFlowUnits
        :return: JSON object represents StandardVolumeFlow DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "StandardCubicMeterPerSecond"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(standard_volume_flow_dto: StandardVolumeFlowDto):
        """
        Obtain a new instance of StandardVolumeFlow from a DTO unit object.

        :param standard_volume_flow_dto: The StandardVolumeFlow DTO representation.
        :type standard_volume_flow_dto: StandardVolumeFlowDto
        :return: A new instance of StandardVolumeFlow.
        :rtype: StandardVolumeFlow
        """
        return StandardVolumeFlow(standard_volume_flow_dto.value, standard_volume_flow_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of StandardVolumeFlow from a DTO unit json representation.

        :param data: The StandardVolumeFlow DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "StandardCubicMeterPerSecond"}
        :return: A new instance of StandardVolumeFlow.
        :rtype: StandardVolumeFlow
        """
        return StandardVolumeFlow.from_dto(StandardVolumeFlowDto.from_json(data))

    def __convert_from_base(self, from_unit: StandardVolumeFlowUnits) -> float:
        value = self._value
        
        if from_unit == StandardVolumeFlowUnits.StandardCubicMeterPerSecond:
            return (value)
        
        if from_unit == StandardVolumeFlowUnits.StandardCubicMeterPerMinute:
            return (value * 60)
        
        if from_unit == StandardVolumeFlowUnits.StandardCubicMeterPerHour:
            return (value * 3600)
        
        if from_unit == StandardVolumeFlowUnits.StandardCubicMeterPerDay:
            return (value * 86400)
        
        if from_unit == StandardVolumeFlowUnits.StandardCubicCentimeterPerMinute:
            return (value * 6e7)
        
        if from_unit == StandardVolumeFlowUnits.StandardLiterPerMinute:
            return (value * 60000)
        
        if from_unit == StandardVolumeFlowUnits.StandardCubicFootPerSecond:
            return (value * 35.314666721)
        
        if from_unit == StandardVolumeFlowUnits.StandardCubicFootPerMinute:
            return (value * 2118.88000326)
        
        if from_unit == StandardVolumeFlowUnits.StandardCubicFootPerHour:
            return (value / 7.8657907199999087346816086183876e-6)
        
        return None


    def __convert_to_base(self, value: float, to_unit: StandardVolumeFlowUnits) -> float:
        
        if to_unit == StandardVolumeFlowUnits.StandardCubicMeterPerSecond:
            return (value)
        
        if to_unit == StandardVolumeFlowUnits.StandardCubicMeterPerMinute:
            return (value / 60)
        
        if to_unit == StandardVolumeFlowUnits.StandardCubicMeterPerHour:
            return (value / 3600)
        
        if to_unit == StandardVolumeFlowUnits.StandardCubicMeterPerDay:
            return (value / 86400)
        
        if to_unit == StandardVolumeFlowUnits.StandardCubicCentimeterPerMinute:
            return (value / 6e7)
        
        if to_unit == StandardVolumeFlowUnits.StandardLiterPerMinute:
            return (value / 60000)
        
        if to_unit == StandardVolumeFlowUnits.StandardCubicFootPerSecond:
            return (value / 35.314666721)
        
        if to_unit == StandardVolumeFlowUnits.StandardCubicFootPerMinute:
            return (value / 2118.88000326)
        
        if to_unit == StandardVolumeFlowUnits.StandardCubicFootPerHour:
            return (value * 7.8657907199999087346816086183876e-6)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_standard_cubic_meters_per_second(standard_cubic_meters_per_second: float):
        """
        Create a new instance of StandardVolumeFlow from a value in standard_cubic_meters_per_second.

        

        :param meters: The StandardVolumeFlow value in standard_cubic_meters_per_second.
        :type standard_cubic_meters_per_second: float
        :return: A new instance of StandardVolumeFlow.
        :rtype: StandardVolumeFlow
        """
        return StandardVolumeFlow(standard_cubic_meters_per_second, StandardVolumeFlowUnits.StandardCubicMeterPerSecond)

    
    @staticmethod
    def from_standard_cubic_meters_per_minute(standard_cubic_meters_per_minute: float):
        """
        Create a new instance of StandardVolumeFlow from a value in standard_cubic_meters_per_minute.

        

        :param meters: The StandardVolumeFlow value in standard_cubic_meters_per_minute.
        :type standard_cubic_meters_per_minute: float
        :return: A new instance of StandardVolumeFlow.
        :rtype: StandardVolumeFlow
        """
        return StandardVolumeFlow(standard_cubic_meters_per_minute, StandardVolumeFlowUnits.StandardCubicMeterPerMinute)

    
    @staticmethod
    def from_standard_cubic_meters_per_hour(standard_cubic_meters_per_hour: float):
        """
        Create a new instance of StandardVolumeFlow from a value in standard_cubic_meters_per_hour.

        

        :param meters: The StandardVolumeFlow value in standard_cubic_meters_per_hour.
        :type standard_cubic_meters_per_hour: float
        :return: A new instance of StandardVolumeFlow.
        :rtype: StandardVolumeFlow
        """
        return StandardVolumeFlow(standard_cubic_meters_per_hour, StandardVolumeFlowUnits.StandardCubicMeterPerHour)

    
    @staticmethod
    def from_standard_cubic_meters_per_day(standard_cubic_meters_per_day: float):
        """
        Create a new instance of StandardVolumeFlow from a value in standard_cubic_meters_per_day.

        

        :param meters: The StandardVolumeFlow value in standard_cubic_meters_per_day.
        :type standard_cubic_meters_per_day: float
        :return: A new instance of StandardVolumeFlow.
        :rtype: StandardVolumeFlow
        """
        return StandardVolumeFlow(standard_cubic_meters_per_day, StandardVolumeFlowUnits.StandardCubicMeterPerDay)

    
    @staticmethod
    def from_standard_cubic_centimeters_per_minute(standard_cubic_centimeters_per_minute: float):
        """
        Create a new instance of StandardVolumeFlow from a value in standard_cubic_centimeters_per_minute.

        

        :param meters: The StandardVolumeFlow value in standard_cubic_centimeters_per_minute.
        :type standard_cubic_centimeters_per_minute: float
        :return: A new instance of StandardVolumeFlow.
        :rtype: StandardVolumeFlow
        """
        return StandardVolumeFlow(standard_cubic_centimeters_per_minute, StandardVolumeFlowUnits.StandardCubicCentimeterPerMinute)

    
    @staticmethod
    def from_standard_liters_per_minute(standard_liters_per_minute: float):
        """
        Create a new instance of StandardVolumeFlow from a value in standard_liters_per_minute.

        

        :param meters: The StandardVolumeFlow value in standard_liters_per_minute.
        :type standard_liters_per_minute: float
        :return: A new instance of StandardVolumeFlow.
        :rtype: StandardVolumeFlow
        """
        return StandardVolumeFlow(standard_liters_per_minute, StandardVolumeFlowUnits.StandardLiterPerMinute)

    
    @staticmethod
    def from_standard_cubic_feet_per_second(standard_cubic_feet_per_second: float):
        """
        Create a new instance of StandardVolumeFlow from a value in standard_cubic_feet_per_second.

        

        :param meters: The StandardVolumeFlow value in standard_cubic_feet_per_second.
        :type standard_cubic_feet_per_second: float
        :return: A new instance of StandardVolumeFlow.
        :rtype: StandardVolumeFlow
        """
        return StandardVolumeFlow(standard_cubic_feet_per_second, StandardVolumeFlowUnits.StandardCubicFootPerSecond)

    
    @staticmethod
    def from_standard_cubic_feet_per_minute(standard_cubic_feet_per_minute: float):
        """
        Create a new instance of StandardVolumeFlow from a value in standard_cubic_feet_per_minute.

        

        :param meters: The StandardVolumeFlow value in standard_cubic_feet_per_minute.
        :type standard_cubic_feet_per_minute: float
        :return: A new instance of StandardVolumeFlow.
        :rtype: StandardVolumeFlow
        """
        return StandardVolumeFlow(standard_cubic_feet_per_minute, StandardVolumeFlowUnits.StandardCubicFootPerMinute)

    
    @staticmethod
    def from_standard_cubic_feet_per_hour(standard_cubic_feet_per_hour: float):
        """
        Create a new instance of StandardVolumeFlow from a value in standard_cubic_feet_per_hour.

        

        :param meters: The StandardVolumeFlow value in standard_cubic_feet_per_hour.
        :type standard_cubic_feet_per_hour: float
        :return: A new instance of StandardVolumeFlow.
        :rtype: StandardVolumeFlow
        """
        return StandardVolumeFlow(standard_cubic_feet_per_hour, StandardVolumeFlowUnits.StandardCubicFootPerHour)

    
    @property
    def standard_cubic_meters_per_second(self) -> float:
        """
        
        """
        if self.__standard_cubic_meters_per_second != None:
            return self.__standard_cubic_meters_per_second
        self.__standard_cubic_meters_per_second = self.__convert_from_base(StandardVolumeFlowUnits.StandardCubicMeterPerSecond)
        return self.__standard_cubic_meters_per_second

    
    @property
    def standard_cubic_meters_per_minute(self) -> float:
        """
        
        """
        if self.__standard_cubic_meters_per_minute != None:
            return self.__standard_cubic_meters_per_minute
        self.__standard_cubic_meters_per_minute = self.__convert_from_base(StandardVolumeFlowUnits.StandardCubicMeterPerMinute)
        return self.__standard_cubic_meters_per_minute

    
    @property
    def standard_cubic_meters_per_hour(self) -> float:
        """
        
        """
        if self.__standard_cubic_meters_per_hour != None:
            return self.__standard_cubic_meters_per_hour
        self.__standard_cubic_meters_per_hour = self.__convert_from_base(StandardVolumeFlowUnits.StandardCubicMeterPerHour)
        return self.__standard_cubic_meters_per_hour

    
    @property
    def standard_cubic_meters_per_day(self) -> float:
        """
        
        """
        if self.__standard_cubic_meters_per_day != None:
            return self.__standard_cubic_meters_per_day
        self.__standard_cubic_meters_per_day = self.__convert_from_base(StandardVolumeFlowUnits.StandardCubicMeterPerDay)
        return self.__standard_cubic_meters_per_day

    
    @property
    def standard_cubic_centimeters_per_minute(self) -> float:
        """
        
        """
        if self.__standard_cubic_centimeters_per_minute != None:
            return self.__standard_cubic_centimeters_per_minute
        self.__standard_cubic_centimeters_per_minute = self.__convert_from_base(StandardVolumeFlowUnits.StandardCubicCentimeterPerMinute)
        return self.__standard_cubic_centimeters_per_minute

    
    @property
    def standard_liters_per_minute(self) -> float:
        """
        
        """
        if self.__standard_liters_per_minute != None:
            return self.__standard_liters_per_minute
        self.__standard_liters_per_minute = self.__convert_from_base(StandardVolumeFlowUnits.StandardLiterPerMinute)
        return self.__standard_liters_per_minute

    
    @property
    def standard_cubic_feet_per_second(self) -> float:
        """
        
        """
        if self.__standard_cubic_feet_per_second != None:
            return self.__standard_cubic_feet_per_second
        self.__standard_cubic_feet_per_second = self.__convert_from_base(StandardVolumeFlowUnits.StandardCubicFootPerSecond)
        return self.__standard_cubic_feet_per_second

    
    @property
    def standard_cubic_feet_per_minute(self) -> float:
        """
        
        """
        if self.__standard_cubic_feet_per_minute != None:
            return self.__standard_cubic_feet_per_minute
        self.__standard_cubic_feet_per_minute = self.__convert_from_base(StandardVolumeFlowUnits.StandardCubicFootPerMinute)
        return self.__standard_cubic_feet_per_minute

    
    @property
    def standard_cubic_feet_per_hour(self) -> float:
        """
        
        """
        if self.__standard_cubic_feet_per_hour != None:
            return self.__standard_cubic_feet_per_hour
        self.__standard_cubic_feet_per_hour = self.__convert_from_base(StandardVolumeFlowUnits.StandardCubicFootPerHour)
        return self.__standard_cubic_feet_per_hour

    
    def to_string(self, unit: StandardVolumeFlowUnits = StandardVolumeFlowUnits.StandardCubicMeterPerSecond, fractional_digits: int = None) -> str:
        """
        Format the StandardVolumeFlow to a string.
        
        Note: the default format for StandardVolumeFlow is StandardCubicMeterPerSecond.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the StandardVolumeFlow. Default is 'StandardCubicMeterPerSecond'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == StandardVolumeFlowUnits.StandardCubicMeterPerSecond:
            return f"""{super()._truncate_fraction_digits(self.standard_cubic_meters_per_second, fractional_digits)} Sm³/s"""
        
        if unit == StandardVolumeFlowUnits.StandardCubicMeterPerMinute:
            return f"""{super()._truncate_fraction_digits(self.standard_cubic_meters_per_minute, fractional_digits)} Sm³/min"""
        
        if unit == StandardVolumeFlowUnits.StandardCubicMeterPerHour:
            return f"""{super()._truncate_fraction_digits(self.standard_cubic_meters_per_hour, fractional_digits)} Sm³/h"""
        
        if unit == StandardVolumeFlowUnits.StandardCubicMeterPerDay:
            return f"""{super()._truncate_fraction_digits(self.standard_cubic_meters_per_day, fractional_digits)} Sm³/d"""
        
        if unit == StandardVolumeFlowUnits.StandardCubicCentimeterPerMinute:
            return f"""{super()._truncate_fraction_digits(self.standard_cubic_centimeters_per_minute, fractional_digits)} sccm"""
        
        if unit == StandardVolumeFlowUnits.StandardLiterPerMinute:
            return f"""{super()._truncate_fraction_digits(self.standard_liters_per_minute, fractional_digits)} slm"""
        
        if unit == StandardVolumeFlowUnits.StandardCubicFootPerSecond:
            return f"""{super()._truncate_fraction_digits(self.standard_cubic_feet_per_second, fractional_digits)} Sft³/s"""
        
        if unit == StandardVolumeFlowUnits.StandardCubicFootPerMinute:
            return f"""{super()._truncate_fraction_digits(self.standard_cubic_feet_per_minute, fractional_digits)} scfm"""
        
        if unit == StandardVolumeFlowUnits.StandardCubicFootPerHour:
            return f"""{super()._truncate_fraction_digits(self.standard_cubic_feet_per_hour, fractional_digits)} scfh"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: StandardVolumeFlowUnits = StandardVolumeFlowUnits.StandardCubicMeterPerSecond) -> str:
        """
        Get StandardVolumeFlow unit abbreviation.
        Note! the default abbreviation for StandardVolumeFlow is StandardCubicMeterPerSecond.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == StandardVolumeFlowUnits.StandardCubicMeterPerSecond:
            return """Sm³/s"""
        
        if unit_abbreviation == StandardVolumeFlowUnits.StandardCubicMeterPerMinute:
            return """Sm³/min"""
        
        if unit_abbreviation == StandardVolumeFlowUnits.StandardCubicMeterPerHour:
            return """Sm³/h"""
        
        if unit_abbreviation == StandardVolumeFlowUnits.StandardCubicMeterPerDay:
            return """Sm³/d"""
        
        if unit_abbreviation == StandardVolumeFlowUnits.StandardCubicCentimeterPerMinute:
            return """sccm"""
        
        if unit_abbreviation == StandardVolumeFlowUnits.StandardLiterPerMinute:
            return """slm"""
        
        if unit_abbreviation == StandardVolumeFlowUnits.StandardCubicFootPerSecond:
            return """Sft³/s"""
        
        if unit_abbreviation == StandardVolumeFlowUnits.StandardCubicFootPerMinute:
            return """scfm"""
        
        if unit_abbreviation == StandardVolumeFlowUnits.StandardCubicFootPerHour:
            return """scfh"""
        
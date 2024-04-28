from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class RotationalAccelerationUnits(Enum):
        """
            RotationalAccelerationUnits enumeration
        """
        
        RadianPerSecondSquared = 'RadianPerSecondSquared'
        """
            
        """
        
        DegreePerSecondSquared = 'DegreePerSecondSquared'
        """
            
        """
        
        RevolutionPerMinutePerSecond = 'RevolutionPerMinutePerSecond'
        """
            
        """
        
        RevolutionPerSecondSquared = 'RevolutionPerSecondSquared'
        """
            
        """
        

class RotationalAccelerationDto:
    """
    A DTO representation of a RotationalAcceleration

    Attributes:
        value (float): The value of the RotationalAcceleration.
        unit (RotationalAccelerationUnits): The specific unit that the RotationalAcceleration value is representing.
    """

    def __init__(self, value: float, unit: RotationalAccelerationUnits):
        """
        Create a new DTO representation of a RotationalAcceleration

        Parameters:
            value (float): The value of the RotationalAcceleration.
            unit (RotationalAccelerationUnits): The specific unit that the RotationalAcceleration value is representing.
        """
        self.value: float = value
        """
        The value of the RotationalAcceleration
        """
        self.unit: RotationalAccelerationUnits = unit
        """
        The specific unit that the RotationalAcceleration value is representing
        """

    def to_json(self):
        """
        Get a RotationalAcceleration DTO JSON object representing the current unit.

        :return: JSON object represents RotationalAcceleration DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "RadianPerSecondSquared"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of RotationalAcceleration DTO from a json representation.

        :param data: The RotationalAcceleration DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "RadianPerSecondSquared"}
        :return: A new instance of RotationalAccelerationDto.
        :rtype: RotationalAccelerationDto
        """
        return RotationalAccelerationDto(value=data["value"], unit=RotationalAccelerationUnits(data["unit"]))


class RotationalAcceleration(AbstractMeasure):
    """
    Angular acceleration is the rate of change of rotational speed.

    Args:
        value (float): The value.
        from_unit (RotationalAccelerationUnits): The RotationalAcceleration unit to create from, The default unit is RadianPerSecondSquared
    """
    def __init__(self, value: float, from_unit: RotationalAccelerationUnits = RotationalAccelerationUnits.RadianPerSecondSquared):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__radians_per_second_squared = None
        
        self.__degrees_per_second_squared = None
        
        self.__revolutions_per_minute_per_second = None
        
        self.__revolutions_per_second_squared = None
        

    def convert(self, unit: RotationalAccelerationUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: RotationalAccelerationUnits = RotationalAccelerationUnits.RadianPerSecondSquared) -> RotationalAccelerationDto:
        """
        Get a new instance of RotationalAcceleration DTO representing the current unit.

        :param hold_in_unit: The specific RotationalAcceleration unit to store the RotationalAcceleration value in the DTO representation.
        :type hold_in_unit: RotationalAccelerationUnits
        :return: A new instance of RotationalAccelerationDto.
        :rtype: RotationalAccelerationDto
        """
        return RotationalAccelerationDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: RotationalAccelerationUnits = RotationalAccelerationUnits.RadianPerSecondSquared):
        """
        Get a RotationalAcceleration DTO JSON object representing the current unit.

        :param hold_in_unit: The specific RotationalAcceleration unit to store the RotationalAcceleration value in the DTO representation.
        :type hold_in_unit: RotationalAccelerationUnits
        :return: JSON object represents RotationalAcceleration DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "RadianPerSecondSquared"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(rotational_acceleration_dto: RotationalAccelerationDto):
        """
        Obtain a new instance of RotationalAcceleration from a DTO unit object.

        :param rotational_acceleration_dto: The RotationalAcceleration DTO representation.
        :type rotational_acceleration_dto: RotationalAccelerationDto
        :return: A new instance of RotationalAcceleration.
        :rtype: RotationalAcceleration
        """
        return RotationalAcceleration(rotational_acceleration_dto.value, rotational_acceleration_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of RotationalAcceleration from a DTO unit json representation.

        :param data: The RotationalAcceleration DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "RadianPerSecondSquared"}
        :return: A new instance of RotationalAcceleration.
        :rtype: RotationalAcceleration
        """
        return RotationalAcceleration.from_dto(RotationalAccelerationDto.from_json(data))

    def __convert_from_base(self, from_unit: RotationalAccelerationUnits) -> float:
        value = self._value
        
        if from_unit == RotationalAccelerationUnits.RadianPerSecondSquared:
            return (value)
        
        if from_unit == RotationalAccelerationUnits.DegreePerSecondSquared:
            return ((180 / math.pi) * value)
        
        if from_unit == RotationalAccelerationUnits.RevolutionPerMinutePerSecond:
            return ((60 / (2 * math.pi)) * value)
        
        if from_unit == RotationalAccelerationUnits.RevolutionPerSecondSquared:
            return ((1 / (2 * math.pi)) * value)
        
        return None


    def __convert_to_base(self, value: float, to_unit: RotationalAccelerationUnits) -> float:
        
        if to_unit == RotationalAccelerationUnits.RadianPerSecondSquared:
            return (value)
        
        if to_unit == RotationalAccelerationUnits.DegreePerSecondSquared:
            return ((math.pi / 180) * value)
        
        if to_unit == RotationalAccelerationUnits.RevolutionPerMinutePerSecond:
            return (((2 * math.pi) / 60) * value)
        
        if to_unit == RotationalAccelerationUnits.RevolutionPerSecondSquared:
            return ((2 * math.pi) * value)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_radians_per_second_squared(radians_per_second_squared: float):
        """
        Create a new instance of RotationalAcceleration from a value in radians_per_second_squared.

        

        :param meters: The RotationalAcceleration value in radians_per_second_squared.
        :type radians_per_second_squared: float
        :return: A new instance of RotationalAcceleration.
        :rtype: RotationalAcceleration
        """
        return RotationalAcceleration(radians_per_second_squared, RotationalAccelerationUnits.RadianPerSecondSquared)

    
    @staticmethod
    def from_degrees_per_second_squared(degrees_per_second_squared: float):
        """
        Create a new instance of RotationalAcceleration from a value in degrees_per_second_squared.

        

        :param meters: The RotationalAcceleration value in degrees_per_second_squared.
        :type degrees_per_second_squared: float
        :return: A new instance of RotationalAcceleration.
        :rtype: RotationalAcceleration
        """
        return RotationalAcceleration(degrees_per_second_squared, RotationalAccelerationUnits.DegreePerSecondSquared)

    
    @staticmethod
    def from_revolutions_per_minute_per_second(revolutions_per_minute_per_second: float):
        """
        Create a new instance of RotationalAcceleration from a value in revolutions_per_minute_per_second.

        

        :param meters: The RotationalAcceleration value in revolutions_per_minute_per_second.
        :type revolutions_per_minute_per_second: float
        :return: A new instance of RotationalAcceleration.
        :rtype: RotationalAcceleration
        """
        return RotationalAcceleration(revolutions_per_minute_per_second, RotationalAccelerationUnits.RevolutionPerMinutePerSecond)

    
    @staticmethod
    def from_revolutions_per_second_squared(revolutions_per_second_squared: float):
        """
        Create a new instance of RotationalAcceleration from a value in revolutions_per_second_squared.

        

        :param meters: The RotationalAcceleration value in revolutions_per_second_squared.
        :type revolutions_per_second_squared: float
        :return: A new instance of RotationalAcceleration.
        :rtype: RotationalAcceleration
        """
        return RotationalAcceleration(revolutions_per_second_squared, RotationalAccelerationUnits.RevolutionPerSecondSquared)

    
    @property
    def radians_per_second_squared(self) -> float:
        """
        
        """
        if self.__radians_per_second_squared != None:
            return self.__radians_per_second_squared
        self.__radians_per_second_squared = self.__convert_from_base(RotationalAccelerationUnits.RadianPerSecondSquared)
        return self.__radians_per_second_squared

    
    @property
    def degrees_per_second_squared(self) -> float:
        """
        
        """
        if self.__degrees_per_second_squared != None:
            return self.__degrees_per_second_squared
        self.__degrees_per_second_squared = self.__convert_from_base(RotationalAccelerationUnits.DegreePerSecondSquared)
        return self.__degrees_per_second_squared

    
    @property
    def revolutions_per_minute_per_second(self) -> float:
        """
        
        """
        if self.__revolutions_per_minute_per_second != None:
            return self.__revolutions_per_minute_per_second
        self.__revolutions_per_minute_per_second = self.__convert_from_base(RotationalAccelerationUnits.RevolutionPerMinutePerSecond)
        return self.__revolutions_per_minute_per_second

    
    @property
    def revolutions_per_second_squared(self) -> float:
        """
        
        """
        if self.__revolutions_per_second_squared != None:
            return self.__revolutions_per_second_squared
        self.__revolutions_per_second_squared = self.__convert_from_base(RotationalAccelerationUnits.RevolutionPerSecondSquared)
        return self.__revolutions_per_second_squared

    
    def to_string(self, unit: RotationalAccelerationUnits = RotationalAccelerationUnits.RadianPerSecondSquared, fractional_digits: int = None) -> str:
        """
        Format the RotationalAcceleration to a string.
        
        Note: the default format for RotationalAcceleration is RadianPerSecondSquared.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the RotationalAcceleration. Default is 'RadianPerSecondSquared'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == RotationalAccelerationUnits.RadianPerSecondSquared:
            return f"""{super()._truncate_fraction_digits(self.radians_per_second_squared, fractional_digits)} rad/s²"""
        
        if unit == RotationalAccelerationUnits.DegreePerSecondSquared:
            return f"""{super()._truncate_fraction_digits(self.degrees_per_second_squared, fractional_digits)} °/s²"""
        
        if unit == RotationalAccelerationUnits.RevolutionPerMinutePerSecond:
            return f"""{super()._truncate_fraction_digits(self.revolutions_per_minute_per_second, fractional_digits)} rpm/s"""
        
        if unit == RotationalAccelerationUnits.RevolutionPerSecondSquared:
            return f"""{super()._truncate_fraction_digits(self.revolutions_per_second_squared, fractional_digits)} r/s²"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: RotationalAccelerationUnits = RotationalAccelerationUnits.RadianPerSecondSquared) -> str:
        """
        Get RotationalAcceleration unit abbreviation.
        Note! the default abbreviation for RotationalAcceleration is RadianPerSecondSquared.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == RotationalAccelerationUnits.RadianPerSecondSquared:
            return """rad/s²"""
        
        if unit_abbreviation == RotationalAccelerationUnits.DegreePerSecondSquared:
            return """°/s²"""
        
        if unit_abbreviation == RotationalAccelerationUnits.RevolutionPerMinutePerSecond:
            return """rpm/s"""
        
        if unit_abbreviation == RotationalAccelerationUnits.RevolutionPerSecondSquared:
            return """r/s²"""
        
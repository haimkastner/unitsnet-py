from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class RotationalAccelerationUnits(Enum):
        """
            RotationalAccelerationUnits enumeration
        """
        
        RadianPerSecondSquared = 'radian_per_second_squared'
        """
            
        """
        
        DegreePerSecondSquared = 'degree_per_second_squared'
        """
            
        """
        
        RevolutionPerMinutePerSecond = 'revolution_per_minute_per_second'
        """
            
        """
        
        RevolutionPerSecondSquared = 'revolution_per_second_squared'
        """
            
        """
        

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

    
    def to_string(self, unit: RotationalAccelerationUnits = RotationalAccelerationUnits.RadianPerSecondSquared) -> str:
        """
        Format the RotationalAcceleration to string.
        Note! the default format for RotationalAcceleration is RadianPerSecondSquared.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == RotationalAccelerationUnits.RadianPerSecondSquared:
            return f"""{self.radians_per_second_squared} rad/s²"""
        
        if unit == RotationalAccelerationUnits.DegreePerSecondSquared:
            return f"""{self.degrees_per_second_squared} °/s²"""
        
        if unit == RotationalAccelerationUnits.RevolutionPerMinutePerSecond:
            return f"""{self.revolutions_per_minute_per_second} rpm/s"""
        
        if unit == RotationalAccelerationUnits.RevolutionPerSecondSquared:
            return f"""{self.revolutions_per_second_squared} r/s²"""
        
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
        
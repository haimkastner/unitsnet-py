from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class TemperatureChangeRateUnits(Enum):
        """
            TemperatureChangeRateUnits enumeration
        """
        
        DegreeCelsiusPerSecond = 'degree_celsius_per_second'
        """
            
        """
        
        DegreeCelsiusPerMinute = 'degree_celsius_per_minute'
        """
            
        """
        
        NanodegreeCelsiusPerSecond = 'nanodegree_celsius_per_second'
        """
            
        """
        
        MicrodegreeCelsiusPerSecond = 'microdegree_celsius_per_second'
        """
            
        """
        
        MillidegreeCelsiusPerSecond = 'millidegree_celsius_per_second'
        """
            
        """
        
        CentidegreeCelsiusPerSecond = 'centidegree_celsius_per_second'
        """
            
        """
        
        DecidegreeCelsiusPerSecond = 'decidegree_celsius_per_second'
        """
            
        """
        
        DecadegreeCelsiusPerSecond = 'decadegree_celsius_per_second'
        """
            
        """
        
        HectodegreeCelsiusPerSecond = 'hectodegree_celsius_per_second'
        """
            
        """
        
        KilodegreeCelsiusPerSecond = 'kilodegree_celsius_per_second'
        """
            
        """
        

class TemperatureChangeRate(AbstractMeasure):
    """
    Temperature change rate is the ratio of the temperature change to the time during which the change occurred (value of temperature changes per unit time).

    Args:
        value (float): The value.
        from_unit (TemperatureChangeRateUnits): The TemperatureChangeRate unit to create from, The default unit is DegreeCelsiusPerSecond
    """
    def __init__(self, value: float, from_unit: TemperatureChangeRateUnits = TemperatureChangeRateUnits.DegreeCelsiusPerSecond):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__degrees_celsius_per_second = None
        
        self.__degrees_celsius_per_minute = None
        
        self.__nanodegrees_celsius_per_second = None
        
        self.__microdegrees_celsius_per_second = None
        
        self.__millidegrees_celsius_per_second = None
        
        self.__centidegrees_celsius_per_second = None
        
        self.__decidegrees_celsius_per_second = None
        
        self.__decadegrees_celsius_per_second = None
        
        self.__hectodegrees_celsius_per_second = None
        
        self.__kilodegrees_celsius_per_second = None
        

    def convert(self, unit: TemperatureChangeRateUnits) -> float:
        return self.__convert_from_base(unit)

    def __convert_from_base(self, from_unit: TemperatureChangeRateUnits) -> float:
        value = self._value
        
        if from_unit == TemperatureChangeRateUnits.DegreeCelsiusPerSecond:
            return (value)
        
        if from_unit == TemperatureChangeRateUnits.DegreeCelsiusPerMinute:
            return (value * 60)
        
        if from_unit == TemperatureChangeRateUnits.NanodegreeCelsiusPerSecond:
            return ((value) / 1e-09)
        
        if from_unit == TemperatureChangeRateUnits.MicrodegreeCelsiusPerSecond:
            return ((value) / 1e-06)
        
        if from_unit == TemperatureChangeRateUnits.MillidegreeCelsiusPerSecond:
            return ((value) / 0.001)
        
        if from_unit == TemperatureChangeRateUnits.CentidegreeCelsiusPerSecond:
            return ((value) / 0.01)
        
        if from_unit == TemperatureChangeRateUnits.DecidegreeCelsiusPerSecond:
            return ((value) / 0.1)
        
        if from_unit == TemperatureChangeRateUnits.DecadegreeCelsiusPerSecond:
            return ((value) / 10.0)
        
        if from_unit == TemperatureChangeRateUnits.HectodegreeCelsiusPerSecond:
            return ((value) / 100.0)
        
        if from_unit == TemperatureChangeRateUnits.KilodegreeCelsiusPerSecond:
            return ((value) / 1000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: TemperatureChangeRateUnits) -> float:
        
        if to_unit == TemperatureChangeRateUnits.DegreeCelsiusPerSecond:
            return (value)
        
        if to_unit == TemperatureChangeRateUnits.DegreeCelsiusPerMinute:
            return (value / 60)
        
        if to_unit == TemperatureChangeRateUnits.NanodegreeCelsiusPerSecond:
            return ((value) * 1e-09)
        
        if to_unit == TemperatureChangeRateUnits.MicrodegreeCelsiusPerSecond:
            return ((value) * 1e-06)
        
        if to_unit == TemperatureChangeRateUnits.MillidegreeCelsiusPerSecond:
            return ((value) * 0.001)
        
        if to_unit == TemperatureChangeRateUnits.CentidegreeCelsiusPerSecond:
            return ((value) * 0.01)
        
        if to_unit == TemperatureChangeRateUnits.DecidegreeCelsiusPerSecond:
            return ((value) * 0.1)
        
        if to_unit == TemperatureChangeRateUnits.DecadegreeCelsiusPerSecond:
            return ((value) * 10.0)
        
        if to_unit == TemperatureChangeRateUnits.HectodegreeCelsiusPerSecond:
            return ((value) * 100.0)
        
        if to_unit == TemperatureChangeRateUnits.KilodegreeCelsiusPerSecond:
            return ((value) * 1000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_degrees_celsius_per_second(degrees_celsius_per_second: float):
        """
        Create a new instance of TemperatureChangeRate from a value in degrees_celsius_per_second.

        

        :param meters: The TemperatureChangeRate value in degrees_celsius_per_second.
        :type degrees_celsius_per_second: float
        :return: A new instance of TemperatureChangeRate.
        :rtype: TemperatureChangeRate
        """
        return TemperatureChangeRate(degrees_celsius_per_second, TemperatureChangeRateUnits.DegreeCelsiusPerSecond)

    
    @staticmethod
    def from_degrees_celsius_per_minute(degrees_celsius_per_minute: float):
        """
        Create a new instance of TemperatureChangeRate from a value in degrees_celsius_per_minute.

        

        :param meters: The TemperatureChangeRate value in degrees_celsius_per_minute.
        :type degrees_celsius_per_minute: float
        :return: A new instance of TemperatureChangeRate.
        :rtype: TemperatureChangeRate
        """
        return TemperatureChangeRate(degrees_celsius_per_minute, TemperatureChangeRateUnits.DegreeCelsiusPerMinute)

    
    @staticmethod
    def from_nanodegrees_celsius_per_second(nanodegrees_celsius_per_second: float):
        """
        Create a new instance of TemperatureChangeRate from a value in nanodegrees_celsius_per_second.

        

        :param meters: The TemperatureChangeRate value in nanodegrees_celsius_per_second.
        :type nanodegrees_celsius_per_second: float
        :return: A new instance of TemperatureChangeRate.
        :rtype: TemperatureChangeRate
        """
        return TemperatureChangeRate(nanodegrees_celsius_per_second, TemperatureChangeRateUnits.NanodegreeCelsiusPerSecond)

    
    @staticmethod
    def from_microdegrees_celsius_per_second(microdegrees_celsius_per_second: float):
        """
        Create a new instance of TemperatureChangeRate from a value in microdegrees_celsius_per_second.

        

        :param meters: The TemperatureChangeRate value in microdegrees_celsius_per_second.
        :type microdegrees_celsius_per_second: float
        :return: A new instance of TemperatureChangeRate.
        :rtype: TemperatureChangeRate
        """
        return TemperatureChangeRate(microdegrees_celsius_per_second, TemperatureChangeRateUnits.MicrodegreeCelsiusPerSecond)

    
    @staticmethod
    def from_millidegrees_celsius_per_second(millidegrees_celsius_per_second: float):
        """
        Create a new instance of TemperatureChangeRate from a value in millidegrees_celsius_per_second.

        

        :param meters: The TemperatureChangeRate value in millidegrees_celsius_per_second.
        :type millidegrees_celsius_per_second: float
        :return: A new instance of TemperatureChangeRate.
        :rtype: TemperatureChangeRate
        """
        return TemperatureChangeRate(millidegrees_celsius_per_second, TemperatureChangeRateUnits.MillidegreeCelsiusPerSecond)

    
    @staticmethod
    def from_centidegrees_celsius_per_second(centidegrees_celsius_per_second: float):
        """
        Create a new instance of TemperatureChangeRate from a value in centidegrees_celsius_per_second.

        

        :param meters: The TemperatureChangeRate value in centidegrees_celsius_per_second.
        :type centidegrees_celsius_per_second: float
        :return: A new instance of TemperatureChangeRate.
        :rtype: TemperatureChangeRate
        """
        return TemperatureChangeRate(centidegrees_celsius_per_second, TemperatureChangeRateUnits.CentidegreeCelsiusPerSecond)

    
    @staticmethod
    def from_decidegrees_celsius_per_second(decidegrees_celsius_per_second: float):
        """
        Create a new instance of TemperatureChangeRate from a value in decidegrees_celsius_per_second.

        

        :param meters: The TemperatureChangeRate value in decidegrees_celsius_per_second.
        :type decidegrees_celsius_per_second: float
        :return: A new instance of TemperatureChangeRate.
        :rtype: TemperatureChangeRate
        """
        return TemperatureChangeRate(decidegrees_celsius_per_second, TemperatureChangeRateUnits.DecidegreeCelsiusPerSecond)

    
    @staticmethod
    def from_decadegrees_celsius_per_second(decadegrees_celsius_per_second: float):
        """
        Create a new instance of TemperatureChangeRate from a value in decadegrees_celsius_per_second.

        

        :param meters: The TemperatureChangeRate value in decadegrees_celsius_per_second.
        :type decadegrees_celsius_per_second: float
        :return: A new instance of TemperatureChangeRate.
        :rtype: TemperatureChangeRate
        """
        return TemperatureChangeRate(decadegrees_celsius_per_second, TemperatureChangeRateUnits.DecadegreeCelsiusPerSecond)

    
    @staticmethod
    def from_hectodegrees_celsius_per_second(hectodegrees_celsius_per_second: float):
        """
        Create a new instance of TemperatureChangeRate from a value in hectodegrees_celsius_per_second.

        

        :param meters: The TemperatureChangeRate value in hectodegrees_celsius_per_second.
        :type hectodegrees_celsius_per_second: float
        :return: A new instance of TemperatureChangeRate.
        :rtype: TemperatureChangeRate
        """
        return TemperatureChangeRate(hectodegrees_celsius_per_second, TemperatureChangeRateUnits.HectodegreeCelsiusPerSecond)

    
    @staticmethod
    def from_kilodegrees_celsius_per_second(kilodegrees_celsius_per_second: float):
        """
        Create a new instance of TemperatureChangeRate from a value in kilodegrees_celsius_per_second.

        

        :param meters: The TemperatureChangeRate value in kilodegrees_celsius_per_second.
        :type kilodegrees_celsius_per_second: float
        :return: A new instance of TemperatureChangeRate.
        :rtype: TemperatureChangeRate
        """
        return TemperatureChangeRate(kilodegrees_celsius_per_second, TemperatureChangeRateUnits.KilodegreeCelsiusPerSecond)

    
    @property
    def degrees_celsius_per_second(self) -> float:
        """
        
        """
        if self.__degrees_celsius_per_second != None:
            return self.__degrees_celsius_per_second
        self.__degrees_celsius_per_second = self.__convert_from_base(TemperatureChangeRateUnits.DegreeCelsiusPerSecond)
        return self.__degrees_celsius_per_second

    
    @property
    def degrees_celsius_per_minute(self) -> float:
        """
        
        """
        if self.__degrees_celsius_per_minute != None:
            return self.__degrees_celsius_per_minute
        self.__degrees_celsius_per_minute = self.__convert_from_base(TemperatureChangeRateUnits.DegreeCelsiusPerMinute)
        return self.__degrees_celsius_per_minute

    
    @property
    def nanodegrees_celsius_per_second(self) -> float:
        """
        
        """
        if self.__nanodegrees_celsius_per_second != None:
            return self.__nanodegrees_celsius_per_second
        self.__nanodegrees_celsius_per_second = self.__convert_from_base(TemperatureChangeRateUnits.NanodegreeCelsiusPerSecond)
        return self.__nanodegrees_celsius_per_second

    
    @property
    def microdegrees_celsius_per_second(self) -> float:
        """
        
        """
        if self.__microdegrees_celsius_per_second != None:
            return self.__microdegrees_celsius_per_second
        self.__microdegrees_celsius_per_second = self.__convert_from_base(TemperatureChangeRateUnits.MicrodegreeCelsiusPerSecond)
        return self.__microdegrees_celsius_per_second

    
    @property
    def millidegrees_celsius_per_second(self) -> float:
        """
        
        """
        if self.__millidegrees_celsius_per_second != None:
            return self.__millidegrees_celsius_per_second
        self.__millidegrees_celsius_per_second = self.__convert_from_base(TemperatureChangeRateUnits.MillidegreeCelsiusPerSecond)
        return self.__millidegrees_celsius_per_second

    
    @property
    def centidegrees_celsius_per_second(self) -> float:
        """
        
        """
        if self.__centidegrees_celsius_per_second != None:
            return self.__centidegrees_celsius_per_second
        self.__centidegrees_celsius_per_second = self.__convert_from_base(TemperatureChangeRateUnits.CentidegreeCelsiusPerSecond)
        return self.__centidegrees_celsius_per_second

    
    @property
    def decidegrees_celsius_per_second(self) -> float:
        """
        
        """
        if self.__decidegrees_celsius_per_second != None:
            return self.__decidegrees_celsius_per_second
        self.__decidegrees_celsius_per_second = self.__convert_from_base(TemperatureChangeRateUnits.DecidegreeCelsiusPerSecond)
        return self.__decidegrees_celsius_per_second

    
    @property
    def decadegrees_celsius_per_second(self) -> float:
        """
        
        """
        if self.__decadegrees_celsius_per_second != None:
            return self.__decadegrees_celsius_per_second
        self.__decadegrees_celsius_per_second = self.__convert_from_base(TemperatureChangeRateUnits.DecadegreeCelsiusPerSecond)
        return self.__decadegrees_celsius_per_second

    
    @property
    def hectodegrees_celsius_per_second(self) -> float:
        """
        
        """
        if self.__hectodegrees_celsius_per_second != None:
            return self.__hectodegrees_celsius_per_second
        self.__hectodegrees_celsius_per_second = self.__convert_from_base(TemperatureChangeRateUnits.HectodegreeCelsiusPerSecond)
        return self.__hectodegrees_celsius_per_second

    
    @property
    def kilodegrees_celsius_per_second(self) -> float:
        """
        
        """
        if self.__kilodegrees_celsius_per_second != None:
            return self.__kilodegrees_celsius_per_second
        self.__kilodegrees_celsius_per_second = self.__convert_from_base(TemperatureChangeRateUnits.KilodegreeCelsiusPerSecond)
        return self.__kilodegrees_celsius_per_second

    
    def to_string(self, unit: TemperatureChangeRateUnits = TemperatureChangeRateUnits.DegreeCelsiusPerSecond) -> str:
        """
        Format the TemperatureChangeRate to string.
        Note! the default format for TemperatureChangeRate is DegreeCelsiusPerSecond.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == TemperatureChangeRateUnits.DegreeCelsiusPerSecond:
            return f"""{self.degrees_celsius_per_second} °C/s"""
        
        if unit == TemperatureChangeRateUnits.DegreeCelsiusPerMinute:
            return f"""{self.degrees_celsius_per_minute} °C/min"""
        
        if unit == TemperatureChangeRateUnits.NanodegreeCelsiusPerSecond:
            return f"""{self.nanodegrees_celsius_per_second} n°C/s"""
        
        if unit == TemperatureChangeRateUnits.MicrodegreeCelsiusPerSecond:
            return f"""{self.microdegrees_celsius_per_second} μ°C/s"""
        
        if unit == TemperatureChangeRateUnits.MillidegreeCelsiusPerSecond:
            return f"""{self.millidegrees_celsius_per_second} m°C/s"""
        
        if unit == TemperatureChangeRateUnits.CentidegreeCelsiusPerSecond:
            return f"""{self.centidegrees_celsius_per_second} c°C/s"""
        
        if unit == TemperatureChangeRateUnits.DecidegreeCelsiusPerSecond:
            return f"""{self.decidegrees_celsius_per_second} d°C/s"""
        
        if unit == TemperatureChangeRateUnits.DecadegreeCelsiusPerSecond:
            return f"""{self.decadegrees_celsius_per_second} da°C/s"""
        
        if unit == TemperatureChangeRateUnits.HectodegreeCelsiusPerSecond:
            return f"""{self.hectodegrees_celsius_per_second} h°C/s"""
        
        if unit == TemperatureChangeRateUnits.KilodegreeCelsiusPerSecond:
            return f"""{self.kilodegrees_celsius_per_second} k°C/s"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: TemperatureChangeRateUnits = TemperatureChangeRateUnits.DegreeCelsiusPerSecond) -> str:
        """
        Get TemperatureChangeRate unit abbreviation.
        Note! the default abbreviation for TemperatureChangeRate is DegreeCelsiusPerSecond.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == TemperatureChangeRateUnits.DegreeCelsiusPerSecond:
            return """°C/s"""
        
        if unit_abbreviation == TemperatureChangeRateUnits.DegreeCelsiusPerMinute:
            return """°C/min"""
        
        if unit_abbreviation == TemperatureChangeRateUnits.NanodegreeCelsiusPerSecond:
            return """n°C/s"""
        
        if unit_abbreviation == TemperatureChangeRateUnits.MicrodegreeCelsiusPerSecond:
            return """μ°C/s"""
        
        if unit_abbreviation == TemperatureChangeRateUnits.MillidegreeCelsiusPerSecond:
            return """m°C/s"""
        
        if unit_abbreviation == TemperatureChangeRateUnits.CentidegreeCelsiusPerSecond:
            return """c°C/s"""
        
        if unit_abbreviation == TemperatureChangeRateUnits.DecidegreeCelsiusPerSecond:
            return """d°C/s"""
        
        if unit_abbreviation == TemperatureChangeRateUnits.DecadegreeCelsiusPerSecond:
            return """da°C/s"""
        
        if unit_abbreviation == TemperatureChangeRateUnits.HectodegreeCelsiusPerSecond:
            return """h°C/s"""
        
        if unit_abbreviation == TemperatureChangeRateUnits.KilodegreeCelsiusPerSecond:
            return """k°C/s"""
        
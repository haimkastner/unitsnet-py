from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class TemperatureChangeRateUnits(Enum):
        """
            TemperatureChangeRateUnits enumeration
        """
        
        DegreeCelsiusPerSecond = 'DegreeCelsiusPerSecond'
        """
            
        """
        
        DegreeCelsiusPerMinute = 'DegreeCelsiusPerMinute'
        """
            
        """
        
        DegreeKelvinPerMinute = 'DegreeKelvinPerMinute'
        """
            
        """
        
        DegreeFahrenheitPerMinute = 'DegreeFahrenheitPerMinute'
        """
            
        """
        
        DegreeFahrenheitPerSecond = 'DegreeFahrenheitPerSecond'
        """
            
        """
        
        DegreeKelvinPerSecond = 'DegreeKelvinPerSecond'
        """
            
        """
        
        DegreeCelsiusPerHour = 'DegreeCelsiusPerHour'
        """
            
        """
        
        DegreeKelvinPerHour = 'DegreeKelvinPerHour'
        """
            
        """
        
        DegreeFahrenheitPerHour = 'DegreeFahrenheitPerHour'
        """
            
        """
        
        NanodegreeCelsiusPerSecond = 'NanodegreeCelsiusPerSecond'
        """
            
        """
        
        MicrodegreeCelsiusPerSecond = 'MicrodegreeCelsiusPerSecond'
        """
            
        """
        
        MillidegreeCelsiusPerSecond = 'MillidegreeCelsiusPerSecond'
        """
            
        """
        
        CentidegreeCelsiusPerSecond = 'CentidegreeCelsiusPerSecond'
        """
            
        """
        
        DecidegreeCelsiusPerSecond = 'DecidegreeCelsiusPerSecond'
        """
            
        """
        
        DecadegreeCelsiusPerSecond = 'DecadegreeCelsiusPerSecond'
        """
            
        """
        
        HectodegreeCelsiusPerSecond = 'HectodegreeCelsiusPerSecond'
        """
            
        """
        
        KilodegreeCelsiusPerSecond = 'KilodegreeCelsiusPerSecond'
        """
            
        """
        

class TemperatureChangeRateDto:
    """
    A DTO representation of a TemperatureChangeRate

    Attributes:
        value (float): The value of the TemperatureChangeRate.
        unit (TemperatureChangeRateUnits): The specific unit that the TemperatureChangeRate value is representing.
    """

    def __init__(self, value: float, unit: TemperatureChangeRateUnits):
        """
        Create a new DTO representation of a TemperatureChangeRate

        Parameters:
            value (float): The value of the TemperatureChangeRate.
            unit (TemperatureChangeRateUnits): The specific unit that the TemperatureChangeRate value is representing.
        """
        self.value: float = value
        """
        The value of the TemperatureChangeRate
        """
        self.unit: TemperatureChangeRateUnits = unit
        """
        The specific unit that the TemperatureChangeRate value is representing
        """

    def to_json(self):
        """
        Get a TemperatureChangeRate DTO JSON object representing the current unit.

        :return: JSON object represents TemperatureChangeRate DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "DegreeCelsiusPerSecond"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of TemperatureChangeRate DTO from a json representation.

        :param data: The TemperatureChangeRate DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "DegreeCelsiusPerSecond"}
        :return: A new instance of TemperatureChangeRateDto.
        :rtype: TemperatureChangeRateDto
        """
        return TemperatureChangeRateDto(value=data["value"], unit=TemperatureChangeRateUnits(data["unit"]))


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
        
        self.__degrees_kelvin_per_minute = None
        
        self.__degrees_fahrenheit_per_minute = None
        
        self.__degrees_fahrenheit_per_second = None
        
        self.__degrees_kelvin_per_second = None
        
        self.__degrees_celsius_per_hour = None
        
        self.__degrees_kelvin_per_hour = None
        
        self.__degrees_fahrenheit_per_hour = None
        
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

    def to_dto(self, hold_in_unit: TemperatureChangeRateUnits = TemperatureChangeRateUnits.DegreeCelsiusPerSecond) -> TemperatureChangeRateDto:
        """
        Get a new instance of TemperatureChangeRate DTO representing the current unit.

        :param hold_in_unit: The specific TemperatureChangeRate unit to store the TemperatureChangeRate value in the DTO representation.
        :type hold_in_unit: TemperatureChangeRateUnits
        :return: A new instance of TemperatureChangeRateDto.
        :rtype: TemperatureChangeRateDto
        """
        return TemperatureChangeRateDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: TemperatureChangeRateUnits = TemperatureChangeRateUnits.DegreeCelsiusPerSecond):
        """
        Get a TemperatureChangeRate DTO JSON object representing the current unit.

        :param hold_in_unit: The specific TemperatureChangeRate unit to store the TemperatureChangeRate value in the DTO representation.
        :type hold_in_unit: TemperatureChangeRateUnits
        :return: JSON object represents TemperatureChangeRate DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "DegreeCelsiusPerSecond"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(temperature_change_rate_dto: TemperatureChangeRateDto):
        """
        Obtain a new instance of TemperatureChangeRate from a DTO unit object.

        :param temperature_change_rate_dto: The TemperatureChangeRate DTO representation.
        :type temperature_change_rate_dto: TemperatureChangeRateDto
        :return: A new instance of TemperatureChangeRate.
        :rtype: TemperatureChangeRate
        """
        return TemperatureChangeRate(temperature_change_rate_dto.value, temperature_change_rate_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of TemperatureChangeRate from a DTO unit json representation.

        :param data: The TemperatureChangeRate DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "DegreeCelsiusPerSecond"}
        :return: A new instance of TemperatureChangeRate.
        :rtype: TemperatureChangeRate
        """
        return TemperatureChangeRate.from_dto(TemperatureChangeRateDto.from_json(data))

    def __convert_from_base(self, from_unit: TemperatureChangeRateUnits) -> float:
        value = self._value
        
        if from_unit == TemperatureChangeRateUnits.DegreeCelsiusPerSecond:
            return (value)
        
        if from_unit == TemperatureChangeRateUnits.DegreeCelsiusPerMinute:
            return (value * 60)
        
        if from_unit == TemperatureChangeRateUnits.DegreeKelvinPerMinute:
            return (value * 60)
        
        if from_unit == TemperatureChangeRateUnits.DegreeFahrenheitPerMinute:
            return (value * 9 / 5 * 60)
        
        if from_unit == TemperatureChangeRateUnits.DegreeFahrenheitPerSecond:
            return (value * 9 / 5)
        
        if from_unit == TemperatureChangeRateUnits.DegreeKelvinPerSecond:
            return (value)
        
        if from_unit == TemperatureChangeRateUnits.DegreeCelsiusPerHour:
            return (value * 3600)
        
        if from_unit == TemperatureChangeRateUnits.DegreeKelvinPerHour:
            return (value * 3600)
        
        if from_unit == TemperatureChangeRateUnits.DegreeFahrenheitPerHour:
            return (value * 9 / 5 * 3600)
        
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
        
        if to_unit == TemperatureChangeRateUnits.DegreeKelvinPerMinute:
            return (value / 60)
        
        if to_unit == TemperatureChangeRateUnits.DegreeFahrenheitPerMinute:
            return (value * 5 / 9 / 60)
        
        if to_unit == TemperatureChangeRateUnits.DegreeFahrenheitPerSecond:
            return (value * 5 / 9)
        
        if to_unit == TemperatureChangeRateUnits.DegreeKelvinPerSecond:
            return (value)
        
        if to_unit == TemperatureChangeRateUnits.DegreeCelsiusPerHour:
            return (value / 3600)
        
        if to_unit == TemperatureChangeRateUnits.DegreeKelvinPerHour:
            return (value / 3600)
        
        if to_unit == TemperatureChangeRateUnits.DegreeFahrenheitPerHour:
            return (value * 5 / 9 / 3600)
        
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
    def from_degrees_kelvin_per_minute(degrees_kelvin_per_minute: float):
        """
        Create a new instance of TemperatureChangeRate from a value in degrees_kelvin_per_minute.

        

        :param meters: The TemperatureChangeRate value in degrees_kelvin_per_minute.
        :type degrees_kelvin_per_minute: float
        :return: A new instance of TemperatureChangeRate.
        :rtype: TemperatureChangeRate
        """
        return TemperatureChangeRate(degrees_kelvin_per_minute, TemperatureChangeRateUnits.DegreeKelvinPerMinute)

    
    @staticmethod
    def from_degrees_fahrenheit_per_minute(degrees_fahrenheit_per_minute: float):
        """
        Create a new instance of TemperatureChangeRate from a value in degrees_fahrenheit_per_minute.

        

        :param meters: The TemperatureChangeRate value in degrees_fahrenheit_per_minute.
        :type degrees_fahrenheit_per_minute: float
        :return: A new instance of TemperatureChangeRate.
        :rtype: TemperatureChangeRate
        """
        return TemperatureChangeRate(degrees_fahrenheit_per_minute, TemperatureChangeRateUnits.DegreeFahrenheitPerMinute)

    
    @staticmethod
    def from_degrees_fahrenheit_per_second(degrees_fahrenheit_per_second: float):
        """
        Create a new instance of TemperatureChangeRate from a value in degrees_fahrenheit_per_second.

        

        :param meters: The TemperatureChangeRate value in degrees_fahrenheit_per_second.
        :type degrees_fahrenheit_per_second: float
        :return: A new instance of TemperatureChangeRate.
        :rtype: TemperatureChangeRate
        """
        return TemperatureChangeRate(degrees_fahrenheit_per_second, TemperatureChangeRateUnits.DegreeFahrenheitPerSecond)

    
    @staticmethod
    def from_degrees_kelvin_per_second(degrees_kelvin_per_second: float):
        """
        Create a new instance of TemperatureChangeRate from a value in degrees_kelvin_per_second.

        

        :param meters: The TemperatureChangeRate value in degrees_kelvin_per_second.
        :type degrees_kelvin_per_second: float
        :return: A new instance of TemperatureChangeRate.
        :rtype: TemperatureChangeRate
        """
        return TemperatureChangeRate(degrees_kelvin_per_second, TemperatureChangeRateUnits.DegreeKelvinPerSecond)

    
    @staticmethod
    def from_degrees_celsius_per_hour(degrees_celsius_per_hour: float):
        """
        Create a new instance of TemperatureChangeRate from a value in degrees_celsius_per_hour.

        

        :param meters: The TemperatureChangeRate value in degrees_celsius_per_hour.
        :type degrees_celsius_per_hour: float
        :return: A new instance of TemperatureChangeRate.
        :rtype: TemperatureChangeRate
        """
        return TemperatureChangeRate(degrees_celsius_per_hour, TemperatureChangeRateUnits.DegreeCelsiusPerHour)

    
    @staticmethod
    def from_degrees_kelvin_per_hour(degrees_kelvin_per_hour: float):
        """
        Create a new instance of TemperatureChangeRate from a value in degrees_kelvin_per_hour.

        

        :param meters: The TemperatureChangeRate value in degrees_kelvin_per_hour.
        :type degrees_kelvin_per_hour: float
        :return: A new instance of TemperatureChangeRate.
        :rtype: TemperatureChangeRate
        """
        return TemperatureChangeRate(degrees_kelvin_per_hour, TemperatureChangeRateUnits.DegreeKelvinPerHour)

    
    @staticmethod
    def from_degrees_fahrenheit_per_hour(degrees_fahrenheit_per_hour: float):
        """
        Create a new instance of TemperatureChangeRate from a value in degrees_fahrenheit_per_hour.

        

        :param meters: The TemperatureChangeRate value in degrees_fahrenheit_per_hour.
        :type degrees_fahrenheit_per_hour: float
        :return: A new instance of TemperatureChangeRate.
        :rtype: TemperatureChangeRate
        """
        return TemperatureChangeRate(degrees_fahrenheit_per_hour, TemperatureChangeRateUnits.DegreeFahrenheitPerHour)

    
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
    def degrees_kelvin_per_minute(self) -> float:
        """
        
        """
        if self.__degrees_kelvin_per_minute != None:
            return self.__degrees_kelvin_per_minute
        self.__degrees_kelvin_per_minute = self.__convert_from_base(TemperatureChangeRateUnits.DegreeKelvinPerMinute)
        return self.__degrees_kelvin_per_minute

    
    @property
    def degrees_fahrenheit_per_minute(self) -> float:
        """
        
        """
        if self.__degrees_fahrenheit_per_minute != None:
            return self.__degrees_fahrenheit_per_minute
        self.__degrees_fahrenheit_per_minute = self.__convert_from_base(TemperatureChangeRateUnits.DegreeFahrenheitPerMinute)
        return self.__degrees_fahrenheit_per_minute

    
    @property
    def degrees_fahrenheit_per_second(self) -> float:
        """
        
        """
        if self.__degrees_fahrenheit_per_second != None:
            return self.__degrees_fahrenheit_per_second
        self.__degrees_fahrenheit_per_second = self.__convert_from_base(TemperatureChangeRateUnits.DegreeFahrenheitPerSecond)
        return self.__degrees_fahrenheit_per_second

    
    @property
    def degrees_kelvin_per_second(self) -> float:
        """
        
        """
        if self.__degrees_kelvin_per_second != None:
            return self.__degrees_kelvin_per_second
        self.__degrees_kelvin_per_second = self.__convert_from_base(TemperatureChangeRateUnits.DegreeKelvinPerSecond)
        return self.__degrees_kelvin_per_second

    
    @property
    def degrees_celsius_per_hour(self) -> float:
        """
        
        """
        if self.__degrees_celsius_per_hour != None:
            return self.__degrees_celsius_per_hour
        self.__degrees_celsius_per_hour = self.__convert_from_base(TemperatureChangeRateUnits.DegreeCelsiusPerHour)
        return self.__degrees_celsius_per_hour

    
    @property
    def degrees_kelvin_per_hour(self) -> float:
        """
        
        """
        if self.__degrees_kelvin_per_hour != None:
            return self.__degrees_kelvin_per_hour
        self.__degrees_kelvin_per_hour = self.__convert_from_base(TemperatureChangeRateUnits.DegreeKelvinPerHour)
        return self.__degrees_kelvin_per_hour

    
    @property
    def degrees_fahrenheit_per_hour(self) -> float:
        """
        
        """
        if self.__degrees_fahrenheit_per_hour != None:
            return self.__degrees_fahrenheit_per_hour
        self.__degrees_fahrenheit_per_hour = self.__convert_from_base(TemperatureChangeRateUnits.DegreeFahrenheitPerHour)
        return self.__degrees_fahrenheit_per_hour

    
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

    
    def to_string(self, unit: TemperatureChangeRateUnits = TemperatureChangeRateUnits.DegreeCelsiusPerSecond, fractional_digits: int = None) -> str:
        """
        Format the TemperatureChangeRate to a string.
        
        Note: the default format for TemperatureChangeRate is DegreeCelsiusPerSecond.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the TemperatureChangeRate. Default is 'DegreeCelsiusPerSecond'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == TemperatureChangeRateUnits.DegreeCelsiusPerSecond:
            return f"""{super()._truncate_fraction_digits(self.degrees_celsius_per_second, fractional_digits)} °C/s"""
        
        if unit == TemperatureChangeRateUnits.DegreeCelsiusPerMinute:
            return f"""{super()._truncate_fraction_digits(self.degrees_celsius_per_minute, fractional_digits)} °C/min"""
        
        if unit == TemperatureChangeRateUnits.DegreeKelvinPerMinute:
            return f"""{super()._truncate_fraction_digits(self.degrees_kelvin_per_minute, fractional_digits)} K/min"""
        
        if unit == TemperatureChangeRateUnits.DegreeFahrenheitPerMinute:
            return f"""{super()._truncate_fraction_digits(self.degrees_fahrenheit_per_minute, fractional_digits)} °F/min"""
        
        if unit == TemperatureChangeRateUnits.DegreeFahrenheitPerSecond:
            return f"""{super()._truncate_fraction_digits(self.degrees_fahrenheit_per_second, fractional_digits)} °F/s"""
        
        if unit == TemperatureChangeRateUnits.DegreeKelvinPerSecond:
            return f"""{super()._truncate_fraction_digits(self.degrees_kelvin_per_second, fractional_digits)} K/s"""
        
        if unit == TemperatureChangeRateUnits.DegreeCelsiusPerHour:
            return f"""{super()._truncate_fraction_digits(self.degrees_celsius_per_hour, fractional_digits)} °C/h"""
        
        if unit == TemperatureChangeRateUnits.DegreeKelvinPerHour:
            return f"""{super()._truncate_fraction_digits(self.degrees_kelvin_per_hour, fractional_digits)} K/h"""
        
        if unit == TemperatureChangeRateUnits.DegreeFahrenheitPerHour:
            return f"""{super()._truncate_fraction_digits(self.degrees_fahrenheit_per_hour, fractional_digits)} °F/h"""
        
        if unit == TemperatureChangeRateUnits.NanodegreeCelsiusPerSecond:
            return f"""{super()._truncate_fraction_digits(self.nanodegrees_celsius_per_second, fractional_digits)} n°C/s"""
        
        if unit == TemperatureChangeRateUnits.MicrodegreeCelsiusPerSecond:
            return f"""{super()._truncate_fraction_digits(self.microdegrees_celsius_per_second, fractional_digits)} μ°C/s"""
        
        if unit == TemperatureChangeRateUnits.MillidegreeCelsiusPerSecond:
            return f"""{super()._truncate_fraction_digits(self.millidegrees_celsius_per_second, fractional_digits)} m°C/s"""
        
        if unit == TemperatureChangeRateUnits.CentidegreeCelsiusPerSecond:
            return f"""{super()._truncate_fraction_digits(self.centidegrees_celsius_per_second, fractional_digits)} c°C/s"""
        
        if unit == TemperatureChangeRateUnits.DecidegreeCelsiusPerSecond:
            return f"""{super()._truncate_fraction_digits(self.decidegrees_celsius_per_second, fractional_digits)} d°C/s"""
        
        if unit == TemperatureChangeRateUnits.DecadegreeCelsiusPerSecond:
            return f"""{super()._truncate_fraction_digits(self.decadegrees_celsius_per_second, fractional_digits)} da°C/s"""
        
        if unit == TemperatureChangeRateUnits.HectodegreeCelsiusPerSecond:
            return f"""{super()._truncate_fraction_digits(self.hectodegrees_celsius_per_second, fractional_digits)} h°C/s"""
        
        if unit == TemperatureChangeRateUnits.KilodegreeCelsiusPerSecond:
            return f"""{super()._truncate_fraction_digits(self.kilodegrees_celsius_per_second, fractional_digits)} k°C/s"""
        
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
        
        if unit_abbreviation == TemperatureChangeRateUnits.DegreeKelvinPerMinute:
            return """K/min"""
        
        if unit_abbreviation == TemperatureChangeRateUnits.DegreeFahrenheitPerMinute:
            return """°F/min"""
        
        if unit_abbreviation == TemperatureChangeRateUnits.DegreeFahrenheitPerSecond:
            return """°F/s"""
        
        if unit_abbreviation == TemperatureChangeRateUnits.DegreeKelvinPerSecond:
            return """K/s"""
        
        if unit_abbreviation == TemperatureChangeRateUnits.DegreeCelsiusPerHour:
            return """°C/h"""
        
        if unit_abbreviation == TemperatureChangeRateUnits.DegreeKelvinPerHour:
            return """K/h"""
        
        if unit_abbreviation == TemperatureChangeRateUnits.DegreeFahrenheitPerHour:
            return """°F/h"""
        
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
        
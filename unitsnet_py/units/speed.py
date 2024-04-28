from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class SpeedUnits(Enum):
        """
            SpeedUnits enumeration
        """
        
        MeterPerSecond = 'MeterPerSecond'
        """
            
        """
        
        MeterPerMinute = 'MeterPerMinute'
        """
            
        """
        
        MeterPerHour = 'MeterPerHour'
        """
            
        """
        
        FootPerSecond = 'FootPerSecond'
        """
            
        """
        
        FootPerMinute = 'FootPerMinute'
        """
            
        """
        
        FootPerHour = 'FootPerHour'
        """
            
        """
        
        UsSurveyFootPerSecond = 'UsSurveyFootPerSecond'
        """
            
        """
        
        UsSurveyFootPerMinute = 'UsSurveyFootPerMinute'
        """
            
        """
        
        UsSurveyFootPerHour = 'UsSurveyFootPerHour'
        """
            
        """
        
        InchPerSecond = 'InchPerSecond'
        """
            
        """
        
        InchPerMinute = 'InchPerMinute'
        """
            
        """
        
        InchPerHour = 'InchPerHour'
        """
            
        """
        
        YardPerSecond = 'YardPerSecond'
        """
            
        """
        
        YardPerMinute = 'YardPerMinute'
        """
            
        """
        
        YardPerHour = 'YardPerHour'
        """
            
        """
        
        Knot = 'Knot'
        """
            The knot, by definition, is a unit of speed equals to 1 nautical mile per hour, which is exactly 1852.000 metres per hour. The length of the internationally agreed nautical mile is 1852 m. The US adopted the international definition in 1954, the UK adopted the international nautical mile definition in 1970.
        """
        
        MilePerHour = 'MilePerHour'
        """
            
        """
        
        Mach = 'Mach'
        """
            
        """
        
        NanometerPerSecond = 'NanometerPerSecond'
        """
            
        """
        
        MicrometerPerSecond = 'MicrometerPerSecond'
        """
            
        """
        
        MillimeterPerSecond = 'MillimeterPerSecond'
        """
            
        """
        
        CentimeterPerSecond = 'CentimeterPerSecond'
        """
            
        """
        
        DecimeterPerSecond = 'DecimeterPerSecond'
        """
            
        """
        
        KilometerPerSecond = 'KilometerPerSecond'
        """
            
        """
        
        NanometerPerMinute = 'NanometerPerMinute'
        """
            
        """
        
        MicrometerPerMinute = 'MicrometerPerMinute'
        """
            
        """
        
        MillimeterPerMinute = 'MillimeterPerMinute'
        """
            
        """
        
        CentimeterPerMinute = 'CentimeterPerMinute'
        """
            
        """
        
        DecimeterPerMinute = 'DecimeterPerMinute'
        """
            
        """
        
        KilometerPerMinute = 'KilometerPerMinute'
        """
            
        """
        
        MillimeterPerHour = 'MillimeterPerHour'
        """
            
        """
        
        CentimeterPerHour = 'CentimeterPerHour'
        """
            
        """
        
        KilometerPerHour = 'KilometerPerHour'
        """
            
        """
        

class SpeedDto:
    """
    A DTO representation of a Speed

    Attributes:
        value (float): The value of the Speed.
        unit (SpeedUnits): The specific unit that the Speed value is representing.
    """

    def __init__(self, value: float, unit: SpeedUnits):
        """
        Create a new DTO representation of a Speed

        Parameters:
            value (float): The value of the Speed.
            unit (SpeedUnits): The specific unit that the Speed value is representing.
        """
        self.value: float = value
        """
        The value of the Speed
        """
        self.unit: SpeedUnits = unit
        """
        The specific unit that the Speed value is representing
        """

    def to_json(self):
        """
        Get a Speed DTO JSON object representing the current unit.

        :return: JSON object represents Speed DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "MeterPerSecond"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of Speed DTO from a json representation.

        :param data: The Speed DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "MeterPerSecond"}
        :return: A new instance of SpeedDto.
        :rtype: SpeedDto
        """
        return SpeedDto(value=data["value"], unit=SpeedUnits(data["unit"]))


class Speed(AbstractMeasure):
    """
    In everyday use and in kinematics, the speed of an object is the magnitude of its velocity (the rate of change of its position); it is thus a scalar quantity.[1] The average speed of an object in an interval of time is the distance travelled by the object divided by the duration of the interval;[2] the instantaneous speed is the limit of the average speed as the duration of the time interval approaches zero.

    Args:
        value (float): The value.
        from_unit (SpeedUnits): The Speed unit to create from, The default unit is MeterPerSecond
    """
    def __init__(self, value: float, from_unit: SpeedUnits = SpeedUnits.MeterPerSecond):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__meters_per_second = None
        
        self.__meters_per_minutes = None
        
        self.__meters_per_hour = None
        
        self.__feet_per_second = None
        
        self.__feet_per_minute = None
        
        self.__feet_per_hour = None
        
        self.__us_survey_feet_per_second = None
        
        self.__us_survey_feet_per_minute = None
        
        self.__us_survey_feet_per_hour = None
        
        self.__inches_per_second = None
        
        self.__inches_per_minute = None
        
        self.__inches_per_hour = None
        
        self.__yards_per_second = None
        
        self.__yards_per_minute = None
        
        self.__yards_per_hour = None
        
        self.__knots = None
        
        self.__miles_per_hour = None
        
        self.__mach = None
        
        self.__nanometers_per_second = None
        
        self.__micrometers_per_second = None
        
        self.__millimeters_per_second = None
        
        self.__centimeters_per_second = None
        
        self.__decimeters_per_second = None
        
        self.__kilometers_per_second = None
        
        self.__nanometers_per_minutes = None
        
        self.__micrometers_per_minutes = None
        
        self.__millimeters_per_minutes = None
        
        self.__centimeters_per_minutes = None
        
        self.__decimeters_per_minutes = None
        
        self.__kilometers_per_minutes = None
        
        self.__millimeters_per_hour = None
        
        self.__centimeters_per_hour = None
        
        self.__kilometers_per_hour = None
        

    def convert(self, unit: SpeedUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: SpeedUnits = SpeedUnits.MeterPerSecond) -> SpeedDto:
        """
        Get a new instance of Speed DTO representing the current unit.

        :param hold_in_unit: The specific Speed unit to store the Speed value in the DTO representation.
        :type hold_in_unit: SpeedUnits
        :return: A new instance of SpeedDto.
        :rtype: SpeedDto
        """
        return SpeedDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: SpeedUnits = SpeedUnits.MeterPerSecond):
        """
        Get a Speed DTO JSON object representing the current unit.

        :param hold_in_unit: The specific Speed unit to store the Speed value in the DTO representation.
        :type hold_in_unit: SpeedUnits
        :return: JSON object represents Speed DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "MeterPerSecond"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(speed_dto: SpeedDto):
        """
        Obtain a new instance of Speed from a DTO unit object.

        :param speed_dto: The Speed DTO representation.
        :type speed_dto: SpeedDto
        :return: A new instance of Speed.
        :rtype: Speed
        """
        return Speed(speed_dto.value, speed_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of Speed from a DTO unit json representation.

        :param data: The Speed DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "MeterPerSecond"}
        :return: A new instance of Speed.
        :rtype: Speed
        """
        return Speed.from_dto(SpeedDto.from_json(data))

    def __convert_from_base(self, from_unit: SpeedUnits) -> float:
        value = self._value
        
        if from_unit == SpeedUnits.MeterPerSecond:
            return (value)
        
        if from_unit == SpeedUnits.MeterPerMinute:
            return (value * 60)
        
        if from_unit == SpeedUnits.MeterPerHour:
            return (value * 3600)
        
        if from_unit == SpeedUnits.FootPerSecond:
            return (value / 0.3048)
        
        if from_unit == SpeedUnits.FootPerMinute:
            return (value / 0.3048 * 60)
        
        if from_unit == SpeedUnits.FootPerHour:
            return (value / 0.3048 * 3600)
        
        if from_unit == SpeedUnits.UsSurveyFootPerSecond:
            return (value * 3937 / 1200)
        
        if from_unit == SpeedUnits.UsSurveyFootPerMinute:
            return ((value * 3937 / 1200) * 60)
        
        if from_unit == SpeedUnits.UsSurveyFootPerHour:
            return ((value * 3937 / 1200) * 3600)
        
        if from_unit == SpeedUnits.InchPerSecond:
            return (value / 2.54e-2)
        
        if from_unit == SpeedUnits.InchPerMinute:
            return ((value / 2.54e-2) * 60)
        
        if from_unit == SpeedUnits.InchPerHour:
            return ((value / 2.54e-2) * 3600)
        
        if from_unit == SpeedUnits.YardPerSecond:
            return (value / 0.9144)
        
        if from_unit == SpeedUnits.YardPerMinute:
            return (value / 0.9144 * 60)
        
        if from_unit == SpeedUnits.YardPerHour:
            return (value / 0.9144 * 3600)
        
        if from_unit == SpeedUnits.Knot:
            return (value / (1852.0 / 3600.0))
        
        if from_unit == SpeedUnits.MilePerHour:
            return (value / 0.44704)
        
        if from_unit == SpeedUnits.Mach:
            return (value / 340.29)
        
        if from_unit == SpeedUnits.NanometerPerSecond:
            return ((value) / 1e-09)
        
        if from_unit == SpeedUnits.MicrometerPerSecond:
            return ((value) / 1e-06)
        
        if from_unit == SpeedUnits.MillimeterPerSecond:
            return ((value) / 0.001)
        
        if from_unit == SpeedUnits.CentimeterPerSecond:
            return ((value) / 0.01)
        
        if from_unit == SpeedUnits.DecimeterPerSecond:
            return ((value) / 0.1)
        
        if from_unit == SpeedUnits.KilometerPerSecond:
            return ((value) / 1000.0)
        
        if from_unit == SpeedUnits.NanometerPerMinute:
            return ((value * 60) / 1e-09)
        
        if from_unit == SpeedUnits.MicrometerPerMinute:
            return ((value * 60) / 1e-06)
        
        if from_unit == SpeedUnits.MillimeterPerMinute:
            return ((value * 60) / 0.001)
        
        if from_unit == SpeedUnits.CentimeterPerMinute:
            return ((value * 60) / 0.01)
        
        if from_unit == SpeedUnits.DecimeterPerMinute:
            return ((value * 60) / 0.1)
        
        if from_unit == SpeedUnits.KilometerPerMinute:
            return ((value * 60) / 1000.0)
        
        if from_unit == SpeedUnits.MillimeterPerHour:
            return ((value * 3600) / 0.001)
        
        if from_unit == SpeedUnits.CentimeterPerHour:
            return ((value * 3600) / 0.01)
        
        if from_unit == SpeedUnits.KilometerPerHour:
            return ((value * 3600) / 1000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: SpeedUnits) -> float:
        
        if to_unit == SpeedUnits.MeterPerSecond:
            return (value)
        
        if to_unit == SpeedUnits.MeterPerMinute:
            return (value / 60)
        
        if to_unit == SpeedUnits.MeterPerHour:
            return (value / 3600)
        
        if to_unit == SpeedUnits.FootPerSecond:
            return (value * 0.3048)
        
        if to_unit == SpeedUnits.FootPerMinute:
            return (value * 0.3048 / 60)
        
        if to_unit == SpeedUnits.FootPerHour:
            return (value * 0.3048 / 3600)
        
        if to_unit == SpeedUnits.UsSurveyFootPerSecond:
            return (value * 1200 / 3937)
        
        if to_unit == SpeedUnits.UsSurveyFootPerMinute:
            return ((value * 1200 / 3937) / 60)
        
        if to_unit == SpeedUnits.UsSurveyFootPerHour:
            return ((value * 1200 / 3937) / 3600)
        
        if to_unit == SpeedUnits.InchPerSecond:
            return (value * 2.54e-2)
        
        if to_unit == SpeedUnits.InchPerMinute:
            return ((value / 60) * 2.54e-2)
        
        if to_unit == SpeedUnits.InchPerHour:
            return ((value / 3600) * 2.54e-2)
        
        if to_unit == SpeedUnits.YardPerSecond:
            return (value * 0.9144)
        
        if to_unit == SpeedUnits.YardPerMinute:
            return (value * 0.9144 / 60)
        
        if to_unit == SpeedUnits.YardPerHour:
            return (value * 0.9144 / 3600)
        
        if to_unit == SpeedUnits.Knot:
            return (value * (1852.0 / 3600.0))
        
        if to_unit == SpeedUnits.MilePerHour:
            return (value * 0.44704)
        
        if to_unit == SpeedUnits.Mach:
            return (value * 340.29)
        
        if to_unit == SpeedUnits.NanometerPerSecond:
            return ((value) * 1e-09)
        
        if to_unit == SpeedUnits.MicrometerPerSecond:
            return ((value) * 1e-06)
        
        if to_unit == SpeedUnits.MillimeterPerSecond:
            return ((value) * 0.001)
        
        if to_unit == SpeedUnits.CentimeterPerSecond:
            return ((value) * 0.01)
        
        if to_unit == SpeedUnits.DecimeterPerSecond:
            return ((value) * 0.1)
        
        if to_unit == SpeedUnits.KilometerPerSecond:
            return ((value) * 1000.0)
        
        if to_unit == SpeedUnits.NanometerPerMinute:
            return ((value / 60) * 1e-09)
        
        if to_unit == SpeedUnits.MicrometerPerMinute:
            return ((value / 60) * 1e-06)
        
        if to_unit == SpeedUnits.MillimeterPerMinute:
            return ((value / 60) * 0.001)
        
        if to_unit == SpeedUnits.CentimeterPerMinute:
            return ((value / 60) * 0.01)
        
        if to_unit == SpeedUnits.DecimeterPerMinute:
            return ((value / 60) * 0.1)
        
        if to_unit == SpeedUnits.KilometerPerMinute:
            return ((value / 60) * 1000.0)
        
        if to_unit == SpeedUnits.MillimeterPerHour:
            return ((value / 3600) * 0.001)
        
        if to_unit == SpeedUnits.CentimeterPerHour:
            return ((value / 3600) * 0.01)
        
        if to_unit == SpeedUnits.KilometerPerHour:
            return ((value / 3600) * 1000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_meters_per_second(meters_per_second: float):
        """
        Create a new instance of Speed from a value in meters_per_second.

        

        :param meters: The Speed value in meters_per_second.
        :type meters_per_second: float
        :return: A new instance of Speed.
        :rtype: Speed
        """
        return Speed(meters_per_second, SpeedUnits.MeterPerSecond)

    
    @staticmethod
    def from_meters_per_minutes(meters_per_minutes: float):
        """
        Create a new instance of Speed from a value in meters_per_minutes.

        

        :param meters: The Speed value in meters_per_minutes.
        :type meters_per_minutes: float
        :return: A new instance of Speed.
        :rtype: Speed
        """
        return Speed(meters_per_minutes, SpeedUnits.MeterPerMinute)

    
    @staticmethod
    def from_meters_per_hour(meters_per_hour: float):
        """
        Create a new instance of Speed from a value in meters_per_hour.

        

        :param meters: The Speed value in meters_per_hour.
        :type meters_per_hour: float
        :return: A new instance of Speed.
        :rtype: Speed
        """
        return Speed(meters_per_hour, SpeedUnits.MeterPerHour)

    
    @staticmethod
    def from_feet_per_second(feet_per_second: float):
        """
        Create a new instance of Speed from a value in feet_per_second.

        

        :param meters: The Speed value in feet_per_second.
        :type feet_per_second: float
        :return: A new instance of Speed.
        :rtype: Speed
        """
        return Speed(feet_per_second, SpeedUnits.FootPerSecond)

    
    @staticmethod
    def from_feet_per_minute(feet_per_minute: float):
        """
        Create a new instance of Speed from a value in feet_per_minute.

        

        :param meters: The Speed value in feet_per_minute.
        :type feet_per_minute: float
        :return: A new instance of Speed.
        :rtype: Speed
        """
        return Speed(feet_per_minute, SpeedUnits.FootPerMinute)

    
    @staticmethod
    def from_feet_per_hour(feet_per_hour: float):
        """
        Create a new instance of Speed from a value in feet_per_hour.

        

        :param meters: The Speed value in feet_per_hour.
        :type feet_per_hour: float
        :return: A new instance of Speed.
        :rtype: Speed
        """
        return Speed(feet_per_hour, SpeedUnits.FootPerHour)

    
    @staticmethod
    def from_us_survey_feet_per_second(us_survey_feet_per_second: float):
        """
        Create a new instance of Speed from a value in us_survey_feet_per_second.

        

        :param meters: The Speed value in us_survey_feet_per_second.
        :type us_survey_feet_per_second: float
        :return: A new instance of Speed.
        :rtype: Speed
        """
        return Speed(us_survey_feet_per_second, SpeedUnits.UsSurveyFootPerSecond)

    
    @staticmethod
    def from_us_survey_feet_per_minute(us_survey_feet_per_minute: float):
        """
        Create a new instance of Speed from a value in us_survey_feet_per_minute.

        

        :param meters: The Speed value in us_survey_feet_per_minute.
        :type us_survey_feet_per_minute: float
        :return: A new instance of Speed.
        :rtype: Speed
        """
        return Speed(us_survey_feet_per_minute, SpeedUnits.UsSurveyFootPerMinute)

    
    @staticmethod
    def from_us_survey_feet_per_hour(us_survey_feet_per_hour: float):
        """
        Create a new instance of Speed from a value in us_survey_feet_per_hour.

        

        :param meters: The Speed value in us_survey_feet_per_hour.
        :type us_survey_feet_per_hour: float
        :return: A new instance of Speed.
        :rtype: Speed
        """
        return Speed(us_survey_feet_per_hour, SpeedUnits.UsSurveyFootPerHour)

    
    @staticmethod
    def from_inches_per_second(inches_per_second: float):
        """
        Create a new instance of Speed from a value in inches_per_second.

        

        :param meters: The Speed value in inches_per_second.
        :type inches_per_second: float
        :return: A new instance of Speed.
        :rtype: Speed
        """
        return Speed(inches_per_second, SpeedUnits.InchPerSecond)

    
    @staticmethod
    def from_inches_per_minute(inches_per_minute: float):
        """
        Create a new instance of Speed from a value in inches_per_minute.

        

        :param meters: The Speed value in inches_per_minute.
        :type inches_per_minute: float
        :return: A new instance of Speed.
        :rtype: Speed
        """
        return Speed(inches_per_minute, SpeedUnits.InchPerMinute)

    
    @staticmethod
    def from_inches_per_hour(inches_per_hour: float):
        """
        Create a new instance of Speed from a value in inches_per_hour.

        

        :param meters: The Speed value in inches_per_hour.
        :type inches_per_hour: float
        :return: A new instance of Speed.
        :rtype: Speed
        """
        return Speed(inches_per_hour, SpeedUnits.InchPerHour)

    
    @staticmethod
    def from_yards_per_second(yards_per_second: float):
        """
        Create a new instance of Speed from a value in yards_per_second.

        

        :param meters: The Speed value in yards_per_second.
        :type yards_per_second: float
        :return: A new instance of Speed.
        :rtype: Speed
        """
        return Speed(yards_per_second, SpeedUnits.YardPerSecond)

    
    @staticmethod
    def from_yards_per_minute(yards_per_minute: float):
        """
        Create a new instance of Speed from a value in yards_per_minute.

        

        :param meters: The Speed value in yards_per_minute.
        :type yards_per_minute: float
        :return: A new instance of Speed.
        :rtype: Speed
        """
        return Speed(yards_per_minute, SpeedUnits.YardPerMinute)

    
    @staticmethod
    def from_yards_per_hour(yards_per_hour: float):
        """
        Create a new instance of Speed from a value in yards_per_hour.

        

        :param meters: The Speed value in yards_per_hour.
        :type yards_per_hour: float
        :return: A new instance of Speed.
        :rtype: Speed
        """
        return Speed(yards_per_hour, SpeedUnits.YardPerHour)

    
    @staticmethod
    def from_knots(knots: float):
        """
        Create a new instance of Speed from a value in knots.

        The knot, by definition, is a unit of speed equals to 1 nautical mile per hour, which is exactly 1852.000 metres per hour. The length of the internationally agreed nautical mile is 1852 m. The US adopted the international definition in 1954, the UK adopted the international nautical mile definition in 1970.

        :param meters: The Speed value in knots.
        :type knots: float
        :return: A new instance of Speed.
        :rtype: Speed
        """
        return Speed(knots, SpeedUnits.Knot)

    
    @staticmethod
    def from_miles_per_hour(miles_per_hour: float):
        """
        Create a new instance of Speed from a value in miles_per_hour.

        

        :param meters: The Speed value in miles_per_hour.
        :type miles_per_hour: float
        :return: A new instance of Speed.
        :rtype: Speed
        """
        return Speed(miles_per_hour, SpeedUnits.MilePerHour)

    
    @staticmethod
    def from_mach(mach: float):
        """
        Create a new instance of Speed from a value in mach.

        

        :param meters: The Speed value in mach.
        :type mach: float
        :return: A new instance of Speed.
        :rtype: Speed
        """
        return Speed(mach, SpeedUnits.Mach)

    
    @staticmethod
    def from_nanometers_per_second(nanometers_per_second: float):
        """
        Create a new instance of Speed from a value in nanometers_per_second.

        

        :param meters: The Speed value in nanometers_per_second.
        :type nanometers_per_second: float
        :return: A new instance of Speed.
        :rtype: Speed
        """
        return Speed(nanometers_per_second, SpeedUnits.NanometerPerSecond)

    
    @staticmethod
    def from_micrometers_per_second(micrometers_per_second: float):
        """
        Create a new instance of Speed from a value in micrometers_per_second.

        

        :param meters: The Speed value in micrometers_per_second.
        :type micrometers_per_second: float
        :return: A new instance of Speed.
        :rtype: Speed
        """
        return Speed(micrometers_per_second, SpeedUnits.MicrometerPerSecond)

    
    @staticmethod
    def from_millimeters_per_second(millimeters_per_second: float):
        """
        Create a new instance of Speed from a value in millimeters_per_second.

        

        :param meters: The Speed value in millimeters_per_second.
        :type millimeters_per_second: float
        :return: A new instance of Speed.
        :rtype: Speed
        """
        return Speed(millimeters_per_second, SpeedUnits.MillimeterPerSecond)

    
    @staticmethod
    def from_centimeters_per_second(centimeters_per_second: float):
        """
        Create a new instance of Speed from a value in centimeters_per_second.

        

        :param meters: The Speed value in centimeters_per_second.
        :type centimeters_per_second: float
        :return: A new instance of Speed.
        :rtype: Speed
        """
        return Speed(centimeters_per_second, SpeedUnits.CentimeterPerSecond)

    
    @staticmethod
    def from_decimeters_per_second(decimeters_per_second: float):
        """
        Create a new instance of Speed from a value in decimeters_per_second.

        

        :param meters: The Speed value in decimeters_per_second.
        :type decimeters_per_second: float
        :return: A new instance of Speed.
        :rtype: Speed
        """
        return Speed(decimeters_per_second, SpeedUnits.DecimeterPerSecond)

    
    @staticmethod
    def from_kilometers_per_second(kilometers_per_second: float):
        """
        Create a new instance of Speed from a value in kilometers_per_second.

        

        :param meters: The Speed value in kilometers_per_second.
        :type kilometers_per_second: float
        :return: A new instance of Speed.
        :rtype: Speed
        """
        return Speed(kilometers_per_second, SpeedUnits.KilometerPerSecond)

    
    @staticmethod
    def from_nanometers_per_minutes(nanometers_per_minutes: float):
        """
        Create a new instance of Speed from a value in nanometers_per_minutes.

        

        :param meters: The Speed value in nanometers_per_minutes.
        :type nanometers_per_minutes: float
        :return: A new instance of Speed.
        :rtype: Speed
        """
        return Speed(nanometers_per_minutes, SpeedUnits.NanometerPerMinute)

    
    @staticmethod
    def from_micrometers_per_minutes(micrometers_per_minutes: float):
        """
        Create a new instance of Speed from a value in micrometers_per_minutes.

        

        :param meters: The Speed value in micrometers_per_minutes.
        :type micrometers_per_minutes: float
        :return: A new instance of Speed.
        :rtype: Speed
        """
        return Speed(micrometers_per_minutes, SpeedUnits.MicrometerPerMinute)

    
    @staticmethod
    def from_millimeters_per_minutes(millimeters_per_minutes: float):
        """
        Create a new instance of Speed from a value in millimeters_per_minutes.

        

        :param meters: The Speed value in millimeters_per_minutes.
        :type millimeters_per_minutes: float
        :return: A new instance of Speed.
        :rtype: Speed
        """
        return Speed(millimeters_per_minutes, SpeedUnits.MillimeterPerMinute)

    
    @staticmethod
    def from_centimeters_per_minutes(centimeters_per_minutes: float):
        """
        Create a new instance of Speed from a value in centimeters_per_minutes.

        

        :param meters: The Speed value in centimeters_per_minutes.
        :type centimeters_per_minutes: float
        :return: A new instance of Speed.
        :rtype: Speed
        """
        return Speed(centimeters_per_minutes, SpeedUnits.CentimeterPerMinute)

    
    @staticmethod
    def from_decimeters_per_minutes(decimeters_per_minutes: float):
        """
        Create a new instance of Speed from a value in decimeters_per_minutes.

        

        :param meters: The Speed value in decimeters_per_minutes.
        :type decimeters_per_minutes: float
        :return: A new instance of Speed.
        :rtype: Speed
        """
        return Speed(decimeters_per_minutes, SpeedUnits.DecimeterPerMinute)

    
    @staticmethod
    def from_kilometers_per_minutes(kilometers_per_minutes: float):
        """
        Create a new instance of Speed from a value in kilometers_per_minutes.

        

        :param meters: The Speed value in kilometers_per_minutes.
        :type kilometers_per_minutes: float
        :return: A new instance of Speed.
        :rtype: Speed
        """
        return Speed(kilometers_per_minutes, SpeedUnits.KilometerPerMinute)

    
    @staticmethod
    def from_millimeters_per_hour(millimeters_per_hour: float):
        """
        Create a new instance of Speed from a value in millimeters_per_hour.

        

        :param meters: The Speed value in millimeters_per_hour.
        :type millimeters_per_hour: float
        :return: A new instance of Speed.
        :rtype: Speed
        """
        return Speed(millimeters_per_hour, SpeedUnits.MillimeterPerHour)

    
    @staticmethod
    def from_centimeters_per_hour(centimeters_per_hour: float):
        """
        Create a new instance of Speed from a value in centimeters_per_hour.

        

        :param meters: The Speed value in centimeters_per_hour.
        :type centimeters_per_hour: float
        :return: A new instance of Speed.
        :rtype: Speed
        """
        return Speed(centimeters_per_hour, SpeedUnits.CentimeterPerHour)

    
    @staticmethod
    def from_kilometers_per_hour(kilometers_per_hour: float):
        """
        Create a new instance of Speed from a value in kilometers_per_hour.

        

        :param meters: The Speed value in kilometers_per_hour.
        :type kilometers_per_hour: float
        :return: A new instance of Speed.
        :rtype: Speed
        """
        return Speed(kilometers_per_hour, SpeedUnits.KilometerPerHour)

    
    @property
    def meters_per_second(self) -> float:
        """
        
        """
        if self.__meters_per_second != None:
            return self.__meters_per_second
        self.__meters_per_second = self.__convert_from_base(SpeedUnits.MeterPerSecond)
        return self.__meters_per_second

    
    @property
    def meters_per_minutes(self) -> float:
        """
        
        """
        if self.__meters_per_minutes != None:
            return self.__meters_per_minutes
        self.__meters_per_minutes = self.__convert_from_base(SpeedUnits.MeterPerMinute)
        return self.__meters_per_minutes

    
    @property
    def meters_per_hour(self) -> float:
        """
        
        """
        if self.__meters_per_hour != None:
            return self.__meters_per_hour
        self.__meters_per_hour = self.__convert_from_base(SpeedUnits.MeterPerHour)
        return self.__meters_per_hour

    
    @property
    def feet_per_second(self) -> float:
        """
        
        """
        if self.__feet_per_second != None:
            return self.__feet_per_second
        self.__feet_per_second = self.__convert_from_base(SpeedUnits.FootPerSecond)
        return self.__feet_per_second

    
    @property
    def feet_per_minute(self) -> float:
        """
        
        """
        if self.__feet_per_minute != None:
            return self.__feet_per_minute
        self.__feet_per_minute = self.__convert_from_base(SpeedUnits.FootPerMinute)
        return self.__feet_per_minute

    
    @property
    def feet_per_hour(self) -> float:
        """
        
        """
        if self.__feet_per_hour != None:
            return self.__feet_per_hour
        self.__feet_per_hour = self.__convert_from_base(SpeedUnits.FootPerHour)
        return self.__feet_per_hour

    
    @property
    def us_survey_feet_per_second(self) -> float:
        """
        
        """
        if self.__us_survey_feet_per_second != None:
            return self.__us_survey_feet_per_second
        self.__us_survey_feet_per_second = self.__convert_from_base(SpeedUnits.UsSurveyFootPerSecond)
        return self.__us_survey_feet_per_second

    
    @property
    def us_survey_feet_per_minute(self) -> float:
        """
        
        """
        if self.__us_survey_feet_per_minute != None:
            return self.__us_survey_feet_per_minute
        self.__us_survey_feet_per_minute = self.__convert_from_base(SpeedUnits.UsSurveyFootPerMinute)
        return self.__us_survey_feet_per_minute

    
    @property
    def us_survey_feet_per_hour(self) -> float:
        """
        
        """
        if self.__us_survey_feet_per_hour != None:
            return self.__us_survey_feet_per_hour
        self.__us_survey_feet_per_hour = self.__convert_from_base(SpeedUnits.UsSurveyFootPerHour)
        return self.__us_survey_feet_per_hour

    
    @property
    def inches_per_second(self) -> float:
        """
        
        """
        if self.__inches_per_second != None:
            return self.__inches_per_second
        self.__inches_per_second = self.__convert_from_base(SpeedUnits.InchPerSecond)
        return self.__inches_per_second

    
    @property
    def inches_per_minute(self) -> float:
        """
        
        """
        if self.__inches_per_minute != None:
            return self.__inches_per_minute
        self.__inches_per_minute = self.__convert_from_base(SpeedUnits.InchPerMinute)
        return self.__inches_per_minute

    
    @property
    def inches_per_hour(self) -> float:
        """
        
        """
        if self.__inches_per_hour != None:
            return self.__inches_per_hour
        self.__inches_per_hour = self.__convert_from_base(SpeedUnits.InchPerHour)
        return self.__inches_per_hour

    
    @property
    def yards_per_second(self) -> float:
        """
        
        """
        if self.__yards_per_second != None:
            return self.__yards_per_second
        self.__yards_per_second = self.__convert_from_base(SpeedUnits.YardPerSecond)
        return self.__yards_per_second

    
    @property
    def yards_per_minute(self) -> float:
        """
        
        """
        if self.__yards_per_minute != None:
            return self.__yards_per_minute
        self.__yards_per_minute = self.__convert_from_base(SpeedUnits.YardPerMinute)
        return self.__yards_per_minute

    
    @property
    def yards_per_hour(self) -> float:
        """
        
        """
        if self.__yards_per_hour != None:
            return self.__yards_per_hour
        self.__yards_per_hour = self.__convert_from_base(SpeedUnits.YardPerHour)
        return self.__yards_per_hour

    
    @property
    def knots(self) -> float:
        """
        The knot, by definition, is a unit of speed equals to 1 nautical mile per hour, which is exactly 1852.000 metres per hour. The length of the internationally agreed nautical mile is 1852 m. The US adopted the international definition in 1954, the UK adopted the international nautical mile definition in 1970.
        """
        if self.__knots != None:
            return self.__knots
        self.__knots = self.__convert_from_base(SpeedUnits.Knot)
        return self.__knots

    
    @property
    def miles_per_hour(self) -> float:
        """
        
        """
        if self.__miles_per_hour != None:
            return self.__miles_per_hour
        self.__miles_per_hour = self.__convert_from_base(SpeedUnits.MilePerHour)
        return self.__miles_per_hour

    
    @property
    def mach(self) -> float:
        """
        
        """
        if self.__mach != None:
            return self.__mach
        self.__mach = self.__convert_from_base(SpeedUnits.Mach)
        return self.__mach

    
    @property
    def nanometers_per_second(self) -> float:
        """
        
        """
        if self.__nanometers_per_second != None:
            return self.__nanometers_per_second
        self.__nanometers_per_second = self.__convert_from_base(SpeedUnits.NanometerPerSecond)
        return self.__nanometers_per_second

    
    @property
    def micrometers_per_second(self) -> float:
        """
        
        """
        if self.__micrometers_per_second != None:
            return self.__micrometers_per_second
        self.__micrometers_per_second = self.__convert_from_base(SpeedUnits.MicrometerPerSecond)
        return self.__micrometers_per_second

    
    @property
    def millimeters_per_second(self) -> float:
        """
        
        """
        if self.__millimeters_per_second != None:
            return self.__millimeters_per_second
        self.__millimeters_per_second = self.__convert_from_base(SpeedUnits.MillimeterPerSecond)
        return self.__millimeters_per_second

    
    @property
    def centimeters_per_second(self) -> float:
        """
        
        """
        if self.__centimeters_per_second != None:
            return self.__centimeters_per_second
        self.__centimeters_per_second = self.__convert_from_base(SpeedUnits.CentimeterPerSecond)
        return self.__centimeters_per_second

    
    @property
    def decimeters_per_second(self) -> float:
        """
        
        """
        if self.__decimeters_per_second != None:
            return self.__decimeters_per_second
        self.__decimeters_per_second = self.__convert_from_base(SpeedUnits.DecimeterPerSecond)
        return self.__decimeters_per_second

    
    @property
    def kilometers_per_second(self) -> float:
        """
        
        """
        if self.__kilometers_per_second != None:
            return self.__kilometers_per_second
        self.__kilometers_per_second = self.__convert_from_base(SpeedUnits.KilometerPerSecond)
        return self.__kilometers_per_second

    
    @property
    def nanometers_per_minutes(self) -> float:
        """
        
        """
        if self.__nanometers_per_minutes != None:
            return self.__nanometers_per_minutes
        self.__nanometers_per_minutes = self.__convert_from_base(SpeedUnits.NanometerPerMinute)
        return self.__nanometers_per_minutes

    
    @property
    def micrometers_per_minutes(self) -> float:
        """
        
        """
        if self.__micrometers_per_minutes != None:
            return self.__micrometers_per_minutes
        self.__micrometers_per_minutes = self.__convert_from_base(SpeedUnits.MicrometerPerMinute)
        return self.__micrometers_per_minutes

    
    @property
    def millimeters_per_minutes(self) -> float:
        """
        
        """
        if self.__millimeters_per_minutes != None:
            return self.__millimeters_per_minutes
        self.__millimeters_per_minutes = self.__convert_from_base(SpeedUnits.MillimeterPerMinute)
        return self.__millimeters_per_minutes

    
    @property
    def centimeters_per_minutes(self) -> float:
        """
        
        """
        if self.__centimeters_per_minutes != None:
            return self.__centimeters_per_minutes
        self.__centimeters_per_minutes = self.__convert_from_base(SpeedUnits.CentimeterPerMinute)
        return self.__centimeters_per_minutes

    
    @property
    def decimeters_per_minutes(self) -> float:
        """
        
        """
        if self.__decimeters_per_minutes != None:
            return self.__decimeters_per_minutes
        self.__decimeters_per_minutes = self.__convert_from_base(SpeedUnits.DecimeterPerMinute)
        return self.__decimeters_per_minutes

    
    @property
    def kilometers_per_minutes(self) -> float:
        """
        
        """
        if self.__kilometers_per_minutes != None:
            return self.__kilometers_per_minutes
        self.__kilometers_per_minutes = self.__convert_from_base(SpeedUnits.KilometerPerMinute)
        return self.__kilometers_per_minutes

    
    @property
    def millimeters_per_hour(self) -> float:
        """
        
        """
        if self.__millimeters_per_hour != None:
            return self.__millimeters_per_hour
        self.__millimeters_per_hour = self.__convert_from_base(SpeedUnits.MillimeterPerHour)
        return self.__millimeters_per_hour

    
    @property
    def centimeters_per_hour(self) -> float:
        """
        
        """
        if self.__centimeters_per_hour != None:
            return self.__centimeters_per_hour
        self.__centimeters_per_hour = self.__convert_from_base(SpeedUnits.CentimeterPerHour)
        return self.__centimeters_per_hour

    
    @property
    def kilometers_per_hour(self) -> float:
        """
        
        """
        if self.__kilometers_per_hour != None:
            return self.__kilometers_per_hour
        self.__kilometers_per_hour = self.__convert_from_base(SpeedUnits.KilometerPerHour)
        return self.__kilometers_per_hour

    
    def to_string(self, unit: SpeedUnits = SpeedUnits.MeterPerSecond, fractional_digits: int = None) -> str:
        """
        Format the Speed to a string.
        
        Note: the default format for Speed is MeterPerSecond.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the Speed. Default is 'MeterPerSecond'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == SpeedUnits.MeterPerSecond:
            return f"""{super()._truncate_fraction_digits(self.meters_per_second, fractional_digits)} m/s"""
        
        if unit == SpeedUnits.MeterPerMinute:
            return f"""{super()._truncate_fraction_digits(self.meters_per_minutes, fractional_digits)} m/min"""
        
        if unit == SpeedUnits.MeterPerHour:
            return f"""{super()._truncate_fraction_digits(self.meters_per_hour, fractional_digits)} m/h"""
        
        if unit == SpeedUnits.FootPerSecond:
            return f"""{super()._truncate_fraction_digits(self.feet_per_second, fractional_digits)} ft/s"""
        
        if unit == SpeedUnits.FootPerMinute:
            return f"""{super()._truncate_fraction_digits(self.feet_per_minute, fractional_digits)} ft/min"""
        
        if unit == SpeedUnits.FootPerHour:
            return f"""{super()._truncate_fraction_digits(self.feet_per_hour, fractional_digits)} ft/h"""
        
        if unit == SpeedUnits.UsSurveyFootPerSecond:
            return f"""{super()._truncate_fraction_digits(self.us_survey_feet_per_second, fractional_digits)} ftUS/s"""
        
        if unit == SpeedUnits.UsSurveyFootPerMinute:
            return f"""{super()._truncate_fraction_digits(self.us_survey_feet_per_minute, fractional_digits)} ftUS/min"""
        
        if unit == SpeedUnits.UsSurveyFootPerHour:
            return f"""{super()._truncate_fraction_digits(self.us_survey_feet_per_hour, fractional_digits)} ftUS/h"""
        
        if unit == SpeedUnits.InchPerSecond:
            return f"""{super()._truncate_fraction_digits(self.inches_per_second, fractional_digits)} in/s"""
        
        if unit == SpeedUnits.InchPerMinute:
            return f"""{super()._truncate_fraction_digits(self.inches_per_minute, fractional_digits)} in/min"""
        
        if unit == SpeedUnits.InchPerHour:
            return f"""{super()._truncate_fraction_digits(self.inches_per_hour, fractional_digits)} in/h"""
        
        if unit == SpeedUnits.YardPerSecond:
            return f"""{super()._truncate_fraction_digits(self.yards_per_second, fractional_digits)} yd/s"""
        
        if unit == SpeedUnits.YardPerMinute:
            return f"""{super()._truncate_fraction_digits(self.yards_per_minute, fractional_digits)} yd/min"""
        
        if unit == SpeedUnits.YardPerHour:
            return f"""{super()._truncate_fraction_digits(self.yards_per_hour, fractional_digits)} yd/h"""
        
        if unit == SpeedUnits.Knot:
            return f"""{super()._truncate_fraction_digits(self.knots, fractional_digits)} kn"""
        
        if unit == SpeedUnits.MilePerHour:
            return f"""{super()._truncate_fraction_digits(self.miles_per_hour, fractional_digits)} mph"""
        
        if unit == SpeedUnits.Mach:
            return f"""{super()._truncate_fraction_digits(self.mach, fractional_digits)} M"""
        
        if unit == SpeedUnits.NanometerPerSecond:
            return f"""{super()._truncate_fraction_digits(self.nanometers_per_second, fractional_digits)} nm/s"""
        
        if unit == SpeedUnits.MicrometerPerSecond:
            return f"""{super()._truncate_fraction_digits(self.micrometers_per_second, fractional_digits)} μm/s"""
        
        if unit == SpeedUnits.MillimeterPerSecond:
            return f"""{super()._truncate_fraction_digits(self.millimeters_per_second, fractional_digits)} mm/s"""
        
        if unit == SpeedUnits.CentimeterPerSecond:
            return f"""{super()._truncate_fraction_digits(self.centimeters_per_second, fractional_digits)} cm/s"""
        
        if unit == SpeedUnits.DecimeterPerSecond:
            return f"""{super()._truncate_fraction_digits(self.decimeters_per_second, fractional_digits)} dm/s"""
        
        if unit == SpeedUnits.KilometerPerSecond:
            return f"""{super()._truncate_fraction_digits(self.kilometers_per_second, fractional_digits)} km/s"""
        
        if unit == SpeedUnits.NanometerPerMinute:
            return f"""{super()._truncate_fraction_digits(self.nanometers_per_minutes, fractional_digits)} nm/min"""
        
        if unit == SpeedUnits.MicrometerPerMinute:
            return f"""{super()._truncate_fraction_digits(self.micrometers_per_minutes, fractional_digits)} μm/min"""
        
        if unit == SpeedUnits.MillimeterPerMinute:
            return f"""{super()._truncate_fraction_digits(self.millimeters_per_minutes, fractional_digits)} mm/min"""
        
        if unit == SpeedUnits.CentimeterPerMinute:
            return f"""{super()._truncate_fraction_digits(self.centimeters_per_minutes, fractional_digits)} cm/min"""
        
        if unit == SpeedUnits.DecimeterPerMinute:
            return f"""{super()._truncate_fraction_digits(self.decimeters_per_minutes, fractional_digits)} dm/min"""
        
        if unit == SpeedUnits.KilometerPerMinute:
            return f"""{super()._truncate_fraction_digits(self.kilometers_per_minutes, fractional_digits)} km/min"""
        
        if unit == SpeedUnits.MillimeterPerHour:
            return f"""{super()._truncate_fraction_digits(self.millimeters_per_hour, fractional_digits)} mm/h"""
        
        if unit == SpeedUnits.CentimeterPerHour:
            return f"""{super()._truncate_fraction_digits(self.centimeters_per_hour, fractional_digits)} cm/h"""
        
        if unit == SpeedUnits.KilometerPerHour:
            return f"""{super()._truncate_fraction_digits(self.kilometers_per_hour, fractional_digits)} km/h"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: SpeedUnits = SpeedUnits.MeterPerSecond) -> str:
        """
        Get Speed unit abbreviation.
        Note! the default abbreviation for Speed is MeterPerSecond.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == SpeedUnits.MeterPerSecond:
            return """m/s"""
        
        if unit_abbreviation == SpeedUnits.MeterPerMinute:
            return """m/min"""
        
        if unit_abbreviation == SpeedUnits.MeterPerHour:
            return """m/h"""
        
        if unit_abbreviation == SpeedUnits.FootPerSecond:
            return """ft/s"""
        
        if unit_abbreviation == SpeedUnits.FootPerMinute:
            return """ft/min"""
        
        if unit_abbreviation == SpeedUnits.FootPerHour:
            return """ft/h"""
        
        if unit_abbreviation == SpeedUnits.UsSurveyFootPerSecond:
            return """ftUS/s"""
        
        if unit_abbreviation == SpeedUnits.UsSurveyFootPerMinute:
            return """ftUS/min"""
        
        if unit_abbreviation == SpeedUnits.UsSurveyFootPerHour:
            return """ftUS/h"""
        
        if unit_abbreviation == SpeedUnits.InchPerSecond:
            return """in/s"""
        
        if unit_abbreviation == SpeedUnits.InchPerMinute:
            return """in/min"""
        
        if unit_abbreviation == SpeedUnits.InchPerHour:
            return """in/h"""
        
        if unit_abbreviation == SpeedUnits.YardPerSecond:
            return """yd/s"""
        
        if unit_abbreviation == SpeedUnits.YardPerMinute:
            return """yd/min"""
        
        if unit_abbreviation == SpeedUnits.YardPerHour:
            return """yd/h"""
        
        if unit_abbreviation == SpeedUnits.Knot:
            return """kn"""
        
        if unit_abbreviation == SpeedUnits.MilePerHour:
            return """mph"""
        
        if unit_abbreviation == SpeedUnits.Mach:
            return """M"""
        
        if unit_abbreviation == SpeedUnits.NanometerPerSecond:
            return """nm/s"""
        
        if unit_abbreviation == SpeedUnits.MicrometerPerSecond:
            return """μm/s"""
        
        if unit_abbreviation == SpeedUnits.MillimeterPerSecond:
            return """mm/s"""
        
        if unit_abbreviation == SpeedUnits.CentimeterPerSecond:
            return """cm/s"""
        
        if unit_abbreviation == SpeedUnits.DecimeterPerSecond:
            return """dm/s"""
        
        if unit_abbreviation == SpeedUnits.KilometerPerSecond:
            return """km/s"""
        
        if unit_abbreviation == SpeedUnits.NanometerPerMinute:
            return """nm/min"""
        
        if unit_abbreviation == SpeedUnits.MicrometerPerMinute:
            return """μm/min"""
        
        if unit_abbreviation == SpeedUnits.MillimeterPerMinute:
            return """mm/min"""
        
        if unit_abbreviation == SpeedUnits.CentimeterPerMinute:
            return """cm/min"""
        
        if unit_abbreviation == SpeedUnits.DecimeterPerMinute:
            return """dm/min"""
        
        if unit_abbreviation == SpeedUnits.KilometerPerMinute:
            return """km/min"""
        
        if unit_abbreviation == SpeedUnits.MillimeterPerHour:
            return """mm/h"""
        
        if unit_abbreviation == SpeedUnits.CentimeterPerHour:
            return """cm/h"""
        
        if unit_abbreviation == SpeedUnits.KilometerPerHour:
            return """km/h"""
        
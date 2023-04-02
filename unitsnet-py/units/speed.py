from enum import Enum
import math
import string


class SpeedUnits(Enum):
        """
            SpeedUnits enumeration
        """
        
        MeterPerSecond = 'meter_per_second'
        """
            
        """
        
        MeterPerMinute = 'meter_per_minute'
        """
            
        """
        
        MeterPerHour = 'meter_per_hour'
        """
            
        """
        
        FootPerSecond = 'foot_per_second'
        """
            
        """
        
        FootPerMinute = 'foot_per_minute'
        """
            
        """
        
        FootPerHour = 'foot_per_hour'
        """
            
        """
        
        UsSurveyFootPerSecond = 'us_survey_foot_per_second'
        """
            
        """
        
        UsSurveyFootPerMinute = 'us_survey_foot_per_minute'
        """
            
        """
        
        UsSurveyFootPerHour = 'us_survey_foot_per_hour'
        """
            
        """
        
        InchPerSecond = 'inch_per_second'
        """
            
        """
        
        InchPerMinute = 'inch_per_minute'
        """
            
        """
        
        InchPerHour = 'inch_per_hour'
        """
            
        """
        
        YardPerSecond = 'yard_per_second'
        """
            
        """
        
        YardPerMinute = 'yard_per_minute'
        """
            
        """
        
        YardPerHour = 'yard_per_hour'
        """
            
        """
        
        Knot = 'knot'
        """
            The knot, by definition, is a unit of speed equals to 1 nautical mile per hour, which is exactly 1852.000 metres per hour. The length of the internationally agreed nautical mile is 1852 m. The US adopted the international definition in 1954, the UK adopted the international nautical mile definition in 1970.
        """
        
        MilePerHour = 'mile_per_hour'
        """
            
        """
        
        Mach = 'mach'
        """
            
        """
        
        NanoMeterPerSecond = 'nano_meter_per_second'
        """
            
        """
        
        MicroMeterPerSecond = 'micro_meter_per_second'
        """
            
        """
        
        MilliMeterPerSecond = 'milli_meter_per_second'
        """
            
        """
        
        CentiMeterPerSecond = 'centi_meter_per_second'
        """
            
        """
        
        DeciMeterPerSecond = 'deci_meter_per_second'
        """
            
        """
        
        KiloMeterPerSecond = 'kilo_meter_per_second'
        """
            
        """
        
        NanoMeterPerMinute = 'nano_meter_per_minute'
        """
            
        """
        
        MicroMeterPerMinute = 'micro_meter_per_minute'
        """
            
        """
        
        MilliMeterPerMinute = 'milli_meter_per_minute'
        """
            
        """
        
        CentiMeterPerMinute = 'centi_meter_per_minute'
        """
            
        """
        
        DeciMeterPerMinute = 'deci_meter_per_minute'
        """
            
        """
        
        KiloMeterPerMinute = 'kilo_meter_per_minute'
        """
            
        """
        
        MilliMeterPerHour = 'milli_meter_per_hour'
        """
            
        """
        
        CentiMeterPerHour = 'centi_meter_per_hour'
        """
            
        """
        
        KiloMeterPerHour = 'kilo_meter_per_hour'
        """
            
        """
        

class Speed:
    """
    In everyday use and in kinematics, the speed of an object is the magnitude of its velocity (the rate of change of its position); it is thus a scalar quantity.[1] The average speed of an object in an interval of time is the distance travelled by the object divided by the duration of the interval;[2] the instantaneous speed is the limit of the average speed as the duration of the time interval approaches zero.

    Args:
        value (float): The value.
        from_unit (SpeedUnits): The Speed unit to create from, The default unit is MeterPerSecond
    """
    def __init__(self, value: float, from_unit: SpeedUnits = SpeedUnits.MeterPerSecond):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
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
        
        self.__nano_meters_per_second = None
        
        self.__micro_meters_per_second = None
        
        self.__milli_meters_per_second = None
        
        self.__centi_meters_per_second = None
        
        self.__deci_meters_per_second = None
        
        self.__kilo_meters_per_second = None
        
        self.__nano_meters_per_minutes = None
        
        self.__micro_meters_per_minutes = None
        
        self.__milli_meters_per_minutes = None
        
        self.__centi_meters_per_minutes = None
        
        self.__deci_meters_per_minutes = None
        
        self.__kilo_meters_per_minutes = None
        
        self.__milli_meters_per_hour = None
        
        self.__centi_meters_per_hour = None
        
        self.__kilo_meters_per_hour = None
        

    def __convert_from_base(self, from_unit: SpeedUnits) -> float:
        value = self.__value
        
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
        
        if from_unit == SpeedUnits.NanoMeterPerSecond:
            return ((value) / 1e-09)
        
        if from_unit == SpeedUnits.MicroMeterPerSecond:
            return ((value) / 1e-06)
        
        if from_unit == SpeedUnits.MilliMeterPerSecond:
            return ((value) / 0.001)
        
        if from_unit == SpeedUnits.CentiMeterPerSecond:
            return ((value) / 0.01)
        
        if from_unit == SpeedUnits.DeciMeterPerSecond:
            return ((value) / 0.1)
        
        if from_unit == SpeedUnits.KiloMeterPerSecond:
            return ((value) / 1000.0)
        
        if from_unit == SpeedUnits.NanoMeterPerMinute:
            return ((value * 60) / 1e-09)
        
        if from_unit == SpeedUnits.MicroMeterPerMinute:
            return ((value * 60) / 1e-06)
        
        if from_unit == SpeedUnits.MilliMeterPerMinute:
            return ((value * 60) / 0.001)
        
        if from_unit == SpeedUnits.CentiMeterPerMinute:
            return ((value * 60) / 0.01)
        
        if from_unit == SpeedUnits.DeciMeterPerMinute:
            return ((value * 60) / 0.1)
        
        if from_unit == SpeedUnits.KiloMeterPerMinute:
            return ((value * 60) / 1000.0)
        
        if from_unit == SpeedUnits.MilliMeterPerHour:
            return ((value * 3600) / 0.001)
        
        if from_unit == SpeedUnits.CentiMeterPerHour:
            return ((value * 3600) / 0.01)
        
        if from_unit == SpeedUnits.KiloMeterPerHour:
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
        
        if to_unit == SpeedUnits.NanoMeterPerSecond:
            return ((value) * 1e-09)
        
        if to_unit == SpeedUnits.MicroMeterPerSecond:
            return ((value) * 1e-06)
        
        if to_unit == SpeedUnits.MilliMeterPerSecond:
            return ((value) * 0.001)
        
        if to_unit == SpeedUnits.CentiMeterPerSecond:
            return ((value) * 0.01)
        
        if to_unit == SpeedUnits.DeciMeterPerSecond:
            return ((value) * 0.1)
        
        if to_unit == SpeedUnits.KiloMeterPerSecond:
            return ((value) * 1000.0)
        
        if to_unit == SpeedUnits.NanoMeterPerMinute:
            return ((value / 60) * 1e-09)
        
        if to_unit == SpeedUnits.MicroMeterPerMinute:
            return ((value / 60) * 1e-06)
        
        if to_unit == SpeedUnits.MilliMeterPerMinute:
            return ((value / 60) * 0.001)
        
        if to_unit == SpeedUnits.CentiMeterPerMinute:
            return ((value / 60) * 0.01)
        
        if to_unit == SpeedUnits.DeciMeterPerMinute:
            return ((value / 60) * 0.1)
        
        if to_unit == SpeedUnits.KiloMeterPerMinute:
            return ((value / 60) * 1000.0)
        
        if to_unit == SpeedUnits.MilliMeterPerHour:
            return ((value / 3600) * 0.001)
        
        if to_unit == SpeedUnits.CentiMeterPerHour:
            return ((value / 3600) * 0.01)
        
        if to_unit == SpeedUnits.KiloMeterPerHour:
            return ((value / 3600) * 1000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
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
    def from_nano_meters_per_second(nano_meters_per_second: float):
        """
        Create a new instance of Speed from a value in nano_meters_per_second.

        

        :param meters: The Speed value in nano_meters_per_second.
        :type nano_meters_per_second: float
        :return: A new instance of Speed.
        :rtype: Speed
        """
        return Speed(nano_meters_per_second, SpeedUnits.NanoMeterPerSecond)

    
    @staticmethod
    def from_micro_meters_per_second(micro_meters_per_second: float):
        """
        Create a new instance of Speed from a value in micro_meters_per_second.

        

        :param meters: The Speed value in micro_meters_per_second.
        :type micro_meters_per_second: float
        :return: A new instance of Speed.
        :rtype: Speed
        """
        return Speed(micro_meters_per_second, SpeedUnits.MicroMeterPerSecond)

    
    @staticmethod
    def from_milli_meters_per_second(milli_meters_per_second: float):
        """
        Create a new instance of Speed from a value in milli_meters_per_second.

        

        :param meters: The Speed value in milli_meters_per_second.
        :type milli_meters_per_second: float
        :return: A new instance of Speed.
        :rtype: Speed
        """
        return Speed(milli_meters_per_second, SpeedUnits.MilliMeterPerSecond)

    
    @staticmethod
    def from_centi_meters_per_second(centi_meters_per_second: float):
        """
        Create a new instance of Speed from a value in centi_meters_per_second.

        

        :param meters: The Speed value in centi_meters_per_second.
        :type centi_meters_per_second: float
        :return: A new instance of Speed.
        :rtype: Speed
        """
        return Speed(centi_meters_per_second, SpeedUnits.CentiMeterPerSecond)

    
    @staticmethod
    def from_deci_meters_per_second(deci_meters_per_second: float):
        """
        Create a new instance of Speed from a value in deci_meters_per_second.

        

        :param meters: The Speed value in deci_meters_per_second.
        :type deci_meters_per_second: float
        :return: A new instance of Speed.
        :rtype: Speed
        """
        return Speed(deci_meters_per_second, SpeedUnits.DeciMeterPerSecond)

    
    @staticmethod
    def from_kilo_meters_per_second(kilo_meters_per_second: float):
        """
        Create a new instance of Speed from a value in kilo_meters_per_second.

        

        :param meters: The Speed value in kilo_meters_per_second.
        :type kilo_meters_per_second: float
        :return: A new instance of Speed.
        :rtype: Speed
        """
        return Speed(kilo_meters_per_second, SpeedUnits.KiloMeterPerSecond)

    
    @staticmethod
    def from_nano_meters_per_minutes(nano_meters_per_minutes: float):
        """
        Create a new instance of Speed from a value in nano_meters_per_minutes.

        

        :param meters: The Speed value in nano_meters_per_minutes.
        :type nano_meters_per_minutes: float
        :return: A new instance of Speed.
        :rtype: Speed
        """
        return Speed(nano_meters_per_minutes, SpeedUnits.NanoMeterPerMinute)

    
    @staticmethod
    def from_micro_meters_per_minutes(micro_meters_per_minutes: float):
        """
        Create a new instance of Speed from a value in micro_meters_per_minutes.

        

        :param meters: The Speed value in micro_meters_per_minutes.
        :type micro_meters_per_minutes: float
        :return: A new instance of Speed.
        :rtype: Speed
        """
        return Speed(micro_meters_per_minutes, SpeedUnits.MicroMeterPerMinute)

    
    @staticmethod
    def from_milli_meters_per_minutes(milli_meters_per_minutes: float):
        """
        Create a new instance of Speed from a value in milli_meters_per_minutes.

        

        :param meters: The Speed value in milli_meters_per_minutes.
        :type milli_meters_per_minutes: float
        :return: A new instance of Speed.
        :rtype: Speed
        """
        return Speed(milli_meters_per_minutes, SpeedUnits.MilliMeterPerMinute)

    
    @staticmethod
    def from_centi_meters_per_minutes(centi_meters_per_minutes: float):
        """
        Create a new instance of Speed from a value in centi_meters_per_minutes.

        

        :param meters: The Speed value in centi_meters_per_minutes.
        :type centi_meters_per_minutes: float
        :return: A new instance of Speed.
        :rtype: Speed
        """
        return Speed(centi_meters_per_minutes, SpeedUnits.CentiMeterPerMinute)

    
    @staticmethod
    def from_deci_meters_per_minutes(deci_meters_per_minutes: float):
        """
        Create a new instance of Speed from a value in deci_meters_per_minutes.

        

        :param meters: The Speed value in deci_meters_per_minutes.
        :type deci_meters_per_minutes: float
        :return: A new instance of Speed.
        :rtype: Speed
        """
        return Speed(deci_meters_per_minutes, SpeedUnits.DeciMeterPerMinute)

    
    @staticmethod
    def from_kilo_meters_per_minutes(kilo_meters_per_minutes: float):
        """
        Create a new instance of Speed from a value in kilo_meters_per_minutes.

        

        :param meters: The Speed value in kilo_meters_per_minutes.
        :type kilo_meters_per_minutes: float
        :return: A new instance of Speed.
        :rtype: Speed
        """
        return Speed(kilo_meters_per_minutes, SpeedUnits.KiloMeterPerMinute)

    
    @staticmethod
    def from_milli_meters_per_hour(milli_meters_per_hour: float):
        """
        Create a new instance of Speed from a value in milli_meters_per_hour.

        

        :param meters: The Speed value in milli_meters_per_hour.
        :type milli_meters_per_hour: float
        :return: A new instance of Speed.
        :rtype: Speed
        """
        return Speed(milli_meters_per_hour, SpeedUnits.MilliMeterPerHour)

    
    @staticmethod
    def from_centi_meters_per_hour(centi_meters_per_hour: float):
        """
        Create a new instance of Speed from a value in centi_meters_per_hour.

        

        :param meters: The Speed value in centi_meters_per_hour.
        :type centi_meters_per_hour: float
        :return: A new instance of Speed.
        :rtype: Speed
        """
        return Speed(centi_meters_per_hour, SpeedUnits.CentiMeterPerHour)

    
    @staticmethod
    def from_kilo_meters_per_hour(kilo_meters_per_hour: float):
        """
        Create a new instance of Speed from a value in kilo_meters_per_hour.

        

        :param meters: The Speed value in kilo_meters_per_hour.
        :type kilo_meters_per_hour: float
        :return: A new instance of Speed.
        :rtype: Speed
        """
        return Speed(kilo_meters_per_hour, SpeedUnits.KiloMeterPerHour)

    
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
    def nano_meters_per_second(self) -> float:
        """
        
        """
        if self.__nano_meters_per_second != None:
            return self.__nano_meters_per_second
        self.__nano_meters_per_second = self.__convert_from_base(SpeedUnits.NanoMeterPerSecond)
        return self.__nano_meters_per_second

    
    @property
    def micro_meters_per_second(self) -> float:
        """
        
        """
        if self.__micro_meters_per_second != None:
            return self.__micro_meters_per_second
        self.__micro_meters_per_second = self.__convert_from_base(SpeedUnits.MicroMeterPerSecond)
        return self.__micro_meters_per_second

    
    @property
    def milli_meters_per_second(self) -> float:
        """
        
        """
        if self.__milli_meters_per_second != None:
            return self.__milli_meters_per_second
        self.__milli_meters_per_second = self.__convert_from_base(SpeedUnits.MilliMeterPerSecond)
        return self.__milli_meters_per_second

    
    @property
    def centi_meters_per_second(self) -> float:
        """
        
        """
        if self.__centi_meters_per_second != None:
            return self.__centi_meters_per_second
        self.__centi_meters_per_second = self.__convert_from_base(SpeedUnits.CentiMeterPerSecond)
        return self.__centi_meters_per_second

    
    @property
    def deci_meters_per_second(self) -> float:
        """
        
        """
        if self.__deci_meters_per_second != None:
            return self.__deci_meters_per_second
        self.__deci_meters_per_second = self.__convert_from_base(SpeedUnits.DeciMeterPerSecond)
        return self.__deci_meters_per_second

    
    @property
    def kilo_meters_per_second(self) -> float:
        """
        
        """
        if self.__kilo_meters_per_second != None:
            return self.__kilo_meters_per_second
        self.__kilo_meters_per_second = self.__convert_from_base(SpeedUnits.KiloMeterPerSecond)
        return self.__kilo_meters_per_second

    
    @property
    def nano_meters_per_minutes(self) -> float:
        """
        
        """
        if self.__nano_meters_per_minutes != None:
            return self.__nano_meters_per_minutes
        self.__nano_meters_per_minutes = self.__convert_from_base(SpeedUnits.NanoMeterPerMinute)
        return self.__nano_meters_per_minutes

    
    @property
    def micro_meters_per_minutes(self) -> float:
        """
        
        """
        if self.__micro_meters_per_minutes != None:
            return self.__micro_meters_per_minutes
        self.__micro_meters_per_minutes = self.__convert_from_base(SpeedUnits.MicroMeterPerMinute)
        return self.__micro_meters_per_minutes

    
    @property
    def milli_meters_per_minutes(self) -> float:
        """
        
        """
        if self.__milli_meters_per_minutes != None:
            return self.__milli_meters_per_minutes
        self.__milli_meters_per_minutes = self.__convert_from_base(SpeedUnits.MilliMeterPerMinute)
        return self.__milli_meters_per_minutes

    
    @property
    def centi_meters_per_minutes(self) -> float:
        """
        
        """
        if self.__centi_meters_per_minutes != None:
            return self.__centi_meters_per_minutes
        self.__centi_meters_per_minutes = self.__convert_from_base(SpeedUnits.CentiMeterPerMinute)
        return self.__centi_meters_per_minutes

    
    @property
    def deci_meters_per_minutes(self) -> float:
        """
        
        """
        if self.__deci_meters_per_minutes != None:
            return self.__deci_meters_per_minutes
        self.__deci_meters_per_minutes = self.__convert_from_base(SpeedUnits.DeciMeterPerMinute)
        return self.__deci_meters_per_minutes

    
    @property
    def kilo_meters_per_minutes(self) -> float:
        """
        
        """
        if self.__kilo_meters_per_minutes != None:
            return self.__kilo_meters_per_minutes
        self.__kilo_meters_per_minutes = self.__convert_from_base(SpeedUnits.KiloMeterPerMinute)
        return self.__kilo_meters_per_minutes

    
    @property
    def milli_meters_per_hour(self) -> float:
        """
        
        """
        if self.__milli_meters_per_hour != None:
            return self.__milli_meters_per_hour
        self.__milli_meters_per_hour = self.__convert_from_base(SpeedUnits.MilliMeterPerHour)
        return self.__milli_meters_per_hour

    
    @property
    def centi_meters_per_hour(self) -> float:
        """
        
        """
        if self.__centi_meters_per_hour != None:
            return self.__centi_meters_per_hour
        self.__centi_meters_per_hour = self.__convert_from_base(SpeedUnits.CentiMeterPerHour)
        return self.__centi_meters_per_hour

    
    @property
    def kilo_meters_per_hour(self) -> float:
        """
        
        """
        if self.__kilo_meters_per_hour != None:
            return self.__kilo_meters_per_hour
        self.__kilo_meters_per_hour = self.__convert_from_base(SpeedUnits.KiloMeterPerHour)
        return self.__kilo_meters_per_hour

    
    def to_string(self, unit: SpeedUnits = SpeedUnits.MeterPerSecond) -> string:
        """
        Format the Speed to string.
        Note! the default format for Speed is MeterPerSecond.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == SpeedUnits.MeterPerSecond:
            return f"""{self.meters_per_second} m/s"""
        
        if unit == SpeedUnits.MeterPerMinute:
            return f"""{self.meters_per_minutes} m/min"""
        
        if unit == SpeedUnits.MeterPerHour:
            return f"""{self.meters_per_hour} m/h"""
        
        if unit == SpeedUnits.FootPerSecond:
            return f"""{self.feet_per_second} ft/s"""
        
        if unit == SpeedUnits.FootPerMinute:
            return f"""{self.feet_per_minute} ft/min"""
        
        if unit == SpeedUnits.FootPerHour:
            return f"""{self.feet_per_hour} ft/h"""
        
        if unit == SpeedUnits.UsSurveyFootPerSecond:
            return f"""{self.us_survey_feet_per_second} ftUS/s"""
        
        if unit == SpeedUnits.UsSurveyFootPerMinute:
            return f"""{self.us_survey_feet_per_minute} ftUS/min"""
        
        if unit == SpeedUnits.UsSurveyFootPerHour:
            return f"""{self.us_survey_feet_per_hour} ftUS/h"""
        
        if unit == SpeedUnits.InchPerSecond:
            return f"""{self.inches_per_second} in/s"""
        
        if unit == SpeedUnits.InchPerMinute:
            return f"""{self.inches_per_minute} in/min"""
        
        if unit == SpeedUnits.InchPerHour:
            return f"""{self.inches_per_hour} in/h"""
        
        if unit == SpeedUnits.YardPerSecond:
            return f"""{self.yards_per_second} yd/s"""
        
        if unit == SpeedUnits.YardPerMinute:
            return f"""{self.yards_per_minute} yd/min"""
        
        if unit == SpeedUnits.YardPerHour:
            return f"""{self.yards_per_hour} yd/h"""
        
        if unit == SpeedUnits.Knot:
            return f"""{self.knots} kn"""
        
        if unit == SpeedUnits.MilePerHour:
            return f"""{self.miles_per_hour} mph"""
        
        if unit == SpeedUnits.Mach:
            return f"""{self.mach} M"""
        
        if unit == SpeedUnits.NanoMeterPerSecond:
            return f"""{self.nano_meters_per_second} """
        
        if unit == SpeedUnits.MicroMeterPerSecond:
            return f"""{self.micro_meters_per_second} """
        
        if unit == SpeedUnits.MilliMeterPerSecond:
            return f"""{self.milli_meters_per_second} """
        
        if unit == SpeedUnits.CentiMeterPerSecond:
            return f"""{self.centi_meters_per_second} """
        
        if unit == SpeedUnits.DeciMeterPerSecond:
            return f"""{self.deci_meters_per_second} """
        
        if unit == SpeedUnits.KiloMeterPerSecond:
            return f"""{self.kilo_meters_per_second} """
        
        if unit == SpeedUnits.NanoMeterPerMinute:
            return f"""{self.nano_meters_per_minutes} """
        
        if unit == SpeedUnits.MicroMeterPerMinute:
            return f"""{self.micro_meters_per_minutes} """
        
        if unit == SpeedUnits.MilliMeterPerMinute:
            return f"""{self.milli_meters_per_minutes} """
        
        if unit == SpeedUnits.CentiMeterPerMinute:
            return f"""{self.centi_meters_per_minutes} """
        
        if unit == SpeedUnits.DeciMeterPerMinute:
            return f"""{self.deci_meters_per_minutes} """
        
        if unit == SpeedUnits.KiloMeterPerMinute:
            return f"""{self.kilo_meters_per_minutes} """
        
        if unit == SpeedUnits.MilliMeterPerHour:
            return f"""{self.milli_meters_per_hour} """
        
        if unit == SpeedUnits.CentiMeterPerHour:
            return f"""{self.centi_meters_per_hour} """
        
        if unit == SpeedUnits.KiloMeterPerHour:
            return f"""{self.kilo_meters_per_hour} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: SpeedUnits = SpeedUnits.MeterPerSecond) -> string:
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
        
        if unit_abbreviation == SpeedUnits.NanoMeterPerSecond:
            return """"""
        
        if unit_abbreviation == SpeedUnits.MicroMeterPerSecond:
            return """"""
        
        if unit_abbreviation == SpeedUnits.MilliMeterPerSecond:
            return """"""
        
        if unit_abbreviation == SpeedUnits.CentiMeterPerSecond:
            return """"""
        
        if unit_abbreviation == SpeedUnits.DeciMeterPerSecond:
            return """"""
        
        if unit_abbreviation == SpeedUnits.KiloMeterPerSecond:
            return """"""
        
        if unit_abbreviation == SpeedUnits.NanoMeterPerMinute:
            return """"""
        
        if unit_abbreviation == SpeedUnits.MicroMeterPerMinute:
            return """"""
        
        if unit_abbreviation == SpeedUnits.MilliMeterPerMinute:
            return """"""
        
        if unit_abbreviation == SpeedUnits.CentiMeterPerMinute:
            return """"""
        
        if unit_abbreviation == SpeedUnits.DeciMeterPerMinute:
            return """"""
        
        if unit_abbreviation == SpeedUnits.KiloMeterPerMinute:
            return """"""
        
        if unit_abbreviation == SpeedUnits.MilliMeterPerHour:
            return """"""
        
        if unit_abbreviation == SpeedUnits.CentiMeterPerHour:
            return """"""
        
        if unit_abbreviation == SpeedUnits.KiloMeterPerHour:
            return """"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, Speed):
            raise TypeError("unsupported operand type(s) for +: 'Speed' and '{}'".format(type(other).__name__))
        return Speed(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, Speed):
            raise TypeError("unsupported operand type(s) for *: 'Speed' and '{}'".format(type(other).__name__))
        return Speed(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, Speed):
            raise TypeError("unsupported operand type(s) for -: 'Speed' and '{}'".format(type(other).__name__))
        return Speed(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, Speed):
            raise TypeError("unsupported operand type(s) for /: 'Speed' and '{}'".format(type(other).__name__))
        return Speed(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, Speed):
            raise TypeError("unsupported operand type(s) for %: 'Speed' and '{}'".format(type(other).__name__))
        return Speed(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, Speed):
            raise TypeError("unsupported operand type(s) for **: 'Speed' and '{}'".format(type(other).__name__))
        return Speed(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, Speed):
            raise TypeError("unsupported operand type(s) for ==: 'Speed' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, Speed):
            raise TypeError("unsupported operand type(s) for <: 'Speed' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, Speed):
            raise TypeError("unsupported operand type(s) for >: 'Speed' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, Speed):
            raise TypeError("unsupported operand type(s) for <=: 'Speed' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, Speed):
            raise TypeError("unsupported operand type(s) for >=: 'Speed' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value
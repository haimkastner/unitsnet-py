from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class DurationUnits(Enum):
        """
            DurationUnits enumeration
        """
        
        Year365 = 'year365'
        """
            
        """
        
        Month30 = 'month30'
        """
            
        """
        
        Week = 'week'
        """
            
        """
        
        Day = 'day'
        """
            
        """
        
        Hour = 'hour'
        """
            
        """
        
        Minute = 'minute'
        """
            
        """
        
        Second = 'second'
        """
            
        """
        
        JulianYear = 'julian_year'
        """
            
        """
        
        Nanosecond = 'nanosecond'
        """
            
        """
        
        Microsecond = 'microsecond'
        """
            
        """
        
        Millisecond = 'millisecond'
        """
            
        """
        

class Duration(AbstractMeasure):
    """
    Time is a dimension in which events can be ordered from the past through the present into the future, and also the measure of durations of events and the intervals between them.

    Args:
        value (float): The value.
        from_unit (DurationUnits): The Duration unit to create from, The default unit is Second
    """
    def __init__(self, value: float, from_unit: DurationUnits = DurationUnits.Second):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__years365 = None
        
        self.__months30 = None
        
        self.__weeks = None
        
        self.__days = None
        
        self.__hours = None
        
        self.__minutes = None
        
        self.__seconds = None
        
        self.__julian_years = None
        
        self.__nanoseconds = None
        
        self.__microseconds = None
        
        self.__milliseconds = None
        

    def convert(self, unit: DurationUnits) -> float:
        return self.__convert_from_base(unit)

    def __convert_from_base(self, from_unit: DurationUnits) -> float:
        value = self._value
        
        if from_unit == DurationUnits.Year365:
            return (value / (365 * 24 * 3600))
        
        if from_unit == DurationUnits.Month30:
            return (value / (30 * 24 * 3600))
        
        if from_unit == DurationUnits.Week:
            return (value / (7 * 24 * 3600))
        
        if from_unit == DurationUnits.Day:
            return (value / (24 * 3600))
        
        if from_unit == DurationUnits.Hour:
            return (value / 3600)
        
        if from_unit == DurationUnits.Minute:
            return (value / 60)
        
        if from_unit == DurationUnits.Second:
            return (value)
        
        if from_unit == DurationUnits.JulianYear:
            return (value / (365.25 * 24 * 3600))
        
        if from_unit == DurationUnits.Nanosecond:
            return ((value) / 1e-09)
        
        if from_unit == DurationUnits.Microsecond:
            return ((value) / 1e-06)
        
        if from_unit == DurationUnits.Millisecond:
            return ((value) / 0.001)
        
        return None


    def __convert_to_base(self, value: float, to_unit: DurationUnits) -> float:
        
        if to_unit == DurationUnits.Year365:
            return (value * 365 * 24 * 3600)
        
        if to_unit == DurationUnits.Month30:
            return (value * 30 * 24 * 3600)
        
        if to_unit == DurationUnits.Week:
            return (value * 7 * 24 * 3600)
        
        if to_unit == DurationUnits.Day:
            return (value * 24 * 3600)
        
        if to_unit == DurationUnits.Hour:
            return (value * 3600)
        
        if to_unit == DurationUnits.Minute:
            return (value * 60)
        
        if to_unit == DurationUnits.Second:
            return (value)
        
        if to_unit == DurationUnits.JulianYear:
            return (value * 365.25 * 24 * 3600)
        
        if to_unit == DurationUnits.Nanosecond:
            return ((value) * 1e-09)
        
        if to_unit == DurationUnits.Microsecond:
            return ((value) * 1e-06)
        
        if to_unit == DurationUnits.Millisecond:
            return ((value) * 0.001)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_years365(years365: float):
        """
        Create a new instance of Duration from a value in years365.

        

        :param meters: The Duration value in years365.
        :type years365: float
        :return: A new instance of Duration.
        :rtype: Duration
        """
        return Duration(years365, DurationUnits.Year365)

    
    @staticmethod
    def from_months30(months30: float):
        """
        Create a new instance of Duration from a value in months30.

        

        :param meters: The Duration value in months30.
        :type months30: float
        :return: A new instance of Duration.
        :rtype: Duration
        """
        return Duration(months30, DurationUnits.Month30)

    
    @staticmethod
    def from_weeks(weeks: float):
        """
        Create a new instance of Duration from a value in weeks.

        

        :param meters: The Duration value in weeks.
        :type weeks: float
        :return: A new instance of Duration.
        :rtype: Duration
        """
        return Duration(weeks, DurationUnits.Week)

    
    @staticmethod
    def from_days(days: float):
        """
        Create a new instance of Duration from a value in days.

        

        :param meters: The Duration value in days.
        :type days: float
        :return: A new instance of Duration.
        :rtype: Duration
        """
        return Duration(days, DurationUnits.Day)

    
    @staticmethod
    def from_hours(hours: float):
        """
        Create a new instance of Duration from a value in hours.

        

        :param meters: The Duration value in hours.
        :type hours: float
        :return: A new instance of Duration.
        :rtype: Duration
        """
        return Duration(hours, DurationUnits.Hour)

    
    @staticmethod
    def from_minutes(minutes: float):
        """
        Create a new instance of Duration from a value in minutes.

        

        :param meters: The Duration value in minutes.
        :type minutes: float
        :return: A new instance of Duration.
        :rtype: Duration
        """
        return Duration(minutes, DurationUnits.Minute)

    
    @staticmethod
    def from_seconds(seconds: float):
        """
        Create a new instance of Duration from a value in seconds.

        

        :param meters: The Duration value in seconds.
        :type seconds: float
        :return: A new instance of Duration.
        :rtype: Duration
        """
        return Duration(seconds, DurationUnits.Second)

    
    @staticmethod
    def from_julian_years(julian_years: float):
        """
        Create a new instance of Duration from a value in julian_years.

        

        :param meters: The Duration value in julian_years.
        :type julian_years: float
        :return: A new instance of Duration.
        :rtype: Duration
        """
        return Duration(julian_years, DurationUnits.JulianYear)

    
    @staticmethod
    def from_nanoseconds(nanoseconds: float):
        """
        Create a new instance of Duration from a value in nanoseconds.

        

        :param meters: The Duration value in nanoseconds.
        :type nanoseconds: float
        :return: A new instance of Duration.
        :rtype: Duration
        """
        return Duration(nanoseconds, DurationUnits.Nanosecond)

    
    @staticmethod
    def from_microseconds(microseconds: float):
        """
        Create a new instance of Duration from a value in microseconds.

        

        :param meters: The Duration value in microseconds.
        :type microseconds: float
        :return: A new instance of Duration.
        :rtype: Duration
        """
        return Duration(microseconds, DurationUnits.Microsecond)

    
    @staticmethod
    def from_milliseconds(milliseconds: float):
        """
        Create a new instance of Duration from a value in milliseconds.

        

        :param meters: The Duration value in milliseconds.
        :type milliseconds: float
        :return: A new instance of Duration.
        :rtype: Duration
        """
        return Duration(milliseconds, DurationUnits.Millisecond)

    
    @property
    def years365(self) -> float:
        """
        
        """
        if self.__years365 != None:
            return self.__years365
        self.__years365 = self.__convert_from_base(DurationUnits.Year365)
        return self.__years365

    
    @property
    def months30(self) -> float:
        """
        
        """
        if self.__months30 != None:
            return self.__months30
        self.__months30 = self.__convert_from_base(DurationUnits.Month30)
        return self.__months30

    
    @property
    def weeks(self) -> float:
        """
        
        """
        if self.__weeks != None:
            return self.__weeks
        self.__weeks = self.__convert_from_base(DurationUnits.Week)
        return self.__weeks

    
    @property
    def days(self) -> float:
        """
        
        """
        if self.__days != None:
            return self.__days
        self.__days = self.__convert_from_base(DurationUnits.Day)
        return self.__days

    
    @property
    def hours(self) -> float:
        """
        
        """
        if self.__hours != None:
            return self.__hours
        self.__hours = self.__convert_from_base(DurationUnits.Hour)
        return self.__hours

    
    @property
    def minutes(self) -> float:
        """
        
        """
        if self.__minutes != None:
            return self.__minutes
        self.__minutes = self.__convert_from_base(DurationUnits.Minute)
        return self.__minutes

    
    @property
    def seconds(self) -> float:
        """
        
        """
        if self.__seconds != None:
            return self.__seconds
        self.__seconds = self.__convert_from_base(DurationUnits.Second)
        return self.__seconds

    
    @property
    def julian_years(self) -> float:
        """
        
        """
        if self.__julian_years != None:
            return self.__julian_years
        self.__julian_years = self.__convert_from_base(DurationUnits.JulianYear)
        return self.__julian_years

    
    @property
    def nanoseconds(self) -> float:
        """
        
        """
        if self.__nanoseconds != None:
            return self.__nanoseconds
        self.__nanoseconds = self.__convert_from_base(DurationUnits.Nanosecond)
        return self.__nanoseconds

    
    @property
    def microseconds(self) -> float:
        """
        
        """
        if self.__microseconds != None:
            return self.__microseconds
        self.__microseconds = self.__convert_from_base(DurationUnits.Microsecond)
        return self.__microseconds

    
    @property
    def milliseconds(self) -> float:
        """
        
        """
        if self.__milliseconds != None:
            return self.__milliseconds
        self.__milliseconds = self.__convert_from_base(DurationUnits.Millisecond)
        return self.__milliseconds

    
    def to_string(self, unit: DurationUnits = DurationUnits.Second) -> str:
        """
        Format the Duration to string.
        Note! the default format for Duration is Second.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == DurationUnits.Year365:
            return f"""{self.years365} yr"""
        
        if unit == DurationUnits.Month30:
            return f"""{self.months30} mo"""
        
        if unit == DurationUnits.Week:
            return f"""{self.weeks} wk"""
        
        if unit == DurationUnits.Day:
            return f"""{self.days} d"""
        
        if unit == DurationUnits.Hour:
            return f"""{self.hours} h"""
        
        if unit == DurationUnits.Minute:
            return f"""{self.minutes} m"""
        
        if unit == DurationUnits.Second:
            return f"""{self.seconds} s"""
        
        if unit == DurationUnits.JulianYear:
            return f"""{self.julian_years} jyr"""
        
        if unit == DurationUnits.Nanosecond:
            return f"""{self.nanoseconds} ns"""
        
        if unit == DurationUnits.Microsecond:
            return f"""{self.microseconds} μs"""
        
        if unit == DurationUnits.Millisecond:
            return f"""{self.milliseconds} ms"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: DurationUnits = DurationUnits.Second) -> str:
        """
        Get Duration unit abbreviation.
        Note! the default abbreviation for Duration is Second.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == DurationUnits.Year365:
            return """yr"""
        
        if unit_abbreviation == DurationUnits.Month30:
            return """mo"""
        
        if unit_abbreviation == DurationUnits.Week:
            return """wk"""
        
        if unit_abbreviation == DurationUnits.Day:
            return """d"""
        
        if unit_abbreviation == DurationUnits.Hour:
            return """h"""
        
        if unit_abbreviation == DurationUnits.Minute:
            return """m"""
        
        if unit_abbreviation == DurationUnits.Second:
            return """s"""
        
        if unit_abbreviation == DurationUnits.JulianYear:
            return """jyr"""
        
        if unit_abbreviation == DurationUnits.Nanosecond:
            return """ns"""
        
        if unit_abbreviation == DurationUnits.Microsecond:
            return """μs"""
        
        if unit_abbreviation == DurationUnits.Millisecond:
            return """ms"""
        
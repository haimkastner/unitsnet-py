from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class DurationUnits(Enum):
        """
            DurationUnits enumeration
        """
        
        Year365 = 'Year365'
        """
            
        """
        
        Month30 = 'Month30'
        """
            
        """
        
        Week = 'Week'
        """
            
        """
        
        Day = 'Day'
        """
            
        """
        
        Hour = 'Hour'
        """
            
        """
        
        Minute = 'Minute'
        """
            
        """
        
        Second = 'Second'
        """
            
        """
        
        JulianYear = 'JulianYear'
        """
            
        """
        
        Sol = 'Sol'
        """
            
        """
        
        Nanosecond = 'Nanosecond'
        """
            
        """
        
        Microsecond = 'Microsecond'
        """
            
        """
        
        Millisecond = 'Millisecond'
        """
            
        """
        

class DurationDto:
    """
    A DTO representation of a Duration

    Attributes:
        value (float): The value of the Duration.
        unit (DurationUnits): The specific unit that the Duration value is representing.
    """

    def __init__(self, value: float, unit: DurationUnits):
        """
        Create a new DTO representation of a Duration

        Parameters:
            value (float): The value of the Duration.
            unit (DurationUnits): The specific unit that the Duration value is representing.
        """
        self.value: float = value
        """
        The value of the Duration
        """
        self.unit: DurationUnits = unit
        """
        The specific unit that the Duration value is representing
        """

    def to_json(self):
        """
        Get a Duration DTO JSON object representing the current unit.

        :return: JSON object represents Duration DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "Second"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of Duration DTO from a json representation.

        :param data: The Duration DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "Second"}
        :return: A new instance of DurationDto.
        :rtype: DurationDto
        """
        return DurationDto(value=data["value"], unit=DurationUnits(data["unit"]))


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
        
        self.__sols = None
        
        self.__nanoseconds = None
        
        self.__microseconds = None
        
        self.__milliseconds = None
        

    def convert(self, unit: DurationUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: DurationUnits = DurationUnits.Second) -> DurationDto:
        """
        Get a new instance of Duration DTO representing the current unit.

        :param hold_in_unit: The specific Duration unit to store the Duration value in the DTO representation.
        :type hold_in_unit: DurationUnits
        :return: A new instance of DurationDto.
        :rtype: DurationDto
        """
        return DurationDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: DurationUnits = DurationUnits.Second):
        """
        Get a Duration DTO JSON object representing the current unit.

        :param hold_in_unit: The specific Duration unit to store the Duration value in the DTO representation.
        :type hold_in_unit: DurationUnits
        :return: JSON object represents Duration DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "Second"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(duration_dto: DurationDto):
        """
        Obtain a new instance of Duration from a DTO unit object.

        :param duration_dto: The Duration DTO representation.
        :type duration_dto: DurationDto
        :return: A new instance of Duration.
        :rtype: Duration
        """
        return Duration(duration_dto.value, duration_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of Duration from a DTO unit json representation.

        :param data: The Duration DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "Second"}
        :return: A new instance of Duration.
        :rtype: Duration
        """
        return Duration.from_dto(DurationDto.from_json(data))

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
        
        if from_unit == DurationUnits.Sol:
            return (value / 88775.244)
        
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
        
        if to_unit == DurationUnits.Sol:
            return (value * 88775.244)
        
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
    def from_sols(sols: float):
        """
        Create a new instance of Duration from a value in sols.

        

        :param meters: The Duration value in sols.
        :type sols: float
        :return: A new instance of Duration.
        :rtype: Duration
        """
        return Duration(sols, DurationUnits.Sol)

    
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
    def sols(self) -> float:
        """
        
        """
        if self.__sols != None:
            return self.__sols
        self.__sols = self.__convert_from_base(DurationUnits.Sol)
        return self.__sols

    
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

    
    def to_string(self, unit: DurationUnits = DurationUnits.Second, fractional_digits: int = None) -> str:
        """
        Format the Duration to a string.
        
        Note: the default format for Duration is Second.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the Duration. Default is 'Second'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == DurationUnits.Year365:
            return f"""{super()._truncate_fraction_digits(self.years365, fractional_digits)} yr"""
        
        if unit == DurationUnits.Month30:
            return f"""{super()._truncate_fraction_digits(self.months30, fractional_digits)} mo"""
        
        if unit == DurationUnits.Week:
            return f"""{super()._truncate_fraction_digits(self.weeks, fractional_digits)} wk"""
        
        if unit == DurationUnits.Day:
            return f"""{super()._truncate_fraction_digits(self.days, fractional_digits)} d"""
        
        if unit == DurationUnits.Hour:
            return f"""{super()._truncate_fraction_digits(self.hours, fractional_digits)} h"""
        
        if unit == DurationUnits.Minute:
            return f"""{super()._truncate_fraction_digits(self.minutes, fractional_digits)} m"""
        
        if unit == DurationUnits.Second:
            return f"""{super()._truncate_fraction_digits(self.seconds, fractional_digits)} s"""
        
        if unit == DurationUnits.JulianYear:
            return f"""{super()._truncate_fraction_digits(self.julian_years, fractional_digits)} jyr"""
        
        if unit == DurationUnits.Sol:
            return f"""{super()._truncate_fraction_digits(self.sols, fractional_digits)} sol"""
        
        if unit == DurationUnits.Nanosecond:
            return f"""{super()._truncate_fraction_digits(self.nanoseconds, fractional_digits)} ns"""
        
        if unit == DurationUnits.Microsecond:
            return f"""{super()._truncate_fraction_digits(self.microseconds, fractional_digits)} μs"""
        
        if unit == DurationUnits.Millisecond:
            return f"""{super()._truncate_fraction_digits(self.milliseconds, fractional_digits)} ms"""
        
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
        
        if unit_abbreviation == DurationUnits.Sol:
            return """sol"""
        
        if unit_abbreviation == DurationUnits.Nanosecond:
            return """ns"""
        
        if unit_abbreviation == DurationUnits.Microsecond:
            return """μs"""
        
        if unit_abbreviation == DurationUnits.Millisecond:
            return """ms"""
        
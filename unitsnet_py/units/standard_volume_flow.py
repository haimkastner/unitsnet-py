from enum import Enum
import math
import string


class StandardVolumeFlowUnits(Enum):
        """
            StandardVolumeFlowUnits enumeration
        """
        
        StandardCubicMeterPerSecond = 'standard_cubic_meter_per_second'
        """
            
        """
        
        StandardCubicMeterPerMinute = 'standard_cubic_meter_per_minute'
        """
            
        """
        
        StandardCubicMeterPerHour = 'standard_cubic_meter_per_hour'
        """
            
        """
        
        StandardCubicMeterPerDay = 'standard_cubic_meter_per_day'
        """
            
        """
        
        StandardCubicCentimeterPerMinute = 'standard_cubic_centimeter_per_minute'
        """
            
        """
        
        StandardLiterPerMinute = 'standard_liter_per_minute'
        """
            
        """
        
        StandardCubicFootPerSecond = 'standard_cubic_foot_per_second'
        """
            
        """
        
        StandardCubicFootPerMinute = 'standard_cubic_foot_per_minute'
        """
            
        """
        
        StandardCubicFootPerHour = 'standard_cubic_foot_per_hour'
        """
            
        """
        

class StandardVolumeFlow:
    """
    The molar flow rate of a gas corrected to standardized conditions of temperature and pressure thus representing a fixed number of moles of gas regardless of composition and actual flow conditions.

    Args:
        value (float): The value.
        from_unit (StandardVolumeFlowUnits): The StandardVolumeFlow unit to create from, The default unit is StandardCubicMeterPerSecond
    """
    def __init__(self, value: float, from_unit: StandardVolumeFlowUnits = StandardVolumeFlowUnits.StandardCubicMeterPerSecond):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__standard_cubic_meters_per_second = None
        
        self.__standard_cubic_meters_per_minute = None
        
        self.__standard_cubic_meters_per_hour = None
        
        self.__standard_cubic_meters_per_day = None
        
        self.__standard_cubic_centimeters_per_minute = None
        
        self.__standard_liters_per_minute = None
        
        self.__standard_cubic_feet_per_second = None
        
        self.__standard_cubic_feet_per_minute = None
        
        self.__standard_cubic_feet_per_hour = None
        

    def __convert_from_base(self, from_unit: StandardVolumeFlowUnits) -> float:
        value = self.__value
        
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
        return self.__value

    
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

    
    def to_string(self, unit: StandardVolumeFlowUnits = StandardVolumeFlowUnits.StandardCubicMeterPerSecond) -> string:
        """
        Format the StandardVolumeFlow to string.
        Note! the default format for StandardVolumeFlow is StandardCubicMeterPerSecond.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == StandardVolumeFlowUnits.StandardCubicMeterPerSecond:
            return f"""{self.standard_cubic_meters_per_second} Sm³/s"""
        
        if unit == StandardVolumeFlowUnits.StandardCubicMeterPerMinute:
            return f"""{self.standard_cubic_meters_per_minute} Sm³/min"""
        
        if unit == StandardVolumeFlowUnits.StandardCubicMeterPerHour:
            return f"""{self.standard_cubic_meters_per_hour} Sm³/h"""
        
        if unit == StandardVolumeFlowUnits.StandardCubicMeterPerDay:
            return f"""{self.standard_cubic_meters_per_day} Sm³/d"""
        
        if unit == StandardVolumeFlowUnits.StandardCubicCentimeterPerMinute:
            return f"""{self.standard_cubic_centimeters_per_minute} sccm"""
        
        if unit == StandardVolumeFlowUnits.StandardLiterPerMinute:
            return f"""{self.standard_liters_per_minute} slm"""
        
        if unit == StandardVolumeFlowUnits.StandardCubicFootPerSecond:
            return f"""{self.standard_cubic_feet_per_second} Sft³/s"""
        
        if unit == StandardVolumeFlowUnits.StandardCubicFootPerMinute:
            return f"""{self.standard_cubic_feet_per_minute} scfm"""
        
        if unit == StandardVolumeFlowUnits.StandardCubicFootPerHour:
            return f"""{self.standard_cubic_feet_per_hour} scfh"""
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: StandardVolumeFlowUnits = StandardVolumeFlowUnits.StandardCubicMeterPerSecond) -> string:
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
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, StandardVolumeFlow):
            raise TypeError("unsupported operand type(s) for +: 'StandardVolumeFlow' and '{}'".format(type(other).__name__))
        return StandardVolumeFlow(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, StandardVolumeFlow):
            raise TypeError("unsupported operand type(s) for *: 'StandardVolumeFlow' and '{}'".format(type(other).__name__))
        return StandardVolumeFlow(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, StandardVolumeFlow):
            raise TypeError("unsupported operand type(s) for -: 'StandardVolumeFlow' and '{}'".format(type(other).__name__))
        return StandardVolumeFlow(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, StandardVolumeFlow):
            raise TypeError("unsupported operand type(s) for /: 'StandardVolumeFlow' and '{}'".format(type(other).__name__))
        return StandardVolumeFlow(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, StandardVolumeFlow):
            raise TypeError("unsupported operand type(s) for %: 'StandardVolumeFlow' and '{}'".format(type(other).__name__))
        return StandardVolumeFlow(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, StandardVolumeFlow):
            raise TypeError("unsupported operand type(s) for **: 'StandardVolumeFlow' and '{}'".format(type(other).__name__))
        return StandardVolumeFlow(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, StandardVolumeFlow):
            raise TypeError("unsupported operand type(s) for ==: 'StandardVolumeFlow' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, StandardVolumeFlow):
            raise TypeError("unsupported operand type(s) for <: 'StandardVolumeFlow' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, StandardVolumeFlow):
            raise TypeError("unsupported operand type(s) for >: 'StandardVolumeFlow' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, StandardVolumeFlow):
            raise TypeError("unsupported operand type(s) for <=: 'StandardVolumeFlow' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, StandardVolumeFlow):
            raise TypeError("unsupported operand type(s) for >=: 'StandardVolumeFlow' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value
from enum import Enum
import math
import string


class AccelerationUnits(Enum):
        """
            AccelerationUnits enumeration
        """
        
        MeterPerSecondSquared = 'meter_per_second_squared'
        """
            
        """
        
        InchPerSecondSquared = 'inch_per_second_squared'
        """
            
        """
        
        FootPerSecondSquared = 'foot_per_second_squared'
        """
            
        """
        
        KnotPerSecond = 'knot_per_second'
        """
            
        """
        
        KnotPerMinute = 'knot_per_minute'
        """
            
        """
        
        KnotPerHour = 'knot_per_hour'
        """
            
        """
        
        StandardGravity = 'standard_gravity'
        """
            
        """
        
        NanoMeterPerSecondSquared = 'nano_meter_per_second_squared'
        """
            
        """
        
        MicroMeterPerSecondSquared = 'micro_meter_per_second_squared'
        """
            
        """
        
        MilliMeterPerSecondSquared = 'milli_meter_per_second_squared'
        """
            
        """
        
        CentiMeterPerSecondSquared = 'centi_meter_per_second_squared'
        """
            
        """
        
        DeciMeterPerSecondSquared = 'deci_meter_per_second_squared'
        """
            
        """
        
        KiloMeterPerSecondSquared = 'kilo_meter_per_second_squared'
        """
            
        """
        
        MilliStandardGravity = 'milli_standard_gravity'
        """
            
        """
        
    
class Acceleration:
    """
    Acceleration, in physics, is the rate at which the velocity of an object changes over time. An object's acceleration is the net result of any and all forces acting on the object, as described by Newton's Second Law. The SI unit for acceleration is the Meter per second squared (m/s²). Accelerations are vector quantities (they have magnitude and direction) and add according to the parallelogram law. As a vector, the calculated net force is equal to the product of the object's mass (a scalar quantity) and the acceleration.

    Args:
        value (float): The value.
        from_unit (AccelerationUnits): The Acceleration unit to create from, The default unit is MeterPerSecondSquared
    """
    def __init__(self, value: float, from_unit: AccelerationUnits = AccelerationUnits.MeterPerSecondSquared):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__meters_per_second_squared = None
        
        self.__inches_per_second_squared = None
        
        self.__feet_per_second_squared = None
        
        self.__knots_per_second = None
        
        self.__knots_per_minute = None
        
        self.__knots_per_hour = None
        
        self.__standard_gravity = None
        
        self.__nano_meters_per_second_squared = None
        
        self.__micro_meters_per_second_squared = None
        
        self.__milli_meters_per_second_squared = None
        
        self.__centi_meters_per_second_squared = None
        
        self.__deci_meters_per_second_squared = None
        
        self.__kilo_meters_per_second_squared = None
        
        self.__milli_standard_gravity = None
        

    def __convert_from_base(self, from_unit: AccelerationUnits) -> float:
        value = self.__value
        
        if from_unit == AccelerationUnits.MeterPerSecondSquared:
            return (value)
        
        if from_unit == AccelerationUnits.InchPerSecondSquared:
            return (value / 0.0254)
        
        if from_unit == AccelerationUnits.FootPerSecondSquared:
            return (value / 0.304800)
        
        if from_unit == AccelerationUnits.KnotPerSecond:
            return (value / 0.5144444444444)
        
        if from_unit == AccelerationUnits.KnotPerMinute:
            return (value / 0.5144444444444 * 60)
        
        if from_unit == AccelerationUnits.KnotPerHour:
            return (value / 0.5144444444444 * 3600)
        
        if from_unit == AccelerationUnits.StandardGravity:
            return (value / 9.80665)
        
        if from_unit == AccelerationUnits.NanoMeterPerSecondSquared:
            return ((value) / 1e-09)
        
        if from_unit == AccelerationUnits.MicroMeterPerSecondSquared:
            return ((value) / 1e-06)
        
        if from_unit == AccelerationUnits.MilliMeterPerSecondSquared:
            return ((value) / 0.001)
        
        if from_unit == AccelerationUnits.CentiMeterPerSecondSquared:
            return ((value) / 0.01)
        
        if from_unit == AccelerationUnits.DeciMeterPerSecondSquared:
            return ((value) / 0.1)
        
        if from_unit == AccelerationUnits.KiloMeterPerSecondSquared:
            return ((value) / 1000.0)
        
        if from_unit == AccelerationUnits.MilliStandardGravity:
            return ((value / 9.80665) / 0.001)
        
        return None


    def __convert_to_base(self, value: float, to_unit: AccelerationUnits) -> float:
        
        if to_unit == AccelerationUnits.MeterPerSecondSquared:
            return (value)
        
        if to_unit == AccelerationUnits.InchPerSecondSquared:
            return (value * 0.0254)
        
        if to_unit == AccelerationUnits.FootPerSecondSquared:
            return (value * 0.304800)
        
        if to_unit == AccelerationUnits.KnotPerSecond:
            return (value * 0.5144444444444)
        
        if to_unit == AccelerationUnits.KnotPerMinute:
            return (value * 0.5144444444444 / 60)
        
        if to_unit == AccelerationUnits.KnotPerHour:
            return (value * 0.5144444444444 / 3600)
        
        if to_unit == AccelerationUnits.StandardGravity:
            return (value * 9.80665)
        
        if to_unit == AccelerationUnits.NanoMeterPerSecondSquared:
            return ((value) * 1e-09)
        
        if to_unit == AccelerationUnits.MicroMeterPerSecondSquared:
            return ((value) * 1e-06)
        
        if to_unit == AccelerationUnits.MilliMeterPerSecondSquared:
            return ((value) * 0.001)
        
        if to_unit == AccelerationUnits.CentiMeterPerSecondSquared:
            return ((value) * 0.01)
        
        if to_unit == AccelerationUnits.DeciMeterPerSecondSquared:
            return ((value) * 0.1)
        
        if to_unit == AccelerationUnits.KiloMeterPerSecondSquared:
            return ((value) * 1000.0)
        
        if to_unit == AccelerationUnits.MilliStandardGravity:
            return ((value * 9.80665) * 0.001)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
    @staticmethod
    def from_meters_per_second_squared(meters_per_second_squared: float):
        """
        Create a new instance of Acceleration from a value in meters_per_second_squared.

        

        :param meters: The Acceleration value in meters_per_second_squared.
        :type meters_per_second_squared: float
        :return: A new instance of Acceleration.
        :rtype: Acceleration
        """
        return Acceleration(meters_per_second_squared, AccelerationUnits.MeterPerSecondSquared)

    
    @staticmethod
    def from_inches_per_second_squared(inches_per_second_squared: float):
        """
        Create a new instance of Acceleration from a value in inches_per_second_squared.

        

        :param meters: The Acceleration value in inches_per_second_squared.
        :type inches_per_second_squared: float
        :return: A new instance of Acceleration.
        :rtype: Acceleration
        """
        return Acceleration(inches_per_second_squared, AccelerationUnits.InchPerSecondSquared)

    
    @staticmethod
    def from_feet_per_second_squared(feet_per_second_squared: float):
        """
        Create a new instance of Acceleration from a value in feet_per_second_squared.

        

        :param meters: The Acceleration value in feet_per_second_squared.
        :type feet_per_second_squared: float
        :return: A new instance of Acceleration.
        :rtype: Acceleration
        """
        return Acceleration(feet_per_second_squared, AccelerationUnits.FootPerSecondSquared)

    
    @staticmethod
    def from_knots_per_second(knots_per_second: float):
        """
        Create a new instance of Acceleration from a value in knots_per_second.

        

        :param meters: The Acceleration value in knots_per_second.
        :type knots_per_second: float
        :return: A new instance of Acceleration.
        :rtype: Acceleration
        """
        return Acceleration(knots_per_second, AccelerationUnits.KnotPerSecond)

    
    @staticmethod
    def from_knots_per_minute(knots_per_minute: float):
        """
        Create a new instance of Acceleration from a value in knots_per_minute.

        

        :param meters: The Acceleration value in knots_per_minute.
        :type knots_per_minute: float
        :return: A new instance of Acceleration.
        :rtype: Acceleration
        """
        return Acceleration(knots_per_minute, AccelerationUnits.KnotPerMinute)

    
    @staticmethod
    def from_knots_per_hour(knots_per_hour: float):
        """
        Create a new instance of Acceleration from a value in knots_per_hour.

        

        :param meters: The Acceleration value in knots_per_hour.
        :type knots_per_hour: float
        :return: A new instance of Acceleration.
        :rtype: Acceleration
        """
        return Acceleration(knots_per_hour, AccelerationUnits.KnotPerHour)

    
    @staticmethod
    def from_standard_gravity(standard_gravity: float):
        """
        Create a new instance of Acceleration from a value in standard_gravity.

        

        :param meters: The Acceleration value in standard_gravity.
        :type standard_gravity: float
        :return: A new instance of Acceleration.
        :rtype: Acceleration
        """
        return Acceleration(standard_gravity, AccelerationUnits.StandardGravity)

    
    @staticmethod
    def from_nano_meters_per_second_squared(nano_meters_per_second_squared: float):
        """
        Create a new instance of Acceleration from a value in nano_meters_per_second_squared.

        

        :param meters: The Acceleration value in nano_meters_per_second_squared.
        :type nano_meters_per_second_squared: float
        :return: A new instance of Acceleration.
        :rtype: Acceleration
        """
        return Acceleration(nano_meters_per_second_squared, AccelerationUnits.NanoMeterPerSecondSquared)

    
    @staticmethod
    def from_micro_meters_per_second_squared(micro_meters_per_second_squared: float):
        """
        Create a new instance of Acceleration from a value in micro_meters_per_second_squared.

        

        :param meters: The Acceleration value in micro_meters_per_second_squared.
        :type micro_meters_per_second_squared: float
        :return: A new instance of Acceleration.
        :rtype: Acceleration
        """
        return Acceleration(micro_meters_per_second_squared, AccelerationUnits.MicroMeterPerSecondSquared)

    
    @staticmethod
    def from_milli_meters_per_second_squared(milli_meters_per_second_squared: float):
        """
        Create a new instance of Acceleration from a value in milli_meters_per_second_squared.

        

        :param meters: The Acceleration value in milli_meters_per_second_squared.
        :type milli_meters_per_second_squared: float
        :return: A new instance of Acceleration.
        :rtype: Acceleration
        """
        return Acceleration(milli_meters_per_second_squared, AccelerationUnits.MilliMeterPerSecondSquared)

    
    @staticmethod
    def from_centi_meters_per_second_squared(centi_meters_per_second_squared: float):
        """
        Create a new instance of Acceleration from a value in centi_meters_per_second_squared.

        

        :param meters: The Acceleration value in centi_meters_per_second_squared.
        :type centi_meters_per_second_squared: float
        :return: A new instance of Acceleration.
        :rtype: Acceleration
        """
        return Acceleration(centi_meters_per_second_squared, AccelerationUnits.CentiMeterPerSecondSquared)

    
    @staticmethod
    def from_deci_meters_per_second_squared(deci_meters_per_second_squared: float):
        """
        Create a new instance of Acceleration from a value in deci_meters_per_second_squared.

        

        :param meters: The Acceleration value in deci_meters_per_second_squared.
        :type deci_meters_per_second_squared: float
        :return: A new instance of Acceleration.
        :rtype: Acceleration
        """
        return Acceleration(deci_meters_per_second_squared, AccelerationUnits.DeciMeterPerSecondSquared)

    
    @staticmethod
    def from_kilo_meters_per_second_squared(kilo_meters_per_second_squared: float):
        """
        Create a new instance of Acceleration from a value in kilo_meters_per_second_squared.

        

        :param meters: The Acceleration value in kilo_meters_per_second_squared.
        :type kilo_meters_per_second_squared: float
        :return: A new instance of Acceleration.
        :rtype: Acceleration
        """
        return Acceleration(kilo_meters_per_second_squared, AccelerationUnits.KiloMeterPerSecondSquared)

    
    @staticmethod
    def from_milli_standard_gravity(milli_standard_gravity: float):
        """
        Create a new instance of Acceleration from a value in milli_standard_gravity.

        

        :param meters: The Acceleration value in milli_standard_gravity.
        :type milli_standard_gravity: float
        :return: A new instance of Acceleration.
        :rtype: Acceleration
        """
        return Acceleration(milli_standard_gravity, AccelerationUnits.MilliStandardGravity)

    
    @property
    def meters_per_second_squared(self) -> float:
        """
        
        """
        if self.__meters_per_second_squared != None:
            return self.__meters_per_second_squared
        self.__meters_per_second_squared = self.__convert_from_base(AccelerationUnits.MeterPerSecondSquared)
        return self.__meters_per_second_squared

    
    @property
    def inches_per_second_squared(self) -> float:
        """
        
        """
        if self.__inches_per_second_squared != None:
            return self.__inches_per_second_squared
        self.__inches_per_second_squared = self.__convert_from_base(AccelerationUnits.InchPerSecondSquared)
        return self.__inches_per_second_squared

    
    @property
    def feet_per_second_squared(self) -> float:
        """
        
        """
        if self.__feet_per_second_squared != None:
            return self.__feet_per_second_squared
        self.__feet_per_second_squared = self.__convert_from_base(AccelerationUnits.FootPerSecondSquared)
        return self.__feet_per_second_squared

    
    @property
    def knots_per_second(self) -> float:
        """
        
        """
        if self.__knots_per_second != None:
            return self.__knots_per_second
        self.__knots_per_second = self.__convert_from_base(AccelerationUnits.KnotPerSecond)
        return self.__knots_per_second

    
    @property
    def knots_per_minute(self) -> float:
        """
        
        """
        if self.__knots_per_minute != None:
            return self.__knots_per_minute
        self.__knots_per_minute = self.__convert_from_base(AccelerationUnits.KnotPerMinute)
        return self.__knots_per_minute

    
    @property
    def knots_per_hour(self) -> float:
        """
        
        """
        if self.__knots_per_hour != None:
            return self.__knots_per_hour
        self.__knots_per_hour = self.__convert_from_base(AccelerationUnits.KnotPerHour)
        return self.__knots_per_hour

    
    @property
    def standard_gravity(self) -> float:
        """
        
        """
        if self.__standard_gravity != None:
            return self.__standard_gravity
        self.__standard_gravity = self.__convert_from_base(AccelerationUnits.StandardGravity)
        return self.__standard_gravity

    
    @property
    def nano_meters_per_second_squared(self) -> float:
        """
        
        """
        if self.__nano_meters_per_second_squared != None:
            return self.__nano_meters_per_second_squared
        self.__nano_meters_per_second_squared = self.__convert_from_base(AccelerationUnits.NanoMeterPerSecondSquared)
        return self.__nano_meters_per_second_squared

    
    @property
    def micro_meters_per_second_squared(self) -> float:
        """
        
        """
        if self.__micro_meters_per_second_squared != None:
            return self.__micro_meters_per_second_squared
        self.__micro_meters_per_second_squared = self.__convert_from_base(AccelerationUnits.MicroMeterPerSecondSquared)
        return self.__micro_meters_per_second_squared

    
    @property
    def milli_meters_per_second_squared(self) -> float:
        """
        
        """
        if self.__milli_meters_per_second_squared != None:
            return self.__milli_meters_per_second_squared
        self.__milli_meters_per_second_squared = self.__convert_from_base(AccelerationUnits.MilliMeterPerSecondSquared)
        return self.__milli_meters_per_second_squared

    
    @property
    def centi_meters_per_second_squared(self) -> float:
        """
        
        """
        if self.__centi_meters_per_second_squared != None:
            return self.__centi_meters_per_second_squared
        self.__centi_meters_per_second_squared = self.__convert_from_base(AccelerationUnits.CentiMeterPerSecondSquared)
        return self.__centi_meters_per_second_squared

    
    @property
    def deci_meters_per_second_squared(self) -> float:
        """
        
        """
        if self.__deci_meters_per_second_squared != None:
            return self.__deci_meters_per_second_squared
        self.__deci_meters_per_second_squared = self.__convert_from_base(AccelerationUnits.DeciMeterPerSecondSquared)
        return self.__deci_meters_per_second_squared

    
    @property
    def kilo_meters_per_second_squared(self) -> float:
        """
        
        """
        if self.__kilo_meters_per_second_squared != None:
            return self.__kilo_meters_per_second_squared
        self.__kilo_meters_per_second_squared = self.__convert_from_base(AccelerationUnits.KiloMeterPerSecondSquared)
        return self.__kilo_meters_per_second_squared

    
    @property
    def milli_standard_gravity(self) -> float:
        """
        
        """
        if self.__milli_standard_gravity != None:
            return self.__milli_standard_gravity
        self.__milli_standard_gravity = self.__convert_from_base(AccelerationUnits.MilliStandardGravity)
        return self.__milli_standard_gravity

    
    def to_string(self, unit: AccelerationUnits = AccelerationUnits.MeterPerSecondSquared) -> string:
        """
        Format the Acceleration to string.
        Note! the default format for Acceleration is MeterPerSecondSquared.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == AccelerationUnits.MeterPerSecondSquared:
            return f"""{self.meters_per_second_squared} m/s²"""
        
        if unit == AccelerationUnits.InchPerSecondSquared:
            return f"""{self.inches_per_second_squared} in/s²"""
        
        if unit == AccelerationUnits.FootPerSecondSquared:
            return f"""{self.feet_per_second_squared} ft/s²"""
        
        if unit == AccelerationUnits.KnotPerSecond:
            return f"""{self.knots_per_second} kn/s"""
        
        if unit == AccelerationUnits.KnotPerMinute:
            return f"""{self.knots_per_minute} kn/min"""
        
        if unit == AccelerationUnits.KnotPerHour:
            return f"""{self.knots_per_hour} kn/h"""
        
        if unit == AccelerationUnits.StandardGravity:
            return f"""{self.standard_gravity} g"""
        
        if unit == AccelerationUnits.NanoMeterPerSecondSquared:
            return f"""{self.nano_meters_per_second_squared} """
        
        if unit == AccelerationUnits.MicroMeterPerSecondSquared:
            return f"""{self.micro_meters_per_second_squared} """
        
        if unit == AccelerationUnits.MilliMeterPerSecondSquared:
            return f"""{self.milli_meters_per_second_squared} """
        
        if unit == AccelerationUnits.CentiMeterPerSecondSquared:
            return f"""{self.centi_meters_per_second_squared} """
        
        if unit == AccelerationUnits.DeciMeterPerSecondSquared:
            return f"""{self.deci_meters_per_second_squared} """
        
        if unit == AccelerationUnits.KiloMeterPerSecondSquared:
            return f"""{self.kilo_meters_per_second_squared} """
        
        if unit == AccelerationUnits.MilliStandardGravity:
            return f"""{self.milli_standard_gravity} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: AccelerationUnits = AccelerationUnits.MeterPerSecondSquared) -> string:
        """
        Get Acceleration unit abbreviation.
        Note! the default abbreviation for Acceleration is MeterPerSecondSquared.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == AccelerationUnits.MeterPerSecondSquared:
            return """m/s²"""
        
        if unit_abbreviation == AccelerationUnits.InchPerSecondSquared:
            return """in/s²"""
        
        if unit_abbreviation == AccelerationUnits.FootPerSecondSquared:
            return """ft/s²"""
        
        if unit_abbreviation == AccelerationUnits.KnotPerSecond:
            return """kn/s"""
        
        if unit_abbreviation == AccelerationUnits.KnotPerMinute:
            return """kn/min"""
        
        if unit_abbreviation == AccelerationUnits.KnotPerHour:
            return """kn/h"""
        
        if unit_abbreviation == AccelerationUnits.StandardGravity:
            return """g"""
        
        if unit_abbreviation == AccelerationUnits.NanoMeterPerSecondSquared:
            return """"""
        
        if unit_abbreviation == AccelerationUnits.MicroMeterPerSecondSquared:
            return """"""
        
        if unit_abbreviation == AccelerationUnits.MilliMeterPerSecondSquared:
            return """"""
        
        if unit_abbreviation == AccelerationUnits.CentiMeterPerSecondSquared:
            return """"""
        
        if unit_abbreviation == AccelerationUnits.DeciMeterPerSecondSquared:
            return """"""
        
        if unit_abbreviation == AccelerationUnits.KiloMeterPerSecondSquared:
            return """"""
        
        if unit_abbreviation == AccelerationUnits.MilliStandardGravity:
            return """"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, Acceleration):
            raise TypeError("unsupported operand type(s) for +: 'Acceleration' and '{}'".format(type(other).__name__))
        return Acceleration(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, Acceleration):
            raise TypeError("unsupported operand type(s) for *: 'Acceleration' and '{}'".format(type(other).__name__))
        return Acceleration(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, Acceleration):
            raise TypeError("unsupported operand type(s) for -: 'Acceleration' and '{}'".format(type(other).__name__))
        return Acceleration(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, Acceleration):
            raise TypeError("unsupported operand type(s) for /: 'Acceleration' and '{}'".format(type(other).__name__))
        return Acceleration(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, Acceleration):
            raise TypeError("unsupported operand type(s) for %: 'Acceleration' and '{}'".format(type(other).__name__))
        return Acceleration(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, Acceleration):
            raise TypeError("unsupported operand type(s) for **: 'Acceleration' and '{}'".format(type(other).__name__))
        return Acceleration(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, Acceleration):
            raise TypeError("unsupported operand type(s) for ==: 'Acceleration' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, Acceleration):
            raise TypeError("unsupported operand type(s) for <: 'Acceleration' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, Acceleration):
            raise TypeError("unsupported operand type(s) for >: 'Acceleration' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, Acceleration):
            raise TypeError("unsupported operand type(s) for <=: 'Acceleration' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, Acceleration):
            raise TypeError("unsupported operand type(s) for >=: 'Acceleration' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value
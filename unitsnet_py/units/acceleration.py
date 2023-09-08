from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



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
        
        NanometerPerSecondSquared = 'nanometer_per_second_squared'
        """
            
        """
        
        MicrometerPerSecondSquared = 'micrometer_per_second_squared'
        """
            
        """
        
        MillimeterPerSecondSquared = 'millimeter_per_second_squared'
        """
            
        """
        
        CentimeterPerSecondSquared = 'centimeter_per_second_squared'
        """
            
        """
        
        DecimeterPerSecondSquared = 'decimeter_per_second_squared'
        """
            
        """
        
        KilometerPerSecondSquared = 'kilometer_per_second_squared'
        """
            
        """
        
        MillistandardGravity = 'millistandard_gravity'
        """
            
        """
        

class Acceleration(AbstractMeasure):
    """
    Acceleration, in physics, is the rate at which the velocity of an object changes over time. An object's acceleration is the net result of any and all forces acting on the object, as described by Newton's Second Law. The SI unit for acceleration is the Meter per second squared (m/s²). Accelerations are vector quantities (they have magnitude and direction) and add according to the parallelogram law. As a vector, the calculated net force is equal to the product of the object's mass (a scalar quantity) and the acceleration.

    Args:
        value (float): The value.
        from_unit (AccelerationUnits): The Acceleration unit to create from, The default unit is MeterPerSecondSquared
    """
    def __init__(self, value: float, from_unit: AccelerationUnits = AccelerationUnits.MeterPerSecondSquared):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__meters_per_second_squared = None
        
        self.__inches_per_second_squared = None
        
        self.__feet_per_second_squared = None
        
        self.__knots_per_second = None
        
        self.__knots_per_minute = None
        
        self.__knots_per_hour = None
        
        self.__standard_gravity = None
        
        self.__nanometers_per_second_squared = None
        
        self.__micrometers_per_second_squared = None
        
        self.__millimeters_per_second_squared = None
        
        self.__centimeters_per_second_squared = None
        
        self.__decimeters_per_second_squared = None
        
        self.__kilometers_per_second_squared = None
        
        self.__millistandard_gravity = None
        

    def convert(self, unit: AccelerationUnits) -> float:
        return self.__convert_from_base(unit)

    def __convert_from_base(self, from_unit: AccelerationUnits) -> float:
        value = self._value
        
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
        
        if from_unit == AccelerationUnits.NanometerPerSecondSquared:
            return ((value) / 1e-09)
        
        if from_unit == AccelerationUnits.MicrometerPerSecondSquared:
            return ((value) / 1e-06)
        
        if from_unit == AccelerationUnits.MillimeterPerSecondSquared:
            return ((value) / 0.001)
        
        if from_unit == AccelerationUnits.CentimeterPerSecondSquared:
            return ((value) / 0.01)
        
        if from_unit == AccelerationUnits.DecimeterPerSecondSquared:
            return ((value) / 0.1)
        
        if from_unit == AccelerationUnits.KilometerPerSecondSquared:
            return ((value) / 1000.0)
        
        if from_unit == AccelerationUnits.MillistandardGravity:
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
        
        if to_unit == AccelerationUnits.NanometerPerSecondSquared:
            return ((value) * 1e-09)
        
        if to_unit == AccelerationUnits.MicrometerPerSecondSquared:
            return ((value) * 1e-06)
        
        if to_unit == AccelerationUnits.MillimeterPerSecondSquared:
            return ((value) * 0.001)
        
        if to_unit == AccelerationUnits.CentimeterPerSecondSquared:
            return ((value) * 0.01)
        
        if to_unit == AccelerationUnits.DecimeterPerSecondSquared:
            return ((value) * 0.1)
        
        if to_unit == AccelerationUnits.KilometerPerSecondSquared:
            return ((value) * 1000.0)
        
        if to_unit == AccelerationUnits.MillistandardGravity:
            return ((value * 9.80665) * 0.001)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
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
    def from_nanometers_per_second_squared(nanometers_per_second_squared: float):
        """
        Create a new instance of Acceleration from a value in nanometers_per_second_squared.

        

        :param meters: The Acceleration value in nanometers_per_second_squared.
        :type nanometers_per_second_squared: float
        :return: A new instance of Acceleration.
        :rtype: Acceleration
        """
        return Acceleration(nanometers_per_second_squared, AccelerationUnits.NanometerPerSecondSquared)

    
    @staticmethod
    def from_micrometers_per_second_squared(micrometers_per_second_squared: float):
        """
        Create a new instance of Acceleration from a value in micrometers_per_second_squared.

        

        :param meters: The Acceleration value in micrometers_per_second_squared.
        :type micrometers_per_second_squared: float
        :return: A new instance of Acceleration.
        :rtype: Acceleration
        """
        return Acceleration(micrometers_per_second_squared, AccelerationUnits.MicrometerPerSecondSquared)

    
    @staticmethod
    def from_millimeters_per_second_squared(millimeters_per_second_squared: float):
        """
        Create a new instance of Acceleration from a value in millimeters_per_second_squared.

        

        :param meters: The Acceleration value in millimeters_per_second_squared.
        :type millimeters_per_second_squared: float
        :return: A new instance of Acceleration.
        :rtype: Acceleration
        """
        return Acceleration(millimeters_per_second_squared, AccelerationUnits.MillimeterPerSecondSquared)

    
    @staticmethod
    def from_centimeters_per_second_squared(centimeters_per_second_squared: float):
        """
        Create a new instance of Acceleration from a value in centimeters_per_second_squared.

        

        :param meters: The Acceleration value in centimeters_per_second_squared.
        :type centimeters_per_second_squared: float
        :return: A new instance of Acceleration.
        :rtype: Acceleration
        """
        return Acceleration(centimeters_per_second_squared, AccelerationUnits.CentimeterPerSecondSquared)

    
    @staticmethod
    def from_decimeters_per_second_squared(decimeters_per_second_squared: float):
        """
        Create a new instance of Acceleration from a value in decimeters_per_second_squared.

        

        :param meters: The Acceleration value in decimeters_per_second_squared.
        :type decimeters_per_second_squared: float
        :return: A new instance of Acceleration.
        :rtype: Acceleration
        """
        return Acceleration(decimeters_per_second_squared, AccelerationUnits.DecimeterPerSecondSquared)

    
    @staticmethod
    def from_kilometers_per_second_squared(kilometers_per_second_squared: float):
        """
        Create a new instance of Acceleration from a value in kilometers_per_second_squared.

        

        :param meters: The Acceleration value in kilometers_per_second_squared.
        :type kilometers_per_second_squared: float
        :return: A new instance of Acceleration.
        :rtype: Acceleration
        """
        return Acceleration(kilometers_per_second_squared, AccelerationUnits.KilometerPerSecondSquared)

    
    @staticmethod
    def from_millistandard_gravity(millistandard_gravity: float):
        """
        Create a new instance of Acceleration from a value in millistandard_gravity.

        

        :param meters: The Acceleration value in millistandard_gravity.
        :type millistandard_gravity: float
        :return: A new instance of Acceleration.
        :rtype: Acceleration
        """
        return Acceleration(millistandard_gravity, AccelerationUnits.MillistandardGravity)

    
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
    def nanometers_per_second_squared(self) -> float:
        """
        
        """
        if self.__nanometers_per_second_squared != None:
            return self.__nanometers_per_second_squared
        self.__nanometers_per_second_squared = self.__convert_from_base(AccelerationUnits.NanometerPerSecondSquared)
        return self.__nanometers_per_second_squared

    
    @property
    def micrometers_per_second_squared(self) -> float:
        """
        
        """
        if self.__micrometers_per_second_squared != None:
            return self.__micrometers_per_second_squared
        self.__micrometers_per_second_squared = self.__convert_from_base(AccelerationUnits.MicrometerPerSecondSquared)
        return self.__micrometers_per_second_squared

    
    @property
    def millimeters_per_second_squared(self) -> float:
        """
        
        """
        if self.__millimeters_per_second_squared != None:
            return self.__millimeters_per_second_squared
        self.__millimeters_per_second_squared = self.__convert_from_base(AccelerationUnits.MillimeterPerSecondSquared)
        return self.__millimeters_per_second_squared

    
    @property
    def centimeters_per_second_squared(self) -> float:
        """
        
        """
        if self.__centimeters_per_second_squared != None:
            return self.__centimeters_per_second_squared
        self.__centimeters_per_second_squared = self.__convert_from_base(AccelerationUnits.CentimeterPerSecondSquared)
        return self.__centimeters_per_second_squared

    
    @property
    def decimeters_per_second_squared(self) -> float:
        """
        
        """
        if self.__decimeters_per_second_squared != None:
            return self.__decimeters_per_second_squared
        self.__decimeters_per_second_squared = self.__convert_from_base(AccelerationUnits.DecimeterPerSecondSquared)
        return self.__decimeters_per_second_squared

    
    @property
    def kilometers_per_second_squared(self) -> float:
        """
        
        """
        if self.__kilometers_per_second_squared != None:
            return self.__kilometers_per_second_squared
        self.__kilometers_per_second_squared = self.__convert_from_base(AccelerationUnits.KilometerPerSecondSquared)
        return self.__kilometers_per_second_squared

    
    @property
    def millistandard_gravity(self) -> float:
        """
        
        """
        if self.__millistandard_gravity != None:
            return self.__millistandard_gravity
        self.__millistandard_gravity = self.__convert_from_base(AccelerationUnits.MillistandardGravity)
        return self.__millistandard_gravity

    
    def to_string(self, unit: AccelerationUnits = AccelerationUnits.MeterPerSecondSquared) -> str:
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
        
        if unit == AccelerationUnits.NanometerPerSecondSquared:
            return f"""{self.nanometers_per_second_squared} nm/s²"""
        
        if unit == AccelerationUnits.MicrometerPerSecondSquared:
            return f"""{self.micrometers_per_second_squared} μm/s²"""
        
        if unit == AccelerationUnits.MillimeterPerSecondSquared:
            return f"""{self.millimeters_per_second_squared} mm/s²"""
        
        if unit == AccelerationUnits.CentimeterPerSecondSquared:
            return f"""{self.centimeters_per_second_squared} cm/s²"""
        
        if unit == AccelerationUnits.DecimeterPerSecondSquared:
            return f"""{self.decimeters_per_second_squared} dm/s²"""
        
        if unit == AccelerationUnits.KilometerPerSecondSquared:
            return f"""{self.kilometers_per_second_squared} km/s²"""
        
        if unit == AccelerationUnits.MillistandardGravity:
            return f"""{self.millistandard_gravity} mg"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: AccelerationUnits = AccelerationUnits.MeterPerSecondSquared) -> str:
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
        
        if unit_abbreviation == AccelerationUnits.NanometerPerSecondSquared:
            return """nm/s²"""
        
        if unit_abbreviation == AccelerationUnits.MicrometerPerSecondSquared:
            return """μm/s²"""
        
        if unit_abbreviation == AccelerationUnits.MillimeterPerSecondSquared:
            return """mm/s²"""
        
        if unit_abbreviation == AccelerationUnits.CentimeterPerSecondSquared:
            return """cm/s²"""
        
        if unit_abbreviation == AccelerationUnits.DecimeterPerSecondSquared:
            return """dm/s²"""
        
        if unit_abbreviation == AccelerationUnits.KilometerPerSecondSquared:
            return """km/s²"""
        
        if unit_abbreviation == AccelerationUnits.MillistandardGravity:
            return """mg"""
        
from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class RotationalSpeedUnits(Enum):
        """
            RotationalSpeedUnits enumeration
        """
        
        RadianPerSecond = 'radian_per_second'
        """
            
        """
        
        DegreePerSecond = 'degree_per_second'
        """
            
        """
        
        DegreePerMinute = 'degree_per_minute'
        """
            
        """
        
        RevolutionPerSecond = 'revolution_per_second'
        """
            
        """
        
        RevolutionPerMinute = 'revolution_per_minute'
        """
            
        """
        
        NanoradianPerSecond = 'nanoradian_per_second'
        """
            
        """
        
        MicroradianPerSecond = 'microradian_per_second'
        """
            
        """
        
        MilliradianPerSecond = 'milliradian_per_second'
        """
            
        """
        
        CentiradianPerSecond = 'centiradian_per_second'
        """
            
        """
        
        DeciradianPerSecond = 'deciradian_per_second'
        """
            
        """
        
        NanodegreePerSecond = 'nanodegree_per_second'
        """
            
        """
        
        MicrodegreePerSecond = 'microdegree_per_second'
        """
            
        """
        
        MillidegreePerSecond = 'millidegree_per_second'
        """
            
        """
        

class RotationalSpeed(AbstractMeasure):
    """
    Rotational speed (sometimes called speed of revolution) is the number of complete rotations, revolutions, cycles, or turns per time unit. Rotational speed is a cyclic frequency, measured in radians per second or in hertz in the SI System by scientists, or in revolutions per minute (rpm or min-1) or revolutions per second in everyday life. The symbol for rotational speed is ω (the Greek lowercase letter "omega").

    Args:
        value (float): The value.
        from_unit (RotationalSpeedUnits): The RotationalSpeed unit to create from, The default unit is RadianPerSecond
    """
    def __init__(self, value: float, from_unit: RotationalSpeedUnits = RotationalSpeedUnits.RadianPerSecond):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__radians_per_second = None
        
        self.__degrees_per_second = None
        
        self.__degrees_per_minute = None
        
        self.__revolutions_per_second = None
        
        self.__revolutions_per_minute = None
        
        self.__nanoradians_per_second = None
        
        self.__microradians_per_second = None
        
        self.__milliradians_per_second = None
        
        self.__centiradians_per_second = None
        
        self.__deciradians_per_second = None
        
        self.__nanodegrees_per_second = None
        
        self.__microdegrees_per_second = None
        
        self.__millidegrees_per_second = None
        

    def convert(self, unit: RotationalSpeedUnits) -> float:
        return self.__convert_from_base(unit)

    def __convert_from_base(self, from_unit: RotationalSpeedUnits) -> float:
        value = self._value
        
        if from_unit == RotationalSpeedUnits.RadianPerSecond:
            return (value)
        
        if from_unit == RotationalSpeedUnits.DegreePerSecond:
            return ((180 / math.pi) * value)
        
        if from_unit == RotationalSpeedUnits.DegreePerMinute:
            return ((180 * 60 / math.pi) * value)
        
        if from_unit == RotationalSpeedUnits.RevolutionPerSecond:
            return (value / 6.2831853072)
        
        if from_unit == RotationalSpeedUnits.RevolutionPerMinute:
            return ((value / 6.2831853072) * 60)
        
        if from_unit == RotationalSpeedUnits.NanoradianPerSecond:
            return ((value) / 1e-09)
        
        if from_unit == RotationalSpeedUnits.MicroradianPerSecond:
            return ((value) / 1e-06)
        
        if from_unit == RotationalSpeedUnits.MilliradianPerSecond:
            return ((value) / 0.001)
        
        if from_unit == RotationalSpeedUnits.CentiradianPerSecond:
            return ((value) / 0.01)
        
        if from_unit == RotationalSpeedUnits.DeciradianPerSecond:
            return ((value) / 0.1)
        
        if from_unit == RotationalSpeedUnits.NanodegreePerSecond:
            return (((180 / math.pi) * value) / 1e-09)
        
        if from_unit == RotationalSpeedUnits.MicrodegreePerSecond:
            return (((180 / math.pi) * value) / 1e-06)
        
        if from_unit == RotationalSpeedUnits.MillidegreePerSecond:
            return (((180 / math.pi) * value) / 0.001)
        
        return None


    def __convert_to_base(self, value: float, to_unit: RotationalSpeedUnits) -> float:
        
        if to_unit == RotationalSpeedUnits.RadianPerSecond:
            return (value)
        
        if to_unit == RotationalSpeedUnits.DegreePerSecond:
            return ((math.pi / 180) * value)
        
        if to_unit == RotationalSpeedUnits.DegreePerMinute:
            return ((math.pi / (180 * 60)) * value)
        
        if to_unit == RotationalSpeedUnits.RevolutionPerSecond:
            return (value * 6.2831853072)
        
        if to_unit == RotationalSpeedUnits.RevolutionPerMinute:
            return ((value * 6.2831853072) / 60)
        
        if to_unit == RotationalSpeedUnits.NanoradianPerSecond:
            return ((value) * 1e-09)
        
        if to_unit == RotationalSpeedUnits.MicroradianPerSecond:
            return ((value) * 1e-06)
        
        if to_unit == RotationalSpeedUnits.MilliradianPerSecond:
            return ((value) * 0.001)
        
        if to_unit == RotationalSpeedUnits.CentiradianPerSecond:
            return ((value) * 0.01)
        
        if to_unit == RotationalSpeedUnits.DeciradianPerSecond:
            return ((value) * 0.1)
        
        if to_unit == RotationalSpeedUnits.NanodegreePerSecond:
            return (((math.pi / 180) * value) * 1e-09)
        
        if to_unit == RotationalSpeedUnits.MicrodegreePerSecond:
            return (((math.pi / 180) * value) * 1e-06)
        
        if to_unit == RotationalSpeedUnits.MillidegreePerSecond:
            return (((math.pi / 180) * value) * 0.001)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_radians_per_second(radians_per_second: float):
        """
        Create a new instance of RotationalSpeed from a value in radians_per_second.

        

        :param meters: The RotationalSpeed value in radians_per_second.
        :type radians_per_second: float
        :return: A new instance of RotationalSpeed.
        :rtype: RotationalSpeed
        """
        return RotationalSpeed(radians_per_second, RotationalSpeedUnits.RadianPerSecond)

    
    @staticmethod
    def from_degrees_per_second(degrees_per_second: float):
        """
        Create a new instance of RotationalSpeed from a value in degrees_per_second.

        

        :param meters: The RotationalSpeed value in degrees_per_second.
        :type degrees_per_second: float
        :return: A new instance of RotationalSpeed.
        :rtype: RotationalSpeed
        """
        return RotationalSpeed(degrees_per_second, RotationalSpeedUnits.DegreePerSecond)

    
    @staticmethod
    def from_degrees_per_minute(degrees_per_minute: float):
        """
        Create a new instance of RotationalSpeed from a value in degrees_per_minute.

        

        :param meters: The RotationalSpeed value in degrees_per_minute.
        :type degrees_per_minute: float
        :return: A new instance of RotationalSpeed.
        :rtype: RotationalSpeed
        """
        return RotationalSpeed(degrees_per_minute, RotationalSpeedUnits.DegreePerMinute)

    
    @staticmethod
    def from_revolutions_per_second(revolutions_per_second: float):
        """
        Create a new instance of RotationalSpeed from a value in revolutions_per_second.

        

        :param meters: The RotationalSpeed value in revolutions_per_second.
        :type revolutions_per_second: float
        :return: A new instance of RotationalSpeed.
        :rtype: RotationalSpeed
        """
        return RotationalSpeed(revolutions_per_second, RotationalSpeedUnits.RevolutionPerSecond)

    
    @staticmethod
    def from_revolutions_per_minute(revolutions_per_minute: float):
        """
        Create a new instance of RotationalSpeed from a value in revolutions_per_minute.

        

        :param meters: The RotationalSpeed value in revolutions_per_minute.
        :type revolutions_per_minute: float
        :return: A new instance of RotationalSpeed.
        :rtype: RotationalSpeed
        """
        return RotationalSpeed(revolutions_per_minute, RotationalSpeedUnits.RevolutionPerMinute)

    
    @staticmethod
    def from_nanoradians_per_second(nanoradians_per_second: float):
        """
        Create a new instance of RotationalSpeed from a value in nanoradians_per_second.

        

        :param meters: The RotationalSpeed value in nanoradians_per_second.
        :type nanoradians_per_second: float
        :return: A new instance of RotationalSpeed.
        :rtype: RotationalSpeed
        """
        return RotationalSpeed(nanoradians_per_second, RotationalSpeedUnits.NanoradianPerSecond)

    
    @staticmethod
    def from_microradians_per_second(microradians_per_second: float):
        """
        Create a new instance of RotationalSpeed from a value in microradians_per_second.

        

        :param meters: The RotationalSpeed value in microradians_per_second.
        :type microradians_per_second: float
        :return: A new instance of RotationalSpeed.
        :rtype: RotationalSpeed
        """
        return RotationalSpeed(microradians_per_second, RotationalSpeedUnits.MicroradianPerSecond)

    
    @staticmethod
    def from_milliradians_per_second(milliradians_per_second: float):
        """
        Create a new instance of RotationalSpeed from a value in milliradians_per_second.

        

        :param meters: The RotationalSpeed value in milliradians_per_second.
        :type milliradians_per_second: float
        :return: A new instance of RotationalSpeed.
        :rtype: RotationalSpeed
        """
        return RotationalSpeed(milliradians_per_second, RotationalSpeedUnits.MilliradianPerSecond)

    
    @staticmethod
    def from_centiradians_per_second(centiradians_per_second: float):
        """
        Create a new instance of RotationalSpeed from a value in centiradians_per_second.

        

        :param meters: The RotationalSpeed value in centiradians_per_second.
        :type centiradians_per_second: float
        :return: A new instance of RotationalSpeed.
        :rtype: RotationalSpeed
        """
        return RotationalSpeed(centiradians_per_second, RotationalSpeedUnits.CentiradianPerSecond)

    
    @staticmethod
    def from_deciradians_per_second(deciradians_per_second: float):
        """
        Create a new instance of RotationalSpeed from a value in deciradians_per_second.

        

        :param meters: The RotationalSpeed value in deciradians_per_second.
        :type deciradians_per_second: float
        :return: A new instance of RotationalSpeed.
        :rtype: RotationalSpeed
        """
        return RotationalSpeed(deciradians_per_second, RotationalSpeedUnits.DeciradianPerSecond)

    
    @staticmethod
    def from_nanodegrees_per_second(nanodegrees_per_second: float):
        """
        Create a new instance of RotationalSpeed from a value in nanodegrees_per_second.

        

        :param meters: The RotationalSpeed value in nanodegrees_per_second.
        :type nanodegrees_per_second: float
        :return: A new instance of RotationalSpeed.
        :rtype: RotationalSpeed
        """
        return RotationalSpeed(nanodegrees_per_second, RotationalSpeedUnits.NanodegreePerSecond)

    
    @staticmethod
    def from_microdegrees_per_second(microdegrees_per_second: float):
        """
        Create a new instance of RotationalSpeed from a value in microdegrees_per_second.

        

        :param meters: The RotationalSpeed value in microdegrees_per_second.
        :type microdegrees_per_second: float
        :return: A new instance of RotationalSpeed.
        :rtype: RotationalSpeed
        """
        return RotationalSpeed(microdegrees_per_second, RotationalSpeedUnits.MicrodegreePerSecond)

    
    @staticmethod
    def from_millidegrees_per_second(millidegrees_per_second: float):
        """
        Create a new instance of RotationalSpeed from a value in millidegrees_per_second.

        

        :param meters: The RotationalSpeed value in millidegrees_per_second.
        :type millidegrees_per_second: float
        :return: A new instance of RotationalSpeed.
        :rtype: RotationalSpeed
        """
        return RotationalSpeed(millidegrees_per_second, RotationalSpeedUnits.MillidegreePerSecond)

    
    @property
    def radians_per_second(self) -> float:
        """
        
        """
        if self.__radians_per_second != None:
            return self.__radians_per_second
        self.__radians_per_second = self.__convert_from_base(RotationalSpeedUnits.RadianPerSecond)
        return self.__radians_per_second

    
    @property
    def degrees_per_second(self) -> float:
        """
        
        """
        if self.__degrees_per_second != None:
            return self.__degrees_per_second
        self.__degrees_per_second = self.__convert_from_base(RotationalSpeedUnits.DegreePerSecond)
        return self.__degrees_per_second

    
    @property
    def degrees_per_minute(self) -> float:
        """
        
        """
        if self.__degrees_per_minute != None:
            return self.__degrees_per_minute
        self.__degrees_per_minute = self.__convert_from_base(RotationalSpeedUnits.DegreePerMinute)
        return self.__degrees_per_minute

    
    @property
    def revolutions_per_second(self) -> float:
        """
        
        """
        if self.__revolutions_per_second != None:
            return self.__revolutions_per_second
        self.__revolutions_per_second = self.__convert_from_base(RotationalSpeedUnits.RevolutionPerSecond)
        return self.__revolutions_per_second

    
    @property
    def revolutions_per_minute(self) -> float:
        """
        
        """
        if self.__revolutions_per_minute != None:
            return self.__revolutions_per_minute
        self.__revolutions_per_minute = self.__convert_from_base(RotationalSpeedUnits.RevolutionPerMinute)
        return self.__revolutions_per_minute

    
    @property
    def nanoradians_per_second(self) -> float:
        """
        
        """
        if self.__nanoradians_per_second != None:
            return self.__nanoradians_per_second
        self.__nanoradians_per_second = self.__convert_from_base(RotationalSpeedUnits.NanoradianPerSecond)
        return self.__nanoradians_per_second

    
    @property
    def microradians_per_second(self) -> float:
        """
        
        """
        if self.__microradians_per_second != None:
            return self.__microradians_per_second
        self.__microradians_per_second = self.__convert_from_base(RotationalSpeedUnits.MicroradianPerSecond)
        return self.__microradians_per_second

    
    @property
    def milliradians_per_second(self) -> float:
        """
        
        """
        if self.__milliradians_per_second != None:
            return self.__milliradians_per_second
        self.__milliradians_per_second = self.__convert_from_base(RotationalSpeedUnits.MilliradianPerSecond)
        return self.__milliradians_per_second

    
    @property
    def centiradians_per_second(self) -> float:
        """
        
        """
        if self.__centiradians_per_second != None:
            return self.__centiradians_per_second
        self.__centiradians_per_second = self.__convert_from_base(RotationalSpeedUnits.CentiradianPerSecond)
        return self.__centiradians_per_second

    
    @property
    def deciradians_per_second(self) -> float:
        """
        
        """
        if self.__deciradians_per_second != None:
            return self.__deciradians_per_second
        self.__deciradians_per_second = self.__convert_from_base(RotationalSpeedUnits.DeciradianPerSecond)
        return self.__deciradians_per_second

    
    @property
    def nanodegrees_per_second(self) -> float:
        """
        
        """
        if self.__nanodegrees_per_second != None:
            return self.__nanodegrees_per_second
        self.__nanodegrees_per_second = self.__convert_from_base(RotationalSpeedUnits.NanodegreePerSecond)
        return self.__nanodegrees_per_second

    
    @property
    def microdegrees_per_second(self) -> float:
        """
        
        """
        if self.__microdegrees_per_second != None:
            return self.__microdegrees_per_second
        self.__microdegrees_per_second = self.__convert_from_base(RotationalSpeedUnits.MicrodegreePerSecond)
        return self.__microdegrees_per_second

    
    @property
    def millidegrees_per_second(self) -> float:
        """
        
        """
        if self.__millidegrees_per_second != None:
            return self.__millidegrees_per_second
        self.__millidegrees_per_second = self.__convert_from_base(RotationalSpeedUnits.MillidegreePerSecond)
        return self.__millidegrees_per_second

    
    def to_string(self, unit: RotationalSpeedUnits = RotationalSpeedUnits.RadianPerSecond) -> str:
        """
        Format the RotationalSpeed to string.
        Note! the default format for RotationalSpeed is RadianPerSecond.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == RotationalSpeedUnits.RadianPerSecond:
            return f"""{self.radians_per_second} rad/s"""
        
        if unit == RotationalSpeedUnits.DegreePerSecond:
            return f"""{self.degrees_per_second} °/s"""
        
        if unit == RotationalSpeedUnits.DegreePerMinute:
            return f"""{self.degrees_per_minute} °/min"""
        
        if unit == RotationalSpeedUnits.RevolutionPerSecond:
            return f"""{self.revolutions_per_second} r/s"""
        
        if unit == RotationalSpeedUnits.RevolutionPerMinute:
            return f"""{self.revolutions_per_minute} rpm"""
        
        if unit == RotationalSpeedUnits.NanoradianPerSecond:
            return f"""{self.nanoradians_per_second} nrad/s"""
        
        if unit == RotationalSpeedUnits.MicroradianPerSecond:
            return f"""{self.microradians_per_second} μrad/s"""
        
        if unit == RotationalSpeedUnits.MilliradianPerSecond:
            return f"""{self.milliradians_per_second} mrad/s"""
        
        if unit == RotationalSpeedUnits.CentiradianPerSecond:
            return f"""{self.centiradians_per_second} crad/s"""
        
        if unit == RotationalSpeedUnits.DeciradianPerSecond:
            return f"""{self.deciradians_per_second} drad/s"""
        
        if unit == RotationalSpeedUnits.NanodegreePerSecond:
            return f"""{self.nanodegrees_per_second} n°/s"""
        
        if unit == RotationalSpeedUnits.MicrodegreePerSecond:
            return f"""{self.microdegrees_per_second} μ°/s"""
        
        if unit == RotationalSpeedUnits.MillidegreePerSecond:
            return f"""{self.millidegrees_per_second} m°/s"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: RotationalSpeedUnits = RotationalSpeedUnits.RadianPerSecond) -> str:
        """
        Get RotationalSpeed unit abbreviation.
        Note! the default abbreviation for RotationalSpeed is RadianPerSecond.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == RotationalSpeedUnits.RadianPerSecond:
            return """rad/s"""
        
        if unit_abbreviation == RotationalSpeedUnits.DegreePerSecond:
            return """°/s"""
        
        if unit_abbreviation == RotationalSpeedUnits.DegreePerMinute:
            return """°/min"""
        
        if unit_abbreviation == RotationalSpeedUnits.RevolutionPerSecond:
            return """r/s"""
        
        if unit_abbreviation == RotationalSpeedUnits.RevolutionPerMinute:
            return """rpm"""
        
        if unit_abbreviation == RotationalSpeedUnits.NanoradianPerSecond:
            return """nrad/s"""
        
        if unit_abbreviation == RotationalSpeedUnits.MicroradianPerSecond:
            return """μrad/s"""
        
        if unit_abbreviation == RotationalSpeedUnits.MilliradianPerSecond:
            return """mrad/s"""
        
        if unit_abbreviation == RotationalSpeedUnits.CentiradianPerSecond:
            return """crad/s"""
        
        if unit_abbreviation == RotationalSpeedUnits.DeciradianPerSecond:
            return """drad/s"""
        
        if unit_abbreviation == RotationalSpeedUnits.NanodegreePerSecond:
            return """n°/s"""
        
        if unit_abbreviation == RotationalSpeedUnits.MicrodegreePerSecond:
            return """μ°/s"""
        
        if unit_abbreviation == RotationalSpeedUnits.MillidegreePerSecond:
            return """m°/s"""
        
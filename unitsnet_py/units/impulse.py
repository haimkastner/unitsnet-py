from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class ImpulseUnits(Enum):
        """
            ImpulseUnits enumeration
        """
        
        KilogramMeterPerSecond = 'kilogram_meter_per_second'
        """
            
        """
        
        NewtonSecond = 'newton_second'
        """
            
        """
        
        PoundFootPerSecond = 'pound_foot_per_second'
        """
            
        """
        
        PoundForceSecond = 'pound_force_second'
        """
            
        """
        
        SlugFootPerSecond = 'slug_foot_per_second'
        """
            
        """
        
        NanonewtonSecond = 'nanonewton_second'
        """
            
        """
        
        MicronewtonSecond = 'micronewton_second'
        """
            
        """
        
        MillinewtonSecond = 'millinewton_second'
        """
            
        """
        
        CentinewtonSecond = 'centinewton_second'
        """
            
        """
        
        DecinewtonSecond = 'decinewton_second'
        """
            
        """
        
        DecanewtonSecond = 'decanewton_second'
        """
            
        """
        
        KilonewtonSecond = 'kilonewton_second'
        """
            
        """
        
        MeganewtonSecond = 'meganewton_second'
        """
            
        """
        

class Impulse(AbstractMeasure):
    """
    In classical mechanics, impulse is the integral of a force, F, over the time interval, t, for which it acts. Impulse applied to an object produces an equivalent vector change in its linear momentum, also in the resultant direction.

    Args:
        value (float): The value.
        from_unit (ImpulseUnits): The Impulse unit to create from, The default unit is NewtonSecond
    """
    def __init__(self, value: float, from_unit: ImpulseUnits = ImpulseUnits.NewtonSecond):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__kilogram_meters_per_second = None
        
        self.__newton_seconds = None
        
        self.__pound_feet_per_second = None
        
        self.__pound_force_seconds = None
        
        self.__slug_feet_per_second = None
        
        self.__nanonewton_seconds = None
        
        self.__micronewton_seconds = None
        
        self.__millinewton_seconds = None
        
        self.__centinewton_seconds = None
        
        self.__decinewton_seconds = None
        
        self.__decanewton_seconds = None
        
        self.__kilonewton_seconds = None
        
        self.__meganewton_seconds = None
        

    def convert(self, unit: ImpulseUnits) -> float:
        return self.__convert_from_base(unit)

    def __convert_from_base(self, from_unit: ImpulseUnits) -> float:
        value = self._value
        
        if from_unit == ImpulseUnits.KilogramMeterPerSecond:
            return (value)
        
        if from_unit == ImpulseUnits.NewtonSecond:
            return (value)
        
        if from_unit == ImpulseUnits.PoundFootPerSecond:
            return (value * 7.230657989877)
        
        if from_unit == ImpulseUnits.PoundForceSecond:
            return (value * 0.2248089430997)
        
        if from_unit == ImpulseUnits.SlugFootPerSecond:
            return (value * 0.224735720691)
        
        if from_unit == ImpulseUnits.NanonewtonSecond:
            return ((value) / 1e-09)
        
        if from_unit == ImpulseUnits.MicronewtonSecond:
            return ((value) / 1e-06)
        
        if from_unit == ImpulseUnits.MillinewtonSecond:
            return ((value) / 0.001)
        
        if from_unit == ImpulseUnits.CentinewtonSecond:
            return ((value) / 0.01)
        
        if from_unit == ImpulseUnits.DecinewtonSecond:
            return ((value) / 0.1)
        
        if from_unit == ImpulseUnits.DecanewtonSecond:
            return ((value) / 10.0)
        
        if from_unit == ImpulseUnits.KilonewtonSecond:
            return ((value) / 1000.0)
        
        if from_unit == ImpulseUnits.MeganewtonSecond:
            return ((value) / 1000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: ImpulseUnits) -> float:
        
        if to_unit == ImpulseUnits.KilogramMeterPerSecond:
            return (value)
        
        if to_unit == ImpulseUnits.NewtonSecond:
            return (value)
        
        if to_unit == ImpulseUnits.PoundFootPerSecond:
            return (value / 7.230657989877)
        
        if to_unit == ImpulseUnits.PoundForceSecond:
            return (value / 0.2248089430997)
        
        if to_unit == ImpulseUnits.SlugFootPerSecond:
            return (value / 0.224735720691)
        
        if to_unit == ImpulseUnits.NanonewtonSecond:
            return ((value) * 1e-09)
        
        if to_unit == ImpulseUnits.MicronewtonSecond:
            return ((value) * 1e-06)
        
        if to_unit == ImpulseUnits.MillinewtonSecond:
            return ((value) * 0.001)
        
        if to_unit == ImpulseUnits.CentinewtonSecond:
            return ((value) * 0.01)
        
        if to_unit == ImpulseUnits.DecinewtonSecond:
            return ((value) * 0.1)
        
        if to_unit == ImpulseUnits.DecanewtonSecond:
            return ((value) * 10.0)
        
        if to_unit == ImpulseUnits.KilonewtonSecond:
            return ((value) * 1000.0)
        
        if to_unit == ImpulseUnits.MeganewtonSecond:
            return ((value) * 1000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_kilogram_meters_per_second(kilogram_meters_per_second: float):
        """
        Create a new instance of Impulse from a value in kilogram_meters_per_second.

        

        :param meters: The Impulse value in kilogram_meters_per_second.
        :type kilogram_meters_per_second: float
        :return: A new instance of Impulse.
        :rtype: Impulse
        """
        return Impulse(kilogram_meters_per_second, ImpulseUnits.KilogramMeterPerSecond)

    
    @staticmethod
    def from_newton_seconds(newton_seconds: float):
        """
        Create a new instance of Impulse from a value in newton_seconds.

        

        :param meters: The Impulse value in newton_seconds.
        :type newton_seconds: float
        :return: A new instance of Impulse.
        :rtype: Impulse
        """
        return Impulse(newton_seconds, ImpulseUnits.NewtonSecond)

    
    @staticmethod
    def from_pound_feet_per_second(pound_feet_per_second: float):
        """
        Create a new instance of Impulse from a value in pound_feet_per_second.

        

        :param meters: The Impulse value in pound_feet_per_second.
        :type pound_feet_per_second: float
        :return: A new instance of Impulse.
        :rtype: Impulse
        """
        return Impulse(pound_feet_per_second, ImpulseUnits.PoundFootPerSecond)

    
    @staticmethod
    def from_pound_force_seconds(pound_force_seconds: float):
        """
        Create a new instance of Impulse from a value in pound_force_seconds.

        

        :param meters: The Impulse value in pound_force_seconds.
        :type pound_force_seconds: float
        :return: A new instance of Impulse.
        :rtype: Impulse
        """
        return Impulse(pound_force_seconds, ImpulseUnits.PoundForceSecond)

    
    @staticmethod
    def from_slug_feet_per_second(slug_feet_per_second: float):
        """
        Create a new instance of Impulse from a value in slug_feet_per_second.

        

        :param meters: The Impulse value in slug_feet_per_second.
        :type slug_feet_per_second: float
        :return: A new instance of Impulse.
        :rtype: Impulse
        """
        return Impulse(slug_feet_per_second, ImpulseUnits.SlugFootPerSecond)

    
    @staticmethod
    def from_nanonewton_seconds(nanonewton_seconds: float):
        """
        Create a new instance of Impulse from a value in nanonewton_seconds.

        

        :param meters: The Impulse value in nanonewton_seconds.
        :type nanonewton_seconds: float
        :return: A new instance of Impulse.
        :rtype: Impulse
        """
        return Impulse(nanonewton_seconds, ImpulseUnits.NanonewtonSecond)

    
    @staticmethod
    def from_micronewton_seconds(micronewton_seconds: float):
        """
        Create a new instance of Impulse from a value in micronewton_seconds.

        

        :param meters: The Impulse value in micronewton_seconds.
        :type micronewton_seconds: float
        :return: A new instance of Impulse.
        :rtype: Impulse
        """
        return Impulse(micronewton_seconds, ImpulseUnits.MicronewtonSecond)

    
    @staticmethod
    def from_millinewton_seconds(millinewton_seconds: float):
        """
        Create a new instance of Impulse from a value in millinewton_seconds.

        

        :param meters: The Impulse value in millinewton_seconds.
        :type millinewton_seconds: float
        :return: A new instance of Impulse.
        :rtype: Impulse
        """
        return Impulse(millinewton_seconds, ImpulseUnits.MillinewtonSecond)

    
    @staticmethod
    def from_centinewton_seconds(centinewton_seconds: float):
        """
        Create a new instance of Impulse from a value in centinewton_seconds.

        

        :param meters: The Impulse value in centinewton_seconds.
        :type centinewton_seconds: float
        :return: A new instance of Impulse.
        :rtype: Impulse
        """
        return Impulse(centinewton_seconds, ImpulseUnits.CentinewtonSecond)

    
    @staticmethod
    def from_decinewton_seconds(decinewton_seconds: float):
        """
        Create a new instance of Impulse from a value in decinewton_seconds.

        

        :param meters: The Impulse value in decinewton_seconds.
        :type decinewton_seconds: float
        :return: A new instance of Impulse.
        :rtype: Impulse
        """
        return Impulse(decinewton_seconds, ImpulseUnits.DecinewtonSecond)

    
    @staticmethod
    def from_decanewton_seconds(decanewton_seconds: float):
        """
        Create a new instance of Impulse from a value in decanewton_seconds.

        

        :param meters: The Impulse value in decanewton_seconds.
        :type decanewton_seconds: float
        :return: A new instance of Impulse.
        :rtype: Impulse
        """
        return Impulse(decanewton_seconds, ImpulseUnits.DecanewtonSecond)

    
    @staticmethod
    def from_kilonewton_seconds(kilonewton_seconds: float):
        """
        Create a new instance of Impulse from a value in kilonewton_seconds.

        

        :param meters: The Impulse value in kilonewton_seconds.
        :type kilonewton_seconds: float
        :return: A new instance of Impulse.
        :rtype: Impulse
        """
        return Impulse(kilonewton_seconds, ImpulseUnits.KilonewtonSecond)

    
    @staticmethod
    def from_meganewton_seconds(meganewton_seconds: float):
        """
        Create a new instance of Impulse from a value in meganewton_seconds.

        

        :param meters: The Impulse value in meganewton_seconds.
        :type meganewton_seconds: float
        :return: A new instance of Impulse.
        :rtype: Impulse
        """
        return Impulse(meganewton_seconds, ImpulseUnits.MeganewtonSecond)

    
    @property
    def kilogram_meters_per_second(self) -> float:
        """
        
        """
        if self.__kilogram_meters_per_second != None:
            return self.__kilogram_meters_per_second
        self.__kilogram_meters_per_second = self.__convert_from_base(ImpulseUnits.KilogramMeterPerSecond)
        return self.__kilogram_meters_per_second

    
    @property
    def newton_seconds(self) -> float:
        """
        
        """
        if self.__newton_seconds != None:
            return self.__newton_seconds
        self.__newton_seconds = self.__convert_from_base(ImpulseUnits.NewtonSecond)
        return self.__newton_seconds

    
    @property
    def pound_feet_per_second(self) -> float:
        """
        
        """
        if self.__pound_feet_per_second != None:
            return self.__pound_feet_per_second
        self.__pound_feet_per_second = self.__convert_from_base(ImpulseUnits.PoundFootPerSecond)
        return self.__pound_feet_per_second

    
    @property
    def pound_force_seconds(self) -> float:
        """
        
        """
        if self.__pound_force_seconds != None:
            return self.__pound_force_seconds
        self.__pound_force_seconds = self.__convert_from_base(ImpulseUnits.PoundForceSecond)
        return self.__pound_force_seconds

    
    @property
    def slug_feet_per_second(self) -> float:
        """
        
        """
        if self.__slug_feet_per_second != None:
            return self.__slug_feet_per_second
        self.__slug_feet_per_second = self.__convert_from_base(ImpulseUnits.SlugFootPerSecond)
        return self.__slug_feet_per_second

    
    @property
    def nanonewton_seconds(self) -> float:
        """
        
        """
        if self.__nanonewton_seconds != None:
            return self.__nanonewton_seconds
        self.__nanonewton_seconds = self.__convert_from_base(ImpulseUnits.NanonewtonSecond)
        return self.__nanonewton_seconds

    
    @property
    def micronewton_seconds(self) -> float:
        """
        
        """
        if self.__micronewton_seconds != None:
            return self.__micronewton_seconds
        self.__micronewton_seconds = self.__convert_from_base(ImpulseUnits.MicronewtonSecond)
        return self.__micronewton_seconds

    
    @property
    def millinewton_seconds(self) -> float:
        """
        
        """
        if self.__millinewton_seconds != None:
            return self.__millinewton_seconds
        self.__millinewton_seconds = self.__convert_from_base(ImpulseUnits.MillinewtonSecond)
        return self.__millinewton_seconds

    
    @property
    def centinewton_seconds(self) -> float:
        """
        
        """
        if self.__centinewton_seconds != None:
            return self.__centinewton_seconds
        self.__centinewton_seconds = self.__convert_from_base(ImpulseUnits.CentinewtonSecond)
        return self.__centinewton_seconds

    
    @property
    def decinewton_seconds(self) -> float:
        """
        
        """
        if self.__decinewton_seconds != None:
            return self.__decinewton_seconds
        self.__decinewton_seconds = self.__convert_from_base(ImpulseUnits.DecinewtonSecond)
        return self.__decinewton_seconds

    
    @property
    def decanewton_seconds(self) -> float:
        """
        
        """
        if self.__decanewton_seconds != None:
            return self.__decanewton_seconds
        self.__decanewton_seconds = self.__convert_from_base(ImpulseUnits.DecanewtonSecond)
        return self.__decanewton_seconds

    
    @property
    def kilonewton_seconds(self) -> float:
        """
        
        """
        if self.__kilonewton_seconds != None:
            return self.__kilonewton_seconds
        self.__kilonewton_seconds = self.__convert_from_base(ImpulseUnits.KilonewtonSecond)
        return self.__kilonewton_seconds

    
    @property
    def meganewton_seconds(self) -> float:
        """
        
        """
        if self.__meganewton_seconds != None:
            return self.__meganewton_seconds
        self.__meganewton_seconds = self.__convert_from_base(ImpulseUnits.MeganewtonSecond)
        return self.__meganewton_seconds

    
    def to_string(self, unit: ImpulseUnits = ImpulseUnits.NewtonSecond) -> str:
        """
        Format the Impulse to string.
        Note! the default format for Impulse is NewtonSecond.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == ImpulseUnits.KilogramMeterPerSecond:
            return f"""{self.kilogram_meters_per_second} kg·m/s"""
        
        if unit == ImpulseUnits.NewtonSecond:
            return f"""{self.newton_seconds} N·s"""
        
        if unit == ImpulseUnits.PoundFootPerSecond:
            return f"""{self.pound_feet_per_second} lb·ft/s"""
        
        if unit == ImpulseUnits.PoundForceSecond:
            return f"""{self.pound_force_seconds} lbf·s"""
        
        if unit == ImpulseUnits.SlugFootPerSecond:
            return f"""{self.slug_feet_per_second} slug·ft/s"""
        
        if unit == ImpulseUnits.NanonewtonSecond:
            return f"""{self.nanonewton_seconds} nN·s"""
        
        if unit == ImpulseUnits.MicronewtonSecond:
            return f"""{self.micronewton_seconds} μN·s"""
        
        if unit == ImpulseUnits.MillinewtonSecond:
            return f"""{self.millinewton_seconds} mN·s"""
        
        if unit == ImpulseUnits.CentinewtonSecond:
            return f"""{self.centinewton_seconds} cN·s"""
        
        if unit == ImpulseUnits.DecinewtonSecond:
            return f"""{self.decinewton_seconds} dN·s"""
        
        if unit == ImpulseUnits.DecanewtonSecond:
            return f"""{self.decanewton_seconds} daN·s"""
        
        if unit == ImpulseUnits.KilonewtonSecond:
            return f"""{self.kilonewton_seconds} kN·s"""
        
        if unit == ImpulseUnits.MeganewtonSecond:
            return f"""{self.meganewton_seconds} MN·s"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: ImpulseUnits = ImpulseUnits.NewtonSecond) -> str:
        """
        Get Impulse unit abbreviation.
        Note! the default abbreviation for Impulse is NewtonSecond.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == ImpulseUnits.KilogramMeterPerSecond:
            return """kg·m/s"""
        
        if unit_abbreviation == ImpulseUnits.NewtonSecond:
            return """N·s"""
        
        if unit_abbreviation == ImpulseUnits.PoundFootPerSecond:
            return """lb·ft/s"""
        
        if unit_abbreviation == ImpulseUnits.PoundForceSecond:
            return """lbf·s"""
        
        if unit_abbreviation == ImpulseUnits.SlugFootPerSecond:
            return """slug·ft/s"""
        
        if unit_abbreviation == ImpulseUnits.NanonewtonSecond:
            return """nN·s"""
        
        if unit_abbreviation == ImpulseUnits.MicronewtonSecond:
            return """μN·s"""
        
        if unit_abbreviation == ImpulseUnits.MillinewtonSecond:
            return """mN·s"""
        
        if unit_abbreviation == ImpulseUnits.CentinewtonSecond:
            return """cN·s"""
        
        if unit_abbreviation == ImpulseUnits.DecinewtonSecond:
            return """dN·s"""
        
        if unit_abbreviation == ImpulseUnits.DecanewtonSecond:
            return """daN·s"""
        
        if unit_abbreviation == ImpulseUnits.KilonewtonSecond:
            return """kN·s"""
        
        if unit_abbreviation == ImpulseUnits.MeganewtonSecond:
            return """MN·s"""
        
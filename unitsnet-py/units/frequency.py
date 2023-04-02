from enum import Enum
import math
import string


class FrequencyUnits(Enum):
        """
            FrequencyUnits enumeration
        """
        
        Hertz = 'hertz'
        """
            
        """
        
        RadianPerSecond = 'radian_per_second'
        """
            
        """
        
        CyclePerMinute = 'cycle_per_minute'
        """
            
        """
        
        CyclePerHour = 'cycle_per_hour'
        """
            
        """
        
        BeatPerMinute = 'beat_per_minute'
        """
            
        """
        
        PerSecond = 'per_second'
        """
            
        """
        
        BUnit = 'b_unit'
        """
            
        """
        
        MicroHertz = 'micro_hertz'
        """
            
        """
        
        MilliHertz = 'milli_hertz'
        """
            
        """
        
        KiloHertz = 'kilo_hertz'
        """
            
        """
        
        MegaHertz = 'mega_hertz'
        """
            
        """
        
        GigaHertz = 'giga_hertz'
        """
            
        """
        
        TeraHertz = 'tera_hertz'
        """
            
        """
        

class Frequency:
    """
    The number of occurrences of a repeating event per unit time.

    Args:
        value (float): The value.
        from_unit (FrequencyUnits): The Frequency unit to create from, The default unit is Hertz
    """
    def __init__(self, value: float, from_unit: FrequencyUnits = FrequencyUnits.Hertz):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__hertz = None
        
        self.__radians_per_second = None
        
        self.__cycles_per_minute = None
        
        self.__cycles_per_hour = None
        
        self.__beats_per_minute = None
        
        self.__per_second = None
        
        self.__b_units = None
        
        self.__micro_hertz = None
        
        self.__milli_hertz = None
        
        self.__kilo_hertz = None
        
        self.__mega_hertz = None
        
        self.__giga_hertz = None
        
        self.__tera_hertz = None
        

    def __convert_from_base(self, from_unit: FrequencyUnits) -> float:
        value = self.__value
        
        if from_unit == FrequencyUnits.Hertz:
            return (value)
        
        if from_unit == FrequencyUnits.RadianPerSecond:
            return (value * 6.2831853072)
        
        if from_unit == FrequencyUnits.CyclePerMinute:
            return (value * 60)
        
        if from_unit == FrequencyUnits.CyclePerHour:
            return (value * 3600)
        
        if from_unit == FrequencyUnits.BeatPerMinute:
            return (value * 60)
        
        if from_unit == FrequencyUnits.PerSecond:
            return (value)
        
        if from_unit == FrequencyUnits.BUnit:
            return (value * value * 1e-3)
        
        if from_unit == FrequencyUnits.MicroHertz:
            return ((value) / 1e-06)
        
        if from_unit == FrequencyUnits.MilliHertz:
            return ((value) / 0.001)
        
        if from_unit == FrequencyUnits.KiloHertz:
            return ((value) / 1000.0)
        
        if from_unit == FrequencyUnits.MegaHertz:
            return ((value) / 1000000.0)
        
        if from_unit == FrequencyUnits.GigaHertz:
            return ((value) / 1000000000.0)
        
        if from_unit == FrequencyUnits.TeraHertz:
            return ((value) / 1000000000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: FrequencyUnits) -> float:
        
        if to_unit == FrequencyUnits.Hertz:
            return (value)
        
        if to_unit == FrequencyUnits.RadianPerSecond:
            return (value / 6.2831853072)
        
        if to_unit == FrequencyUnits.CyclePerMinute:
            return (value / 60)
        
        if to_unit == FrequencyUnits.CyclePerHour:
            return (value / 3600)
        
        if to_unit == FrequencyUnits.BeatPerMinute:
            return (value / 60)
        
        if to_unit == FrequencyUnits.PerSecond:
            return (value)
        
        if to_unit == FrequencyUnits.BUnit:
            return (math.sqrt(value * 1e3))
        
        if to_unit == FrequencyUnits.MicroHertz:
            return ((value) * 1e-06)
        
        if to_unit == FrequencyUnits.MilliHertz:
            return ((value) * 0.001)
        
        if to_unit == FrequencyUnits.KiloHertz:
            return ((value) * 1000.0)
        
        if to_unit == FrequencyUnits.MegaHertz:
            return ((value) * 1000000.0)
        
        if to_unit == FrequencyUnits.GigaHertz:
            return ((value) * 1000000000.0)
        
        if to_unit == FrequencyUnits.TeraHertz:
            return ((value) * 1000000000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
    @staticmethod
    def from_hertz(hertz: float):
        """
        Create a new instance of Frequency from a value in hertz.

        

        :param meters: The Frequency value in hertz.
        :type hertz: float
        :return: A new instance of Frequency.
        :rtype: Frequency
        """
        return Frequency(hertz, FrequencyUnits.Hertz)

    
    @staticmethod
    def from_radians_per_second(radians_per_second: float):
        """
        Create a new instance of Frequency from a value in radians_per_second.

        

        :param meters: The Frequency value in radians_per_second.
        :type radians_per_second: float
        :return: A new instance of Frequency.
        :rtype: Frequency
        """
        return Frequency(radians_per_second, FrequencyUnits.RadianPerSecond)

    
    @staticmethod
    def from_cycles_per_minute(cycles_per_minute: float):
        """
        Create a new instance of Frequency from a value in cycles_per_minute.

        

        :param meters: The Frequency value in cycles_per_minute.
        :type cycles_per_minute: float
        :return: A new instance of Frequency.
        :rtype: Frequency
        """
        return Frequency(cycles_per_minute, FrequencyUnits.CyclePerMinute)

    
    @staticmethod
    def from_cycles_per_hour(cycles_per_hour: float):
        """
        Create a new instance of Frequency from a value in cycles_per_hour.

        

        :param meters: The Frequency value in cycles_per_hour.
        :type cycles_per_hour: float
        :return: A new instance of Frequency.
        :rtype: Frequency
        """
        return Frequency(cycles_per_hour, FrequencyUnits.CyclePerHour)

    
    @staticmethod
    def from_beats_per_minute(beats_per_minute: float):
        """
        Create a new instance of Frequency from a value in beats_per_minute.

        

        :param meters: The Frequency value in beats_per_minute.
        :type beats_per_minute: float
        :return: A new instance of Frequency.
        :rtype: Frequency
        """
        return Frequency(beats_per_minute, FrequencyUnits.BeatPerMinute)

    
    @staticmethod
    def from_per_second(per_second: float):
        """
        Create a new instance of Frequency from a value in per_second.

        

        :param meters: The Frequency value in per_second.
        :type per_second: float
        :return: A new instance of Frequency.
        :rtype: Frequency
        """
        return Frequency(per_second, FrequencyUnits.PerSecond)

    
    @staticmethod
    def from_b_units(b_units: float):
        """
        Create a new instance of Frequency from a value in b_units.

        

        :param meters: The Frequency value in b_units.
        :type b_units: float
        :return: A new instance of Frequency.
        :rtype: Frequency
        """
        return Frequency(b_units, FrequencyUnits.BUnit)

    
    @staticmethod
    def from_micro_hertz(micro_hertz: float):
        """
        Create a new instance of Frequency from a value in micro_hertz.

        

        :param meters: The Frequency value in micro_hertz.
        :type micro_hertz: float
        :return: A new instance of Frequency.
        :rtype: Frequency
        """
        return Frequency(micro_hertz, FrequencyUnits.MicroHertz)

    
    @staticmethod
    def from_milli_hertz(milli_hertz: float):
        """
        Create a new instance of Frequency from a value in milli_hertz.

        

        :param meters: The Frequency value in milli_hertz.
        :type milli_hertz: float
        :return: A new instance of Frequency.
        :rtype: Frequency
        """
        return Frequency(milli_hertz, FrequencyUnits.MilliHertz)

    
    @staticmethod
    def from_kilo_hertz(kilo_hertz: float):
        """
        Create a new instance of Frequency from a value in kilo_hertz.

        

        :param meters: The Frequency value in kilo_hertz.
        :type kilo_hertz: float
        :return: A new instance of Frequency.
        :rtype: Frequency
        """
        return Frequency(kilo_hertz, FrequencyUnits.KiloHertz)

    
    @staticmethod
    def from_mega_hertz(mega_hertz: float):
        """
        Create a new instance of Frequency from a value in mega_hertz.

        

        :param meters: The Frequency value in mega_hertz.
        :type mega_hertz: float
        :return: A new instance of Frequency.
        :rtype: Frequency
        """
        return Frequency(mega_hertz, FrequencyUnits.MegaHertz)

    
    @staticmethod
    def from_giga_hertz(giga_hertz: float):
        """
        Create a new instance of Frequency from a value in giga_hertz.

        

        :param meters: The Frequency value in giga_hertz.
        :type giga_hertz: float
        :return: A new instance of Frequency.
        :rtype: Frequency
        """
        return Frequency(giga_hertz, FrequencyUnits.GigaHertz)

    
    @staticmethod
    def from_tera_hertz(tera_hertz: float):
        """
        Create a new instance of Frequency from a value in tera_hertz.

        

        :param meters: The Frequency value in tera_hertz.
        :type tera_hertz: float
        :return: A new instance of Frequency.
        :rtype: Frequency
        """
        return Frequency(tera_hertz, FrequencyUnits.TeraHertz)

    
    @property
    def hertz(self) -> float:
        """
        
        """
        if self.__hertz != None:
            return self.__hertz
        self.__hertz = self.__convert_from_base(FrequencyUnits.Hertz)
        return self.__hertz

    
    @property
    def radians_per_second(self) -> float:
        """
        
        """
        if self.__radians_per_second != None:
            return self.__radians_per_second
        self.__radians_per_second = self.__convert_from_base(FrequencyUnits.RadianPerSecond)
        return self.__radians_per_second

    
    @property
    def cycles_per_minute(self) -> float:
        """
        
        """
        if self.__cycles_per_minute != None:
            return self.__cycles_per_minute
        self.__cycles_per_minute = self.__convert_from_base(FrequencyUnits.CyclePerMinute)
        return self.__cycles_per_minute

    
    @property
    def cycles_per_hour(self) -> float:
        """
        
        """
        if self.__cycles_per_hour != None:
            return self.__cycles_per_hour
        self.__cycles_per_hour = self.__convert_from_base(FrequencyUnits.CyclePerHour)
        return self.__cycles_per_hour

    
    @property
    def beats_per_minute(self) -> float:
        """
        
        """
        if self.__beats_per_minute != None:
            return self.__beats_per_minute
        self.__beats_per_minute = self.__convert_from_base(FrequencyUnits.BeatPerMinute)
        return self.__beats_per_minute

    
    @property
    def per_second(self) -> float:
        """
        
        """
        if self.__per_second != None:
            return self.__per_second
        self.__per_second = self.__convert_from_base(FrequencyUnits.PerSecond)
        return self.__per_second

    
    @property
    def b_units(self) -> float:
        """
        
        """
        if self.__b_units != None:
            return self.__b_units
        self.__b_units = self.__convert_from_base(FrequencyUnits.BUnit)
        return self.__b_units

    
    @property
    def micro_hertz(self) -> float:
        """
        
        """
        if self.__micro_hertz != None:
            return self.__micro_hertz
        self.__micro_hertz = self.__convert_from_base(FrequencyUnits.MicroHertz)
        return self.__micro_hertz

    
    @property
    def milli_hertz(self) -> float:
        """
        
        """
        if self.__milli_hertz != None:
            return self.__milli_hertz
        self.__milli_hertz = self.__convert_from_base(FrequencyUnits.MilliHertz)
        return self.__milli_hertz

    
    @property
    def kilo_hertz(self) -> float:
        """
        
        """
        if self.__kilo_hertz != None:
            return self.__kilo_hertz
        self.__kilo_hertz = self.__convert_from_base(FrequencyUnits.KiloHertz)
        return self.__kilo_hertz

    
    @property
    def mega_hertz(self) -> float:
        """
        
        """
        if self.__mega_hertz != None:
            return self.__mega_hertz
        self.__mega_hertz = self.__convert_from_base(FrequencyUnits.MegaHertz)
        return self.__mega_hertz

    
    @property
    def giga_hertz(self) -> float:
        """
        
        """
        if self.__giga_hertz != None:
            return self.__giga_hertz
        self.__giga_hertz = self.__convert_from_base(FrequencyUnits.GigaHertz)
        return self.__giga_hertz

    
    @property
    def tera_hertz(self) -> float:
        """
        
        """
        if self.__tera_hertz != None:
            return self.__tera_hertz
        self.__tera_hertz = self.__convert_from_base(FrequencyUnits.TeraHertz)
        return self.__tera_hertz

    
    def to_string(self, unit: FrequencyUnits = FrequencyUnits.Hertz) -> string:
        """
        Format the Frequency to string.
        Note! the default format for Frequency is Hertz.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == FrequencyUnits.Hertz:
            return f"""{self.hertz} Hz"""
        
        if unit == FrequencyUnits.RadianPerSecond:
            return f"""{self.radians_per_second} rad/s"""
        
        if unit == FrequencyUnits.CyclePerMinute:
            return f"""{self.cycles_per_minute} cpm"""
        
        if unit == FrequencyUnits.CyclePerHour:
            return f"""{self.cycles_per_hour} cph"""
        
        if unit == FrequencyUnits.BeatPerMinute:
            return f"""{self.beats_per_minute} bpm"""
        
        if unit == FrequencyUnits.PerSecond:
            return f"""{self.per_second} s⁻¹"""
        
        if unit == FrequencyUnits.BUnit:
            return f"""{self.b_units} B Units"""
        
        if unit == FrequencyUnits.MicroHertz:
            return f"""{self.micro_hertz} """
        
        if unit == FrequencyUnits.MilliHertz:
            return f"""{self.milli_hertz} """
        
        if unit == FrequencyUnits.KiloHertz:
            return f"""{self.kilo_hertz} """
        
        if unit == FrequencyUnits.MegaHertz:
            return f"""{self.mega_hertz} """
        
        if unit == FrequencyUnits.GigaHertz:
            return f"""{self.giga_hertz} """
        
        if unit == FrequencyUnits.TeraHertz:
            return f"""{self.tera_hertz} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: FrequencyUnits = FrequencyUnits.Hertz) -> string:
        """
        Get Frequency unit abbreviation.
        Note! the default abbreviation for Frequency is Hertz.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == FrequencyUnits.Hertz:
            return """Hz"""
        
        if unit_abbreviation == FrequencyUnits.RadianPerSecond:
            return """rad/s"""
        
        if unit_abbreviation == FrequencyUnits.CyclePerMinute:
            return """cpm"""
        
        if unit_abbreviation == FrequencyUnits.CyclePerHour:
            return """cph"""
        
        if unit_abbreviation == FrequencyUnits.BeatPerMinute:
            return """bpm"""
        
        if unit_abbreviation == FrequencyUnits.PerSecond:
            return """s⁻¹"""
        
        if unit_abbreviation == FrequencyUnits.BUnit:
            return """B Units"""
        
        if unit_abbreviation == FrequencyUnits.MicroHertz:
            return """"""
        
        if unit_abbreviation == FrequencyUnits.MilliHertz:
            return """"""
        
        if unit_abbreviation == FrequencyUnits.KiloHertz:
            return """"""
        
        if unit_abbreviation == FrequencyUnits.MegaHertz:
            return """"""
        
        if unit_abbreviation == FrequencyUnits.GigaHertz:
            return """"""
        
        if unit_abbreviation == FrequencyUnits.TeraHertz:
            return """"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, Frequency):
            raise TypeError("unsupported operand type(s) for +: 'Frequency' and '{}'".format(type(other).__name__))
        return Frequency(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, Frequency):
            raise TypeError("unsupported operand type(s) for *: 'Frequency' and '{}'".format(type(other).__name__))
        return Frequency(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, Frequency):
            raise TypeError("unsupported operand type(s) for -: 'Frequency' and '{}'".format(type(other).__name__))
        return Frequency(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, Frequency):
            raise TypeError("unsupported operand type(s) for /: 'Frequency' and '{}'".format(type(other).__name__))
        return Frequency(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, Frequency):
            raise TypeError("unsupported operand type(s) for %: 'Frequency' and '{}'".format(type(other).__name__))
        return Frequency(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, Frequency):
            raise TypeError("unsupported operand type(s) for **: 'Frequency' and '{}'".format(type(other).__name__))
        return Frequency(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, Frequency):
            raise TypeError("unsupported operand type(s) for ==: 'Frequency' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, Frequency):
            raise TypeError("unsupported operand type(s) for <: 'Frequency' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, Frequency):
            raise TypeError("unsupported operand type(s) for >: 'Frequency' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, Frequency):
            raise TypeError("unsupported operand type(s) for <=: 'Frequency' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, Frequency):
            raise TypeError("unsupported operand type(s) for >=: 'Frequency' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value
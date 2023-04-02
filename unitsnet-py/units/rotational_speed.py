from enum import Enum
import math
import string


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
        
        NanoRadianPerSecond = 'nano_radian_per_second'
        """
            
        """
        
        MicroRadianPerSecond = 'micro_radian_per_second'
        """
            
        """
        
        MilliRadianPerSecond = 'milli_radian_per_second'
        """
            
        """
        
        CentiRadianPerSecond = 'centi_radian_per_second'
        """
            
        """
        
        DeciRadianPerSecond = 'deci_radian_per_second'
        """
            
        """
        
        NanoDegreePerSecond = 'nano_degree_per_second'
        """
            
        """
        
        MicroDegreePerSecond = 'micro_degree_per_second'
        """
            
        """
        
        MilliDegreePerSecond = 'milli_degree_per_second'
        """
            
        """
        

class RotationalSpeed:
    """
    Rotational speed (sometimes called speed of revolution) is the number of complete rotations, revolutions, cycles, or turns per time unit. Rotational speed is a cyclic frequency, measured in radians per second or in hertz in the SI System by scientists, or in revolutions per minute (rpm or min-1) or revolutions per second in everyday life. The symbol for rotational speed is ω (the Greek lowercase letter "omega").

    Args:
        value (float): The value.
        from_unit (RotationalSpeedUnits): The RotationalSpeed unit to create from, The default unit is RadianPerSecond
    """
    def __init__(self, value: float, from_unit: RotationalSpeedUnits = RotationalSpeedUnits.RadianPerSecond):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__radians_per_second = None
        
        self.__degrees_per_second = None
        
        self.__degrees_per_minute = None
        
        self.__revolutions_per_second = None
        
        self.__revolutions_per_minute = None
        
        self.__nano_radians_per_second = None
        
        self.__micro_radians_per_second = None
        
        self.__milli_radians_per_second = None
        
        self.__centi_radians_per_second = None
        
        self.__deci_radians_per_second = None
        
        self.__nano_degrees_per_second = None
        
        self.__micro_degrees_per_second = None
        
        self.__milli_degrees_per_second = None
        

    def __convert_from_base(self, from_unit: RotationalSpeedUnits) -> float:
        value = self.__value
        
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
        
        if from_unit == RotationalSpeedUnits.NanoRadianPerSecond:
            return ((value) / 1e-09)
        
        if from_unit == RotationalSpeedUnits.MicroRadianPerSecond:
            return ((value) / 1e-06)
        
        if from_unit == RotationalSpeedUnits.MilliRadianPerSecond:
            return ((value) / 0.001)
        
        if from_unit == RotationalSpeedUnits.CentiRadianPerSecond:
            return ((value) / 0.01)
        
        if from_unit == RotationalSpeedUnits.DeciRadianPerSecond:
            return ((value) / 0.1)
        
        if from_unit == RotationalSpeedUnits.NanoDegreePerSecond:
            return (((180 / math.pi) * value) / 1e-09)
        
        if from_unit == RotationalSpeedUnits.MicroDegreePerSecond:
            return (((180 / math.pi) * value) / 1e-06)
        
        if from_unit == RotationalSpeedUnits.MilliDegreePerSecond:
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
        
        if to_unit == RotationalSpeedUnits.NanoRadianPerSecond:
            return ((value) * 1e-09)
        
        if to_unit == RotationalSpeedUnits.MicroRadianPerSecond:
            return ((value) * 1e-06)
        
        if to_unit == RotationalSpeedUnits.MilliRadianPerSecond:
            return ((value) * 0.001)
        
        if to_unit == RotationalSpeedUnits.CentiRadianPerSecond:
            return ((value) * 0.01)
        
        if to_unit == RotationalSpeedUnits.DeciRadianPerSecond:
            return ((value) * 0.1)
        
        if to_unit == RotationalSpeedUnits.NanoDegreePerSecond:
            return (((math.pi / 180) * value) * 1e-09)
        
        if to_unit == RotationalSpeedUnits.MicroDegreePerSecond:
            return (((math.pi / 180) * value) * 1e-06)
        
        if to_unit == RotationalSpeedUnits.MilliDegreePerSecond:
            return (((math.pi / 180) * value) * 0.001)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
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
    def from_nano_radians_per_second(nano_radians_per_second: float):
        """
        Create a new instance of RotationalSpeed from a value in nano_radians_per_second.

        

        :param meters: The RotationalSpeed value in nano_radians_per_second.
        :type nano_radians_per_second: float
        :return: A new instance of RotationalSpeed.
        :rtype: RotationalSpeed
        """
        return RotationalSpeed(nano_radians_per_second, RotationalSpeedUnits.NanoRadianPerSecond)

    
    @staticmethod
    def from_micro_radians_per_second(micro_radians_per_second: float):
        """
        Create a new instance of RotationalSpeed from a value in micro_radians_per_second.

        

        :param meters: The RotationalSpeed value in micro_radians_per_second.
        :type micro_radians_per_second: float
        :return: A new instance of RotationalSpeed.
        :rtype: RotationalSpeed
        """
        return RotationalSpeed(micro_radians_per_second, RotationalSpeedUnits.MicroRadianPerSecond)

    
    @staticmethod
    def from_milli_radians_per_second(milli_radians_per_second: float):
        """
        Create a new instance of RotationalSpeed from a value in milli_radians_per_second.

        

        :param meters: The RotationalSpeed value in milli_radians_per_second.
        :type milli_radians_per_second: float
        :return: A new instance of RotationalSpeed.
        :rtype: RotationalSpeed
        """
        return RotationalSpeed(milli_radians_per_second, RotationalSpeedUnits.MilliRadianPerSecond)

    
    @staticmethod
    def from_centi_radians_per_second(centi_radians_per_second: float):
        """
        Create a new instance of RotationalSpeed from a value in centi_radians_per_second.

        

        :param meters: The RotationalSpeed value in centi_radians_per_second.
        :type centi_radians_per_second: float
        :return: A new instance of RotationalSpeed.
        :rtype: RotationalSpeed
        """
        return RotationalSpeed(centi_radians_per_second, RotationalSpeedUnits.CentiRadianPerSecond)

    
    @staticmethod
    def from_deci_radians_per_second(deci_radians_per_second: float):
        """
        Create a new instance of RotationalSpeed from a value in deci_radians_per_second.

        

        :param meters: The RotationalSpeed value in deci_radians_per_second.
        :type deci_radians_per_second: float
        :return: A new instance of RotationalSpeed.
        :rtype: RotationalSpeed
        """
        return RotationalSpeed(deci_radians_per_second, RotationalSpeedUnits.DeciRadianPerSecond)

    
    @staticmethod
    def from_nano_degrees_per_second(nano_degrees_per_second: float):
        """
        Create a new instance of RotationalSpeed from a value in nano_degrees_per_second.

        

        :param meters: The RotationalSpeed value in nano_degrees_per_second.
        :type nano_degrees_per_second: float
        :return: A new instance of RotationalSpeed.
        :rtype: RotationalSpeed
        """
        return RotationalSpeed(nano_degrees_per_second, RotationalSpeedUnits.NanoDegreePerSecond)

    
    @staticmethod
    def from_micro_degrees_per_second(micro_degrees_per_second: float):
        """
        Create a new instance of RotationalSpeed from a value in micro_degrees_per_second.

        

        :param meters: The RotationalSpeed value in micro_degrees_per_second.
        :type micro_degrees_per_second: float
        :return: A new instance of RotationalSpeed.
        :rtype: RotationalSpeed
        """
        return RotationalSpeed(micro_degrees_per_second, RotationalSpeedUnits.MicroDegreePerSecond)

    
    @staticmethod
    def from_milli_degrees_per_second(milli_degrees_per_second: float):
        """
        Create a new instance of RotationalSpeed from a value in milli_degrees_per_second.

        

        :param meters: The RotationalSpeed value in milli_degrees_per_second.
        :type milli_degrees_per_second: float
        :return: A new instance of RotationalSpeed.
        :rtype: RotationalSpeed
        """
        return RotationalSpeed(milli_degrees_per_second, RotationalSpeedUnits.MilliDegreePerSecond)

    
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
    def nano_radians_per_second(self) -> float:
        """
        
        """
        if self.__nano_radians_per_second != None:
            return self.__nano_radians_per_second
        self.__nano_radians_per_second = self.__convert_from_base(RotationalSpeedUnits.NanoRadianPerSecond)
        return self.__nano_radians_per_second

    
    @property
    def micro_radians_per_second(self) -> float:
        """
        
        """
        if self.__micro_radians_per_second != None:
            return self.__micro_radians_per_second
        self.__micro_radians_per_second = self.__convert_from_base(RotationalSpeedUnits.MicroRadianPerSecond)
        return self.__micro_radians_per_second

    
    @property
    def milli_radians_per_second(self) -> float:
        """
        
        """
        if self.__milli_radians_per_second != None:
            return self.__milli_radians_per_second
        self.__milli_radians_per_second = self.__convert_from_base(RotationalSpeedUnits.MilliRadianPerSecond)
        return self.__milli_radians_per_second

    
    @property
    def centi_radians_per_second(self) -> float:
        """
        
        """
        if self.__centi_radians_per_second != None:
            return self.__centi_radians_per_second
        self.__centi_radians_per_second = self.__convert_from_base(RotationalSpeedUnits.CentiRadianPerSecond)
        return self.__centi_radians_per_second

    
    @property
    def deci_radians_per_second(self) -> float:
        """
        
        """
        if self.__deci_radians_per_second != None:
            return self.__deci_radians_per_second
        self.__deci_radians_per_second = self.__convert_from_base(RotationalSpeedUnits.DeciRadianPerSecond)
        return self.__deci_radians_per_second

    
    @property
    def nano_degrees_per_second(self) -> float:
        """
        
        """
        if self.__nano_degrees_per_second != None:
            return self.__nano_degrees_per_second
        self.__nano_degrees_per_second = self.__convert_from_base(RotationalSpeedUnits.NanoDegreePerSecond)
        return self.__nano_degrees_per_second

    
    @property
    def micro_degrees_per_second(self) -> float:
        """
        
        """
        if self.__micro_degrees_per_second != None:
            return self.__micro_degrees_per_second
        self.__micro_degrees_per_second = self.__convert_from_base(RotationalSpeedUnits.MicroDegreePerSecond)
        return self.__micro_degrees_per_second

    
    @property
    def milli_degrees_per_second(self) -> float:
        """
        
        """
        if self.__milli_degrees_per_second != None:
            return self.__milli_degrees_per_second
        self.__milli_degrees_per_second = self.__convert_from_base(RotationalSpeedUnits.MilliDegreePerSecond)
        return self.__milli_degrees_per_second

    
    def to_string(self, unit: RotationalSpeedUnits = RotationalSpeedUnits.RadianPerSecond) -> string:
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
        
        if unit == RotationalSpeedUnits.NanoRadianPerSecond:
            return f"""{self.nano_radians_per_second} """
        
        if unit == RotationalSpeedUnits.MicroRadianPerSecond:
            return f"""{self.micro_radians_per_second} """
        
        if unit == RotationalSpeedUnits.MilliRadianPerSecond:
            return f"""{self.milli_radians_per_second} """
        
        if unit == RotationalSpeedUnits.CentiRadianPerSecond:
            return f"""{self.centi_radians_per_second} """
        
        if unit == RotationalSpeedUnits.DeciRadianPerSecond:
            return f"""{self.deci_radians_per_second} """
        
        if unit == RotationalSpeedUnits.NanoDegreePerSecond:
            return f"""{self.nano_degrees_per_second} """
        
        if unit == RotationalSpeedUnits.MicroDegreePerSecond:
            return f"""{self.micro_degrees_per_second} """
        
        if unit == RotationalSpeedUnits.MilliDegreePerSecond:
            return f"""{self.milli_degrees_per_second} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: RotationalSpeedUnits = RotationalSpeedUnits.RadianPerSecond) -> string:
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
        
        if unit_abbreviation == RotationalSpeedUnits.NanoRadianPerSecond:
            return """"""
        
        if unit_abbreviation == RotationalSpeedUnits.MicroRadianPerSecond:
            return """"""
        
        if unit_abbreviation == RotationalSpeedUnits.MilliRadianPerSecond:
            return """"""
        
        if unit_abbreviation == RotationalSpeedUnits.CentiRadianPerSecond:
            return """"""
        
        if unit_abbreviation == RotationalSpeedUnits.DeciRadianPerSecond:
            return """"""
        
        if unit_abbreviation == RotationalSpeedUnits.NanoDegreePerSecond:
            return """"""
        
        if unit_abbreviation == RotationalSpeedUnits.MicroDegreePerSecond:
            return """"""
        
        if unit_abbreviation == RotationalSpeedUnits.MilliDegreePerSecond:
            return """"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, RotationalSpeed):
            raise TypeError("unsupported operand type(s) for +: 'RotationalSpeed' and '{}'".format(type(other).__name__))
        return RotationalSpeed(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, RotationalSpeed):
            raise TypeError("unsupported operand type(s) for *: 'RotationalSpeed' and '{}'".format(type(other).__name__))
        return RotationalSpeed(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, RotationalSpeed):
            raise TypeError("unsupported operand type(s) for -: 'RotationalSpeed' and '{}'".format(type(other).__name__))
        return RotationalSpeed(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, RotationalSpeed):
            raise TypeError("unsupported operand type(s) for /: 'RotationalSpeed' and '{}'".format(type(other).__name__))
        return RotationalSpeed(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, RotationalSpeed):
            raise TypeError("unsupported operand type(s) for %: 'RotationalSpeed' and '{}'".format(type(other).__name__))
        return RotationalSpeed(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, RotationalSpeed):
            raise TypeError("unsupported operand type(s) for **: 'RotationalSpeed' and '{}'".format(type(other).__name__))
        return RotationalSpeed(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, RotationalSpeed):
            raise TypeError("unsupported operand type(s) for ==: 'RotationalSpeed' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, RotationalSpeed):
            raise TypeError("unsupported operand type(s) for <: 'RotationalSpeed' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, RotationalSpeed):
            raise TypeError("unsupported operand type(s) for >: 'RotationalSpeed' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, RotationalSpeed):
            raise TypeError("unsupported operand type(s) for <=: 'RotationalSpeed' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, RotationalSpeed):
            raise TypeError("unsupported operand type(s) for >=: 'RotationalSpeed' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value
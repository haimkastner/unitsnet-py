from enum import Enum
import math
import string


class TemperatureChangeRateUnits(Enum):
        """
            TemperatureChangeRateUnits enumeration
        """
        
        DegreeCelsiusPerSecond = 'degree_celsius_per_second'
        """
            
        """
        
        DegreeCelsiusPerMinute = 'degree_celsius_per_minute'
        """
            
        """
        
        NanoDegreeCelsiusPerSecond = 'nano_degree_celsius_per_second'
        """
            
        """
        
        MicroDegreeCelsiusPerSecond = 'micro_degree_celsius_per_second'
        """
            
        """
        
        MilliDegreeCelsiusPerSecond = 'milli_degree_celsius_per_second'
        """
            
        """
        
        CentiDegreeCelsiusPerSecond = 'centi_degree_celsius_per_second'
        """
            
        """
        
        DeciDegreeCelsiusPerSecond = 'deci_degree_celsius_per_second'
        """
            
        """
        
        DecaDegreeCelsiusPerSecond = 'deca_degree_celsius_per_second'
        """
            
        """
        
        HectoDegreeCelsiusPerSecond = 'hecto_degree_celsius_per_second'
        """
            
        """
        
        KiloDegreeCelsiusPerSecond = 'kilo_degree_celsius_per_second'
        """
            
        """
        

class TemperatureChangeRate:
    """
    Temperature change rate is the ratio of the temperature change to the time during which the change occurred (value of temperature changes per unit time).

    Args:
        value (float): The value.
        from_unit (TemperatureChangeRateUnits): The TemperatureChangeRate unit to create from, The default unit is DegreeCelsiusPerSecond
    """
    def __init__(self, value: float, from_unit: TemperatureChangeRateUnits = TemperatureChangeRateUnits.DegreeCelsiusPerSecond):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__degrees_celsius_per_second = None
        
        self.__degrees_celsius_per_minute = None
        
        self.__nano_degrees_celsius_per_second = None
        
        self.__micro_degrees_celsius_per_second = None
        
        self.__milli_degrees_celsius_per_second = None
        
        self.__centi_degrees_celsius_per_second = None
        
        self.__deci_degrees_celsius_per_second = None
        
        self.__deca_degrees_celsius_per_second = None
        
        self.__hecto_degrees_celsius_per_second = None
        
        self.__kilo_degrees_celsius_per_second = None
        

    def __convert_from_base(self, from_unit: TemperatureChangeRateUnits) -> float:
        value = self.__value
        
        if from_unit == TemperatureChangeRateUnits.DegreeCelsiusPerSecond:
            return (value)
        
        if from_unit == TemperatureChangeRateUnits.DegreeCelsiusPerMinute:
            return (value * 60)
        
        if from_unit == TemperatureChangeRateUnits.NanoDegreeCelsiusPerSecond:
            return ((value) / 1e-09)
        
        if from_unit == TemperatureChangeRateUnits.MicroDegreeCelsiusPerSecond:
            return ((value) / 1e-06)
        
        if from_unit == TemperatureChangeRateUnits.MilliDegreeCelsiusPerSecond:
            return ((value) / 0.001)
        
        if from_unit == TemperatureChangeRateUnits.CentiDegreeCelsiusPerSecond:
            return ((value) / 0.01)
        
        if from_unit == TemperatureChangeRateUnits.DeciDegreeCelsiusPerSecond:
            return ((value) / 0.1)
        
        if from_unit == TemperatureChangeRateUnits.DecaDegreeCelsiusPerSecond:
            return ((value) / 10.0)
        
        if from_unit == TemperatureChangeRateUnits.HectoDegreeCelsiusPerSecond:
            return ((value) / 100.0)
        
        if from_unit == TemperatureChangeRateUnits.KiloDegreeCelsiusPerSecond:
            return ((value) / 1000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: TemperatureChangeRateUnits) -> float:
        
        if to_unit == TemperatureChangeRateUnits.DegreeCelsiusPerSecond:
            return (value)
        
        if to_unit == TemperatureChangeRateUnits.DegreeCelsiusPerMinute:
            return (value / 60)
        
        if to_unit == TemperatureChangeRateUnits.NanoDegreeCelsiusPerSecond:
            return ((value) * 1e-09)
        
        if to_unit == TemperatureChangeRateUnits.MicroDegreeCelsiusPerSecond:
            return ((value) * 1e-06)
        
        if to_unit == TemperatureChangeRateUnits.MilliDegreeCelsiusPerSecond:
            return ((value) * 0.001)
        
        if to_unit == TemperatureChangeRateUnits.CentiDegreeCelsiusPerSecond:
            return ((value) * 0.01)
        
        if to_unit == TemperatureChangeRateUnits.DeciDegreeCelsiusPerSecond:
            return ((value) * 0.1)
        
        if to_unit == TemperatureChangeRateUnits.DecaDegreeCelsiusPerSecond:
            return ((value) * 10.0)
        
        if to_unit == TemperatureChangeRateUnits.HectoDegreeCelsiusPerSecond:
            return ((value) * 100.0)
        
        if to_unit == TemperatureChangeRateUnits.KiloDegreeCelsiusPerSecond:
            return ((value) * 1000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
    @staticmethod
    def from_degrees_celsius_per_second(degrees_celsius_per_second: float):
        """
        Create a new instance of TemperatureChangeRate from a value in degrees_celsius_per_second.

        

        :param meters: The TemperatureChangeRate value in degrees_celsius_per_second.
        :type degrees_celsius_per_second: float
        :return: A new instance of TemperatureChangeRate.
        :rtype: TemperatureChangeRate
        """
        return TemperatureChangeRate(degrees_celsius_per_second, TemperatureChangeRateUnits.DegreeCelsiusPerSecond)

    
    @staticmethod
    def from_degrees_celsius_per_minute(degrees_celsius_per_minute: float):
        """
        Create a new instance of TemperatureChangeRate from a value in degrees_celsius_per_minute.

        

        :param meters: The TemperatureChangeRate value in degrees_celsius_per_minute.
        :type degrees_celsius_per_minute: float
        :return: A new instance of TemperatureChangeRate.
        :rtype: TemperatureChangeRate
        """
        return TemperatureChangeRate(degrees_celsius_per_minute, TemperatureChangeRateUnits.DegreeCelsiusPerMinute)

    
    @staticmethod
    def from_nano_degrees_celsius_per_second(nano_degrees_celsius_per_second: float):
        """
        Create a new instance of TemperatureChangeRate from a value in nano_degrees_celsius_per_second.

        

        :param meters: The TemperatureChangeRate value in nano_degrees_celsius_per_second.
        :type nano_degrees_celsius_per_second: float
        :return: A new instance of TemperatureChangeRate.
        :rtype: TemperatureChangeRate
        """
        return TemperatureChangeRate(nano_degrees_celsius_per_second, TemperatureChangeRateUnits.NanoDegreeCelsiusPerSecond)

    
    @staticmethod
    def from_micro_degrees_celsius_per_second(micro_degrees_celsius_per_second: float):
        """
        Create a new instance of TemperatureChangeRate from a value in micro_degrees_celsius_per_second.

        

        :param meters: The TemperatureChangeRate value in micro_degrees_celsius_per_second.
        :type micro_degrees_celsius_per_second: float
        :return: A new instance of TemperatureChangeRate.
        :rtype: TemperatureChangeRate
        """
        return TemperatureChangeRate(micro_degrees_celsius_per_second, TemperatureChangeRateUnits.MicroDegreeCelsiusPerSecond)

    
    @staticmethod
    def from_milli_degrees_celsius_per_second(milli_degrees_celsius_per_second: float):
        """
        Create a new instance of TemperatureChangeRate from a value in milli_degrees_celsius_per_second.

        

        :param meters: The TemperatureChangeRate value in milli_degrees_celsius_per_second.
        :type milli_degrees_celsius_per_second: float
        :return: A new instance of TemperatureChangeRate.
        :rtype: TemperatureChangeRate
        """
        return TemperatureChangeRate(milli_degrees_celsius_per_second, TemperatureChangeRateUnits.MilliDegreeCelsiusPerSecond)

    
    @staticmethod
    def from_centi_degrees_celsius_per_second(centi_degrees_celsius_per_second: float):
        """
        Create a new instance of TemperatureChangeRate from a value in centi_degrees_celsius_per_second.

        

        :param meters: The TemperatureChangeRate value in centi_degrees_celsius_per_second.
        :type centi_degrees_celsius_per_second: float
        :return: A new instance of TemperatureChangeRate.
        :rtype: TemperatureChangeRate
        """
        return TemperatureChangeRate(centi_degrees_celsius_per_second, TemperatureChangeRateUnits.CentiDegreeCelsiusPerSecond)

    
    @staticmethod
    def from_deci_degrees_celsius_per_second(deci_degrees_celsius_per_second: float):
        """
        Create a new instance of TemperatureChangeRate from a value in deci_degrees_celsius_per_second.

        

        :param meters: The TemperatureChangeRate value in deci_degrees_celsius_per_second.
        :type deci_degrees_celsius_per_second: float
        :return: A new instance of TemperatureChangeRate.
        :rtype: TemperatureChangeRate
        """
        return TemperatureChangeRate(deci_degrees_celsius_per_second, TemperatureChangeRateUnits.DeciDegreeCelsiusPerSecond)

    
    @staticmethod
    def from_deca_degrees_celsius_per_second(deca_degrees_celsius_per_second: float):
        """
        Create a new instance of TemperatureChangeRate from a value in deca_degrees_celsius_per_second.

        

        :param meters: The TemperatureChangeRate value in deca_degrees_celsius_per_second.
        :type deca_degrees_celsius_per_second: float
        :return: A new instance of TemperatureChangeRate.
        :rtype: TemperatureChangeRate
        """
        return TemperatureChangeRate(deca_degrees_celsius_per_second, TemperatureChangeRateUnits.DecaDegreeCelsiusPerSecond)

    
    @staticmethod
    def from_hecto_degrees_celsius_per_second(hecto_degrees_celsius_per_second: float):
        """
        Create a new instance of TemperatureChangeRate from a value in hecto_degrees_celsius_per_second.

        

        :param meters: The TemperatureChangeRate value in hecto_degrees_celsius_per_second.
        :type hecto_degrees_celsius_per_second: float
        :return: A new instance of TemperatureChangeRate.
        :rtype: TemperatureChangeRate
        """
        return TemperatureChangeRate(hecto_degrees_celsius_per_second, TemperatureChangeRateUnits.HectoDegreeCelsiusPerSecond)

    
    @staticmethod
    def from_kilo_degrees_celsius_per_second(kilo_degrees_celsius_per_second: float):
        """
        Create a new instance of TemperatureChangeRate from a value in kilo_degrees_celsius_per_second.

        

        :param meters: The TemperatureChangeRate value in kilo_degrees_celsius_per_second.
        :type kilo_degrees_celsius_per_second: float
        :return: A new instance of TemperatureChangeRate.
        :rtype: TemperatureChangeRate
        """
        return TemperatureChangeRate(kilo_degrees_celsius_per_second, TemperatureChangeRateUnits.KiloDegreeCelsiusPerSecond)

    
    @property
    def degrees_celsius_per_second(self) -> float:
        """
        
        """
        if self.__degrees_celsius_per_second != None:
            return self.__degrees_celsius_per_second
        self.__degrees_celsius_per_second = self.__convert_from_base(TemperatureChangeRateUnits.DegreeCelsiusPerSecond)
        return self.__degrees_celsius_per_second

    
    @property
    def degrees_celsius_per_minute(self) -> float:
        """
        
        """
        if self.__degrees_celsius_per_minute != None:
            return self.__degrees_celsius_per_minute
        self.__degrees_celsius_per_minute = self.__convert_from_base(TemperatureChangeRateUnits.DegreeCelsiusPerMinute)
        return self.__degrees_celsius_per_minute

    
    @property
    def nano_degrees_celsius_per_second(self) -> float:
        """
        
        """
        if self.__nano_degrees_celsius_per_second != None:
            return self.__nano_degrees_celsius_per_second
        self.__nano_degrees_celsius_per_second = self.__convert_from_base(TemperatureChangeRateUnits.NanoDegreeCelsiusPerSecond)
        return self.__nano_degrees_celsius_per_second

    
    @property
    def micro_degrees_celsius_per_second(self) -> float:
        """
        
        """
        if self.__micro_degrees_celsius_per_second != None:
            return self.__micro_degrees_celsius_per_second
        self.__micro_degrees_celsius_per_second = self.__convert_from_base(TemperatureChangeRateUnits.MicroDegreeCelsiusPerSecond)
        return self.__micro_degrees_celsius_per_second

    
    @property
    def milli_degrees_celsius_per_second(self) -> float:
        """
        
        """
        if self.__milli_degrees_celsius_per_second != None:
            return self.__milli_degrees_celsius_per_second
        self.__milli_degrees_celsius_per_second = self.__convert_from_base(TemperatureChangeRateUnits.MilliDegreeCelsiusPerSecond)
        return self.__milli_degrees_celsius_per_second

    
    @property
    def centi_degrees_celsius_per_second(self) -> float:
        """
        
        """
        if self.__centi_degrees_celsius_per_second != None:
            return self.__centi_degrees_celsius_per_second
        self.__centi_degrees_celsius_per_second = self.__convert_from_base(TemperatureChangeRateUnits.CentiDegreeCelsiusPerSecond)
        return self.__centi_degrees_celsius_per_second

    
    @property
    def deci_degrees_celsius_per_second(self) -> float:
        """
        
        """
        if self.__deci_degrees_celsius_per_second != None:
            return self.__deci_degrees_celsius_per_second
        self.__deci_degrees_celsius_per_second = self.__convert_from_base(TemperatureChangeRateUnits.DeciDegreeCelsiusPerSecond)
        return self.__deci_degrees_celsius_per_second

    
    @property
    def deca_degrees_celsius_per_second(self) -> float:
        """
        
        """
        if self.__deca_degrees_celsius_per_second != None:
            return self.__deca_degrees_celsius_per_second
        self.__deca_degrees_celsius_per_second = self.__convert_from_base(TemperatureChangeRateUnits.DecaDegreeCelsiusPerSecond)
        return self.__deca_degrees_celsius_per_second

    
    @property
    def hecto_degrees_celsius_per_second(self) -> float:
        """
        
        """
        if self.__hecto_degrees_celsius_per_second != None:
            return self.__hecto_degrees_celsius_per_second
        self.__hecto_degrees_celsius_per_second = self.__convert_from_base(TemperatureChangeRateUnits.HectoDegreeCelsiusPerSecond)
        return self.__hecto_degrees_celsius_per_second

    
    @property
    def kilo_degrees_celsius_per_second(self) -> float:
        """
        
        """
        if self.__kilo_degrees_celsius_per_second != None:
            return self.__kilo_degrees_celsius_per_second
        self.__kilo_degrees_celsius_per_second = self.__convert_from_base(TemperatureChangeRateUnits.KiloDegreeCelsiusPerSecond)
        return self.__kilo_degrees_celsius_per_second

    
    def to_string(self, unit: TemperatureChangeRateUnits = TemperatureChangeRateUnits.DegreeCelsiusPerSecond) -> string:
        """
        Format the TemperatureChangeRate to string.
        Note! the default format for TemperatureChangeRate is DegreeCelsiusPerSecond.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == TemperatureChangeRateUnits.DegreeCelsiusPerSecond:
            return f"""{self.degrees_celsius_per_second} °C/s"""
        
        if unit == TemperatureChangeRateUnits.DegreeCelsiusPerMinute:
            return f"""{self.degrees_celsius_per_minute} °C/min"""
        
        if unit == TemperatureChangeRateUnits.NanoDegreeCelsiusPerSecond:
            return f"""{self.nano_degrees_celsius_per_second} """
        
        if unit == TemperatureChangeRateUnits.MicroDegreeCelsiusPerSecond:
            return f"""{self.micro_degrees_celsius_per_second} """
        
        if unit == TemperatureChangeRateUnits.MilliDegreeCelsiusPerSecond:
            return f"""{self.milli_degrees_celsius_per_second} """
        
        if unit == TemperatureChangeRateUnits.CentiDegreeCelsiusPerSecond:
            return f"""{self.centi_degrees_celsius_per_second} """
        
        if unit == TemperatureChangeRateUnits.DeciDegreeCelsiusPerSecond:
            return f"""{self.deci_degrees_celsius_per_second} """
        
        if unit == TemperatureChangeRateUnits.DecaDegreeCelsiusPerSecond:
            return f"""{self.deca_degrees_celsius_per_second} """
        
        if unit == TemperatureChangeRateUnits.HectoDegreeCelsiusPerSecond:
            return f"""{self.hecto_degrees_celsius_per_second} """
        
        if unit == TemperatureChangeRateUnits.KiloDegreeCelsiusPerSecond:
            return f"""{self.kilo_degrees_celsius_per_second} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: TemperatureChangeRateUnits = TemperatureChangeRateUnits.DegreeCelsiusPerSecond) -> string:
        """
        Get TemperatureChangeRate unit abbreviation.
        Note! the default abbreviation for TemperatureChangeRate is DegreeCelsiusPerSecond.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == TemperatureChangeRateUnits.DegreeCelsiusPerSecond:
            return """°C/s"""
        
        if unit_abbreviation == TemperatureChangeRateUnits.DegreeCelsiusPerMinute:
            return """°C/min"""
        
        if unit_abbreviation == TemperatureChangeRateUnits.NanoDegreeCelsiusPerSecond:
            return """"""
        
        if unit_abbreviation == TemperatureChangeRateUnits.MicroDegreeCelsiusPerSecond:
            return """"""
        
        if unit_abbreviation == TemperatureChangeRateUnits.MilliDegreeCelsiusPerSecond:
            return """"""
        
        if unit_abbreviation == TemperatureChangeRateUnits.CentiDegreeCelsiusPerSecond:
            return """"""
        
        if unit_abbreviation == TemperatureChangeRateUnits.DeciDegreeCelsiusPerSecond:
            return """"""
        
        if unit_abbreviation == TemperatureChangeRateUnits.DecaDegreeCelsiusPerSecond:
            return """"""
        
        if unit_abbreviation == TemperatureChangeRateUnits.HectoDegreeCelsiusPerSecond:
            return """"""
        
        if unit_abbreviation == TemperatureChangeRateUnits.KiloDegreeCelsiusPerSecond:
            return """"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, TemperatureChangeRate):
            raise TypeError("unsupported operand type(s) for +: 'TemperatureChangeRate' and '{}'".format(type(other).__name__))
        return TemperatureChangeRate(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, TemperatureChangeRate):
            raise TypeError("unsupported operand type(s) for *: 'TemperatureChangeRate' and '{}'".format(type(other).__name__))
        return TemperatureChangeRate(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, TemperatureChangeRate):
            raise TypeError("unsupported operand type(s) for -: 'TemperatureChangeRate' and '{}'".format(type(other).__name__))
        return TemperatureChangeRate(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, TemperatureChangeRate):
            raise TypeError("unsupported operand type(s) for /: 'TemperatureChangeRate' and '{}'".format(type(other).__name__))
        return TemperatureChangeRate(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, TemperatureChangeRate):
            raise TypeError("unsupported operand type(s) for %: 'TemperatureChangeRate' and '{}'".format(type(other).__name__))
        return TemperatureChangeRate(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, TemperatureChangeRate):
            raise TypeError("unsupported operand type(s) for **: 'TemperatureChangeRate' and '{}'".format(type(other).__name__))
        return TemperatureChangeRate(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, TemperatureChangeRate):
            raise TypeError("unsupported operand type(s) for ==: 'TemperatureChangeRate' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, TemperatureChangeRate):
            raise TypeError("unsupported operand type(s) for <: 'TemperatureChangeRate' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, TemperatureChangeRate):
            raise TypeError("unsupported operand type(s) for >: 'TemperatureChangeRate' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, TemperatureChangeRate):
            raise TypeError("unsupported operand type(s) for <=: 'TemperatureChangeRate' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, TemperatureChangeRate):
            raise TypeError("unsupported operand type(s) for >=: 'TemperatureChangeRate' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value
from enum import Enum
import math
import string


class IlluminanceUnits(Enum):
        """
            IlluminanceUnits enumeration
        """
        
        Lux = 'lux'
        """
            
        """
        
        MilliLux = 'milli_lux'
        """
            
        """
        
        KiloLux = 'kilo_lux'
        """
            
        """
        
        MegaLux = 'mega_lux'
        """
            
        """
        

class Illuminance:
    """
    In photometry, illuminance is the total luminous flux incident on a surface, per unit area.

    Args:
        value (float): The value.
        from_unit (IlluminanceUnits): The Illuminance unit to create from, The default unit is Lux
    """
    def __init__(self, value: float, from_unit: IlluminanceUnits = IlluminanceUnits.Lux):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__lux = None
        
        self.__milli_lux = None
        
        self.__kilo_lux = None
        
        self.__mega_lux = None
        

    def __convert_from_base(self, from_unit: IlluminanceUnits) -> float:
        value = self.__value
        
        if from_unit == IlluminanceUnits.Lux:
            return (value)
        
        if from_unit == IlluminanceUnits.MilliLux:
            return ((value) / 0.001)
        
        if from_unit == IlluminanceUnits.KiloLux:
            return ((value) / 1000.0)
        
        if from_unit == IlluminanceUnits.MegaLux:
            return ((value) / 1000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: IlluminanceUnits) -> float:
        
        if to_unit == IlluminanceUnits.Lux:
            return (value)
        
        if to_unit == IlluminanceUnits.MilliLux:
            return ((value) * 0.001)
        
        if to_unit == IlluminanceUnits.KiloLux:
            return ((value) * 1000.0)
        
        if to_unit == IlluminanceUnits.MegaLux:
            return ((value) * 1000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
    @staticmethod
    def from_lux(lux: float):
        """
        Create a new instance of Illuminance from a value in lux.

        

        :param meters: The Illuminance value in lux.
        :type lux: float
        :return: A new instance of Illuminance.
        :rtype: Illuminance
        """
        return Illuminance(lux, IlluminanceUnits.Lux)

    
    @staticmethod
    def from_milli_lux(milli_lux: float):
        """
        Create a new instance of Illuminance from a value in milli_lux.

        

        :param meters: The Illuminance value in milli_lux.
        :type milli_lux: float
        :return: A new instance of Illuminance.
        :rtype: Illuminance
        """
        return Illuminance(milli_lux, IlluminanceUnits.MilliLux)

    
    @staticmethod
    def from_kilo_lux(kilo_lux: float):
        """
        Create a new instance of Illuminance from a value in kilo_lux.

        

        :param meters: The Illuminance value in kilo_lux.
        :type kilo_lux: float
        :return: A new instance of Illuminance.
        :rtype: Illuminance
        """
        return Illuminance(kilo_lux, IlluminanceUnits.KiloLux)

    
    @staticmethod
    def from_mega_lux(mega_lux: float):
        """
        Create a new instance of Illuminance from a value in mega_lux.

        

        :param meters: The Illuminance value in mega_lux.
        :type mega_lux: float
        :return: A new instance of Illuminance.
        :rtype: Illuminance
        """
        return Illuminance(mega_lux, IlluminanceUnits.MegaLux)

    
    @property
    def lux(self) -> float:
        """
        
        """
        if self.__lux != None:
            return self.__lux
        self.__lux = self.__convert_from_base(IlluminanceUnits.Lux)
        return self.__lux

    
    @property
    def milli_lux(self) -> float:
        """
        
        """
        if self.__milli_lux != None:
            return self.__milli_lux
        self.__milli_lux = self.__convert_from_base(IlluminanceUnits.MilliLux)
        return self.__milli_lux

    
    @property
    def kilo_lux(self) -> float:
        """
        
        """
        if self.__kilo_lux != None:
            return self.__kilo_lux
        self.__kilo_lux = self.__convert_from_base(IlluminanceUnits.KiloLux)
        return self.__kilo_lux

    
    @property
    def mega_lux(self) -> float:
        """
        
        """
        if self.__mega_lux != None:
            return self.__mega_lux
        self.__mega_lux = self.__convert_from_base(IlluminanceUnits.MegaLux)
        return self.__mega_lux

    
    def to_string(self, unit: IlluminanceUnits = IlluminanceUnits.Lux) -> string:
        """
        Format the Illuminance to string.
        Note! the default format for Illuminance is Lux.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == IlluminanceUnits.Lux:
            return f"""{self.lux} lx"""
        
        if unit == IlluminanceUnits.MilliLux:
            return f"""{self.milli_lux} """
        
        if unit == IlluminanceUnits.KiloLux:
            return f"""{self.kilo_lux} """
        
        if unit == IlluminanceUnits.MegaLux:
            return f"""{self.mega_lux} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: IlluminanceUnits = IlluminanceUnits.Lux) -> string:
        """
        Get Illuminance unit abbreviation.
        Note! the default abbreviation for Illuminance is Lux.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == IlluminanceUnits.Lux:
            return """lx"""
        
        if unit_abbreviation == IlluminanceUnits.MilliLux:
            return """"""
        
        if unit_abbreviation == IlluminanceUnits.KiloLux:
            return """"""
        
        if unit_abbreviation == IlluminanceUnits.MegaLux:
            return """"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, Illuminance):
            raise TypeError("unsupported operand type(s) for +: 'Illuminance' and '{}'".format(type(other).__name__))
        return Illuminance(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, Illuminance):
            raise TypeError("unsupported operand type(s) for *: 'Illuminance' and '{}'".format(type(other).__name__))
        return Illuminance(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, Illuminance):
            raise TypeError("unsupported operand type(s) for -: 'Illuminance' and '{}'".format(type(other).__name__))
        return Illuminance(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, Illuminance):
            raise TypeError("unsupported operand type(s) for /: 'Illuminance' and '{}'".format(type(other).__name__))
        return Illuminance(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, Illuminance):
            raise TypeError("unsupported operand type(s) for %: 'Illuminance' and '{}'".format(type(other).__name__))
        return Illuminance(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, Illuminance):
            raise TypeError("unsupported operand type(s) for **: 'Illuminance' and '{}'".format(type(other).__name__))
        return Illuminance(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, Illuminance):
            raise TypeError("unsupported operand type(s) for ==: 'Illuminance' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, Illuminance):
            raise TypeError("unsupported operand type(s) for <: 'Illuminance' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, Illuminance):
            raise TypeError("unsupported operand type(s) for >: 'Illuminance' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, Illuminance):
            raise TypeError("unsupported operand type(s) for <=: 'Illuminance' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, Illuminance):
            raise TypeError("unsupported operand type(s) for >=: 'Illuminance' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value
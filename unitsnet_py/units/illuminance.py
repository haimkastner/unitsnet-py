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
        
        Millilux = 'millilux'
        """
            
        """
        
        Kilolux = 'kilolux'
        """
            
        """
        
        Megalux = 'megalux'
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
        
        self.__millilux = None
        
        self.__kilolux = None
        
        self.__megalux = None
        

    def __convert_from_base(self, from_unit: IlluminanceUnits) -> float:
        value = self.__value
        
        if from_unit == IlluminanceUnits.Lux:
            return (value)
        
        if from_unit == IlluminanceUnits.Millilux:
            return ((value) / 0.001)
        
        if from_unit == IlluminanceUnits.Kilolux:
            return ((value) / 1000.0)
        
        if from_unit == IlluminanceUnits.Megalux:
            return ((value) / 1000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: IlluminanceUnits) -> float:
        
        if to_unit == IlluminanceUnits.Lux:
            return (value)
        
        if to_unit == IlluminanceUnits.Millilux:
            return ((value) * 0.001)
        
        if to_unit == IlluminanceUnits.Kilolux:
            return ((value) * 1000.0)
        
        if to_unit == IlluminanceUnits.Megalux:
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
    def from_millilux(millilux: float):
        """
        Create a new instance of Illuminance from a value in millilux.

        

        :param meters: The Illuminance value in millilux.
        :type millilux: float
        :return: A new instance of Illuminance.
        :rtype: Illuminance
        """
        return Illuminance(millilux, IlluminanceUnits.Millilux)

    
    @staticmethod
    def from_kilolux(kilolux: float):
        """
        Create a new instance of Illuminance from a value in kilolux.

        

        :param meters: The Illuminance value in kilolux.
        :type kilolux: float
        :return: A new instance of Illuminance.
        :rtype: Illuminance
        """
        return Illuminance(kilolux, IlluminanceUnits.Kilolux)

    
    @staticmethod
    def from_megalux(megalux: float):
        """
        Create a new instance of Illuminance from a value in megalux.

        

        :param meters: The Illuminance value in megalux.
        :type megalux: float
        :return: A new instance of Illuminance.
        :rtype: Illuminance
        """
        return Illuminance(megalux, IlluminanceUnits.Megalux)

    
    @property
    def lux(self) -> float:
        """
        
        """
        if self.__lux != None:
            return self.__lux
        self.__lux = self.__convert_from_base(IlluminanceUnits.Lux)
        return self.__lux

    
    @property
    def millilux(self) -> float:
        """
        
        """
        if self.__millilux != None:
            return self.__millilux
        self.__millilux = self.__convert_from_base(IlluminanceUnits.Millilux)
        return self.__millilux

    
    @property
    def kilolux(self) -> float:
        """
        
        """
        if self.__kilolux != None:
            return self.__kilolux
        self.__kilolux = self.__convert_from_base(IlluminanceUnits.Kilolux)
        return self.__kilolux

    
    @property
    def megalux(self) -> float:
        """
        
        """
        if self.__megalux != None:
            return self.__megalux
        self.__megalux = self.__convert_from_base(IlluminanceUnits.Megalux)
        return self.__megalux

    
    def to_string(self, unit: IlluminanceUnits = IlluminanceUnits.Lux) -> string:
        """
        Format the Illuminance to string.
        Note! the default format for Illuminance is Lux.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == IlluminanceUnits.Lux:
            return f"""{self.lux} lx"""
        
        if unit == IlluminanceUnits.Millilux:
            return f"""{self.millilux} """
        
        if unit == IlluminanceUnits.Kilolux:
            return f"""{self.kilolux} """
        
        if unit == IlluminanceUnits.Megalux:
            return f"""{self.megalux} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: IlluminanceUnits = IlluminanceUnits.Lux) -> string:
        """
        Get Illuminance unit abbreviation.
        Note! the default abbreviation for Illuminance is Lux.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == IlluminanceUnits.Lux:
            return """lx"""
        
        if unit_abbreviation == IlluminanceUnits.Millilux:
            return """"""
        
        if unit_abbreviation == IlluminanceUnits.Kilolux:
            return """"""
        
        if unit_abbreviation == IlluminanceUnits.Megalux:
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
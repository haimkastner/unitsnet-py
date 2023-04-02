from enum import Enum
import math
import string


class ElectricResistanceUnits(Enum):
        """
            ElectricResistanceUnits enumeration
        """
        
        Ohm = 'ohm'
        """
            
        """
        
        MicroOhm = 'micro_ohm'
        """
            
        """
        
        MilliOhm = 'milli_ohm'
        """
            
        """
        
        KiloOhm = 'kilo_ohm'
        """
            
        """
        
        MegaOhm = 'mega_ohm'
        """
            
        """
        
        GigaOhm = 'giga_ohm'
        """
            
        """
        
        TeraOhm = 'tera_ohm'
        """
            
        """
        

class ElectricResistance:
    """
    The electrical resistance of an electrical conductor is the opposition to the passage of an electric current through that conductor.

    Args:
        value (float): The value.
        from_unit (ElectricResistanceUnits): The ElectricResistance unit to create from, The default unit is Ohm
    """
    def __init__(self, value: float, from_unit: ElectricResistanceUnits = ElectricResistanceUnits.Ohm):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__ohms = None
        
        self.__micro_ohms = None
        
        self.__milli_ohms = None
        
        self.__kilo_ohms = None
        
        self.__mega_ohms = None
        
        self.__giga_ohms = None
        
        self.__tera_ohms = None
        

    def __convert_from_base(self, from_unit: ElectricResistanceUnits) -> float:
        value = self.__value
        
        if from_unit == ElectricResistanceUnits.Ohm:
            return (value)
        
        if from_unit == ElectricResistanceUnits.MicroOhm:
            return ((value) / 1e-06)
        
        if from_unit == ElectricResistanceUnits.MilliOhm:
            return ((value) / 0.001)
        
        if from_unit == ElectricResistanceUnits.KiloOhm:
            return ((value) / 1000.0)
        
        if from_unit == ElectricResistanceUnits.MegaOhm:
            return ((value) / 1000000.0)
        
        if from_unit == ElectricResistanceUnits.GigaOhm:
            return ((value) / 1000000000.0)
        
        if from_unit == ElectricResistanceUnits.TeraOhm:
            return ((value) / 1000000000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: ElectricResistanceUnits) -> float:
        
        if to_unit == ElectricResistanceUnits.Ohm:
            return (value)
        
        if to_unit == ElectricResistanceUnits.MicroOhm:
            return ((value) * 1e-06)
        
        if to_unit == ElectricResistanceUnits.MilliOhm:
            return ((value) * 0.001)
        
        if to_unit == ElectricResistanceUnits.KiloOhm:
            return ((value) * 1000.0)
        
        if to_unit == ElectricResistanceUnits.MegaOhm:
            return ((value) * 1000000.0)
        
        if to_unit == ElectricResistanceUnits.GigaOhm:
            return ((value) * 1000000000.0)
        
        if to_unit == ElectricResistanceUnits.TeraOhm:
            return ((value) * 1000000000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
    @staticmethod
    def from_ohms(ohms: float):
        """
        Create a new instance of ElectricResistance from a value in ohms.

        

        :param meters: The ElectricResistance value in ohms.
        :type ohms: float
        :return: A new instance of ElectricResistance.
        :rtype: ElectricResistance
        """
        return ElectricResistance(ohms, ElectricResistanceUnits.Ohm)

    
    @staticmethod
    def from_micro_ohms(micro_ohms: float):
        """
        Create a new instance of ElectricResistance from a value in micro_ohms.

        

        :param meters: The ElectricResistance value in micro_ohms.
        :type micro_ohms: float
        :return: A new instance of ElectricResistance.
        :rtype: ElectricResistance
        """
        return ElectricResistance(micro_ohms, ElectricResistanceUnits.MicroOhm)

    
    @staticmethod
    def from_milli_ohms(milli_ohms: float):
        """
        Create a new instance of ElectricResistance from a value in milli_ohms.

        

        :param meters: The ElectricResistance value in milli_ohms.
        :type milli_ohms: float
        :return: A new instance of ElectricResistance.
        :rtype: ElectricResistance
        """
        return ElectricResistance(milli_ohms, ElectricResistanceUnits.MilliOhm)

    
    @staticmethod
    def from_kilo_ohms(kilo_ohms: float):
        """
        Create a new instance of ElectricResistance from a value in kilo_ohms.

        

        :param meters: The ElectricResistance value in kilo_ohms.
        :type kilo_ohms: float
        :return: A new instance of ElectricResistance.
        :rtype: ElectricResistance
        """
        return ElectricResistance(kilo_ohms, ElectricResistanceUnits.KiloOhm)

    
    @staticmethod
    def from_mega_ohms(mega_ohms: float):
        """
        Create a new instance of ElectricResistance from a value in mega_ohms.

        

        :param meters: The ElectricResistance value in mega_ohms.
        :type mega_ohms: float
        :return: A new instance of ElectricResistance.
        :rtype: ElectricResistance
        """
        return ElectricResistance(mega_ohms, ElectricResistanceUnits.MegaOhm)

    
    @staticmethod
    def from_giga_ohms(giga_ohms: float):
        """
        Create a new instance of ElectricResistance from a value in giga_ohms.

        

        :param meters: The ElectricResistance value in giga_ohms.
        :type giga_ohms: float
        :return: A new instance of ElectricResistance.
        :rtype: ElectricResistance
        """
        return ElectricResistance(giga_ohms, ElectricResistanceUnits.GigaOhm)

    
    @staticmethod
    def from_tera_ohms(tera_ohms: float):
        """
        Create a new instance of ElectricResistance from a value in tera_ohms.

        

        :param meters: The ElectricResistance value in tera_ohms.
        :type tera_ohms: float
        :return: A new instance of ElectricResistance.
        :rtype: ElectricResistance
        """
        return ElectricResistance(tera_ohms, ElectricResistanceUnits.TeraOhm)

    
    @property
    def ohms(self) -> float:
        """
        
        """
        if self.__ohms != None:
            return self.__ohms
        self.__ohms = self.__convert_from_base(ElectricResistanceUnits.Ohm)
        return self.__ohms

    
    @property
    def micro_ohms(self) -> float:
        """
        
        """
        if self.__micro_ohms != None:
            return self.__micro_ohms
        self.__micro_ohms = self.__convert_from_base(ElectricResistanceUnits.MicroOhm)
        return self.__micro_ohms

    
    @property
    def milli_ohms(self) -> float:
        """
        
        """
        if self.__milli_ohms != None:
            return self.__milli_ohms
        self.__milli_ohms = self.__convert_from_base(ElectricResistanceUnits.MilliOhm)
        return self.__milli_ohms

    
    @property
    def kilo_ohms(self) -> float:
        """
        
        """
        if self.__kilo_ohms != None:
            return self.__kilo_ohms
        self.__kilo_ohms = self.__convert_from_base(ElectricResistanceUnits.KiloOhm)
        return self.__kilo_ohms

    
    @property
    def mega_ohms(self) -> float:
        """
        
        """
        if self.__mega_ohms != None:
            return self.__mega_ohms
        self.__mega_ohms = self.__convert_from_base(ElectricResistanceUnits.MegaOhm)
        return self.__mega_ohms

    
    @property
    def giga_ohms(self) -> float:
        """
        
        """
        if self.__giga_ohms != None:
            return self.__giga_ohms
        self.__giga_ohms = self.__convert_from_base(ElectricResistanceUnits.GigaOhm)
        return self.__giga_ohms

    
    @property
    def tera_ohms(self) -> float:
        """
        
        """
        if self.__tera_ohms != None:
            return self.__tera_ohms
        self.__tera_ohms = self.__convert_from_base(ElectricResistanceUnits.TeraOhm)
        return self.__tera_ohms

    
    def to_string(self, unit: ElectricResistanceUnits = ElectricResistanceUnits.Ohm) -> string:
        """
        Format the ElectricResistance to string.
        Note! the default format for ElectricResistance is Ohm.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == ElectricResistanceUnits.Ohm:
            return f"""{self.ohms} Ω"""
        
        if unit == ElectricResistanceUnits.MicroOhm:
            return f"""{self.micro_ohms} """
        
        if unit == ElectricResistanceUnits.MilliOhm:
            return f"""{self.milli_ohms} """
        
        if unit == ElectricResistanceUnits.KiloOhm:
            return f"""{self.kilo_ohms} """
        
        if unit == ElectricResistanceUnits.MegaOhm:
            return f"""{self.mega_ohms} """
        
        if unit == ElectricResistanceUnits.GigaOhm:
            return f"""{self.giga_ohms} """
        
        if unit == ElectricResistanceUnits.TeraOhm:
            return f"""{self.tera_ohms} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: ElectricResistanceUnits = ElectricResistanceUnits.Ohm) -> string:
        """
        Get ElectricResistance unit abbreviation.
        Note! the default abbreviation for ElectricResistance is Ohm.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == ElectricResistanceUnits.Ohm:
            return """Ω"""
        
        if unit_abbreviation == ElectricResistanceUnits.MicroOhm:
            return """"""
        
        if unit_abbreviation == ElectricResistanceUnits.MilliOhm:
            return """"""
        
        if unit_abbreviation == ElectricResistanceUnits.KiloOhm:
            return """"""
        
        if unit_abbreviation == ElectricResistanceUnits.MegaOhm:
            return """"""
        
        if unit_abbreviation == ElectricResistanceUnits.GigaOhm:
            return """"""
        
        if unit_abbreviation == ElectricResistanceUnits.TeraOhm:
            return """"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, ElectricResistance):
            raise TypeError("unsupported operand type(s) for +: 'ElectricResistance' and '{}'".format(type(other).__name__))
        return ElectricResistance(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, ElectricResistance):
            raise TypeError("unsupported operand type(s) for *: 'ElectricResistance' and '{}'".format(type(other).__name__))
        return ElectricResistance(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, ElectricResistance):
            raise TypeError("unsupported operand type(s) for -: 'ElectricResistance' and '{}'".format(type(other).__name__))
        return ElectricResistance(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, ElectricResistance):
            raise TypeError("unsupported operand type(s) for /: 'ElectricResistance' and '{}'".format(type(other).__name__))
        return ElectricResistance(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, ElectricResistance):
            raise TypeError("unsupported operand type(s) for %: 'ElectricResistance' and '{}'".format(type(other).__name__))
        return ElectricResistance(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, ElectricResistance):
            raise TypeError("unsupported operand type(s) for **: 'ElectricResistance' and '{}'".format(type(other).__name__))
        return ElectricResistance(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, ElectricResistance):
            raise TypeError("unsupported operand type(s) for ==: 'ElectricResistance' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, ElectricResistance):
            raise TypeError("unsupported operand type(s) for <: 'ElectricResistance' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, ElectricResistance):
            raise TypeError("unsupported operand type(s) for >: 'ElectricResistance' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, ElectricResistance):
            raise TypeError("unsupported operand type(s) for <=: 'ElectricResistance' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, ElectricResistance):
            raise TypeError("unsupported operand type(s) for >=: 'ElectricResistance' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value
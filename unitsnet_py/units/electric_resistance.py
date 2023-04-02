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
        
        Microohm = 'microohm'
        """
            
        """
        
        Milliohm = 'milliohm'
        """
            
        """
        
        Kiloohm = 'kiloohm'
        """
            
        """
        
        Megaohm = 'megaohm'
        """
            
        """
        
        Gigaohm = 'gigaohm'
        """
            
        """
        
        Teraohm = 'teraohm'
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
        
        self.__microohms = None
        
        self.__milliohms = None
        
        self.__kiloohms = None
        
        self.__megaohms = None
        
        self.__gigaohms = None
        
        self.__teraohms = None
        

    def __convert_from_base(self, from_unit: ElectricResistanceUnits) -> float:
        value = self.__value
        
        if from_unit == ElectricResistanceUnits.Ohm:
            return (value)
        
        if from_unit == ElectricResistanceUnits.Microohm:
            return ((value) / 1e-06)
        
        if from_unit == ElectricResistanceUnits.Milliohm:
            return ((value) / 0.001)
        
        if from_unit == ElectricResistanceUnits.Kiloohm:
            return ((value) / 1000.0)
        
        if from_unit == ElectricResistanceUnits.Megaohm:
            return ((value) / 1000000.0)
        
        if from_unit == ElectricResistanceUnits.Gigaohm:
            return ((value) / 1000000000.0)
        
        if from_unit == ElectricResistanceUnits.Teraohm:
            return ((value) / 1000000000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: ElectricResistanceUnits) -> float:
        
        if to_unit == ElectricResistanceUnits.Ohm:
            return (value)
        
        if to_unit == ElectricResistanceUnits.Microohm:
            return ((value) * 1e-06)
        
        if to_unit == ElectricResistanceUnits.Milliohm:
            return ((value) * 0.001)
        
        if to_unit == ElectricResistanceUnits.Kiloohm:
            return ((value) * 1000.0)
        
        if to_unit == ElectricResistanceUnits.Megaohm:
            return ((value) * 1000000.0)
        
        if to_unit == ElectricResistanceUnits.Gigaohm:
            return ((value) * 1000000000.0)
        
        if to_unit == ElectricResistanceUnits.Teraohm:
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
    def from_microohms(microohms: float):
        """
        Create a new instance of ElectricResistance from a value in microohms.

        

        :param meters: The ElectricResistance value in microohms.
        :type microohms: float
        :return: A new instance of ElectricResistance.
        :rtype: ElectricResistance
        """
        return ElectricResistance(microohms, ElectricResistanceUnits.Microohm)

    
    @staticmethod
    def from_milliohms(milliohms: float):
        """
        Create a new instance of ElectricResistance from a value in milliohms.

        

        :param meters: The ElectricResistance value in milliohms.
        :type milliohms: float
        :return: A new instance of ElectricResistance.
        :rtype: ElectricResistance
        """
        return ElectricResistance(milliohms, ElectricResistanceUnits.Milliohm)

    
    @staticmethod
    def from_kiloohms(kiloohms: float):
        """
        Create a new instance of ElectricResistance from a value in kiloohms.

        

        :param meters: The ElectricResistance value in kiloohms.
        :type kiloohms: float
        :return: A new instance of ElectricResistance.
        :rtype: ElectricResistance
        """
        return ElectricResistance(kiloohms, ElectricResistanceUnits.Kiloohm)

    
    @staticmethod
    def from_megaohms(megaohms: float):
        """
        Create a new instance of ElectricResistance from a value in megaohms.

        

        :param meters: The ElectricResistance value in megaohms.
        :type megaohms: float
        :return: A new instance of ElectricResistance.
        :rtype: ElectricResistance
        """
        return ElectricResistance(megaohms, ElectricResistanceUnits.Megaohm)

    
    @staticmethod
    def from_gigaohms(gigaohms: float):
        """
        Create a new instance of ElectricResistance from a value in gigaohms.

        

        :param meters: The ElectricResistance value in gigaohms.
        :type gigaohms: float
        :return: A new instance of ElectricResistance.
        :rtype: ElectricResistance
        """
        return ElectricResistance(gigaohms, ElectricResistanceUnits.Gigaohm)

    
    @staticmethod
    def from_teraohms(teraohms: float):
        """
        Create a new instance of ElectricResistance from a value in teraohms.

        

        :param meters: The ElectricResistance value in teraohms.
        :type teraohms: float
        :return: A new instance of ElectricResistance.
        :rtype: ElectricResistance
        """
        return ElectricResistance(teraohms, ElectricResistanceUnits.Teraohm)

    
    @property
    def ohms(self) -> float:
        """
        
        """
        if self.__ohms != None:
            return self.__ohms
        self.__ohms = self.__convert_from_base(ElectricResistanceUnits.Ohm)
        return self.__ohms

    
    @property
    def microohms(self) -> float:
        """
        
        """
        if self.__microohms != None:
            return self.__microohms
        self.__microohms = self.__convert_from_base(ElectricResistanceUnits.Microohm)
        return self.__microohms

    
    @property
    def milliohms(self) -> float:
        """
        
        """
        if self.__milliohms != None:
            return self.__milliohms
        self.__milliohms = self.__convert_from_base(ElectricResistanceUnits.Milliohm)
        return self.__milliohms

    
    @property
    def kiloohms(self) -> float:
        """
        
        """
        if self.__kiloohms != None:
            return self.__kiloohms
        self.__kiloohms = self.__convert_from_base(ElectricResistanceUnits.Kiloohm)
        return self.__kiloohms

    
    @property
    def megaohms(self) -> float:
        """
        
        """
        if self.__megaohms != None:
            return self.__megaohms
        self.__megaohms = self.__convert_from_base(ElectricResistanceUnits.Megaohm)
        return self.__megaohms

    
    @property
    def gigaohms(self) -> float:
        """
        
        """
        if self.__gigaohms != None:
            return self.__gigaohms
        self.__gigaohms = self.__convert_from_base(ElectricResistanceUnits.Gigaohm)
        return self.__gigaohms

    
    @property
    def teraohms(self) -> float:
        """
        
        """
        if self.__teraohms != None:
            return self.__teraohms
        self.__teraohms = self.__convert_from_base(ElectricResistanceUnits.Teraohm)
        return self.__teraohms

    
    def to_string(self, unit: ElectricResistanceUnits = ElectricResistanceUnits.Ohm) -> string:
        """
        Format the ElectricResistance to string.
        Note! the default format for ElectricResistance is Ohm.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == ElectricResistanceUnits.Ohm:
            return f"""{self.ohms} Ω"""
        
        if unit == ElectricResistanceUnits.Microohm:
            return f"""{self.microohms} """
        
        if unit == ElectricResistanceUnits.Milliohm:
            return f"""{self.milliohms} """
        
        if unit == ElectricResistanceUnits.Kiloohm:
            return f"""{self.kiloohms} """
        
        if unit == ElectricResistanceUnits.Megaohm:
            return f"""{self.megaohms} """
        
        if unit == ElectricResistanceUnits.Gigaohm:
            return f"""{self.gigaohms} """
        
        if unit == ElectricResistanceUnits.Teraohm:
            return f"""{self.teraohms} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: ElectricResistanceUnits = ElectricResistanceUnits.Ohm) -> string:
        """
        Get ElectricResistance unit abbreviation.
        Note! the default abbreviation for ElectricResistance is Ohm.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == ElectricResistanceUnits.Ohm:
            return """Ω"""
        
        if unit_abbreviation == ElectricResistanceUnits.Microohm:
            return """"""
        
        if unit_abbreviation == ElectricResistanceUnits.Milliohm:
            return """"""
        
        if unit_abbreviation == ElectricResistanceUnits.Kiloohm:
            return """"""
        
        if unit_abbreviation == ElectricResistanceUnits.Megaohm:
            return """"""
        
        if unit_abbreviation == ElectricResistanceUnits.Gigaohm:
            return """"""
        
        if unit_abbreviation == ElectricResistanceUnits.Teraohm:
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
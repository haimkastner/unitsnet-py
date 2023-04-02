from enum import Enum
import math
import string


class ElectricCurrentUnits(Enum):
        """
            ElectricCurrentUnits enumeration
        """
        
        Ampere = 'ampere'
        """
            
        """
        
        Femtoampere = 'femtoampere'
        """
            
        """
        
        Picoampere = 'picoampere'
        """
            
        """
        
        Nanoampere = 'nanoampere'
        """
            
        """
        
        Microampere = 'microampere'
        """
            
        """
        
        Milliampere = 'milliampere'
        """
            
        """
        
        Centiampere = 'centiampere'
        """
            
        """
        
        Kiloampere = 'kiloampere'
        """
            
        """
        
        Megaampere = 'megaampere'
        """
            
        """
        

class ElectricCurrent:
    """
    An electric current is a flow of electric charge. In electric circuits this charge is often carried by moving electrons in a wire. It can also be carried by ions in an electrolyte, or by both ions and electrons such as in a plasma.

    Args:
        value (float): The value.
        from_unit (ElectricCurrentUnits): The ElectricCurrent unit to create from, The default unit is Ampere
    """
    def __init__(self, value: float, from_unit: ElectricCurrentUnits = ElectricCurrentUnits.Ampere):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__amperes = None
        
        self.__femtoamperes = None
        
        self.__picoamperes = None
        
        self.__nanoamperes = None
        
        self.__microamperes = None
        
        self.__milliamperes = None
        
        self.__centiamperes = None
        
        self.__kiloamperes = None
        
        self.__megaamperes = None
        

    def __convert_from_base(self, from_unit: ElectricCurrentUnits) -> float:
        value = self.__value
        
        if from_unit == ElectricCurrentUnits.Ampere:
            return (value)
        
        if from_unit == ElectricCurrentUnits.Femtoampere:
            return ((value) / 1e-15)
        
        if from_unit == ElectricCurrentUnits.Picoampere:
            return ((value) / 1e-12)
        
        if from_unit == ElectricCurrentUnits.Nanoampere:
            return ((value) / 1e-09)
        
        if from_unit == ElectricCurrentUnits.Microampere:
            return ((value) / 1e-06)
        
        if from_unit == ElectricCurrentUnits.Milliampere:
            return ((value) / 0.001)
        
        if from_unit == ElectricCurrentUnits.Centiampere:
            return ((value) / 0.01)
        
        if from_unit == ElectricCurrentUnits.Kiloampere:
            return ((value) / 1000.0)
        
        if from_unit == ElectricCurrentUnits.Megaampere:
            return ((value) / 1000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: ElectricCurrentUnits) -> float:
        
        if to_unit == ElectricCurrentUnits.Ampere:
            return (value)
        
        if to_unit == ElectricCurrentUnits.Femtoampere:
            return ((value) * 1e-15)
        
        if to_unit == ElectricCurrentUnits.Picoampere:
            return ((value) * 1e-12)
        
        if to_unit == ElectricCurrentUnits.Nanoampere:
            return ((value) * 1e-09)
        
        if to_unit == ElectricCurrentUnits.Microampere:
            return ((value) * 1e-06)
        
        if to_unit == ElectricCurrentUnits.Milliampere:
            return ((value) * 0.001)
        
        if to_unit == ElectricCurrentUnits.Centiampere:
            return ((value) * 0.01)
        
        if to_unit == ElectricCurrentUnits.Kiloampere:
            return ((value) * 1000.0)
        
        if to_unit == ElectricCurrentUnits.Megaampere:
            return ((value) * 1000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
    @staticmethod
    def from_amperes(amperes: float):
        """
        Create a new instance of ElectricCurrent from a value in amperes.

        

        :param meters: The ElectricCurrent value in amperes.
        :type amperes: float
        :return: A new instance of ElectricCurrent.
        :rtype: ElectricCurrent
        """
        return ElectricCurrent(amperes, ElectricCurrentUnits.Ampere)

    
    @staticmethod
    def from_femtoamperes(femtoamperes: float):
        """
        Create a new instance of ElectricCurrent from a value in femtoamperes.

        

        :param meters: The ElectricCurrent value in femtoamperes.
        :type femtoamperes: float
        :return: A new instance of ElectricCurrent.
        :rtype: ElectricCurrent
        """
        return ElectricCurrent(femtoamperes, ElectricCurrentUnits.Femtoampere)

    
    @staticmethod
    def from_picoamperes(picoamperes: float):
        """
        Create a new instance of ElectricCurrent from a value in picoamperes.

        

        :param meters: The ElectricCurrent value in picoamperes.
        :type picoamperes: float
        :return: A new instance of ElectricCurrent.
        :rtype: ElectricCurrent
        """
        return ElectricCurrent(picoamperes, ElectricCurrentUnits.Picoampere)

    
    @staticmethod
    def from_nanoamperes(nanoamperes: float):
        """
        Create a new instance of ElectricCurrent from a value in nanoamperes.

        

        :param meters: The ElectricCurrent value in nanoamperes.
        :type nanoamperes: float
        :return: A new instance of ElectricCurrent.
        :rtype: ElectricCurrent
        """
        return ElectricCurrent(nanoamperes, ElectricCurrentUnits.Nanoampere)

    
    @staticmethod
    def from_microamperes(microamperes: float):
        """
        Create a new instance of ElectricCurrent from a value in microamperes.

        

        :param meters: The ElectricCurrent value in microamperes.
        :type microamperes: float
        :return: A new instance of ElectricCurrent.
        :rtype: ElectricCurrent
        """
        return ElectricCurrent(microamperes, ElectricCurrentUnits.Microampere)

    
    @staticmethod
    def from_milliamperes(milliamperes: float):
        """
        Create a new instance of ElectricCurrent from a value in milliamperes.

        

        :param meters: The ElectricCurrent value in milliamperes.
        :type milliamperes: float
        :return: A new instance of ElectricCurrent.
        :rtype: ElectricCurrent
        """
        return ElectricCurrent(milliamperes, ElectricCurrentUnits.Milliampere)

    
    @staticmethod
    def from_centiamperes(centiamperes: float):
        """
        Create a new instance of ElectricCurrent from a value in centiamperes.

        

        :param meters: The ElectricCurrent value in centiamperes.
        :type centiamperes: float
        :return: A new instance of ElectricCurrent.
        :rtype: ElectricCurrent
        """
        return ElectricCurrent(centiamperes, ElectricCurrentUnits.Centiampere)

    
    @staticmethod
    def from_kiloamperes(kiloamperes: float):
        """
        Create a new instance of ElectricCurrent from a value in kiloamperes.

        

        :param meters: The ElectricCurrent value in kiloamperes.
        :type kiloamperes: float
        :return: A new instance of ElectricCurrent.
        :rtype: ElectricCurrent
        """
        return ElectricCurrent(kiloamperes, ElectricCurrentUnits.Kiloampere)

    
    @staticmethod
    def from_megaamperes(megaamperes: float):
        """
        Create a new instance of ElectricCurrent from a value in megaamperes.

        

        :param meters: The ElectricCurrent value in megaamperes.
        :type megaamperes: float
        :return: A new instance of ElectricCurrent.
        :rtype: ElectricCurrent
        """
        return ElectricCurrent(megaamperes, ElectricCurrentUnits.Megaampere)

    
    @property
    def amperes(self) -> float:
        """
        
        """
        if self.__amperes != None:
            return self.__amperes
        self.__amperes = self.__convert_from_base(ElectricCurrentUnits.Ampere)
        return self.__amperes

    
    @property
    def femtoamperes(self) -> float:
        """
        
        """
        if self.__femtoamperes != None:
            return self.__femtoamperes
        self.__femtoamperes = self.__convert_from_base(ElectricCurrentUnits.Femtoampere)
        return self.__femtoamperes

    
    @property
    def picoamperes(self) -> float:
        """
        
        """
        if self.__picoamperes != None:
            return self.__picoamperes
        self.__picoamperes = self.__convert_from_base(ElectricCurrentUnits.Picoampere)
        return self.__picoamperes

    
    @property
    def nanoamperes(self) -> float:
        """
        
        """
        if self.__nanoamperes != None:
            return self.__nanoamperes
        self.__nanoamperes = self.__convert_from_base(ElectricCurrentUnits.Nanoampere)
        return self.__nanoamperes

    
    @property
    def microamperes(self) -> float:
        """
        
        """
        if self.__microamperes != None:
            return self.__microamperes
        self.__microamperes = self.__convert_from_base(ElectricCurrentUnits.Microampere)
        return self.__microamperes

    
    @property
    def milliamperes(self) -> float:
        """
        
        """
        if self.__milliamperes != None:
            return self.__milliamperes
        self.__milliamperes = self.__convert_from_base(ElectricCurrentUnits.Milliampere)
        return self.__milliamperes

    
    @property
    def centiamperes(self) -> float:
        """
        
        """
        if self.__centiamperes != None:
            return self.__centiamperes
        self.__centiamperes = self.__convert_from_base(ElectricCurrentUnits.Centiampere)
        return self.__centiamperes

    
    @property
    def kiloamperes(self) -> float:
        """
        
        """
        if self.__kiloamperes != None:
            return self.__kiloamperes
        self.__kiloamperes = self.__convert_from_base(ElectricCurrentUnits.Kiloampere)
        return self.__kiloamperes

    
    @property
    def megaamperes(self) -> float:
        """
        
        """
        if self.__megaamperes != None:
            return self.__megaamperes
        self.__megaamperes = self.__convert_from_base(ElectricCurrentUnits.Megaampere)
        return self.__megaamperes

    
    def to_string(self, unit: ElectricCurrentUnits = ElectricCurrentUnits.Ampere) -> string:
        """
        Format the ElectricCurrent to string.
        Note! the default format for ElectricCurrent is Ampere.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == ElectricCurrentUnits.Ampere:
            return f"""{self.amperes} A"""
        
        if unit == ElectricCurrentUnits.Femtoampere:
            return f"""{self.femtoamperes} """
        
        if unit == ElectricCurrentUnits.Picoampere:
            return f"""{self.picoamperes} """
        
        if unit == ElectricCurrentUnits.Nanoampere:
            return f"""{self.nanoamperes} """
        
        if unit == ElectricCurrentUnits.Microampere:
            return f"""{self.microamperes} """
        
        if unit == ElectricCurrentUnits.Milliampere:
            return f"""{self.milliamperes} """
        
        if unit == ElectricCurrentUnits.Centiampere:
            return f"""{self.centiamperes} """
        
        if unit == ElectricCurrentUnits.Kiloampere:
            return f"""{self.kiloamperes} """
        
        if unit == ElectricCurrentUnits.Megaampere:
            return f"""{self.megaamperes} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: ElectricCurrentUnits = ElectricCurrentUnits.Ampere) -> string:
        """
        Get ElectricCurrent unit abbreviation.
        Note! the default abbreviation for ElectricCurrent is Ampere.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == ElectricCurrentUnits.Ampere:
            return """A"""
        
        if unit_abbreviation == ElectricCurrentUnits.Femtoampere:
            return """"""
        
        if unit_abbreviation == ElectricCurrentUnits.Picoampere:
            return """"""
        
        if unit_abbreviation == ElectricCurrentUnits.Nanoampere:
            return """"""
        
        if unit_abbreviation == ElectricCurrentUnits.Microampere:
            return """"""
        
        if unit_abbreviation == ElectricCurrentUnits.Milliampere:
            return """"""
        
        if unit_abbreviation == ElectricCurrentUnits.Centiampere:
            return """"""
        
        if unit_abbreviation == ElectricCurrentUnits.Kiloampere:
            return """"""
        
        if unit_abbreviation == ElectricCurrentUnits.Megaampere:
            return """"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, ElectricCurrent):
            raise TypeError("unsupported operand type(s) for +: 'ElectricCurrent' and '{}'".format(type(other).__name__))
        return ElectricCurrent(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, ElectricCurrent):
            raise TypeError("unsupported operand type(s) for *: 'ElectricCurrent' and '{}'".format(type(other).__name__))
        return ElectricCurrent(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, ElectricCurrent):
            raise TypeError("unsupported operand type(s) for -: 'ElectricCurrent' and '{}'".format(type(other).__name__))
        return ElectricCurrent(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, ElectricCurrent):
            raise TypeError("unsupported operand type(s) for /: 'ElectricCurrent' and '{}'".format(type(other).__name__))
        return ElectricCurrent(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, ElectricCurrent):
            raise TypeError("unsupported operand type(s) for %: 'ElectricCurrent' and '{}'".format(type(other).__name__))
        return ElectricCurrent(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, ElectricCurrent):
            raise TypeError("unsupported operand type(s) for **: 'ElectricCurrent' and '{}'".format(type(other).__name__))
        return ElectricCurrent(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, ElectricCurrent):
            raise TypeError("unsupported operand type(s) for ==: 'ElectricCurrent' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, ElectricCurrent):
            raise TypeError("unsupported operand type(s) for <: 'ElectricCurrent' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, ElectricCurrent):
            raise TypeError("unsupported operand type(s) for >: 'ElectricCurrent' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, ElectricCurrent):
            raise TypeError("unsupported operand type(s) for <=: 'ElectricCurrent' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, ElectricCurrent):
            raise TypeError("unsupported operand type(s) for >=: 'ElectricCurrent' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value
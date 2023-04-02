from enum import Enum
import math
import string


class ElectricInductanceUnits(Enum):
        """
            ElectricInductanceUnits enumeration
        """
        
        Henry = 'henry'
        """
            
        """
        
        Picohenry = 'picohenry'
        """
            
        """
        
        Nanohenry = 'nanohenry'
        """
            
        """
        
        Microhenry = 'microhenry'
        """
            
        """
        
        Millihenry = 'millihenry'
        """
            
        """
        

class ElectricInductance:
    """
    Inductance is a property of an electrical conductor which opposes a change in current.

    Args:
        value (float): The value.
        from_unit (ElectricInductanceUnits): The ElectricInductance unit to create from, The default unit is Henry
    """
    def __init__(self, value: float, from_unit: ElectricInductanceUnits = ElectricInductanceUnits.Henry):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__henries = None
        
        self.__picohenries = None
        
        self.__nanohenries = None
        
        self.__microhenries = None
        
        self.__millihenries = None
        

    def __convert_from_base(self, from_unit: ElectricInductanceUnits) -> float:
        value = self.__value
        
        if from_unit == ElectricInductanceUnits.Henry:
            return (value)
        
        if from_unit == ElectricInductanceUnits.Picohenry:
            return ((value) / 1e-12)
        
        if from_unit == ElectricInductanceUnits.Nanohenry:
            return ((value) / 1e-09)
        
        if from_unit == ElectricInductanceUnits.Microhenry:
            return ((value) / 1e-06)
        
        if from_unit == ElectricInductanceUnits.Millihenry:
            return ((value) / 0.001)
        
        return None


    def __convert_to_base(self, value: float, to_unit: ElectricInductanceUnits) -> float:
        
        if to_unit == ElectricInductanceUnits.Henry:
            return (value)
        
        if to_unit == ElectricInductanceUnits.Picohenry:
            return ((value) * 1e-12)
        
        if to_unit == ElectricInductanceUnits.Nanohenry:
            return ((value) * 1e-09)
        
        if to_unit == ElectricInductanceUnits.Microhenry:
            return ((value) * 1e-06)
        
        if to_unit == ElectricInductanceUnits.Millihenry:
            return ((value) * 0.001)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
    @staticmethod
    def from_henries(henries: float):
        """
        Create a new instance of ElectricInductance from a value in henries.

        

        :param meters: The ElectricInductance value in henries.
        :type henries: float
        :return: A new instance of ElectricInductance.
        :rtype: ElectricInductance
        """
        return ElectricInductance(henries, ElectricInductanceUnits.Henry)

    
    @staticmethod
    def from_picohenries(picohenries: float):
        """
        Create a new instance of ElectricInductance from a value in picohenries.

        

        :param meters: The ElectricInductance value in picohenries.
        :type picohenries: float
        :return: A new instance of ElectricInductance.
        :rtype: ElectricInductance
        """
        return ElectricInductance(picohenries, ElectricInductanceUnits.Picohenry)

    
    @staticmethod
    def from_nanohenries(nanohenries: float):
        """
        Create a new instance of ElectricInductance from a value in nanohenries.

        

        :param meters: The ElectricInductance value in nanohenries.
        :type nanohenries: float
        :return: A new instance of ElectricInductance.
        :rtype: ElectricInductance
        """
        return ElectricInductance(nanohenries, ElectricInductanceUnits.Nanohenry)

    
    @staticmethod
    def from_microhenries(microhenries: float):
        """
        Create a new instance of ElectricInductance from a value in microhenries.

        

        :param meters: The ElectricInductance value in microhenries.
        :type microhenries: float
        :return: A new instance of ElectricInductance.
        :rtype: ElectricInductance
        """
        return ElectricInductance(microhenries, ElectricInductanceUnits.Microhenry)

    
    @staticmethod
    def from_millihenries(millihenries: float):
        """
        Create a new instance of ElectricInductance from a value in millihenries.

        

        :param meters: The ElectricInductance value in millihenries.
        :type millihenries: float
        :return: A new instance of ElectricInductance.
        :rtype: ElectricInductance
        """
        return ElectricInductance(millihenries, ElectricInductanceUnits.Millihenry)

    
    @property
    def henries(self) -> float:
        """
        
        """
        if self.__henries != None:
            return self.__henries
        self.__henries = self.__convert_from_base(ElectricInductanceUnits.Henry)
        return self.__henries

    
    @property
    def picohenries(self) -> float:
        """
        
        """
        if self.__picohenries != None:
            return self.__picohenries
        self.__picohenries = self.__convert_from_base(ElectricInductanceUnits.Picohenry)
        return self.__picohenries

    
    @property
    def nanohenries(self) -> float:
        """
        
        """
        if self.__nanohenries != None:
            return self.__nanohenries
        self.__nanohenries = self.__convert_from_base(ElectricInductanceUnits.Nanohenry)
        return self.__nanohenries

    
    @property
    def microhenries(self) -> float:
        """
        
        """
        if self.__microhenries != None:
            return self.__microhenries
        self.__microhenries = self.__convert_from_base(ElectricInductanceUnits.Microhenry)
        return self.__microhenries

    
    @property
    def millihenries(self) -> float:
        """
        
        """
        if self.__millihenries != None:
            return self.__millihenries
        self.__millihenries = self.__convert_from_base(ElectricInductanceUnits.Millihenry)
        return self.__millihenries

    
    def to_string(self, unit: ElectricInductanceUnits = ElectricInductanceUnits.Henry) -> string:
        """
        Format the ElectricInductance to string.
        Note! the default format for ElectricInductance is Henry.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == ElectricInductanceUnits.Henry:
            return f"""{self.henries} H"""
        
        if unit == ElectricInductanceUnits.Picohenry:
            return f"""{self.picohenries} """
        
        if unit == ElectricInductanceUnits.Nanohenry:
            return f"""{self.nanohenries} """
        
        if unit == ElectricInductanceUnits.Microhenry:
            return f"""{self.microhenries} """
        
        if unit == ElectricInductanceUnits.Millihenry:
            return f"""{self.millihenries} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: ElectricInductanceUnits = ElectricInductanceUnits.Henry) -> string:
        """
        Get ElectricInductance unit abbreviation.
        Note! the default abbreviation for ElectricInductance is Henry.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == ElectricInductanceUnits.Henry:
            return """H"""
        
        if unit_abbreviation == ElectricInductanceUnits.Picohenry:
            return """"""
        
        if unit_abbreviation == ElectricInductanceUnits.Nanohenry:
            return """"""
        
        if unit_abbreviation == ElectricInductanceUnits.Microhenry:
            return """"""
        
        if unit_abbreviation == ElectricInductanceUnits.Millihenry:
            return """"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, ElectricInductance):
            raise TypeError("unsupported operand type(s) for +: 'ElectricInductance' and '{}'".format(type(other).__name__))
        return ElectricInductance(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, ElectricInductance):
            raise TypeError("unsupported operand type(s) for *: 'ElectricInductance' and '{}'".format(type(other).__name__))
        return ElectricInductance(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, ElectricInductance):
            raise TypeError("unsupported operand type(s) for -: 'ElectricInductance' and '{}'".format(type(other).__name__))
        return ElectricInductance(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, ElectricInductance):
            raise TypeError("unsupported operand type(s) for /: 'ElectricInductance' and '{}'".format(type(other).__name__))
        return ElectricInductance(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, ElectricInductance):
            raise TypeError("unsupported operand type(s) for %: 'ElectricInductance' and '{}'".format(type(other).__name__))
        return ElectricInductance(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, ElectricInductance):
            raise TypeError("unsupported operand type(s) for **: 'ElectricInductance' and '{}'".format(type(other).__name__))
        return ElectricInductance(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, ElectricInductance):
            raise TypeError("unsupported operand type(s) for ==: 'ElectricInductance' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, ElectricInductance):
            raise TypeError("unsupported operand type(s) for <: 'ElectricInductance' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, ElectricInductance):
            raise TypeError("unsupported operand type(s) for >: 'ElectricInductance' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, ElectricInductance):
            raise TypeError("unsupported operand type(s) for <=: 'ElectricInductance' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, ElectricInductance):
            raise TypeError("unsupported operand type(s) for >=: 'ElectricInductance' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value
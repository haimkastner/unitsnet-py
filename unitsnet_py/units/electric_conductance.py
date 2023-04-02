from enum import Enum
import math
import string


class ElectricConductanceUnits(Enum):
        """
            ElectricConductanceUnits enumeration
        """
        
        Siemens = 'siemens'
        """
            
        """
        
        Nanosiemens = 'nanosiemens'
        """
            
        """
        
        Microsiemens = 'microsiemens'
        """
            
        """
        
        Millisiemens = 'millisiemens'
        """
            
        """
        
        Kilosiemens = 'kilosiemens'
        """
            
        """
        

class ElectricConductance:
    """
    The electrical conductance of an electrical conductor is a measure of the easeness to pass an electric current through that conductor.

    Args:
        value (float): The value.
        from_unit (ElectricConductanceUnits): The ElectricConductance unit to create from, The default unit is Siemens
    """
    def __init__(self, value: float, from_unit: ElectricConductanceUnits = ElectricConductanceUnits.Siemens):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__siemens = None
        
        self.__nanosiemens = None
        
        self.__microsiemens = None
        
        self.__millisiemens = None
        
        self.__kilosiemens = None
        

    def __convert_from_base(self, from_unit: ElectricConductanceUnits) -> float:
        value = self.__value
        
        if from_unit == ElectricConductanceUnits.Siemens:
            return (value)
        
        if from_unit == ElectricConductanceUnits.Nanosiemens:
            return ((value) / 1e-09)
        
        if from_unit == ElectricConductanceUnits.Microsiemens:
            return ((value) / 1e-06)
        
        if from_unit == ElectricConductanceUnits.Millisiemens:
            return ((value) / 0.001)
        
        if from_unit == ElectricConductanceUnits.Kilosiemens:
            return ((value) / 1000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: ElectricConductanceUnits) -> float:
        
        if to_unit == ElectricConductanceUnits.Siemens:
            return (value)
        
        if to_unit == ElectricConductanceUnits.Nanosiemens:
            return ((value) * 1e-09)
        
        if to_unit == ElectricConductanceUnits.Microsiemens:
            return ((value) * 1e-06)
        
        if to_unit == ElectricConductanceUnits.Millisiemens:
            return ((value) * 0.001)
        
        if to_unit == ElectricConductanceUnits.Kilosiemens:
            return ((value) * 1000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
    @staticmethod
    def from_siemens(siemens: float):
        """
        Create a new instance of ElectricConductance from a value in siemens.

        

        :param meters: The ElectricConductance value in siemens.
        :type siemens: float
        :return: A new instance of ElectricConductance.
        :rtype: ElectricConductance
        """
        return ElectricConductance(siemens, ElectricConductanceUnits.Siemens)

    
    @staticmethod
    def from_nanosiemens(nanosiemens: float):
        """
        Create a new instance of ElectricConductance from a value in nanosiemens.

        

        :param meters: The ElectricConductance value in nanosiemens.
        :type nanosiemens: float
        :return: A new instance of ElectricConductance.
        :rtype: ElectricConductance
        """
        return ElectricConductance(nanosiemens, ElectricConductanceUnits.Nanosiemens)

    
    @staticmethod
    def from_microsiemens(microsiemens: float):
        """
        Create a new instance of ElectricConductance from a value in microsiemens.

        

        :param meters: The ElectricConductance value in microsiemens.
        :type microsiemens: float
        :return: A new instance of ElectricConductance.
        :rtype: ElectricConductance
        """
        return ElectricConductance(microsiemens, ElectricConductanceUnits.Microsiemens)

    
    @staticmethod
    def from_millisiemens(millisiemens: float):
        """
        Create a new instance of ElectricConductance from a value in millisiemens.

        

        :param meters: The ElectricConductance value in millisiemens.
        :type millisiemens: float
        :return: A new instance of ElectricConductance.
        :rtype: ElectricConductance
        """
        return ElectricConductance(millisiemens, ElectricConductanceUnits.Millisiemens)

    
    @staticmethod
    def from_kilosiemens(kilosiemens: float):
        """
        Create a new instance of ElectricConductance from a value in kilosiemens.

        

        :param meters: The ElectricConductance value in kilosiemens.
        :type kilosiemens: float
        :return: A new instance of ElectricConductance.
        :rtype: ElectricConductance
        """
        return ElectricConductance(kilosiemens, ElectricConductanceUnits.Kilosiemens)

    
    @property
    def siemens(self) -> float:
        """
        
        """
        if self.__siemens != None:
            return self.__siemens
        self.__siemens = self.__convert_from_base(ElectricConductanceUnits.Siemens)
        return self.__siemens

    
    @property
    def nanosiemens(self) -> float:
        """
        
        """
        if self.__nanosiemens != None:
            return self.__nanosiemens
        self.__nanosiemens = self.__convert_from_base(ElectricConductanceUnits.Nanosiemens)
        return self.__nanosiemens

    
    @property
    def microsiemens(self) -> float:
        """
        
        """
        if self.__microsiemens != None:
            return self.__microsiemens
        self.__microsiemens = self.__convert_from_base(ElectricConductanceUnits.Microsiemens)
        return self.__microsiemens

    
    @property
    def millisiemens(self) -> float:
        """
        
        """
        if self.__millisiemens != None:
            return self.__millisiemens
        self.__millisiemens = self.__convert_from_base(ElectricConductanceUnits.Millisiemens)
        return self.__millisiemens

    
    @property
    def kilosiemens(self) -> float:
        """
        
        """
        if self.__kilosiemens != None:
            return self.__kilosiemens
        self.__kilosiemens = self.__convert_from_base(ElectricConductanceUnits.Kilosiemens)
        return self.__kilosiemens

    
    def to_string(self, unit: ElectricConductanceUnits = ElectricConductanceUnits.Siemens) -> string:
        """
        Format the ElectricConductance to string.
        Note! the default format for ElectricConductance is Siemens.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == ElectricConductanceUnits.Siemens:
            return f"""{self.siemens} S"""
        
        if unit == ElectricConductanceUnits.Nanosiemens:
            return f"""{self.nanosiemens} """
        
        if unit == ElectricConductanceUnits.Microsiemens:
            return f"""{self.microsiemens} """
        
        if unit == ElectricConductanceUnits.Millisiemens:
            return f"""{self.millisiemens} """
        
        if unit == ElectricConductanceUnits.Kilosiemens:
            return f"""{self.kilosiemens} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: ElectricConductanceUnits = ElectricConductanceUnits.Siemens) -> string:
        """
        Get ElectricConductance unit abbreviation.
        Note! the default abbreviation for ElectricConductance is Siemens.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == ElectricConductanceUnits.Siemens:
            return """S"""
        
        if unit_abbreviation == ElectricConductanceUnits.Nanosiemens:
            return """"""
        
        if unit_abbreviation == ElectricConductanceUnits.Microsiemens:
            return """"""
        
        if unit_abbreviation == ElectricConductanceUnits.Millisiemens:
            return """"""
        
        if unit_abbreviation == ElectricConductanceUnits.Kilosiemens:
            return """"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, ElectricConductance):
            raise TypeError("unsupported operand type(s) for +: 'ElectricConductance' and '{}'".format(type(other).__name__))
        return ElectricConductance(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, ElectricConductance):
            raise TypeError("unsupported operand type(s) for *: 'ElectricConductance' and '{}'".format(type(other).__name__))
        return ElectricConductance(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, ElectricConductance):
            raise TypeError("unsupported operand type(s) for -: 'ElectricConductance' and '{}'".format(type(other).__name__))
        return ElectricConductance(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, ElectricConductance):
            raise TypeError("unsupported operand type(s) for /: 'ElectricConductance' and '{}'".format(type(other).__name__))
        return ElectricConductance(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, ElectricConductance):
            raise TypeError("unsupported operand type(s) for %: 'ElectricConductance' and '{}'".format(type(other).__name__))
        return ElectricConductance(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, ElectricConductance):
            raise TypeError("unsupported operand type(s) for **: 'ElectricConductance' and '{}'".format(type(other).__name__))
        return ElectricConductance(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, ElectricConductance):
            raise TypeError("unsupported operand type(s) for ==: 'ElectricConductance' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, ElectricConductance):
            raise TypeError("unsupported operand type(s) for <: 'ElectricConductance' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, ElectricConductance):
            raise TypeError("unsupported operand type(s) for >: 'ElectricConductance' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, ElectricConductance):
            raise TypeError("unsupported operand type(s) for <=: 'ElectricConductance' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, ElectricConductance):
            raise TypeError("unsupported operand type(s) for >=: 'ElectricConductance' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value
from enum import Enum
import math
import string


class CapacitanceUnits(Enum):
        """
            CapacitanceUnits enumeration
        """
        
        Farad = 'farad'
        """
            
        """
        
        Picofarad = 'picofarad'
        """
            
        """
        
        Nanofarad = 'nanofarad'
        """
            
        """
        
        Microfarad = 'microfarad'
        """
            
        """
        
        Millifarad = 'millifarad'
        """
            
        """
        
        Kilofarad = 'kilofarad'
        """
            
        """
        
        Megafarad = 'megafarad'
        """
            
        """
        

class Capacitance:
    """
    Capacitance is the ability of a body to store an electric charge.

    Args:
        value (float): The value.
        from_unit (CapacitanceUnits): The Capacitance unit to create from, The default unit is Farad
    """
    def __init__(self, value: float, from_unit: CapacitanceUnits = CapacitanceUnits.Farad):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__farads = None
        
        self.__picofarads = None
        
        self.__nanofarads = None
        
        self.__microfarads = None
        
        self.__millifarads = None
        
        self.__kilofarads = None
        
        self.__megafarads = None
        

    def __convert_from_base(self, from_unit: CapacitanceUnits) -> float:
        value = self.__value
        
        if from_unit == CapacitanceUnits.Farad:
            return (value)
        
        if from_unit == CapacitanceUnits.Picofarad:
            return ((value) / 1e-12)
        
        if from_unit == CapacitanceUnits.Nanofarad:
            return ((value) / 1e-09)
        
        if from_unit == CapacitanceUnits.Microfarad:
            return ((value) / 1e-06)
        
        if from_unit == CapacitanceUnits.Millifarad:
            return ((value) / 0.001)
        
        if from_unit == CapacitanceUnits.Kilofarad:
            return ((value) / 1000.0)
        
        if from_unit == CapacitanceUnits.Megafarad:
            return ((value) / 1000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: CapacitanceUnits) -> float:
        
        if to_unit == CapacitanceUnits.Farad:
            return (value)
        
        if to_unit == CapacitanceUnits.Picofarad:
            return ((value) * 1e-12)
        
        if to_unit == CapacitanceUnits.Nanofarad:
            return ((value) * 1e-09)
        
        if to_unit == CapacitanceUnits.Microfarad:
            return ((value) * 1e-06)
        
        if to_unit == CapacitanceUnits.Millifarad:
            return ((value) * 0.001)
        
        if to_unit == CapacitanceUnits.Kilofarad:
            return ((value) * 1000.0)
        
        if to_unit == CapacitanceUnits.Megafarad:
            return ((value) * 1000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
    @staticmethod
    def from_farads(farads: float):
        """
        Create a new instance of Capacitance from a value in farads.

        

        :param meters: The Capacitance value in farads.
        :type farads: float
        :return: A new instance of Capacitance.
        :rtype: Capacitance
        """
        return Capacitance(farads, CapacitanceUnits.Farad)

    
    @staticmethod
    def from_picofarads(picofarads: float):
        """
        Create a new instance of Capacitance from a value in picofarads.

        

        :param meters: The Capacitance value in picofarads.
        :type picofarads: float
        :return: A new instance of Capacitance.
        :rtype: Capacitance
        """
        return Capacitance(picofarads, CapacitanceUnits.Picofarad)

    
    @staticmethod
    def from_nanofarads(nanofarads: float):
        """
        Create a new instance of Capacitance from a value in nanofarads.

        

        :param meters: The Capacitance value in nanofarads.
        :type nanofarads: float
        :return: A new instance of Capacitance.
        :rtype: Capacitance
        """
        return Capacitance(nanofarads, CapacitanceUnits.Nanofarad)

    
    @staticmethod
    def from_microfarads(microfarads: float):
        """
        Create a new instance of Capacitance from a value in microfarads.

        

        :param meters: The Capacitance value in microfarads.
        :type microfarads: float
        :return: A new instance of Capacitance.
        :rtype: Capacitance
        """
        return Capacitance(microfarads, CapacitanceUnits.Microfarad)

    
    @staticmethod
    def from_millifarads(millifarads: float):
        """
        Create a new instance of Capacitance from a value in millifarads.

        

        :param meters: The Capacitance value in millifarads.
        :type millifarads: float
        :return: A new instance of Capacitance.
        :rtype: Capacitance
        """
        return Capacitance(millifarads, CapacitanceUnits.Millifarad)

    
    @staticmethod
    def from_kilofarads(kilofarads: float):
        """
        Create a new instance of Capacitance from a value in kilofarads.

        

        :param meters: The Capacitance value in kilofarads.
        :type kilofarads: float
        :return: A new instance of Capacitance.
        :rtype: Capacitance
        """
        return Capacitance(kilofarads, CapacitanceUnits.Kilofarad)

    
    @staticmethod
    def from_megafarads(megafarads: float):
        """
        Create a new instance of Capacitance from a value in megafarads.

        

        :param meters: The Capacitance value in megafarads.
        :type megafarads: float
        :return: A new instance of Capacitance.
        :rtype: Capacitance
        """
        return Capacitance(megafarads, CapacitanceUnits.Megafarad)

    
    @property
    def farads(self) -> float:
        """
        
        """
        if self.__farads != None:
            return self.__farads
        self.__farads = self.__convert_from_base(CapacitanceUnits.Farad)
        return self.__farads

    
    @property
    def picofarads(self) -> float:
        """
        
        """
        if self.__picofarads != None:
            return self.__picofarads
        self.__picofarads = self.__convert_from_base(CapacitanceUnits.Picofarad)
        return self.__picofarads

    
    @property
    def nanofarads(self) -> float:
        """
        
        """
        if self.__nanofarads != None:
            return self.__nanofarads
        self.__nanofarads = self.__convert_from_base(CapacitanceUnits.Nanofarad)
        return self.__nanofarads

    
    @property
    def microfarads(self) -> float:
        """
        
        """
        if self.__microfarads != None:
            return self.__microfarads
        self.__microfarads = self.__convert_from_base(CapacitanceUnits.Microfarad)
        return self.__microfarads

    
    @property
    def millifarads(self) -> float:
        """
        
        """
        if self.__millifarads != None:
            return self.__millifarads
        self.__millifarads = self.__convert_from_base(CapacitanceUnits.Millifarad)
        return self.__millifarads

    
    @property
    def kilofarads(self) -> float:
        """
        
        """
        if self.__kilofarads != None:
            return self.__kilofarads
        self.__kilofarads = self.__convert_from_base(CapacitanceUnits.Kilofarad)
        return self.__kilofarads

    
    @property
    def megafarads(self) -> float:
        """
        
        """
        if self.__megafarads != None:
            return self.__megafarads
        self.__megafarads = self.__convert_from_base(CapacitanceUnits.Megafarad)
        return self.__megafarads

    
    def to_string(self, unit: CapacitanceUnits = CapacitanceUnits.Farad) -> string:
        """
        Format the Capacitance to string.
        Note! the default format for Capacitance is Farad.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == CapacitanceUnits.Farad:
            return f"""{self.farads} F"""
        
        if unit == CapacitanceUnits.Picofarad:
            return f"""{self.picofarads} """
        
        if unit == CapacitanceUnits.Nanofarad:
            return f"""{self.nanofarads} """
        
        if unit == CapacitanceUnits.Microfarad:
            return f"""{self.microfarads} """
        
        if unit == CapacitanceUnits.Millifarad:
            return f"""{self.millifarads} """
        
        if unit == CapacitanceUnits.Kilofarad:
            return f"""{self.kilofarads} """
        
        if unit == CapacitanceUnits.Megafarad:
            return f"""{self.megafarads} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: CapacitanceUnits = CapacitanceUnits.Farad) -> string:
        """
        Get Capacitance unit abbreviation.
        Note! the default abbreviation for Capacitance is Farad.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == CapacitanceUnits.Farad:
            return """F"""
        
        if unit_abbreviation == CapacitanceUnits.Picofarad:
            return """"""
        
        if unit_abbreviation == CapacitanceUnits.Nanofarad:
            return """"""
        
        if unit_abbreviation == CapacitanceUnits.Microfarad:
            return """"""
        
        if unit_abbreviation == CapacitanceUnits.Millifarad:
            return """"""
        
        if unit_abbreviation == CapacitanceUnits.Kilofarad:
            return """"""
        
        if unit_abbreviation == CapacitanceUnits.Megafarad:
            return """"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, Capacitance):
            raise TypeError("unsupported operand type(s) for +: 'Capacitance' and '{}'".format(type(other).__name__))
        return Capacitance(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, Capacitance):
            raise TypeError("unsupported operand type(s) for *: 'Capacitance' and '{}'".format(type(other).__name__))
        return Capacitance(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, Capacitance):
            raise TypeError("unsupported operand type(s) for -: 'Capacitance' and '{}'".format(type(other).__name__))
        return Capacitance(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, Capacitance):
            raise TypeError("unsupported operand type(s) for /: 'Capacitance' and '{}'".format(type(other).__name__))
        return Capacitance(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, Capacitance):
            raise TypeError("unsupported operand type(s) for %: 'Capacitance' and '{}'".format(type(other).__name__))
        return Capacitance(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, Capacitance):
            raise TypeError("unsupported operand type(s) for **: 'Capacitance' and '{}'".format(type(other).__name__))
        return Capacitance(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, Capacitance):
            raise TypeError("unsupported operand type(s) for ==: 'Capacitance' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, Capacitance):
            raise TypeError("unsupported operand type(s) for <: 'Capacitance' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, Capacitance):
            raise TypeError("unsupported operand type(s) for >: 'Capacitance' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, Capacitance):
            raise TypeError("unsupported operand type(s) for <=: 'Capacitance' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, Capacitance):
            raise TypeError("unsupported operand type(s) for >=: 'Capacitance' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value
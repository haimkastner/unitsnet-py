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
        
        PicoHenry = 'pico_henry'
        """
            
        """
        
        NanoHenry = 'nano_henry'
        """
            
        """
        
        MicroHenry = 'micro_henry'
        """
            
        """
        
        MilliHenry = 'milli_henry'
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
        
        self.__pico_henries = None
        
        self.__nano_henries = None
        
        self.__micro_henries = None
        
        self.__milli_henries = None
        

    def __convert_from_base(self, from_unit: ElectricInductanceUnits) -> float:
        value = self.__value
        
        if from_unit == ElectricInductanceUnits.Henry:
            return (value)
        
        if from_unit == ElectricInductanceUnits.PicoHenry:
            return ((value) / 1e-12)
        
        if from_unit == ElectricInductanceUnits.NanoHenry:
            return ((value) / 1e-09)
        
        if from_unit == ElectricInductanceUnits.MicroHenry:
            return ((value) / 1e-06)
        
        if from_unit == ElectricInductanceUnits.MilliHenry:
            return ((value) / 0.001)
        
        return None


    def __convert_to_base(self, value: float, to_unit: ElectricInductanceUnits) -> float:
        
        if to_unit == ElectricInductanceUnits.Henry:
            return (value)
        
        if to_unit == ElectricInductanceUnits.PicoHenry:
            return ((value) * 1e-12)
        
        if to_unit == ElectricInductanceUnits.NanoHenry:
            return ((value) * 1e-09)
        
        if to_unit == ElectricInductanceUnits.MicroHenry:
            return ((value) * 1e-06)
        
        if to_unit == ElectricInductanceUnits.MilliHenry:
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
    def from_pico_henries(pico_henries: float):
        """
        Create a new instance of ElectricInductance from a value in pico_henries.

        

        :param meters: The ElectricInductance value in pico_henries.
        :type pico_henries: float
        :return: A new instance of ElectricInductance.
        :rtype: ElectricInductance
        """
        return ElectricInductance(pico_henries, ElectricInductanceUnits.PicoHenry)

    
    @staticmethod
    def from_nano_henries(nano_henries: float):
        """
        Create a new instance of ElectricInductance from a value in nano_henries.

        

        :param meters: The ElectricInductance value in nano_henries.
        :type nano_henries: float
        :return: A new instance of ElectricInductance.
        :rtype: ElectricInductance
        """
        return ElectricInductance(nano_henries, ElectricInductanceUnits.NanoHenry)

    
    @staticmethod
    def from_micro_henries(micro_henries: float):
        """
        Create a new instance of ElectricInductance from a value in micro_henries.

        

        :param meters: The ElectricInductance value in micro_henries.
        :type micro_henries: float
        :return: A new instance of ElectricInductance.
        :rtype: ElectricInductance
        """
        return ElectricInductance(micro_henries, ElectricInductanceUnits.MicroHenry)

    
    @staticmethod
    def from_milli_henries(milli_henries: float):
        """
        Create a new instance of ElectricInductance from a value in milli_henries.

        

        :param meters: The ElectricInductance value in milli_henries.
        :type milli_henries: float
        :return: A new instance of ElectricInductance.
        :rtype: ElectricInductance
        """
        return ElectricInductance(milli_henries, ElectricInductanceUnits.MilliHenry)

    
    @property
    def henries(self) -> float:
        """
        
        """
        if self.__henries != None:
            return self.__henries
        self.__henries = self.__convert_from_base(ElectricInductanceUnits.Henry)
        return self.__henries

    
    @property
    def pico_henries(self) -> float:
        """
        
        """
        if self.__pico_henries != None:
            return self.__pico_henries
        self.__pico_henries = self.__convert_from_base(ElectricInductanceUnits.PicoHenry)
        return self.__pico_henries

    
    @property
    def nano_henries(self) -> float:
        """
        
        """
        if self.__nano_henries != None:
            return self.__nano_henries
        self.__nano_henries = self.__convert_from_base(ElectricInductanceUnits.NanoHenry)
        return self.__nano_henries

    
    @property
    def micro_henries(self) -> float:
        """
        
        """
        if self.__micro_henries != None:
            return self.__micro_henries
        self.__micro_henries = self.__convert_from_base(ElectricInductanceUnits.MicroHenry)
        return self.__micro_henries

    
    @property
    def milli_henries(self) -> float:
        """
        
        """
        if self.__milli_henries != None:
            return self.__milli_henries
        self.__milli_henries = self.__convert_from_base(ElectricInductanceUnits.MilliHenry)
        return self.__milli_henries

    
    def to_string(self, unit: ElectricInductanceUnits = ElectricInductanceUnits.Henry) -> string:
        """
        Format the ElectricInductance to string.
        Note! the default format for ElectricInductance is Henry.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == ElectricInductanceUnits.Henry:
            return f"""{self.henries} H"""
        
        if unit == ElectricInductanceUnits.PicoHenry:
            return f"""{self.pico_henries} """
        
        if unit == ElectricInductanceUnits.NanoHenry:
            return f"""{self.nano_henries} """
        
        if unit == ElectricInductanceUnits.MicroHenry:
            return f"""{self.micro_henries} """
        
        if unit == ElectricInductanceUnits.MilliHenry:
            return f"""{self.milli_henries} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: ElectricInductanceUnits = ElectricInductanceUnits.Henry) -> string:
        """
        Get ElectricInductance unit abbreviation.
        Note! the default abbreviation for ElectricInductance is Henry.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == ElectricInductanceUnits.Henry:
            return """H"""
        
        if unit_abbreviation == ElectricInductanceUnits.PicoHenry:
            return """"""
        
        if unit_abbreviation == ElectricInductanceUnits.NanoHenry:
            return """"""
        
        if unit_abbreviation == ElectricInductanceUnits.MicroHenry:
            return """"""
        
        if unit_abbreviation == ElectricInductanceUnits.MilliHenry:
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
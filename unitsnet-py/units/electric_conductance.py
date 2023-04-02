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
        
        NanoSiemens = 'nano_siemens'
        """
            
        """
        
        MicroSiemens = 'micro_siemens'
        """
            
        """
        
        MilliSiemens = 'milli_siemens'
        """
            
        """
        
        KiloSiemens = 'kilo_siemens'
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
        
        self.__nano_siemens = None
        
        self.__micro_siemens = None
        
        self.__milli_siemens = None
        
        self.__kilo_siemens = None
        

    def __convert_from_base(self, from_unit: ElectricConductanceUnits) -> float:
        value = self.__value
        
        if from_unit == ElectricConductanceUnits.Siemens:
            return (value)
        
        if from_unit == ElectricConductanceUnits.NanoSiemens:
            return ((value) / 1e-09)
        
        if from_unit == ElectricConductanceUnits.MicroSiemens:
            return ((value) / 1e-06)
        
        if from_unit == ElectricConductanceUnits.MilliSiemens:
            return ((value) / 0.001)
        
        if from_unit == ElectricConductanceUnits.KiloSiemens:
            return ((value) / 1000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: ElectricConductanceUnits) -> float:
        
        if to_unit == ElectricConductanceUnits.Siemens:
            return (value)
        
        if to_unit == ElectricConductanceUnits.NanoSiemens:
            return ((value) * 1e-09)
        
        if to_unit == ElectricConductanceUnits.MicroSiemens:
            return ((value) * 1e-06)
        
        if to_unit == ElectricConductanceUnits.MilliSiemens:
            return ((value) * 0.001)
        
        if to_unit == ElectricConductanceUnits.KiloSiemens:
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
    def from_nano_siemens(nano_siemens: float):
        """
        Create a new instance of ElectricConductance from a value in nano_siemens.

        

        :param meters: The ElectricConductance value in nano_siemens.
        :type nano_siemens: float
        :return: A new instance of ElectricConductance.
        :rtype: ElectricConductance
        """
        return ElectricConductance(nano_siemens, ElectricConductanceUnits.NanoSiemens)

    
    @staticmethod
    def from_micro_siemens(micro_siemens: float):
        """
        Create a new instance of ElectricConductance from a value in micro_siemens.

        

        :param meters: The ElectricConductance value in micro_siemens.
        :type micro_siemens: float
        :return: A new instance of ElectricConductance.
        :rtype: ElectricConductance
        """
        return ElectricConductance(micro_siemens, ElectricConductanceUnits.MicroSiemens)

    
    @staticmethod
    def from_milli_siemens(milli_siemens: float):
        """
        Create a new instance of ElectricConductance from a value in milli_siemens.

        

        :param meters: The ElectricConductance value in milli_siemens.
        :type milli_siemens: float
        :return: A new instance of ElectricConductance.
        :rtype: ElectricConductance
        """
        return ElectricConductance(milli_siemens, ElectricConductanceUnits.MilliSiemens)

    
    @staticmethod
    def from_kilo_siemens(kilo_siemens: float):
        """
        Create a new instance of ElectricConductance from a value in kilo_siemens.

        

        :param meters: The ElectricConductance value in kilo_siemens.
        :type kilo_siemens: float
        :return: A new instance of ElectricConductance.
        :rtype: ElectricConductance
        """
        return ElectricConductance(kilo_siemens, ElectricConductanceUnits.KiloSiemens)

    
    @property
    def siemens(self) -> float:
        """
        
        """
        if self.__siemens != None:
            return self.__siemens
        self.__siemens = self.__convert_from_base(ElectricConductanceUnits.Siemens)
        return self.__siemens

    
    @property
    def nano_siemens(self) -> float:
        """
        
        """
        if self.__nano_siemens != None:
            return self.__nano_siemens
        self.__nano_siemens = self.__convert_from_base(ElectricConductanceUnits.NanoSiemens)
        return self.__nano_siemens

    
    @property
    def micro_siemens(self) -> float:
        """
        
        """
        if self.__micro_siemens != None:
            return self.__micro_siemens
        self.__micro_siemens = self.__convert_from_base(ElectricConductanceUnits.MicroSiemens)
        return self.__micro_siemens

    
    @property
    def milli_siemens(self) -> float:
        """
        
        """
        if self.__milli_siemens != None:
            return self.__milli_siemens
        self.__milli_siemens = self.__convert_from_base(ElectricConductanceUnits.MilliSiemens)
        return self.__milli_siemens

    
    @property
    def kilo_siemens(self) -> float:
        """
        
        """
        if self.__kilo_siemens != None:
            return self.__kilo_siemens
        self.__kilo_siemens = self.__convert_from_base(ElectricConductanceUnits.KiloSiemens)
        return self.__kilo_siemens

    
    def to_string(self, unit: ElectricConductanceUnits = ElectricConductanceUnits.Siemens) -> string:
        """
        Format the ElectricConductance to string.
        Note! the default format for ElectricConductance is Siemens.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == ElectricConductanceUnits.Siemens:
            return f"""{self.siemens} S"""
        
        if unit == ElectricConductanceUnits.NanoSiemens:
            return f"""{self.nano_siemens} """
        
        if unit == ElectricConductanceUnits.MicroSiemens:
            return f"""{self.micro_siemens} """
        
        if unit == ElectricConductanceUnits.MilliSiemens:
            return f"""{self.milli_siemens} """
        
        if unit == ElectricConductanceUnits.KiloSiemens:
            return f"""{self.kilo_siemens} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: ElectricConductanceUnits = ElectricConductanceUnits.Siemens) -> string:
        """
        Get ElectricConductance unit abbreviation.
        Note! the default abbreviation for ElectricConductance is Siemens.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == ElectricConductanceUnits.Siemens:
            return """S"""
        
        if unit_abbreviation == ElectricConductanceUnits.NanoSiemens:
            return """"""
        
        if unit_abbreviation == ElectricConductanceUnits.MicroSiemens:
            return """"""
        
        if unit_abbreviation == ElectricConductanceUnits.MilliSiemens:
            return """"""
        
        if unit_abbreviation == ElectricConductanceUnits.KiloSiemens:
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
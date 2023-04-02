from enum import Enum
import math
import string


class ElectricAdmittanceUnits(Enum):
        """
            ElectricAdmittanceUnits enumeration
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
        

class ElectricAdmittance:
    """
    Electric admittance is a measure of how easily a circuit or device will allow a current to flow. It is defined as the inverse of impedance. The SI unit of admittance is the siemens (symbol S).

    Args:
        value (float): The value.
        from_unit (ElectricAdmittanceUnits): The ElectricAdmittance unit to create from, The default unit is Siemens
    """
    def __init__(self, value: float, from_unit: ElectricAdmittanceUnits = ElectricAdmittanceUnits.Siemens):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__siemens = None
        
        self.__nano_siemens = None
        
        self.__micro_siemens = None
        
        self.__milli_siemens = None
        

    def __convert_from_base(self, from_unit: ElectricAdmittanceUnits) -> float:
        value = self.__value
        
        if from_unit == ElectricAdmittanceUnits.Siemens:
            return (value)
        
        if from_unit == ElectricAdmittanceUnits.NanoSiemens:
            return ((value) / 1e-09)
        
        if from_unit == ElectricAdmittanceUnits.MicroSiemens:
            return ((value) / 1e-06)
        
        if from_unit == ElectricAdmittanceUnits.MilliSiemens:
            return ((value) / 0.001)
        
        return None


    def __convert_to_base(self, value: float, to_unit: ElectricAdmittanceUnits) -> float:
        
        if to_unit == ElectricAdmittanceUnits.Siemens:
            return (value)
        
        if to_unit == ElectricAdmittanceUnits.NanoSiemens:
            return ((value) * 1e-09)
        
        if to_unit == ElectricAdmittanceUnits.MicroSiemens:
            return ((value) * 1e-06)
        
        if to_unit == ElectricAdmittanceUnits.MilliSiemens:
            return ((value) * 0.001)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
    @staticmethod
    def from_siemens(siemens: float):
        """
        Create a new instance of ElectricAdmittance from a value in siemens.

        

        :param meters: The ElectricAdmittance value in siemens.
        :type siemens: float
        :return: A new instance of ElectricAdmittance.
        :rtype: ElectricAdmittance
        """
        return ElectricAdmittance(siemens, ElectricAdmittanceUnits.Siemens)

    
    @staticmethod
    def from_nano_siemens(nano_siemens: float):
        """
        Create a new instance of ElectricAdmittance from a value in nano_siemens.

        

        :param meters: The ElectricAdmittance value in nano_siemens.
        :type nano_siemens: float
        :return: A new instance of ElectricAdmittance.
        :rtype: ElectricAdmittance
        """
        return ElectricAdmittance(nano_siemens, ElectricAdmittanceUnits.NanoSiemens)

    
    @staticmethod
    def from_micro_siemens(micro_siemens: float):
        """
        Create a new instance of ElectricAdmittance from a value in micro_siemens.

        

        :param meters: The ElectricAdmittance value in micro_siemens.
        :type micro_siemens: float
        :return: A new instance of ElectricAdmittance.
        :rtype: ElectricAdmittance
        """
        return ElectricAdmittance(micro_siemens, ElectricAdmittanceUnits.MicroSiemens)

    
    @staticmethod
    def from_milli_siemens(milli_siemens: float):
        """
        Create a new instance of ElectricAdmittance from a value in milli_siemens.

        

        :param meters: The ElectricAdmittance value in milli_siemens.
        :type milli_siemens: float
        :return: A new instance of ElectricAdmittance.
        :rtype: ElectricAdmittance
        """
        return ElectricAdmittance(milli_siemens, ElectricAdmittanceUnits.MilliSiemens)

    
    @property
    def siemens(self) -> float:
        """
        
        """
        if self.__siemens != None:
            return self.__siemens
        self.__siemens = self.__convert_from_base(ElectricAdmittanceUnits.Siemens)
        return self.__siemens

    
    @property
    def nano_siemens(self) -> float:
        """
        
        """
        if self.__nano_siemens != None:
            return self.__nano_siemens
        self.__nano_siemens = self.__convert_from_base(ElectricAdmittanceUnits.NanoSiemens)
        return self.__nano_siemens

    
    @property
    def micro_siemens(self) -> float:
        """
        
        """
        if self.__micro_siemens != None:
            return self.__micro_siemens
        self.__micro_siemens = self.__convert_from_base(ElectricAdmittanceUnits.MicroSiemens)
        return self.__micro_siemens

    
    @property
    def milli_siemens(self) -> float:
        """
        
        """
        if self.__milli_siemens != None:
            return self.__milli_siemens
        self.__milli_siemens = self.__convert_from_base(ElectricAdmittanceUnits.MilliSiemens)
        return self.__milli_siemens

    
    def to_string(self, unit: ElectricAdmittanceUnits = ElectricAdmittanceUnits.Siemens) -> string:
        """
        Format the ElectricAdmittance to string.
        Note! the default format for ElectricAdmittance is Siemens.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == ElectricAdmittanceUnits.Siemens:
            return f"""{self.siemens} S"""
        
        if unit == ElectricAdmittanceUnits.NanoSiemens:
            return f"""{self.nano_siemens} """
        
        if unit == ElectricAdmittanceUnits.MicroSiemens:
            return f"""{self.micro_siemens} """
        
        if unit == ElectricAdmittanceUnits.MilliSiemens:
            return f"""{self.milli_siemens} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: ElectricAdmittanceUnits = ElectricAdmittanceUnits.Siemens) -> string:
        """
        Get ElectricAdmittance unit abbreviation.
        Note! the default abbreviation for ElectricAdmittance is Siemens.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == ElectricAdmittanceUnits.Siemens:
            return """S"""
        
        if unit_abbreviation == ElectricAdmittanceUnits.NanoSiemens:
            return """"""
        
        if unit_abbreviation == ElectricAdmittanceUnits.MicroSiemens:
            return """"""
        
        if unit_abbreviation == ElectricAdmittanceUnits.MilliSiemens:
            return """"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, ElectricAdmittance):
            raise TypeError("unsupported operand type(s) for +: 'ElectricAdmittance' and '{}'".format(type(other).__name__))
        return ElectricAdmittance(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, ElectricAdmittance):
            raise TypeError("unsupported operand type(s) for *: 'ElectricAdmittance' and '{}'".format(type(other).__name__))
        return ElectricAdmittance(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, ElectricAdmittance):
            raise TypeError("unsupported operand type(s) for -: 'ElectricAdmittance' and '{}'".format(type(other).__name__))
        return ElectricAdmittance(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, ElectricAdmittance):
            raise TypeError("unsupported operand type(s) for /: 'ElectricAdmittance' and '{}'".format(type(other).__name__))
        return ElectricAdmittance(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, ElectricAdmittance):
            raise TypeError("unsupported operand type(s) for %: 'ElectricAdmittance' and '{}'".format(type(other).__name__))
        return ElectricAdmittance(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, ElectricAdmittance):
            raise TypeError("unsupported operand type(s) for **: 'ElectricAdmittance' and '{}'".format(type(other).__name__))
        return ElectricAdmittance(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, ElectricAdmittance):
            raise TypeError("unsupported operand type(s) for ==: 'ElectricAdmittance' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, ElectricAdmittance):
            raise TypeError("unsupported operand type(s) for <: 'ElectricAdmittance' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, ElectricAdmittance):
            raise TypeError("unsupported operand type(s) for >: 'ElectricAdmittance' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, ElectricAdmittance):
            raise TypeError("unsupported operand type(s) for <=: 'ElectricAdmittance' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, ElectricAdmittance):
            raise TypeError("unsupported operand type(s) for >=: 'ElectricAdmittance' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value
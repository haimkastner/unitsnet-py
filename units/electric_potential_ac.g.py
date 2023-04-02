from enum import Enum
import math
import string


class ElectricPotentialAcUnits(Enum):
        """
            ElectricPotentialAcUnits enumeration
        """
        
        VoltAc = 'volt_ac'
        """
            
        """
        
        MicroVoltAc = 'micro_volt_ac'
        """
            
        """
        
        MilliVoltAc = 'milli_volt_ac'
        """
            
        """
        
        KiloVoltAc = 'kilo_volt_ac'
        """
            
        """
        
        MegaVoltAc = 'mega_volt_ac'
        """
            
        """
        
    
class ElectricPotentialAc:
    """
    The Electric Potential of a system known to use Alternating Current.

    Args:
        value (float): The value.
        from_unit (ElectricPotentialAcUnits): The ElectricPotentialAc unit to create from, The default unit is VoltAc
    """
    def __init__(self, value: float, from_unit: ElectricPotentialAcUnits = ElectricPotentialAcUnits.VoltAc):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__volts_ac = None
        
        self.__micro_volts_ac = None
        
        self.__milli_volts_ac = None
        
        self.__kilo_volts_ac = None
        
        self.__mega_volts_ac = None
        

    def __convert_from_base(self, from_unit: ElectricPotentialAcUnits) -> float:
        value = self.__value
        
        if from_unit == ElectricPotentialAcUnits.VoltAc:
            return (value)
        
        if from_unit == ElectricPotentialAcUnits.MicroVoltAc:
            return ((value) / 1e-06)
        
        if from_unit == ElectricPotentialAcUnits.MilliVoltAc:
            return ((value) / 0.001)
        
        if from_unit == ElectricPotentialAcUnits.KiloVoltAc:
            return ((value) / 1000.0)
        
        if from_unit == ElectricPotentialAcUnits.MegaVoltAc:
            return ((value) / 1000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: ElectricPotentialAcUnits) -> float:
        
        if to_unit == ElectricPotentialAcUnits.VoltAc:
            return (value)
        
        if to_unit == ElectricPotentialAcUnits.MicroVoltAc:
            return ((value) * 1e-06)
        
        if to_unit == ElectricPotentialAcUnits.MilliVoltAc:
            return ((value) * 0.001)
        
        if to_unit == ElectricPotentialAcUnits.KiloVoltAc:
            return ((value) * 1000.0)
        
        if to_unit == ElectricPotentialAcUnits.MegaVoltAc:
            return ((value) * 1000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
    @staticmethod
    def from_volts_ac(volts_ac: float):
        """
        Create a new instance of ElectricPotentialAc from a value in volts_ac.

        

        :param meters: The ElectricPotentialAc value in volts_ac.
        :type volts_ac: float
        :return: A new instance of ElectricPotentialAc.
        :rtype: ElectricPotentialAc
        """
        return ElectricPotentialAc(volts_ac, ElectricPotentialAcUnits.VoltAc)

    
    @staticmethod
    def from_micro_volts_ac(micro_volts_ac: float):
        """
        Create a new instance of ElectricPotentialAc from a value in micro_volts_ac.

        

        :param meters: The ElectricPotentialAc value in micro_volts_ac.
        :type micro_volts_ac: float
        :return: A new instance of ElectricPotentialAc.
        :rtype: ElectricPotentialAc
        """
        return ElectricPotentialAc(micro_volts_ac, ElectricPotentialAcUnits.MicroVoltAc)

    
    @staticmethod
    def from_milli_volts_ac(milli_volts_ac: float):
        """
        Create a new instance of ElectricPotentialAc from a value in milli_volts_ac.

        

        :param meters: The ElectricPotentialAc value in milli_volts_ac.
        :type milli_volts_ac: float
        :return: A new instance of ElectricPotentialAc.
        :rtype: ElectricPotentialAc
        """
        return ElectricPotentialAc(milli_volts_ac, ElectricPotentialAcUnits.MilliVoltAc)

    
    @staticmethod
    def from_kilo_volts_ac(kilo_volts_ac: float):
        """
        Create a new instance of ElectricPotentialAc from a value in kilo_volts_ac.

        

        :param meters: The ElectricPotentialAc value in kilo_volts_ac.
        :type kilo_volts_ac: float
        :return: A new instance of ElectricPotentialAc.
        :rtype: ElectricPotentialAc
        """
        return ElectricPotentialAc(kilo_volts_ac, ElectricPotentialAcUnits.KiloVoltAc)

    
    @staticmethod
    def from_mega_volts_ac(mega_volts_ac: float):
        """
        Create a new instance of ElectricPotentialAc from a value in mega_volts_ac.

        

        :param meters: The ElectricPotentialAc value in mega_volts_ac.
        :type mega_volts_ac: float
        :return: A new instance of ElectricPotentialAc.
        :rtype: ElectricPotentialAc
        """
        return ElectricPotentialAc(mega_volts_ac, ElectricPotentialAcUnits.MegaVoltAc)

    
    @property
    def volts_ac(self) -> float:
        """
        
        """
        if self.__volts_ac != None:
            return self.__volts_ac
        self.__volts_ac = self.__convert_from_base(ElectricPotentialAcUnits.VoltAc)
        return self.__volts_ac

    
    @property
    def micro_volts_ac(self) -> float:
        """
        
        """
        if self.__micro_volts_ac != None:
            return self.__micro_volts_ac
        self.__micro_volts_ac = self.__convert_from_base(ElectricPotentialAcUnits.MicroVoltAc)
        return self.__micro_volts_ac

    
    @property
    def milli_volts_ac(self) -> float:
        """
        
        """
        if self.__milli_volts_ac != None:
            return self.__milli_volts_ac
        self.__milli_volts_ac = self.__convert_from_base(ElectricPotentialAcUnits.MilliVoltAc)
        return self.__milli_volts_ac

    
    @property
    def kilo_volts_ac(self) -> float:
        """
        
        """
        if self.__kilo_volts_ac != None:
            return self.__kilo_volts_ac
        self.__kilo_volts_ac = self.__convert_from_base(ElectricPotentialAcUnits.KiloVoltAc)
        return self.__kilo_volts_ac

    
    @property
    def mega_volts_ac(self) -> float:
        """
        
        """
        if self.__mega_volts_ac != None:
            return self.__mega_volts_ac
        self.__mega_volts_ac = self.__convert_from_base(ElectricPotentialAcUnits.MegaVoltAc)
        return self.__mega_volts_ac

    
    def to_string(self, unit: ElectricPotentialAcUnits = ElectricPotentialAcUnits.VoltAc) -> string:
        """
        Format the ElectricPotentialAc to string.
        Note! the default format for ElectricPotentialAc is VoltAc.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == ElectricPotentialAcUnits.VoltAc:
            return f"""{self.volts_ac} Vac"""
        
        if unit == ElectricPotentialAcUnits.MicroVoltAc:
            return f"""{self.micro_volts_ac} """
        
        if unit == ElectricPotentialAcUnits.MilliVoltAc:
            return f"""{self.milli_volts_ac} """
        
        if unit == ElectricPotentialAcUnits.KiloVoltAc:
            return f"""{self.kilo_volts_ac} """
        
        if unit == ElectricPotentialAcUnits.MegaVoltAc:
            return f"""{self.mega_volts_ac} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: ElectricPotentialAcUnits = ElectricPotentialAcUnits.VoltAc) -> string:
        """
        Get ElectricPotentialAc unit abbreviation.
        Note! the default abbreviation for ElectricPotentialAc is VoltAc.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == ElectricPotentialAcUnits.VoltAc:
            return """Vac"""
        
        if unit_abbreviation == ElectricPotentialAcUnits.MicroVoltAc:
            return """"""
        
        if unit_abbreviation == ElectricPotentialAcUnits.MilliVoltAc:
            return """"""
        
        if unit_abbreviation == ElectricPotentialAcUnits.KiloVoltAc:
            return """"""
        
        if unit_abbreviation == ElectricPotentialAcUnits.MegaVoltAc:
            return """"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, ElectricPotentialAc):
            raise TypeError("unsupported operand type(s) for +: 'ElectricPotentialAc' and '{}'".format(type(other).__name__))
        return ElectricPotentialAc(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, ElectricPotentialAc):
            raise TypeError("unsupported operand type(s) for *: 'ElectricPotentialAc' and '{}'".format(type(other).__name__))
        return ElectricPotentialAc(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, ElectricPotentialAc):
            raise TypeError("unsupported operand type(s) for -: 'ElectricPotentialAc' and '{}'".format(type(other).__name__))
        return ElectricPotentialAc(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, ElectricPotentialAc):
            raise TypeError("unsupported operand type(s) for /: 'ElectricPotentialAc' and '{}'".format(type(other).__name__))
        return ElectricPotentialAc(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, ElectricPotentialAc):
            raise TypeError("unsupported operand type(s) for %: 'ElectricPotentialAc' and '{}'".format(type(other).__name__))
        return ElectricPotentialAc(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, ElectricPotentialAc):
            raise TypeError("unsupported operand type(s) for **: 'ElectricPotentialAc' and '{}'".format(type(other).__name__))
        return ElectricPotentialAc(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, ElectricPotentialAc):
            raise TypeError("unsupported operand type(s) for ==: 'ElectricPotentialAc' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, ElectricPotentialAc):
            raise TypeError("unsupported operand type(s) for <: 'ElectricPotentialAc' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, ElectricPotentialAc):
            raise TypeError("unsupported operand type(s) for >: 'ElectricPotentialAc' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, ElectricPotentialAc):
            raise TypeError("unsupported operand type(s) for <=: 'ElectricPotentialAc' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, ElectricPotentialAc):
            raise TypeError("unsupported operand type(s) for >=: 'ElectricPotentialAc' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value
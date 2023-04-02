from enum import Enum
import math
import string


class ElectricPotentialDcUnits(Enum):
        """
            ElectricPotentialDcUnits enumeration
        """
        
        VoltDc = 'volt_dc'
        """
            
        """
        
        MicroVoltDc = 'micro_volt_dc'
        """
            
        """
        
        MilliVoltDc = 'milli_volt_dc'
        """
            
        """
        
        KiloVoltDc = 'kilo_volt_dc'
        """
            
        """
        
        MegaVoltDc = 'mega_volt_dc'
        """
            
        """
        
    
class ElectricPotentialDc:
    """
    The Electric Potential of a system known to use Direct Current.

    Args:
        value (float): The value.
        from_unit (ElectricPotentialDcUnits): The ElectricPotentialDc unit to create from, The default unit is VoltDc
    """
    def __init__(self, value: float, from_unit: ElectricPotentialDcUnits = ElectricPotentialDcUnits.VoltDc):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__volts_dc = None
        
        self.__micro_volts_dc = None
        
        self.__milli_volts_dc = None
        
        self.__kilo_volts_dc = None
        
        self.__mega_volts_dc = None
        

    def __convert_from_base(self, from_unit: ElectricPotentialDcUnits) -> float:
        value = self.__value
        
        if from_unit == ElectricPotentialDcUnits.VoltDc:
            return (value)
        
        if from_unit == ElectricPotentialDcUnits.MicroVoltDc:
            return ((value) / 1e-06)
        
        if from_unit == ElectricPotentialDcUnits.MilliVoltDc:
            return ((value) / 0.001)
        
        if from_unit == ElectricPotentialDcUnits.KiloVoltDc:
            return ((value) / 1000.0)
        
        if from_unit == ElectricPotentialDcUnits.MegaVoltDc:
            return ((value) / 1000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: ElectricPotentialDcUnits) -> float:
        
        if to_unit == ElectricPotentialDcUnits.VoltDc:
            return (value)
        
        if to_unit == ElectricPotentialDcUnits.MicroVoltDc:
            return ((value) * 1e-06)
        
        if to_unit == ElectricPotentialDcUnits.MilliVoltDc:
            return ((value) * 0.001)
        
        if to_unit == ElectricPotentialDcUnits.KiloVoltDc:
            return ((value) * 1000.0)
        
        if to_unit == ElectricPotentialDcUnits.MegaVoltDc:
            return ((value) * 1000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
    @staticmethod
    def from_volts_dc(volts_dc: float):
        """
        Create a new instance of ElectricPotentialDc from a value in volts_dc.

        

        :param meters: The ElectricPotentialDc value in volts_dc.
        :type volts_dc: float
        :return: A new instance of ElectricPotentialDc.
        :rtype: ElectricPotentialDc
        """
        return ElectricPotentialDc(volts_dc, ElectricPotentialDcUnits.VoltDc)

    
    @staticmethod
    def from_micro_volts_dc(micro_volts_dc: float):
        """
        Create a new instance of ElectricPotentialDc from a value in micro_volts_dc.

        

        :param meters: The ElectricPotentialDc value in micro_volts_dc.
        :type micro_volts_dc: float
        :return: A new instance of ElectricPotentialDc.
        :rtype: ElectricPotentialDc
        """
        return ElectricPotentialDc(micro_volts_dc, ElectricPotentialDcUnits.MicroVoltDc)

    
    @staticmethod
    def from_milli_volts_dc(milli_volts_dc: float):
        """
        Create a new instance of ElectricPotentialDc from a value in milli_volts_dc.

        

        :param meters: The ElectricPotentialDc value in milli_volts_dc.
        :type milli_volts_dc: float
        :return: A new instance of ElectricPotentialDc.
        :rtype: ElectricPotentialDc
        """
        return ElectricPotentialDc(milli_volts_dc, ElectricPotentialDcUnits.MilliVoltDc)

    
    @staticmethod
    def from_kilo_volts_dc(kilo_volts_dc: float):
        """
        Create a new instance of ElectricPotentialDc from a value in kilo_volts_dc.

        

        :param meters: The ElectricPotentialDc value in kilo_volts_dc.
        :type kilo_volts_dc: float
        :return: A new instance of ElectricPotentialDc.
        :rtype: ElectricPotentialDc
        """
        return ElectricPotentialDc(kilo_volts_dc, ElectricPotentialDcUnits.KiloVoltDc)

    
    @staticmethod
    def from_mega_volts_dc(mega_volts_dc: float):
        """
        Create a new instance of ElectricPotentialDc from a value in mega_volts_dc.

        

        :param meters: The ElectricPotentialDc value in mega_volts_dc.
        :type mega_volts_dc: float
        :return: A new instance of ElectricPotentialDc.
        :rtype: ElectricPotentialDc
        """
        return ElectricPotentialDc(mega_volts_dc, ElectricPotentialDcUnits.MegaVoltDc)

    
    @property
    def volts_dc(self) -> float:
        """
        
        """
        if self.__volts_dc != None:
            return self.__volts_dc
        self.__volts_dc = self.__convert_from_base(ElectricPotentialDcUnits.VoltDc)
        return self.__volts_dc

    
    @property
    def micro_volts_dc(self) -> float:
        """
        
        """
        if self.__micro_volts_dc != None:
            return self.__micro_volts_dc
        self.__micro_volts_dc = self.__convert_from_base(ElectricPotentialDcUnits.MicroVoltDc)
        return self.__micro_volts_dc

    
    @property
    def milli_volts_dc(self) -> float:
        """
        
        """
        if self.__milli_volts_dc != None:
            return self.__milli_volts_dc
        self.__milli_volts_dc = self.__convert_from_base(ElectricPotentialDcUnits.MilliVoltDc)
        return self.__milli_volts_dc

    
    @property
    def kilo_volts_dc(self) -> float:
        """
        
        """
        if self.__kilo_volts_dc != None:
            return self.__kilo_volts_dc
        self.__kilo_volts_dc = self.__convert_from_base(ElectricPotentialDcUnits.KiloVoltDc)
        return self.__kilo_volts_dc

    
    @property
    def mega_volts_dc(self) -> float:
        """
        
        """
        if self.__mega_volts_dc != None:
            return self.__mega_volts_dc
        self.__mega_volts_dc = self.__convert_from_base(ElectricPotentialDcUnits.MegaVoltDc)
        return self.__mega_volts_dc

    
    def to_string(self, unit: ElectricPotentialDcUnits = ElectricPotentialDcUnits.VoltDc) -> string:
        """
        Format the ElectricPotentialDc to string.
        Note! the default format for ElectricPotentialDc is VoltDc.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == ElectricPotentialDcUnits.VoltDc:
            return f"""{self.volts_dc} Vdc"""
        
        if unit == ElectricPotentialDcUnits.MicroVoltDc:
            return f"""{self.micro_volts_dc} """
        
        if unit == ElectricPotentialDcUnits.MilliVoltDc:
            return f"""{self.milli_volts_dc} """
        
        if unit == ElectricPotentialDcUnits.KiloVoltDc:
            return f"""{self.kilo_volts_dc} """
        
        if unit == ElectricPotentialDcUnits.MegaVoltDc:
            return f"""{self.mega_volts_dc} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: ElectricPotentialDcUnits = ElectricPotentialDcUnits.VoltDc) -> string:
        """
        Get ElectricPotentialDc unit abbreviation.
        Note! the default abbreviation for ElectricPotentialDc is VoltDc.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == ElectricPotentialDcUnits.VoltDc:
            return """Vdc"""
        
        if unit_abbreviation == ElectricPotentialDcUnits.MicroVoltDc:
            return """"""
        
        if unit_abbreviation == ElectricPotentialDcUnits.MilliVoltDc:
            return """"""
        
        if unit_abbreviation == ElectricPotentialDcUnits.KiloVoltDc:
            return """"""
        
        if unit_abbreviation == ElectricPotentialDcUnits.MegaVoltDc:
            return """"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, ElectricPotentialDc):
            raise TypeError("unsupported operand type(s) for +: 'ElectricPotentialDc' and '{}'".format(type(other).__name__))
        return ElectricPotentialDc(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, ElectricPotentialDc):
            raise TypeError("unsupported operand type(s) for *: 'ElectricPotentialDc' and '{}'".format(type(other).__name__))
        return ElectricPotentialDc(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, ElectricPotentialDc):
            raise TypeError("unsupported operand type(s) for -: 'ElectricPotentialDc' and '{}'".format(type(other).__name__))
        return ElectricPotentialDc(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, ElectricPotentialDc):
            raise TypeError("unsupported operand type(s) for /: 'ElectricPotentialDc' and '{}'".format(type(other).__name__))
        return ElectricPotentialDc(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, ElectricPotentialDc):
            raise TypeError("unsupported operand type(s) for %: 'ElectricPotentialDc' and '{}'".format(type(other).__name__))
        return ElectricPotentialDc(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, ElectricPotentialDc):
            raise TypeError("unsupported operand type(s) for **: 'ElectricPotentialDc' and '{}'".format(type(other).__name__))
        return ElectricPotentialDc(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, ElectricPotentialDc):
            raise TypeError("unsupported operand type(s) for ==: 'ElectricPotentialDc' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, ElectricPotentialDc):
            raise TypeError("unsupported operand type(s) for <: 'ElectricPotentialDc' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, ElectricPotentialDc):
            raise TypeError("unsupported operand type(s) for >: 'ElectricPotentialDc' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, ElectricPotentialDc):
            raise TypeError("unsupported operand type(s) for <=: 'ElectricPotentialDc' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, ElectricPotentialDc):
            raise TypeError("unsupported operand type(s) for >=: 'ElectricPotentialDc' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value
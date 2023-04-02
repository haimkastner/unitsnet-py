from enum import Enum
import math
import string


class ElectricPotentialUnits(Enum):
        """
            ElectricPotentialUnits enumeration
        """
        
        Volt = 'volt'
        """
            
        """
        
        NanoVolt = 'nano_volt'
        """
            
        """
        
        MicroVolt = 'micro_volt'
        """
            
        """
        
        MilliVolt = 'milli_volt'
        """
            
        """
        
        KiloVolt = 'kilo_volt'
        """
            
        """
        
        MegaVolt = 'mega_volt'
        """
            
        """
        

class ElectricPotential:
    """
    In classical electromagnetism, the electric potential (a scalar quantity denoted by Φ, ΦE or V and also called the electric field potential or the electrostatic potential) at a point is the amount of electric potential energy that a unitary point charge would have when located at that point.

    Args:
        value (float): The value.
        from_unit (ElectricPotentialUnits): The ElectricPotential unit to create from, The default unit is Volt
    """
    def __init__(self, value: float, from_unit: ElectricPotentialUnits = ElectricPotentialUnits.Volt):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__volts = None
        
        self.__nano_volts = None
        
        self.__micro_volts = None
        
        self.__milli_volts = None
        
        self.__kilo_volts = None
        
        self.__mega_volts = None
        

    def __convert_from_base(self, from_unit: ElectricPotentialUnits) -> float:
        value = self.__value
        
        if from_unit == ElectricPotentialUnits.Volt:
            return (value)
        
        if from_unit == ElectricPotentialUnits.NanoVolt:
            return ((value) / 1e-09)
        
        if from_unit == ElectricPotentialUnits.MicroVolt:
            return ((value) / 1e-06)
        
        if from_unit == ElectricPotentialUnits.MilliVolt:
            return ((value) / 0.001)
        
        if from_unit == ElectricPotentialUnits.KiloVolt:
            return ((value) / 1000.0)
        
        if from_unit == ElectricPotentialUnits.MegaVolt:
            return ((value) / 1000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: ElectricPotentialUnits) -> float:
        
        if to_unit == ElectricPotentialUnits.Volt:
            return (value)
        
        if to_unit == ElectricPotentialUnits.NanoVolt:
            return ((value) * 1e-09)
        
        if to_unit == ElectricPotentialUnits.MicroVolt:
            return ((value) * 1e-06)
        
        if to_unit == ElectricPotentialUnits.MilliVolt:
            return ((value) * 0.001)
        
        if to_unit == ElectricPotentialUnits.KiloVolt:
            return ((value) * 1000.0)
        
        if to_unit == ElectricPotentialUnits.MegaVolt:
            return ((value) * 1000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
    @staticmethod
    def from_volts(volts: float):
        """
        Create a new instance of ElectricPotential from a value in volts.

        

        :param meters: The ElectricPotential value in volts.
        :type volts: float
        :return: A new instance of ElectricPotential.
        :rtype: ElectricPotential
        """
        return ElectricPotential(volts, ElectricPotentialUnits.Volt)

    
    @staticmethod
    def from_nano_volts(nano_volts: float):
        """
        Create a new instance of ElectricPotential from a value in nano_volts.

        

        :param meters: The ElectricPotential value in nano_volts.
        :type nano_volts: float
        :return: A new instance of ElectricPotential.
        :rtype: ElectricPotential
        """
        return ElectricPotential(nano_volts, ElectricPotentialUnits.NanoVolt)

    
    @staticmethod
    def from_micro_volts(micro_volts: float):
        """
        Create a new instance of ElectricPotential from a value in micro_volts.

        

        :param meters: The ElectricPotential value in micro_volts.
        :type micro_volts: float
        :return: A new instance of ElectricPotential.
        :rtype: ElectricPotential
        """
        return ElectricPotential(micro_volts, ElectricPotentialUnits.MicroVolt)

    
    @staticmethod
    def from_milli_volts(milli_volts: float):
        """
        Create a new instance of ElectricPotential from a value in milli_volts.

        

        :param meters: The ElectricPotential value in milli_volts.
        :type milli_volts: float
        :return: A new instance of ElectricPotential.
        :rtype: ElectricPotential
        """
        return ElectricPotential(milli_volts, ElectricPotentialUnits.MilliVolt)

    
    @staticmethod
    def from_kilo_volts(kilo_volts: float):
        """
        Create a new instance of ElectricPotential from a value in kilo_volts.

        

        :param meters: The ElectricPotential value in kilo_volts.
        :type kilo_volts: float
        :return: A new instance of ElectricPotential.
        :rtype: ElectricPotential
        """
        return ElectricPotential(kilo_volts, ElectricPotentialUnits.KiloVolt)

    
    @staticmethod
    def from_mega_volts(mega_volts: float):
        """
        Create a new instance of ElectricPotential from a value in mega_volts.

        

        :param meters: The ElectricPotential value in mega_volts.
        :type mega_volts: float
        :return: A new instance of ElectricPotential.
        :rtype: ElectricPotential
        """
        return ElectricPotential(mega_volts, ElectricPotentialUnits.MegaVolt)

    
    @property
    def volts(self) -> float:
        """
        
        """
        if self.__volts != None:
            return self.__volts
        self.__volts = self.__convert_from_base(ElectricPotentialUnits.Volt)
        return self.__volts

    
    @property
    def nano_volts(self) -> float:
        """
        
        """
        if self.__nano_volts != None:
            return self.__nano_volts
        self.__nano_volts = self.__convert_from_base(ElectricPotentialUnits.NanoVolt)
        return self.__nano_volts

    
    @property
    def micro_volts(self) -> float:
        """
        
        """
        if self.__micro_volts != None:
            return self.__micro_volts
        self.__micro_volts = self.__convert_from_base(ElectricPotentialUnits.MicroVolt)
        return self.__micro_volts

    
    @property
    def milli_volts(self) -> float:
        """
        
        """
        if self.__milli_volts != None:
            return self.__milli_volts
        self.__milli_volts = self.__convert_from_base(ElectricPotentialUnits.MilliVolt)
        return self.__milli_volts

    
    @property
    def kilo_volts(self) -> float:
        """
        
        """
        if self.__kilo_volts != None:
            return self.__kilo_volts
        self.__kilo_volts = self.__convert_from_base(ElectricPotentialUnits.KiloVolt)
        return self.__kilo_volts

    
    @property
    def mega_volts(self) -> float:
        """
        
        """
        if self.__mega_volts != None:
            return self.__mega_volts
        self.__mega_volts = self.__convert_from_base(ElectricPotentialUnits.MegaVolt)
        return self.__mega_volts

    
    def to_string(self, unit: ElectricPotentialUnits = ElectricPotentialUnits.Volt) -> string:
        """
        Format the ElectricPotential to string.
        Note! the default format for ElectricPotential is Volt.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == ElectricPotentialUnits.Volt:
            return f"""{self.volts} V"""
        
        if unit == ElectricPotentialUnits.NanoVolt:
            return f"""{self.nano_volts} """
        
        if unit == ElectricPotentialUnits.MicroVolt:
            return f"""{self.micro_volts} """
        
        if unit == ElectricPotentialUnits.MilliVolt:
            return f"""{self.milli_volts} """
        
        if unit == ElectricPotentialUnits.KiloVolt:
            return f"""{self.kilo_volts} """
        
        if unit == ElectricPotentialUnits.MegaVolt:
            return f"""{self.mega_volts} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: ElectricPotentialUnits = ElectricPotentialUnits.Volt) -> string:
        """
        Get ElectricPotential unit abbreviation.
        Note! the default abbreviation for ElectricPotential is Volt.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == ElectricPotentialUnits.Volt:
            return """V"""
        
        if unit_abbreviation == ElectricPotentialUnits.NanoVolt:
            return """"""
        
        if unit_abbreviation == ElectricPotentialUnits.MicroVolt:
            return """"""
        
        if unit_abbreviation == ElectricPotentialUnits.MilliVolt:
            return """"""
        
        if unit_abbreviation == ElectricPotentialUnits.KiloVolt:
            return """"""
        
        if unit_abbreviation == ElectricPotentialUnits.MegaVolt:
            return """"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, ElectricPotential):
            raise TypeError("unsupported operand type(s) for +: 'ElectricPotential' and '{}'".format(type(other).__name__))
        return ElectricPotential(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, ElectricPotential):
            raise TypeError("unsupported operand type(s) for *: 'ElectricPotential' and '{}'".format(type(other).__name__))
        return ElectricPotential(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, ElectricPotential):
            raise TypeError("unsupported operand type(s) for -: 'ElectricPotential' and '{}'".format(type(other).__name__))
        return ElectricPotential(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, ElectricPotential):
            raise TypeError("unsupported operand type(s) for /: 'ElectricPotential' and '{}'".format(type(other).__name__))
        return ElectricPotential(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, ElectricPotential):
            raise TypeError("unsupported operand type(s) for %: 'ElectricPotential' and '{}'".format(type(other).__name__))
        return ElectricPotential(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, ElectricPotential):
            raise TypeError("unsupported operand type(s) for **: 'ElectricPotential' and '{}'".format(type(other).__name__))
        return ElectricPotential(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, ElectricPotential):
            raise TypeError("unsupported operand type(s) for ==: 'ElectricPotential' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, ElectricPotential):
            raise TypeError("unsupported operand type(s) for <: 'ElectricPotential' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, ElectricPotential):
            raise TypeError("unsupported operand type(s) for >: 'ElectricPotential' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, ElectricPotential):
            raise TypeError("unsupported operand type(s) for <=: 'ElectricPotential' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, ElectricPotential):
            raise TypeError("unsupported operand type(s) for >=: 'ElectricPotential' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value
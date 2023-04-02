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
        
        FemtoAmpere = 'femto_ampere'
        """
            
        """
        
        PicoAmpere = 'pico_ampere'
        """
            
        """
        
        NanoAmpere = 'nano_ampere'
        """
            
        """
        
        MicroAmpere = 'micro_ampere'
        """
            
        """
        
        MilliAmpere = 'milli_ampere'
        """
            
        """
        
        CentiAmpere = 'centi_ampere'
        """
            
        """
        
        KiloAmpere = 'kilo_ampere'
        """
            
        """
        
        MegaAmpere = 'mega_ampere'
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
        
        self.__femto_amperes = None
        
        self.__pico_amperes = None
        
        self.__nano_amperes = None
        
        self.__micro_amperes = None
        
        self.__milli_amperes = None
        
        self.__centi_amperes = None
        
        self.__kilo_amperes = None
        
        self.__mega_amperes = None
        

    def __convert_from_base(self, from_unit: ElectricCurrentUnits) -> float:
        value = self.__value
        
        if from_unit == ElectricCurrentUnits.Ampere:
            return (value)
        
        if from_unit == ElectricCurrentUnits.FemtoAmpere:
            return ((value) / 1e-15)
        
        if from_unit == ElectricCurrentUnits.PicoAmpere:
            return ((value) / 1e-12)
        
        if from_unit == ElectricCurrentUnits.NanoAmpere:
            return ((value) / 1e-09)
        
        if from_unit == ElectricCurrentUnits.MicroAmpere:
            return ((value) / 1e-06)
        
        if from_unit == ElectricCurrentUnits.MilliAmpere:
            return ((value) / 0.001)
        
        if from_unit == ElectricCurrentUnits.CentiAmpere:
            return ((value) / 0.01)
        
        if from_unit == ElectricCurrentUnits.KiloAmpere:
            return ((value) / 1000.0)
        
        if from_unit == ElectricCurrentUnits.MegaAmpere:
            return ((value) / 1000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: ElectricCurrentUnits) -> float:
        
        if to_unit == ElectricCurrentUnits.Ampere:
            return (value)
        
        if to_unit == ElectricCurrentUnits.FemtoAmpere:
            return ((value) * 1e-15)
        
        if to_unit == ElectricCurrentUnits.PicoAmpere:
            return ((value) * 1e-12)
        
        if to_unit == ElectricCurrentUnits.NanoAmpere:
            return ((value) * 1e-09)
        
        if to_unit == ElectricCurrentUnits.MicroAmpere:
            return ((value) * 1e-06)
        
        if to_unit == ElectricCurrentUnits.MilliAmpere:
            return ((value) * 0.001)
        
        if to_unit == ElectricCurrentUnits.CentiAmpere:
            return ((value) * 0.01)
        
        if to_unit == ElectricCurrentUnits.KiloAmpere:
            return ((value) * 1000.0)
        
        if to_unit == ElectricCurrentUnits.MegaAmpere:
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
    def from_femto_amperes(femto_amperes: float):
        """
        Create a new instance of ElectricCurrent from a value in femto_amperes.

        

        :param meters: The ElectricCurrent value in femto_amperes.
        :type femto_amperes: float
        :return: A new instance of ElectricCurrent.
        :rtype: ElectricCurrent
        """
        return ElectricCurrent(femto_amperes, ElectricCurrentUnits.FemtoAmpere)

    
    @staticmethod
    def from_pico_amperes(pico_amperes: float):
        """
        Create a new instance of ElectricCurrent from a value in pico_amperes.

        

        :param meters: The ElectricCurrent value in pico_amperes.
        :type pico_amperes: float
        :return: A new instance of ElectricCurrent.
        :rtype: ElectricCurrent
        """
        return ElectricCurrent(pico_amperes, ElectricCurrentUnits.PicoAmpere)

    
    @staticmethod
    def from_nano_amperes(nano_amperes: float):
        """
        Create a new instance of ElectricCurrent from a value in nano_amperes.

        

        :param meters: The ElectricCurrent value in nano_amperes.
        :type nano_amperes: float
        :return: A new instance of ElectricCurrent.
        :rtype: ElectricCurrent
        """
        return ElectricCurrent(nano_amperes, ElectricCurrentUnits.NanoAmpere)

    
    @staticmethod
    def from_micro_amperes(micro_amperes: float):
        """
        Create a new instance of ElectricCurrent from a value in micro_amperes.

        

        :param meters: The ElectricCurrent value in micro_amperes.
        :type micro_amperes: float
        :return: A new instance of ElectricCurrent.
        :rtype: ElectricCurrent
        """
        return ElectricCurrent(micro_amperes, ElectricCurrentUnits.MicroAmpere)

    
    @staticmethod
    def from_milli_amperes(milli_amperes: float):
        """
        Create a new instance of ElectricCurrent from a value in milli_amperes.

        

        :param meters: The ElectricCurrent value in milli_amperes.
        :type milli_amperes: float
        :return: A new instance of ElectricCurrent.
        :rtype: ElectricCurrent
        """
        return ElectricCurrent(milli_amperes, ElectricCurrentUnits.MilliAmpere)

    
    @staticmethod
    def from_centi_amperes(centi_amperes: float):
        """
        Create a new instance of ElectricCurrent from a value in centi_amperes.

        

        :param meters: The ElectricCurrent value in centi_amperes.
        :type centi_amperes: float
        :return: A new instance of ElectricCurrent.
        :rtype: ElectricCurrent
        """
        return ElectricCurrent(centi_amperes, ElectricCurrentUnits.CentiAmpere)

    
    @staticmethod
    def from_kilo_amperes(kilo_amperes: float):
        """
        Create a new instance of ElectricCurrent from a value in kilo_amperes.

        

        :param meters: The ElectricCurrent value in kilo_amperes.
        :type kilo_amperes: float
        :return: A new instance of ElectricCurrent.
        :rtype: ElectricCurrent
        """
        return ElectricCurrent(kilo_amperes, ElectricCurrentUnits.KiloAmpere)

    
    @staticmethod
    def from_mega_amperes(mega_amperes: float):
        """
        Create a new instance of ElectricCurrent from a value in mega_amperes.

        

        :param meters: The ElectricCurrent value in mega_amperes.
        :type mega_amperes: float
        :return: A new instance of ElectricCurrent.
        :rtype: ElectricCurrent
        """
        return ElectricCurrent(mega_amperes, ElectricCurrentUnits.MegaAmpere)

    
    @property
    def amperes(self) -> float:
        """
        
        """
        if self.__amperes != None:
            return self.__amperes
        self.__amperes = self.__convert_from_base(ElectricCurrentUnits.Ampere)
        return self.__amperes

    
    @property
    def femto_amperes(self) -> float:
        """
        
        """
        if self.__femto_amperes != None:
            return self.__femto_amperes
        self.__femto_amperes = self.__convert_from_base(ElectricCurrentUnits.FemtoAmpere)
        return self.__femto_amperes

    
    @property
    def pico_amperes(self) -> float:
        """
        
        """
        if self.__pico_amperes != None:
            return self.__pico_amperes
        self.__pico_amperes = self.__convert_from_base(ElectricCurrentUnits.PicoAmpere)
        return self.__pico_amperes

    
    @property
    def nano_amperes(self) -> float:
        """
        
        """
        if self.__nano_amperes != None:
            return self.__nano_amperes
        self.__nano_amperes = self.__convert_from_base(ElectricCurrentUnits.NanoAmpere)
        return self.__nano_amperes

    
    @property
    def micro_amperes(self) -> float:
        """
        
        """
        if self.__micro_amperes != None:
            return self.__micro_amperes
        self.__micro_amperes = self.__convert_from_base(ElectricCurrentUnits.MicroAmpere)
        return self.__micro_amperes

    
    @property
    def milli_amperes(self) -> float:
        """
        
        """
        if self.__milli_amperes != None:
            return self.__milli_amperes
        self.__milli_amperes = self.__convert_from_base(ElectricCurrentUnits.MilliAmpere)
        return self.__milli_amperes

    
    @property
    def centi_amperes(self) -> float:
        """
        
        """
        if self.__centi_amperes != None:
            return self.__centi_amperes
        self.__centi_amperes = self.__convert_from_base(ElectricCurrentUnits.CentiAmpere)
        return self.__centi_amperes

    
    @property
    def kilo_amperes(self) -> float:
        """
        
        """
        if self.__kilo_amperes != None:
            return self.__kilo_amperes
        self.__kilo_amperes = self.__convert_from_base(ElectricCurrentUnits.KiloAmpere)
        return self.__kilo_amperes

    
    @property
    def mega_amperes(self) -> float:
        """
        
        """
        if self.__mega_amperes != None:
            return self.__mega_amperes
        self.__mega_amperes = self.__convert_from_base(ElectricCurrentUnits.MegaAmpere)
        return self.__mega_amperes

    
    def to_string(self, unit: ElectricCurrentUnits = ElectricCurrentUnits.Ampere) -> string:
        """
        Format the ElectricCurrent to string.
        Note! the default format for ElectricCurrent is Ampere.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == ElectricCurrentUnits.Ampere:
            return f"""{self.amperes} A"""
        
        if unit == ElectricCurrentUnits.FemtoAmpere:
            return f"""{self.femto_amperes} """
        
        if unit == ElectricCurrentUnits.PicoAmpere:
            return f"""{self.pico_amperes} """
        
        if unit == ElectricCurrentUnits.NanoAmpere:
            return f"""{self.nano_amperes} """
        
        if unit == ElectricCurrentUnits.MicroAmpere:
            return f"""{self.micro_amperes} """
        
        if unit == ElectricCurrentUnits.MilliAmpere:
            return f"""{self.milli_amperes} """
        
        if unit == ElectricCurrentUnits.CentiAmpere:
            return f"""{self.centi_amperes} """
        
        if unit == ElectricCurrentUnits.KiloAmpere:
            return f"""{self.kilo_amperes} """
        
        if unit == ElectricCurrentUnits.MegaAmpere:
            return f"""{self.mega_amperes} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: ElectricCurrentUnits = ElectricCurrentUnits.Ampere) -> string:
        """
        Get ElectricCurrent unit abbreviation.
        Note! the default abbreviation for ElectricCurrent is Ampere.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == ElectricCurrentUnits.Ampere:
            return """A"""
        
        if unit_abbreviation == ElectricCurrentUnits.FemtoAmpere:
            return """"""
        
        if unit_abbreviation == ElectricCurrentUnits.PicoAmpere:
            return """"""
        
        if unit_abbreviation == ElectricCurrentUnits.NanoAmpere:
            return """"""
        
        if unit_abbreviation == ElectricCurrentUnits.MicroAmpere:
            return """"""
        
        if unit_abbreviation == ElectricCurrentUnits.MilliAmpere:
            return """"""
        
        if unit_abbreviation == ElectricCurrentUnits.CentiAmpere:
            return """"""
        
        if unit_abbreviation == ElectricCurrentUnits.KiloAmpere:
            return """"""
        
        if unit_abbreviation == ElectricCurrentUnits.MegaAmpere:
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
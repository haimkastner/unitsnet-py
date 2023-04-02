from enum import Enum
import math
import string


class ElectricChargeUnits(Enum):
        """
            ElectricChargeUnits enumeration
        """
        
        Coulomb = 'coulomb'
        """
            
        """
        
        AmpereHour = 'ampere_hour'
        """
            
        """
        
        PicoCoulomb = 'pico_coulomb'
        """
            
        """
        
        NanoCoulomb = 'nano_coulomb'
        """
            
        """
        
        MicroCoulomb = 'micro_coulomb'
        """
            
        """
        
        MilliCoulomb = 'milli_coulomb'
        """
            
        """
        
        KiloCoulomb = 'kilo_coulomb'
        """
            
        """
        
        MegaCoulomb = 'mega_coulomb'
        """
            
        """
        
        MilliAmpereHour = 'milli_ampere_hour'
        """
            
        """
        
        KiloAmpereHour = 'kilo_ampere_hour'
        """
            
        """
        
        MegaAmpereHour = 'mega_ampere_hour'
        """
            
        """
        

class ElectricCharge:
    """
    Electric charge is the physical property of matter that causes it to experience a force when placed in an electromagnetic field.

    Args:
        value (float): The value.
        from_unit (ElectricChargeUnits): The ElectricCharge unit to create from, The default unit is Coulomb
    """
    def __init__(self, value: float, from_unit: ElectricChargeUnits = ElectricChargeUnits.Coulomb):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__coulombs = None
        
        self.__ampere_hours = None
        
        self.__pico_coulombs = None
        
        self.__nano_coulombs = None
        
        self.__micro_coulombs = None
        
        self.__milli_coulombs = None
        
        self.__kilo_coulombs = None
        
        self.__mega_coulombs = None
        
        self.__milli_ampere_hours = None
        
        self.__kilo_ampere_hours = None
        
        self.__mega_ampere_hours = None
        

    def __convert_from_base(self, from_unit: ElectricChargeUnits) -> float:
        value = self.__value
        
        if from_unit == ElectricChargeUnits.Coulomb:
            return (value)
        
        if from_unit == ElectricChargeUnits.AmpereHour:
            return (value * 2.77777777777e-4)
        
        if from_unit == ElectricChargeUnits.PicoCoulomb:
            return ((value) / 1e-12)
        
        if from_unit == ElectricChargeUnits.NanoCoulomb:
            return ((value) / 1e-09)
        
        if from_unit == ElectricChargeUnits.MicroCoulomb:
            return ((value) / 1e-06)
        
        if from_unit == ElectricChargeUnits.MilliCoulomb:
            return ((value) / 0.001)
        
        if from_unit == ElectricChargeUnits.KiloCoulomb:
            return ((value) / 1000.0)
        
        if from_unit == ElectricChargeUnits.MegaCoulomb:
            return ((value) / 1000000.0)
        
        if from_unit == ElectricChargeUnits.MilliAmpereHour:
            return ((value * 2.77777777777e-4) / 0.001)
        
        if from_unit == ElectricChargeUnits.KiloAmpereHour:
            return ((value * 2.77777777777e-4) / 1000.0)
        
        if from_unit == ElectricChargeUnits.MegaAmpereHour:
            return ((value * 2.77777777777e-4) / 1000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: ElectricChargeUnits) -> float:
        
        if to_unit == ElectricChargeUnits.Coulomb:
            return (value)
        
        if to_unit == ElectricChargeUnits.AmpereHour:
            return (value / 2.77777777777e-4)
        
        if to_unit == ElectricChargeUnits.PicoCoulomb:
            return ((value) * 1e-12)
        
        if to_unit == ElectricChargeUnits.NanoCoulomb:
            return ((value) * 1e-09)
        
        if to_unit == ElectricChargeUnits.MicroCoulomb:
            return ((value) * 1e-06)
        
        if to_unit == ElectricChargeUnits.MilliCoulomb:
            return ((value) * 0.001)
        
        if to_unit == ElectricChargeUnits.KiloCoulomb:
            return ((value) * 1000.0)
        
        if to_unit == ElectricChargeUnits.MegaCoulomb:
            return ((value) * 1000000.0)
        
        if to_unit == ElectricChargeUnits.MilliAmpereHour:
            return ((value / 2.77777777777e-4) * 0.001)
        
        if to_unit == ElectricChargeUnits.KiloAmpereHour:
            return ((value / 2.77777777777e-4) * 1000.0)
        
        if to_unit == ElectricChargeUnits.MegaAmpereHour:
            return ((value / 2.77777777777e-4) * 1000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
    @staticmethod
    def from_coulombs(coulombs: float):
        """
        Create a new instance of ElectricCharge from a value in coulombs.

        

        :param meters: The ElectricCharge value in coulombs.
        :type coulombs: float
        :return: A new instance of ElectricCharge.
        :rtype: ElectricCharge
        """
        return ElectricCharge(coulombs, ElectricChargeUnits.Coulomb)

    
    @staticmethod
    def from_ampere_hours(ampere_hours: float):
        """
        Create a new instance of ElectricCharge from a value in ampere_hours.

        

        :param meters: The ElectricCharge value in ampere_hours.
        :type ampere_hours: float
        :return: A new instance of ElectricCharge.
        :rtype: ElectricCharge
        """
        return ElectricCharge(ampere_hours, ElectricChargeUnits.AmpereHour)

    
    @staticmethod
    def from_pico_coulombs(pico_coulombs: float):
        """
        Create a new instance of ElectricCharge from a value in pico_coulombs.

        

        :param meters: The ElectricCharge value in pico_coulombs.
        :type pico_coulombs: float
        :return: A new instance of ElectricCharge.
        :rtype: ElectricCharge
        """
        return ElectricCharge(pico_coulombs, ElectricChargeUnits.PicoCoulomb)

    
    @staticmethod
    def from_nano_coulombs(nano_coulombs: float):
        """
        Create a new instance of ElectricCharge from a value in nano_coulombs.

        

        :param meters: The ElectricCharge value in nano_coulombs.
        :type nano_coulombs: float
        :return: A new instance of ElectricCharge.
        :rtype: ElectricCharge
        """
        return ElectricCharge(nano_coulombs, ElectricChargeUnits.NanoCoulomb)

    
    @staticmethod
    def from_micro_coulombs(micro_coulombs: float):
        """
        Create a new instance of ElectricCharge from a value in micro_coulombs.

        

        :param meters: The ElectricCharge value in micro_coulombs.
        :type micro_coulombs: float
        :return: A new instance of ElectricCharge.
        :rtype: ElectricCharge
        """
        return ElectricCharge(micro_coulombs, ElectricChargeUnits.MicroCoulomb)

    
    @staticmethod
    def from_milli_coulombs(milli_coulombs: float):
        """
        Create a new instance of ElectricCharge from a value in milli_coulombs.

        

        :param meters: The ElectricCharge value in milli_coulombs.
        :type milli_coulombs: float
        :return: A new instance of ElectricCharge.
        :rtype: ElectricCharge
        """
        return ElectricCharge(milli_coulombs, ElectricChargeUnits.MilliCoulomb)

    
    @staticmethod
    def from_kilo_coulombs(kilo_coulombs: float):
        """
        Create a new instance of ElectricCharge from a value in kilo_coulombs.

        

        :param meters: The ElectricCharge value in kilo_coulombs.
        :type kilo_coulombs: float
        :return: A new instance of ElectricCharge.
        :rtype: ElectricCharge
        """
        return ElectricCharge(kilo_coulombs, ElectricChargeUnits.KiloCoulomb)

    
    @staticmethod
    def from_mega_coulombs(mega_coulombs: float):
        """
        Create a new instance of ElectricCharge from a value in mega_coulombs.

        

        :param meters: The ElectricCharge value in mega_coulombs.
        :type mega_coulombs: float
        :return: A new instance of ElectricCharge.
        :rtype: ElectricCharge
        """
        return ElectricCharge(mega_coulombs, ElectricChargeUnits.MegaCoulomb)

    
    @staticmethod
    def from_milli_ampere_hours(milli_ampere_hours: float):
        """
        Create a new instance of ElectricCharge from a value in milli_ampere_hours.

        

        :param meters: The ElectricCharge value in milli_ampere_hours.
        :type milli_ampere_hours: float
        :return: A new instance of ElectricCharge.
        :rtype: ElectricCharge
        """
        return ElectricCharge(milli_ampere_hours, ElectricChargeUnits.MilliAmpereHour)

    
    @staticmethod
    def from_kilo_ampere_hours(kilo_ampere_hours: float):
        """
        Create a new instance of ElectricCharge from a value in kilo_ampere_hours.

        

        :param meters: The ElectricCharge value in kilo_ampere_hours.
        :type kilo_ampere_hours: float
        :return: A new instance of ElectricCharge.
        :rtype: ElectricCharge
        """
        return ElectricCharge(kilo_ampere_hours, ElectricChargeUnits.KiloAmpereHour)

    
    @staticmethod
    def from_mega_ampere_hours(mega_ampere_hours: float):
        """
        Create a new instance of ElectricCharge from a value in mega_ampere_hours.

        

        :param meters: The ElectricCharge value in mega_ampere_hours.
        :type mega_ampere_hours: float
        :return: A new instance of ElectricCharge.
        :rtype: ElectricCharge
        """
        return ElectricCharge(mega_ampere_hours, ElectricChargeUnits.MegaAmpereHour)

    
    @property
    def coulombs(self) -> float:
        """
        
        """
        if self.__coulombs != None:
            return self.__coulombs
        self.__coulombs = self.__convert_from_base(ElectricChargeUnits.Coulomb)
        return self.__coulombs

    
    @property
    def ampere_hours(self) -> float:
        """
        
        """
        if self.__ampere_hours != None:
            return self.__ampere_hours
        self.__ampere_hours = self.__convert_from_base(ElectricChargeUnits.AmpereHour)
        return self.__ampere_hours

    
    @property
    def pico_coulombs(self) -> float:
        """
        
        """
        if self.__pico_coulombs != None:
            return self.__pico_coulombs
        self.__pico_coulombs = self.__convert_from_base(ElectricChargeUnits.PicoCoulomb)
        return self.__pico_coulombs

    
    @property
    def nano_coulombs(self) -> float:
        """
        
        """
        if self.__nano_coulombs != None:
            return self.__nano_coulombs
        self.__nano_coulombs = self.__convert_from_base(ElectricChargeUnits.NanoCoulomb)
        return self.__nano_coulombs

    
    @property
    def micro_coulombs(self) -> float:
        """
        
        """
        if self.__micro_coulombs != None:
            return self.__micro_coulombs
        self.__micro_coulombs = self.__convert_from_base(ElectricChargeUnits.MicroCoulomb)
        return self.__micro_coulombs

    
    @property
    def milli_coulombs(self) -> float:
        """
        
        """
        if self.__milli_coulombs != None:
            return self.__milli_coulombs
        self.__milli_coulombs = self.__convert_from_base(ElectricChargeUnits.MilliCoulomb)
        return self.__milli_coulombs

    
    @property
    def kilo_coulombs(self) -> float:
        """
        
        """
        if self.__kilo_coulombs != None:
            return self.__kilo_coulombs
        self.__kilo_coulombs = self.__convert_from_base(ElectricChargeUnits.KiloCoulomb)
        return self.__kilo_coulombs

    
    @property
    def mega_coulombs(self) -> float:
        """
        
        """
        if self.__mega_coulombs != None:
            return self.__mega_coulombs
        self.__mega_coulombs = self.__convert_from_base(ElectricChargeUnits.MegaCoulomb)
        return self.__mega_coulombs

    
    @property
    def milli_ampere_hours(self) -> float:
        """
        
        """
        if self.__milli_ampere_hours != None:
            return self.__milli_ampere_hours
        self.__milli_ampere_hours = self.__convert_from_base(ElectricChargeUnits.MilliAmpereHour)
        return self.__milli_ampere_hours

    
    @property
    def kilo_ampere_hours(self) -> float:
        """
        
        """
        if self.__kilo_ampere_hours != None:
            return self.__kilo_ampere_hours
        self.__kilo_ampere_hours = self.__convert_from_base(ElectricChargeUnits.KiloAmpereHour)
        return self.__kilo_ampere_hours

    
    @property
    def mega_ampere_hours(self) -> float:
        """
        
        """
        if self.__mega_ampere_hours != None:
            return self.__mega_ampere_hours
        self.__mega_ampere_hours = self.__convert_from_base(ElectricChargeUnits.MegaAmpereHour)
        return self.__mega_ampere_hours

    
    def to_string(self, unit: ElectricChargeUnits = ElectricChargeUnits.Coulomb) -> string:
        """
        Format the ElectricCharge to string.
        Note! the default format for ElectricCharge is Coulomb.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == ElectricChargeUnits.Coulomb:
            return f"""{self.coulombs} C"""
        
        if unit == ElectricChargeUnits.AmpereHour:
            return f"""{self.ampere_hours} A-h"""
        
        if unit == ElectricChargeUnits.PicoCoulomb:
            return f"""{self.pico_coulombs} """
        
        if unit == ElectricChargeUnits.NanoCoulomb:
            return f"""{self.nano_coulombs} """
        
        if unit == ElectricChargeUnits.MicroCoulomb:
            return f"""{self.micro_coulombs} """
        
        if unit == ElectricChargeUnits.MilliCoulomb:
            return f"""{self.milli_coulombs} """
        
        if unit == ElectricChargeUnits.KiloCoulomb:
            return f"""{self.kilo_coulombs} """
        
        if unit == ElectricChargeUnits.MegaCoulomb:
            return f"""{self.mega_coulombs} """
        
        if unit == ElectricChargeUnits.MilliAmpereHour:
            return f"""{self.milli_ampere_hours} """
        
        if unit == ElectricChargeUnits.KiloAmpereHour:
            return f"""{self.kilo_ampere_hours} """
        
        if unit == ElectricChargeUnits.MegaAmpereHour:
            return f"""{self.mega_ampere_hours} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: ElectricChargeUnits = ElectricChargeUnits.Coulomb) -> string:
        """
        Get ElectricCharge unit abbreviation.
        Note! the default abbreviation for ElectricCharge is Coulomb.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == ElectricChargeUnits.Coulomb:
            return """C"""
        
        if unit_abbreviation == ElectricChargeUnits.AmpereHour:
            return """A-h"""
        
        if unit_abbreviation == ElectricChargeUnits.PicoCoulomb:
            return """"""
        
        if unit_abbreviation == ElectricChargeUnits.NanoCoulomb:
            return """"""
        
        if unit_abbreviation == ElectricChargeUnits.MicroCoulomb:
            return """"""
        
        if unit_abbreviation == ElectricChargeUnits.MilliCoulomb:
            return """"""
        
        if unit_abbreviation == ElectricChargeUnits.KiloCoulomb:
            return """"""
        
        if unit_abbreviation == ElectricChargeUnits.MegaCoulomb:
            return """"""
        
        if unit_abbreviation == ElectricChargeUnits.MilliAmpereHour:
            return """"""
        
        if unit_abbreviation == ElectricChargeUnits.KiloAmpereHour:
            return """"""
        
        if unit_abbreviation == ElectricChargeUnits.MegaAmpereHour:
            return """"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, ElectricCharge):
            raise TypeError("unsupported operand type(s) for +: 'ElectricCharge' and '{}'".format(type(other).__name__))
        return ElectricCharge(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, ElectricCharge):
            raise TypeError("unsupported operand type(s) for *: 'ElectricCharge' and '{}'".format(type(other).__name__))
        return ElectricCharge(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, ElectricCharge):
            raise TypeError("unsupported operand type(s) for -: 'ElectricCharge' and '{}'".format(type(other).__name__))
        return ElectricCharge(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, ElectricCharge):
            raise TypeError("unsupported operand type(s) for /: 'ElectricCharge' and '{}'".format(type(other).__name__))
        return ElectricCharge(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, ElectricCharge):
            raise TypeError("unsupported operand type(s) for %: 'ElectricCharge' and '{}'".format(type(other).__name__))
        return ElectricCharge(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, ElectricCharge):
            raise TypeError("unsupported operand type(s) for **: 'ElectricCharge' and '{}'".format(type(other).__name__))
        return ElectricCharge(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, ElectricCharge):
            raise TypeError("unsupported operand type(s) for ==: 'ElectricCharge' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, ElectricCharge):
            raise TypeError("unsupported operand type(s) for <: 'ElectricCharge' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, ElectricCharge):
            raise TypeError("unsupported operand type(s) for >: 'ElectricCharge' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, ElectricCharge):
            raise TypeError("unsupported operand type(s) for <=: 'ElectricCharge' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, ElectricCharge):
            raise TypeError("unsupported operand type(s) for >=: 'ElectricCharge' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value
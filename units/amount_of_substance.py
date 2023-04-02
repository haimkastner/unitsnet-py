from enum import Enum
import math
import string


class AmountOfSubstanceUnits(Enum):
        """
            AmountOfSubstanceUnits enumeration
        """
        
        Mole = 'mole'
        """
            
        """
        
        PoundMole = 'pound_mole'
        """
            
        """
        
        NanoMole = 'nano_mole'
        """
            
        """
        
        MicroMole = 'micro_mole'
        """
            
        """
        
        MilliMole = 'milli_mole'
        """
            
        """
        
        CentiMole = 'centi_mole'
        """
            
        """
        
        DeciMole = 'deci_mole'
        """
            
        """
        
        KiloMole = 'kilo_mole'
        """
            
        """
        
        MegaMole = 'mega_mole'
        """
            
        """
        
        NanoPoundMole = 'nano_pound_mole'
        """
            
        """
        
        MicroPoundMole = 'micro_pound_mole'
        """
            
        """
        
        MilliPoundMole = 'milli_pound_mole'
        """
            
        """
        
        CentiPoundMole = 'centi_pound_mole'
        """
            
        """
        
        DeciPoundMole = 'deci_pound_mole'
        """
            
        """
        
        KiloPoundMole = 'kilo_pound_mole'
        """
            
        """
        

class AmountOfSubstance:
    """
    Mole is the amount of substance containing Avagadro's Number (6.02 x 10 ^ 23) of real particles such as molecules,atoms, ions or radicals.

    Args:
        value (float): The value.
        from_unit (AmountOfSubstanceUnits): The AmountOfSubstance unit to create from, The default unit is Mole
    """
    def __init__(self, value: float, from_unit: AmountOfSubstanceUnits = AmountOfSubstanceUnits.Mole):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__moles = None
        
        self.__pound_moles = None
        
        self.__nano_moles = None
        
        self.__micro_moles = None
        
        self.__milli_moles = None
        
        self.__centi_moles = None
        
        self.__deci_moles = None
        
        self.__kilo_moles = None
        
        self.__mega_moles = None
        
        self.__nano_pound_moles = None
        
        self.__micro_pound_moles = None
        
        self.__milli_pound_moles = None
        
        self.__centi_pound_moles = None
        
        self.__deci_pound_moles = None
        
        self.__kilo_pound_moles = None
        

    def __convert_from_base(self, from_unit: AmountOfSubstanceUnits) -> float:
        value = self.__value
        
        if from_unit == AmountOfSubstanceUnits.Mole:
            return (value)
        
        if from_unit == AmountOfSubstanceUnits.PoundMole:
            return (value / 453.59237)
        
        if from_unit == AmountOfSubstanceUnits.NanoMole:
            return ((value) / 1e-09)
        
        if from_unit == AmountOfSubstanceUnits.MicroMole:
            return ((value) / 1e-06)
        
        if from_unit == AmountOfSubstanceUnits.MilliMole:
            return ((value) / 0.001)
        
        if from_unit == AmountOfSubstanceUnits.CentiMole:
            return ((value) / 0.01)
        
        if from_unit == AmountOfSubstanceUnits.DeciMole:
            return ((value) / 0.1)
        
        if from_unit == AmountOfSubstanceUnits.KiloMole:
            return ((value) / 1000.0)
        
        if from_unit == AmountOfSubstanceUnits.MegaMole:
            return ((value) / 1000000.0)
        
        if from_unit == AmountOfSubstanceUnits.NanoPoundMole:
            return ((value / 453.59237) / 1e-09)
        
        if from_unit == AmountOfSubstanceUnits.MicroPoundMole:
            return ((value / 453.59237) / 1e-06)
        
        if from_unit == AmountOfSubstanceUnits.MilliPoundMole:
            return ((value / 453.59237) / 0.001)
        
        if from_unit == AmountOfSubstanceUnits.CentiPoundMole:
            return ((value / 453.59237) / 0.01)
        
        if from_unit == AmountOfSubstanceUnits.DeciPoundMole:
            return ((value / 453.59237) / 0.1)
        
        if from_unit == AmountOfSubstanceUnits.KiloPoundMole:
            return ((value / 453.59237) / 1000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: AmountOfSubstanceUnits) -> float:
        
        if to_unit == AmountOfSubstanceUnits.Mole:
            return (value)
        
        if to_unit == AmountOfSubstanceUnits.PoundMole:
            return (value * 453.59237)
        
        if to_unit == AmountOfSubstanceUnits.NanoMole:
            return ((value) * 1e-09)
        
        if to_unit == AmountOfSubstanceUnits.MicroMole:
            return ((value) * 1e-06)
        
        if to_unit == AmountOfSubstanceUnits.MilliMole:
            return ((value) * 0.001)
        
        if to_unit == AmountOfSubstanceUnits.CentiMole:
            return ((value) * 0.01)
        
        if to_unit == AmountOfSubstanceUnits.DeciMole:
            return ((value) * 0.1)
        
        if to_unit == AmountOfSubstanceUnits.KiloMole:
            return ((value) * 1000.0)
        
        if to_unit == AmountOfSubstanceUnits.MegaMole:
            return ((value) * 1000000.0)
        
        if to_unit == AmountOfSubstanceUnits.NanoPoundMole:
            return ((value * 453.59237) * 1e-09)
        
        if to_unit == AmountOfSubstanceUnits.MicroPoundMole:
            return ((value * 453.59237) * 1e-06)
        
        if to_unit == AmountOfSubstanceUnits.MilliPoundMole:
            return ((value * 453.59237) * 0.001)
        
        if to_unit == AmountOfSubstanceUnits.CentiPoundMole:
            return ((value * 453.59237) * 0.01)
        
        if to_unit == AmountOfSubstanceUnits.DeciPoundMole:
            return ((value * 453.59237) * 0.1)
        
        if to_unit == AmountOfSubstanceUnits.KiloPoundMole:
            return ((value * 453.59237) * 1000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
    @staticmethod
    def from_moles(moles: float):
        """
        Create a new instance of AmountOfSubstance from a value in moles.

        

        :param meters: The AmountOfSubstance value in moles.
        :type moles: float
        :return: A new instance of AmountOfSubstance.
        :rtype: AmountOfSubstance
        """
        return AmountOfSubstance(moles, AmountOfSubstanceUnits.Mole)

    
    @staticmethod
    def from_pound_moles(pound_moles: float):
        """
        Create a new instance of AmountOfSubstance from a value in pound_moles.

        

        :param meters: The AmountOfSubstance value in pound_moles.
        :type pound_moles: float
        :return: A new instance of AmountOfSubstance.
        :rtype: AmountOfSubstance
        """
        return AmountOfSubstance(pound_moles, AmountOfSubstanceUnits.PoundMole)

    
    @staticmethod
    def from_nano_moles(nano_moles: float):
        """
        Create a new instance of AmountOfSubstance from a value in nano_moles.

        

        :param meters: The AmountOfSubstance value in nano_moles.
        :type nano_moles: float
        :return: A new instance of AmountOfSubstance.
        :rtype: AmountOfSubstance
        """
        return AmountOfSubstance(nano_moles, AmountOfSubstanceUnits.NanoMole)

    
    @staticmethod
    def from_micro_moles(micro_moles: float):
        """
        Create a new instance of AmountOfSubstance from a value in micro_moles.

        

        :param meters: The AmountOfSubstance value in micro_moles.
        :type micro_moles: float
        :return: A new instance of AmountOfSubstance.
        :rtype: AmountOfSubstance
        """
        return AmountOfSubstance(micro_moles, AmountOfSubstanceUnits.MicroMole)

    
    @staticmethod
    def from_milli_moles(milli_moles: float):
        """
        Create a new instance of AmountOfSubstance from a value in milli_moles.

        

        :param meters: The AmountOfSubstance value in milli_moles.
        :type milli_moles: float
        :return: A new instance of AmountOfSubstance.
        :rtype: AmountOfSubstance
        """
        return AmountOfSubstance(milli_moles, AmountOfSubstanceUnits.MilliMole)

    
    @staticmethod
    def from_centi_moles(centi_moles: float):
        """
        Create a new instance of AmountOfSubstance from a value in centi_moles.

        

        :param meters: The AmountOfSubstance value in centi_moles.
        :type centi_moles: float
        :return: A new instance of AmountOfSubstance.
        :rtype: AmountOfSubstance
        """
        return AmountOfSubstance(centi_moles, AmountOfSubstanceUnits.CentiMole)

    
    @staticmethod
    def from_deci_moles(deci_moles: float):
        """
        Create a new instance of AmountOfSubstance from a value in deci_moles.

        

        :param meters: The AmountOfSubstance value in deci_moles.
        :type deci_moles: float
        :return: A new instance of AmountOfSubstance.
        :rtype: AmountOfSubstance
        """
        return AmountOfSubstance(deci_moles, AmountOfSubstanceUnits.DeciMole)

    
    @staticmethod
    def from_kilo_moles(kilo_moles: float):
        """
        Create a new instance of AmountOfSubstance from a value in kilo_moles.

        

        :param meters: The AmountOfSubstance value in kilo_moles.
        :type kilo_moles: float
        :return: A new instance of AmountOfSubstance.
        :rtype: AmountOfSubstance
        """
        return AmountOfSubstance(kilo_moles, AmountOfSubstanceUnits.KiloMole)

    
    @staticmethod
    def from_mega_moles(mega_moles: float):
        """
        Create a new instance of AmountOfSubstance from a value in mega_moles.

        

        :param meters: The AmountOfSubstance value in mega_moles.
        :type mega_moles: float
        :return: A new instance of AmountOfSubstance.
        :rtype: AmountOfSubstance
        """
        return AmountOfSubstance(mega_moles, AmountOfSubstanceUnits.MegaMole)

    
    @staticmethod
    def from_nano_pound_moles(nano_pound_moles: float):
        """
        Create a new instance of AmountOfSubstance from a value in nano_pound_moles.

        

        :param meters: The AmountOfSubstance value in nano_pound_moles.
        :type nano_pound_moles: float
        :return: A new instance of AmountOfSubstance.
        :rtype: AmountOfSubstance
        """
        return AmountOfSubstance(nano_pound_moles, AmountOfSubstanceUnits.NanoPoundMole)

    
    @staticmethod
    def from_micro_pound_moles(micro_pound_moles: float):
        """
        Create a new instance of AmountOfSubstance from a value in micro_pound_moles.

        

        :param meters: The AmountOfSubstance value in micro_pound_moles.
        :type micro_pound_moles: float
        :return: A new instance of AmountOfSubstance.
        :rtype: AmountOfSubstance
        """
        return AmountOfSubstance(micro_pound_moles, AmountOfSubstanceUnits.MicroPoundMole)

    
    @staticmethod
    def from_milli_pound_moles(milli_pound_moles: float):
        """
        Create a new instance of AmountOfSubstance from a value in milli_pound_moles.

        

        :param meters: The AmountOfSubstance value in milli_pound_moles.
        :type milli_pound_moles: float
        :return: A new instance of AmountOfSubstance.
        :rtype: AmountOfSubstance
        """
        return AmountOfSubstance(milli_pound_moles, AmountOfSubstanceUnits.MilliPoundMole)

    
    @staticmethod
    def from_centi_pound_moles(centi_pound_moles: float):
        """
        Create a new instance of AmountOfSubstance from a value in centi_pound_moles.

        

        :param meters: The AmountOfSubstance value in centi_pound_moles.
        :type centi_pound_moles: float
        :return: A new instance of AmountOfSubstance.
        :rtype: AmountOfSubstance
        """
        return AmountOfSubstance(centi_pound_moles, AmountOfSubstanceUnits.CentiPoundMole)

    
    @staticmethod
    def from_deci_pound_moles(deci_pound_moles: float):
        """
        Create a new instance of AmountOfSubstance from a value in deci_pound_moles.

        

        :param meters: The AmountOfSubstance value in deci_pound_moles.
        :type deci_pound_moles: float
        :return: A new instance of AmountOfSubstance.
        :rtype: AmountOfSubstance
        """
        return AmountOfSubstance(deci_pound_moles, AmountOfSubstanceUnits.DeciPoundMole)

    
    @staticmethod
    def from_kilo_pound_moles(kilo_pound_moles: float):
        """
        Create a new instance of AmountOfSubstance from a value in kilo_pound_moles.

        

        :param meters: The AmountOfSubstance value in kilo_pound_moles.
        :type kilo_pound_moles: float
        :return: A new instance of AmountOfSubstance.
        :rtype: AmountOfSubstance
        """
        return AmountOfSubstance(kilo_pound_moles, AmountOfSubstanceUnits.KiloPoundMole)

    
    @property
    def moles(self) -> float:
        """
        
        """
        if self.__moles != None:
            return self.__moles
        self.__moles = self.__convert_from_base(AmountOfSubstanceUnits.Mole)
        return self.__moles

    
    @property
    def pound_moles(self) -> float:
        """
        
        """
        if self.__pound_moles != None:
            return self.__pound_moles
        self.__pound_moles = self.__convert_from_base(AmountOfSubstanceUnits.PoundMole)
        return self.__pound_moles

    
    @property
    def nano_moles(self) -> float:
        """
        
        """
        if self.__nano_moles != None:
            return self.__nano_moles
        self.__nano_moles = self.__convert_from_base(AmountOfSubstanceUnits.NanoMole)
        return self.__nano_moles

    
    @property
    def micro_moles(self) -> float:
        """
        
        """
        if self.__micro_moles != None:
            return self.__micro_moles
        self.__micro_moles = self.__convert_from_base(AmountOfSubstanceUnits.MicroMole)
        return self.__micro_moles

    
    @property
    def milli_moles(self) -> float:
        """
        
        """
        if self.__milli_moles != None:
            return self.__milli_moles
        self.__milli_moles = self.__convert_from_base(AmountOfSubstanceUnits.MilliMole)
        return self.__milli_moles

    
    @property
    def centi_moles(self) -> float:
        """
        
        """
        if self.__centi_moles != None:
            return self.__centi_moles
        self.__centi_moles = self.__convert_from_base(AmountOfSubstanceUnits.CentiMole)
        return self.__centi_moles

    
    @property
    def deci_moles(self) -> float:
        """
        
        """
        if self.__deci_moles != None:
            return self.__deci_moles
        self.__deci_moles = self.__convert_from_base(AmountOfSubstanceUnits.DeciMole)
        return self.__deci_moles

    
    @property
    def kilo_moles(self) -> float:
        """
        
        """
        if self.__kilo_moles != None:
            return self.__kilo_moles
        self.__kilo_moles = self.__convert_from_base(AmountOfSubstanceUnits.KiloMole)
        return self.__kilo_moles

    
    @property
    def mega_moles(self) -> float:
        """
        
        """
        if self.__mega_moles != None:
            return self.__mega_moles
        self.__mega_moles = self.__convert_from_base(AmountOfSubstanceUnits.MegaMole)
        return self.__mega_moles

    
    @property
    def nano_pound_moles(self) -> float:
        """
        
        """
        if self.__nano_pound_moles != None:
            return self.__nano_pound_moles
        self.__nano_pound_moles = self.__convert_from_base(AmountOfSubstanceUnits.NanoPoundMole)
        return self.__nano_pound_moles

    
    @property
    def micro_pound_moles(self) -> float:
        """
        
        """
        if self.__micro_pound_moles != None:
            return self.__micro_pound_moles
        self.__micro_pound_moles = self.__convert_from_base(AmountOfSubstanceUnits.MicroPoundMole)
        return self.__micro_pound_moles

    
    @property
    def milli_pound_moles(self) -> float:
        """
        
        """
        if self.__milli_pound_moles != None:
            return self.__milli_pound_moles
        self.__milli_pound_moles = self.__convert_from_base(AmountOfSubstanceUnits.MilliPoundMole)
        return self.__milli_pound_moles

    
    @property
    def centi_pound_moles(self) -> float:
        """
        
        """
        if self.__centi_pound_moles != None:
            return self.__centi_pound_moles
        self.__centi_pound_moles = self.__convert_from_base(AmountOfSubstanceUnits.CentiPoundMole)
        return self.__centi_pound_moles

    
    @property
    def deci_pound_moles(self) -> float:
        """
        
        """
        if self.__deci_pound_moles != None:
            return self.__deci_pound_moles
        self.__deci_pound_moles = self.__convert_from_base(AmountOfSubstanceUnits.DeciPoundMole)
        return self.__deci_pound_moles

    
    @property
    def kilo_pound_moles(self) -> float:
        """
        
        """
        if self.__kilo_pound_moles != None:
            return self.__kilo_pound_moles
        self.__kilo_pound_moles = self.__convert_from_base(AmountOfSubstanceUnits.KiloPoundMole)
        return self.__kilo_pound_moles

    
    def to_string(self, unit: AmountOfSubstanceUnits = AmountOfSubstanceUnits.Mole) -> string:
        """
        Format the AmountOfSubstance to string.
        Note! the default format for AmountOfSubstance is Mole.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == AmountOfSubstanceUnits.Mole:
            return f"""{self.moles} mol"""
        
        if unit == AmountOfSubstanceUnits.PoundMole:
            return f"""{self.pound_moles} lbmol"""
        
        if unit == AmountOfSubstanceUnits.NanoMole:
            return f"""{self.nano_moles} """
        
        if unit == AmountOfSubstanceUnits.MicroMole:
            return f"""{self.micro_moles} """
        
        if unit == AmountOfSubstanceUnits.MilliMole:
            return f"""{self.milli_moles} """
        
        if unit == AmountOfSubstanceUnits.CentiMole:
            return f"""{self.centi_moles} """
        
        if unit == AmountOfSubstanceUnits.DeciMole:
            return f"""{self.deci_moles} """
        
        if unit == AmountOfSubstanceUnits.KiloMole:
            return f"""{self.kilo_moles} """
        
        if unit == AmountOfSubstanceUnits.MegaMole:
            return f"""{self.mega_moles} """
        
        if unit == AmountOfSubstanceUnits.NanoPoundMole:
            return f"""{self.nano_pound_moles} """
        
        if unit == AmountOfSubstanceUnits.MicroPoundMole:
            return f"""{self.micro_pound_moles} """
        
        if unit == AmountOfSubstanceUnits.MilliPoundMole:
            return f"""{self.milli_pound_moles} """
        
        if unit == AmountOfSubstanceUnits.CentiPoundMole:
            return f"""{self.centi_pound_moles} """
        
        if unit == AmountOfSubstanceUnits.DeciPoundMole:
            return f"""{self.deci_pound_moles} """
        
        if unit == AmountOfSubstanceUnits.KiloPoundMole:
            return f"""{self.kilo_pound_moles} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: AmountOfSubstanceUnits = AmountOfSubstanceUnits.Mole) -> string:
        """
        Get AmountOfSubstance unit abbreviation.
        Note! the default abbreviation for AmountOfSubstance is Mole.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == AmountOfSubstanceUnits.Mole:
            return """mol"""
        
        if unit_abbreviation == AmountOfSubstanceUnits.PoundMole:
            return """lbmol"""
        
        if unit_abbreviation == AmountOfSubstanceUnits.NanoMole:
            return """"""
        
        if unit_abbreviation == AmountOfSubstanceUnits.MicroMole:
            return """"""
        
        if unit_abbreviation == AmountOfSubstanceUnits.MilliMole:
            return """"""
        
        if unit_abbreviation == AmountOfSubstanceUnits.CentiMole:
            return """"""
        
        if unit_abbreviation == AmountOfSubstanceUnits.DeciMole:
            return """"""
        
        if unit_abbreviation == AmountOfSubstanceUnits.KiloMole:
            return """"""
        
        if unit_abbreviation == AmountOfSubstanceUnits.MegaMole:
            return """"""
        
        if unit_abbreviation == AmountOfSubstanceUnits.NanoPoundMole:
            return """"""
        
        if unit_abbreviation == AmountOfSubstanceUnits.MicroPoundMole:
            return """"""
        
        if unit_abbreviation == AmountOfSubstanceUnits.MilliPoundMole:
            return """"""
        
        if unit_abbreviation == AmountOfSubstanceUnits.CentiPoundMole:
            return """"""
        
        if unit_abbreviation == AmountOfSubstanceUnits.DeciPoundMole:
            return """"""
        
        if unit_abbreviation == AmountOfSubstanceUnits.KiloPoundMole:
            return """"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, AmountOfSubstance):
            raise TypeError("unsupported operand type(s) for +: 'AmountOfSubstance' and '{}'".format(type(other).__name__))
        return AmountOfSubstance(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, AmountOfSubstance):
            raise TypeError("unsupported operand type(s) for *: 'AmountOfSubstance' and '{}'".format(type(other).__name__))
        return AmountOfSubstance(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, AmountOfSubstance):
            raise TypeError("unsupported operand type(s) for -: 'AmountOfSubstance' and '{}'".format(type(other).__name__))
        return AmountOfSubstance(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, AmountOfSubstance):
            raise TypeError("unsupported operand type(s) for /: 'AmountOfSubstance' and '{}'".format(type(other).__name__))
        return AmountOfSubstance(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, AmountOfSubstance):
            raise TypeError("unsupported operand type(s) for %: 'AmountOfSubstance' and '{}'".format(type(other).__name__))
        return AmountOfSubstance(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, AmountOfSubstance):
            raise TypeError("unsupported operand type(s) for **: 'AmountOfSubstance' and '{}'".format(type(other).__name__))
        return AmountOfSubstance(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, AmountOfSubstance):
            raise TypeError("unsupported operand type(s) for ==: 'AmountOfSubstance' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, AmountOfSubstance):
            raise TypeError("unsupported operand type(s) for <: 'AmountOfSubstance' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, AmountOfSubstance):
            raise TypeError("unsupported operand type(s) for >: 'AmountOfSubstance' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, AmountOfSubstance):
            raise TypeError("unsupported operand type(s) for <=: 'AmountOfSubstance' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, AmountOfSubstance):
            raise TypeError("unsupported operand type(s) for >=: 'AmountOfSubstance' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value
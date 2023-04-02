from enum import Enum
import math
import string


class MolarMassUnits(Enum):
        """
            MolarMassUnits enumeration
        """
        
        GramPerMole = 'gram_per_mole'
        """
            
        """
        
        KilogramPerKilomole = 'kilogram_per_kilomole'
        """
            
        """
        
        PoundPerMole = 'pound_per_mole'
        """
            
        """
        
        NanoGramPerMole = 'nano_gram_per_mole'
        """
            
        """
        
        MicroGramPerMole = 'micro_gram_per_mole'
        """
            
        """
        
        MilliGramPerMole = 'milli_gram_per_mole'
        """
            
        """
        
        CentiGramPerMole = 'centi_gram_per_mole'
        """
            
        """
        
        DeciGramPerMole = 'deci_gram_per_mole'
        """
            
        """
        
        DecaGramPerMole = 'deca_gram_per_mole'
        """
            
        """
        
        HectoGramPerMole = 'hecto_gram_per_mole'
        """
            
        """
        
        KiloGramPerMole = 'kilo_gram_per_mole'
        """
            
        """
        
        KiloPoundPerMole = 'kilo_pound_per_mole'
        """
            
        """
        
        MegaPoundPerMole = 'mega_pound_per_mole'
        """
            
        """
        
    
class MolarMass:
    """
    In chemistry, the molar mass M is a physical property defined as the mass of a given substance (chemical element or chemical compound) divided by the amount of substance.

    Args:
        value (float): The value.
        from_unit (MolarMassUnits): The MolarMass unit to create from, The default unit is KilogramPerMole
    """
    def __init__(self, value: float, from_unit: MolarMassUnits = MolarMassUnits.KilogramPerMole):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__grams_per_mole = None
        
        self.__kilograms_per_kilomole = None
        
        self.__pounds_per_mole = None
        
        self.__nano_grams_per_mole = None
        
        self.__micro_grams_per_mole = None
        
        self.__milli_grams_per_mole = None
        
        self.__centi_grams_per_mole = None
        
        self.__deci_grams_per_mole = None
        
        self.__deca_grams_per_mole = None
        
        self.__hecto_grams_per_mole = None
        
        self.__kilo_grams_per_mole = None
        
        self.__kilo_pounds_per_mole = None
        
        self.__mega_pounds_per_mole = None
        

    def __convert_from_base(self, from_unit: MolarMassUnits) -> float:
        value = self.__value
        
        if from_unit == MolarMassUnits.GramPerMole:
            return (value * 1e3)
        
        if from_unit == MolarMassUnits.KilogramPerKilomole:
            return (value * 1e3)
        
        if from_unit == MolarMassUnits.PoundPerMole:
            return (value / 0.45359237)
        
        if from_unit == MolarMassUnits.NanoGramPerMole:
            return ((value * 1e3) / 1e-09)
        
        if from_unit == MolarMassUnits.MicroGramPerMole:
            return ((value * 1e3) / 1e-06)
        
        if from_unit == MolarMassUnits.MilliGramPerMole:
            return ((value * 1e3) / 0.001)
        
        if from_unit == MolarMassUnits.CentiGramPerMole:
            return ((value * 1e3) / 0.01)
        
        if from_unit == MolarMassUnits.DeciGramPerMole:
            return ((value * 1e3) / 0.1)
        
        if from_unit == MolarMassUnits.DecaGramPerMole:
            return ((value * 1e3) / 10.0)
        
        if from_unit == MolarMassUnits.HectoGramPerMole:
            return ((value * 1e3) / 100.0)
        
        if from_unit == MolarMassUnits.KiloGramPerMole:
            return ((value * 1e3) / 1000.0)
        
        if from_unit == MolarMassUnits.KiloPoundPerMole:
            return ((value / 0.45359237) / 1000.0)
        
        if from_unit == MolarMassUnits.MegaPoundPerMole:
            return ((value / 0.45359237) / 1000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: MolarMassUnits) -> float:
        
        if to_unit == MolarMassUnits.GramPerMole:
            return (value / 1e3)
        
        if to_unit == MolarMassUnits.KilogramPerKilomole:
            return (value / 1e3)
        
        if to_unit == MolarMassUnits.PoundPerMole:
            return (value * 0.45359237)
        
        if to_unit == MolarMassUnits.NanoGramPerMole:
            return ((value / 1e3) * 1e-09)
        
        if to_unit == MolarMassUnits.MicroGramPerMole:
            return ((value / 1e3) * 1e-06)
        
        if to_unit == MolarMassUnits.MilliGramPerMole:
            return ((value / 1e3) * 0.001)
        
        if to_unit == MolarMassUnits.CentiGramPerMole:
            return ((value / 1e3) * 0.01)
        
        if to_unit == MolarMassUnits.DeciGramPerMole:
            return ((value / 1e3) * 0.1)
        
        if to_unit == MolarMassUnits.DecaGramPerMole:
            return ((value / 1e3) * 10.0)
        
        if to_unit == MolarMassUnits.HectoGramPerMole:
            return ((value / 1e3) * 100.0)
        
        if to_unit == MolarMassUnits.KiloGramPerMole:
            return ((value / 1e3) * 1000.0)
        
        if to_unit == MolarMassUnits.KiloPoundPerMole:
            return ((value * 0.45359237) * 1000.0)
        
        if to_unit == MolarMassUnits.MegaPoundPerMole:
            return ((value * 0.45359237) * 1000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
    @staticmethod
    def from_grams_per_mole(grams_per_mole: float):
        """
        Create a new instance of MolarMass from a value in grams_per_mole.

        

        :param meters: The MolarMass value in grams_per_mole.
        :type grams_per_mole: float
        :return: A new instance of MolarMass.
        :rtype: MolarMass
        """
        return MolarMass(grams_per_mole, MolarMassUnits.GramPerMole)

    
    @staticmethod
    def from_kilograms_per_kilomole(kilograms_per_kilomole: float):
        """
        Create a new instance of MolarMass from a value in kilograms_per_kilomole.

        

        :param meters: The MolarMass value in kilograms_per_kilomole.
        :type kilograms_per_kilomole: float
        :return: A new instance of MolarMass.
        :rtype: MolarMass
        """
        return MolarMass(kilograms_per_kilomole, MolarMassUnits.KilogramPerKilomole)

    
    @staticmethod
    def from_pounds_per_mole(pounds_per_mole: float):
        """
        Create a new instance of MolarMass from a value in pounds_per_mole.

        

        :param meters: The MolarMass value in pounds_per_mole.
        :type pounds_per_mole: float
        :return: A new instance of MolarMass.
        :rtype: MolarMass
        """
        return MolarMass(pounds_per_mole, MolarMassUnits.PoundPerMole)

    
    @staticmethod
    def from_nano_grams_per_mole(nano_grams_per_mole: float):
        """
        Create a new instance of MolarMass from a value in nano_grams_per_mole.

        

        :param meters: The MolarMass value in nano_grams_per_mole.
        :type nano_grams_per_mole: float
        :return: A new instance of MolarMass.
        :rtype: MolarMass
        """
        return MolarMass(nano_grams_per_mole, MolarMassUnits.NanoGramPerMole)

    
    @staticmethod
    def from_micro_grams_per_mole(micro_grams_per_mole: float):
        """
        Create a new instance of MolarMass from a value in micro_grams_per_mole.

        

        :param meters: The MolarMass value in micro_grams_per_mole.
        :type micro_grams_per_mole: float
        :return: A new instance of MolarMass.
        :rtype: MolarMass
        """
        return MolarMass(micro_grams_per_mole, MolarMassUnits.MicroGramPerMole)

    
    @staticmethod
    def from_milli_grams_per_mole(milli_grams_per_mole: float):
        """
        Create a new instance of MolarMass from a value in milli_grams_per_mole.

        

        :param meters: The MolarMass value in milli_grams_per_mole.
        :type milli_grams_per_mole: float
        :return: A new instance of MolarMass.
        :rtype: MolarMass
        """
        return MolarMass(milli_grams_per_mole, MolarMassUnits.MilliGramPerMole)

    
    @staticmethod
    def from_centi_grams_per_mole(centi_grams_per_mole: float):
        """
        Create a new instance of MolarMass from a value in centi_grams_per_mole.

        

        :param meters: The MolarMass value in centi_grams_per_mole.
        :type centi_grams_per_mole: float
        :return: A new instance of MolarMass.
        :rtype: MolarMass
        """
        return MolarMass(centi_grams_per_mole, MolarMassUnits.CentiGramPerMole)

    
    @staticmethod
    def from_deci_grams_per_mole(deci_grams_per_mole: float):
        """
        Create a new instance of MolarMass from a value in deci_grams_per_mole.

        

        :param meters: The MolarMass value in deci_grams_per_mole.
        :type deci_grams_per_mole: float
        :return: A new instance of MolarMass.
        :rtype: MolarMass
        """
        return MolarMass(deci_grams_per_mole, MolarMassUnits.DeciGramPerMole)

    
    @staticmethod
    def from_deca_grams_per_mole(deca_grams_per_mole: float):
        """
        Create a new instance of MolarMass from a value in deca_grams_per_mole.

        

        :param meters: The MolarMass value in deca_grams_per_mole.
        :type deca_grams_per_mole: float
        :return: A new instance of MolarMass.
        :rtype: MolarMass
        """
        return MolarMass(deca_grams_per_mole, MolarMassUnits.DecaGramPerMole)

    
    @staticmethod
    def from_hecto_grams_per_mole(hecto_grams_per_mole: float):
        """
        Create a new instance of MolarMass from a value in hecto_grams_per_mole.

        

        :param meters: The MolarMass value in hecto_grams_per_mole.
        :type hecto_grams_per_mole: float
        :return: A new instance of MolarMass.
        :rtype: MolarMass
        """
        return MolarMass(hecto_grams_per_mole, MolarMassUnits.HectoGramPerMole)

    
    @staticmethod
    def from_kilo_grams_per_mole(kilo_grams_per_mole: float):
        """
        Create a new instance of MolarMass from a value in kilo_grams_per_mole.

        

        :param meters: The MolarMass value in kilo_grams_per_mole.
        :type kilo_grams_per_mole: float
        :return: A new instance of MolarMass.
        :rtype: MolarMass
        """
        return MolarMass(kilo_grams_per_mole, MolarMassUnits.KiloGramPerMole)

    
    @staticmethod
    def from_kilo_pounds_per_mole(kilo_pounds_per_mole: float):
        """
        Create a new instance of MolarMass from a value in kilo_pounds_per_mole.

        

        :param meters: The MolarMass value in kilo_pounds_per_mole.
        :type kilo_pounds_per_mole: float
        :return: A new instance of MolarMass.
        :rtype: MolarMass
        """
        return MolarMass(kilo_pounds_per_mole, MolarMassUnits.KiloPoundPerMole)

    
    @staticmethod
    def from_mega_pounds_per_mole(mega_pounds_per_mole: float):
        """
        Create a new instance of MolarMass from a value in mega_pounds_per_mole.

        

        :param meters: The MolarMass value in mega_pounds_per_mole.
        :type mega_pounds_per_mole: float
        :return: A new instance of MolarMass.
        :rtype: MolarMass
        """
        return MolarMass(mega_pounds_per_mole, MolarMassUnits.MegaPoundPerMole)

    
    @property
    def grams_per_mole(self) -> float:
        """
        
        """
        if self.__grams_per_mole != None:
            return self.__grams_per_mole
        self.__grams_per_mole = self.__convert_from_base(MolarMassUnits.GramPerMole)
        return self.__grams_per_mole

    
    @property
    def kilograms_per_kilomole(self) -> float:
        """
        
        """
        if self.__kilograms_per_kilomole != None:
            return self.__kilograms_per_kilomole
        self.__kilograms_per_kilomole = self.__convert_from_base(MolarMassUnits.KilogramPerKilomole)
        return self.__kilograms_per_kilomole

    
    @property
    def pounds_per_mole(self) -> float:
        """
        
        """
        if self.__pounds_per_mole != None:
            return self.__pounds_per_mole
        self.__pounds_per_mole = self.__convert_from_base(MolarMassUnits.PoundPerMole)
        return self.__pounds_per_mole

    
    @property
    def nano_grams_per_mole(self) -> float:
        """
        
        """
        if self.__nano_grams_per_mole != None:
            return self.__nano_grams_per_mole
        self.__nano_grams_per_mole = self.__convert_from_base(MolarMassUnits.NanoGramPerMole)
        return self.__nano_grams_per_mole

    
    @property
    def micro_grams_per_mole(self) -> float:
        """
        
        """
        if self.__micro_grams_per_mole != None:
            return self.__micro_grams_per_mole
        self.__micro_grams_per_mole = self.__convert_from_base(MolarMassUnits.MicroGramPerMole)
        return self.__micro_grams_per_mole

    
    @property
    def milli_grams_per_mole(self) -> float:
        """
        
        """
        if self.__milli_grams_per_mole != None:
            return self.__milli_grams_per_mole
        self.__milli_grams_per_mole = self.__convert_from_base(MolarMassUnits.MilliGramPerMole)
        return self.__milli_grams_per_mole

    
    @property
    def centi_grams_per_mole(self) -> float:
        """
        
        """
        if self.__centi_grams_per_mole != None:
            return self.__centi_grams_per_mole
        self.__centi_grams_per_mole = self.__convert_from_base(MolarMassUnits.CentiGramPerMole)
        return self.__centi_grams_per_mole

    
    @property
    def deci_grams_per_mole(self) -> float:
        """
        
        """
        if self.__deci_grams_per_mole != None:
            return self.__deci_grams_per_mole
        self.__deci_grams_per_mole = self.__convert_from_base(MolarMassUnits.DeciGramPerMole)
        return self.__deci_grams_per_mole

    
    @property
    def deca_grams_per_mole(self) -> float:
        """
        
        """
        if self.__deca_grams_per_mole != None:
            return self.__deca_grams_per_mole
        self.__deca_grams_per_mole = self.__convert_from_base(MolarMassUnits.DecaGramPerMole)
        return self.__deca_grams_per_mole

    
    @property
    def hecto_grams_per_mole(self) -> float:
        """
        
        """
        if self.__hecto_grams_per_mole != None:
            return self.__hecto_grams_per_mole
        self.__hecto_grams_per_mole = self.__convert_from_base(MolarMassUnits.HectoGramPerMole)
        return self.__hecto_grams_per_mole

    
    @property
    def kilo_grams_per_mole(self) -> float:
        """
        
        """
        if self.__kilo_grams_per_mole != None:
            return self.__kilo_grams_per_mole
        self.__kilo_grams_per_mole = self.__convert_from_base(MolarMassUnits.KiloGramPerMole)
        return self.__kilo_grams_per_mole

    
    @property
    def kilo_pounds_per_mole(self) -> float:
        """
        
        """
        if self.__kilo_pounds_per_mole != None:
            return self.__kilo_pounds_per_mole
        self.__kilo_pounds_per_mole = self.__convert_from_base(MolarMassUnits.KiloPoundPerMole)
        return self.__kilo_pounds_per_mole

    
    @property
    def mega_pounds_per_mole(self) -> float:
        """
        
        """
        if self.__mega_pounds_per_mole != None:
            return self.__mega_pounds_per_mole
        self.__mega_pounds_per_mole = self.__convert_from_base(MolarMassUnits.MegaPoundPerMole)
        return self.__mega_pounds_per_mole

    
    def to_string(self, unit: MolarMassUnits = MolarMassUnits.KilogramPerMole) -> string:
        """
        Format the MolarMass to string.
        Note! the default format for MolarMass is KilogramPerMole.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == MolarMassUnits.GramPerMole:
            return f"""{self.grams_per_mole} g/mol"""
        
        if unit == MolarMassUnits.KilogramPerKilomole:
            return f"""{self.kilograms_per_kilomole} kg/kmol"""
        
        if unit == MolarMassUnits.PoundPerMole:
            return f"""{self.pounds_per_mole} lb/mol"""
        
        if unit == MolarMassUnits.NanoGramPerMole:
            return f"""{self.nano_grams_per_mole} """
        
        if unit == MolarMassUnits.MicroGramPerMole:
            return f"""{self.micro_grams_per_mole} """
        
        if unit == MolarMassUnits.MilliGramPerMole:
            return f"""{self.milli_grams_per_mole} """
        
        if unit == MolarMassUnits.CentiGramPerMole:
            return f"""{self.centi_grams_per_mole} """
        
        if unit == MolarMassUnits.DeciGramPerMole:
            return f"""{self.deci_grams_per_mole} """
        
        if unit == MolarMassUnits.DecaGramPerMole:
            return f"""{self.deca_grams_per_mole} """
        
        if unit == MolarMassUnits.HectoGramPerMole:
            return f"""{self.hecto_grams_per_mole} """
        
        if unit == MolarMassUnits.KiloGramPerMole:
            return f"""{self.kilo_grams_per_mole} """
        
        if unit == MolarMassUnits.KiloPoundPerMole:
            return f"""{self.kilo_pounds_per_mole} """
        
        if unit == MolarMassUnits.MegaPoundPerMole:
            return f"""{self.mega_pounds_per_mole} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: MolarMassUnits = MolarMassUnits.KilogramPerMole) -> string:
        """
        Get MolarMass unit abbreviation.
        Note! the default abbreviation for MolarMass is KilogramPerMole.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == MolarMassUnits.GramPerMole:
            return """g/mol"""
        
        if unit_abbreviation == MolarMassUnits.KilogramPerKilomole:
            return """kg/kmol"""
        
        if unit_abbreviation == MolarMassUnits.PoundPerMole:
            return """lb/mol"""
        
        if unit_abbreviation == MolarMassUnits.NanoGramPerMole:
            return """"""
        
        if unit_abbreviation == MolarMassUnits.MicroGramPerMole:
            return """"""
        
        if unit_abbreviation == MolarMassUnits.MilliGramPerMole:
            return """"""
        
        if unit_abbreviation == MolarMassUnits.CentiGramPerMole:
            return """"""
        
        if unit_abbreviation == MolarMassUnits.DeciGramPerMole:
            return """"""
        
        if unit_abbreviation == MolarMassUnits.DecaGramPerMole:
            return """"""
        
        if unit_abbreviation == MolarMassUnits.HectoGramPerMole:
            return """"""
        
        if unit_abbreviation == MolarMassUnits.KiloGramPerMole:
            return """"""
        
        if unit_abbreviation == MolarMassUnits.KiloPoundPerMole:
            return """"""
        
        if unit_abbreviation == MolarMassUnits.MegaPoundPerMole:
            return """"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, MolarMass):
            raise TypeError("unsupported operand type(s) for +: 'MolarMass' and '{}'".format(type(other).__name__))
        return MolarMass(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, MolarMass):
            raise TypeError("unsupported operand type(s) for *: 'MolarMass' and '{}'".format(type(other).__name__))
        return MolarMass(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, MolarMass):
            raise TypeError("unsupported operand type(s) for -: 'MolarMass' and '{}'".format(type(other).__name__))
        return MolarMass(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, MolarMass):
            raise TypeError("unsupported operand type(s) for /: 'MolarMass' and '{}'".format(type(other).__name__))
        return MolarMass(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, MolarMass):
            raise TypeError("unsupported operand type(s) for %: 'MolarMass' and '{}'".format(type(other).__name__))
        return MolarMass(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, MolarMass):
            raise TypeError("unsupported operand type(s) for **: 'MolarMass' and '{}'".format(type(other).__name__))
        return MolarMass(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, MolarMass):
            raise TypeError("unsupported operand type(s) for ==: 'MolarMass' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, MolarMass):
            raise TypeError("unsupported operand type(s) for <: 'MolarMass' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, MolarMass):
            raise TypeError("unsupported operand type(s) for >: 'MolarMass' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, MolarMass):
            raise TypeError("unsupported operand type(s) for <=: 'MolarMass' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, MolarMass):
            raise TypeError("unsupported operand type(s) for >=: 'MolarMass' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value
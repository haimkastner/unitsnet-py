from enum import Enum
import math
import string


class MolarityUnits(Enum):
        """
            MolarityUnits enumeration
        """
        
        MolePerCubicMeter = 'mole_per_cubic_meter'
        """
            
        """
        
        MolePerLiter = 'mole_per_liter'
        """
            
        """
        
        PoundMolePerCubicFoot = 'pound_mole_per_cubic_foot'
        """
            
        """
        
        KiloMolePerCubicMeter = 'kilo_mole_per_cubic_meter'
        """
            
        """
        
        FemtoMolePerLiter = 'femto_mole_per_liter'
        """
            
        """
        
        PicoMolePerLiter = 'pico_mole_per_liter'
        """
            
        """
        
        NanoMolePerLiter = 'nano_mole_per_liter'
        """
            
        """
        
        MicroMolePerLiter = 'micro_mole_per_liter'
        """
            
        """
        
        MilliMolePerLiter = 'milli_mole_per_liter'
        """
            
        """
        
        CentiMolePerLiter = 'centi_mole_per_liter'
        """
            
        """
        
        DeciMolePerLiter = 'deci_mole_per_liter'
        """
            
        """
        
    
class Molarity:
    """
    Molar concentration, also called molarity, amount concentration or substance concentration, is a measure of the concentration of a solute in a solution, or of any chemical species, in terms of amount of substance in a given volume. 

    Args:
        value (float): The value.
        from_unit (MolarityUnits): The Molarity unit to create from, The default unit is MolePerCubicMeter
    """
    def __init__(self, value: float, from_unit: MolarityUnits = MolarityUnits.MolePerCubicMeter):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__moles_per_cubic_meter = None
        
        self.__moles_per_liter = None
        
        self.__pound_moles_per_cubic_foot = None
        
        self.__kilo_moles_per_cubic_meter = None
        
        self.__femto_moles_per_liter = None
        
        self.__pico_moles_per_liter = None
        
        self.__nano_moles_per_liter = None
        
        self.__micro_moles_per_liter = None
        
        self.__milli_moles_per_liter = None
        
        self.__centi_moles_per_liter = None
        
        self.__deci_moles_per_liter = None
        

    def __convert_from_base(self, from_unit: MolarityUnits) -> float:
        value = self.__value
        
        if from_unit == MolarityUnits.MolePerCubicMeter:
            return (value)
        
        if from_unit == MolarityUnits.MolePerLiter:
            return (value * 1e-3)
        
        if from_unit == MolarityUnits.PoundMolePerCubicFoot:
            return (value * 6.2427960576144611956325455827221e-5)
        
        if from_unit == MolarityUnits.KiloMolePerCubicMeter:
            return ((value) / 1000.0)
        
        if from_unit == MolarityUnits.FemtoMolePerLiter:
            return ((value * 1e-3) / 1e-15)
        
        if from_unit == MolarityUnits.PicoMolePerLiter:
            return ((value * 1e-3) / 1e-12)
        
        if from_unit == MolarityUnits.NanoMolePerLiter:
            return ((value * 1e-3) / 1e-09)
        
        if from_unit == MolarityUnits.MicroMolePerLiter:
            return ((value * 1e-3) / 1e-06)
        
        if from_unit == MolarityUnits.MilliMolePerLiter:
            return ((value * 1e-3) / 0.001)
        
        if from_unit == MolarityUnits.CentiMolePerLiter:
            return ((value * 1e-3) / 0.01)
        
        if from_unit == MolarityUnits.DeciMolePerLiter:
            return ((value * 1e-3) / 0.1)
        
        return None


    def __convert_to_base(self, value: float, to_unit: MolarityUnits) -> float:
        
        if to_unit == MolarityUnits.MolePerCubicMeter:
            return (value)
        
        if to_unit == MolarityUnits.MolePerLiter:
            return (value / 1e-3)
        
        if to_unit == MolarityUnits.PoundMolePerCubicFoot:
            return (value / 6.2427960576144611956325455827221e-5)
        
        if to_unit == MolarityUnits.KiloMolePerCubicMeter:
            return ((value) * 1000.0)
        
        if to_unit == MolarityUnits.FemtoMolePerLiter:
            return ((value / 1e-3) * 1e-15)
        
        if to_unit == MolarityUnits.PicoMolePerLiter:
            return ((value / 1e-3) * 1e-12)
        
        if to_unit == MolarityUnits.NanoMolePerLiter:
            return ((value / 1e-3) * 1e-09)
        
        if to_unit == MolarityUnits.MicroMolePerLiter:
            return ((value / 1e-3) * 1e-06)
        
        if to_unit == MolarityUnits.MilliMolePerLiter:
            return ((value / 1e-3) * 0.001)
        
        if to_unit == MolarityUnits.CentiMolePerLiter:
            return ((value / 1e-3) * 0.01)
        
        if to_unit == MolarityUnits.DeciMolePerLiter:
            return ((value / 1e-3) * 0.1)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
    @staticmethod
    def from_moles_per_cubic_meter(moles_per_cubic_meter: float):
        """
        Create a new instance of Molarity from a value in moles_per_cubic_meter.

        

        :param meters: The Molarity value in moles_per_cubic_meter.
        :type moles_per_cubic_meter: float
        :return: A new instance of Molarity.
        :rtype: Molarity
        """
        return Molarity(moles_per_cubic_meter, MolarityUnits.MolePerCubicMeter)

    
    @staticmethod
    def from_moles_per_liter(moles_per_liter: float):
        """
        Create a new instance of Molarity from a value in moles_per_liter.

        

        :param meters: The Molarity value in moles_per_liter.
        :type moles_per_liter: float
        :return: A new instance of Molarity.
        :rtype: Molarity
        """
        return Molarity(moles_per_liter, MolarityUnits.MolePerLiter)

    
    @staticmethod
    def from_pound_moles_per_cubic_foot(pound_moles_per_cubic_foot: float):
        """
        Create a new instance of Molarity from a value in pound_moles_per_cubic_foot.

        

        :param meters: The Molarity value in pound_moles_per_cubic_foot.
        :type pound_moles_per_cubic_foot: float
        :return: A new instance of Molarity.
        :rtype: Molarity
        """
        return Molarity(pound_moles_per_cubic_foot, MolarityUnits.PoundMolePerCubicFoot)

    
    @staticmethod
    def from_kilo_moles_per_cubic_meter(kilo_moles_per_cubic_meter: float):
        """
        Create a new instance of Molarity from a value in kilo_moles_per_cubic_meter.

        

        :param meters: The Molarity value in kilo_moles_per_cubic_meter.
        :type kilo_moles_per_cubic_meter: float
        :return: A new instance of Molarity.
        :rtype: Molarity
        """
        return Molarity(kilo_moles_per_cubic_meter, MolarityUnits.KiloMolePerCubicMeter)

    
    @staticmethod
    def from_femto_moles_per_liter(femto_moles_per_liter: float):
        """
        Create a new instance of Molarity from a value in femto_moles_per_liter.

        

        :param meters: The Molarity value in femto_moles_per_liter.
        :type femto_moles_per_liter: float
        :return: A new instance of Molarity.
        :rtype: Molarity
        """
        return Molarity(femto_moles_per_liter, MolarityUnits.FemtoMolePerLiter)

    
    @staticmethod
    def from_pico_moles_per_liter(pico_moles_per_liter: float):
        """
        Create a new instance of Molarity from a value in pico_moles_per_liter.

        

        :param meters: The Molarity value in pico_moles_per_liter.
        :type pico_moles_per_liter: float
        :return: A new instance of Molarity.
        :rtype: Molarity
        """
        return Molarity(pico_moles_per_liter, MolarityUnits.PicoMolePerLiter)

    
    @staticmethod
    def from_nano_moles_per_liter(nano_moles_per_liter: float):
        """
        Create a new instance of Molarity from a value in nano_moles_per_liter.

        

        :param meters: The Molarity value in nano_moles_per_liter.
        :type nano_moles_per_liter: float
        :return: A new instance of Molarity.
        :rtype: Molarity
        """
        return Molarity(nano_moles_per_liter, MolarityUnits.NanoMolePerLiter)

    
    @staticmethod
    def from_micro_moles_per_liter(micro_moles_per_liter: float):
        """
        Create a new instance of Molarity from a value in micro_moles_per_liter.

        

        :param meters: The Molarity value in micro_moles_per_liter.
        :type micro_moles_per_liter: float
        :return: A new instance of Molarity.
        :rtype: Molarity
        """
        return Molarity(micro_moles_per_liter, MolarityUnits.MicroMolePerLiter)

    
    @staticmethod
    def from_milli_moles_per_liter(milli_moles_per_liter: float):
        """
        Create a new instance of Molarity from a value in milli_moles_per_liter.

        

        :param meters: The Molarity value in milli_moles_per_liter.
        :type milli_moles_per_liter: float
        :return: A new instance of Molarity.
        :rtype: Molarity
        """
        return Molarity(milli_moles_per_liter, MolarityUnits.MilliMolePerLiter)

    
    @staticmethod
    def from_centi_moles_per_liter(centi_moles_per_liter: float):
        """
        Create a new instance of Molarity from a value in centi_moles_per_liter.

        

        :param meters: The Molarity value in centi_moles_per_liter.
        :type centi_moles_per_liter: float
        :return: A new instance of Molarity.
        :rtype: Molarity
        """
        return Molarity(centi_moles_per_liter, MolarityUnits.CentiMolePerLiter)

    
    @staticmethod
    def from_deci_moles_per_liter(deci_moles_per_liter: float):
        """
        Create a new instance of Molarity from a value in deci_moles_per_liter.

        

        :param meters: The Molarity value in deci_moles_per_liter.
        :type deci_moles_per_liter: float
        :return: A new instance of Molarity.
        :rtype: Molarity
        """
        return Molarity(deci_moles_per_liter, MolarityUnits.DeciMolePerLiter)

    
    @property
    def moles_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__moles_per_cubic_meter != None:
            return self.__moles_per_cubic_meter
        self.__moles_per_cubic_meter = self.__convert_from_base(MolarityUnits.MolePerCubicMeter)
        return self.__moles_per_cubic_meter

    
    @property
    def moles_per_liter(self) -> float:
        """
        
        """
        if self.__moles_per_liter != None:
            return self.__moles_per_liter
        self.__moles_per_liter = self.__convert_from_base(MolarityUnits.MolePerLiter)
        return self.__moles_per_liter

    
    @property
    def pound_moles_per_cubic_foot(self) -> float:
        """
        
        """
        if self.__pound_moles_per_cubic_foot != None:
            return self.__pound_moles_per_cubic_foot
        self.__pound_moles_per_cubic_foot = self.__convert_from_base(MolarityUnits.PoundMolePerCubicFoot)
        return self.__pound_moles_per_cubic_foot

    
    @property
    def kilo_moles_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__kilo_moles_per_cubic_meter != None:
            return self.__kilo_moles_per_cubic_meter
        self.__kilo_moles_per_cubic_meter = self.__convert_from_base(MolarityUnits.KiloMolePerCubicMeter)
        return self.__kilo_moles_per_cubic_meter

    
    @property
    def femto_moles_per_liter(self) -> float:
        """
        
        """
        if self.__femto_moles_per_liter != None:
            return self.__femto_moles_per_liter
        self.__femto_moles_per_liter = self.__convert_from_base(MolarityUnits.FemtoMolePerLiter)
        return self.__femto_moles_per_liter

    
    @property
    def pico_moles_per_liter(self) -> float:
        """
        
        """
        if self.__pico_moles_per_liter != None:
            return self.__pico_moles_per_liter
        self.__pico_moles_per_liter = self.__convert_from_base(MolarityUnits.PicoMolePerLiter)
        return self.__pico_moles_per_liter

    
    @property
    def nano_moles_per_liter(self) -> float:
        """
        
        """
        if self.__nano_moles_per_liter != None:
            return self.__nano_moles_per_liter
        self.__nano_moles_per_liter = self.__convert_from_base(MolarityUnits.NanoMolePerLiter)
        return self.__nano_moles_per_liter

    
    @property
    def micro_moles_per_liter(self) -> float:
        """
        
        """
        if self.__micro_moles_per_liter != None:
            return self.__micro_moles_per_liter
        self.__micro_moles_per_liter = self.__convert_from_base(MolarityUnits.MicroMolePerLiter)
        return self.__micro_moles_per_liter

    
    @property
    def milli_moles_per_liter(self) -> float:
        """
        
        """
        if self.__milli_moles_per_liter != None:
            return self.__milli_moles_per_liter
        self.__milli_moles_per_liter = self.__convert_from_base(MolarityUnits.MilliMolePerLiter)
        return self.__milli_moles_per_liter

    
    @property
    def centi_moles_per_liter(self) -> float:
        """
        
        """
        if self.__centi_moles_per_liter != None:
            return self.__centi_moles_per_liter
        self.__centi_moles_per_liter = self.__convert_from_base(MolarityUnits.CentiMolePerLiter)
        return self.__centi_moles_per_liter

    
    @property
    def deci_moles_per_liter(self) -> float:
        """
        
        """
        if self.__deci_moles_per_liter != None:
            return self.__deci_moles_per_liter
        self.__deci_moles_per_liter = self.__convert_from_base(MolarityUnits.DeciMolePerLiter)
        return self.__deci_moles_per_liter

    
    def to_string(self, unit: MolarityUnits = MolarityUnits.MolePerCubicMeter) -> string:
        """
        Format the Molarity to string.
        Note! the default format for Molarity is MolePerCubicMeter.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == MolarityUnits.MolePerCubicMeter:
            return f"""{self.moles_per_cubic_meter} mol/m³"""
        
        if unit == MolarityUnits.MolePerLiter:
            return f"""{self.moles_per_liter} mol/L"""
        
        if unit == MolarityUnits.PoundMolePerCubicFoot:
            return f"""{self.pound_moles_per_cubic_foot} lbmol/ft³"""
        
        if unit == MolarityUnits.KiloMolePerCubicMeter:
            return f"""{self.kilo_moles_per_cubic_meter} """
        
        if unit == MolarityUnits.FemtoMolePerLiter:
            return f"""{self.femto_moles_per_liter} """
        
        if unit == MolarityUnits.PicoMolePerLiter:
            return f"""{self.pico_moles_per_liter} """
        
        if unit == MolarityUnits.NanoMolePerLiter:
            return f"""{self.nano_moles_per_liter} """
        
        if unit == MolarityUnits.MicroMolePerLiter:
            return f"""{self.micro_moles_per_liter} """
        
        if unit == MolarityUnits.MilliMolePerLiter:
            return f"""{self.milli_moles_per_liter} """
        
        if unit == MolarityUnits.CentiMolePerLiter:
            return f"""{self.centi_moles_per_liter} """
        
        if unit == MolarityUnits.DeciMolePerLiter:
            return f"""{self.deci_moles_per_liter} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: MolarityUnits = MolarityUnits.MolePerCubicMeter) -> string:
        """
        Get Molarity unit abbreviation.
        Note! the default abbreviation for Molarity is MolePerCubicMeter.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == MolarityUnits.MolePerCubicMeter:
            return """mol/m³"""
        
        if unit_abbreviation == MolarityUnits.MolePerLiter:
            return """mol/L"""
        
        if unit_abbreviation == MolarityUnits.PoundMolePerCubicFoot:
            return """lbmol/ft³"""
        
        if unit_abbreviation == MolarityUnits.KiloMolePerCubicMeter:
            return """"""
        
        if unit_abbreviation == MolarityUnits.FemtoMolePerLiter:
            return """"""
        
        if unit_abbreviation == MolarityUnits.PicoMolePerLiter:
            return """"""
        
        if unit_abbreviation == MolarityUnits.NanoMolePerLiter:
            return """"""
        
        if unit_abbreviation == MolarityUnits.MicroMolePerLiter:
            return """"""
        
        if unit_abbreviation == MolarityUnits.MilliMolePerLiter:
            return """"""
        
        if unit_abbreviation == MolarityUnits.CentiMolePerLiter:
            return """"""
        
        if unit_abbreviation == MolarityUnits.DeciMolePerLiter:
            return """"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, Molarity):
            raise TypeError("unsupported operand type(s) for +: 'Molarity' and '{}'".format(type(other).__name__))
        return Molarity(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, Molarity):
            raise TypeError("unsupported operand type(s) for *: 'Molarity' and '{}'".format(type(other).__name__))
        return Molarity(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, Molarity):
            raise TypeError("unsupported operand type(s) for -: 'Molarity' and '{}'".format(type(other).__name__))
        return Molarity(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, Molarity):
            raise TypeError("unsupported operand type(s) for /: 'Molarity' and '{}'".format(type(other).__name__))
        return Molarity(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, Molarity):
            raise TypeError("unsupported operand type(s) for %: 'Molarity' and '{}'".format(type(other).__name__))
        return Molarity(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, Molarity):
            raise TypeError("unsupported operand type(s) for **: 'Molarity' and '{}'".format(type(other).__name__))
        return Molarity(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, Molarity):
            raise TypeError("unsupported operand type(s) for ==: 'Molarity' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, Molarity):
            raise TypeError("unsupported operand type(s) for <: 'Molarity' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, Molarity):
            raise TypeError("unsupported operand type(s) for >: 'Molarity' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, Molarity):
            raise TypeError("unsupported operand type(s) for <=: 'Molarity' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, Molarity):
            raise TypeError("unsupported operand type(s) for >=: 'Molarity' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value
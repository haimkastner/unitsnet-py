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
        
        KilomolePerCubicMeter = 'kilomole_per_cubic_meter'
        """
            
        """
        
        FemtomolePerLiter = 'femtomole_per_liter'
        """
            
        """
        
        PicomolePerLiter = 'picomole_per_liter'
        """
            
        """
        
        NanomolePerLiter = 'nanomole_per_liter'
        """
            
        """
        
        MicromolePerLiter = 'micromole_per_liter'
        """
            
        """
        
        MillimolePerLiter = 'millimole_per_liter'
        """
            
        """
        
        CentimolePerLiter = 'centimole_per_liter'
        """
            
        """
        
        DecimolePerLiter = 'decimole_per_liter'
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
        
        self.__kilomoles_per_cubic_meter = None
        
        self.__femtomoles_per_liter = None
        
        self.__picomoles_per_liter = None
        
        self.__nanomoles_per_liter = None
        
        self.__micromoles_per_liter = None
        
        self.__millimoles_per_liter = None
        
        self.__centimoles_per_liter = None
        
        self.__decimoles_per_liter = None
        

    def __convert_from_base(self, from_unit: MolarityUnits) -> float:
        value = self.__value
        
        if from_unit == MolarityUnits.MolePerCubicMeter:
            return (value)
        
        if from_unit == MolarityUnits.MolePerLiter:
            return (value * 1e-3)
        
        if from_unit == MolarityUnits.PoundMolePerCubicFoot:
            return (value * 6.2427960576144611956325455827221e-5)
        
        if from_unit == MolarityUnits.KilomolePerCubicMeter:
            return ((value) / 1000.0)
        
        if from_unit == MolarityUnits.FemtomolePerLiter:
            return ((value * 1e-3) / 1e-15)
        
        if from_unit == MolarityUnits.PicomolePerLiter:
            return ((value * 1e-3) / 1e-12)
        
        if from_unit == MolarityUnits.NanomolePerLiter:
            return ((value * 1e-3) / 1e-09)
        
        if from_unit == MolarityUnits.MicromolePerLiter:
            return ((value * 1e-3) / 1e-06)
        
        if from_unit == MolarityUnits.MillimolePerLiter:
            return ((value * 1e-3) / 0.001)
        
        if from_unit == MolarityUnits.CentimolePerLiter:
            return ((value * 1e-3) / 0.01)
        
        if from_unit == MolarityUnits.DecimolePerLiter:
            return ((value * 1e-3) / 0.1)
        
        return None


    def __convert_to_base(self, value: float, to_unit: MolarityUnits) -> float:
        
        if to_unit == MolarityUnits.MolePerCubicMeter:
            return (value)
        
        if to_unit == MolarityUnits.MolePerLiter:
            return (value / 1e-3)
        
        if to_unit == MolarityUnits.PoundMolePerCubicFoot:
            return (value / 6.2427960576144611956325455827221e-5)
        
        if to_unit == MolarityUnits.KilomolePerCubicMeter:
            return ((value) * 1000.0)
        
        if to_unit == MolarityUnits.FemtomolePerLiter:
            return ((value / 1e-3) * 1e-15)
        
        if to_unit == MolarityUnits.PicomolePerLiter:
            return ((value / 1e-3) * 1e-12)
        
        if to_unit == MolarityUnits.NanomolePerLiter:
            return ((value / 1e-3) * 1e-09)
        
        if to_unit == MolarityUnits.MicromolePerLiter:
            return ((value / 1e-3) * 1e-06)
        
        if to_unit == MolarityUnits.MillimolePerLiter:
            return ((value / 1e-3) * 0.001)
        
        if to_unit == MolarityUnits.CentimolePerLiter:
            return ((value / 1e-3) * 0.01)
        
        if to_unit == MolarityUnits.DecimolePerLiter:
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
    def from_kilomoles_per_cubic_meter(kilomoles_per_cubic_meter: float):
        """
        Create a new instance of Molarity from a value in kilomoles_per_cubic_meter.

        

        :param meters: The Molarity value in kilomoles_per_cubic_meter.
        :type kilomoles_per_cubic_meter: float
        :return: A new instance of Molarity.
        :rtype: Molarity
        """
        return Molarity(kilomoles_per_cubic_meter, MolarityUnits.KilomolePerCubicMeter)

    
    @staticmethod
    def from_femtomoles_per_liter(femtomoles_per_liter: float):
        """
        Create a new instance of Molarity from a value in femtomoles_per_liter.

        

        :param meters: The Molarity value in femtomoles_per_liter.
        :type femtomoles_per_liter: float
        :return: A new instance of Molarity.
        :rtype: Molarity
        """
        return Molarity(femtomoles_per_liter, MolarityUnits.FemtomolePerLiter)

    
    @staticmethod
    def from_picomoles_per_liter(picomoles_per_liter: float):
        """
        Create a new instance of Molarity from a value in picomoles_per_liter.

        

        :param meters: The Molarity value in picomoles_per_liter.
        :type picomoles_per_liter: float
        :return: A new instance of Molarity.
        :rtype: Molarity
        """
        return Molarity(picomoles_per_liter, MolarityUnits.PicomolePerLiter)

    
    @staticmethod
    def from_nanomoles_per_liter(nanomoles_per_liter: float):
        """
        Create a new instance of Molarity from a value in nanomoles_per_liter.

        

        :param meters: The Molarity value in nanomoles_per_liter.
        :type nanomoles_per_liter: float
        :return: A new instance of Molarity.
        :rtype: Molarity
        """
        return Molarity(nanomoles_per_liter, MolarityUnits.NanomolePerLiter)

    
    @staticmethod
    def from_micromoles_per_liter(micromoles_per_liter: float):
        """
        Create a new instance of Molarity from a value in micromoles_per_liter.

        

        :param meters: The Molarity value in micromoles_per_liter.
        :type micromoles_per_liter: float
        :return: A new instance of Molarity.
        :rtype: Molarity
        """
        return Molarity(micromoles_per_liter, MolarityUnits.MicromolePerLiter)

    
    @staticmethod
    def from_millimoles_per_liter(millimoles_per_liter: float):
        """
        Create a new instance of Molarity from a value in millimoles_per_liter.

        

        :param meters: The Molarity value in millimoles_per_liter.
        :type millimoles_per_liter: float
        :return: A new instance of Molarity.
        :rtype: Molarity
        """
        return Molarity(millimoles_per_liter, MolarityUnits.MillimolePerLiter)

    
    @staticmethod
    def from_centimoles_per_liter(centimoles_per_liter: float):
        """
        Create a new instance of Molarity from a value in centimoles_per_liter.

        

        :param meters: The Molarity value in centimoles_per_liter.
        :type centimoles_per_liter: float
        :return: A new instance of Molarity.
        :rtype: Molarity
        """
        return Molarity(centimoles_per_liter, MolarityUnits.CentimolePerLiter)

    
    @staticmethod
    def from_decimoles_per_liter(decimoles_per_liter: float):
        """
        Create a new instance of Molarity from a value in decimoles_per_liter.

        

        :param meters: The Molarity value in decimoles_per_liter.
        :type decimoles_per_liter: float
        :return: A new instance of Molarity.
        :rtype: Molarity
        """
        return Molarity(decimoles_per_liter, MolarityUnits.DecimolePerLiter)

    
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
    def kilomoles_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__kilomoles_per_cubic_meter != None:
            return self.__kilomoles_per_cubic_meter
        self.__kilomoles_per_cubic_meter = self.__convert_from_base(MolarityUnits.KilomolePerCubicMeter)
        return self.__kilomoles_per_cubic_meter

    
    @property
    def femtomoles_per_liter(self) -> float:
        """
        
        """
        if self.__femtomoles_per_liter != None:
            return self.__femtomoles_per_liter
        self.__femtomoles_per_liter = self.__convert_from_base(MolarityUnits.FemtomolePerLiter)
        return self.__femtomoles_per_liter

    
    @property
    def picomoles_per_liter(self) -> float:
        """
        
        """
        if self.__picomoles_per_liter != None:
            return self.__picomoles_per_liter
        self.__picomoles_per_liter = self.__convert_from_base(MolarityUnits.PicomolePerLiter)
        return self.__picomoles_per_liter

    
    @property
    def nanomoles_per_liter(self) -> float:
        """
        
        """
        if self.__nanomoles_per_liter != None:
            return self.__nanomoles_per_liter
        self.__nanomoles_per_liter = self.__convert_from_base(MolarityUnits.NanomolePerLiter)
        return self.__nanomoles_per_liter

    
    @property
    def micromoles_per_liter(self) -> float:
        """
        
        """
        if self.__micromoles_per_liter != None:
            return self.__micromoles_per_liter
        self.__micromoles_per_liter = self.__convert_from_base(MolarityUnits.MicromolePerLiter)
        return self.__micromoles_per_liter

    
    @property
    def millimoles_per_liter(self) -> float:
        """
        
        """
        if self.__millimoles_per_liter != None:
            return self.__millimoles_per_liter
        self.__millimoles_per_liter = self.__convert_from_base(MolarityUnits.MillimolePerLiter)
        return self.__millimoles_per_liter

    
    @property
    def centimoles_per_liter(self) -> float:
        """
        
        """
        if self.__centimoles_per_liter != None:
            return self.__centimoles_per_liter
        self.__centimoles_per_liter = self.__convert_from_base(MolarityUnits.CentimolePerLiter)
        return self.__centimoles_per_liter

    
    @property
    def decimoles_per_liter(self) -> float:
        """
        
        """
        if self.__decimoles_per_liter != None:
            return self.__decimoles_per_liter
        self.__decimoles_per_liter = self.__convert_from_base(MolarityUnits.DecimolePerLiter)
        return self.__decimoles_per_liter

    
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
        
        if unit == MolarityUnits.KilomolePerCubicMeter:
            return f"""{self.kilomoles_per_cubic_meter} """
        
        if unit == MolarityUnits.FemtomolePerLiter:
            return f"""{self.femtomoles_per_liter} """
        
        if unit == MolarityUnits.PicomolePerLiter:
            return f"""{self.picomoles_per_liter} """
        
        if unit == MolarityUnits.NanomolePerLiter:
            return f"""{self.nanomoles_per_liter} """
        
        if unit == MolarityUnits.MicromolePerLiter:
            return f"""{self.micromoles_per_liter} """
        
        if unit == MolarityUnits.MillimolePerLiter:
            return f"""{self.millimoles_per_liter} """
        
        if unit == MolarityUnits.CentimolePerLiter:
            return f"""{self.centimoles_per_liter} """
        
        if unit == MolarityUnits.DecimolePerLiter:
            return f"""{self.decimoles_per_liter} """
        
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
        
        if unit_abbreviation == MolarityUnits.KilomolePerCubicMeter:
            return """"""
        
        if unit_abbreviation == MolarityUnits.FemtomolePerLiter:
            return """"""
        
        if unit_abbreviation == MolarityUnits.PicomolePerLiter:
            return """"""
        
        if unit_abbreviation == MolarityUnits.NanomolePerLiter:
            return """"""
        
        if unit_abbreviation == MolarityUnits.MicromolePerLiter:
            return """"""
        
        if unit_abbreviation == MolarityUnits.MillimolePerLiter:
            return """"""
        
        if unit_abbreviation == MolarityUnits.CentimolePerLiter:
            return """"""
        
        if unit_abbreviation == MolarityUnits.DecimolePerLiter:
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
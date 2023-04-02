from enum import Enum
import math
import string


class MolarEntropyUnits(Enum):
        """
            MolarEntropyUnits enumeration
        """
        
        JoulePerMoleKelvin = 'joule_per_mole_kelvin'
        """
            
        """
        
        KilojoulePerMoleKelvin = 'kilojoule_per_mole_kelvin'
        """
            
        """
        
        MegajoulePerMoleKelvin = 'megajoule_per_mole_kelvin'
        """
            
        """
        

class MolarEntropy:
    """
    Molar entropy is amount of energy required to increase temperature of 1 mole substance by 1 Kelvin.

    Args:
        value (float): The value.
        from_unit (MolarEntropyUnits): The MolarEntropy unit to create from, The default unit is JoulePerMoleKelvin
    """
    def __init__(self, value: float, from_unit: MolarEntropyUnits = MolarEntropyUnits.JoulePerMoleKelvin):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__joules_per_mole_kelvin = None
        
        self.__kilojoules_per_mole_kelvin = None
        
        self.__megajoules_per_mole_kelvin = None
        

    def __convert_from_base(self, from_unit: MolarEntropyUnits) -> float:
        value = self.__value
        
        if from_unit == MolarEntropyUnits.JoulePerMoleKelvin:
            return (value)
        
        if from_unit == MolarEntropyUnits.KilojoulePerMoleKelvin:
            return ((value) / 1000.0)
        
        if from_unit == MolarEntropyUnits.MegajoulePerMoleKelvin:
            return ((value) / 1000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: MolarEntropyUnits) -> float:
        
        if to_unit == MolarEntropyUnits.JoulePerMoleKelvin:
            return (value)
        
        if to_unit == MolarEntropyUnits.KilojoulePerMoleKelvin:
            return ((value) * 1000.0)
        
        if to_unit == MolarEntropyUnits.MegajoulePerMoleKelvin:
            return ((value) * 1000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
    @staticmethod
    def from_joules_per_mole_kelvin(joules_per_mole_kelvin: float):
        """
        Create a new instance of MolarEntropy from a value in joules_per_mole_kelvin.

        

        :param meters: The MolarEntropy value in joules_per_mole_kelvin.
        :type joules_per_mole_kelvin: float
        :return: A new instance of MolarEntropy.
        :rtype: MolarEntropy
        """
        return MolarEntropy(joules_per_mole_kelvin, MolarEntropyUnits.JoulePerMoleKelvin)

    
    @staticmethod
    def from_kilojoules_per_mole_kelvin(kilojoules_per_mole_kelvin: float):
        """
        Create a new instance of MolarEntropy from a value in kilojoules_per_mole_kelvin.

        

        :param meters: The MolarEntropy value in kilojoules_per_mole_kelvin.
        :type kilojoules_per_mole_kelvin: float
        :return: A new instance of MolarEntropy.
        :rtype: MolarEntropy
        """
        return MolarEntropy(kilojoules_per_mole_kelvin, MolarEntropyUnits.KilojoulePerMoleKelvin)

    
    @staticmethod
    def from_megajoules_per_mole_kelvin(megajoules_per_mole_kelvin: float):
        """
        Create a new instance of MolarEntropy from a value in megajoules_per_mole_kelvin.

        

        :param meters: The MolarEntropy value in megajoules_per_mole_kelvin.
        :type megajoules_per_mole_kelvin: float
        :return: A new instance of MolarEntropy.
        :rtype: MolarEntropy
        """
        return MolarEntropy(megajoules_per_mole_kelvin, MolarEntropyUnits.MegajoulePerMoleKelvin)

    
    @property
    def joules_per_mole_kelvin(self) -> float:
        """
        
        """
        if self.__joules_per_mole_kelvin != None:
            return self.__joules_per_mole_kelvin
        self.__joules_per_mole_kelvin = self.__convert_from_base(MolarEntropyUnits.JoulePerMoleKelvin)
        return self.__joules_per_mole_kelvin

    
    @property
    def kilojoules_per_mole_kelvin(self) -> float:
        """
        
        """
        if self.__kilojoules_per_mole_kelvin != None:
            return self.__kilojoules_per_mole_kelvin
        self.__kilojoules_per_mole_kelvin = self.__convert_from_base(MolarEntropyUnits.KilojoulePerMoleKelvin)
        return self.__kilojoules_per_mole_kelvin

    
    @property
    def megajoules_per_mole_kelvin(self) -> float:
        """
        
        """
        if self.__megajoules_per_mole_kelvin != None:
            return self.__megajoules_per_mole_kelvin
        self.__megajoules_per_mole_kelvin = self.__convert_from_base(MolarEntropyUnits.MegajoulePerMoleKelvin)
        return self.__megajoules_per_mole_kelvin

    
    def to_string(self, unit: MolarEntropyUnits = MolarEntropyUnits.JoulePerMoleKelvin) -> string:
        """
        Format the MolarEntropy to string.
        Note! the default format for MolarEntropy is JoulePerMoleKelvin.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == MolarEntropyUnits.JoulePerMoleKelvin:
            return f"""{self.joules_per_mole_kelvin} J/(mol*K)"""
        
        if unit == MolarEntropyUnits.KilojoulePerMoleKelvin:
            return f"""{self.kilojoules_per_mole_kelvin} """
        
        if unit == MolarEntropyUnits.MegajoulePerMoleKelvin:
            return f"""{self.megajoules_per_mole_kelvin} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: MolarEntropyUnits = MolarEntropyUnits.JoulePerMoleKelvin) -> string:
        """
        Get MolarEntropy unit abbreviation.
        Note! the default abbreviation for MolarEntropy is JoulePerMoleKelvin.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == MolarEntropyUnits.JoulePerMoleKelvin:
            return """J/(mol*K)"""
        
        if unit_abbreviation == MolarEntropyUnits.KilojoulePerMoleKelvin:
            return """"""
        
        if unit_abbreviation == MolarEntropyUnits.MegajoulePerMoleKelvin:
            return """"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, MolarEntropy):
            raise TypeError("unsupported operand type(s) for +: 'MolarEntropy' and '{}'".format(type(other).__name__))
        return MolarEntropy(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, MolarEntropy):
            raise TypeError("unsupported operand type(s) for *: 'MolarEntropy' and '{}'".format(type(other).__name__))
        return MolarEntropy(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, MolarEntropy):
            raise TypeError("unsupported operand type(s) for -: 'MolarEntropy' and '{}'".format(type(other).__name__))
        return MolarEntropy(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, MolarEntropy):
            raise TypeError("unsupported operand type(s) for /: 'MolarEntropy' and '{}'".format(type(other).__name__))
        return MolarEntropy(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, MolarEntropy):
            raise TypeError("unsupported operand type(s) for %: 'MolarEntropy' and '{}'".format(type(other).__name__))
        return MolarEntropy(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, MolarEntropy):
            raise TypeError("unsupported operand type(s) for **: 'MolarEntropy' and '{}'".format(type(other).__name__))
        return MolarEntropy(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, MolarEntropy):
            raise TypeError("unsupported operand type(s) for ==: 'MolarEntropy' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, MolarEntropy):
            raise TypeError("unsupported operand type(s) for <: 'MolarEntropy' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, MolarEntropy):
            raise TypeError("unsupported operand type(s) for >: 'MolarEntropy' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, MolarEntropy):
            raise TypeError("unsupported operand type(s) for <=: 'MolarEntropy' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, MolarEntropy):
            raise TypeError("unsupported operand type(s) for >=: 'MolarEntropy' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value
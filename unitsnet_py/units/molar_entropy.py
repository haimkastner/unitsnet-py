from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



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
        

class MolarEntropy(AbstractMeasure):
    """
    Molar entropy is amount of energy required to increase temperature of 1 mole substance by 1 Kelvin.

    Args:
        value (float): The value.
        from_unit (MolarEntropyUnits): The MolarEntropy unit to create from, The default unit is JoulePerMoleKelvin
    """
    def __init__(self, value: float, from_unit: MolarEntropyUnits = MolarEntropyUnits.JoulePerMoleKelvin):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__joules_per_mole_kelvin = None
        
        self.__kilojoules_per_mole_kelvin = None
        
        self.__megajoules_per_mole_kelvin = None
        

    def convert(self, unit: MolarEntropyUnits) -> float:
        return self.__convert_from_base(unit)

    def __convert_from_base(self, from_unit: MolarEntropyUnits) -> float:
        value = self._value
        
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
        return self._value

    
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

    
    def to_string(self, unit: MolarEntropyUnits = MolarEntropyUnits.JoulePerMoleKelvin) -> str:
        """
        Format the MolarEntropy to string.
        Note! the default format for MolarEntropy is JoulePerMoleKelvin.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == MolarEntropyUnits.JoulePerMoleKelvin:
            return f"""{self.joules_per_mole_kelvin} J/(mol*K)"""
        
        if unit == MolarEntropyUnits.KilojoulePerMoleKelvin:
            return f"""{self.kilojoules_per_mole_kelvin} kJ/(mol*K)"""
        
        if unit == MolarEntropyUnits.MegajoulePerMoleKelvin:
            return f"""{self.megajoules_per_mole_kelvin} MJ/(mol*K)"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: MolarEntropyUnits = MolarEntropyUnits.JoulePerMoleKelvin) -> str:
        """
        Get MolarEntropy unit abbreviation.
        Note! the default abbreviation for MolarEntropy is JoulePerMoleKelvin.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == MolarEntropyUnits.JoulePerMoleKelvin:
            return """J/(mol*K)"""
        
        if unit_abbreviation == MolarEntropyUnits.KilojoulePerMoleKelvin:
            return """kJ/(mol*K)"""
        
        if unit_abbreviation == MolarEntropyUnits.MegajoulePerMoleKelvin:
            return """MJ/(mol*K)"""
        
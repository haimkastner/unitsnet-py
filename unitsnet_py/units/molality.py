from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class MolalityUnits(Enum):
        """
            MolalityUnits enumeration
        """
        
        MolePerKilogram = 'mole_per_kilogram'
        """
            
        """
        
        MolePerGram = 'mole_per_gram'
        """
            
        """
        

class Molality(AbstractMeasure):
    """
    Molality is a measure of the amount of solute in a solution relative to a given mass of solvent.

    Args:
        value (float): The value.
        from_unit (MolalityUnits): The Molality unit to create from, The default unit is MolePerKilogram
    """
    def __init__(self, value: float, from_unit: MolalityUnits = MolalityUnits.MolePerKilogram):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__moles_per_kilogram = None
        
        self.__moles_per_gram = None
        

    def convert(self, unit: MolalityUnits) -> float:
        return self.__convert_from_base(unit)

    def __convert_from_base(self, from_unit: MolalityUnits) -> float:
        value = self._value
        
        if from_unit == MolalityUnits.MolePerKilogram:
            return (value)
        
        if from_unit == MolalityUnits.MolePerGram:
            return (value * 1e-3)
        
        return None


    def __convert_to_base(self, value: float, to_unit: MolalityUnits) -> float:
        
        if to_unit == MolalityUnits.MolePerKilogram:
            return (value)
        
        if to_unit == MolalityUnits.MolePerGram:
            return (value / 1e-3)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_moles_per_kilogram(moles_per_kilogram: float):
        """
        Create a new instance of Molality from a value in moles_per_kilogram.

        

        :param meters: The Molality value in moles_per_kilogram.
        :type moles_per_kilogram: float
        :return: A new instance of Molality.
        :rtype: Molality
        """
        return Molality(moles_per_kilogram, MolalityUnits.MolePerKilogram)

    
    @staticmethod
    def from_moles_per_gram(moles_per_gram: float):
        """
        Create a new instance of Molality from a value in moles_per_gram.

        

        :param meters: The Molality value in moles_per_gram.
        :type moles_per_gram: float
        :return: A new instance of Molality.
        :rtype: Molality
        """
        return Molality(moles_per_gram, MolalityUnits.MolePerGram)

    
    @property
    def moles_per_kilogram(self) -> float:
        """
        
        """
        if self.__moles_per_kilogram != None:
            return self.__moles_per_kilogram
        self.__moles_per_kilogram = self.__convert_from_base(MolalityUnits.MolePerKilogram)
        return self.__moles_per_kilogram

    
    @property
    def moles_per_gram(self) -> float:
        """
        
        """
        if self.__moles_per_gram != None:
            return self.__moles_per_gram
        self.__moles_per_gram = self.__convert_from_base(MolalityUnits.MolePerGram)
        return self.__moles_per_gram

    
    def to_string(self, unit: MolalityUnits = MolalityUnits.MolePerKilogram) -> str:
        """
        Format the Molality to string.
        Note! the default format for Molality is MolePerKilogram.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == MolalityUnits.MolePerKilogram:
            return f"""{self.moles_per_kilogram} mol/kg"""
        
        if unit == MolalityUnits.MolePerGram:
            return f"""{self.moles_per_gram} mol/g"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: MolalityUnits = MolalityUnits.MolePerKilogram) -> str:
        """
        Get Molality unit abbreviation.
        Note! the default abbreviation for Molality is MolePerKilogram.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == MolalityUnits.MolePerKilogram:
            return """mol/kg"""
        
        if unit_abbreviation == MolalityUnits.MolePerGram:
            return """mol/g"""
        
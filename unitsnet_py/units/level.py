from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class LevelUnits(Enum):
        """
            LevelUnits enumeration
        """
        
        Decibel = 'decibel'
        """
            
        """
        
        Neper = 'neper'
        """
            
        """
        

class Level(AbstractMeasure):
    """
    Level is the logarithm of the ratio of a quantity Q to a reference value of that quantity, Q₀, expressed in dimensionless units.

    Args:
        value (float): The value.
        from_unit (LevelUnits): The Level unit to create from, The default unit is Decibel
    """
    def __init__(self, value: float, from_unit: LevelUnits = LevelUnits.Decibel):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__decibels = None
        
        self.__nepers = None
        

    def convert(self, unit: LevelUnits) -> float:
        return self.__convert_from_base(unit)

    def __convert_from_base(self, from_unit: LevelUnits) -> float:
        value = self._value
        
        if from_unit == LevelUnits.Decibel:
            return (value)
        
        if from_unit == LevelUnits.Neper:
            return (0.115129254 * value)
        
        return None


    def __convert_to_base(self, value: float, to_unit: LevelUnits) -> float:
        
        if to_unit == LevelUnits.Decibel:
            return (value)
        
        if to_unit == LevelUnits.Neper:
            return ((1 / 0.115129254) * value)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_decibels(decibels: float):
        """
        Create a new instance of Level from a value in decibels.

        

        :param meters: The Level value in decibels.
        :type decibels: float
        :return: A new instance of Level.
        :rtype: Level
        """
        return Level(decibels, LevelUnits.Decibel)

    
    @staticmethod
    def from_nepers(nepers: float):
        """
        Create a new instance of Level from a value in nepers.

        

        :param meters: The Level value in nepers.
        :type nepers: float
        :return: A new instance of Level.
        :rtype: Level
        """
        return Level(nepers, LevelUnits.Neper)

    
    @property
    def decibels(self) -> float:
        """
        
        """
        if self.__decibels != None:
            return self.__decibels
        self.__decibels = self.__convert_from_base(LevelUnits.Decibel)
        return self.__decibels

    
    @property
    def nepers(self) -> float:
        """
        
        """
        if self.__nepers != None:
            return self.__nepers
        self.__nepers = self.__convert_from_base(LevelUnits.Neper)
        return self.__nepers

    
    def to_string(self, unit: LevelUnits = LevelUnits.Decibel) -> str:
        """
        Format the Level to string.
        Note! the default format for Level is Decibel.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == LevelUnits.Decibel:
            return f"""{self.decibels} dB"""
        
        if unit == LevelUnits.Neper:
            return f"""{self.nepers} Np"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: LevelUnits = LevelUnits.Decibel) -> str:
        """
        Get Level unit abbreviation.
        Note! the default abbreviation for Level is Decibel.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == LevelUnits.Decibel:
            return """dB"""
        
        if unit_abbreviation == LevelUnits.Neper:
            return """Np"""
        
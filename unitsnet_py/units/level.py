from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class LevelUnits(Enum):
        """
            LevelUnits enumeration
        """
        
        Decibel = 'Decibel'
        """
            
        """
        
        Neper = 'Neper'
        """
            
        """
        

class LevelDto:
    """
    A DTO representation of a Level

    Attributes:
        value (float): The value of the Level.
        unit (LevelUnits): The specific unit that the Level value is representing.
    """

    def __init__(self, value: float, unit: LevelUnits):
        """
        Create a new DTO representation of a Level

        Parameters:
            value (float): The value of the Level.
            unit (LevelUnits): The specific unit that the Level value is representing.
        """
        self.value: float = value
        """
        The value of the Level
        """
        self.unit: LevelUnits = unit
        """
        The specific unit that the Level value is representing
        """

    def to_json(self):
        """
        Get a Level DTO JSON object representing the current unit.

        :return: JSON object represents Level DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "Decibel"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of Level DTO from a json representation.

        :param data: The Level DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "Decibel"}
        :return: A new instance of LevelDto.
        :rtype: LevelDto
        """
        return LevelDto(value=data["value"], unit=LevelUnits(data["unit"]))


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

    def to_dto(self, hold_in_unit: LevelUnits = LevelUnits.Decibel) -> LevelDto:
        """
        Get a new instance of Level DTO representing the current unit.

        :param hold_in_unit: The specific Level unit to store the Level value in the DTO representation.
        :type hold_in_unit: LevelUnits
        :return: A new instance of LevelDto.
        :rtype: LevelDto
        """
        return LevelDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: LevelUnits = LevelUnits.Decibel):
        """
        Get a Level DTO JSON object representing the current unit.

        :param hold_in_unit: The specific Level unit to store the Level value in the DTO representation.
        :type hold_in_unit: LevelUnits
        :return: JSON object represents Level DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "Decibel"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(level_dto: LevelDto):
        """
        Obtain a new instance of Level from a DTO unit object.

        :param level_dto: The Level DTO representation.
        :type level_dto: LevelDto
        :return: A new instance of Level.
        :rtype: Level
        """
        return Level(level_dto.value, level_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of Level from a DTO unit json representation.

        :param data: The Level DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "Decibel"}
        :return: A new instance of Level.
        :rtype: Level
        """
        return Level.from_dto(LevelDto.from_json(data))

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

    
    def to_string(self, unit: LevelUnits = LevelUnits.Decibel, fractional_digits: int = None) -> str:
        """
        Format the Level to a string.
        
        Note: the default format for Level is Decibel.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the Level. Default is 'Decibel'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == LevelUnits.Decibel:
            return f"""{super()._truncate_fraction_digits(self.decibels, fractional_digits)} dB"""
        
        if unit == LevelUnits.Neper:
            return f"""{super()._truncate_fraction_digits(self.nepers, fractional_digits)} Np"""
        
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
        
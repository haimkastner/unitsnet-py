from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class MolalityUnits(Enum):
        """
            MolalityUnits enumeration
        """
        
        MolePerKilogram = 'MolePerKilogram'
        """
            
        """
        
        MolePerGram = 'MolePerGram'
        """
            
        """
        
        MillimolePerKilogram = 'MillimolePerKilogram'
        """
            
        """
        

class MolalityDto:
    """
    A DTO representation of a Molality

    Attributes:
        value (float): The value of the Molality.
        unit (MolalityUnits): The specific unit that the Molality value is representing.
    """

    def __init__(self, value: float, unit: MolalityUnits):
        """
        Create a new DTO representation of a Molality

        Parameters:
            value (float): The value of the Molality.
            unit (MolalityUnits): The specific unit that the Molality value is representing.
        """
        self.value: float = value
        """
        The value of the Molality
        """
        self.unit: MolalityUnits = unit
        """
        The specific unit that the Molality value is representing
        """

    def to_json(self):
        """
        Get a Molality DTO JSON object representing the current unit.

        :return: JSON object represents Molality DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "MolePerKilogram"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of Molality DTO from a json representation.

        :param data: The Molality DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "MolePerKilogram"}
        :return: A new instance of MolalityDto.
        :rtype: MolalityDto
        """
        return MolalityDto(value=data["value"], unit=MolalityUnits(data["unit"]))


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
        
        self.__millimoles_per_kilogram = None
        

    def convert(self, unit: MolalityUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: MolalityUnits = MolalityUnits.MolePerKilogram) -> MolalityDto:
        """
        Get a new instance of Molality DTO representing the current unit.

        :param hold_in_unit: The specific Molality unit to store the Molality value in the DTO representation.
        :type hold_in_unit: MolalityUnits
        :return: A new instance of MolalityDto.
        :rtype: MolalityDto
        """
        return MolalityDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: MolalityUnits = MolalityUnits.MolePerKilogram):
        """
        Get a Molality DTO JSON object representing the current unit.

        :param hold_in_unit: The specific Molality unit to store the Molality value in the DTO representation.
        :type hold_in_unit: MolalityUnits
        :return: JSON object represents Molality DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "MolePerKilogram"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(molality_dto: MolalityDto):
        """
        Obtain a new instance of Molality from a DTO unit object.

        :param molality_dto: The Molality DTO representation.
        :type molality_dto: MolalityDto
        :return: A new instance of Molality.
        :rtype: Molality
        """
        return Molality(molality_dto.value, molality_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of Molality from a DTO unit json representation.

        :param data: The Molality DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "MolePerKilogram"}
        :return: A new instance of Molality.
        :rtype: Molality
        """
        return Molality.from_dto(MolalityDto.from_json(data))

    def __convert_from_base(self, from_unit: MolalityUnits) -> float:
        value = self._value
        
        if from_unit == MolalityUnits.MolePerKilogram:
            return (value)
        
        if from_unit == MolalityUnits.MolePerGram:
            return (value * 1e-3)
        
        if from_unit == MolalityUnits.MillimolePerKilogram:
            return ((value) / 0.001)
        
        return None


    def __convert_to_base(self, value: float, to_unit: MolalityUnits) -> float:
        
        if to_unit == MolalityUnits.MolePerKilogram:
            return (value)
        
        if to_unit == MolalityUnits.MolePerGram:
            return (value / 1e-3)
        
        if to_unit == MolalityUnits.MillimolePerKilogram:
            return ((value) * 0.001)
        
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

    
    @staticmethod
    def from_millimoles_per_kilogram(millimoles_per_kilogram: float):
        """
        Create a new instance of Molality from a value in millimoles_per_kilogram.

        

        :param meters: The Molality value in millimoles_per_kilogram.
        :type millimoles_per_kilogram: float
        :return: A new instance of Molality.
        :rtype: Molality
        """
        return Molality(millimoles_per_kilogram, MolalityUnits.MillimolePerKilogram)

    
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

    
    @property
    def millimoles_per_kilogram(self) -> float:
        """
        
        """
        if self.__millimoles_per_kilogram != None:
            return self.__millimoles_per_kilogram
        self.__millimoles_per_kilogram = self.__convert_from_base(MolalityUnits.MillimolePerKilogram)
        return self.__millimoles_per_kilogram

    
    def to_string(self, unit: MolalityUnits = MolalityUnits.MolePerKilogram, fractional_digits: int = None) -> str:
        """
        Format the Molality to a string.
        
        Note: the default format for Molality is MolePerKilogram.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the Molality. Default is 'MolePerKilogram'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == MolalityUnits.MolePerKilogram:
            return f"""{super()._truncate_fraction_digits(self.moles_per_kilogram, fractional_digits)} mol/kg"""
        
        if unit == MolalityUnits.MolePerGram:
            return f"""{super()._truncate_fraction_digits(self.moles_per_gram, fractional_digits)} mol/g"""
        
        if unit == MolalityUnits.MillimolePerKilogram:
            return f"""{super()._truncate_fraction_digits(self.millimoles_per_kilogram, fractional_digits)} mmol/kg"""
        
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
        
        if unit_abbreviation == MolalityUnits.MillimolePerKilogram:
            return """mmol/kg"""
        
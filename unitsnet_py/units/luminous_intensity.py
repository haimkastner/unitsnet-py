from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class LuminousIntensityUnits(Enum):
        """
            LuminousIntensityUnits enumeration
        """
        
        Candela = 'Candela'
        """
            
        """
        

class LuminousIntensityDto:
    """
    A DTO representation of a LuminousIntensity

    Attributes:
        value (float): The value of the LuminousIntensity.
        unit (LuminousIntensityUnits): The specific unit that the LuminousIntensity value is representing.
    """

    def __init__(self, value: float, unit: LuminousIntensityUnits):
        """
        Create a new DTO representation of a LuminousIntensity

        Parameters:
            value (float): The value of the LuminousIntensity.
            unit (LuminousIntensityUnits): The specific unit that the LuminousIntensity value is representing.
        """
        self.value: float = value
        """
        The value of the LuminousIntensity
        """
        self.unit: LuminousIntensityUnits = unit
        """
        The specific unit that the LuminousIntensity value is representing
        """

    def to_json(self):
        """
        Get a LuminousIntensity DTO JSON object representing the current unit.

        :return: JSON object represents LuminousIntensity DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "Candela"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of LuminousIntensity DTO from a json representation.

        :param data: The LuminousIntensity DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "Candela"}
        :return: A new instance of LuminousIntensityDto.
        :rtype: LuminousIntensityDto
        """
        return LuminousIntensityDto(value=data["value"], unit=LuminousIntensityUnits(data["unit"]))


class LuminousIntensity(AbstractMeasure):
    """
    In photometry, luminous intensity is a measure of the wavelength-weighted power emitted by a light source in a particular direction per unit solid angle, based on the luminosity function, a standardized model of the sensitivity of the human eye.

    Args:
        value (float): The value.
        from_unit (LuminousIntensityUnits): The LuminousIntensity unit to create from, The default unit is Candela
    """
    def __init__(self, value: float, from_unit: LuminousIntensityUnits = LuminousIntensityUnits.Candela):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__candela = None
        

    def convert(self, unit: LuminousIntensityUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: LuminousIntensityUnits = LuminousIntensityUnits.Candela) -> LuminousIntensityDto:
        """
        Get a new instance of LuminousIntensity DTO representing the current unit.

        :param hold_in_unit: The specific LuminousIntensity unit to store the LuminousIntensity value in the DTO representation.
        :type hold_in_unit: LuminousIntensityUnits
        :return: A new instance of LuminousIntensityDto.
        :rtype: LuminousIntensityDto
        """
        return LuminousIntensityDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: LuminousIntensityUnits = LuminousIntensityUnits.Candela):
        """
        Get a LuminousIntensity DTO JSON object representing the current unit.

        :param hold_in_unit: The specific LuminousIntensity unit to store the LuminousIntensity value in the DTO representation.
        :type hold_in_unit: LuminousIntensityUnits
        :return: JSON object represents LuminousIntensity DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "Candela"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(luminous_intensity_dto: LuminousIntensityDto):
        """
        Obtain a new instance of LuminousIntensity from a DTO unit object.

        :param luminous_intensity_dto: The LuminousIntensity DTO representation.
        :type luminous_intensity_dto: LuminousIntensityDto
        :return: A new instance of LuminousIntensity.
        :rtype: LuminousIntensity
        """
        return LuminousIntensity(luminous_intensity_dto.value, luminous_intensity_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of LuminousIntensity from a DTO unit json representation.

        :param data: The LuminousIntensity DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "Candela"}
        :return: A new instance of LuminousIntensity.
        :rtype: LuminousIntensity
        """
        return LuminousIntensity.from_dto(LuminousIntensityDto.from_json(data))

    def __convert_from_base(self, from_unit: LuminousIntensityUnits) -> float:
        value = self._value
        
        if from_unit == LuminousIntensityUnits.Candela:
            return (value)
        
        return None


    def __convert_to_base(self, value: float, to_unit: LuminousIntensityUnits) -> float:
        
        if to_unit == LuminousIntensityUnits.Candela:
            return (value)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_candela(candela: float):
        """
        Create a new instance of LuminousIntensity from a value in candela.

        

        :param meters: The LuminousIntensity value in candela.
        :type candela: float
        :return: A new instance of LuminousIntensity.
        :rtype: LuminousIntensity
        """
        return LuminousIntensity(candela, LuminousIntensityUnits.Candela)

    
    @property
    def candela(self) -> float:
        """
        
        """
        if self.__candela != None:
            return self.__candela
        self.__candela = self.__convert_from_base(LuminousIntensityUnits.Candela)
        return self.__candela

    
    def to_string(self, unit: LuminousIntensityUnits = LuminousIntensityUnits.Candela, fractional_digits: int = None) -> str:
        """
        Format the LuminousIntensity to a string.
        
        Note: the default format for LuminousIntensity is Candela.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the LuminousIntensity. Default is 'Candela'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == LuminousIntensityUnits.Candela:
            return f"""{super()._truncate_fraction_digits(self.candela, fractional_digits)} cd"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: LuminousIntensityUnits = LuminousIntensityUnits.Candela) -> str:
        """
        Get LuminousIntensity unit abbreviation.
        Note! the default abbreviation for LuminousIntensity is Candela.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == LuminousIntensityUnits.Candela:
            return """cd"""
        
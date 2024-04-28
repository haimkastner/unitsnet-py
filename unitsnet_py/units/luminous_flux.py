from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class LuminousFluxUnits(Enum):
        """
            LuminousFluxUnits enumeration
        """
        
        Lumen = 'Lumen'
        """
            
        """
        

class LuminousFluxDto:
    """
    A DTO representation of a LuminousFlux

    Attributes:
        value (float): The value of the LuminousFlux.
        unit (LuminousFluxUnits): The specific unit that the LuminousFlux value is representing.
    """

    def __init__(self, value: float, unit: LuminousFluxUnits):
        """
        Create a new DTO representation of a LuminousFlux

        Parameters:
            value (float): The value of the LuminousFlux.
            unit (LuminousFluxUnits): The specific unit that the LuminousFlux value is representing.
        """
        self.value: float = value
        """
        The value of the LuminousFlux
        """
        self.unit: LuminousFluxUnits = unit
        """
        The specific unit that the LuminousFlux value is representing
        """

    def to_json(self):
        """
        Get a LuminousFlux DTO JSON object representing the current unit.

        :return: JSON object represents LuminousFlux DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "Lumen"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of LuminousFlux DTO from a json representation.

        :param data: The LuminousFlux DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "Lumen"}
        :return: A new instance of LuminousFluxDto.
        :rtype: LuminousFluxDto
        """
        return LuminousFluxDto(value=data["value"], unit=LuminousFluxUnits(data["unit"]))


class LuminousFlux(AbstractMeasure):
    """
    In photometry, luminous flux or luminous power is the measure of the perceived power of light.

    Args:
        value (float): The value.
        from_unit (LuminousFluxUnits): The LuminousFlux unit to create from, The default unit is Lumen
    """
    def __init__(self, value: float, from_unit: LuminousFluxUnits = LuminousFluxUnits.Lumen):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__lumens = None
        

    def convert(self, unit: LuminousFluxUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: LuminousFluxUnits = LuminousFluxUnits.Lumen) -> LuminousFluxDto:
        """
        Get a new instance of LuminousFlux DTO representing the current unit.

        :param hold_in_unit: The specific LuminousFlux unit to store the LuminousFlux value in the DTO representation.
        :type hold_in_unit: LuminousFluxUnits
        :return: A new instance of LuminousFluxDto.
        :rtype: LuminousFluxDto
        """
        return LuminousFluxDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: LuminousFluxUnits = LuminousFluxUnits.Lumen):
        """
        Get a LuminousFlux DTO JSON object representing the current unit.

        :param hold_in_unit: The specific LuminousFlux unit to store the LuminousFlux value in the DTO representation.
        :type hold_in_unit: LuminousFluxUnits
        :return: JSON object represents LuminousFlux DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "Lumen"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(luminous_flux_dto: LuminousFluxDto):
        """
        Obtain a new instance of LuminousFlux from a DTO unit object.

        :param luminous_flux_dto: The LuminousFlux DTO representation.
        :type luminous_flux_dto: LuminousFluxDto
        :return: A new instance of LuminousFlux.
        :rtype: LuminousFlux
        """
        return LuminousFlux(luminous_flux_dto.value, luminous_flux_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of LuminousFlux from a DTO unit json representation.

        :param data: The LuminousFlux DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "Lumen"}
        :return: A new instance of LuminousFlux.
        :rtype: LuminousFlux
        """
        return LuminousFlux.from_dto(LuminousFluxDto.from_json(data))

    def __convert_from_base(self, from_unit: LuminousFluxUnits) -> float:
        value = self._value
        
        if from_unit == LuminousFluxUnits.Lumen:
            return (value)
        
        return None


    def __convert_to_base(self, value: float, to_unit: LuminousFluxUnits) -> float:
        
        if to_unit == LuminousFluxUnits.Lumen:
            return (value)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_lumens(lumens: float):
        """
        Create a new instance of LuminousFlux from a value in lumens.

        

        :param meters: The LuminousFlux value in lumens.
        :type lumens: float
        :return: A new instance of LuminousFlux.
        :rtype: LuminousFlux
        """
        return LuminousFlux(lumens, LuminousFluxUnits.Lumen)

    
    @property
    def lumens(self) -> float:
        """
        
        """
        if self.__lumens != None:
            return self.__lumens
        self.__lumens = self.__convert_from_base(LuminousFluxUnits.Lumen)
        return self.__lumens

    
    def to_string(self, unit: LuminousFluxUnits = LuminousFluxUnits.Lumen, fractional_digits: int = None) -> str:
        """
        Format the LuminousFlux to a string.
        
        Note: the default format for LuminousFlux is Lumen.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the LuminousFlux. Default is 'Lumen'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == LuminousFluxUnits.Lumen:
            return f"""{super()._truncate_fraction_digits(self.lumens, fractional_digits)} lm"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: LuminousFluxUnits = LuminousFluxUnits.Lumen) -> str:
        """
        Get LuminousFlux unit abbreviation.
        Note! the default abbreviation for LuminousFlux is Lumen.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == LuminousFluxUnits.Lumen:
            return """lm"""
        
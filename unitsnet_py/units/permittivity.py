from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class PermittivityUnits(Enum):
        """
            PermittivityUnits enumeration
        """
        
        FaradPerMeter = 'FaradPerMeter'
        """
            
        """
        

class PermittivityDto:
    """
    A DTO representation of a Permittivity

    Attributes:
        value (float): The value of the Permittivity.
        unit (PermittivityUnits): The specific unit that the Permittivity value is representing.
    """

    def __init__(self, value: float, unit: PermittivityUnits):
        """
        Create a new DTO representation of a Permittivity

        Parameters:
            value (float): The value of the Permittivity.
            unit (PermittivityUnits): The specific unit that the Permittivity value is representing.
        """
        self.value: float = value
        """
        The value of the Permittivity
        """
        self.unit: PermittivityUnits = unit
        """
        The specific unit that the Permittivity value is representing
        """

    def to_json(self):
        """
        Get a Permittivity DTO JSON object representing the current unit.

        :return: JSON object represents Permittivity DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "FaradPerMeter"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of Permittivity DTO from a json representation.

        :param data: The Permittivity DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "FaradPerMeter"}
        :return: A new instance of PermittivityDto.
        :rtype: PermittivityDto
        """
        return PermittivityDto(value=data["value"], unit=PermittivityUnits(data["unit"]))


class Permittivity(AbstractMeasure):
    """
    In electromagnetism, permittivity is the measure of resistance that is encountered when forming an electric field in a particular medium.

    Args:
        value (float): The value.
        from_unit (PermittivityUnits): The Permittivity unit to create from, The default unit is FaradPerMeter
    """
    def __init__(self, value: float, from_unit: PermittivityUnits = PermittivityUnits.FaradPerMeter):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__farads_per_meter = None
        

    def convert(self, unit: PermittivityUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: PermittivityUnits = PermittivityUnits.FaradPerMeter) -> PermittivityDto:
        """
        Get a new instance of Permittivity DTO representing the current unit.

        :param hold_in_unit: The specific Permittivity unit to store the Permittivity value in the DTO representation.
        :type hold_in_unit: PermittivityUnits
        :return: A new instance of PermittivityDto.
        :rtype: PermittivityDto
        """
        return PermittivityDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: PermittivityUnits = PermittivityUnits.FaradPerMeter):
        """
        Get a Permittivity DTO JSON object representing the current unit.

        :param hold_in_unit: The specific Permittivity unit to store the Permittivity value in the DTO representation.
        :type hold_in_unit: PermittivityUnits
        :return: JSON object represents Permittivity DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "FaradPerMeter"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(permittivity_dto: PermittivityDto):
        """
        Obtain a new instance of Permittivity from a DTO unit object.

        :param permittivity_dto: The Permittivity DTO representation.
        :type permittivity_dto: PermittivityDto
        :return: A new instance of Permittivity.
        :rtype: Permittivity
        """
        return Permittivity(permittivity_dto.value, permittivity_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of Permittivity from a DTO unit json representation.

        :param data: The Permittivity DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "FaradPerMeter"}
        :return: A new instance of Permittivity.
        :rtype: Permittivity
        """
        return Permittivity.from_dto(PermittivityDto.from_json(data))

    def __convert_from_base(self, from_unit: PermittivityUnits) -> float:
        value = self._value
        
        if from_unit == PermittivityUnits.FaradPerMeter:
            return (value)
        
        return None


    def __convert_to_base(self, value: float, to_unit: PermittivityUnits) -> float:
        
        if to_unit == PermittivityUnits.FaradPerMeter:
            return (value)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_farads_per_meter(farads_per_meter: float):
        """
        Create a new instance of Permittivity from a value in farads_per_meter.

        

        :param meters: The Permittivity value in farads_per_meter.
        :type farads_per_meter: float
        :return: A new instance of Permittivity.
        :rtype: Permittivity
        """
        return Permittivity(farads_per_meter, PermittivityUnits.FaradPerMeter)

    
    @property
    def farads_per_meter(self) -> float:
        """
        
        """
        if self.__farads_per_meter != None:
            return self.__farads_per_meter
        self.__farads_per_meter = self.__convert_from_base(PermittivityUnits.FaradPerMeter)
        return self.__farads_per_meter

    
    def to_string(self, unit: PermittivityUnits = PermittivityUnits.FaradPerMeter, fractional_digits: int = None) -> str:
        """
        Format the Permittivity to a string.
        
        Note: the default format for Permittivity is FaradPerMeter.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the Permittivity. Default is 'FaradPerMeter'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == PermittivityUnits.FaradPerMeter:
            return f"""{super()._truncate_fraction_digits(self.farads_per_meter, fractional_digits)} F/m"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: PermittivityUnits = PermittivityUnits.FaradPerMeter) -> str:
        """
        Get Permittivity unit abbreviation.
        Note! the default abbreviation for Permittivity is FaradPerMeter.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == PermittivityUnits.FaradPerMeter:
            return """F/m"""
        
from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class MagnetizationUnits(Enum):
        """
            MagnetizationUnits enumeration
        """
        
        AmperePerMeter = 'AmperePerMeter'
        """
            
        """
        

class MagnetizationDto:
    """
    A DTO representation of a Magnetization

    Attributes:
        value (float): The value of the Magnetization.
        unit (MagnetizationUnits): The specific unit that the Magnetization value is representing.
    """

    def __init__(self, value: float, unit: MagnetizationUnits):
        """
        Create a new DTO representation of a Magnetization

        Parameters:
            value (float): The value of the Magnetization.
            unit (MagnetizationUnits): The specific unit that the Magnetization value is representing.
        """
        self.value: float = value
        """
        The value of the Magnetization
        """
        self.unit: MagnetizationUnits = unit
        """
        The specific unit that the Magnetization value is representing
        """

    def to_json(self):
        """
        Get a Magnetization DTO JSON object representing the current unit.

        :return: JSON object represents Magnetization DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "AmperePerMeter"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of Magnetization DTO from a json representation.

        :param data: The Magnetization DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "AmperePerMeter"}
        :return: A new instance of MagnetizationDto.
        :rtype: MagnetizationDto
        """
        return MagnetizationDto(value=data["value"], unit=MagnetizationUnits(data["unit"]))


class Magnetization(AbstractMeasure):
    """
    In classical electromagnetism, magnetization is the vector field that expresses the density of permanent or induced magnetic dipole moments in a magnetic material.

    Args:
        value (float): The value.
        from_unit (MagnetizationUnits): The Magnetization unit to create from, The default unit is AmperePerMeter
    """
    def __init__(self, value: float, from_unit: MagnetizationUnits = MagnetizationUnits.AmperePerMeter):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__amperes_per_meter = None
        

    def convert(self, unit: MagnetizationUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: MagnetizationUnits = MagnetizationUnits.AmperePerMeter) -> MagnetizationDto:
        """
        Get a new instance of Magnetization DTO representing the current unit.

        :param hold_in_unit: The specific Magnetization unit to store the Magnetization value in the DTO representation.
        :type hold_in_unit: MagnetizationUnits
        :return: A new instance of MagnetizationDto.
        :rtype: MagnetizationDto
        """
        return MagnetizationDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: MagnetizationUnits = MagnetizationUnits.AmperePerMeter):
        """
        Get a Magnetization DTO JSON object representing the current unit.

        :param hold_in_unit: The specific Magnetization unit to store the Magnetization value in the DTO representation.
        :type hold_in_unit: MagnetizationUnits
        :return: JSON object represents Magnetization DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "AmperePerMeter"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(magnetization_dto: MagnetizationDto):
        """
        Obtain a new instance of Magnetization from a DTO unit object.

        :param magnetization_dto: The Magnetization DTO representation.
        :type magnetization_dto: MagnetizationDto
        :return: A new instance of Magnetization.
        :rtype: Magnetization
        """
        return Magnetization(magnetization_dto.value, magnetization_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of Magnetization from a DTO unit json representation.

        :param data: The Magnetization DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "AmperePerMeter"}
        :return: A new instance of Magnetization.
        :rtype: Magnetization
        """
        return Magnetization.from_dto(MagnetizationDto.from_json(data))

    def __convert_from_base(self, from_unit: MagnetizationUnits) -> float:
        value = self._value
        
        if from_unit == MagnetizationUnits.AmperePerMeter:
            return (value)
        
        return None


    def __convert_to_base(self, value: float, to_unit: MagnetizationUnits) -> float:
        
        if to_unit == MagnetizationUnits.AmperePerMeter:
            return (value)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_amperes_per_meter(amperes_per_meter: float):
        """
        Create a new instance of Magnetization from a value in amperes_per_meter.

        

        :param meters: The Magnetization value in amperes_per_meter.
        :type amperes_per_meter: float
        :return: A new instance of Magnetization.
        :rtype: Magnetization
        """
        return Magnetization(amperes_per_meter, MagnetizationUnits.AmperePerMeter)

    
    @property
    def amperes_per_meter(self) -> float:
        """
        
        """
        if self.__amperes_per_meter != None:
            return self.__amperes_per_meter
        self.__amperes_per_meter = self.__convert_from_base(MagnetizationUnits.AmperePerMeter)
        return self.__amperes_per_meter

    
    def to_string(self, unit: MagnetizationUnits = MagnetizationUnits.AmperePerMeter, fractional_digits: int = None) -> str:
        """
        Format the Magnetization to a string.
        
        Note: the default format for Magnetization is AmperePerMeter.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the Magnetization. Default is 'AmperePerMeter'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == MagnetizationUnits.AmperePerMeter:
            return f"""{super()._truncate_fraction_digits(self.amperes_per_meter, fractional_digits)} A/m"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: MagnetizationUnits = MagnetizationUnits.AmperePerMeter) -> str:
        """
        Get Magnetization unit abbreviation.
        Note! the default abbreviation for Magnetization is AmperePerMeter.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == MagnetizationUnits.AmperePerMeter:
            return """A/m"""
        
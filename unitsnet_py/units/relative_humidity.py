from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class RelativeHumidityUnits(Enum):
        """
            RelativeHumidityUnits enumeration
        """
        
        Percent = 'Percent'
        """
            
        """
        

class RelativeHumidityDto:
    """
    A DTO representation of a RelativeHumidity

    Attributes:
        value (float): The value of the RelativeHumidity.
        unit (RelativeHumidityUnits): The specific unit that the RelativeHumidity value is representing.
    """

    def __init__(self, value: float, unit: RelativeHumidityUnits):
        """
        Create a new DTO representation of a RelativeHumidity

        Parameters:
            value (float): The value of the RelativeHumidity.
            unit (RelativeHumidityUnits): The specific unit that the RelativeHumidity value is representing.
        """
        self.value: float = value
        """
        The value of the RelativeHumidity
        """
        self.unit: RelativeHumidityUnits = unit
        """
        The specific unit that the RelativeHumidity value is representing
        """

    def to_json(self):
        """
        Get a RelativeHumidity DTO JSON object representing the current unit.

        :return: JSON object represents RelativeHumidity DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "Percent"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of RelativeHumidity DTO from a json representation.

        :param data: The RelativeHumidity DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "Percent"}
        :return: A new instance of RelativeHumidityDto.
        :rtype: RelativeHumidityDto
        """
        return RelativeHumidityDto(value=data["value"], unit=RelativeHumidityUnits(data["unit"]))


class RelativeHumidity(AbstractMeasure):
    """
    Relative humidity is a ratio of the actual water vapor present in the air to the maximum water vapor in the air at the given temperature.

    Args:
        value (float): The value.
        from_unit (RelativeHumidityUnits): The RelativeHumidity unit to create from, The default unit is Percent
    """
    def __init__(self, value: float, from_unit: RelativeHumidityUnits = RelativeHumidityUnits.Percent):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__percent = None
        

    def convert(self, unit: RelativeHumidityUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: RelativeHumidityUnits = RelativeHumidityUnits.Percent) -> RelativeHumidityDto:
        """
        Get a new instance of RelativeHumidity DTO representing the current unit.

        :param hold_in_unit: The specific RelativeHumidity unit to store the RelativeHumidity value in the DTO representation.
        :type hold_in_unit: RelativeHumidityUnits
        :return: A new instance of RelativeHumidityDto.
        :rtype: RelativeHumidityDto
        """
        return RelativeHumidityDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: RelativeHumidityUnits = RelativeHumidityUnits.Percent):
        """
        Get a RelativeHumidity DTO JSON object representing the current unit.

        :param hold_in_unit: The specific RelativeHumidity unit to store the RelativeHumidity value in the DTO representation.
        :type hold_in_unit: RelativeHumidityUnits
        :return: JSON object represents RelativeHumidity DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "Percent"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(relative_humidity_dto: RelativeHumidityDto):
        """
        Obtain a new instance of RelativeHumidity from a DTO unit object.

        :param relative_humidity_dto: The RelativeHumidity DTO representation.
        :type relative_humidity_dto: RelativeHumidityDto
        :return: A new instance of RelativeHumidity.
        :rtype: RelativeHumidity
        """
        return RelativeHumidity(relative_humidity_dto.value, relative_humidity_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of RelativeHumidity from a DTO unit json representation.

        :param data: The RelativeHumidity DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "Percent"}
        :return: A new instance of RelativeHumidity.
        :rtype: RelativeHumidity
        """
        return RelativeHumidity.from_dto(RelativeHumidityDto.from_json(data))

    def __convert_from_base(self, from_unit: RelativeHumidityUnits) -> float:
        value = self._value
        
        if from_unit == RelativeHumidityUnits.Percent:
            return (value)
        
        return None


    def __convert_to_base(self, value: float, to_unit: RelativeHumidityUnits) -> float:
        
        if to_unit == RelativeHumidityUnits.Percent:
            return (value)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_percent(percent: float):
        """
        Create a new instance of RelativeHumidity from a value in percent.

        

        :param meters: The RelativeHumidity value in percent.
        :type percent: float
        :return: A new instance of RelativeHumidity.
        :rtype: RelativeHumidity
        """
        return RelativeHumidity(percent, RelativeHumidityUnits.Percent)

    
    @property
    def percent(self) -> float:
        """
        
        """
        if self.__percent != None:
            return self.__percent
        self.__percent = self.__convert_from_base(RelativeHumidityUnits.Percent)
        return self.__percent

    
    def to_string(self, unit: RelativeHumidityUnits = RelativeHumidityUnits.Percent, fractional_digits: int = None) -> str:
        """
        Format the RelativeHumidity to a string.
        
        Note: the default format for RelativeHumidity is Percent.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the RelativeHumidity. Default is 'Percent'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == RelativeHumidityUnits.Percent:
            return f"""{super()._truncate_fraction_digits(self.percent, fractional_digits)} %RH"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: RelativeHumidityUnits = RelativeHumidityUnits.Percent) -> str:
        """
        Get RelativeHumidity unit abbreviation.
        Note! the default abbreviation for RelativeHumidity is Percent.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == RelativeHumidityUnits.Percent:
            return """%RH"""
        
from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class ElectricFieldUnits(Enum):
        """
            ElectricFieldUnits enumeration
        """
        
        VoltPerMeter = 'VoltPerMeter'
        """
            
        """
        

class ElectricFieldDto:
    """
    A DTO representation of a ElectricField

    Attributes:
        value (float): The value of the ElectricField.
        unit (ElectricFieldUnits): The specific unit that the ElectricField value is representing.
    """

    def __init__(self, value: float, unit: ElectricFieldUnits):
        """
        Create a new DTO representation of a ElectricField

        Parameters:
            value (float): The value of the ElectricField.
            unit (ElectricFieldUnits): The specific unit that the ElectricField value is representing.
        """
        self.value: float = value
        """
        The value of the ElectricField
        """
        self.unit: ElectricFieldUnits = unit
        """
        The specific unit that the ElectricField value is representing
        """

    def to_json(self):
        """
        Get a ElectricField DTO JSON object representing the current unit.

        :return: JSON object represents ElectricField DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "VoltPerMeter"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of ElectricField DTO from a json representation.

        :param data: The ElectricField DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "VoltPerMeter"}
        :return: A new instance of ElectricFieldDto.
        :rtype: ElectricFieldDto
        """
        return ElectricFieldDto(value=data["value"], unit=ElectricFieldUnits(data["unit"]))


class ElectricField(AbstractMeasure):
    """
    An electric field is a force field that surrounds electric charges that attracts or repels other electric charges.

    Args:
        value (float): The value.
        from_unit (ElectricFieldUnits): The ElectricField unit to create from, The default unit is VoltPerMeter
    """
    def __init__(self, value: float, from_unit: ElectricFieldUnits = ElectricFieldUnits.VoltPerMeter):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__volts_per_meter = None
        

    def convert(self, unit: ElectricFieldUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: ElectricFieldUnits = ElectricFieldUnits.VoltPerMeter) -> ElectricFieldDto:
        """
        Get a new instance of ElectricField DTO representing the current unit.

        :param hold_in_unit: The specific ElectricField unit to store the ElectricField value in the DTO representation.
        :type hold_in_unit: ElectricFieldUnits
        :return: A new instance of ElectricFieldDto.
        :rtype: ElectricFieldDto
        """
        return ElectricFieldDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: ElectricFieldUnits = ElectricFieldUnits.VoltPerMeter):
        """
        Get a ElectricField DTO JSON object representing the current unit.

        :param hold_in_unit: The specific ElectricField unit to store the ElectricField value in the DTO representation.
        :type hold_in_unit: ElectricFieldUnits
        :return: JSON object represents ElectricField DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "VoltPerMeter"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(electric_field_dto: ElectricFieldDto):
        """
        Obtain a new instance of ElectricField from a DTO unit object.

        :param electric_field_dto: The ElectricField DTO representation.
        :type electric_field_dto: ElectricFieldDto
        :return: A new instance of ElectricField.
        :rtype: ElectricField
        """
        return ElectricField(electric_field_dto.value, electric_field_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of ElectricField from a DTO unit json representation.

        :param data: The ElectricField DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "VoltPerMeter"}
        :return: A new instance of ElectricField.
        :rtype: ElectricField
        """
        return ElectricField.from_dto(ElectricFieldDto.from_json(data))

    def __convert_from_base(self, from_unit: ElectricFieldUnits) -> float:
        value = self._value
        
        if from_unit == ElectricFieldUnits.VoltPerMeter:
            return (value)
        
        return None


    def __convert_to_base(self, value: float, to_unit: ElectricFieldUnits) -> float:
        
        if to_unit == ElectricFieldUnits.VoltPerMeter:
            return (value)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_volts_per_meter(volts_per_meter: float):
        """
        Create a new instance of ElectricField from a value in volts_per_meter.

        

        :param meters: The ElectricField value in volts_per_meter.
        :type volts_per_meter: float
        :return: A new instance of ElectricField.
        :rtype: ElectricField
        """
        return ElectricField(volts_per_meter, ElectricFieldUnits.VoltPerMeter)

    
    @property
    def volts_per_meter(self) -> float:
        """
        
        """
        if self.__volts_per_meter != None:
            return self.__volts_per_meter
        self.__volts_per_meter = self.__convert_from_base(ElectricFieldUnits.VoltPerMeter)
        return self.__volts_per_meter

    
    def to_string(self, unit: ElectricFieldUnits = ElectricFieldUnits.VoltPerMeter, fractional_digits: int = None) -> str:
        """
        Format the ElectricField to a string.
        
        Note: the default format for ElectricField is VoltPerMeter.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the ElectricField. Default is 'VoltPerMeter'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == ElectricFieldUnits.VoltPerMeter:
            return f"""{super()._truncate_fraction_digits(self.volts_per_meter, fractional_digits)} V/m"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: ElectricFieldUnits = ElectricFieldUnits.VoltPerMeter) -> str:
        """
        Get ElectricField unit abbreviation.
        Note! the default abbreviation for ElectricField is VoltPerMeter.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == ElectricFieldUnits.VoltPerMeter:
            return """V/m"""
        
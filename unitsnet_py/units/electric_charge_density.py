from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class ElectricChargeDensityUnits(Enum):
        """
            ElectricChargeDensityUnits enumeration
        """
        
        CoulombPerCubicMeter = 'CoulombPerCubicMeter'
        """
            
        """
        

class ElectricChargeDensityDto:
    """
    A DTO representation of a ElectricChargeDensity

    Attributes:
        value (float): The value of the ElectricChargeDensity.
        unit (ElectricChargeDensityUnits): The specific unit that the ElectricChargeDensity value is representing.
    """

    def __init__(self, value: float, unit: ElectricChargeDensityUnits):
        """
        Create a new DTO representation of a ElectricChargeDensity

        Parameters:
            value (float): The value of the ElectricChargeDensity.
            unit (ElectricChargeDensityUnits): The specific unit that the ElectricChargeDensity value is representing.
        """
        self.value: float = value
        """
        The value of the ElectricChargeDensity
        """
        self.unit: ElectricChargeDensityUnits = unit
        """
        The specific unit that the ElectricChargeDensity value is representing
        """

    def to_json(self):
        """
        Get a ElectricChargeDensity DTO JSON object representing the current unit.

        :return: JSON object represents ElectricChargeDensity DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "CoulombPerCubicMeter"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of ElectricChargeDensity DTO from a json representation.

        :param data: The ElectricChargeDensity DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "CoulombPerCubicMeter"}
        :return: A new instance of ElectricChargeDensityDto.
        :rtype: ElectricChargeDensityDto
        """
        return ElectricChargeDensityDto(value=data["value"], unit=ElectricChargeDensityUnits(data["unit"]))


class ElectricChargeDensity(AbstractMeasure):
    """
    In electromagnetism, charge density is a measure of the amount of electric charge per volume.

    Args:
        value (float): The value.
        from_unit (ElectricChargeDensityUnits): The ElectricChargeDensity unit to create from, The default unit is CoulombPerCubicMeter
    """
    def __init__(self, value: float, from_unit: ElectricChargeDensityUnits = ElectricChargeDensityUnits.CoulombPerCubicMeter):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__coulombs_per_cubic_meter = None
        

    def convert(self, unit: ElectricChargeDensityUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: ElectricChargeDensityUnits = ElectricChargeDensityUnits.CoulombPerCubicMeter) -> ElectricChargeDensityDto:
        """
        Get a new instance of ElectricChargeDensity DTO representing the current unit.

        :param hold_in_unit: The specific ElectricChargeDensity unit to store the ElectricChargeDensity value in the DTO representation.
        :type hold_in_unit: ElectricChargeDensityUnits
        :return: A new instance of ElectricChargeDensityDto.
        :rtype: ElectricChargeDensityDto
        """
        return ElectricChargeDensityDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: ElectricChargeDensityUnits = ElectricChargeDensityUnits.CoulombPerCubicMeter):
        """
        Get a ElectricChargeDensity DTO JSON object representing the current unit.

        :param hold_in_unit: The specific ElectricChargeDensity unit to store the ElectricChargeDensity value in the DTO representation.
        :type hold_in_unit: ElectricChargeDensityUnits
        :return: JSON object represents ElectricChargeDensity DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "CoulombPerCubicMeter"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(electric_charge_density_dto: ElectricChargeDensityDto):
        """
        Obtain a new instance of ElectricChargeDensity from a DTO unit object.

        :param electric_charge_density_dto: The ElectricChargeDensity DTO representation.
        :type electric_charge_density_dto: ElectricChargeDensityDto
        :return: A new instance of ElectricChargeDensity.
        :rtype: ElectricChargeDensity
        """
        return ElectricChargeDensity(electric_charge_density_dto.value, electric_charge_density_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of ElectricChargeDensity from a DTO unit json representation.

        :param data: The ElectricChargeDensity DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "CoulombPerCubicMeter"}
        :return: A new instance of ElectricChargeDensity.
        :rtype: ElectricChargeDensity
        """
        return ElectricChargeDensity.from_dto(ElectricChargeDensityDto.from_json(data))

    def __convert_from_base(self, from_unit: ElectricChargeDensityUnits) -> float:
        value = self._value
        
        if from_unit == ElectricChargeDensityUnits.CoulombPerCubicMeter:
            return (value)
        
        return None


    def __convert_to_base(self, value: float, to_unit: ElectricChargeDensityUnits) -> float:
        
        if to_unit == ElectricChargeDensityUnits.CoulombPerCubicMeter:
            return (value)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_coulombs_per_cubic_meter(coulombs_per_cubic_meter: float):
        """
        Create a new instance of ElectricChargeDensity from a value in coulombs_per_cubic_meter.

        

        :param meters: The ElectricChargeDensity value in coulombs_per_cubic_meter.
        :type coulombs_per_cubic_meter: float
        :return: A new instance of ElectricChargeDensity.
        :rtype: ElectricChargeDensity
        """
        return ElectricChargeDensity(coulombs_per_cubic_meter, ElectricChargeDensityUnits.CoulombPerCubicMeter)

    
    @property
    def coulombs_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__coulombs_per_cubic_meter != None:
            return self.__coulombs_per_cubic_meter
        self.__coulombs_per_cubic_meter = self.__convert_from_base(ElectricChargeDensityUnits.CoulombPerCubicMeter)
        return self.__coulombs_per_cubic_meter

    
    def to_string(self, unit: ElectricChargeDensityUnits = ElectricChargeDensityUnits.CoulombPerCubicMeter, fractional_digits: int = None) -> str:
        """
        Format the ElectricChargeDensity to a string.
        
        Note: the default format for ElectricChargeDensity is CoulombPerCubicMeter.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the ElectricChargeDensity. Default is 'CoulombPerCubicMeter'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == ElectricChargeDensityUnits.CoulombPerCubicMeter:
            return f"""{super()._truncate_fraction_digits(self.coulombs_per_cubic_meter, fractional_digits)} C/m³"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: ElectricChargeDensityUnits = ElectricChargeDensityUnits.CoulombPerCubicMeter) -> str:
        """
        Get ElectricChargeDensity unit abbreviation.
        Note! the default abbreviation for ElectricChargeDensity is CoulombPerCubicMeter.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == ElectricChargeDensityUnits.CoulombPerCubicMeter:
            return """C/m³"""
        
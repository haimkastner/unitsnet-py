from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class ElectricApparentEnergyUnits(Enum):
        """
            ElectricApparentEnergyUnits enumeration
        """
        
        VoltampereHour = 'VoltampereHour'
        """
            
        """
        
        KilovoltampereHour = 'KilovoltampereHour'
        """
            
        """
        
        MegavoltampereHour = 'MegavoltampereHour'
        """
            
        """
        

class ElectricApparentEnergyDto:
    """
    A DTO representation of a ElectricApparentEnergy

    Attributes:
        value (float): The value of the ElectricApparentEnergy.
        unit (ElectricApparentEnergyUnits): The specific unit that the ElectricApparentEnergy value is representing.
    """

    def __init__(self, value: float, unit: ElectricApparentEnergyUnits):
        """
        Create a new DTO representation of a ElectricApparentEnergy

        Parameters:
            value (float): The value of the ElectricApparentEnergy.
            unit (ElectricApparentEnergyUnits): The specific unit that the ElectricApparentEnergy value is representing.
        """
        self.value: float = value
        """
        The value of the ElectricApparentEnergy
        """
        self.unit: ElectricApparentEnergyUnits = unit
        """
        The specific unit that the ElectricApparentEnergy value is representing
        """

    def to_json(self):
        """
        Get a ElectricApparentEnergy DTO JSON object representing the current unit.

        :return: JSON object represents ElectricApparentEnergy DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "VoltampereHour"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of ElectricApparentEnergy DTO from a json representation.

        :param data: The ElectricApparentEnergy DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "VoltampereHour"}
        :return: A new instance of ElectricApparentEnergyDto.
        :rtype: ElectricApparentEnergyDto
        """
        return ElectricApparentEnergyDto(value=data["value"], unit=ElectricApparentEnergyUnits(data["unit"]))


class ElectricApparentEnergy(AbstractMeasure):
    """
    A unit for expressing the integral of apparent power over time, equal to the product of 1 volt-ampere and 1 hour, or to 3600 joules.

    Args:
        value (float): The value.
        from_unit (ElectricApparentEnergyUnits): The ElectricApparentEnergy unit to create from, The default unit is VoltampereHour
    """
    def __init__(self, value: float, from_unit: ElectricApparentEnergyUnits = ElectricApparentEnergyUnits.VoltampereHour):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__voltampere_hours = None
        
        self.__kilovoltampere_hours = None
        
        self.__megavoltampere_hours = None
        

    def convert(self, unit: ElectricApparentEnergyUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: ElectricApparentEnergyUnits = ElectricApparentEnergyUnits.VoltampereHour) -> ElectricApparentEnergyDto:
        """
        Get a new instance of ElectricApparentEnergy DTO representing the current unit.

        :param hold_in_unit: The specific ElectricApparentEnergy unit to store the ElectricApparentEnergy value in the DTO representation.
        :type hold_in_unit: ElectricApparentEnergyUnits
        :return: A new instance of ElectricApparentEnergyDto.
        :rtype: ElectricApparentEnergyDto
        """
        return ElectricApparentEnergyDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: ElectricApparentEnergyUnits = ElectricApparentEnergyUnits.VoltampereHour):
        """
        Get a ElectricApparentEnergy DTO JSON object representing the current unit.

        :param hold_in_unit: The specific ElectricApparentEnergy unit to store the ElectricApparentEnergy value in the DTO representation.
        :type hold_in_unit: ElectricApparentEnergyUnits
        :return: JSON object represents ElectricApparentEnergy DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "VoltampereHour"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(electric_apparent_energy_dto: ElectricApparentEnergyDto):
        """
        Obtain a new instance of ElectricApparentEnergy from a DTO unit object.

        :param electric_apparent_energy_dto: The ElectricApparentEnergy DTO representation.
        :type electric_apparent_energy_dto: ElectricApparentEnergyDto
        :return: A new instance of ElectricApparentEnergy.
        :rtype: ElectricApparentEnergy
        """
        return ElectricApparentEnergy(electric_apparent_energy_dto.value, electric_apparent_energy_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of ElectricApparentEnergy from a DTO unit json representation.

        :param data: The ElectricApparentEnergy DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "VoltampereHour"}
        :return: A new instance of ElectricApparentEnergy.
        :rtype: ElectricApparentEnergy
        """
        return ElectricApparentEnergy.from_dto(ElectricApparentEnergyDto.from_json(data))

    def __convert_from_base(self, from_unit: ElectricApparentEnergyUnits) -> float:
        value = self._value
        
        if from_unit == ElectricApparentEnergyUnits.VoltampereHour:
            return (value)
        
        if from_unit == ElectricApparentEnergyUnits.KilovoltampereHour:
            return ((value) / 1000.0)
        
        if from_unit == ElectricApparentEnergyUnits.MegavoltampereHour:
            return ((value) / 1000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: ElectricApparentEnergyUnits) -> float:
        
        if to_unit == ElectricApparentEnergyUnits.VoltampereHour:
            return (value)
        
        if to_unit == ElectricApparentEnergyUnits.KilovoltampereHour:
            return ((value) * 1000.0)
        
        if to_unit == ElectricApparentEnergyUnits.MegavoltampereHour:
            return ((value) * 1000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_voltampere_hours(voltampere_hours: float):
        """
        Create a new instance of ElectricApparentEnergy from a value in voltampere_hours.

        

        :param meters: The ElectricApparentEnergy value in voltampere_hours.
        :type voltampere_hours: float
        :return: A new instance of ElectricApparentEnergy.
        :rtype: ElectricApparentEnergy
        """
        return ElectricApparentEnergy(voltampere_hours, ElectricApparentEnergyUnits.VoltampereHour)

    
    @staticmethod
    def from_kilovoltampere_hours(kilovoltampere_hours: float):
        """
        Create a new instance of ElectricApparentEnergy from a value in kilovoltampere_hours.

        

        :param meters: The ElectricApparentEnergy value in kilovoltampere_hours.
        :type kilovoltampere_hours: float
        :return: A new instance of ElectricApparentEnergy.
        :rtype: ElectricApparentEnergy
        """
        return ElectricApparentEnergy(kilovoltampere_hours, ElectricApparentEnergyUnits.KilovoltampereHour)

    
    @staticmethod
    def from_megavoltampere_hours(megavoltampere_hours: float):
        """
        Create a new instance of ElectricApparentEnergy from a value in megavoltampere_hours.

        

        :param meters: The ElectricApparentEnergy value in megavoltampere_hours.
        :type megavoltampere_hours: float
        :return: A new instance of ElectricApparentEnergy.
        :rtype: ElectricApparentEnergy
        """
        return ElectricApparentEnergy(megavoltampere_hours, ElectricApparentEnergyUnits.MegavoltampereHour)

    
    @property
    def voltampere_hours(self) -> float:
        """
        
        """
        if self.__voltampere_hours != None:
            return self.__voltampere_hours
        self.__voltampere_hours = self.__convert_from_base(ElectricApparentEnergyUnits.VoltampereHour)
        return self.__voltampere_hours

    
    @property
    def kilovoltampere_hours(self) -> float:
        """
        
        """
        if self.__kilovoltampere_hours != None:
            return self.__kilovoltampere_hours
        self.__kilovoltampere_hours = self.__convert_from_base(ElectricApparentEnergyUnits.KilovoltampereHour)
        return self.__kilovoltampere_hours

    
    @property
    def megavoltampere_hours(self) -> float:
        """
        
        """
        if self.__megavoltampere_hours != None:
            return self.__megavoltampere_hours
        self.__megavoltampere_hours = self.__convert_from_base(ElectricApparentEnergyUnits.MegavoltampereHour)
        return self.__megavoltampere_hours

    
    def to_string(self, unit: ElectricApparentEnergyUnits = ElectricApparentEnergyUnits.VoltampereHour, fractional_digits: int = None) -> str:
        """
        Format the ElectricApparentEnergy to a string.
        
        Note: the default format for ElectricApparentEnergy is VoltampereHour.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the ElectricApparentEnergy. Default is 'VoltampereHour'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == ElectricApparentEnergyUnits.VoltampereHour:
            return f"""{super()._truncate_fraction_digits(self.voltampere_hours, fractional_digits)} VAh"""
        
        if unit == ElectricApparentEnergyUnits.KilovoltampereHour:
            return f"""{super()._truncate_fraction_digits(self.kilovoltampere_hours, fractional_digits)} kVAh"""
        
        if unit == ElectricApparentEnergyUnits.MegavoltampereHour:
            return f"""{super()._truncate_fraction_digits(self.megavoltampere_hours, fractional_digits)} MVAh"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: ElectricApparentEnergyUnits = ElectricApparentEnergyUnits.VoltampereHour) -> str:
        """
        Get ElectricApparentEnergy unit abbreviation.
        Note! the default abbreviation for ElectricApparentEnergy is VoltampereHour.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == ElectricApparentEnergyUnits.VoltampereHour:
            return """VAh"""
        
        if unit_abbreviation == ElectricApparentEnergyUnits.KilovoltampereHour:
            return """kVAh"""
        
        if unit_abbreviation == ElectricApparentEnergyUnits.MegavoltampereHour:
            return """MVAh"""
        
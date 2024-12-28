from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class ElectricReactiveEnergyUnits(Enum):
        """
            ElectricReactiveEnergyUnits enumeration
        """
        
        VoltampereReactiveHour = 'VoltampereReactiveHour'
        """
            
        """
        
        KilovoltampereReactiveHour = 'KilovoltampereReactiveHour'
        """
            
        """
        
        MegavoltampereReactiveHour = 'MegavoltampereReactiveHour'
        """
            
        """
        

class ElectricReactiveEnergyDto:
    """
    A DTO representation of a ElectricReactiveEnergy

    Attributes:
        value (float): The value of the ElectricReactiveEnergy.
        unit (ElectricReactiveEnergyUnits): The specific unit that the ElectricReactiveEnergy value is representing.
    """

    def __init__(self, value: float, unit: ElectricReactiveEnergyUnits):
        """
        Create a new DTO representation of a ElectricReactiveEnergy

        Parameters:
            value (float): The value of the ElectricReactiveEnergy.
            unit (ElectricReactiveEnergyUnits): The specific unit that the ElectricReactiveEnergy value is representing.
        """
        self.value: float = value
        """
        The value of the ElectricReactiveEnergy
        """
        self.unit: ElectricReactiveEnergyUnits = unit
        """
        The specific unit that the ElectricReactiveEnergy value is representing
        """

    def to_json(self):
        """
        Get a ElectricReactiveEnergy DTO JSON object representing the current unit.

        :return: JSON object represents ElectricReactiveEnergy DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "VoltampereReactiveHour"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of ElectricReactiveEnergy DTO from a json representation.

        :param data: The ElectricReactiveEnergy DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "VoltampereReactiveHour"}
        :return: A new instance of ElectricReactiveEnergyDto.
        :rtype: ElectricReactiveEnergyDto
        """
        return ElectricReactiveEnergyDto(value=data["value"], unit=ElectricReactiveEnergyUnits(data["unit"]))


class ElectricReactiveEnergy(AbstractMeasure):
    """
    The volt-ampere reactive hour (expressed as varh) is the reactive power of one Volt-ampere reactive produced in one hour.

    Args:
        value (float): The value.
        from_unit (ElectricReactiveEnergyUnits): The ElectricReactiveEnergy unit to create from, The default unit is VoltampereReactiveHour
    """
    def __init__(self, value: float, from_unit: ElectricReactiveEnergyUnits = ElectricReactiveEnergyUnits.VoltampereReactiveHour):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__voltampere_reactive_hours = None
        
        self.__kilovoltampere_reactive_hours = None
        
        self.__megavoltampere_reactive_hours = None
        

    def convert(self, unit: ElectricReactiveEnergyUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: ElectricReactiveEnergyUnits = ElectricReactiveEnergyUnits.VoltampereReactiveHour) -> ElectricReactiveEnergyDto:
        """
        Get a new instance of ElectricReactiveEnergy DTO representing the current unit.

        :param hold_in_unit: The specific ElectricReactiveEnergy unit to store the ElectricReactiveEnergy value in the DTO representation.
        :type hold_in_unit: ElectricReactiveEnergyUnits
        :return: A new instance of ElectricReactiveEnergyDto.
        :rtype: ElectricReactiveEnergyDto
        """
        return ElectricReactiveEnergyDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: ElectricReactiveEnergyUnits = ElectricReactiveEnergyUnits.VoltampereReactiveHour):
        """
        Get a ElectricReactiveEnergy DTO JSON object representing the current unit.

        :param hold_in_unit: The specific ElectricReactiveEnergy unit to store the ElectricReactiveEnergy value in the DTO representation.
        :type hold_in_unit: ElectricReactiveEnergyUnits
        :return: JSON object represents ElectricReactiveEnergy DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "VoltampereReactiveHour"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(electric_reactive_energy_dto: ElectricReactiveEnergyDto):
        """
        Obtain a new instance of ElectricReactiveEnergy from a DTO unit object.

        :param electric_reactive_energy_dto: The ElectricReactiveEnergy DTO representation.
        :type electric_reactive_energy_dto: ElectricReactiveEnergyDto
        :return: A new instance of ElectricReactiveEnergy.
        :rtype: ElectricReactiveEnergy
        """
        return ElectricReactiveEnergy(electric_reactive_energy_dto.value, electric_reactive_energy_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of ElectricReactiveEnergy from a DTO unit json representation.

        :param data: The ElectricReactiveEnergy DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "VoltampereReactiveHour"}
        :return: A new instance of ElectricReactiveEnergy.
        :rtype: ElectricReactiveEnergy
        """
        return ElectricReactiveEnergy.from_dto(ElectricReactiveEnergyDto.from_json(data))

    def __convert_from_base(self, from_unit: ElectricReactiveEnergyUnits) -> float:
        value = self._value
        
        if from_unit == ElectricReactiveEnergyUnits.VoltampereReactiveHour:
            return (value)
        
        if from_unit == ElectricReactiveEnergyUnits.KilovoltampereReactiveHour:
            return ((value) / 1000.0)
        
        if from_unit == ElectricReactiveEnergyUnits.MegavoltampereReactiveHour:
            return ((value) / 1000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: ElectricReactiveEnergyUnits) -> float:
        
        if to_unit == ElectricReactiveEnergyUnits.VoltampereReactiveHour:
            return (value)
        
        if to_unit == ElectricReactiveEnergyUnits.KilovoltampereReactiveHour:
            return ((value) * 1000.0)
        
        if to_unit == ElectricReactiveEnergyUnits.MegavoltampereReactiveHour:
            return ((value) * 1000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_voltampere_reactive_hours(voltampere_reactive_hours: float):
        """
        Create a new instance of ElectricReactiveEnergy from a value in voltampere_reactive_hours.

        

        :param meters: The ElectricReactiveEnergy value in voltampere_reactive_hours.
        :type voltampere_reactive_hours: float
        :return: A new instance of ElectricReactiveEnergy.
        :rtype: ElectricReactiveEnergy
        """
        return ElectricReactiveEnergy(voltampere_reactive_hours, ElectricReactiveEnergyUnits.VoltampereReactiveHour)

    
    @staticmethod
    def from_kilovoltampere_reactive_hours(kilovoltampere_reactive_hours: float):
        """
        Create a new instance of ElectricReactiveEnergy from a value in kilovoltampere_reactive_hours.

        

        :param meters: The ElectricReactiveEnergy value in kilovoltampere_reactive_hours.
        :type kilovoltampere_reactive_hours: float
        :return: A new instance of ElectricReactiveEnergy.
        :rtype: ElectricReactiveEnergy
        """
        return ElectricReactiveEnergy(kilovoltampere_reactive_hours, ElectricReactiveEnergyUnits.KilovoltampereReactiveHour)

    
    @staticmethod
    def from_megavoltampere_reactive_hours(megavoltampere_reactive_hours: float):
        """
        Create a new instance of ElectricReactiveEnergy from a value in megavoltampere_reactive_hours.

        

        :param meters: The ElectricReactiveEnergy value in megavoltampere_reactive_hours.
        :type megavoltampere_reactive_hours: float
        :return: A new instance of ElectricReactiveEnergy.
        :rtype: ElectricReactiveEnergy
        """
        return ElectricReactiveEnergy(megavoltampere_reactive_hours, ElectricReactiveEnergyUnits.MegavoltampereReactiveHour)

    
    @property
    def voltampere_reactive_hours(self) -> float:
        """
        
        """
        if self.__voltampere_reactive_hours != None:
            return self.__voltampere_reactive_hours
        self.__voltampere_reactive_hours = self.__convert_from_base(ElectricReactiveEnergyUnits.VoltampereReactiveHour)
        return self.__voltampere_reactive_hours

    
    @property
    def kilovoltampere_reactive_hours(self) -> float:
        """
        
        """
        if self.__kilovoltampere_reactive_hours != None:
            return self.__kilovoltampere_reactive_hours
        self.__kilovoltampere_reactive_hours = self.__convert_from_base(ElectricReactiveEnergyUnits.KilovoltampereReactiveHour)
        return self.__kilovoltampere_reactive_hours

    
    @property
    def megavoltampere_reactive_hours(self) -> float:
        """
        
        """
        if self.__megavoltampere_reactive_hours != None:
            return self.__megavoltampere_reactive_hours
        self.__megavoltampere_reactive_hours = self.__convert_from_base(ElectricReactiveEnergyUnits.MegavoltampereReactiveHour)
        return self.__megavoltampere_reactive_hours

    
    def to_string(self, unit: ElectricReactiveEnergyUnits = ElectricReactiveEnergyUnits.VoltampereReactiveHour, fractional_digits: int = None) -> str:
        """
        Format the ElectricReactiveEnergy to a string.
        
        Note: the default format for ElectricReactiveEnergy is VoltampereReactiveHour.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the ElectricReactiveEnergy. Default is 'VoltampereReactiveHour'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == ElectricReactiveEnergyUnits.VoltampereReactiveHour:
            return f"""{super()._truncate_fraction_digits(self.voltampere_reactive_hours, fractional_digits)} varh"""
        
        if unit == ElectricReactiveEnergyUnits.KilovoltampereReactiveHour:
            return f"""{super()._truncate_fraction_digits(self.kilovoltampere_reactive_hours, fractional_digits)} kvarh"""
        
        if unit == ElectricReactiveEnergyUnits.MegavoltampereReactiveHour:
            return f"""{super()._truncate_fraction_digits(self.megavoltampere_reactive_hours, fractional_digits)} Mvarh"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: ElectricReactiveEnergyUnits = ElectricReactiveEnergyUnits.VoltampereReactiveHour) -> str:
        """
        Get ElectricReactiveEnergy unit abbreviation.
        Note! the default abbreviation for ElectricReactiveEnergy is VoltampereReactiveHour.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == ElectricReactiveEnergyUnits.VoltampereReactiveHour:
            return """varh"""
        
        if unit_abbreviation == ElectricReactiveEnergyUnits.KilovoltampereReactiveHour:
            return """kvarh"""
        
        if unit_abbreviation == ElectricReactiveEnergyUnits.MegavoltampereReactiveHour:
            return """Mvarh"""
        
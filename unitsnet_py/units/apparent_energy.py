from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class ApparentEnergyUnits(Enum):
        """
            ApparentEnergyUnits enumeration
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
        

class ApparentEnergyDto:
    """
    A DTO representation of a ApparentEnergy

    Attributes:
        value (float): The value of the ApparentEnergy.
        unit (ApparentEnergyUnits): The specific unit that the ApparentEnergy value is representing.
    """

    def __init__(self, value: float, unit: ApparentEnergyUnits):
        """
        Create a new DTO representation of a ApparentEnergy

        Parameters:
            value (float): The value of the ApparentEnergy.
            unit (ApparentEnergyUnits): The specific unit that the ApparentEnergy value is representing.
        """
        self.value: float = value
        """
        The value of the ApparentEnergy
        """
        self.unit: ApparentEnergyUnits = unit
        """
        The specific unit that the ApparentEnergy value is representing
        """

    def to_json(self):
        """
        Get a ApparentEnergy DTO JSON object representing the current unit.

        :return: JSON object represents ApparentEnergy DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "VoltampereHour"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of ApparentEnergy DTO from a json representation.

        :param data: The ApparentEnergy DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "VoltampereHour"}
        :return: A new instance of ApparentEnergyDto.
        :rtype: ApparentEnergyDto
        """
        return ApparentEnergyDto(value=data["value"], unit=ApparentEnergyUnits(data["unit"]))


class ApparentEnergy(AbstractMeasure):
    """
    A unit for expressing the integral of apparent power over time, equal to the product of 1 volt-ampere and 1 hour, or to 3600 joules.

    Args:
        value (float): The value.
        from_unit (ApparentEnergyUnits): The ApparentEnergy unit to create from, The default unit is VoltampereHour
    """
    def __init__(self, value: float, from_unit: ApparentEnergyUnits = ApparentEnergyUnits.VoltampereHour):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__voltampere_hours = None
        
        self.__kilovoltampere_hours = None
        
        self.__megavoltampere_hours = None
        

    def convert(self, unit: ApparentEnergyUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: ApparentEnergyUnits = ApparentEnergyUnits.VoltampereHour) -> ApparentEnergyDto:
        """
        Get a new instance of ApparentEnergy DTO representing the current unit.

        :param hold_in_unit: The specific ApparentEnergy unit to store the ApparentEnergy value in the DTO representation.
        :type hold_in_unit: ApparentEnergyUnits
        :return: A new instance of ApparentEnergyDto.
        :rtype: ApparentEnergyDto
        """
        return ApparentEnergyDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: ApparentEnergyUnits = ApparentEnergyUnits.VoltampereHour):
        """
        Get a ApparentEnergy DTO JSON object representing the current unit.

        :param hold_in_unit: The specific ApparentEnergy unit to store the ApparentEnergy value in the DTO representation.
        :type hold_in_unit: ApparentEnergyUnits
        :return: JSON object represents ApparentEnergy DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "VoltampereHour"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(apparent_energy_dto: ApparentEnergyDto):
        """
        Obtain a new instance of ApparentEnergy from a DTO unit object.

        :param apparent_energy_dto: The ApparentEnergy DTO representation.
        :type apparent_energy_dto: ApparentEnergyDto
        :return: A new instance of ApparentEnergy.
        :rtype: ApparentEnergy
        """
        return ApparentEnergy(apparent_energy_dto.value, apparent_energy_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of ApparentEnergy from a DTO unit json representation.

        :param data: The ApparentEnergy DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "VoltampereHour"}
        :return: A new instance of ApparentEnergy.
        :rtype: ApparentEnergy
        """
        return ApparentEnergy.from_dto(ApparentEnergyDto.from_json(data))

    def __convert_from_base(self, from_unit: ApparentEnergyUnits) -> float:
        value = self._value
        
        if from_unit == ApparentEnergyUnits.VoltampereHour:
            return (value)
        
        if from_unit == ApparentEnergyUnits.KilovoltampereHour:
            return ((value) / 1000.0)
        
        if from_unit == ApparentEnergyUnits.MegavoltampereHour:
            return ((value) / 1000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: ApparentEnergyUnits) -> float:
        
        if to_unit == ApparentEnergyUnits.VoltampereHour:
            return (value)
        
        if to_unit == ApparentEnergyUnits.KilovoltampereHour:
            return ((value) * 1000.0)
        
        if to_unit == ApparentEnergyUnits.MegavoltampereHour:
            return ((value) * 1000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_voltampere_hours(voltampere_hours: float):
        """
        Create a new instance of ApparentEnergy from a value in voltampere_hours.

        

        :param meters: The ApparentEnergy value in voltampere_hours.
        :type voltampere_hours: float
        :return: A new instance of ApparentEnergy.
        :rtype: ApparentEnergy
        """
        return ApparentEnergy(voltampere_hours, ApparentEnergyUnits.VoltampereHour)

    
    @staticmethod
    def from_kilovoltampere_hours(kilovoltampere_hours: float):
        """
        Create a new instance of ApparentEnergy from a value in kilovoltampere_hours.

        

        :param meters: The ApparentEnergy value in kilovoltampere_hours.
        :type kilovoltampere_hours: float
        :return: A new instance of ApparentEnergy.
        :rtype: ApparentEnergy
        """
        return ApparentEnergy(kilovoltampere_hours, ApparentEnergyUnits.KilovoltampereHour)

    
    @staticmethod
    def from_megavoltampere_hours(megavoltampere_hours: float):
        """
        Create a new instance of ApparentEnergy from a value in megavoltampere_hours.

        

        :param meters: The ApparentEnergy value in megavoltampere_hours.
        :type megavoltampere_hours: float
        :return: A new instance of ApparentEnergy.
        :rtype: ApparentEnergy
        """
        return ApparentEnergy(megavoltampere_hours, ApparentEnergyUnits.MegavoltampereHour)

    
    @property
    def voltampere_hours(self) -> float:
        """
        
        """
        if self.__voltampere_hours != None:
            return self.__voltampere_hours
        self.__voltampere_hours = self.__convert_from_base(ApparentEnergyUnits.VoltampereHour)
        return self.__voltampere_hours

    
    @property
    def kilovoltampere_hours(self) -> float:
        """
        
        """
        if self.__kilovoltampere_hours != None:
            return self.__kilovoltampere_hours
        self.__kilovoltampere_hours = self.__convert_from_base(ApparentEnergyUnits.KilovoltampereHour)
        return self.__kilovoltampere_hours

    
    @property
    def megavoltampere_hours(self) -> float:
        """
        
        """
        if self.__megavoltampere_hours != None:
            return self.__megavoltampere_hours
        self.__megavoltampere_hours = self.__convert_from_base(ApparentEnergyUnits.MegavoltampereHour)
        return self.__megavoltampere_hours

    
    def to_string(self, unit: ApparentEnergyUnits = ApparentEnergyUnits.VoltampereHour, fractional_digits: int = None) -> str:
        """
        Format the ApparentEnergy to a string.
        
        Note: the default format for ApparentEnergy is VoltampereHour.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the ApparentEnergy. Default is 'VoltampereHour'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == ApparentEnergyUnits.VoltampereHour:
            return f"""{super()._truncate_fraction_digits(self.voltampere_hours, fractional_digits)} VAh"""
        
        if unit == ApparentEnergyUnits.KilovoltampereHour:
            return f"""{super()._truncate_fraction_digits(self.kilovoltampere_hours, fractional_digits)} kVAh"""
        
        if unit == ApparentEnergyUnits.MegavoltampereHour:
            return f"""{super()._truncate_fraction_digits(self.megavoltampere_hours, fractional_digits)} MVAh"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: ApparentEnergyUnits = ApparentEnergyUnits.VoltampereHour) -> str:
        """
        Get ApparentEnergy unit abbreviation.
        Note! the default abbreviation for ApparentEnergy is VoltampereHour.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == ApparentEnergyUnits.VoltampereHour:
            return """VAh"""
        
        if unit_abbreviation == ApparentEnergyUnits.KilovoltampereHour:
            return """kVAh"""
        
        if unit_abbreviation == ApparentEnergyUnits.MegavoltampereHour:
            return """MVAh"""
        
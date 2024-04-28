from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class PowerRatioUnits(Enum):
        """
            PowerRatioUnits enumeration
        """
        
        DecibelWatt = 'DecibelWatt'
        """
            
        """
        
        DecibelMilliwatt = 'DecibelMilliwatt'
        """
            
        """
        

class PowerRatioDto:
    """
    A DTO representation of a PowerRatio

    Attributes:
        value (float): The value of the PowerRatio.
        unit (PowerRatioUnits): The specific unit that the PowerRatio value is representing.
    """

    def __init__(self, value: float, unit: PowerRatioUnits):
        """
        Create a new DTO representation of a PowerRatio

        Parameters:
            value (float): The value of the PowerRatio.
            unit (PowerRatioUnits): The specific unit that the PowerRatio value is representing.
        """
        self.value: float = value
        """
        The value of the PowerRatio
        """
        self.unit: PowerRatioUnits = unit
        """
        The specific unit that the PowerRatio value is representing
        """

    def to_json(self):
        """
        Get a PowerRatio DTO JSON object representing the current unit.

        :return: JSON object represents PowerRatio DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "DecibelWatt"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of PowerRatio DTO from a json representation.

        :param data: The PowerRatio DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "DecibelWatt"}
        :return: A new instance of PowerRatioDto.
        :rtype: PowerRatioDto
        """
        return PowerRatioDto(value=data["value"], unit=PowerRatioUnits(data["unit"]))


class PowerRatio(AbstractMeasure):
    """
    The strength of a signal expressed in decibels (dB) relative to one watt.

    Args:
        value (float): The value.
        from_unit (PowerRatioUnits): The PowerRatio unit to create from, The default unit is DecibelWatt
    """
    def __init__(self, value: float, from_unit: PowerRatioUnits = PowerRatioUnits.DecibelWatt):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__decibel_watts = None
        
        self.__decibel_milliwatts = None
        

    def convert(self, unit: PowerRatioUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: PowerRatioUnits = PowerRatioUnits.DecibelWatt) -> PowerRatioDto:
        """
        Get a new instance of PowerRatio DTO representing the current unit.

        :param hold_in_unit: The specific PowerRatio unit to store the PowerRatio value in the DTO representation.
        :type hold_in_unit: PowerRatioUnits
        :return: A new instance of PowerRatioDto.
        :rtype: PowerRatioDto
        """
        return PowerRatioDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: PowerRatioUnits = PowerRatioUnits.DecibelWatt):
        """
        Get a PowerRatio DTO JSON object representing the current unit.

        :param hold_in_unit: The specific PowerRatio unit to store the PowerRatio value in the DTO representation.
        :type hold_in_unit: PowerRatioUnits
        :return: JSON object represents PowerRatio DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "DecibelWatt"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(power_ratio_dto: PowerRatioDto):
        """
        Obtain a new instance of PowerRatio from a DTO unit object.

        :param power_ratio_dto: The PowerRatio DTO representation.
        :type power_ratio_dto: PowerRatioDto
        :return: A new instance of PowerRatio.
        :rtype: PowerRatio
        """
        return PowerRatio(power_ratio_dto.value, power_ratio_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of PowerRatio from a DTO unit json representation.

        :param data: The PowerRatio DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "DecibelWatt"}
        :return: A new instance of PowerRatio.
        :rtype: PowerRatio
        """
        return PowerRatio.from_dto(PowerRatioDto.from_json(data))

    def __convert_from_base(self, from_unit: PowerRatioUnits) -> float:
        value = self._value
        
        if from_unit == PowerRatioUnits.DecibelWatt:
            return (value)
        
        if from_unit == PowerRatioUnits.DecibelMilliwatt:
            return (value + 30)
        
        return None


    def __convert_to_base(self, value: float, to_unit: PowerRatioUnits) -> float:
        
        if to_unit == PowerRatioUnits.DecibelWatt:
            return (value)
        
        if to_unit == PowerRatioUnits.DecibelMilliwatt:
            return (value - 30)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_decibel_watts(decibel_watts: float):
        """
        Create a new instance of PowerRatio from a value in decibel_watts.

        

        :param meters: The PowerRatio value in decibel_watts.
        :type decibel_watts: float
        :return: A new instance of PowerRatio.
        :rtype: PowerRatio
        """
        return PowerRatio(decibel_watts, PowerRatioUnits.DecibelWatt)

    
    @staticmethod
    def from_decibel_milliwatts(decibel_milliwatts: float):
        """
        Create a new instance of PowerRatio from a value in decibel_milliwatts.

        

        :param meters: The PowerRatio value in decibel_milliwatts.
        :type decibel_milliwatts: float
        :return: A new instance of PowerRatio.
        :rtype: PowerRatio
        """
        return PowerRatio(decibel_milliwatts, PowerRatioUnits.DecibelMilliwatt)

    
    @property
    def decibel_watts(self) -> float:
        """
        
        """
        if self.__decibel_watts != None:
            return self.__decibel_watts
        self.__decibel_watts = self.__convert_from_base(PowerRatioUnits.DecibelWatt)
        return self.__decibel_watts

    
    @property
    def decibel_milliwatts(self) -> float:
        """
        
        """
        if self.__decibel_milliwatts != None:
            return self.__decibel_milliwatts
        self.__decibel_milliwatts = self.__convert_from_base(PowerRatioUnits.DecibelMilliwatt)
        return self.__decibel_milliwatts

    
    def to_string(self, unit: PowerRatioUnits = PowerRatioUnits.DecibelWatt, fractional_digits: int = None) -> str:
        """
        Format the PowerRatio to a string.
        
        Note: the default format for PowerRatio is DecibelWatt.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the PowerRatio. Default is 'DecibelWatt'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == PowerRatioUnits.DecibelWatt:
            return f"""{super()._truncate_fraction_digits(self.decibel_watts, fractional_digits)} dBW"""
        
        if unit == PowerRatioUnits.DecibelMilliwatt:
            return f"""{super()._truncate_fraction_digits(self.decibel_milliwatts, fractional_digits)} dBmW"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: PowerRatioUnits = PowerRatioUnits.DecibelWatt) -> str:
        """
        Get PowerRatio unit abbreviation.
        Note! the default abbreviation for PowerRatio is DecibelWatt.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == PowerRatioUnits.DecibelWatt:
            return """dBW"""
        
        if unit_abbreviation == PowerRatioUnits.DecibelMilliwatt:
            return """dBmW"""
        
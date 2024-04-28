from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class RatioChangeRateUnits(Enum):
        """
            RatioChangeRateUnits enumeration
        """
        
        PercentPerSecond = 'PercentPerSecond'
        """
            
        """
        
        DecimalFractionPerSecond = 'DecimalFractionPerSecond'
        """
            
        """
        

class RatioChangeRateDto:
    """
    A DTO representation of a RatioChangeRate

    Attributes:
        value (float): The value of the RatioChangeRate.
        unit (RatioChangeRateUnits): The specific unit that the RatioChangeRate value is representing.
    """

    def __init__(self, value: float, unit: RatioChangeRateUnits):
        """
        Create a new DTO representation of a RatioChangeRate

        Parameters:
            value (float): The value of the RatioChangeRate.
            unit (RatioChangeRateUnits): The specific unit that the RatioChangeRate value is representing.
        """
        self.value: float = value
        """
        The value of the RatioChangeRate
        """
        self.unit: RatioChangeRateUnits = unit
        """
        The specific unit that the RatioChangeRate value is representing
        """

    def to_json(self):
        """
        Get a RatioChangeRate DTO JSON object representing the current unit.

        :return: JSON object represents RatioChangeRate DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "DecimalFractionPerSecond"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of RatioChangeRate DTO from a json representation.

        :param data: The RatioChangeRate DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "DecimalFractionPerSecond"}
        :return: A new instance of RatioChangeRateDto.
        :rtype: RatioChangeRateDto
        """
        return RatioChangeRateDto(value=data["value"], unit=RatioChangeRateUnits(data["unit"]))


class RatioChangeRate(AbstractMeasure):
    """
    The change in ratio per unit of time.

    Args:
        value (float): The value.
        from_unit (RatioChangeRateUnits): The RatioChangeRate unit to create from, The default unit is DecimalFractionPerSecond
    """
    def __init__(self, value: float, from_unit: RatioChangeRateUnits = RatioChangeRateUnits.DecimalFractionPerSecond):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__percents_per_second = None
        
        self.__decimal_fractions_per_second = None
        

    def convert(self, unit: RatioChangeRateUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: RatioChangeRateUnits = RatioChangeRateUnits.DecimalFractionPerSecond) -> RatioChangeRateDto:
        """
        Get a new instance of RatioChangeRate DTO representing the current unit.

        :param hold_in_unit: The specific RatioChangeRate unit to store the RatioChangeRate value in the DTO representation.
        :type hold_in_unit: RatioChangeRateUnits
        :return: A new instance of RatioChangeRateDto.
        :rtype: RatioChangeRateDto
        """
        return RatioChangeRateDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: RatioChangeRateUnits = RatioChangeRateUnits.DecimalFractionPerSecond):
        """
        Get a RatioChangeRate DTO JSON object representing the current unit.

        :param hold_in_unit: The specific RatioChangeRate unit to store the RatioChangeRate value in the DTO representation.
        :type hold_in_unit: RatioChangeRateUnits
        :return: JSON object represents RatioChangeRate DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "DecimalFractionPerSecond"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(ratio_change_rate_dto: RatioChangeRateDto):
        """
        Obtain a new instance of RatioChangeRate from a DTO unit object.

        :param ratio_change_rate_dto: The RatioChangeRate DTO representation.
        :type ratio_change_rate_dto: RatioChangeRateDto
        :return: A new instance of RatioChangeRate.
        :rtype: RatioChangeRate
        """
        return RatioChangeRate(ratio_change_rate_dto.value, ratio_change_rate_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of RatioChangeRate from a DTO unit json representation.

        :param data: The RatioChangeRate DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "DecimalFractionPerSecond"}
        :return: A new instance of RatioChangeRate.
        :rtype: RatioChangeRate
        """
        return RatioChangeRate.from_dto(RatioChangeRateDto.from_json(data))

    def __convert_from_base(self, from_unit: RatioChangeRateUnits) -> float:
        value = self._value
        
        if from_unit == RatioChangeRateUnits.PercentPerSecond:
            return (value * 1e2)
        
        if from_unit == RatioChangeRateUnits.DecimalFractionPerSecond:
            return (value)
        
        return None


    def __convert_to_base(self, value: float, to_unit: RatioChangeRateUnits) -> float:
        
        if to_unit == RatioChangeRateUnits.PercentPerSecond:
            return (value / 1e2)
        
        if to_unit == RatioChangeRateUnits.DecimalFractionPerSecond:
            return (value)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_percents_per_second(percents_per_second: float):
        """
        Create a new instance of RatioChangeRate from a value in percents_per_second.

        

        :param meters: The RatioChangeRate value in percents_per_second.
        :type percents_per_second: float
        :return: A new instance of RatioChangeRate.
        :rtype: RatioChangeRate
        """
        return RatioChangeRate(percents_per_second, RatioChangeRateUnits.PercentPerSecond)

    
    @staticmethod
    def from_decimal_fractions_per_second(decimal_fractions_per_second: float):
        """
        Create a new instance of RatioChangeRate from a value in decimal_fractions_per_second.

        

        :param meters: The RatioChangeRate value in decimal_fractions_per_second.
        :type decimal_fractions_per_second: float
        :return: A new instance of RatioChangeRate.
        :rtype: RatioChangeRate
        """
        return RatioChangeRate(decimal_fractions_per_second, RatioChangeRateUnits.DecimalFractionPerSecond)

    
    @property
    def percents_per_second(self) -> float:
        """
        
        """
        if self.__percents_per_second != None:
            return self.__percents_per_second
        self.__percents_per_second = self.__convert_from_base(RatioChangeRateUnits.PercentPerSecond)
        return self.__percents_per_second

    
    @property
    def decimal_fractions_per_second(self) -> float:
        """
        
        """
        if self.__decimal_fractions_per_second != None:
            return self.__decimal_fractions_per_second
        self.__decimal_fractions_per_second = self.__convert_from_base(RatioChangeRateUnits.DecimalFractionPerSecond)
        return self.__decimal_fractions_per_second

    
    def to_string(self, unit: RatioChangeRateUnits = RatioChangeRateUnits.DecimalFractionPerSecond, fractional_digits: int = None) -> str:
        """
        Format the RatioChangeRate to a string.
        
        Note: the default format for RatioChangeRate is DecimalFractionPerSecond.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the RatioChangeRate. Default is 'DecimalFractionPerSecond'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == RatioChangeRateUnits.PercentPerSecond:
            return f"""{super()._truncate_fraction_digits(self.percents_per_second, fractional_digits)} %/s"""
        
        if unit == RatioChangeRateUnits.DecimalFractionPerSecond:
            return f"""{super()._truncate_fraction_digits(self.decimal_fractions_per_second, fractional_digits)} /s"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: RatioChangeRateUnits = RatioChangeRateUnits.DecimalFractionPerSecond) -> str:
        """
        Get RatioChangeRate unit abbreviation.
        Note! the default abbreviation for RatioChangeRate is DecimalFractionPerSecond.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == RatioChangeRateUnits.PercentPerSecond:
            return """%/s"""
        
        if unit_abbreviation == RatioChangeRateUnits.DecimalFractionPerSecond:
            return """/s"""
        
from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class RatioUnits(Enum):
        """
            RatioUnits enumeration
        """
        
        DecimalFraction = 'DecimalFraction'
        """
            
        """
        
        Percent = 'Percent'
        """
            
        """
        
        PartPerThousand = 'PartPerThousand'
        """
            
        """
        
        PartPerMillion = 'PartPerMillion'
        """
            
        """
        
        PartPerBillion = 'PartPerBillion'
        """
            
        """
        
        PartPerTrillion = 'PartPerTrillion'
        """
            
        """
        

class RatioDto:
    """
    A DTO representation of a Ratio

    Attributes:
        value (float): The value of the Ratio.
        unit (RatioUnits): The specific unit that the Ratio value is representing.
    """

    def __init__(self, value: float, unit: RatioUnits):
        """
        Create a new DTO representation of a Ratio

        Parameters:
            value (float): The value of the Ratio.
            unit (RatioUnits): The specific unit that the Ratio value is representing.
        """
        self.value: float = value
        """
        The value of the Ratio
        """
        self.unit: RatioUnits = unit
        """
        The specific unit that the Ratio value is representing
        """

    def to_json(self):
        """
        Get a Ratio DTO JSON object representing the current unit.

        :return: JSON object represents Ratio DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "DecimalFraction"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of Ratio DTO from a json representation.

        :param data: The Ratio DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "DecimalFraction"}
        :return: A new instance of RatioDto.
        :rtype: RatioDto
        """
        return RatioDto(value=data["value"], unit=RatioUnits(data["unit"]))


class Ratio(AbstractMeasure):
    """
    In mathematics, a ratio is a relationship between two numbers of the same kind (e.g., objects, persons, students, spoonfuls, units of whatever identical dimension), usually expressed as "a to b" or a:b, sometimes expressed arithmetically as a dimensionless quotient of the two that explicitly indicates how many times the first number contains the second (not necessarily an integer).

    Args:
        value (float): The value.
        from_unit (RatioUnits): The Ratio unit to create from, The default unit is DecimalFraction
    """
    def __init__(self, value: float, from_unit: RatioUnits = RatioUnits.DecimalFraction):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__decimal_fractions = None
        
        self.__percent = None
        
        self.__parts_per_thousand = None
        
        self.__parts_per_million = None
        
        self.__parts_per_billion = None
        
        self.__parts_per_trillion = None
        

    def convert(self, unit: RatioUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: RatioUnits = RatioUnits.DecimalFraction) -> RatioDto:
        """
        Get a new instance of Ratio DTO representing the current unit.

        :param hold_in_unit: The specific Ratio unit to store the Ratio value in the DTO representation.
        :type hold_in_unit: RatioUnits
        :return: A new instance of RatioDto.
        :rtype: RatioDto
        """
        return RatioDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: RatioUnits = RatioUnits.DecimalFraction):
        """
        Get a Ratio DTO JSON object representing the current unit.

        :param hold_in_unit: The specific Ratio unit to store the Ratio value in the DTO representation.
        :type hold_in_unit: RatioUnits
        :return: JSON object represents Ratio DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "DecimalFraction"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(ratio_dto: RatioDto):
        """
        Obtain a new instance of Ratio from a DTO unit object.

        :param ratio_dto: The Ratio DTO representation.
        :type ratio_dto: RatioDto
        :return: A new instance of Ratio.
        :rtype: Ratio
        """
        return Ratio(ratio_dto.value, ratio_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of Ratio from a DTO unit json representation.

        :param data: The Ratio DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "DecimalFraction"}
        :return: A new instance of Ratio.
        :rtype: Ratio
        """
        return Ratio.from_dto(RatioDto.from_json(data))

    def __convert_from_base(self, from_unit: RatioUnits) -> float:
        value = self._value
        
        if from_unit == RatioUnits.DecimalFraction:
            return (value)
        
        if from_unit == RatioUnits.Percent:
            return (value * 1e2)
        
        if from_unit == RatioUnits.PartPerThousand:
            return (value * 1e3)
        
        if from_unit == RatioUnits.PartPerMillion:
            return (value * 1e6)
        
        if from_unit == RatioUnits.PartPerBillion:
            return (value * 1e9)
        
        if from_unit == RatioUnits.PartPerTrillion:
            return (value * 1e12)
        
        return None


    def __convert_to_base(self, value: float, to_unit: RatioUnits) -> float:
        
        if to_unit == RatioUnits.DecimalFraction:
            return (value)
        
        if to_unit == RatioUnits.Percent:
            return (value / 1e2)
        
        if to_unit == RatioUnits.PartPerThousand:
            return (value / 1e3)
        
        if to_unit == RatioUnits.PartPerMillion:
            return (value / 1e6)
        
        if to_unit == RatioUnits.PartPerBillion:
            return (value / 1e9)
        
        if to_unit == RatioUnits.PartPerTrillion:
            return (value / 1e12)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_decimal_fractions(decimal_fractions: float):
        """
        Create a new instance of Ratio from a value in decimal_fractions.

        

        :param meters: The Ratio value in decimal_fractions.
        :type decimal_fractions: float
        :return: A new instance of Ratio.
        :rtype: Ratio
        """
        return Ratio(decimal_fractions, RatioUnits.DecimalFraction)

    
    @staticmethod
    def from_percent(percent: float):
        """
        Create a new instance of Ratio from a value in percent.

        

        :param meters: The Ratio value in percent.
        :type percent: float
        :return: A new instance of Ratio.
        :rtype: Ratio
        """
        return Ratio(percent, RatioUnits.Percent)

    
    @staticmethod
    def from_parts_per_thousand(parts_per_thousand: float):
        """
        Create a new instance of Ratio from a value in parts_per_thousand.

        

        :param meters: The Ratio value in parts_per_thousand.
        :type parts_per_thousand: float
        :return: A new instance of Ratio.
        :rtype: Ratio
        """
        return Ratio(parts_per_thousand, RatioUnits.PartPerThousand)

    
    @staticmethod
    def from_parts_per_million(parts_per_million: float):
        """
        Create a new instance of Ratio from a value in parts_per_million.

        

        :param meters: The Ratio value in parts_per_million.
        :type parts_per_million: float
        :return: A new instance of Ratio.
        :rtype: Ratio
        """
        return Ratio(parts_per_million, RatioUnits.PartPerMillion)

    
    @staticmethod
    def from_parts_per_billion(parts_per_billion: float):
        """
        Create a new instance of Ratio from a value in parts_per_billion.

        

        :param meters: The Ratio value in parts_per_billion.
        :type parts_per_billion: float
        :return: A new instance of Ratio.
        :rtype: Ratio
        """
        return Ratio(parts_per_billion, RatioUnits.PartPerBillion)

    
    @staticmethod
    def from_parts_per_trillion(parts_per_trillion: float):
        """
        Create a new instance of Ratio from a value in parts_per_trillion.

        

        :param meters: The Ratio value in parts_per_trillion.
        :type parts_per_trillion: float
        :return: A new instance of Ratio.
        :rtype: Ratio
        """
        return Ratio(parts_per_trillion, RatioUnits.PartPerTrillion)

    
    @property
    def decimal_fractions(self) -> float:
        """
        
        """
        if self.__decimal_fractions != None:
            return self.__decimal_fractions
        self.__decimal_fractions = self.__convert_from_base(RatioUnits.DecimalFraction)
        return self.__decimal_fractions

    
    @property
    def percent(self) -> float:
        """
        
        """
        if self.__percent != None:
            return self.__percent
        self.__percent = self.__convert_from_base(RatioUnits.Percent)
        return self.__percent

    
    @property
    def parts_per_thousand(self) -> float:
        """
        
        """
        if self.__parts_per_thousand != None:
            return self.__parts_per_thousand
        self.__parts_per_thousand = self.__convert_from_base(RatioUnits.PartPerThousand)
        return self.__parts_per_thousand

    
    @property
    def parts_per_million(self) -> float:
        """
        
        """
        if self.__parts_per_million != None:
            return self.__parts_per_million
        self.__parts_per_million = self.__convert_from_base(RatioUnits.PartPerMillion)
        return self.__parts_per_million

    
    @property
    def parts_per_billion(self) -> float:
        """
        
        """
        if self.__parts_per_billion != None:
            return self.__parts_per_billion
        self.__parts_per_billion = self.__convert_from_base(RatioUnits.PartPerBillion)
        return self.__parts_per_billion

    
    @property
    def parts_per_trillion(self) -> float:
        """
        
        """
        if self.__parts_per_trillion != None:
            return self.__parts_per_trillion
        self.__parts_per_trillion = self.__convert_from_base(RatioUnits.PartPerTrillion)
        return self.__parts_per_trillion

    
    def to_string(self, unit: RatioUnits = RatioUnits.DecimalFraction, fractional_digits: int = None) -> str:
        """
        Format the Ratio to a string.
        
        Note: the default format for Ratio is DecimalFraction.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the Ratio. Default is 'DecimalFraction'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == RatioUnits.DecimalFraction:
            return f"""{super()._truncate_fraction_digits(self.decimal_fractions, fractional_digits)} """
        
        if unit == RatioUnits.Percent:
            return f"""{super()._truncate_fraction_digits(self.percent, fractional_digits)} %"""
        
        if unit == RatioUnits.PartPerThousand:
            return f"""{super()._truncate_fraction_digits(self.parts_per_thousand, fractional_digits)} ‰"""
        
        if unit == RatioUnits.PartPerMillion:
            return f"""{super()._truncate_fraction_digits(self.parts_per_million, fractional_digits)} ppm"""
        
        if unit == RatioUnits.PartPerBillion:
            return f"""{super()._truncate_fraction_digits(self.parts_per_billion, fractional_digits)} ppb"""
        
        if unit == RatioUnits.PartPerTrillion:
            return f"""{super()._truncate_fraction_digits(self.parts_per_trillion, fractional_digits)} ppt"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: RatioUnits = RatioUnits.DecimalFraction) -> str:
        """
        Get Ratio unit abbreviation.
        Note! the default abbreviation for Ratio is DecimalFraction.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == RatioUnits.DecimalFraction:
            return """"""
        
        if unit_abbreviation == RatioUnits.Percent:
            return """%"""
        
        if unit_abbreviation == RatioUnits.PartPerThousand:
            return """‰"""
        
        if unit_abbreviation == RatioUnits.PartPerMillion:
            return """ppm"""
        
        if unit_abbreviation == RatioUnits.PartPerBillion:
            return """ppb"""
        
        if unit_abbreviation == RatioUnits.PartPerTrillion:
            return """ppt"""
        
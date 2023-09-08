from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class RatioUnits(Enum):
        """
            RatioUnits enumeration
        """
        
        DecimalFraction = 'decimal_fraction'
        """
            
        """
        
        Percent = 'percent'
        """
            
        """
        
        PartPerThousand = 'part_per_thousand'
        """
            
        """
        
        PartPerMillion = 'part_per_million'
        """
            
        """
        
        PartPerBillion = 'part_per_billion'
        """
            
        """
        
        PartPerTrillion = 'part_per_trillion'
        """
            
        """
        

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

    
    def to_string(self, unit: RatioUnits = RatioUnits.DecimalFraction) -> str:
        """
        Format the Ratio to string.
        Note! the default format for Ratio is DecimalFraction.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == RatioUnits.DecimalFraction:
            return f"""{self.decimal_fractions} """
        
        if unit == RatioUnits.Percent:
            return f"""{self.percent} %"""
        
        if unit == RatioUnits.PartPerThousand:
            return f"""{self.parts_per_thousand} ‰"""
        
        if unit == RatioUnits.PartPerMillion:
            return f"""{self.parts_per_million} ppm"""
        
        if unit == RatioUnits.PartPerBillion:
            return f"""{self.parts_per_billion} ppb"""
        
        if unit == RatioUnits.PartPerTrillion:
            return f"""{self.parts_per_trillion} ppt"""
        
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
        
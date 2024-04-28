from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class AreaDensityUnits(Enum):
        """
            AreaDensityUnits enumeration
        """
        
        KilogramPerSquareMeter = 'KilogramPerSquareMeter'
        """
            
        """
        
        GramPerSquareMeter = 'GramPerSquareMeter'
        """
            Also known as grammage for paper industry. In fiber industry used with abbreviation 'gsm'.
        """
        
        MilligramPerSquareMeter = 'MilligramPerSquareMeter'
        """
            
        """
        

class AreaDensityDto:
    """
    A DTO representation of a AreaDensity

    Attributes:
        value (float): The value of the AreaDensity.
        unit (AreaDensityUnits): The specific unit that the AreaDensity value is representing.
    """

    def __init__(self, value: float, unit: AreaDensityUnits):
        """
        Create a new DTO representation of a AreaDensity

        Parameters:
            value (float): The value of the AreaDensity.
            unit (AreaDensityUnits): The specific unit that the AreaDensity value is representing.
        """
        self.value: float = value
        """
        The value of the AreaDensity
        """
        self.unit: AreaDensityUnits = unit
        """
        The specific unit that the AreaDensity value is representing
        """

    def to_json(self):
        """
        Get a AreaDensity DTO JSON object representing the current unit.

        :return: JSON object represents AreaDensity DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "KilogramPerSquareMeter"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of AreaDensity DTO from a json representation.

        :param data: The AreaDensity DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "KilogramPerSquareMeter"}
        :return: A new instance of AreaDensityDto.
        :rtype: AreaDensityDto
        """
        return AreaDensityDto(value=data["value"], unit=AreaDensityUnits(data["unit"]))


class AreaDensity(AbstractMeasure):
    """
    The area density of a two-dimensional object is calculated as the mass per unit area. For paper this is also called grammage.

    Args:
        value (float): The value.
        from_unit (AreaDensityUnits): The AreaDensity unit to create from, The default unit is KilogramPerSquareMeter
    """
    def __init__(self, value: float, from_unit: AreaDensityUnits = AreaDensityUnits.KilogramPerSquareMeter):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__kilograms_per_square_meter = None
        
        self.__grams_per_square_meter = None
        
        self.__milligrams_per_square_meter = None
        

    def convert(self, unit: AreaDensityUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: AreaDensityUnits = AreaDensityUnits.KilogramPerSquareMeter) -> AreaDensityDto:
        """
        Get a new instance of AreaDensity DTO representing the current unit.

        :param hold_in_unit: The specific AreaDensity unit to store the AreaDensity value in the DTO representation.
        :type hold_in_unit: AreaDensityUnits
        :return: A new instance of AreaDensityDto.
        :rtype: AreaDensityDto
        """
        return AreaDensityDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: AreaDensityUnits = AreaDensityUnits.KilogramPerSquareMeter):
        """
        Get a AreaDensity DTO JSON object representing the current unit.

        :param hold_in_unit: The specific AreaDensity unit to store the AreaDensity value in the DTO representation.
        :type hold_in_unit: AreaDensityUnits
        :return: JSON object represents AreaDensity DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "KilogramPerSquareMeter"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(area_density_dto: AreaDensityDto):
        """
        Obtain a new instance of AreaDensity from a DTO unit object.

        :param area_density_dto: The AreaDensity DTO representation.
        :type area_density_dto: AreaDensityDto
        :return: A new instance of AreaDensity.
        :rtype: AreaDensity
        """
        return AreaDensity(area_density_dto.value, area_density_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of AreaDensity from a DTO unit json representation.

        :param data: The AreaDensity DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "KilogramPerSquareMeter"}
        :return: A new instance of AreaDensity.
        :rtype: AreaDensity
        """
        return AreaDensity.from_dto(AreaDensityDto.from_json(data))

    def __convert_from_base(self, from_unit: AreaDensityUnits) -> float:
        value = self._value
        
        if from_unit == AreaDensityUnits.KilogramPerSquareMeter:
            return (value)
        
        if from_unit == AreaDensityUnits.GramPerSquareMeter:
            return (value * 1000)
        
        if from_unit == AreaDensityUnits.MilligramPerSquareMeter:
            return (value * 1000000)
        
        return None


    def __convert_to_base(self, value: float, to_unit: AreaDensityUnits) -> float:
        
        if to_unit == AreaDensityUnits.KilogramPerSquareMeter:
            return (value)
        
        if to_unit == AreaDensityUnits.GramPerSquareMeter:
            return (value / 1000)
        
        if to_unit == AreaDensityUnits.MilligramPerSquareMeter:
            return (value / 1000000)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_kilograms_per_square_meter(kilograms_per_square_meter: float):
        """
        Create a new instance of AreaDensity from a value in kilograms_per_square_meter.

        

        :param meters: The AreaDensity value in kilograms_per_square_meter.
        :type kilograms_per_square_meter: float
        :return: A new instance of AreaDensity.
        :rtype: AreaDensity
        """
        return AreaDensity(kilograms_per_square_meter, AreaDensityUnits.KilogramPerSquareMeter)

    
    @staticmethod
    def from_grams_per_square_meter(grams_per_square_meter: float):
        """
        Create a new instance of AreaDensity from a value in grams_per_square_meter.

        Also known as grammage for paper industry. In fiber industry used with abbreviation 'gsm'.

        :param meters: The AreaDensity value in grams_per_square_meter.
        :type grams_per_square_meter: float
        :return: A new instance of AreaDensity.
        :rtype: AreaDensity
        """
        return AreaDensity(grams_per_square_meter, AreaDensityUnits.GramPerSquareMeter)

    
    @staticmethod
    def from_milligrams_per_square_meter(milligrams_per_square_meter: float):
        """
        Create a new instance of AreaDensity from a value in milligrams_per_square_meter.

        

        :param meters: The AreaDensity value in milligrams_per_square_meter.
        :type milligrams_per_square_meter: float
        :return: A new instance of AreaDensity.
        :rtype: AreaDensity
        """
        return AreaDensity(milligrams_per_square_meter, AreaDensityUnits.MilligramPerSquareMeter)

    
    @property
    def kilograms_per_square_meter(self) -> float:
        """
        
        """
        if self.__kilograms_per_square_meter != None:
            return self.__kilograms_per_square_meter
        self.__kilograms_per_square_meter = self.__convert_from_base(AreaDensityUnits.KilogramPerSquareMeter)
        return self.__kilograms_per_square_meter

    
    @property
    def grams_per_square_meter(self) -> float:
        """
        Also known as grammage for paper industry. In fiber industry used with abbreviation 'gsm'.
        """
        if self.__grams_per_square_meter != None:
            return self.__grams_per_square_meter
        self.__grams_per_square_meter = self.__convert_from_base(AreaDensityUnits.GramPerSquareMeter)
        return self.__grams_per_square_meter

    
    @property
    def milligrams_per_square_meter(self) -> float:
        """
        
        """
        if self.__milligrams_per_square_meter != None:
            return self.__milligrams_per_square_meter
        self.__milligrams_per_square_meter = self.__convert_from_base(AreaDensityUnits.MilligramPerSquareMeter)
        return self.__milligrams_per_square_meter

    
    def to_string(self, unit: AreaDensityUnits = AreaDensityUnits.KilogramPerSquareMeter, fractional_digits: int = None) -> str:
        """
        Format the AreaDensity to a string.
        
        Note: the default format for AreaDensity is KilogramPerSquareMeter.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the AreaDensity. Default is 'KilogramPerSquareMeter'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == AreaDensityUnits.KilogramPerSquareMeter:
            return f"""{super()._truncate_fraction_digits(self.kilograms_per_square_meter, fractional_digits)} kg/m²"""
        
        if unit == AreaDensityUnits.GramPerSquareMeter:
            return f"""{super()._truncate_fraction_digits(self.grams_per_square_meter, fractional_digits)} g/m²"""
        
        if unit == AreaDensityUnits.MilligramPerSquareMeter:
            return f"""{super()._truncate_fraction_digits(self.milligrams_per_square_meter, fractional_digits)} mg/m²"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: AreaDensityUnits = AreaDensityUnits.KilogramPerSquareMeter) -> str:
        """
        Get AreaDensity unit abbreviation.
        Note! the default abbreviation for AreaDensity is KilogramPerSquareMeter.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == AreaDensityUnits.KilogramPerSquareMeter:
            return """kg/m²"""
        
        if unit_abbreviation == AreaDensityUnits.GramPerSquareMeter:
            return """g/m²"""
        
        if unit_abbreviation == AreaDensityUnits.MilligramPerSquareMeter:
            return """mg/m²"""
        
from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class AreaUnits(Enum):
        """
            AreaUnits enumeration
        """
        
        SquareKilometer = 'SquareKilometer'
        """
            
        """
        
        SquareMeter = 'SquareMeter'
        """
            
        """
        
        SquareDecimeter = 'SquareDecimeter'
        """
            
        """
        
        SquareCentimeter = 'SquareCentimeter'
        """
            
        """
        
        SquareMillimeter = 'SquareMillimeter'
        """
            
        """
        
        SquareMicrometer = 'SquareMicrometer'
        """
            
        """
        
        SquareMile = 'SquareMile'
        """
            The statute mile was standardised between the British Commonwealth and the United States by an international agreement in 1959, when it was formally redefined with respect to SI units as exactly 1,609.344 metres.
        """
        
        SquareYard = 'SquareYard'
        """
            The yard (symbol: yd) is an English unit of length in both the British imperial and US customary systems of measurement equalling 3 feet (or 36 inches). Since 1959 the yard has been by international agreement standardized as exactly 0.9144 meter. A distance of 1,760 yards is equal to 1 mile.
        """
        
        SquareFoot = 'SquareFoot'
        """
            
        """
        
        UsSurveySquareFoot = 'UsSurveySquareFoot'
        """
            In the United States, the foot was defined as 12 inches, with the inch being defined by the Mendenhall Order of 1893 as 39.37 inches = 1 m. This makes a U.S. survey foot exactly 1200/3937 meters.
        """
        
        SquareInch = 'SquareInch'
        """
            
        """
        
        Acre = 'Acre'
        """
            Based upon the international yard and pound agreement of 1959, an acre may be declared as exactly 4,046.8564224 square metres.
        """
        
        Hectare = 'Hectare'
        """
            
        """
        
        SquareNauticalMile = 'SquareNauticalMile'
        """
            
        """
        

class AreaDto:
    """
    A DTO representation of a Area

    Attributes:
        value (float): The value of the Area.
        unit (AreaUnits): The specific unit that the Area value is representing.
    """

    def __init__(self, value: float, unit: AreaUnits):
        """
        Create a new DTO representation of a Area

        Parameters:
            value (float): The value of the Area.
            unit (AreaUnits): The specific unit that the Area value is representing.
        """
        self.value: float = value
        """
        The value of the Area
        """
        self.unit: AreaUnits = unit
        """
        The specific unit that the Area value is representing
        """

    def to_json(self):
        """
        Get a Area DTO JSON object representing the current unit.

        :return: JSON object represents Area DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "SquareMeter"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of Area DTO from a json representation.

        :param data: The Area DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "SquareMeter"}
        :return: A new instance of AreaDto.
        :rtype: AreaDto
        """
        return AreaDto(value=data["value"], unit=AreaUnits(data["unit"]))


class Area(AbstractMeasure):
    """
    Area is a quantity that expresses the extent of a two-dimensional surface or shape, or planar lamina, in the plane. Area can be understood as the amount of material with a given thickness that would be necessary to fashion a model of the shape, or the amount of paint necessary to cover the surface with a single coat.[1] It is the two-dimensional analog of the length of a curve (a one-dimensional concept) or the volume of a solid (a three-dimensional concept).

    Args:
        value (float): The value.
        from_unit (AreaUnits): The Area unit to create from, The default unit is SquareMeter
    """
    def __init__(self, value: float, from_unit: AreaUnits = AreaUnits.SquareMeter):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__square_kilometers = None
        
        self.__square_meters = None
        
        self.__square_decimeters = None
        
        self.__square_centimeters = None
        
        self.__square_millimeters = None
        
        self.__square_micrometers = None
        
        self.__square_miles = None
        
        self.__square_yards = None
        
        self.__square_feet = None
        
        self.__us_survey_square_feet = None
        
        self.__square_inches = None
        
        self.__acres = None
        
        self.__hectares = None
        
        self.__square_nautical_miles = None
        

    def convert(self, unit: AreaUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: AreaUnits = AreaUnits.SquareMeter) -> AreaDto:
        """
        Get a new instance of Area DTO representing the current unit.

        :param hold_in_unit: The specific Area unit to store the Area value in the DTO representation.
        :type hold_in_unit: AreaUnits
        :return: A new instance of AreaDto.
        :rtype: AreaDto
        """
        return AreaDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: AreaUnits = AreaUnits.SquareMeter):
        """
        Get a Area DTO JSON object representing the current unit.

        :param hold_in_unit: The specific Area unit to store the Area value in the DTO representation.
        :type hold_in_unit: AreaUnits
        :return: JSON object represents Area DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "SquareMeter"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(area_dto: AreaDto):
        """
        Obtain a new instance of Area from a DTO unit object.

        :param area_dto: The Area DTO representation.
        :type area_dto: AreaDto
        :return: A new instance of Area.
        :rtype: Area
        """
        return Area(area_dto.value, area_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of Area from a DTO unit json representation.

        :param data: The Area DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "SquareMeter"}
        :return: A new instance of Area.
        :rtype: Area
        """
        return Area.from_dto(AreaDto.from_json(data))

    def __convert_from_base(self, from_unit: AreaUnits) -> float:
        value = self._value
        
        if from_unit == AreaUnits.SquareKilometer:
            return (value / 1e6)
        
        if from_unit == AreaUnits.SquareMeter:
            return (value)
        
        if from_unit == AreaUnits.SquareDecimeter:
            return (value / 1e-2)
        
        if from_unit == AreaUnits.SquareCentimeter:
            return (value / 1e-4)
        
        if from_unit == AreaUnits.SquareMillimeter:
            return (value / 1e-6)
        
        if from_unit == AreaUnits.SquareMicrometer:
            return (value / 1e-12)
        
        if from_unit == AreaUnits.SquareMile:
            return (value / 1609.344 / 1609.344)
        
        if from_unit == AreaUnits.SquareYard:
            return (value / 0.9144 / 0.9144)
        
        if from_unit == AreaUnits.SquareFoot:
            return (value / 9.290304e-2)
        
        if from_unit == AreaUnits.UsSurveySquareFoot:
            return (value / (1200.0 / 3937.0) / (1200.0 / 3937.0))
        
        if from_unit == AreaUnits.SquareInch:
            return (value / 0.00064516)
        
        if from_unit == AreaUnits.Acre:
            return (value / 4046.8564224)
        
        if from_unit == AreaUnits.Hectare:
            return (value / 1e4)
        
        if from_unit == AreaUnits.SquareNauticalMile:
            return (value / 3429904)
        
        return None


    def __convert_to_base(self, value: float, to_unit: AreaUnits) -> float:
        
        if to_unit == AreaUnits.SquareKilometer:
            return (value * 1e6)
        
        if to_unit == AreaUnits.SquareMeter:
            return (value)
        
        if to_unit == AreaUnits.SquareDecimeter:
            return (value * 1e-2)
        
        if to_unit == AreaUnits.SquareCentimeter:
            return (value * 1e-4)
        
        if to_unit == AreaUnits.SquareMillimeter:
            return (value * 1e-6)
        
        if to_unit == AreaUnits.SquareMicrometer:
            return (value * 1e-12)
        
        if to_unit == AreaUnits.SquareMile:
            return (value * 1609.344 * 1609.344)
        
        if to_unit == AreaUnits.SquareYard:
            return (value * 0.9144 * 0.9144)
        
        if to_unit == AreaUnits.SquareFoot:
            return (value * 9.290304e-2)
        
        if to_unit == AreaUnits.UsSurveySquareFoot:
            return (value * (1200.0 / 3937.0) * (1200.0 / 3937.0))
        
        if to_unit == AreaUnits.SquareInch:
            return (value * 0.00064516)
        
        if to_unit == AreaUnits.Acre:
            return (value * 4046.8564224)
        
        if to_unit == AreaUnits.Hectare:
            return (value * 1e4)
        
        if to_unit == AreaUnits.SquareNauticalMile:
            return (value * 3429904)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_square_kilometers(square_kilometers: float):
        """
        Create a new instance of Area from a value in square_kilometers.

        

        :param meters: The Area value in square_kilometers.
        :type square_kilometers: float
        :return: A new instance of Area.
        :rtype: Area
        """
        return Area(square_kilometers, AreaUnits.SquareKilometer)

    
    @staticmethod
    def from_square_meters(square_meters: float):
        """
        Create a new instance of Area from a value in square_meters.

        

        :param meters: The Area value in square_meters.
        :type square_meters: float
        :return: A new instance of Area.
        :rtype: Area
        """
        return Area(square_meters, AreaUnits.SquareMeter)

    
    @staticmethod
    def from_square_decimeters(square_decimeters: float):
        """
        Create a new instance of Area from a value in square_decimeters.

        

        :param meters: The Area value in square_decimeters.
        :type square_decimeters: float
        :return: A new instance of Area.
        :rtype: Area
        """
        return Area(square_decimeters, AreaUnits.SquareDecimeter)

    
    @staticmethod
    def from_square_centimeters(square_centimeters: float):
        """
        Create a new instance of Area from a value in square_centimeters.

        

        :param meters: The Area value in square_centimeters.
        :type square_centimeters: float
        :return: A new instance of Area.
        :rtype: Area
        """
        return Area(square_centimeters, AreaUnits.SquareCentimeter)

    
    @staticmethod
    def from_square_millimeters(square_millimeters: float):
        """
        Create a new instance of Area from a value in square_millimeters.

        

        :param meters: The Area value in square_millimeters.
        :type square_millimeters: float
        :return: A new instance of Area.
        :rtype: Area
        """
        return Area(square_millimeters, AreaUnits.SquareMillimeter)

    
    @staticmethod
    def from_square_micrometers(square_micrometers: float):
        """
        Create a new instance of Area from a value in square_micrometers.

        

        :param meters: The Area value in square_micrometers.
        :type square_micrometers: float
        :return: A new instance of Area.
        :rtype: Area
        """
        return Area(square_micrometers, AreaUnits.SquareMicrometer)

    
    @staticmethod
    def from_square_miles(square_miles: float):
        """
        Create a new instance of Area from a value in square_miles.

        The statute mile was standardised between the British Commonwealth and the United States by an international agreement in 1959, when it was formally redefined with respect to SI units as exactly 1,609.344 metres.

        :param meters: The Area value in square_miles.
        :type square_miles: float
        :return: A new instance of Area.
        :rtype: Area
        """
        return Area(square_miles, AreaUnits.SquareMile)

    
    @staticmethod
    def from_square_yards(square_yards: float):
        """
        Create a new instance of Area from a value in square_yards.

        The yard (symbol: yd) is an English unit of length in both the British imperial and US customary systems of measurement equalling 3 feet (or 36 inches). Since 1959 the yard has been by international agreement standardized as exactly 0.9144 meter. A distance of 1,760 yards is equal to 1 mile.

        :param meters: The Area value in square_yards.
        :type square_yards: float
        :return: A new instance of Area.
        :rtype: Area
        """
        return Area(square_yards, AreaUnits.SquareYard)

    
    @staticmethod
    def from_square_feet(square_feet: float):
        """
        Create a new instance of Area from a value in square_feet.

        

        :param meters: The Area value in square_feet.
        :type square_feet: float
        :return: A new instance of Area.
        :rtype: Area
        """
        return Area(square_feet, AreaUnits.SquareFoot)

    
    @staticmethod
    def from_us_survey_square_feet(us_survey_square_feet: float):
        """
        Create a new instance of Area from a value in us_survey_square_feet.

        In the United States, the foot was defined as 12 inches, with the inch being defined by the Mendenhall Order of 1893 as 39.37 inches = 1 m. This makes a U.S. survey foot exactly 1200/3937 meters.

        :param meters: The Area value in us_survey_square_feet.
        :type us_survey_square_feet: float
        :return: A new instance of Area.
        :rtype: Area
        """
        return Area(us_survey_square_feet, AreaUnits.UsSurveySquareFoot)

    
    @staticmethod
    def from_square_inches(square_inches: float):
        """
        Create a new instance of Area from a value in square_inches.

        

        :param meters: The Area value in square_inches.
        :type square_inches: float
        :return: A new instance of Area.
        :rtype: Area
        """
        return Area(square_inches, AreaUnits.SquareInch)

    
    @staticmethod
    def from_acres(acres: float):
        """
        Create a new instance of Area from a value in acres.

        Based upon the international yard and pound agreement of 1959, an acre may be declared as exactly 4,046.8564224 square metres.

        :param meters: The Area value in acres.
        :type acres: float
        :return: A new instance of Area.
        :rtype: Area
        """
        return Area(acres, AreaUnits.Acre)

    
    @staticmethod
    def from_hectares(hectares: float):
        """
        Create a new instance of Area from a value in hectares.

        

        :param meters: The Area value in hectares.
        :type hectares: float
        :return: A new instance of Area.
        :rtype: Area
        """
        return Area(hectares, AreaUnits.Hectare)

    
    @staticmethod
    def from_square_nautical_miles(square_nautical_miles: float):
        """
        Create a new instance of Area from a value in square_nautical_miles.

        

        :param meters: The Area value in square_nautical_miles.
        :type square_nautical_miles: float
        :return: A new instance of Area.
        :rtype: Area
        """
        return Area(square_nautical_miles, AreaUnits.SquareNauticalMile)

    
    @property
    def square_kilometers(self) -> float:
        """
        
        """
        if self.__square_kilometers != None:
            return self.__square_kilometers
        self.__square_kilometers = self.__convert_from_base(AreaUnits.SquareKilometer)
        return self.__square_kilometers

    
    @property
    def square_meters(self) -> float:
        """
        
        """
        if self.__square_meters != None:
            return self.__square_meters
        self.__square_meters = self.__convert_from_base(AreaUnits.SquareMeter)
        return self.__square_meters

    
    @property
    def square_decimeters(self) -> float:
        """
        
        """
        if self.__square_decimeters != None:
            return self.__square_decimeters
        self.__square_decimeters = self.__convert_from_base(AreaUnits.SquareDecimeter)
        return self.__square_decimeters

    
    @property
    def square_centimeters(self) -> float:
        """
        
        """
        if self.__square_centimeters != None:
            return self.__square_centimeters
        self.__square_centimeters = self.__convert_from_base(AreaUnits.SquareCentimeter)
        return self.__square_centimeters

    
    @property
    def square_millimeters(self) -> float:
        """
        
        """
        if self.__square_millimeters != None:
            return self.__square_millimeters
        self.__square_millimeters = self.__convert_from_base(AreaUnits.SquareMillimeter)
        return self.__square_millimeters

    
    @property
    def square_micrometers(self) -> float:
        """
        
        """
        if self.__square_micrometers != None:
            return self.__square_micrometers
        self.__square_micrometers = self.__convert_from_base(AreaUnits.SquareMicrometer)
        return self.__square_micrometers

    
    @property
    def square_miles(self) -> float:
        """
        The statute mile was standardised between the British Commonwealth and the United States by an international agreement in 1959, when it was formally redefined with respect to SI units as exactly 1,609.344 metres.
        """
        if self.__square_miles != None:
            return self.__square_miles
        self.__square_miles = self.__convert_from_base(AreaUnits.SquareMile)
        return self.__square_miles

    
    @property
    def square_yards(self) -> float:
        """
        The yard (symbol: yd) is an English unit of length in both the British imperial and US customary systems of measurement equalling 3 feet (or 36 inches). Since 1959 the yard has been by international agreement standardized as exactly 0.9144 meter. A distance of 1,760 yards is equal to 1 mile.
        """
        if self.__square_yards != None:
            return self.__square_yards
        self.__square_yards = self.__convert_from_base(AreaUnits.SquareYard)
        return self.__square_yards

    
    @property
    def square_feet(self) -> float:
        """
        
        """
        if self.__square_feet != None:
            return self.__square_feet
        self.__square_feet = self.__convert_from_base(AreaUnits.SquareFoot)
        return self.__square_feet

    
    @property
    def us_survey_square_feet(self) -> float:
        """
        In the United States, the foot was defined as 12 inches, with the inch being defined by the Mendenhall Order of 1893 as 39.37 inches = 1 m. This makes a U.S. survey foot exactly 1200/3937 meters.
        """
        if self.__us_survey_square_feet != None:
            return self.__us_survey_square_feet
        self.__us_survey_square_feet = self.__convert_from_base(AreaUnits.UsSurveySquareFoot)
        return self.__us_survey_square_feet

    
    @property
    def square_inches(self) -> float:
        """
        
        """
        if self.__square_inches != None:
            return self.__square_inches
        self.__square_inches = self.__convert_from_base(AreaUnits.SquareInch)
        return self.__square_inches

    
    @property
    def acres(self) -> float:
        """
        Based upon the international yard and pound agreement of 1959, an acre may be declared as exactly 4,046.8564224 square metres.
        """
        if self.__acres != None:
            return self.__acres
        self.__acres = self.__convert_from_base(AreaUnits.Acre)
        return self.__acres

    
    @property
    def hectares(self) -> float:
        """
        
        """
        if self.__hectares != None:
            return self.__hectares
        self.__hectares = self.__convert_from_base(AreaUnits.Hectare)
        return self.__hectares

    
    @property
    def square_nautical_miles(self) -> float:
        """
        
        """
        if self.__square_nautical_miles != None:
            return self.__square_nautical_miles
        self.__square_nautical_miles = self.__convert_from_base(AreaUnits.SquareNauticalMile)
        return self.__square_nautical_miles

    
    def to_string(self, unit: AreaUnits = AreaUnits.SquareMeter, fractional_digits: int = None) -> str:
        """
        Format the Area to a string.
        
        Note: the default format for Area is SquareMeter.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the Area. Default is 'SquareMeter'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == AreaUnits.SquareKilometer:
            return f"""{super()._truncate_fraction_digits(self.square_kilometers, fractional_digits)} km²"""
        
        if unit == AreaUnits.SquareMeter:
            return f"""{super()._truncate_fraction_digits(self.square_meters, fractional_digits)} m²"""
        
        if unit == AreaUnits.SquareDecimeter:
            return f"""{super()._truncate_fraction_digits(self.square_decimeters, fractional_digits)} dm²"""
        
        if unit == AreaUnits.SquareCentimeter:
            return f"""{super()._truncate_fraction_digits(self.square_centimeters, fractional_digits)} cm²"""
        
        if unit == AreaUnits.SquareMillimeter:
            return f"""{super()._truncate_fraction_digits(self.square_millimeters, fractional_digits)} mm²"""
        
        if unit == AreaUnits.SquareMicrometer:
            return f"""{super()._truncate_fraction_digits(self.square_micrometers, fractional_digits)} µm²"""
        
        if unit == AreaUnits.SquareMile:
            return f"""{super()._truncate_fraction_digits(self.square_miles, fractional_digits)} mi²"""
        
        if unit == AreaUnits.SquareYard:
            return f"""{super()._truncate_fraction_digits(self.square_yards, fractional_digits)} yd²"""
        
        if unit == AreaUnits.SquareFoot:
            return f"""{super()._truncate_fraction_digits(self.square_feet, fractional_digits)} ft²"""
        
        if unit == AreaUnits.UsSurveySquareFoot:
            return f"""{super()._truncate_fraction_digits(self.us_survey_square_feet, fractional_digits)} ft² (US)"""
        
        if unit == AreaUnits.SquareInch:
            return f"""{super()._truncate_fraction_digits(self.square_inches, fractional_digits)} in²"""
        
        if unit == AreaUnits.Acre:
            return f"""{super()._truncate_fraction_digits(self.acres, fractional_digits)} ac"""
        
        if unit == AreaUnits.Hectare:
            return f"""{super()._truncate_fraction_digits(self.hectares, fractional_digits)} ha"""
        
        if unit == AreaUnits.SquareNauticalMile:
            return f"""{super()._truncate_fraction_digits(self.square_nautical_miles, fractional_digits)} nmi²"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: AreaUnits = AreaUnits.SquareMeter) -> str:
        """
        Get Area unit abbreviation.
        Note! the default abbreviation for Area is SquareMeter.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == AreaUnits.SquareKilometer:
            return """km²"""
        
        if unit_abbreviation == AreaUnits.SquareMeter:
            return """m²"""
        
        if unit_abbreviation == AreaUnits.SquareDecimeter:
            return """dm²"""
        
        if unit_abbreviation == AreaUnits.SquareCentimeter:
            return """cm²"""
        
        if unit_abbreviation == AreaUnits.SquareMillimeter:
            return """mm²"""
        
        if unit_abbreviation == AreaUnits.SquareMicrometer:
            return """µm²"""
        
        if unit_abbreviation == AreaUnits.SquareMile:
            return """mi²"""
        
        if unit_abbreviation == AreaUnits.SquareYard:
            return """yd²"""
        
        if unit_abbreviation == AreaUnits.SquareFoot:
            return """ft²"""
        
        if unit_abbreviation == AreaUnits.UsSurveySquareFoot:
            return """ft² (US)"""
        
        if unit_abbreviation == AreaUnits.SquareInch:
            return """in²"""
        
        if unit_abbreviation == AreaUnits.Acre:
            return """ac"""
        
        if unit_abbreviation == AreaUnits.Hectare:
            return """ha"""
        
        if unit_abbreviation == AreaUnits.SquareNauticalMile:
            return """nmi²"""
        
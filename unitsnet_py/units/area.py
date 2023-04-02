from enum import Enum
import math
import string


class AreaUnits(Enum):
        """
            AreaUnits enumeration
        """
        
        SquareKilometer = 'square_kilometer'
        """
            
        """
        
        SquareMeter = 'square_meter'
        """
            
        """
        
        SquareDecimeter = 'square_decimeter'
        """
            
        """
        
        SquareCentimeter = 'square_centimeter'
        """
            
        """
        
        SquareMillimeter = 'square_millimeter'
        """
            
        """
        
        SquareMicrometer = 'square_micrometer'
        """
            
        """
        
        SquareMile = 'square_mile'
        """
            The statute mile was standardised between the British Commonwealth and the United States by an international agreement in 1959, when it was formally redefined with respect to SI units as exactly 1,609.344 metres.
        """
        
        SquareYard = 'square_yard'
        """
            The yard (symbol: yd) is an English unit of length in both the British imperial and US customary systems of measurement equalling 3 feet (or 36 inches). Since 1959 the yard has been by international agreement standardized as exactly 0.9144 meter. A distance of 1,760 yards is equal to 1 mile.
        """
        
        SquareFoot = 'square_foot'
        """
            
        """
        
        UsSurveySquareFoot = 'us_survey_square_foot'
        """
            In the United States, the foot was defined as 12 inches, with the inch being defined by the Mendenhall Order of 1893 as 39.37 inches = 1 m. This makes a U.S. survey foot exactly 1200/3937 meters.
        """
        
        SquareInch = 'square_inch'
        """
            
        """
        
        Acre = 'acre'
        """
            Based upon the international yard and pound agreement of 1959, an acre may be declared as exactly 4,046.8564224 square metres.
        """
        
        Hectare = 'hectare'
        """
            
        """
        
        SquareNauticalMile = 'square_nautical_mile'
        """
            
        """
        

class Area:
    """
    Area is a quantity that expresses the extent of a two-dimensional surface or shape, or planar lamina, in the plane. Area can be understood as the amount of material with a given thickness that would be necessary to fashion a model of the shape, or the amount of paint necessary to cover the surface with a single coat.[1] It is the two-dimensional analog of the length of a curve (a one-dimensional concept) or the volume of a solid (a three-dimensional concept).

    Args:
        value (float): The value.
        from_unit (AreaUnits): The Area unit to create from, The default unit is SquareMeter
    """
    def __init__(self, value: float, from_unit: AreaUnits = AreaUnits.SquareMeter):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
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
        

    def __convert_from_base(self, from_unit: AreaUnits) -> float:
        value = self.__value
        
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
        return self.__value

    
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

    
    def to_string(self, unit: AreaUnits = AreaUnits.SquareMeter) -> string:
        """
        Format the Area to string.
        Note! the default format for Area is SquareMeter.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == AreaUnits.SquareKilometer:
            return f"""{self.square_kilometers} km²"""
        
        if unit == AreaUnits.SquareMeter:
            return f"""{self.square_meters} m²"""
        
        if unit == AreaUnits.SquareDecimeter:
            return f"""{self.square_decimeters} dm²"""
        
        if unit == AreaUnits.SquareCentimeter:
            return f"""{self.square_centimeters} cm²"""
        
        if unit == AreaUnits.SquareMillimeter:
            return f"""{self.square_millimeters} mm²"""
        
        if unit == AreaUnits.SquareMicrometer:
            return f"""{self.square_micrometers} µm²"""
        
        if unit == AreaUnits.SquareMile:
            return f"""{self.square_miles} mi²"""
        
        if unit == AreaUnits.SquareYard:
            return f"""{self.square_yards} yd²"""
        
        if unit == AreaUnits.SquareFoot:
            return f"""{self.square_feet} ft²"""
        
        if unit == AreaUnits.UsSurveySquareFoot:
            return f"""{self.us_survey_square_feet} ft² (US)"""
        
        if unit == AreaUnits.SquareInch:
            return f"""{self.square_inches} in²"""
        
        if unit == AreaUnits.Acre:
            return f"""{self.acres} ac"""
        
        if unit == AreaUnits.Hectare:
            return f"""{self.hectares} ha"""
        
        if unit == AreaUnits.SquareNauticalMile:
            return f"""{self.square_nautical_miles} nmi²"""
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: AreaUnits = AreaUnits.SquareMeter) -> string:
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
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, Area):
            raise TypeError("unsupported operand type(s) for +: 'Area' and '{}'".format(type(other).__name__))
        return Area(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, Area):
            raise TypeError("unsupported operand type(s) for *: 'Area' and '{}'".format(type(other).__name__))
        return Area(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, Area):
            raise TypeError("unsupported operand type(s) for -: 'Area' and '{}'".format(type(other).__name__))
        return Area(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, Area):
            raise TypeError("unsupported operand type(s) for /: 'Area' and '{}'".format(type(other).__name__))
        return Area(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, Area):
            raise TypeError("unsupported operand type(s) for %: 'Area' and '{}'".format(type(other).__name__))
        return Area(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, Area):
            raise TypeError("unsupported operand type(s) for **: 'Area' and '{}'".format(type(other).__name__))
        return Area(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, Area):
            raise TypeError("unsupported operand type(s) for ==: 'Area' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, Area):
            raise TypeError("unsupported operand type(s) for <: 'Area' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, Area):
            raise TypeError("unsupported operand type(s) for >: 'Area' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, Area):
            raise TypeError("unsupported operand type(s) for <=: 'Area' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, Area):
            raise TypeError("unsupported operand type(s) for >=: 'Area' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value
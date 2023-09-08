from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class ReciprocalAreaUnits(Enum):
        """
            ReciprocalAreaUnits enumeration
        """
        
        InverseSquareMeter = 'inverse_square_meter'
        """
            
        """
        
        InverseSquareKilometer = 'inverse_square_kilometer'
        """
            
        """
        
        InverseSquareDecimeter = 'inverse_square_decimeter'
        """
            
        """
        
        InverseSquareCentimeter = 'inverse_square_centimeter'
        """
            
        """
        
        InverseSquareMillimeter = 'inverse_square_millimeter'
        """
            
        """
        
        InverseSquareMicrometer = 'inverse_square_micrometer'
        """
            
        """
        
        InverseSquareMile = 'inverse_square_mile'
        """
            
        """
        
        InverseSquareYard = 'inverse_square_yard'
        """
            
        """
        
        InverseSquareFoot = 'inverse_square_foot'
        """
            
        """
        
        InverseUsSurveySquareFoot = 'inverse_us_survey_square_foot'
        """
            
        """
        
        InverseSquareInch = 'inverse_square_inch'
        """
            
        """
        

class ReciprocalArea(AbstractMeasure):
    """
    Reciprocal area (Inverse-square) quantity is used to specify a physical quantity inversely proportional to the square of the distance.

    Args:
        value (float): The value.
        from_unit (ReciprocalAreaUnits): The ReciprocalArea unit to create from, The default unit is InverseSquareMeter
    """
    def __init__(self, value: float, from_unit: ReciprocalAreaUnits = ReciprocalAreaUnits.InverseSquareMeter):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__inverse_square_meters = None
        
        self.__inverse_square_kilometers = None
        
        self.__inverse_square_decimeters = None
        
        self.__inverse_square_centimeters = None
        
        self.__inverse_square_millimeters = None
        
        self.__inverse_square_micrometers = None
        
        self.__inverse_square_miles = None
        
        self.__inverse_square_yards = None
        
        self.__inverse_square_feet = None
        
        self.__inverse_us_survey_square_feet = None
        
        self.__inverse_square_inches = None
        

    def convert(self, unit: ReciprocalAreaUnits) -> float:
        return self.__convert_from_base(unit)

    def __convert_from_base(self, from_unit: ReciprocalAreaUnits) -> float:
        value = self._value
        
        if from_unit == ReciprocalAreaUnits.InverseSquareMeter:
            return (value)
        
        if from_unit == ReciprocalAreaUnits.InverseSquareKilometer:
            return (value * 1e6)
        
        if from_unit == ReciprocalAreaUnits.InverseSquareDecimeter:
            return (value * 1e-2)
        
        if from_unit == ReciprocalAreaUnits.InverseSquareCentimeter:
            return (value * 1e-4)
        
        if from_unit == ReciprocalAreaUnits.InverseSquareMillimeter:
            return (value * 1e-6)
        
        if from_unit == ReciprocalAreaUnits.InverseSquareMicrometer:
            return (value * 1e-12)
        
        if from_unit == ReciprocalAreaUnits.InverseSquareMile:
            return (value * 2.59e6)
        
        if from_unit == ReciprocalAreaUnits.InverseSquareYard:
            return (value * 0.836127)
        
        if from_unit == ReciprocalAreaUnits.InverseSquareFoot:
            return (value * 0.092903)
        
        if from_unit == ReciprocalAreaUnits.InverseUsSurveySquareFoot:
            return (value * 0.09290341161)
        
        if from_unit == ReciprocalAreaUnits.InverseSquareInch:
            return (value * 0.00064516)
        
        return None


    def __convert_to_base(self, value: float, to_unit: ReciprocalAreaUnits) -> float:
        
        if to_unit == ReciprocalAreaUnits.InverseSquareMeter:
            return (value)
        
        if to_unit == ReciprocalAreaUnits.InverseSquareKilometer:
            return (value / 1e6)
        
        if to_unit == ReciprocalAreaUnits.InverseSquareDecimeter:
            return (value / 1e-2)
        
        if to_unit == ReciprocalAreaUnits.InverseSquareCentimeter:
            return (value / 1e-4)
        
        if to_unit == ReciprocalAreaUnits.InverseSquareMillimeter:
            return (value / 1e-6)
        
        if to_unit == ReciprocalAreaUnits.InverseSquareMicrometer:
            return (value / 1e-12)
        
        if to_unit == ReciprocalAreaUnits.InverseSquareMile:
            return (value / 2.59e6)
        
        if to_unit == ReciprocalAreaUnits.InverseSquareYard:
            return (value / 0.836127)
        
        if to_unit == ReciprocalAreaUnits.InverseSquareFoot:
            return (value / 0.092903)
        
        if to_unit == ReciprocalAreaUnits.InverseUsSurveySquareFoot:
            return (value / 0.09290341161)
        
        if to_unit == ReciprocalAreaUnits.InverseSquareInch:
            return (value / 0.00064516)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_inverse_square_meters(inverse_square_meters: float):
        """
        Create a new instance of ReciprocalArea from a value in inverse_square_meters.

        

        :param meters: The ReciprocalArea value in inverse_square_meters.
        :type inverse_square_meters: float
        :return: A new instance of ReciprocalArea.
        :rtype: ReciprocalArea
        """
        return ReciprocalArea(inverse_square_meters, ReciprocalAreaUnits.InverseSquareMeter)

    
    @staticmethod
    def from_inverse_square_kilometers(inverse_square_kilometers: float):
        """
        Create a new instance of ReciprocalArea from a value in inverse_square_kilometers.

        

        :param meters: The ReciprocalArea value in inverse_square_kilometers.
        :type inverse_square_kilometers: float
        :return: A new instance of ReciprocalArea.
        :rtype: ReciprocalArea
        """
        return ReciprocalArea(inverse_square_kilometers, ReciprocalAreaUnits.InverseSquareKilometer)

    
    @staticmethod
    def from_inverse_square_decimeters(inverse_square_decimeters: float):
        """
        Create a new instance of ReciprocalArea from a value in inverse_square_decimeters.

        

        :param meters: The ReciprocalArea value in inverse_square_decimeters.
        :type inverse_square_decimeters: float
        :return: A new instance of ReciprocalArea.
        :rtype: ReciprocalArea
        """
        return ReciprocalArea(inverse_square_decimeters, ReciprocalAreaUnits.InverseSquareDecimeter)

    
    @staticmethod
    def from_inverse_square_centimeters(inverse_square_centimeters: float):
        """
        Create a new instance of ReciprocalArea from a value in inverse_square_centimeters.

        

        :param meters: The ReciprocalArea value in inverse_square_centimeters.
        :type inverse_square_centimeters: float
        :return: A new instance of ReciprocalArea.
        :rtype: ReciprocalArea
        """
        return ReciprocalArea(inverse_square_centimeters, ReciprocalAreaUnits.InverseSquareCentimeter)

    
    @staticmethod
    def from_inverse_square_millimeters(inverse_square_millimeters: float):
        """
        Create a new instance of ReciprocalArea from a value in inverse_square_millimeters.

        

        :param meters: The ReciprocalArea value in inverse_square_millimeters.
        :type inverse_square_millimeters: float
        :return: A new instance of ReciprocalArea.
        :rtype: ReciprocalArea
        """
        return ReciprocalArea(inverse_square_millimeters, ReciprocalAreaUnits.InverseSquareMillimeter)

    
    @staticmethod
    def from_inverse_square_micrometers(inverse_square_micrometers: float):
        """
        Create a new instance of ReciprocalArea from a value in inverse_square_micrometers.

        

        :param meters: The ReciprocalArea value in inverse_square_micrometers.
        :type inverse_square_micrometers: float
        :return: A new instance of ReciprocalArea.
        :rtype: ReciprocalArea
        """
        return ReciprocalArea(inverse_square_micrometers, ReciprocalAreaUnits.InverseSquareMicrometer)

    
    @staticmethod
    def from_inverse_square_miles(inverse_square_miles: float):
        """
        Create a new instance of ReciprocalArea from a value in inverse_square_miles.

        

        :param meters: The ReciprocalArea value in inverse_square_miles.
        :type inverse_square_miles: float
        :return: A new instance of ReciprocalArea.
        :rtype: ReciprocalArea
        """
        return ReciprocalArea(inverse_square_miles, ReciprocalAreaUnits.InverseSquareMile)

    
    @staticmethod
    def from_inverse_square_yards(inverse_square_yards: float):
        """
        Create a new instance of ReciprocalArea from a value in inverse_square_yards.

        

        :param meters: The ReciprocalArea value in inverse_square_yards.
        :type inverse_square_yards: float
        :return: A new instance of ReciprocalArea.
        :rtype: ReciprocalArea
        """
        return ReciprocalArea(inverse_square_yards, ReciprocalAreaUnits.InverseSquareYard)

    
    @staticmethod
    def from_inverse_square_feet(inverse_square_feet: float):
        """
        Create a new instance of ReciprocalArea from a value in inverse_square_feet.

        

        :param meters: The ReciprocalArea value in inverse_square_feet.
        :type inverse_square_feet: float
        :return: A new instance of ReciprocalArea.
        :rtype: ReciprocalArea
        """
        return ReciprocalArea(inverse_square_feet, ReciprocalAreaUnits.InverseSquareFoot)

    
    @staticmethod
    def from_inverse_us_survey_square_feet(inverse_us_survey_square_feet: float):
        """
        Create a new instance of ReciprocalArea from a value in inverse_us_survey_square_feet.

        

        :param meters: The ReciprocalArea value in inverse_us_survey_square_feet.
        :type inverse_us_survey_square_feet: float
        :return: A new instance of ReciprocalArea.
        :rtype: ReciprocalArea
        """
        return ReciprocalArea(inverse_us_survey_square_feet, ReciprocalAreaUnits.InverseUsSurveySquareFoot)

    
    @staticmethod
    def from_inverse_square_inches(inverse_square_inches: float):
        """
        Create a new instance of ReciprocalArea from a value in inverse_square_inches.

        

        :param meters: The ReciprocalArea value in inverse_square_inches.
        :type inverse_square_inches: float
        :return: A new instance of ReciprocalArea.
        :rtype: ReciprocalArea
        """
        return ReciprocalArea(inverse_square_inches, ReciprocalAreaUnits.InverseSquareInch)

    
    @property
    def inverse_square_meters(self) -> float:
        """
        
        """
        if self.__inverse_square_meters != None:
            return self.__inverse_square_meters
        self.__inverse_square_meters = self.__convert_from_base(ReciprocalAreaUnits.InverseSquareMeter)
        return self.__inverse_square_meters

    
    @property
    def inverse_square_kilometers(self) -> float:
        """
        
        """
        if self.__inverse_square_kilometers != None:
            return self.__inverse_square_kilometers
        self.__inverse_square_kilometers = self.__convert_from_base(ReciprocalAreaUnits.InverseSquareKilometer)
        return self.__inverse_square_kilometers

    
    @property
    def inverse_square_decimeters(self) -> float:
        """
        
        """
        if self.__inverse_square_decimeters != None:
            return self.__inverse_square_decimeters
        self.__inverse_square_decimeters = self.__convert_from_base(ReciprocalAreaUnits.InverseSquareDecimeter)
        return self.__inverse_square_decimeters

    
    @property
    def inverse_square_centimeters(self) -> float:
        """
        
        """
        if self.__inverse_square_centimeters != None:
            return self.__inverse_square_centimeters
        self.__inverse_square_centimeters = self.__convert_from_base(ReciprocalAreaUnits.InverseSquareCentimeter)
        return self.__inverse_square_centimeters

    
    @property
    def inverse_square_millimeters(self) -> float:
        """
        
        """
        if self.__inverse_square_millimeters != None:
            return self.__inverse_square_millimeters
        self.__inverse_square_millimeters = self.__convert_from_base(ReciprocalAreaUnits.InverseSquareMillimeter)
        return self.__inverse_square_millimeters

    
    @property
    def inverse_square_micrometers(self) -> float:
        """
        
        """
        if self.__inverse_square_micrometers != None:
            return self.__inverse_square_micrometers
        self.__inverse_square_micrometers = self.__convert_from_base(ReciprocalAreaUnits.InverseSquareMicrometer)
        return self.__inverse_square_micrometers

    
    @property
    def inverse_square_miles(self) -> float:
        """
        
        """
        if self.__inverse_square_miles != None:
            return self.__inverse_square_miles
        self.__inverse_square_miles = self.__convert_from_base(ReciprocalAreaUnits.InverseSquareMile)
        return self.__inverse_square_miles

    
    @property
    def inverse_square_yards(self) -> float:
        """
        
        """
        if self.__inverse_square_yards != None:
            return self.__inverse_square_yards
        self.__inverse_square_yards = self.__convert_from_base(ReciprocalAreaUnits.InverseSquareYard)
        return self.__inverse_square_yards

    
    @property
    def inverse_square_feet(self) -> float:
        """
        
        """
        if self.__inverse_square_feet != None:
            return self.__inverse_square_feet
        self.__inverse_square_feet = self.__convert_from_base(ReciprocalAreaUnits.InverseSquareFoot)
        return self.__inverse_square_feet

    
    @property
    def inverse_us_survey_square_feet(self) -> float:
        """
        
        """
        if self.__inverse_us_survey_square_feet != None:
            return self.__inverse_us_survey_square_feet
        self.__inverse_us_survey_square_feet = self.__convert_from_base(ReciprocalAreaUnits.InverseUsSurveySquareFoot)
        return self.__inverse_us_survey_square_feet

    
    @property
    def inverse_square_inches(self) -> float:
        """
        
        """
        if self.__inverse_square_inches != None:
            return self.__inverse_square_inches
        self.__inverse_square_inches = self.__convert_from_base(ReciprocalAreaUnits.InverseSquareInch)
        return self.__inverse_square_inches

    
    def to_string(self, unit: ReciprocalAreaUnits = ReciprocalAreaUnits.InverseSquareMeter) -> str:
        """
        Format the ReciprocalArea to string.
        Note! the default format for ReciprocalArea is InverseSquareMeter.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == ReciprocalAreaUnits.InverseSquareMeter:
            return f"""{self.inverse_square_meters} m⁻²"""
        
        if unit == ReciprocalAreaUnits.InverseSquareKilometer:
            return f"""{self.inverse_square_kilometers} km⁻²"""
        
        if unit == ReciprocalAreaUnits.InverseSquareDecimeter:
            return f"""{self.inverse_square_decimeters} dm⁻²"""
        
        if unit == ReciprocalAreaUnits.InverseSquareCentimeter:
            return f"""{self.inverse_square_centimeters} cm⁻²"""
        
        if unit == ReciprocalAreaUnits.InverseSquareMillimeter:
            return f"""{self.inverse_square_millimeters} mm⁻²"""
        
        if unit == ReciprocalAreaUnits.InverseSquareMicrometer:
            return f"""{self.inverse_square_micrometers} µm⁻²"""
        
        if unit == ReciprocalAreaUnits.InverseSquareMile:
            return f"""{self.inverse_square_miles} mi⁻²"""
        
        if unit == ReciprocalAreaUnits.InverseSquareYard:
            return f"""{self.inverse_square_yards} yd⁻²"""
        
        if unit == ReciprocalAreaUnits.InverseSquareFoot:
            return f"""{self.inverse_square_feet} ft⁻²"""
        
        if unit == ReciprocalAreaUnits.InverseUsSurveySquareFoot:
            return f"""{self.inverse_us_survey_square_feet} ft⁻² (US)"""
        
        if unit == ReciprocalAreaUnits.InverseSquareInch:
            return f"""{self.inverse_square_inches} in⁻²"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: ReciprocalAreaUnits = ReciprocalAreaUnits.InverseSquareMeter) -> str:
        """
        Get ReciprocalArea unit abbreviation.
        Note! the default abbreviation for ReciprocalArea is InverseSquareMeter.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == ReciprocalAreaUnits.InverseSquareMeter:
            return """m⁻²"""
        
        if unit_abbreviation == ReciprocalAreaUnits.InverseSquareKilometer:
            return """km⁻²"""
        
        if unit_abbreviation == ReciprocalAreaUnits.InverseSquareDecimeter:
            return """dm⁻²"""
        
        if unit_abbreviation == ReciprocalAreaUnits.InverseSquareCentimeter:
            return """cm⁻²"""
        
        if unit_abbreviation == ReciprocalAreaUnits.InverseSquareMillimeter:
            return """mm⁻²"""
        
        if unit_abbreviation == ReciprocalAreaUnits.InverseSquareMicrometer:
            return """µm⁻²"""
        
        if unit_abbreviation == ReciprocalAreaUnits.InverseSquareMile:
            return """mi⁻²"""
        
        if unit_abbreviation == ReciprocalAreaUnits.InverseSquareYard:
            return """yd⁻²"""
        
        if unit_abbreviation == ReciprocalAreaUnits.InverseSquareFoot:
            return """ft⁻²"""
        
        if unit_abbreviation == ReciprocalAreaUnits.InverseUsSurveySquareFoot:
            return """ft⁻² (US)"""
        
        if unit_abbreviation == ReciprocalAreaUnits.InverseSquareInch:
            return """in⁻²"""
        
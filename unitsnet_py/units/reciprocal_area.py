from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class ReciprocalAreaUnits(Enum):
        """
            ReciprocalAreaUnits enumeration
        """
        
        InverseSquareMeter = 'InverseSquareMeter'
        """
            
        """
        
        InverseSquareKilometer = 'InverseSquareKilometer'
        """
            
        """
        
        InverseSquareDecimeter = 'InverseSquareDecimeter'
        """
            
        """
        
        InverseSquareCentimeter = 'InverseSquareCentimeter'
        """
            
        """
        
        InverseSquareMillimeter = 'InverseSquareMillimeter'
        """
            
        """
        
        InverseSquareMicrometer = 'InverseSquareMicrometer'
        """
            
        """
        
        InverseSquareMile = 'InverseSquareMile'
        """
            
        """
        
        InverseSquareYard = 'InverseSquareYard'
        """
            
        """
        
        InverseSquareFoot = 'InverseSquareFoot'
        """
            
        """
        
        InverseUsSurveySquareFoot = 'InverseUsSurveySquareFoot'
        """
            
        """
        
        InverseSquareInch = 'InverseSquareInch'
        """
            
        """
        

class ReciprocalAreaDto:
    """
    A DTO representation of a ReciprocalArea

    Attributes:
        value (float): The value of the ReciprocalArea.
        unit (ReciprocalAreaUnits): The specific unit that the ReciprocalArea value is representing.
    """

    def __init__(self, value: float, unit: ReciprocalAreaUnits):
        """
        Create a new DTO representation of a ReciprocalArea

        Parameters:
            value (float): The value of the ReciprocalArea.
            unit (ReciprocalAreaUnits): The specific unit that the ReciprocalArea value is representing.
        """
        self.value: float = value
        """
        The value of the ReciprocalArea
        """
        self.unit: ReciprocalAreaUnits = unit
        """
        The specific unit that the ReciprocalArea value is representing
        """

    def to_json(self):
        """
        Get a ReciprocalArea DTO JSON object representing the current unit.

        :return: JSON object represents ReciprocalArea DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "InverseSquareMeter"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of ReciprocalArea DTO from a json representation.

        :param data: The ReciprocalArea DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "InverseSquareMeter"}
        :return: A new instance of ReciprocalAreaDto.
        :rtype: ReciprocalAreaDto
        """
        return ReciprocalAreaDto(value=data["value"], unit=ReciprocalAreaUnits(data["unit"]))


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

    def to_dto(self, hold_in_unit: ReciprocalAreaUnits = ReciprocalAreaUnits.InverseSquareMeter) -> ReciprocalAreaDto:
        """
        Get a new instance of ReciprocalArea DTO representing the current unit.

        :param hold_in_unit: The specific ReciprocalArea unit to store the ReciprocalArea value in the DTO representation.
        :type hold_in_unit: ReciprocalAreaUnits
        :return: A new instance of ReciprocalAreaDto.
        :rtype: ReciprocalAreaDto
        """
        return ReciprocalAreaDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: ReciprocalAreaUnits = ReciprocalAreaUnits.InverseSquareMeter):
        """
        Get a ReciprocalArea DTO JSON object representing the current unit.

        :param hold_in_unit: The specific ReciprocalArea unit to store the ReciprocalArea value in the DTO representation.
        :type hold_in_unit: ReciprocalAreaUnits
        :return: JSON object represents ReciprocalArea DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "InverseSquareMeter"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(reciprocal_area_dto: ReciprocalAreaDto):
        """
        Obtain a new instance of ReciprocalArea from a DTO unit object.

        :param reciprocal_area_dto: The ReciprocalArea DTO representation.
        :type reciprocal_area_dto: ReciprocalAreaDto
        :return: A new instance of ReciprocalArea.
        :rtype: ReciprocalArea
        """
        return ReciprocalArea(reciprocal_area_dto.value, reciprocal_area_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of ReciprocalArea from a DTO unit json representation.

        :param data: The ReciprocalArea DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "InverseSquareMeter"}
        :return: A new instance of ReciprocalArea.
        :rtype: ReciprocalArea
        """
        return ReciprocalArea.from_dto(ReciprocalAreaDto.from_json(data))

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

    
    def to_string(self, unit: ReciprocalAreaUnits = ReciprocalAreaUnits.InverseSquareMeter, fractional_digits: int = None) -> str:
        """
        Format the ReciprocalArea to a string.
        
        Note: the default format for ReciprocalArea is InverseSquareMeter.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the ReciprocalArea. Default is 'InverseSquareMeter'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == ReciprocalAreaUnits.InverseSquareMeter:
            return f"""{super()._truncate_fraction_digits(self.inverse_square_meters, fractional_digits)} m⁻²"""
        
        if unit == ReciprocalAreaUnits.InverseSquareKilometer:
            return f"""{super()._truncate_fraction_digits(self.inverse_square_kilometers, fractional_digits)} km⁻²"""
        
        if unit == ReciprocalAreaUnits.InverseSquareDecimeter:
            return f"""{super()._truncate_fraction_digits(self.inverse_square_decimeters, fractional_digits)} dm⁻²"""
        
        if unit == ReciprocalAreaUnits.InverseSquareCentimeter:
            return f"""{super()._truncate_fraction_digits(self.inverse_square_centimeters, fractional_digits)} cm⁻²"""
        
        if unit == ReciprocalAreaUnits.InverseSquareMillimeter:
            return f"""{super()._truncate_fraction_digits(self.inverse_square_millimeters, fractional_digits)} mm⁻²"""
        
        if unit == ReciprocalAreaUnits.InverseSquareMicrometer:
            return f"""{super()._truncate_fraction_digits(self.inverse_square_micrometers, fractional_digits)} µm⁻²"""
        
        if unit == ReciprocalAreaUnits.InverseSquareMile:
            return f"""{super()._truncate_fraction_digits(self.inverse_square_miles, fractional_digits)} mi⁻²"""
        
        if unit == ReciprocalAreaUnits.InverseSquareYard:
            return f"""{super()._truncate_fraction_digits(self.inverse_square_yards, fractional_digits)} yd⁻²"""
        
        if unit == ReciprocalAreaUnits.InverseSquareFoot:
            return f"""{super()._truncate_fraction_digits(self.inverse_square_feet, fractional_digits)} ft⁻²"""
        
        if unit == ReciprocalAreaUnits.InverseUsSurveySquareFoot:
            return f"""{super()._truncate_fraction_digits(self.inverse_us_survey_square_feet, fractional_digits)} ft⁻² (US)"""
        
        if unit == ReciprocalAreaUnits.InverseSquareInch:
            return f"""{super()._truncate_fraction_digits(self.inverse_square_inches, fractional_digits)} in⁻²"""
        
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
        
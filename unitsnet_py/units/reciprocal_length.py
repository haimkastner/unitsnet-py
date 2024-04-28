from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class ReciprocalLengthUnits(Enum):
        """
            ReciprocalLengthUnits enumeration
        """
        
        InverseMeter = 'InverseMeter'
        """
            
        """
        
        InverseCentimeter = 'InverseCentimeter'
        """
            
        """
        
        InverseMillimeter = 'InverseMillimeter'
        """
            
        """
        
        InverseMile = 'InverseMile'
        """
            
        """
        
        InverseYard = 'InverseYard'
        """
            
        """
        
        InverseFoot = 'InverseFoot'
        """
            
        """
        
        InverseUsSurveyFoot = 'InverseUsSurveyFoot'
        """
            
        """
        
        InverseInch = 'InverseInch'
        """
            
        """
        
        InverseMil = 'InverseMil'
        """
            
        """
        
        InverseMicroinch = 'InverseMicroinch'
        """
            
        """
        

class ReciprocalLengthDto:
    """
    A DTO representation of a ReciprocalLength

    Attributes:
        value (float): The value of the ReciprocalLength.
        unit (ReciprocalLengthUnits): The specific unit that the ReciprocalLength value is representing.
    """

    def __init__(self, value: float, unit: ReciprocalLengthUnits):
        """
        Create a new DTO representation of a ReciprocalLength

        Parameters:
            value (float): The value of the ReciprocalLength.
            unit (ReciprocalLengthUnits): The specific unit that the ReciprocalLength value is representing.
        """
        self.value: float = value
        """
        The value of the ReciprocalLength
        """
        self.unit: ReciprocalLengthUnits = unit
        """
        The specific unit that the ReciprocalLength value is representing
        """

    def to_json(self):
        """
        Get a ReciprocalLength DTO JSON object representing the current unit.

        :return: JSON object represents ReciprocalLength DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "InverseMeter"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of ReciprocalLength DTO from a json representation.

        :param data: The ReciprocalLength DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "InverseMeter"}
        :return: A new instance of ReciprocalLengthDto.
        :rtype: ReciprocalLengthDto
        """
        return ReciprocalLengthDto(value=data["value"], unit=ReciprocalLengthUnits(data["unit"]))


class ReciprocalLength(AbstractMeasure):
    """
    Reciprocal (Inverse) Length is used in various fields of science and mathematics. It is defined as the inverse value of a length unit.

    Args:
        value (float): The value.
        from_unit (ReciprocalLengthUnits): The ReciprocalLength unit to create from, The default unit is InverseMeter
    """
    def __init__(self, value: float, from_unit: ReciprocalLengthUnits = ReciprocalLengthUnits.InverseMeter):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__inverse_meters = None
        
        self.__inverse_centimeters = None
        
        self.__inverse_millimeters = None
        
        self.__inverse_miles = None
        
        self.__inverse_yards = None
        
        self.__inverse_feet = None
        
        self.__inverse_us_survey_feet = None
        
        self.__inverse_inches = None
        
        self.__inverse_mils = None
        
        self.__inverse_microinches = None
        

    def convert(self, unit: ReciprocalLengthUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: ReciprocalLengthUnits = ReciprocalLengthUnits.InverseMeter) -> ReciprocalLengthDto:
        """
        Get a new instance of ReciprocalLength DTO representing the current unit.

        :param hold_in_unit: The specific ReciprocalLength unit to store the ReciprocalLength value in the DTO representation.
        :type hold_in_unit: ReciprocalLengthUnits
        :return: A new instance of ReciprocalLengthDto.
        :rtype: ReciprocalLengthDto
        """
        return ReciprocalLengthDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: ReciprocalLengthUnits = ReciprocalLengthUnits.InverseMeter):
        """
        Get a ReciprocalLength DTO JSON object representing the current unit.

        :param hold_in_unit: The specific ReciprocalLength unit to store the ReciprocalLength value in the DTO representation.
        :type hold_in_unit: ReciprocalLengthUnits
        :return: JSON object represents ReciprocalLength DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "InverseMeter"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(reciprocal_length_dto: ReciprocalLengthDto):
        """
        Obtain a new instance of ReciprocalLength from a DTO unit object.

        :param reciprocal_length_dto: The ReciprocalLength DTO representation.
        :type reciprocal_length_dto: ReciprocalLengthDto
        :return: A new instance of ReciprocalLength.
        :rtype: ReciprocalLength
        """
        return ReciprocalLength(reciprocal_length_dto.value, reciprocal_length_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of ReciprocalLength from a DTO unit json representation.

        :param data: The ReciprocalLength DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "InverseMeter"}
        :return: A new instance of ReciprocalLength.
        :rtype: ReciprocalLength
        """
        return ReciprocalLength.from_dto(ReciprocalLengthDto.from_json(data))

    def __convert_from_base(self, from_unit: ReciprocalLengthUnits) -> float:
        value = self._value
        
        if from_unit == ReciprocalLengthUnits.InverseMeter:
            return (value)
        
        if from_unit == ReciprocalLengthUnits.InverseCentimeter:
            return (value / 1e2)
        
        if from_unit == ReciprocalLengthUnits.InverseMillimeter:
            return (value / 1e3)
        
        if from_unit == ReciprocalLengthUnits.InverseMile:
            return (value * 1609.344)
        
        if from_unit == ReciprocalLengthUnits.InverseYard:
            return (value * 0.9144)
        
        if from_unit == ReciprocalLengthUnits.InverseFoot:
            return (value * 0.3048)
        
        if from_unit == ReciprocalLengthUnits.InverseUsSurveyFoot:
            return (value * 1200 / 3937)
        
        if from_unit == ReciprocalLengthUnits.InverseInch:
            return (value * 2.54e-2)
        
        if from_unit == ReciprocalLengthUnits.InverseMil:
            return (value * 2.54e-5)
        
        if from_unit == ReciprocalLengthUnits.InverseMicroinch:
            return (value * 2.54e-8)
        
        return None


    def __convert_to_base(self, value: float, to_unit: ReciprocalLengthUnits) -> float:
        
        if to_unit == ReciprocalLengthUnits.InverseMeter:
            return (value)
        
        if to_unit == ReciprocalLengthUnits.InverseCentimeter:
            return (value * 1e2)
        
        if to_unit == ReciprocalLengthUnits.InverseMillimeter:
            return (value * 1e3)
        
        if to_unit == ReciprocalLengthUnits.InverseMile:
            return (value / 1609.344)
        
        if to_unit == ReciprocalLengthUnits.InverseYard:
            return (value / 0.9144)
        
        if to_unit == ReciprocalLengthUnits.InverseFoot:
            return (value / 0.3048)
        
        if to_unit == ReciprocalLengthUnits.InverseUsSurveyFoot:
            return (value * 3937 / 1200)
        
        if to_unit == ReciprocalLengthUnits.InverseInch:
            return (value / 2.54e-2)
        
        if to_unit == ReciprocalLengthUnits.InverseMil:
            return (value / 2.54e-5)
        
        if to_unit == ReciprocalLengthUnits.InverseMicroinch:
            return (value / 2.54e-8)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_inverse_meters(inverse_meters: float):
        """
        Create a new instance of ReciprocalLength from a value in inverse_meters.

        

        :param meters: The ReciprocalLength value in inverse_meters.
        :type inverse_meters: float
        :return: A new instance of ReciprocalLength.
        :rtype: ReciprocalLength
        """
        return ReciprocalLength(inverse_meters, ReciprocalLengthUnits.InverseMeter)

    
    @staticmethod
    def from_inverse_centimeters(inverse_centimeters: float):
        """
        Create a new instance of ReciprocalLength from a value in inverse_centimeters.

        

        :param meters: The ReciprocalLength value in inverse_centimeters.
        :type inverse_centimeters: float
        :return: A new instance of ReciprocalLength.
        :rtype: ReciprocalLength
        """
        return ReciprocalLength(inverse_centimeters, ReciprocalLengthUnits.InverseCentimeter)

    
    @staticmethod
    def from_inverse_millimeters(inverse_millimeters: float):
        """
        Create a new instance of ReciprocalLength from a value in inverse_millimeters.

        

        :param meters: The ReciprocalLength value in inverse_millimeters.
        :type inverse_millimeters: float
        :return: A new instance of ReciprocalLength.
        :rtype: ReciprocalLength
        """
        return ReciprocalLength(inverse_millimeters, ReciprocalLengthUnits.InverseMillimeter)

    
    @staticmethod
    def from_inverse_miles(inverse_miles: float):
        """
        Create a new instance of ReciprocalLength from a value in inverse_miles.

        

        :param meters: The ReciprocalLength value in inverse_miles.
        :type inverse_miles: float
        :return: A new instance of ReciprocalLength.
        :rtype: ReciprocalLength
        """
        return ReciprocalLength(inverse_miles, ReciprocalLengthUnits.InverseMile)

    
    @staticmethod
    def from_inverse_yards(inverse_yards: float):
        """
        Create a new instance of ReciprocalLength from a value in inverse_yards.

        

        :param meters: The ReciprocalLength value in inverse_yards.
        :type inverse_yards: float
        :return: A new instance of ReciprocalLength.
        :rtype: ReciprocalLength
        """
        return ReciprocalLength(inverse_yards, ReciprocalLengthUnits.InverseYard)

    
    @staticmethod
    def from_inverse_feet(inverse_feet: float):
        """
        Create a new instance of ReciprocalLength from a value in inverse_feet.

        

        :param meters: The ReciprocalLength value in inverse_feet.
        :type inverse_feet: float
        :return: A new instance of ReciprocalLength.
        :rtype: ReciprocalLength
        """
        return ReciprocalLength(inverse_feet, ReciprocalLengthUnits.InverseFoot)

    
    @staticmethod
    def from_inverse_us_survey_feet(inverse_us_survey_feet: float):
        """
        Create a new instance of ReciprocalLength from a value in inverse_us_survey_feet.

        

        :param meters: The ReciprocalLength value in inverse_us_survey_feet.
        :type inverse_us_survey_feet: float
        :return: A new instance of ReciprocalLength.
        :rtype: ReciprocalLength
        """
        return ReciprocalLength(inverse_us_survey_feet, ReciprocalLengthUnits.InverseUsSurveyFoot)

    
    @staticmethod
    def from_inverse_inches(inverse_inches: float):
        """
        Create a new instance of ReciprocalLength from a value in inverse_inches.

        

        :param meters: The ReciprocalLength value in inverse_inches.
        :type inverse_inches: float
        :return: A new instance of ReciprocalLength.
        :rtype: ReciprocalLength
        """
        return ReciprocalLength(inverse_inches, ReciprocalLengthUnits.InverseInch)

    
    @staticmethod
    def from_inverse_mils(inverse_mils: float):
        """
        Create a new instance of ReciprocalLength from a value in inverse_mils.

        

        :param meters: The ReciprocalLength value in inverse_mils.
        :type inverse_mils: float
        :return: A new instance of ReciprocalLength.
        :rtype: ReciprocalLength
        """
        return ReciprocalLength(inverse_mils, ReciprocalLengthUnits.InverseMil)

    
    @staticmethod
    def from_inverse_microinches(inverse_microinches: float):
        """
        Create a new instance of ReciprocalLength from a value in inverse_microinches.

        

        :param meters: The ReciprocalLength value in inverse_microinches.
        :type inverse_microinches: float
        :return: A new instance of ReciprocalLength.
        :rtype: ReciprocalLength
        """
        return ReciprocalLength(inverse_microinches, ReciprocalLengthUnits.InverseMicroinch)

    
    @property
    def inverse_meters(self) -> float:
        """
        
        """
        if self.__inverse_meters != None:
            return self.__inverse_meters
        self.__inverse_meters = self.__convert_from_base(ReciprocalLengthUnits.InverseMeter)
        return self.__inverse_meters

    
    @property
    def inverse_centimeters(self) -> float:
        """
        
        """
        if self.__inverse_centimeters != None:
            return self.__inverse_centimeters
        self.__inverse_centimeters = self.__convert_from_base(ReciprocalLengthUnits.InverseCentimeter)
        return self.__inverse_centimeters

    
    @property
    def inverse_millimeters(self) -> float:
        """
        
        """
        if self.__inverse_millimeters != None:
            return self.__inverse_millimeters
        self.__inverse_millimeters = self.__convert_from_base(ReciprocalLengthUnits.InverseMillimeter)
        return self.__inverse_millimeters

    
    @property
    def inverse_miles(self) -> float:
        """
        
        """
        if self.__inverse_miles != None:
            return self.__inverse_miles
        self.__inverse_miles = self.__convert_from_base(ReciprocalLengthUnits.InverseMile)
        return self.__inverse_miles

    
    @property
    def inverse_yards(self) -> float:
        """
        
        """
        if self.__inverse_yards != None:
            return self.__inverse_yards
        self.__inverse_yards = self.__convert_from_base(ReciprocalLengthUnits.InverseYard)
        return self.__inverse_yards

    
    @property
    def inverse_feet(self) -> float:
        """
        
        """
        if self.__inverse_feet != None:
            return self.__inverse_feet
        self.__inverse_feet = self.__convert_from_base(ReciprocalLengthUnits.InverseFoot)
        return self.__inverse_feet

    
    @property
    def inverse_us_survey_feet(self) -> float:
        """
        
        """
        if self.__inverse_us_survey_feet != None:
            return self.__inverse_us_survey_feet
        self.__inverse_us_survey_feet = self.__convert_from_base(ReciprocalLengthUnits.InverseUsSurveyFoot)
        return self.__inverse_us_survey_feet

    
    @property
    def inverse_inches(self) -> float:
        """
        
        """
        if self.__inverse_inches != None:
            return self.__inverse_inches
        self.__inverse_inches = self.__convert_from_base(ReciprocalLengthUnits.InverseInch)
        return self.__inverse_inches

    
    @property
    def inverse_mils(self) -> float:
        """
        
        """
        if self.__inverse_mils != None:
            return self.__inverse_mils
        self.__inverse_mils = self.__convert_from_base(ReciprocalLengthUnits.InverseMil)
        return self.__inverse_mils

    
    @property
    def inverse_microinches(self) -> float:
        """
        
        """
        if self.__inverse_microinches != None:
            return self.__inverse_microinches
        self.__inverse_microinches = self.__convert_from_base(ReciprocalLengthUnits.InverseMicroinch)
        return self.__inverse_microinches

    
    def to_string(self, unit: ReciprocalLengthUnits = ReciprocalLengthUnits.InverseMeter, fractional_digits: int = None) -> str:
        """
        Format the ReciprocalLength to a string.
        
        Note: the default format for ReciprocalLength is InverseMeter.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the ReciprocalLength. Default is 'InverseMeter'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == ReciprocalLengthUnits.InverseMeter:
            return f"""{super()._truncate_fraction_digits(self.inverse_meters, fractional_digits)} m⁻¹"""
        
        if unit == ReciprocalLengthUnits.InverseCentimeter:
            return f"""{super()._truncate_fraction_digits(self.inverse_centimeters, fractional_digits)} cm⁻¹"""
        
        if unit == ReciprocalLengthUnits.InverseMillimeter:
            return f"""{super()._truncate_fraction_digits(self.inverse_millimeters, fractional_digits)} mm⁻¹"""
        
        if unit == ReciprocalLengthUnits.InverseMile:
            return f"""{super()._truncate_fraction_digits(self.inverse_miles, fractional_digits)} mi⁻¹"""
        
        if unit == ReciprocalLengthUnits.InverseYard:
            return f"""{super()._truncate_fraction_digits(self.inverse_yards, fractional_digits)} yd⁻¹"""
        
        if unit == ReciprocalLengthUnits.InverseFoot:
            return f"""{super()._truncate_fraction_digits(self.inverse_feet, fractional_digits)} ft⁻¹"""
        
        if unit == ReciprocalLengthUnits.InverseUsSurveyFoot:
            return f"""{super()._truncate_fraction_digits(self.inverse_us_survey_feet, fractional_digits)} ftUS⁻¹"""
        
        if unit == ReciprocalLengthUnits.InverseInch:
            return f"""{super()._truncate_fraction_digits(self.inverse_inches, fractional_digits)} in⁻¹"""
        
        if unit == ReciprocalLengthUnits.InverseMil:
            return f"""{super()._truncate_fraction_digits(self.inverse_mils, fractional_digits)} mil⁻¹"""
        
        if unit == ReciprocalLengthUnits.InverseMicroinch:
            return f"""{super()._truncate_fraction_digits(self.inverse_microinches, fractional_digits)} µin⁻¹"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: ReciprocalLengthUnits = ReciprocalLengthUnits.InverseMeter) -> str:
        """
        Get ReciprocalLength unit abbreviation.
        Note! the default abbreviation for ReciprocalLength is InverseMeter.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == ReciprocalLengthUnits.InverseMeter:
            return """m⁻¹"""
        
        if unit_abbreviation == ReciprocalLengthUnits.InverseCentimeter:
            return """cm⁻¹"""
        
        if unit_abbreviation == ReciprocalLengthUnits.InverseMillimeter:
            return """mm⁻¹"""
        
        if unit_abbreviation == ReciprocalLengthUnits.InverseMile:
            return """mi⁻¹"""
        
        if unit_abbreviation == ReciprocalLengthUnits.InverseYard:
            return """yd⁻¹"""
        
        if unit_abbreviation == ReciprocalLengthUnits.InverseFoot:
            return """ft⁻¹"""
        
        if unit_abbreviation == ReciprocalLengthUnits.InverseUsSurveyFoot:
            return """ftUS⁻¹"""
        
        if unit_abbreviation == ReciprocalLengthUnits.InverseInch:
            return """in⁻¹"""
        
        if unit_abbreviation == ReciprocalLengthUnits.InverseMil:
            return """mil⁻¹"""
        
        if unit_abbreviation == ReciprocalLengthUnits.InverseMicroinch:
            return """µin⁻¹"""
        
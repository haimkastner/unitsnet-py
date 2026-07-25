from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class AreaPerLengthUnits(Enum):
        """
            AreaPerLengthUnits enumeration
        """
        
        SquareMeterPerMeter = 'SquareMeterPerMeter'
        """
            
        """
        
        SquareCentimeterPerMeter = 'SquareCentimeterPerMeter'
        """
            
        """
        
        SquareMillimeterPerMeter = 'SquareMillimeterPerMeter'
        """
            
        """
        
        SquareInchPerFoot = 'SquareInchPerFoot'
        """
            
        """
        
        SquareInchPerInch = 'SquareInchPerInch'
        """
            
        """
        
        SquareFootPerFoot = 'SquareFootPerFoot'
        """
            
        """
        

class AreaPerLengthDto:
    """
    A DTO representation of a AreaPerLength

    Attributes:
        value (float): The value of the AreaPerLength.
        unit (AreaPerLengthUnits): The specific unit that the AreaPerLength value is representing.
    """

    def __init__(self, value: float, unit: AreaPerLengthUnits):
        """
        Create a new DTO representation of a AreaPerLength

        Parameters:
            value (float): The value of the AreaPerLength.
            unit (AreaPerLengthUnits): The specific unit that the AreaPerLength value is representing.
        """
        self.value: float = value
        """
        The value of the AreaPerLength
        """
        self.unit: AreaPerLengthUnits = unit
        """
        The specific unit that the AreaPerLength value is representing
        """

    def to_json(self):
        """
        Get a AreaPerLength DTO JSON object representing the current unit.

        :return: JSON object represents AreaPerLength DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "SquareMeterPerMeter"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of AreaPerLength DTO from a json representation.

        :param data: The AreaPerLength DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "SquareMeterPerMeter"}
        :return: A new instance of AreaPerLengthDto.
        :rtype: AreaPerLengthDto
        """
        return AreaPerLengthDto(value=data["value"], unit=AreaPerLengthUnits(data["unit"]))


class AreaPerLength(AbstractMeasure):
    """
    The magnitude of area per unit length, typically used in structural engineering to specify distributed reinforcement.

    Args:
        value (float): The value.
        from_unit (AreaPerLengthUnits): The AreaPerLength unit to create from, The default unit is SquareMeterPerMeter
    """
    def __init__(self, value: float, from_unit: AreaPerLengthUnits = AreaPerLengthUnits.SquareMeterPerMeter):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__square_meters_per_meter = None
        
        self.__square_centimeters_per_meter = None
        
        self.__square_millimeters_per_meter = None
        
        self.__square_inches_per_foot = None
        
        self.__square_inches_per_inch = None
        
        self.__square_feet_per_foot = None
        

    def convert(self, unit: AreaPerLengthUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: AreaPerLengthUnits = AreaPerLengthUnits.SquareMeterPerMeter) -> AreaPerLengthDto:
        """
        Get a new instance of AreaPerLength DTO representing the current unit.

        :param hold_in_unit: The specific AreaPerLength unit to store the AreaPerLength value in the DTO representation.
        :type hold_in_unit: AreaPerLengthUnits
        :return: A new instance of AreaPerLengthDto.
        :rtype: AreaPerLengthDto
        """
        return AreaPerLengthDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: AreaPerLengthUnits = AreaPerLengthUnits.SquareMeterPerMeter):
        """
        Get a AreaPerLength DTO JSON object representing the current unit.

        :param hold_in_unit: The specific AreaPerLength unit to store the AreaPerLength value in the DTO representation.
        :type hold_in_unit: AreaPerLengthUnits
        :return: JSON object represents AreaPerLength DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "SquareMeterPerMeter"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(area_per_length_dto: AreaPerLengthDto):
        """
        Obtain a new instance of AreaPerLength from a DTO unit object.

        :param area_per_length_dto: The AreaPerLength DTO representation.
        :type area_per_length_dto: AreaPerLengthDto
        :return: A new instance of AreaPerLength.
        :rtype: AreaPerLength
        """
        return AreaPerLength(area_per_length_dto.value, area_per_length_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of AreaPerLength from a DTO unit json representation.

        :param data: The AreaPerLength DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "SquareMeterPerMeter"}
        :return: A new instance of AreaPerLength.
        :rtype: AreaPerLength
        """
        return AreaPerLength.from_dto(AreaPerLengthDto.from_json(data))

    def __convert_from_base(self, from_unit: AreaPerLengthUnits) -> float:
        value = self._value
        
        if from_unit == AreaPerLengthUnits.SquareMeterPerMeter:
            return (value)
        
        if from_unit == AreaPerLengthUnits.SquareCentimeterPerMeter:
            return (value / 1e-4)
        
        if from_unit == AreaPerLengthUnits.SquareMillimeterPerMeter:
            return (value / 1e-6)
        
        if from_unit == AreaPerLengthUnits.SquareInchPerFoot:
            return (value * 0.3048 / 0.00064516)
        
        if from_unit == AreaPerLengthUnits.SquareInchPerInch:
            return (value * 0.0254 / 0.00064516)
        
        if from_unit == AreaPerLengthUnits.SquareFootPerFoot:
            return (value * 0.3048 / 0.09290304)
        
        return None


    def __convert_to_base(self, value: float, to_unit: AreaPerLengthUnits) -> float:
        
        if to_unit == AreaPerLengthUnits.SquareMeterPerMeter:
            return (value)
        
        if to_unit == AreaPerLengthUnits.SquareCentimeterPerMeter:
            return (value * 1e-4)
        
        if to_unit == AreaPerLengthUnits.SquareMillimeterPerMeter:
            return (value * 1e-6)
        
        if to_unit == AreaPerLengthUnits.SquareInchPerFoot:
            return (value * 0.00064516 / 0.3048)
        
        if to_unit == AreaPerLengthUnits.SquareInchPerInch:
            return (value * 0.00064516 / 0.0254)
        
        if to_unit == AreaPerLengthUnits.SquareFootPerFoot:
            return (value * 0.09290304 / 0.3048)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_square_meters_per_meter(square_meters_per_meter: float):
        """
        Create a new instance of AreaPerLength from a value in square_meters_per_meter.

        

        :param meters: The AreaPerLength value in square_meters_per_meter.
        :type square_meters_per_meter: float
        :return: A new instance of AreaPerLength.
        :rtype: AreaPerLength
        """
        return AreaPerLength(square_meters_per_meter, AreaPerLengthUnits.SquareMeterPerMeter)

    
    @staticmethod
    def from_square_centimeters_per_meter(square_centimeters_per_meter: float):
        """
        Create a new instance of AreaPerLength from a value in square_centimeters_per_meter.

        

        :param meters: The AreaPerLength value in square_centimeters_per_meter.
        :type square_centimeters_per_meter: float
        :return: A new instance of AreaPerLength.
        :rtype: AreaPerLength
        """
        return AreaPerLength(square_centimeters_per_meter, AreaPerLengthUnits.SquareCentimeterPerMeter)

    
    @staticmethod
    def from_square_millimeters_per_meter(square_millimeters_per_meter: float):
        """
        Create a new instance of AreaPerLength from a value in square_millimeters_per_meter.

        

        :param meters: The AreaPerLength value in square_millimeters_per_meter.
        :type square_millimeters_per_meter: float
        :return: A new instance of AreaPerLength.
        :rtype: AreaPerLength
        """
        return AreaPerLength(square_millimeters_per_meter, AreaPerLengthUnits.SquareMillimeterPerMeter)

    
    @staticmethod
    def from_square_inches_per_foot(square_inches_per_foot: float):
        """
        Create a new instance of AreaPerLength from a value in square_inches_per_foot.

        

        :param meters: The AreaPerLength value in square_inches_per_foot.
        :type square_inches_per_foot: float
        :return: A new instance of AreaPerLength.
        :rtype: AreaPerLength
        """
        return AreaPerLength(square_inches_per_foot, AreaPerLengthUnits.SquareInchPerFoot)

    
    @staticmethod
    def from_square_inches_per_inch(square_inches_per_inch: float):
        """
        Create a new instance of AreaPerLength from a value in square_inches_per_inch.

        

        :param meters: The AreaPerLength value in square_inches_per_inch.
        :type square_inches_per_inch: float
        :return: A new instance of AreaPerLength.
        :rtype: AreaPerLength
        """
        return AreaPerLength(square_inches_per_inch, AreaPerLengthUnits.SquareInchPerInch)

    
    @staticmethod
    def from_square_feet_per_foot(square_feet_per_foot: float):
        """
        Create a new instance of AreaPerLength from a value in square_feet_per_foot.

        

        :param meters: The AreaPerLength value in square_feet_per_foot.
        :type square_feet_per_foot: float
        :return: A new instance of AreaPerLength.
        :rtype: AreaPerLength
        """
        return AreaPerLength(square_feet_per_foot, AreaPerLengthUnits.SquareFootPerFoot)

    
    @property
    def square_meters_per_meter(self) -> float:
        """
        
        """
        if self.__square_meters_per_meter != None:
            return self.__square_meters_per_meter
        self.__square_meters_per_meter = self.__convert_from_base(AreaPerLengthUnits.SquareMeterPerMeter)
        return self.__square_meters_per_meter

    
    @property
    def square_centimeters_per_meter(self) -> float:
        """
        
        """
        if self.__square_centimeters_per_meter != None:
            return self.__square_centimeters_per_meter
        self.__square_centimeters_per_meter = self.__convert_from_base(AreaPerLengthUnits.SquareCentimeterPerMeter)
        return self.__square_centimeters_per_meter

    
    @property
    def square_millimeters_per_meter(self) -> float:
        """
        
        """
        if self.__square_millimeters_per_meter != None:
            return self.__square_millimeters_per_meter
        self.__square_millimeters_per_meter = self.__convert_from_base(AreaPerLengthUnits.SquareMillimeterPerMeter)
        return self.__square_millimeters_per_meter

    
    @property
    def square_inches_per_foot(self) -> float:
        """
        
        """
        if self.__square_inches_per_foot != None:
            return self.__square_inches_per_foot
        self.__square_inches_per_foot = self.__convert_from_base(AreaPerLengthUnits.SquareInchPerFoot)
        return self.__square_inches_per_foot

    
    @property
    def square_inches_per_inch(self) -> float:
        """
        
        """
        if self.__square_inches_per_inch != None:
            return self.__square_inches_per_inch
        self.__square_inches_per_inch = self.__convert_from_base(AreaPerLengthUnits.SquareInchPerInch)
        return self.__square_inches_per_inch

    
    @property
    def square_feet_per_foot(self) -> float:
        """
        
        """
        if self.__square_feet_per_foot != None:
            return self.__square_feet_per_foot
        self.__square_feet_per_foot = self.__convert_from_base(AreaPerLengthUnits.SquareFootPerFoot)
        return self.__square_feet_per_foot

    
    def to_string(self, unit: AreaPerLengthUnits = AreaPerLengthUnits.SquareMeterPerMeter, fractional_digits: int = None) -> str:
        """
        Format the AreaPerLength to a string.
        
        Note: the default format for AreaPerLength is SquareMeterPerMeter.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the AreaPerLength. Default is 'SquareMeterPerMeter'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == AreaPerLengthUnits.SquareMeterPerMeter:
            return f"""{super()._truncate_fraction_digits(self.square_meters_per_meter, fractional_digits)} m²/m"""
        
        if unit == AreaPerLengthUnits.SquareCentimeterPerMeter:
            return f"""{super()._truncate_fraction_digits(self.square_centimeters_per_meter, fractional_digits)} cm²/m"""
        
        if unit == AreaPerLengthUnits.SquareMillimeterPerMeter:
            return f"""{super()._truncate_fraction_digits(self.square_millimeters_per_meter, fractional_digits)} mm²/m"""
        
        if unit == AreaPerLengthUnits.SquareInchPerFoot:
            return f"""{super()._truncate_fraction_digits(self.square_inches_per_foot, fractional_digits)} in²/ft"""
        
        if unit == AreaPerLengthUnits.SquareInchPerInch:
            return f"""{super()._truncate_fraction_digits(self.square_inches_per_inch, fractional_digits)} in²/in"""
        
        if unit == AreaPerLengthUnits.SquareFootPerFoot:
            return f"""{super()._truncate_fraction_digits(self.square_feet_per_foot, fractional_digits)} ft²/ft"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: AreaPerLengthUnits = AreaPerLengthUnits.SquareMeterPerMeter) -> str:
        """
        Get AreaPerLength unit abbreviation.
        Note! the default abbreviation for AreaPerLength is SquareMeterPerMeter.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == AreaPerLengthUnits.SquareMeterPerMeter:
            return """m²/m"""
        
        if unit_abbreviation == AreaPerLengthUnits.SquareCentimeterPerMeter:
            return """cm²/m"""
        
        if unit_abbreviation == AreaPerLengthUnits.SquareMillimeterPerMeter:
            return """mm²/m"""
        
        if unit_abbreviation == AreaPerLengthUnits.SquareInchPerFoot:
            return """in²/ft"""
        
        if unit_abbreviation == AreaPerLengthUnits.SquareInchPerInch:
            return """in²/in"""
        
        if unit_abbreviation == AreaPerLengthUnits.SquareFootPerFoot:
            return """ft²/ft"""
        
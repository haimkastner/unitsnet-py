from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class VolumePerLengthUnits(Enum):
        """
            VolumePerLengthUnits enumeration
        """
        
        CubicMeterPerMeter = 'CubicMeterPerMeter'
        """
            
        """
        
        LiterPerMeter = 'LiterPerMeter'
        """
            
        """
        
        LiterPerKilometer = 'LiterPerKilometer'
        """
            
        """
        
        LiterPerMillimeter = 'LiterPerMillimeter'
        """
            
        """
        
        OilBarrelPerFoot = 'OilBarrelPerFoot'
        """
            
        """
        
        CubicYardPerFoot = 'CubicYardPerFoot'
        """
            
        """
        
        CubicYardPerUsSurveyFoot = 'CubicYardPerUsSurveyFoot'
        """
            
        """
        
        UsGallonPerMile = 'UsGallonPerMile'
        """
            
        """
        
        ImperialGallonPerMile = 'ImperialGallonPerMile'
        """
            
        """
        

class VolumePerLengthDto:
    """
    A DTO representation of a VolumePerLength

    Attributes:
        value (float): The value of the VolumePerLength.
        unit (VolumePerLengthUnits): The specific unit that the VolumePerLength value is representing.
    """

    def __init__(self, value: float, unit: VolumePerLengthUnits):
        """
        Create a new DTO representation of a VolumePerLength

        Parameters:
            value (float): The value of the VolumePerLength.
            unit (VolumePerLengthUnits): The specific unit that the VolumePerLength value is representing.
        """
        self.value: float = value
        """
        The value of the VolumePerLength
        """
        self.unit: VolumePerLengthUnits = unit
        """
        The specific unit that the VolumePerLength value is representing
        """

    def to_json(self):
        """
        Get a VolumePerLength DTO JSON object representing the current unit.

        :return: JSON object represents VolumePerLength DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "CubicMeterPerMeter"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of VolumePerLength DTO from a json representation.

        :param data: The VolumePerLength DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "CubicMeterPerMeter"}
        :return: A new instance of VolumePerLengthDto.
        :rtype: VolumePerLengthDto
        """
        return VolumePerLengthDto(value=data["value"], unit=VolumePerLengthUnits(data["unit"]))


class VolumePerLength(AbstractMeasure):
    """
    Volume, typically of fluid, that a container can hold within a unit of length.

    Args:
        value (float): The value.
        from_unit (VolumePerLengthUnits): The VolumePerLength unit to create from, The default unit is CubicMeterPerMeter
    """
    def __init__(self, value: float, from_unit: VolumePerLengthUnits = VolumePerLengthUnits.CubicMeterPerMeter):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__cubic_meters_per_meter = None
        
        self.__liters_per_meter = None
        
        self.__liters_per_kilometer = None
        
        self.__liters_per_millimeter = None
        
        self.__oil_barrels_per_foot = None
        
        self.__cubic_yards_per_foot = None
        
        self.__cubic_yards_per_us_survey_foot = None
        
        self.__us_gallons_per_mile = None
        
        self.__imperial_gallons_per_mile = None
        

    def convert(self, unit: VolumePerLengthUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: VolumePerLengthUnits = VolumePerLengthUnits.CubicMeterPerMeter) -> VolumePerLengthDto:
        """
        Get a new instance of VolumePerLength DTO representing the current unit.

        :param hold_in_unit: The specific VolumePerLength unit to store the VolumePerLength value in the DTO representation.
        :type hold_in_unit: VolumePerLengthUnits
        :return: A new instance of VolumePerLengthDto.
        :rtype: VolumePerLengthDto
        """
        return VolumePerLengthDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: VolumePerLengthUnits = VolumePerLengthUnits.CubicMeterPerMeter):
        """
        Get a VolumePerLength DTO JSON object representing the current unit.

        :param hold_in_unit: The specific VolumePerLength unit to store the VolumePerLength value in the DTO representation.
        :type hold_in_unit: VolumePerLengthUnits
        :return: JSON object represents VolumePerLength DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "CubicMeterPerMeter"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(volume_per_length_dto: VolumePerLengthDto):
        """
        Obtain a new instance of VolumePerLength from a DTO unit object.

        :param volume_per_length_dto: The VolumePerLength DTO representation.
        :type volume_per_length_dto: VolumePerLengthDto
        :return: A new instance of VolumePerLength.
        :rtype: VolumePerLength
        """
        return VolumePerLength(volume_per_length_dto.value, volume_per_length_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of VolumePerLength from a DTO unit json representation.

        :param data: The VolumePerLength DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "CubicMeterPerMeter"}
        :return: A new instance of VolumePerLength.
        :rtype: VolumePerLength
        """
        return VolumePerLength.from_dto(VolumePerLengthDto.from_json(data))

    def __convert_from_base(self, from_unit: VolumePerLengthUnits) -> float:
        value = self._value
        
        if from_unit == VolumePerLengthUnits.CubicMeterPerMeter:
            return (value)
        
        if from_unit == VolumePerLengthUnits.LiterPerMeter:
            return (value * 1000)
        
        if from_unit == VolumePerLengthUnits.LiterPerKilometer:
            return (value * 1e6)
        
        if from_unit == VolumePerLengthUnits.LiterPerMillimeter:
            return (value)
        
        if from_unit == VolumePerLengthUnits.OilBarrelPerFoot:
            return (value * 1.91713408)
        
        if from_unit == VolumePerLengthUnits.CubicYardPerFoot:
            return (value / 2.50838208)
        
        if from_unit == VolumePerLengthUnits.CubicYardPerUsSurveyFoot:
            return (value / 2.50837706323584)
        
        if from_unit == VolumePerLengthUnits.UsGallonPerMile:
            return (value * (1000 * 1609.344 / 3.785411784))
        
        if from_unit == VolumePerLengthUnits.ImperialGallonPerMile:
            return (value * (1000 * 1609.344 / 4.54609))
        
        return None


    def __convert_to_base(self, value: float, to_unit: VolumePerLengthUnits) -> float:
        
        if to_unit == VolumePerLengthUnits.CubicMeterPerMeter:
            return (value)
        
        if to_unit == VolumePerLengthUnits.LiterPerMeter:
            return (value / 1000)
        
        if to_unit == VolumePerLengthUnits.LiterPerKilometer:
            return (value / 1e6)
        
        if to_unit == VolumePerLengthUnits.LiterPerMillimeter:
            return (value)
        
        if to_unit == VolumePerLengthUnits.OilBarrelPerFoot:
            return (value / 1.91713408)
        
        if to_unit == VolumePerLengthUnits.CubicYardPerFoot:
            return (value * 2.50838208)
        
        if to_unit == VolumePerLengthUnits.CubicYardPerUsSurveyFoot:
            return (value * 2.50837706323584)
        
        if to_unit == VolumePerLengthUnits.UsGallonPerMile:
            return (value / (1000 * 1609.344 / 3.785411784))
        
        if to_unit == VolumePerLengthUnits.ImperialGallonPerMile:
            return (value / (1000 * 1609.344 / 4.54609))
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_cubic_meters_per_meter(cubic_meters_per_meter: float):
        """
        Create a new instance of VolumePerLength from a value in cubic_meters_per_meter.

        

        :param meters: The VolumePerLength value in cubic_meters_per_meter.
        :type cubic_meters_per_meter: float
        :return: A new instance of VolumePerLength.
        :rtype: VolumePerLength
        """
        return VolumePerLength(cubic_meters_per_meter, VolumePerLengthUnits.CubicMeterPerMeter)

    
    @staticmethod
    def from_liters_per_meter(liters_per_meter: float):
        """
        Create a new instance of VolumePerLength from a value in liters_per_meter.

        

        :param meters: The VolumePerLength value in liters_per_meter.
        :type liters_per_meter: float
        :return: A new instance of VolumePerLength.
        :rtype: VolumePerLength
        """
        return VolumePerLength(liters_per_meter, VolumePerLengthUnits.LiterPerMeter)

    
    @staticmethod
    def from_liters_per_kilometer(liters_per_kilometer: float):
        """
        Create a new instance of VolumePerLength from a value in liters_per_kilometer.

        

        :param meters: The VolumePerLength value in liters_per_kilometer.
        :type liters_per_kilometer: float
        :return: A new instance of VolumePerLength.
        :rtype: VolumePerLength
        """
        return VolumePerLength(liters_per_kilometer, VolumePerLengthUnits.LiterPerKilometer)

    
    @staticmethod
    def from_liters_per_millimeter(liters_per_millimeter: float):
        """
        Create a new instance of VolumePerLength from a value in liters_per_millimeter.

        

        :param meters: The VolumePerLength value in liters_per_millimeter.
        :type liters_per_millimeter: float
        :return: A new instance of VolumePerLength.
        :rtype: VolumePerLength
        """
        return VolumePerLength(liters_per_millimeter, VolumePerLengthUnits.LiterPerMillimeter)

    
    @staticmethod
    def from_oil_barrels_per_foot(oil_barrels_per_foot: float):
        """
        Create a new instance of VolumePerLength from a value in oil_barrels_per_foot.

        

        :param meters: The VolumePerLength value in oil_barrels_per_foot.
        :type oil_barrels_per_foot: float
        :return: A new instance of VolumePerLength.
        :rtype: VolumePerLength
        """
        return VolumePerLength(oil_barrels_per_foot, VolumePerLengthUnits.OilBarrelPerFoot)

    
    @staticmethod
    def from_cubic_yards_per_foot(cubic_yards_per_foot: float):
        """
        Create a new instance of VolumePerLength from a value in cubic_yards_per_foot.

        

        :param meters: The VolumePerLength value in cubic_yards_per_foot.
        :type cubic_yards_per_foot: float
        :return: A new instance of VolumePerLength.
        :rtype: VolumePerLength
        """
        return VolumePerLength(cubic_yards_per_foot, VolumePerLengthUnits.CubicYardPerFoot)

    
    @staticmethod
    def from_cubic_yards_per_us_survey_foot(cubic_yards_per_us_survey_foot: float):
        """
        Create a new instance of VolumePerLength from a value in cubic_yards_per_us_survey_foot.

        

        :param meters: The VolumePerLength value in cubic_yards_per_us_survey_foot.
        :type cubic_yards_per_us_survey_foot: float
        :return: A new instance of VolumePerLength.
        :rtype: VolumePerLength
        """
        return VolumePerLength(cubic_yards_per_us_survey_foot, VolumePerLengthUnits.CubicYardPerUsSurveyFoot)

    
    @staticmethod
    def from_us_gallons_per_mile(us_gallons_per_mile: float):
        """
        Create a new instance of VolumePerLength from a value in us_gallons_per_mile.

        

        :param meters: The VolumePerLength value in us_gallons_per_mile.
        :type us_gallons_per_mile: float
        :return: A new instance of VolumePerLength.
        :rtype: VolumePerLength
        """
        return VolumePerLength(us_gallons_per_mile, VolumePerLengthUnits.UsGallonPerMile)

    
    @staticmethod
    def from_imperial_gallons_per_mile(imperial_gallons_per_mile: float):
        """
        Create a new instance of VolumePerLength from a value in imperial_gallons_per_mile.

        

        :param meters: The VolumePerLength value in imperial_gallons_per_mile.
        :type imperial_gallons_per_mile: float
        :return: A new instance of VolumePerLength.
        :rtype: VolumePerLength
        """
        return VolumePerLength(imperial_gallons_per_mile, VolumePerLengthUnits.ImperialGallonPerMile)

    
    @property
    def cubic_meters_per_meter(self) -> float:
        """
        
        """
        if self.__cubic_meters_per_meter != None:
            return self.__cubic_meters_per_meter
        self.__cubic_meters_per_meter = self.__convert_from_base(VolumePerLengthUnits.CubicMeterPerMeter)
        return self.__cubic_meters_per_meter

    
    @property
    def liters_per_meter(self) -> float:
        """
        
        """
        if self.__liters_per_meter != None:
            return self.__liters_per_meter
        self.__liters_per_meter = self.__convert_from_base(VolumePerLengthUnits.LiterPerMeter)
        return self.__liters_per_meter

    
    @property
    def liters_per_kilometer(self) -> float:
        """
        
        """
        if self.__liters_per_kilometer != None:
            return self.__liters_per_kilometer
        self.__liters_per_kilometer = self.__convert_from_base(VolumePerLengthUnits.LiterPerKilometer)
        return self.__liters_per_kilometer

    
    @property
    def liters_per_millimeter(self) -> float:
        """
        
        """
        if self.__liters_per_millimeter != None:
            return self.__liters_per_millimeter
        self.__liters_per_millimeter = self.__convert_from_base(VolumePerLengthUnits.LiterPerMillimeter)
        return self.__liters_per_millimeter

    
    @property
    def oil_barrels_per_foot(self) -> float:
        """
        
        """
        if self.__oil_barrels_per_foot != None:
            return self.__oil_barrels_per_foot
        self.__oil_barrels_per_foot = self.__convert_from_base(VolumePerLengthUnits.OilBarrelPerFoot)
        return self.__oil_barrels_per_foot

    
    @property
    def cubic_yards_per_foot(self) -> float:
        """
        
        """
        if self.__cubic_yards_per_foot != None:
            return self.__cubic_yards_per_foot
        self.__cubic_yards_per_foot = self.__convert_from_base(VolumePerLengthUnits.CubicYardPerFoot)
        return self.__cubic_yards_per_foot

    
    @property
    def cubic_yards_per_us_survey_foot(self) -> float:
        """
        
        """
        if self.__cubic_yards_per_us_survey_foot != None:
            return self.__cubic_yards_per_us_survey_foot
        self.__cubic_yards_per_us_survey_foot = self.__convert_from_base(VolumePerLengthUnits.CubicYardPerUsSurveyFoot)
        return self.__cubic_yards_per_us_survey_foot

    
    @property
    def us_gallons_per_mile(self) -> float:
        """
        
        """
        if self.__us_gallons_per_mile != None:
            return self.__us_gallons_per_mile
        self.__us_gallons_per_mile = self.__convert_from_base(VolumePerLengthUnits.UsGallonPerMile)
        return self.__us_gallons_per_mile

    
    @property
    def imperial_gallons_per_mile(self) -> float:
        """
        
        """
        if self.__imperial_gallons_per_mile != None:
            return self.__imperial_gallons_per_mile
        self.__imperial_gallons_per_mile = self.__convert_from_base(VolumePerLengthUnits.ImperialGallonPerMile)
        return self.__imperial_gallons_per_mile

    
    def to_string(self, unit: VolumePerLengthUnits = VolumePerLengthUnits.CubicMeterPerMeter, fractional_digits: int = None) -> str:
        """
        Format the VolumePerLength to a string.
        
        Note: the default format for VolumePerLength is CubicMeterPerMeter.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the VolumePerLength. Default is 'CubicMeterPerMeter'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == VolumePerLengthUnits.CubicMeterPerMeter:
            return f"""{super()._truncate_fraction_digits(self.cubic_meters_per_meter, fractional_digits)} m³/m"""
        
        if unit == VolumePerLengthUnits.LiterPerMeter:
            return f"""{super()._truncate_fraction_digits(self.liters_per_meter, fractional_digits)} l/m"""
        
        if unit == VolumePerLengthUnits.LiterPerKilometer:
            return f"""{super()._truncate_fraction_digits(self.liters_per_kilometer, fractional_digits)} l/km"""
        
        if unit == VolumePerLengthUnits.LiterPerMillimeter:
            return f"""{super()._truncate_fraction_digits(self.liters_per_millimeter, fractional_digits)} l/mm"""
        
        if unit == VolumePerLengthUnits.OilBarrelPerFoot:
            return f"""{super()._truncate_fraction_digits(self.oil_barrels_per_foot, fractional_digits)} bbl/ft"""
        
        if unit == VolumePerLengthUnits.CubicYardPerFoot:
            return f"""{super()._truncate_fraction_digits(self.cubic_yards_per_foot, fractional_digits)} yd³/ft"""
        
        if unit == VolumePerLengthUnits.CubicYardPerUsSurveyFoot:
            return f"""{super()._truncate_fraction_digits(self.cubic_yards_per_us_survey_foot, fractional_digits)} yd³/ftUS"""
        
        if unit == VolumePerLengthUnits.UsGallonPerMile:
            return f"""{super()._truncate_fraction_digits(self.us_gallons_per_mile, fractional_digits)} gal (U.S.)/mi"""
        
        if unit == VolumePerLengthUnits.ImperialGallonPerMile:
            return f"""{super()._truncate_fraction_digits(self.imperial_gallons_per_mile, fractional_digits)} gal (imp.)/mi"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: VolumePerLengthUnits = VolumePerLengthUnits.CubicMeterPerMeter) -> str:
        """
        Get VolumePerLength unit abbreviation.
        Note! the default abbreviation for VolumePerLength is CubicMeterPerMeter.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == VolumePerLengthUnits.CubicMeterPerMeter:
            return """m³/m"""
        
        if unit_abbreviation == VolumePerLengthUnits.LiterPerMeter:
            return """l/m"""
        
        if unit_abbreviation == VolumePerLengthUnits.LiterPerKilometer:
            return """l/km"""
        
        if unit_abbreviation == VolumePerLengthUnits.LiterPerMillimeter:
            return """l/mm"""
        
        if unit_abbreviation == VolumePerLengthUnits.OilBarrelPerFoot:
            return """bbl/ft"""
        
        if unit_abbreviation == VolumePerLengthUnits.CubicYardPerFoot:
            return """yd³/ft"""
        
        if unit_abbreviation == VolumePerLengthUnits.CubicYardPerUsSurveyFoot:
            return """yd³/ftUS"""
        
        if unit_abbreviation == VolumePerLengthUnits.UsGallonPerMile:
            return """gal (U.S.)/mi"""
        
        if unit_abbreviation == VolumePerLengthUnits.ImperialGallonPerMile:
            return """gal (imp.)/mi"""
        
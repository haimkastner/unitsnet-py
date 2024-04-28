from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class SpecificVolumeUnits(Enum):
        """
            SpecificVolumeUnits enumeration
        """
        
        CubicMeterPerKilogram = 'CubicMeterPerKilogram'
        """
            
        """
        
        CubicFootPerPound = 'CubicFootPerPound'
        """
            
        """
        
        MillicubicMeterPerKilogram = 'MillicubicMeterPerKilogram'
        """
            
        """
        

class SpecificVolumeDto:
    """
    A DTO representation of a SpecificVolume

    Attributes:
        value (float): The value of the SpecificVolume.
        unit (SpecificVolumeUnits): The specific unit that the SpecificVolume value is representing.
    """

    def __init__(self, value: float, unit: SpecificVolumeUnits):
        """
        Create a new DTO representation of a SpecificVolume

        Parameters:
            value (float): The value of the SpecificVolume.
            unit (SpecificVolumeUnits): The specific unit that the SpecificVolume value is representing.
        """
        self.value: float = value
        """
        The value of the SpecificVolume
        """
        self.unit: SpecificVolumeUnits = unit
        """
        The specific unit that the SpecificVolume value is representing
        """

    def to_json(self):
        """
        Get a SpecificVolume DTO JSON object representing the current unit.

        :return: JSON object represents SpecificVolume DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "CubicMeterPerKilogram"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of SpecificVolume DTO from a json representation.

        :param data: The SpecificVolume DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "CubicMeterPerKilogram"}
        :return: A new instance of SpecificVolumeDto.
        :rtype: SpecificVolumeDto
        """
        return SpecificVolumeDto(value=data["value"], unit=SpecificVolumeUnits(data["unit"]))


class SpecificVolume(AbstractMeasure):
    """
    In thermodynamics, the specific volume of a substance is the ratio of the substance's volume to its mass. It is the reciprocal of density and an intrinsic property of matter as well.

    Args:
        value (float): The value.
        from_unit (SpecificVolumeUnits): The SpecificVolume unit to create from, The default unit is CubicMeterPerKilogram
    """
    def __init__(self, value: float, from_unit: SpecificVolumeUnits = SpecificVolumeUnits.CubicMeterPerKilogram):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__cubic_meters_per_kilogram = None
        
        self.__cubic_feet_per_pound = None
        
        self.__millicubic_meters_per_kilogram = None
        

    def convert(self, unit: SpecificVolumeUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: SpecificVolumeUnits = SpecificVolumeUnits.CubicMeterPerKilogram) -> SpecificVolumeDto:
        """
        Get a new instance of SpecificVolume DTO representing the current unit.

        :param hold_in_unit: The specific SpecificVolume unit to store the SpecificVolume value in the DTO representation.
        :type hold_in_unit: SpecificVolumeUnits
        :return: A new instance of SpecificVolumeDto.
        :rtype: SpecificVolumeDto
        """
        return SpecificVolumeDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: SpecificVolumeUnits = SpecificVolumeUnits.CubicMeterPerKilogram):
        """
        Get a SpecificVolume DTO JSON object representing the current unit.

        :param hold_in_unit: The specific SpecificVolume unit to store the SpecificVolume value in the DTO representation.
        :type hold_in_unit: SpecificVolumeUnits
        :return: JSON object represents SpecificVolume DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "CubicMeterPerKilogram"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(specific_volume_dto: SpecificVolumeDto):
        """
        Obtain a new instance of SpecificVolume from a DTO unit object.

        :param specific_volume_dto: The SpecificVolume DTO representation.
        :type specific_volume_dto: SpecificVolumeDto
        :return: A new instance of SpecificVolume.
        :rtype: SpecificVolume
        """
        return SpecificVolume(specific_volume_dto.value, specific_volume_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of SpecificVolume from a DTO unit json representation.

        :param data: The SpecificVolume DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "CubicMeterPerKilogram"}
        :return: A new instance of SpecificVolume.
        :rtype: SpecificVolume
        """
        return SpecificVolume.from_dto(SpecificVolumeDto.from_json(data))

    def __convert_from_base(self, from_unit: SpecificVolumeUnits) -> float:
        value = self._value
        
        if from_unit == SpecificVolumeUnits.CubicMeterPerKilogram:
            return (value)
        
        if from_unit == SpecificVolumeUnits.CubicFootPerPound:
            return (value * 16.01846353)
        
        if from_unit == SpecificVolumeUnits.MillicubicMeterPerKilogram:
            return ((value) / 0.001)
        
        return None


    def __convert_to_base(self, value: float, to_unit: SpecificVolumeUnits) -> float:
        
        if to_unit == SpecificVolumeUnits.CubicMeterPerKilogram:
            return (value)
        
        if to_unit == SpecificVolumeUnits.CubicFootPerPound:
            return (value / 16.01846353)
        
        if to_unit == SpecificVolumeUnits.MillicubicMeterPerKilogram:
            return ((value) * 0.001)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_cubic_meters_per_kilogram(cubic_meters_per_kilogram: float):
        """
        Create a new instance of SpecificVolume from a value in cubic_meters_per_kilogram.

        

        :param meters: The SpecificVolume value in cubic_meters_per_kilogram.
        :type cubic_meters_per_kilogram: float
        :return: A new instance of SpecificVolume.
        :rtype: SpecificVolume
        """
        return SpecificVolume(cubic_meters_per_kilogram, SpecificVolumeUnits.CubicMeterPerKilogram)

    
    @staticmethod
    def from_cubic_feet_per_pound(cubic_feet_per_pound: float):
        """
        Create a new instance of SpecificVolume from a value in cubic_feet_per_pound.

        

        :param meters: The SpecificVolume value in cubic_feet_per_pound.
        :type cubic_feet_per_pound: float
        :return: A new instance of SpecificVolume.
        :rtype: SpecificVolume
        """
        return SpecificVolume(cubic_feet_per_pound, SpecificVolumeUnits.CubicFootPerPound)

    
    @staticmethod
    def from_millicubic_meters_per_kilogram(millicubic_meters_per_kilogram: float):
        """
        Create a new instance of SpecificVolume from a value in millicubic_meters_per_kilogram.

        

        :param meters: The SpecificVolume value in millicubic_meters_per_kilogram.
        :type millicubic_meters_per_kilogram: float
        :return: A new instance of SpecificVolume.
        :rtype: SpecificVolume
        """
        return SpecificVolume(millicubic_meters_per_kilogram, SpecificVolumeUnits.MillicubicMeterPerKilogram)

    
    @property
    def cubic_meters_per_kilogram(self) -> float:
        """
        
        """
        if self.__cubic_meters_per_kilogram != None:
            return self.__cubic_meters_per_kilogram
        self.__cubic_meters_per_kilogram = self.__convert_from_base(SpecificVolumeUnits.CubicMeterPerKilogram)
        return self.__cubic_meters_per_kilogram

    
    @property
    def cubic_feet_per_pound(self) -> float:
        """
        
        """
        if self.__cubic_feet_per_pound != None:
            return self.__cubic_feet_per_pound
        self.__cubic_feet_per_pound = self.__convert_from_base(SpecificVolumeUnits.CubicFootPerPound)
        return self.__cubic_feet_per_pound

    
    @property
    def millicubic_meters_per_kilogram(self) -> float:
        """
        
        """
        if self.__millicubic_meters_per_kilogram != None:
            return self.__millicubic_meters_per_kilogram
        self.__millicubic_meters_per_kilogram = self.__convert_from_base(SpecificVolumeUnits.MillicubicMeterPerKilogram)
        return self.__millicubic_meters_per_kilogram

    
    def to_string(self, unit: SpecificVolumeUnits = SpecificVolumeUnits.CubicMeterPerKilogram, fractional_digits: int = None) -> str:
        """
        Format the SpecificVolume to a string.
        
        Note: the default format for SpecificVolume is CubicMeterPerKilogram.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the SpecificVolume. Default is 'CubicMeterPerKilogram'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == SpecificVolumeUnits.CubicMeterPerKilogram:
            return f"""{super()._truncate_fraction_digits(self.cubic_meters_per_kilogram, fractional_digits)} m³/kg"""
        
        if unit == SpecificVolumeUnits.CubicFootPerPound:
            return f"""{super()._truncate_fraction_digits(self.cubic_feet_per_pound, fractional_digits)} ft³/lb"""
        
        if unit == SpecificVolumeUnits.MillicubicMeterPerKilogram:
            return f"""{super()._truncate_fraction_digits(self.millicubic_meters_per_kilogram, fractional_digits)} mm³/kg"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: SpecificVolumeUnits = SpecificVolumeUnits.CubicMeterPerKilogram) -> str:
        """
        Get SpecificVolume unit abbreviation.
        Note! the default abbreviation for SpecificVolume is CubicMeterPerKilogram.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == SpecificVolumeUnits.CubicMeterPerKilogram:
            return """m³/kg"""
        
        if unit_abbreviation == SpecificVolumeUnits.CubicFootPerPound:
            return """ft³/lb"""
        
        if unit_abbreviation == SpecificVolumeUnits.MillicubicMeterPerKilogram:
            return """mm³/kg"""
        
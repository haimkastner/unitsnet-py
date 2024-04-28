from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class WarpingMomentOfInertiaUnits(Enum):
        """
            WarpingMomentOfInertiaUnits enumeration
        """
        
        MeterToTheSixth = 'MeterToTheSixth'
        """
            
        """
        
        DecimeterToTheSixth = 'DecimeterToTheSixth'
        """
            
        """
        
        CentimeterToTheSixth = 'CentimeterToTheSixth'
        """
            
        """
        
        MillimeterToTheSixth = 'MillimeterToTheSixth'
        """
            
        """
        
        FootToTheSixth = 'FootToTheSixth'
        """
            
        """
        
        InchToTheSixth = 'InchToTheSixth'
        """
            
        """
        

class WarpingMomentOfInertiaDto:
    """
    A DTO representation of a WarpingMomentOfInertia

    Attributes:
        value (float): The value of the WarpingMomentOfInertia.
        unit (WarpingMomentOfInertiaUnits): The specific unit that the WarpingMomentOfInertia value is representing.
    """

    def __init__(self, value: float, unit: WarpingMomentOfInertiaUnits):
        """
        Create a new DTO representation of a WarpingMomentOfInertia

        Parameters:
            value (float): The value of the WarpingMomentOfInertia.
            unit (WarpingMomentOfInertiaUnits): The specific unit that the WarpingMomentOfInertia value is representing.
        """
        self.value: float = value
        """
        The value of the WarpingMomentOfInertia
        """
        self.unit: WarpingMomentOfInertiaUnits = unit
        """
        The specific unit that the WarpingMomentOfInertia value is representing
        """

    def to_json(self):
        """
        Get a WarpingMomentOfInertia DTO JSON object representing the current unit.

        :return: JSON object represents WarpingMomentOfInertia DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "MeterToTheSixth"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of WarpingMomentOfInertia DTO from a json representation.

        :param data: The WarpingMomentOfInertia DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "MeterToTheSixth"}
        :return: A new instance of WarpingMomentOfInertiaDto.
        :rtype: WarpingMomentOfInertiaDto
        """
        return WarpingMomentOfInertiaDto(value=data["value"], unit=WarpingMomentOfInertiaUnits(data["unit"]))


class WarpingMomentOfInertia(AbstractMeasure):
    """
    A geometric property of an area that is used to determine the warping stress.

    Args:
        value (float): The value.
        from_unit (WarpingMomentOfInertiaUnits): The WarpingMomentOfInertia unit to create from, The default unit is MeterToTheSixth
    """
    def __init__(self, value: float, from_unit: WarpingMomentOfInertiaUnits = WarpingMomentOfInertiaUnits.MeterToTheSixth):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__meters_to_the_sixth = None
        
        self.__decimeters_to_the_sixth = None
        
        self.__centimeters_to_the_sixth = None
        
        self.__millimeters_to_the_sixth = None
        
        self.__feet_to_the_sixth = None
        
        self.__inches_to_the_sixth = None
        

    def convert(self, unit: WarpingMomentOfInertiaUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: WarpingMomentOfInertiaUnits = WarpingMomentOfInertiaUnits.MeterToTheSixth) -> WarpingMomentOfInertiaDto:
        """
        Get a new instance of WarpingMomentOfInertia DTO representing the current unit.

        :param hold_in_unit: The specific WarpingMomentOfInertia unit to store the WarpingMomentOfInertia value in the DTO representation.
        :type hold_in_unit: WarpingMomentOfInertiaUnits
        :return: A new instance of WarpingMomentOfInertiaDto.
        :rtype: WarpingMomentOfInertiaDto
        """
        return WarpingMomentOfInertiaDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: WarpingMomentOfInertiaUnits = WarpingMomentOfInertiaUnits.MeterToTheSixth):
        """
        Get a WarpingMomentOfInertia DTO JSON object representing the current unit.

        :param hold_in_unit: The specific WarpingMomentOfInertia unit to store the WarpingMomentOfInertia value in the DTO representation.
        :type hold_in_unit: WarpingMomentOfInertiaUnits
        :return: JSON object represents WarpingMomentOfInertia DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "MeterToTheSixth"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(warping_moment_of_inertia_dto: WarpingMomentOfInertiaDto):
        """
        Obtain a new instance of WarpingMomentOfInertia from a DTO unit object.

        :param warping_moment_of_inertia_dto: The WarpingMomentOfInertia DTO representation.
        :type warping_moment_of_inertia_dto: WarpingMomentOfInertiaDto
        :return: A new instance of WarpingMomentOfInertia.
        :rtype: WarpingMomentOfInertia
        """
        return WarpingMomentOfInertia(warping_moment_of_inertia_dto.value, warping_moment_of_inertia_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of WarpingMomentOfInertia from a DTO unit json representation.

        :param data: The WarpingMomentOfInertia DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "MeterToTheSixth"}
        :return: A new instance of WarpingMomentOfInertia.
        :rtype: WarpingMomentOfInertia
        """
        return WarpingMomentOfInertia.from_dto(WarpingMomentOfInertiaDto.from_json(data))

    def __convert_from_base(self, from_unit: WarpingMomentOfInertiaUnits) -> float:
        value = self._value
        
        if from_unit == WarpingMomentOfInertiaUnits.MeterToTheSixth:
            return (value)
        
        if from_unit == WarpingMomentOfInertiaUnits.DecimeterToTheSixth:
            return (value * 1e6)
        
        if from_unit == WarpingMomentOfInertiaUnits.CentimeterToTheSixth:
            return (value * 1e12)
        
        if from_unit == WarpingMomentOfInertiaUnits.MillimeterToTheSixth:
            return (value * 1e18)
        
        if from_unit == WarpingMomentOfInertiaUnits.FootToTheSixth:
            return (value / math.pow(0.3048, 6))
        
        if from_unit == WarpingMomentOfInertiaUnits.InchToTheSixth:
            return (value / math.pow(2.54e-2, 6))
        
        return None


    def __convert_to_base(self, value: float, to_unit: WarpingMomentOfInertiaUnits) -> float:
        
        if to_unit == WarpingMomentOfInertiaUnits.MeterToTheSixth:
            return (value)
        
        if to_unit == WarpingMomentOfInertiaUnits.DecimeterToTheSixth:
            return (value / 1e6)
        
        if to_unit == WarpingMomentOfInertiaUnits.CentimeterToTheSixth:
            return (value / 1e12)
        
        if to_unit == WarpingMomentOfInertiaUnits.MillimeterToTheSixth:
            return (value / 1e18)
        
        if to_unit == WarpingMomentOfInertiaUnits.FootToTheSixth:
            return (value * math.pow(0.3048, 6))
        
        if to_unit == WarpingMomentOfInertiaUnits.InchToTheSixth:
            return (value * math.pow(2.54e-2, 6))
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_meters_to_the_sixth(meters_to_the_sixth: float):
        """
        Create a new instance of WarpingMomentOfInertia from a value in meters_to_the_sixth.

        

        :param meters: The WarpingMomentOfInertia value in meters_to_the_sixth.
        :type meters_to_the_sixth: float
        :return: A new instance of WarpingMomentOfInertia.
        :rtype: WarpingMomentOfInertia
        """
        return WarpingMomentOfInertia(meters_to_the_sixth, WarpingMomentOfInertiaUnits.MeterToTheSixth)

    
    @staticmethod
    def from_decimeters_to_the_sixth(decimeters_to_the_sixth: float):
        """
        Create a new instance of WarpingMomentOfInertia from a value in decimeters_to_the_sixth.

        

        :param meters: The WarpingMomentOfInertia value in decimeters_to_the_sixth.
        :type decimeters_to_the_sixth: float
        :return: A new instance of WarpingMomentOfInertia.
        :rtype: WarpingMomentOfInertia
        """
        return WarpingMomentOfInertia(decimeters_to_the_sixth, WarpingMomentOfInertiaUnits.DecimeterToTheSixth)

    
    @staticmethod
    def from_centimeters_to_the_sixth(centimeters_to_the_sixth: float):
        """
        Create a new instance of WarpingMomentOfInertia from a value in centimeters_to_the_sixth.

        

        :param meters: The WarpingMomentOfInertia value in centimeters_to_the_sixth.
        :type centimeters_to_the_sixth: float
        :return: A new instance of WarpingMomentOfInertia.
        :rtype: WarpingMomentOfInertia
        """
        return WarpingMomentOfInertia(centimeters_to_the_sixth, WarpingMomentOfInertiaUnits.CentimeterToTheSixth)

    
    @staticmethod
    def from_millimeters_to_the_sixth(millimeters_to_the_sixth: float):
        """
        Create a new instance of WarpingMomentOfInertia from a value in millimeters_to_the_sixth.

        

        :param meters: The WarpingMomentOfInertia value in millimeters_to_the_sixth.
        :type millimeters_to_the_sixth: float
        :return: A new instance of WarpingMomentOfInertia.
        :rtype: WarpingMomentOfInertia
        """
        return WarpingMomentOfInertia(millimeters_to_the_sixth, WarpingMomentOfInertiaUnits.MillimeterToTheSixth)

    
    @staticmethod
    def from_feet_to_the_sixth(feet_to_the_sixth: float):
        """
        Create a new instance of WarpingMomentOfInertia from a value in feet_to_the_sixth.

        

        :param meters: The WarpingMomentOfInertia value in feet_to_the_sixth.
        :type feet_to_the_sixth: float
        :return: A new instance of WarpingMomentOfInertia.
        :rtype: WarpingMomentOfInertia
        """
        return WarpingMomentOfInertia(feet_to_the_sixth, WarpingMomentOfInertiaUnits.FootToTheSixth)

    
    @staticmethod
    def from_inches_to_the_sixth(inches_to_the_sixth: float):
        """
        Create a new instance of WarpingMomentOfInertia from a value in inches_to_the_sixth.

        

        :param meters: The WarpingMomentOfInertia value in inches_to_the_sixth.
        :type inches_to_the_sixth: float
        :return: A new instance of WarpingMomentOfInertia.
        :rtype: WarpingMomentOfInertia
        """
        return WarpingMomentOfInertia(inches_to_the_sixth, WarpingMomentOfInertiaUnits.InchToTheSixth)

    
    @property
    def meters_to_the_sixth(self) -> float:
        """
        
        """
        if self.__meters_to_the_sixth != None:
            return self.__meters_to_the_sixth
        self.__meters_to_the_sixth = self.__convert_from_base(WarpingMomentOfInertiaUnits.MeterToTheSixth)
        return self.__meters_to_the_sixth

    
    @property
    def decimeters_to_the_sixth(self) -> float:
        """
        
        """
        if self.__decimeters_to_the_sixth != None:
            return self.__decimeters_to_the_sixth
        self.__decimeters_to_the_sixth = self.__convert_from_base(WarpingMomentOfInertiaUnits.DecimeterToTheSixth)
        return self.__decimeters_to_the_sixth

    
    @property
    def centimeters_to_the_sixth(self) -> float:
        """
        
        """
        if self.__centimeters_to_the_sixth != None:
            return self.__centimeters_to_the_sixth
        self.__centimeters_to_the_sixth = self.__convert_from_base(WarpingMomentOfInertiaUnits.CentimeterToTheSixth)
        return self.__centimeters_to_the_sixth

    
    @property
    def millimeters_to_the_sixth(self) -> float:
        """
        
        """
        if self.__millimeters_to_the_sixth != None:
            return self.__millimeters_to_the_sixth
        self.__millimeters_to_the_sixth = self.__convert_from_base(WarpingMomentOfInertiaUnits.MillimeterToTheSixth)
        return self.__millimeters_to_the_sixth

    
    @property
    def feet_to_the_sixth(self) -> float:
        """
        
        """
        if self.__feet_to_the_sixth != None:
            return self.__feet_to_the_sixth
        self.__feet_to_the_sixth = self.__convert_from_base(WarpingMomentOfInertiaUnits.FootToTheSixth)
        return self.__feet_to_the_sixth

    
    @property
    def inches_to_the_sixth(self) -> float:
        """
        
        """
        if self.__inches_to_the_sixth != None:
            return self.__inches_to_the_sixth
        self.__inches_to_the_sixth = self.__convert_from_base(WarpingMomentOfInertiaUnits.InchToTheSixth)
        return self.__inches_to_the_sixth

    
    def to_string(self, unit: WarpingMomentOfInertiaUnits = WarpingMomentOfInertiaUnits.MeterToTheSixth, fractional_digits: int = None) -> str:
        """
        Format the WarpingMomentOfInertia to a string.
        
        Note: the default format for WarpingMomentOfInertia is MeterToTheSixth.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the WarpingMomentOfInertia. Default is 'MeterToTheSixth'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == WarpingMomentOfInertiaUnits.MeterToTheSixth:
            return f"""{super()._truncate_fraction_digits(self.meters_to_the_sixth, fractional_digits)} m⁶"""
        
        if unit == WarpingMomentOfInertiaUnits.DecimeterToTheSixth:
            return f"""{super()._truncate_fraction_digits(self.decimeters_to_the_sixth, fractional_digits)} dm⁶"""
        
        if unit == WarpingMomentOfInertiaUnits.CentimeterToTheSixth:
            return f"""{super()._truncate_fraction_digits(self.centimeters_to_the_sixth, fractional_digits)} cm⁶"""
        
        if unit == WarpingMomentOfInertiaUnits.MillimeterToTheSixth:
            return f"""{super()._truncate_fraction_digits(self.millimeters_to_the_sixth, fractional_digits)} mm⁶"""
        
        if unit == WarpingMomentOfInertiaUnits.FootToTheSixth:
            return f"""{super()._truncate_fraction_digits(self.feet_to_the_sixth, fractional_digits)} ft⁶"""
        
        if unit == WarpingMomentOfInertiaUnits.InchToTheSixth:
            return f"""{super()._truncate_fraction_digits(self.inches_to_the_sixth, fractional_digits)} in⁶"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: WarpingMomentOfInertiaUnits = WarpingMomentOfInertiaUnits.MeterToTheSixth) -> str:
        """
        Get WarpingMomentOfInertia unit abbreviation.
        Note! the default abbreviation for WarpingMomentOfInertia is MeterToTheSixth.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == WarpingMomentOfInertiaUnits.MeterToTheSixth:
            return """m⁶"""
        
        if unit_abbreviation == WarpingMomentOfInertiaUnits.DecimeterToTheSixth:
            return """dm⁶"""
        
        if unit_abbreviation == WarpingMomentOfInertiaUnits.CentimeterToTheSixth:
            return """cm⁶"""
        
        if unit_abbreviation == WarpingMomentOfInertiaUnits.MillimeterToTheSixth:
            return """mm⁶"""
        
        if unit_abbreviation == WarpingMomentOfInertiaUnits.FootToTheSixth:
            return """ft⁶"""
        
        if unit_abbreviation == WarpingMomentOfInertiaUnits.InchToTheSixth:
            return """in⁶"""
        
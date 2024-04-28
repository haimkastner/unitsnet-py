from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class JerkUnits(Enum):
        """
            JerkUnits enumeration
        """
        
        MeterPerSecondCubed = 'MeterPerSecondCubed'
        """
            
        """
        
        InchPerSecondCubed = 'InchPerSecondCubed'
        """
            
        """
        
        FootPerSecondCubed = 'FootPerSecondCubed'
        """
            
        """
        
        StandardGravitiesPerSecond = 'StandardGravitiesPerSecond'
        """
            
        """
        
        NanometerPerSecondCubed = 'NanometerPerSecondCubed'
        """
            
        """
        
        MicrometerPerSecondCubed = 'MicrometerPerSecondCubed'
        """
            
        """
        
        MillimeterPerSecondCubed = 'MillimeterPerSecondCubed'
        """
            
        """
        
        CentimeterPerSecondCubed = 'CentimeterPerSecondCubed'
        """
            
        """
        
        DecimeterPerSecondCubed = 'DecimeterPerSecondCubed'
        """
            
        """
        
        KilometerPerSecondCubed = 'KilometerPerSecondCubed'
        """
            
        """
        
        MillistandardGravitiesPerSecond = 'MillistandardGravitiesPerSecond'
        """
            
        """
        

class JerkDto:
    """
    A DTO representation of a Jerk

    Attributes:
        value (float): The value of the Jerk.
        unit (JerkUnits): The specific unit that the Jerk value is representing.
    """

    def __init__(self, value: float, unit: JerkUnits):
        """
        Create a new DTO representation of a Jerk

        Parameters:
            value (float): The value of the Jerk.
            unit (JerkUnits): The specific unit that the Jerk value is representing.
        """
        self.value: float = value
        """
        The value of the Jerk
        """
        self.unit: JerkUnits = unit
        """
        The specific unit that the Jerk value is representing
        """

    def to_json(self):
        """
        Get a Jerk DTO JSON object representing the current unit.

        :return: JSON object represents Jerk DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "MeterPerSecondCubed"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of Jerk DTO from a json representation.

        :param data: The Jerk DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "MeterPerSecondCubed"}
        :return: A new instance of JerkDto.
        :rtype: JerkDto
        """
        return JerkDto(value=data["value"], unit=JerkUnits(data["unit"]))


class Jerk(AbstractMeasure):
    """
    None

    Args:
        value (float): The value.
        from_unit (JerkUnits): The Jerk unit to create from, The default unit is MeterPerSecondCubed
    """
    def __init__(self, value: float, from_unit: JerkUnits = JerkUnits.MeterPerSecondCubed):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__meters_per_second_cubed = None
        
        self.__inches_per_second_cubed = None
        
        self.__feet_per_second_cubed = None
        
        self.__standard_gravities_per_second = None
        
        self.__nanometers_per_second_cubed = None
        
        self.__micrometers_per_second_cubed = None
        
        self.__millimeters_per_second_cubed = None
        
        self.__centimeters_per_second_cubed = None
        
        self.__decimeters_per_second_cubed = None
        
        self.__kilometers_per_second_cubed = None
        
        self.__millistandard_gravities_per_second = None
        

    def convert(self, unit: JerkUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: JerkUnits = JerkUnits.MeterPerSecondCubed) -> JerkDto:
        """
        Get a new instance of Jerk DTO representing the current unit.

        :param hold_in_unit: The specific Jerk unit to store the Jerk value in the DTO representation.
        :type hold_in_unit: JerkUnits
        :return: A new instance of JerkDto.
        :rtype: JerkDto
        """
        return JerkDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: JerkUnits = JerkUnits.MeterPerSecondCubed):
        """
        Get a Jerk DTO JSON object representing the current unit.

        :param hold_in_unit: The specific Jerk unit to store the Jerk value in the DTO representation.
        :type hold_in_unit: JerkUnits
        :return: JSON object represents Jerk DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "MeterPerSecondCubed"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(jerk_dto: JerkDto):
        """
        Obtain a new instance of Jerk from a DTO unit object.

        :param jerk_dto: The Jerk DTO representation.
        :type jerk_dto: JerkDto
        :return: A new instance of Jerk.
        :rtype: Jerk
        """
        return Jerk(jerk_dto.value, jerk_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of Jerk from a DTO unit json representation.

        :param data: The Jerk DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "MeterPerSecondCubed"}
        :return: A new instance of Jerk.
        :rtype: Jerk
        """
        return Jerk.from_dto(JerkDto.from_json(data))

    def __convert_from_base(self, from_unit: JerkUnits) -> float:
        value = self._value
        
        if from_unit == JerkUnits.MeterPerSecondCubed:
            return (value)
        
        if from_unit == JerkUnits.InchPerSecondCubed:
            return (value / 0.0254)
        
        if from_unit == JerkUnits.FootPerSecondCubed:
            return (value / 0.304800)
        
        if from_unit == JerkUnits.StandardGravitiesPerSecond:
            return (value / 9.80665)
        
        if from_unit == JerkUnits.NanometerPerSecondCubed:
            return ((value) / 1e-09)
        
        if from_unit == JerkUnits.MicrometerPerSecondCubed:
            return ((value) / 1e-06)
        
        if from_unit == JerkUnits.MillimeterPerSecondCubed:
            return ((value) / 0.001)
        
        if from_unit == JerkUnits.CentimeterPerSecondCubed:
            return ((value) / 0.01)
        
        if from_unit == JerkUnits.DecimeterPerSecondCubed:
            return ((value) / 0.1)
        
        if from_unit == JerkUnits.KilometerPerSecondCubed:
            return ((value) / 1000.0)
        
        if from_unit == JerkUnits.MillistandardGravitiesPerSecond:
            return ((value / 9.80665) / 0.001)
        
        return None


    def __convert_to_base(self, value: float, to_unit: JerkUnits) -> float:
        
        if to_unit == JerkUnits.MeterPerSecondCubed:
            return (value)
        
        if to_unit == JerkUnits.InchPerSecondCubed:
            return (value * 0.0254)
        
        if to_unit == JerkUnits.FootPerSecondCubed:
            return (value * 0.304800)
        
        if to_unit == JerkUnits.StandardGravitiesPerSecond:
            return (value * 9.80665)
        
        if to_unit == JerkUnits.NanometerPerSecondCubed:
            return ((value) * 1e-09)
        
        if to_unit == JerkUnits.MicrometerPerSecondCubed:
            return ((value) * 1e-06)
        
        if to_unit == JerkUnits.MillimeterPerSecondCubed:
            return ((value) * 0.001)
        
        if to_unit == JerkUnits.CentimeterPerSecondCubed:
            return ((value) * 0.01)
        
        if to_unit == JerkUnits.DecimeterPerSecondCubed:
            return ((value) * 0.1)
        
        if to_unit == JerkUnits.KilometerPerSecondCubed:
            return ((value) * 1000.0)
        
        if to_unit == JerkUnits.MillistandardGravitiesPerSecond:
            return ((value * 9.80665) * 0.001)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_meters_per_second_cubed(meters_per_second_cubed: float):
        """
        Create a new instance of Jerk from a value in meters_per_second_cubed.

        

        :param meters: The Jerk value in meters_per_second_cubed.
        :type meters_per_second_cubed: float
        :return: A new instance of Jerk.
        :rtype: Jerk
        """
        return Jerk(meters_per_second_cubed, JerkUnits.MeterPerSecondCubed)

    
    @staticmethod
    def from_inches_per_second_cubed(inches_per_second_cubed: float):
        """
        Create a new instance of Jerk from a value in inches_per_second_cubed.

        

        :param meters: The Jerk value in inches_per_second_cubed.
        :type inches_per_second_cubed: float
        :return: A new instance of Jerk.
        :rtype: Jerk
        """
        return Jerk(inches_per_second_cubed, JerkUnits.InchPerSecondCubed)

    
    @staticmethod
    def from_feet_per_second_cubed(feet_per_second_cubed: float):
        """
        Create a new instance of Jerk from a value in feet_per_second_cubed.

        

        :param meters: The Jerk value in feet_per_second_cubed.
        :type feet_per_second_cubed: float
        :return: A new instance of Jerk.
        :rtype: Jerk
        """
        return Jerk(feet_per_second_cubed, JerkUnits.FootPerSecondCubed)

    
    @staticmethod
    def from_standard_gravities_per_second(standard_gravities_per_second: float):
        """
        Create a new instance of Jerk from a value in standard_gravities_per_second.

        

        :param meters: The Jerk value in standard_gravities_per_second.
        :type standard_gravities_per_second: float
        :return: A new instance of Jerk.
        :rtype: Jerk
        """
        return Jerk(standard_gravities_per_second, JerkUnits.StandardGravitiesPerSecond)

    
    @staticmethod
    def from_nanometers_per_second_cubed(nanometers_per_second_cubed: float):
        """
        Create a new instance of Jerk from a value in nanometers_per_second_cubed.

        

        :param meters: The Jerk value in nanometers_per_second_cubed.
        :type nanometers_per_second_cubed: float
        :return: A new instance of Jerk.
        :rtype: Jerk
        """
        return Jerk(nanometers_per_second_cubed, JerkUnits.NanometerPerSecondCubed)

    
    @staticmethod
    def from_micrometers_per_second_cubed(micrometers_per_second_cubed: float):
        """
        Create a new instance of Jerk from a value in micrometers_per_second_cubed.

        

        :param meters: The Jerk value in micrometers_per_second_cubed.
        :type micrometers_per_second_cubed: float
        :return: A new instance of Jerk.
        :rtype: Jerk
        """
        return Jerk(micrometers_per_second_cubed, JerkUnits.MicrometerPerSecondCubed)

    
    @staticmethod
    def from_millimeters_per_second_cubed(millimeters_per_second_cubed: float):
        """
        Create a new instance of Jerk from a value in millimeters_per_second_cubed.

        

        :param meters: The Jerk value in millimeters_per_second_cubed.
        :type millimeters_per_second_cubed: float
        :return: A new instance of Jerk.
        :rtype: Jerk
        """
        return Jerk(millimeters_per_second_cubed, JerkUnits.MillimeterPerSecondCubed)

    
    @staticmethod
    def from_centimeters_per_second_cubed(centimeters_per_second_cubed: float):
        """
        Create a new instance of Jerk from a value in centimeters_per_second_cubed.

        

        :param meters: The Jerk value in centimeters_per_second_cubed.
        :type centimeters_per_second_cubed: float
        :return: A new instance of Jerk.
        :rtype: Jerk
        """
        return Jerk(centimeters_per_second_cubed, JerkUnits.CentimeterPerSecondCubed)

    
    @staticmethod
    def from_decimeters_per_second_cubed(decimeters_per_second_cubed: float):
        """
        Create a new instance of Jerk from a value in decimeters_per_second_cubed.

        

        :param meters: The Jerk value in decimeters_per_second_cubed.
        :type decimeters_per_second_cubed: float
        :return: A new instance of Jerk.
        :rtype: Jerk
        """
        return Jerk(decimeters_per_second_cubed, JerkUnits.DecimeterPerSecondCubed)

    
    @staticmethod
    def from_kilometers_per_second_cubed(kilometers_per_second_cubed: float):
        """
        Create a new instance of Jerk from a value in kilometers_per_second_cubed.

        

        :param meters: The Jerk value in kilometers_per_second_cubed.
        :type kilometers_per_second_cubed: float
        :return: A new instance of Jerk.
        :rtype: Jerk
        """
        return Jerk(kilometers_per_second_cubed, JerkUnits.KilometerPerSecondCubed)

    
    @staticmethod
    def from_millistandard_gravities_per_second(millistandard_gravities_per_second: float):
        """
        Create a new instance of Jerk from a value in millistandard_gravities_per_second.

        

        :param meters: The Jerk value in millistandard_gravities_per_second.
        :type millistandard_gravities_per_second: float
        :return: A new instance of Jerk.
        :rtype: Jerk
        """
        return Jerk(millistandard_gravities_per_second, JerkUnits.MillistandardGravitiesPerSecond)

    
    @property
    def meters_per_second_cubed(self) -> float:
        """
        
        """
        if self.__meters_per_second_cubed != None:
            return self.__meters_per_second_cubed
        self.__meters_per_second_cubed = self.__convert_from_base(JerkUnits.MeterPerSecondCubed)
        return self.__meters_per_second_cubed

    
    @property
    def inches_per_second_cubed(self) -> float:
        """
        
        """
        if self.__inches_per_second_cubed != None:
            return self.__inches_per_second_cubed
        self.__inches_per_second_cubed = self.__convert_from_base(JerkUnits.InchPerSecondCubed)
        return self.__inches_per_second_cubed

    
    @property
    def feet_per_second_cubed(self) -> float:
        """
        
        """
        if self.__feet_per_second_cubed != None:
            return self.__feet_per_second_cubed
        self.__feet_per_second_cubed = self.__convert_from_base(JerkUnits.FootPerSecondCubed)
        return self.__feet_per_second_cubed

    
    @property
    def standard_gravities_per_second(self) -> float:
        """
        
        """
        if self.__standard_gravities_per_second != None:
            return self.__standard_gravities_per_second
        self.__standard_gravities_per_second = self.__convert_from_base(JerkUnits.StandardGravitiesPerSecond)
        return self.__standard_gravities_per_second

    
    @property
    def nanometers_per_second_cubed(self) -> float:
        """
        
        """
        if self.__nanometers_per_second_cubed != None:
            return self.__nanometers_per_second_cubed
        self.__nanometers_per_second_cubed = self.__convert_from_base(JerkUnits.NanometerPerSecondCubed)
        return self.__nanometers_per_second_cubed

    
    @property
    def micrometers_per_second_cubed(self) -> float:
        """
        
        """
        if self.__micrometers_per_second_cubed != None:
            return self.__micrometers_per_second_cubed
        self.__micrometers_per_second_cubed = self.__convert_from_base(JerkUnits.MicrometerPerSecondCubed)
        return self.__micrometers_per_second_cubed

    
    @property
    def millimeters_per_second_cubed(self) -> float:
        """
        
        """
        if self.__millimeters_per_second_cubed != None:
            return self.__millimeters_per_second_cubed
        self.__millimeters_per_second_cubed = self.__convert_from_base(JerkUnits.MillimeterPerSecondCubed)
        return self.__millimeters_per_second_cubed

    
    @property
    def centimeters_per_second_cubed(self) -> float:
        """
        
        """
        if self.__centimeters_per_second_cubed != None:
            return self.__centimeters_per_second_cubed
        self.__centimeters_per_second_cubed = self.__convert_from_base(JerkUnits.CentimeterPerSecondCubed)
        return self.__centimeters_per_second_cubed

    
    @property
    def decimeters_per_second_cubed(self) -> float:
        """
        
        """
        if self.__decimeters_per_second_cubed != None:
            return self.__decimeters_per_second_cubed
        self.__decimeters_per_second_cubed = self.__convert_from_base(JerkUnits.DecimeterPerSecondCubed)
        return self.__decimeters_per_second_cubed

    
    @property
    def kilometers_per_second_cubed(self) -> float:
        """
        
        """
        if self.__kilometers_per_second_cubed != None:
            return self.__kilometers_per_second_cubed
        self.__kilometers_per_second_cubed = self.__convert_from_base(JerkUnits.KilometerPerSecondCubed)
        return self.__kilometers_per_second_cubed

    
    @property
    def millistandard_gravities_per_second(self) -> float:
        """
        
        """
        if self.__millistandard_gravities_per_second != None:
            return self.__millistandard_gravities_per_second
        self.__millistandard_gravities_per_second = self.__convert_from_base(JerkUnits.MillistandardGravitiesPerSecond)
        return self.__millistandard_gravities_per_second

    
    def to_string(self, unit: JerkUnits = JerkUnits.MeterPerSecondCubed, fractional_digits: int = None) -> str:
        """
        Format the Jerk to a string.
        
        Note: the default format for Jerk is MeterPerSecondCubed.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the Jerk. Default is 'MeterPerSecondCubed'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == JerkUnits.MeterPerSecondCubed:
            return f"""{super()._truncate_fraction_digits(self.meters_per_second_cubed, fractional_digits)} m/s³"""
        
        if unit == JerkUnits.InchPerSecondCubed:
            return f"""{super()._truncate_fraction_digits(self.inches_per_second_cubed, fractional_digits)} in/s³"""
        
        if unit == JerkUnits.FootPerSecondCubed:
            return f"""{super()._truncate_fraction_digits(self.feet_per_second_cubed, fractional_digits)} ft/s³"""
        
        if unit == JerkUnits.StandardGravitiesPerSecond:
            return f"""{super()._truncate_fraction_digits(self.standard_gravities_per_second, fractional_digits)} g/s"""
        
        if unit == JerkUnits.NanometerPerSecondCubed:
            return f"""{super()._truncate_fraction_digits(self.nanometers_per_second_cubed, fractional_digits)} nm/s³"""
        
        if unit == JerkUnits.MicrometerPerSecondCubed:
            return f"""{super()._truncate_fraction_digits(self.micrometers_per_second_cubed, fractional_digits)} μm/s³"""
        
        if unit == JerkUnits.MillimeterPerSecondCubed:
            return f"""{super()._truncate_fraction_digits(self.millimeters_per_second_cubed, fractional_digits)} mm/s³"""
        
        if unit == JerkUnits.CentimeterPerSecondCubed:
            return f"""{super()._truncate_fraction_digits(self.centimeters_per_second_cubed, fractional_digits)} cm/s³"""
        
        if unit == JerkUnits.DecimeterPerSecondCubed:
            return f"""{super()._truncate_fraction_digits(self.decimeters_per_second_cubed, fractional_digits)} dm/s³"""
        
        if unit == JerkUnits.KilometerPerSecondCubed:
            return f"""{super()._truncate_fraction_digits(self.kilometers_per_second_cubed, fractional_digits)} km/s³"""
        
        if unit == JerkUnits.MillistandardGravitiesPerSecond:
            return f"""{super()._truncate_fraction_digits(self.millistandard_gravities_per_second, fractional_digits)} mg/s"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: JerkUnits = JerkUnits.MeterPerSecondCubed) -> str:
        """
        Get Jerk unit abbreviation.
        Note! the default abbreviation for Jerk is MeterPerSecondCubed.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == JerkUnits.MeterPerSecondCubed:
            return """m/s³"""
        
        if unit_abbreviation == JerkUnits.InchPerSecondCubed:
            return """in/s³"""
        
        if unit_abbreviation == JerkUnits.FootPerSecondCubed:
            return """ft/s³"""
        
        if unit_abbreviation == JerkUnits.StandardGravitiesPerSecond:
            return """g/s"""
        
        if unit_abbreviation == JerkUnits.NanometerPerSecondCubed:
            return """nm/s³"""
        
        if unit_abbreviation == JerkUnits.MicrometerPerSecondCubed:
            return """μm/s³"""
        
        if unit_abbreviation == JerkUnits.MillimeterPerSecondCubed:
            return """mm/s³"""
        
        if unit_abbreviation == JerkUnits.CentimeterPerSecondCubed:
            return """cm/s³"""
        
        if unit_abbreviation == JerkUnits.DecimeterPerSecondCubed:
            return """dm/s³"""
        
        if unit_abbreviation == JerkUnits.KilometerPerSecondCubed:
            return """km/s³"""
        
        if unit_abbreviation == JerkUnits.MillistandardGravitiesPerSecond:
            return """mg/s"""
        
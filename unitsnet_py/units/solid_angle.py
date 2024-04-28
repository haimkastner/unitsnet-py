from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class SolidAngleUnits(Enum):
        """
            SolidAngleUnits enumeration
        """
        
        Steradian = 'Steradian'
        """
            
        """
        

class SolidAngleDto:
    """
    A DTO representation of a SolidAngle

    Attributes:
        value (float): The value of the SolidAngle.
        unit (SolidAngleUnits): The specific unit that the SolidAngle value is representing.
    """

    def __init__(self, value: float, unit: SolidAngleUnits):
        """
        Create a new DTO representation of a SolidAngle

        Parameters:
            value (float): The value of the SolidAngle.
            unit (SolidAngleUnits): The specific unit that the SolidAngle value is representing.
        """
        self.value: float = value
        """
        The value of the SolidAngle
        """
        self.unit: SolidAngleUnits = unit
        """
        The specific unit that the SolidAngle value is representing
        """

    def to_json(self):
        """
        Get a SolidAngle DTO JSON object representing the current unit.

        :return: JSON object represents SolidAngle DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "Steradian"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of SolidAngle DTO from a json representation.

        :param data: The SolidAngle DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "Steradian"}
        :return: A new instance of SolidAngleDto.
        :rtype: SolidAngleDto
        """
        return SolidAngleDto(value=data["value"], unit=SolidAngleUnits(data["unit"]))


class SolidAngle(AbstractMeasure):
    """
    In geometry, a solid angle is the two-dimensional angle in three-dimensional space that an object subtends at a point.

    Args:
        value (float): The value.
        from_unit (SolidAngleUnits): The SolidAngle unit to create from, The default unit is Steradian
    """
    def __init__(self, value: float, from_unit: SolidAngleUnits = SolidAngleUnits.Steradian):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__steradians = None
        

    def convert(self, unit: SolidAngleUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: SolidAngleUnits = SolidAngleUnits.Steradian) -> SolidAngleDto:
        """
        Get a new instance of SolidAngle DTO representing the current unit.

        :param hold_in_unit: The specific SolidAngle unit to store the SolidAngle value in the DTO representation.
        :type hold_in_unit: SolidAngleUnits
        :return: A new instance of SolidAngleDto.
        :rtype: SolidAngleDto
        """
        return SolidAngleDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: SolidAngleUnits = SolidAngleUnits.Steradian):
        """
        Get a SolidAngle DTO JSON object representing the current unit.

        :param hold_in_unit: The specific SolidAngle unit to store the SolidAngle value in the DTO representation.
        :type hold_in_unit: SolidAngleUnits
        :return: JSON object represents SolidAngle DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "Steradian"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(solid_angle_dto: SolidAngleDto):
        """
        Obtain a new instance of SolidAngle from a DTO unit object.

        :param solid_angle_dto: The SolidAngle DTO representation.
        :type solid_angle_dto: SolidAngleDto
        :return: A new instance of SolidAngle.
        :rtype: SolidAngle
        """
        return SolidAngle(solid_angle_dto.value, solid_angle_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of SolidAngle from a DTO unit json representation.

        :param data: The SolidAngle DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "Steradian"}
        :return: A new instance of SolidAngle.
        :rtype: SolidAngle
        """
        return SolidAngle.from_dto(SolidAngleDto.from_json(data))

    def __convert_from_base(self, from_unit: SolidAngleUnits) -> float:
        value = self._value
        
        if from_unit == SolidAngleUnits.Steradian:
            return (value)
        
        return None


    def __convert_to_base(self, value: float, to_unit: SolidAngleUnits) -> float:
        
        if to_unit == SolidAngleUnits.Steradian:
            return (value)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_steradians(steradians: float):
        """
        Create a new instance of SolidAngle from a value in steradians.

        

        :param meters: The SolidAngle value in steradians.
        :type steradians: float
        :return: A new instance of SolidAngle.
        :rtype: SolidAngle
        """
        return SolidAngle(steradians, SolidAngleUnits.Steradian)

    
    @property
    def steradians(self) -> float:
        """
        
        """
        if self.__steradians != None:
            return self.__steradians
        self.__steradians = self.__convert_from_base(SolidAngleUnits.Steradian)
        return self.__steradians

    
    def to_string(self, unit: SolidAngleUnits = SolidAngleUnits.Steradian, fractional_digits: int = None) -> str:
        """
        Format the SolidAngle to a string.
        
        Note: the default format for SolidAngle is Steradian.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the SolidAngle. Default is 'Steradian'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == SolidAngleUnits.Steradian:
            return f"""{super()._truncate_fraction_digits(self.steradians, fractional_digits)} sr"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: SolidAngleUnits = SolidAngleUnits.Steradian) -> str:
        """
        Get SolidAngle unit abbreviation.
        Note! the default abbreviation for SolidAngle is Steradian.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == SolidAngleUnits.Steradian:
            return """sr"""
        
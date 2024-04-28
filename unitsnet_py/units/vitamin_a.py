from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class VitaminAUnits(Enum):
        """
            VitaminAUnits enumeration
        """
        
        InternationalUnit = 'InternationalUnit'
        """
            
        """
        

class VitaminADto:
    """
    A DTO representation of a VitaminA

    Attributes:
        value (float): The value of the VitaminA.
        unit (VitaminAUnits): The specific unit that the VitaminA value is representing.
    """

    def __init__(self, value: float, unit: VitaminAUnits):
        """
        Create a new DTO representation of a VitaminA

        Parameters:
            value (float): The value of the VitaminA.
            unit (VitaminAUnits): The specific unit that the VitaminA value is representing.
        """
        self.value: float = value
        """
        The value of the VitaminA
        """
        self.unit: VitaminAUnits = unit
        """
        The specific unit that the VitaminA value is representing
        """

    def to_json(self):
        """
        Get a VitaminA DTO JSON object representing the current unit.

        :return: JSON object represents VitaminA DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "InternationalUnit"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of VitaminA DTO from a json representation.

        :param data: The VitaminA DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "InternationalUnit"}
        :return: A new instance of VitaminADto.
        :rtype: VitaminADto
        """
        return VitaminADto(value=data["value"], unit=VitaminAUnits(data["unit"]))


class VitaminA(AbstractMeasure):
    """
    Vitamin A: 1 IU is the biological equivalent of 0.3 µg retinol, or of 0.6 µg beta-carotene.

    Args:
        value (float): The value.
        from_unit (VitaminAUnits): The VitaminA unit to create from, The default unit is InternationalUnit
    """
    def __init__(self, value: float, from_unit: VitaminAUnits = VitaminAUnits.InternationalUnit):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__international_units = None
        

    def convert(self, unit: VitaminAUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: VitaminAUnits = VitaminAUnits.InternationalUnit) -> VitaminADto:
        """
        Get a new instance of VitaminA DTO representing the current unit.

        :param hold_in_unit: The specific VitaminA unit to store the VitaminA value in the DTO representation.
        :type hold_in_unit: VitaminAUnits
        :return: A new instance of VitaminADto.
        :rtype: VitaminADto
        """
        return VitaminADto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: VitaminAUnits = VitaminAUnits.InternationalUnit):
        """
        Get a VitaminA DTO JSON object representing the current unit.

        :param hold_in_unit: The specific VitaminA unit to store the VitaminA value in the DTO representation.
        :type hold_in_unit: VitaminAUnits
        :return: JSON object represents VitaminA DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "InternationalUnit"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(vitamin_a_dto: VitaminADto):
        """
        Obtain a new instance of VitaminA from a DTO unit object.

        :param vitamin_a_dto: The VitaminA DTO representation.
        :type vitamin_a_dto: VitaminADto
        :return: A new instance of VitaminA.
        :rtype: VitaminA
        """
        return VitaminA(vitamin_a_dto.value, vitamin_a_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of VitaminA from a DTO unit json representation.

        :param data: The VitaminA DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "InternationalUnit"}
        :return: A new instance of VitaminA.
        :rtype: VitaminA
        """
        return VitaminA.from_dto(VitaminADto.from_json(data))

    def __convert_from_base(self, from_unit: VitaminAUnits) -> float:
        value = self._value
        
        if from_unit == VitaminAUnits.InternationalUnit:
            return (value)
        
        return None


    def __convert_to_base(self, value: float, to_unit: VitaminAUnits) -> float:
        
        if to_unit == VitaminAUnits.InternationalUnit:
            return (value)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_international_units(international_units: float):
        """
        Create a new instance of VitaminA from a value in international_units.

        

        :param meters: The VitaminA value in international_units.
        :type international_units: float
        :return: A new instance of VitaminA.
        :rtype: VitaminA
        """
        return VitaminA(international_units, VitaminAUnits.InternationalUnit)

    
    @property
    def international_units(self) -> float:
        """
        
        """
        if self.__international_units != None:
            return self.__international_units
        self.__international_units = self.__convert_from_base(VitaminAUnits.InternationalUnit)
        return self.__international_units

    
    def to_string(self, unit: VitaminAUnits = VitaminAUnits.InternationalUnit, fractional_digits: int = None) -> str:
        """
        Format the VitaminA to a string.
        
        Note: the default format for VitaminA is InternationalUnit.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the VitaminA. Default is 'InternationalUnit'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == VitaminAUnits.InternationalUnit:
            return f"""{super()._truncate_fraction_digits(self.international_units, fractional_digits)} IU"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: VitaminAUnits = VitaminAUnits.InternationalUnit) -> str:
        """
        Get VitaminA unit abbreviation.
        Note! the default abbreviation for VitaminA is InternationalUnit.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == VitaminAUnits.InternationalUnit:
            return """IU"""
        
from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class ScalarUnits(Enum):
        """
            ScalarUnits enumeration
        """
        
        Amount = 'Amount'
        """
            
        """
        

class ScalarDto:
    """
    A DTO representation of a Scalar

    Attributes:
        value (float): The value of the Scalar.
        unit (ScalarUnits): The specific unit that the Scalar value is representing.
    """

    def __init__(self, value: float, unit: ScalarUnits):
        """
        Create a new DTO representation of a Scalar

        Parameters:
            value (float): The value of the Scalar.
            unit (ScalarUnits): The specific unit that the Scalar value is representing.
        """
        self.value: float = value
        """
        The value of the Scalar
        """
        self.unit: ScalarUnits = unit
        """
        The specific unit that the Scalar value is representing
        """

    def to_json(self):
        """
        Get a Scalar DTO JSON object representing the current unit.

        :return: JSON object represents Scalar DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "Amount"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of Scalar DTO from a json representation.

        :param data: The Scalar DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "Amount"}
        :return: A new instance of ScalarDto.
        :rtype: ScalarDto
        """
        return ScalarDto(value=data["value"], unit=ScalarUnits(data["unit"]))


class Scalar(AbstractMeasure):
    """
    A way of representing a number of items.

    Args:
        value (float): The value.
        from_unit (ScalarUnits): The Scalar unit to create from, The default unit is Amount
    """
    def __init__(self, value: float, from_unit: ScalarUnits = ScalarUnits.Amount):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__amount = None
        

    def convert(self, unit: ScalarUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: ScalarUnits = ScalarUnits.Amount) -> ScalarDto:
        """
        Get a new instance of Scalar DTO representing the current unit.

        :param hold_in_unit: The specific Scalar unit to store the Scalar value in the DTO representation.
        :type hold_in_unit: ScalarUnits
        :return: A new instance of ScalarDto.
        :rtype: ScalarDto
        """
        return ScalarDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: ScalarUnits = ScalarUnits.Amount):
        """
        Get a Scalar DTO JSON object representing the current unit.

        :param hold_in_unit: The specific Scalar unit to store the Scalar value in the DTO representation.
        :type hold_in_unit: ScalarUnits
        :return: JSON object represents Scalar DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "Amount"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(scalar_dto: ScalarDto):
        """
        Obtain a new instance of Scalar from a DTO unit object.

        :param scalar_dto: The Scalar DTO representation.
        :type scalar_dto: ScalarDto
        :return: A new instance of Scalar.
        :rtype: Scalar
        """
        return Scalar(scalar_dto.value, scalar_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of Scalar from a DTO unit json representation.

        :param data: The Scalar DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "Amount"}
        :return: A new instance of Scalar.
        :rtype: Scalar
        """
        return Scalar.from_dto(ScalarDto.from_json(data))

    def __convert_from_base(self, from_unit: ScalarUnits) -> float:
        value = self._value
        
        if from_unit == ScalarUnits.Amount:
            return (value)
        
        return None


    def __convert_to_base(self, value: float, to_unit: ScalarUnits) -> float:
        
        if to_unit == ScalarUnits.Amount:
            return (value)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_amount(amount: float):
        """
        Create a new instance of Scalar from a value in amount.

        

        :param meters: The Scalar value in amount.
        :type amount: float
        :return: A new instance of Scalar.
        :rtype: Scalar
        """
        return Scalar(amount, ScalarUnits.Amount)

    
    @property
    def amount(self) -> float:
        """
        
        """
        if self.__amount != None:
            return self.__amount
        self.__amount = self.__convert_from_base(ScalarUnits.Amount)
        return self.__amount

    
    def to_string(self, unit: ScalarUnits = ScalarUnits.Amount, fractional_digits: int = None) -> str:
        """
        Format the Scalar to a string.
        
        Note: the default format for Scalar is Amount.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the Scalar. Default is 'Amount'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == ScalarUnits.Amount:
            return f"""{super()._truncate_fraction_digits(self.amount, fractional_digits)} """
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: ScalarUnits = ScalarUnits.Amount) -> str:
        """
        Get Scalar unit abbreviation.
        Note! the default abbreviation for Scalar is Amount.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == ScalarUnits.Amount:
            return """"""
        
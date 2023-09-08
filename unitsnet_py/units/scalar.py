from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class ScalarUnits(Enum):
        """
            ScalarUnits enumeration
        """
        
        Amount = 'amount'
        """
            
        """
        

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

    
    def to_string(self, unit: ScalarUnits = ScalarUnits.Amount) -> str:
        """
        Format the Scalar to string.
        Note! the default format for Scalar is Amount.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == ScalarUnits.Amount:
            return f"""{self.amount} """
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: ScalarUnits = ScalarUnits.Amount) -> str:
        """
        Get Scalar unit abbreviation.
        Note! the default abbreviation for Scalar is Amount.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == ScalarUnits.Amount:
            return """"""
        
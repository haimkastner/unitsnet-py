from enum import Enum
import math
import string


class ScalarUnits(Enum):
        """
            ScalarUnits enumeration
        """
        
        Amount = 'amount'
        """
            
        """
        

class Scalar:
    """
    A way of representing a number of items.

    Args:
        value (float): The value.
        from_unit (ScalarUnits): The Scalar unit to create from, The default unit is Amount
    """
    def __init__(self, value: float, from_unit: ScalarUnits = ScalarUnits.Amount):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__amount = None
        

    def __convert_from_base(self, from_unit: ScalarUnits) -> float:
        value = self.__value
        
        if from_unit == ScalarUnits.Amount:
            return (value)
        
        return None


    def __convert_to_base(self, value: float, to_unit: ScalarUnits) -> float:
        
        if to_unit == ScalarUnits.Amount:
            return (value)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
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

    
    def to_string(self, unit: ScalarUnits = ScalarUnits.Amount) -> string:
        """
        Format the Scalar to string.
        Note! the default format for Scalar is Amount.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == ScalarUnits.Amount:
            return f"""{self.amount} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: ScalarUnits = ScalarUnits.Amount) -> string:
        """
        Get Scalar unit abbreviation.
        Note! the default abbreviation for Scalar is Amount.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == ScalarUnits.Amount:
            return """"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, Scalar):
            raise TypeError("unsupported operand type(s) for +: 'Scalar' and '{}'".format(type(other).__name__))
        return Scalar(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, Scalar):
            raise TypeError("unsupported operand type(s) for *: 'Scalar' and '{}'".format(type(other).__name__))
        return Scalar(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, Scalar):
            raise TypeError("unsupported operand type(s) for -: 'Scalar' and '{}'".format(type(other).__name__))
        return Scalar(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, Scalar):
            raise TypeError("unsupported operand type(s) for /: 'Scalar' and '{}'".format(type(other).__name__))
        return Scalar(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, Scalar):
            raise TypeError("unsupported operand type(s) for %: 'Scalar' and '{}'".format(type(other).__name__))
        return Scalar(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, Scalar):
            raise TypeError("unsupported operand type(s) for **: 'Scalar' and '{}'".format(type(other).__name__))
        return Scalar(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, Scalar):
            raise TypeError("unsupported operand type(s) for ==: 'Scalar' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, Scalar):
            raise TypeError("unsupported operand type(s) for <: 'Scalar' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, Scalar):
            raise TypeError("unsupported operand type(s) for >: 'Scalar' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, Scalar):
            raise TypeError("unsupported operand type(s) for <=: 'Scalar' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, Scalar):
            raise TypeError("unsupported operand type(s) for >=: 'Scalar' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value
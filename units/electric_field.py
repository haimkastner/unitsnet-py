from enum import Enum
import math
import string


class ElectricFieldUnits(Enum):
        """
            ElectricFieldUnits enumeration
        """
        
        VoltPerMeter = 'volt_per_meter'
        """
            
        """
        

class ElectricField:
    """
    An electric field is a force field that surrounds electric charges that attracts or repels other electric charges.

    Args:
        value (float): The value.
        from_unit (ElectricFieldUnits): The ElectricField unit to create from, The default unit is VoltPerMeter
    """
    def __init__(self, value: float, from_unit: ElectricFieldUnits = ElectricFieldUnits.VoltPerMeter):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__volts_per_meter = None
        

    def __convert_from_base(self, from_unit: ElectricFieldUnits) -> float:
        value = self.__value
        
        if from_unit == ElectricFieldUnits.VoltPerMeter:
            return (value)
        
        return None


    def __convert_to_base(self, value: float, to_unit: ElectricFieldUnits) -> float:
        
        if to_unit == ElectricFieldUnits.VoltPerMeter:
            return (value)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
    @staticmethod
    def from_volts_per_meter(volts_per_meter: float):
        """
        Create a new instance of ElectricField from a value in volts_per_meter.

        

        :param meters: The ElectricField value in volts_per_meter.
        :type volts_per_meter: float
        :return: A new instance of ElectricField.
        :rtype: ElectricField
        """
        return ElectricField(volts_per_meter, ElectricFieldUnits.VoltPerMeter)

    
    @property
    def volts_per_meter(self) -> float:
        """
        
        """
        if self.__volts_per_meter != None:
            return self.__volts_per_meter
        self.__volts_per_meter = self.__convert_from_base(ElectricFieldUnits.VoltPerMeter)
        return self.__volts_per_meter

    
    def to_string(self, unit: ElectricFieldUnits = ElectricFieldUnits.VoltPerMeter) -> string:
        """
        Format the ElectricField to string.
        Note! the default format for ElectricField is VoltPerMeter.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == ElectricFieldUnits.VoltPerMeter:
            return f"""{self.volts_per_meter} V/m"""
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: ElectricFieldUnits = ElectricFieldUnits.VoltPerMeter) -> string:
        """
        Get ElectricField unit abbreviation.
        Note! the default abbreviation for ElectricField is VoltPerMeter.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == ElectricFieldUnits.VoltPerMeter:
            return """V/m"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, ElectricField):
            raise TypeError("unsupported operand type(s) for +: 'ElectricField' and '{}'".format(type(other).__name__))
        return ElectricField(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, ElectricField):
            raise TypeError("unsupported operand type(s) for *: 'ElectricField' and '{}'".format(type(other).__name__))
        return ElectricField(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, ElectricField):
            raise TypeError("unsupported operand type(s) for -: 'ElectricField' and '{}'".format(type(other).__name__))
        return ElectricField(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, ElectricField):
            raise TypeError("unsupported operand type(s) for /: 'ElectricField' and '{}'".format(type(other).__name__))
        return ElectricField(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, ElectricField):
            raise TypeError("unsupported operand type(s) for %: 'ElectricField' and '{}'".format(type(other).__name__))
        return ElectricField(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, ElectricField):
            raise TypeError("unsupported operand type(s) for **: 'ElectricField' and '{}'".format(type(other).__name__))
        return ElectricField(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, ElectricField):
            raise TypeError("unsupported operand type(s) for ==: 'ElectricField' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, ElectricField):
            raise TypeError("unsupported operand type(s) for <: 'ElectricField' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, ElectricField):
            raise TypeError("unsupported operand type(s) for >: 'ElectricField' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, ElectricField):
            raise TypeError("unsupported operand type(s) for <=: 'ElectricField' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, ElectricField):
            raise TypeError("unsupported operand type(s) for >=: 'ElectricField' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value
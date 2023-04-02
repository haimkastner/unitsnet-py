from enum import Enum
import math
import string


class ElectricChargeDensityUnits(Enum):
        """
            ElectricChargeDensityUnits enumeration
        """
        
        CoulombPerCubicMeter = 'coulomb_per_cubic_meter'
        """
            
        """
        

class ElectricChargeDensity:
    """
    In electromagnetism, charge density is a measure of the amount of electric charge per volume.

    Args:
        value (float): The value.
        from_unit (ElectricChargeDensityUnits): The ElectricChargeDensity unit to create from, The default unit is CoulombPerCubicMeter
    """
    def __init__(self, value: float, from_unit: ElectricChargeDensityUnits = ElectricChargeDensityUnits.CoulombPerCubicMeter):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__coulombs_per_cubic_meter = None
        

    def __convert_from_base(self, from_unit: ElectricChargeDensityUnits) -> float:
        value = self.__value
        
        if from_unit == ElectricChargeDensityUnits.CoulombPerCubicMeter:
            return (value)
        
        return None


    def __convert_to_base(self, value: float, to_unit: ElectricChargeDensityUnits) -> float:
        
        if to_unit == ElectricChargeDensityUnits.CoulombPerCubicMeter:
            return (value)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
    @staticmethod
    def from_coulombs_per_cubic_meter(coulombs_per_cubic_meter: float):
        """
        Create a new instance of ElectricChargeDensity from a value in coulombs_per_cubic_meter.

        

        :param meters: The ElectricChargeDensity value in coulombs_per_cubic_meter.
        :type coulombs_per_cubic_meter: float
        :return: A new instance of ElectricChargeDensity.
        :rtype: ElectricChargeDensity
        """
        return ElectricChargeDensity(coulombs_per_cubic_meter, ElectricChargeDensityUnits.CoulombPerCubicMeter)

    
    @property
    def coulombs_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__coulombs_per_cubic_meter != None:
            return self.__coulombs_per_cubic_meter
        self.__coulombs_per_cubic_meter = self.__convert_from_base(ElectricChargeDensityUnits.CoulombPerCubicMeter)
        return self.__coulombs_per_cubic_meter

    
    def to_string(self, unit: ElectricChargeDensityUnits = ElectricChargeDensityUnits.CoulombPerCubicMeter) -> string:
        """
        Format the ElectricChargeDensity to string.
        Note! the default format for ElectricChargeDensity is CoulombPerCubicMeter.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == ElectricChargeDensityUnits.CoulombPerCubicMeter:
            return f"""{self.coulombs_per_cubic_meter} C/m³"""
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: ElectricChargeDensityUnits = ElectricChargeDensityUnits.CoulombPerCubicMeter) -> string:
        """
        Get ElectricChargeDensity unit abbreviation.
        Note! the default abbreviation for ElectricChargeDensity is CoulombPerCubicMeter.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == ElectricChargeDensityUnits.CoulombPerCubicMeter:
            return """C/m³"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, ElectricChargeDensity):
            raise TypeError("unsupported operand type(s) for +: 'ElectricChargeDensity' and '{}'".format(type(other).__name__))
        return ElectricChargeDensity(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, ElectricChargeDensity):
            raise TypeError("unsupported operand type(s) for *: 'ElectricChargeDensity' and '{}'".format(type(other).__name__))
        return ElectricChargeDensity(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, ElectricChargeDensity):
            raise TypeError("unsupported operand type(s) for -: 'ElectricChargeDensity' and '{}'".format(type(other).__name__))
        return ElectricChargeDensity(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, ElectricChargeDensity):
            raise TypeError("unsupported operand type(s) for /: 'ElectricChargeDensity' and '{}'".format(type(other).__name__))
        return ElectricChargeDensity(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, ElectricChargeDensity):
            raise TypeError("unsupported operand type(s) for %: 'ElectricChargeDensity' and '{}'".format(type(other).__name__))
        return ElectricChargeDensity(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, ElectricChargeDensity):
            raise TypeError("unsupported operand type(s) for **: 'ElectricChargeDensity' and '{}'".format(type(other).__name__))
        return ElectricChargeDensity(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, ElectricChargeDensity):
            raise TypeError("unsupported operand type(s) for ==: 'ElectricChargeDensity' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, ElectricChargeDensity):
            raise TypeError("unsupported operand type(s) for <: 'ElectricChargeDensity' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, ElectricChargeDensity):
            raise TypeError("unsupported operand type(s) for >: 'ElectricChargeDensity' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, ElectricChargeDensity):
            raise TypeError("unsupported operand type(s) for <=: 'ElectricChargeDensity' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, ElectricChargeDensity):
            raise TypeError("unsupported operand type(s) for >=: 'ElectricChargeDensity' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value
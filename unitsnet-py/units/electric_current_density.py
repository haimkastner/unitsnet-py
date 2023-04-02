from enum import Enum
import math
import string


class ElectricCurrentDensityUnits(Enum):
        """
            ElectricCurrentDensityUnits enumeration
        """
        
        AmperePerSquareMeter = 'ampere_per_square_meter'
        """
            
        """
        
        AmperePerSquareInch = 'ampere_per_square_inch'
        """
            
        """
        
        AmperePerSquareFoot = 'ampere_per_square_foot'
        """
            
        """
        

class ElectricCurrentDensity:
    """
    In electromagnetism, current density is the electric current per unit area of cross section.

    Args:
        value (float): The value.
        from_unit (ElectricCurrentDensityUnits): The ElectricCurrentDensity unit to create from, The default unit is AmperePerSquareMeter
    """
    def __init__(self, value: float, from_unit: ElectricCurrentDensityUnits = ElectricCurrentDensityUnits.AmperePerSquareMeter):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__amperes_per_square_meter = None
        
        self.__amperes_per_square_inch = None
        
        self.__amperes_per_square_foot = None
        

    def __convert_from_base(self, from_unit: ElectricCurrentDensityUnits) -> float:
        value = self.__value
        
        if from_unit == ElectricCurrentDensityUnits.AmperePerSquareMeter:
            return (value)
        
        if from_unit == ElectricCurrentDensityUnits.AmperePerSquareInch:
            return (value / 1.5500031000062000e3)
        
        if from_unit == ElectricCurrentDensityUnits.AmperePerSquareFoot:
            return (value / 1.0763910416709722e1)
        
        return None


    def __convert_to_base(self, value: float, to_unit: ElectricCurrentDensityUnits) -> float:
        
        if to_unit == ElectricCurrentDensityUnits.AmperePerSquareMeter:
            return (value)
        
        if to_unit == ElectricCurrentDensityUnits.AmperePerSquareInch:
            return (value * 1.5500031000062000e3)
        
        if to_unit == ElectricCurrentDensityUnits.AmperePerSquareFoot:
            return (value * 1.0763910416709722e1)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
    @staticmethod
    def from_amperes_per_square_meter(amperes_per_square_meter: float):
        """
        Create a new instance of ElectricCurrentDensity from a value in amperes_per_square_meter.

        

        :param meters: The ElectricCurrentDensity value in amperes_per_square_meter.
        :type amperes_per_square_meter: float
        :return: A new instance of ElectricCurrentDensity.
        :rtype: ElectricCurrentDensity
        """
        return ElectricCurrentDensity(amperes_per_square_meter, ElectricCurrentDensityUnits.AmperePerSquareMeter)

    
    @staticmethod
    def from_amperes_per_square_inch(amperes_per_square_inch: float):
        """
        Create a new instance of ElectricCurrentDensity from a value in amperes_per_square_inch.

        

        :param meters: The ElectricCurrentDensity value in amperes_per_square_inch.
        :type amperes_per_square_inch: float
        :return: A new instance of ElectricCurrentDensity.
        :rtype: ElectricCurrentDensity
        """
        return ElectricCurrentDensity(amperes_per_square_inch, ElectricCurrentDensityUnits.AmperePerSquareInch)

    
    @staticmethod
    def from_amperes_per_square_foot(amperes_per_square_foot: float):
        """
        Create a new instance of ElectricCurrentDensity from a value in amperes_per_square_foot.

        

        :param meters: The ElectricCurrentDensity value in amperes_per_square_foot.
        :type amperes_per_square_foot: float
        :return: A new instance of ElectricCurrentDensity.
        :rtype: ElectricCurrentDensity
        """
        return ElectricCurrentDensity(amperes_per_square_foot, ElectricCurrentDensityUnits.AmperePerSquareFoot)

    
    @property
    def amperes_per_square_meter(self) -> float:
        """
        
        """
        if self.__amperes_per_square_meter != None:
            return self.__amperes_per_square_meter
        self.__amperes_per_square_meter = self.__convert_from_base(ElectricCurrentDensityUnits.AmperePerSquareMeter)
        return self.__amperes_per_square_meter

    
    @property
    def amperes_per_square_inch(self) -> float:
        """
        
        """
        if self.__amperes_per_square_inch != None:
            return self.__amperes_per_square_inch
        self.__amperes_per_square_inch = self.__convert_from_base(ElectricCurrentDensityUnits.AmperePerSquareInch)
        return self.__amperes_per_square_inch

    
    @property
    def amperes_per_square_foot(self) -> float:
        """
        
        """
        if self.__amperes_per_square_foot != None:
            return self.__amperes_per_square_foot
        self.__amperes_per_square_foot = self.__convert_from_base(ElectricCurrentDensityUnits.AmperePerSquareFoot)
        return self.__amperes_per_square_foot

    
    def to_string(self, unit: ElectricCurrentDensityUnits = ElectricCurrentDensityUnits.AmperePerSquareMeter) -> string:
        """
        Format the ElectricCurrentDensity to string.
        Note! the default format for ElectricCurrentDensity is AmperePerSquareMeter.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == ElectricCurrentDensityUnits.AmperePerSquareMeter:
            return f"""{self.amperes_per_square_meter} A/m²"""
        
        if unit == ElectricCurrentDensityUnits.AmperePerSquareInch:
            return f"""{self.amperes_per_square_inch} A/in²"""
        
        if unit == ElectricCurrentDensityUnits.AmperePerSquareFoot:
            return f"""{self.amperes_per_square_foot} A/ft²"""
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: ElectricCurrentDensityUnits = ElectricCurrentDensityUnits.AmperePerSquareMeter) -> string:
        """
        Get ElectricCurrentDensity unit abbreviation.
        Note! the default abbreviation for ElectricCurrentDensity is AmperePerSquareMeter.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == ElectricCurrentDensityUnits.AmperePerSquareMeter:
            return """A/m²"""
        
        if unit_abbreviation == ElectricCurrentDensityUnits.AmperePerSquareInch:
            return """A/in²"""
        
        if unit_abbreviation == ElectricCurrentDensityUnits.AmperePerSquareFoot:
            return """A/ft²"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, ElectricCurrentDensity):
            raise TypeError("unsupported operand type(s) for +: 'ElectricCurrentDensity' and '{}'".format(type(other).__name__))
        return ElectricCurrentDensity(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, ElectricCurrentDensity):
            raise TypeError("unsupported operand type(s) for *: 'ElectricCurrentDensity' and '{}'".format(type(other).__name__))
        return ElectricCurrentDensity(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, ElectricCurrentDensity):
            raise TypeError("unsupported operand type(s) for -: 'ElectricCurrentDensity' and '{}'".format(type(other).__name__))
        return ElectricCurrentDensity(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, ElectricCurrentDensity):
            raise TypeError("unsupported operand type(s) for /: 'ElectricCurrentDensity' and '{}'".format(type(other).__name__))
        return ElectricCurrentDensity(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, ElectricCurrentDensity):
            raise TypeError("unsupported operand type(s) for %: 'ElectricCurrentDensity' and '{}'".format(type(other).__name__))
        return ElectricCurrentDensity(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, ElectricCurrentDensity):
            raise TypeError("unsupported operand type(s) for **: 'ElectricCurrentDensity' and '{}'".format(type(other).__name__))
        return ElectricCurrentDensity(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, ElectricCurrentDensity):
            raise TypeError("unsupported operand type(s) for ==: 'ElectricCurrentDensity' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, ElectricCurrentDensity):
            raise TypeError("unsupported operand type(s) for <: 'ElectricCurrentDensity' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, ElectricCurrentDensity):
            raise TypeError("unsupported operand type(s) for >: 'ElectricCurrentDensity' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, ElectricCurrentDensity):
            raise TypeError("unsupported operand type(s) for <=: 'ElectricCurrentDensity' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, ElectricCurrentDensity):
            raise TypeError("unsupported operand type(s) for >=: 'ElectricCurrentDensity' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value
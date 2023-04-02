from enum import Enum
import math
import string


class AreaDensityUnits(Enum):
        """
            AreaDensityUnits enumeration
        """
        
        KilogramPerSquareMeter = 'kilogram_per_square_meter'
        """
            
        """
        
        GramPerSquareMeter = 'gram_per_square_meter'
        """
            Also known as grammage for paper industry. In fiber industry used with abbreviation 'gsm'.
        """
        
        MilligramPerSquareMeter = 'milligram_per_square_meter'
        """
            
        """
        

class AreaDensity:
    """
    The area density of a two-dimensional object is calculated as the mass per unit area. For paper this is also called grammage.

    Args:
        value (float): The value.
        from_unit (AreaDensityUnits): The AreaDensity unit to create from, The default unit is KilogramPerSquareMeter
    """
    def __init__(self, value: float, from_unit: AreaDensityUnits = AreaDensityUnits.KilogramPerSquareMeter):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__kilograms_per_square_meter = None
        
        self.__grams_per_square_meter = None
        
        self.__milligrams_per_square_meter = None
        

    def __convert_from_base(self, from_unit: AreaDensityUnits) -> float:
        value = self.__value
        
        if from_unit == AreaDensityUnits.KilogramPerSquareMeter:
            return (value)
        
        if from_unit == AreaDensityUnits.GramPerSquareMeter:
            return (value * 1000)
        
        if from_unit == AreaDensityUnits.MilligramPerSquareMeter:
            return (value * 1000000)
        
        return None


    def __convert_to_base(self, value: float, to_unit: AreaDensityUnits) -> float:
        
        if to_unit == AreaDensityUnits.KilogramPerSquareMeter:
            return (value)
        
        if to_unit == AreaDensityUnits.GramPerSquareMeter:
            return (value / 1000)
        
        if to_unit == AreaDensityUnits.MilligramPerSquareMeter:
            return (value / 1000000)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
    @staticmethod
    def from_kilograms_per_square_meter(kilograms_per_square_meter: float):
        """
        Create a new instance of AreaDensity from a value in kilograms_per_square_meter.

        

        :param meters: The AreaDensity value in kilograms_per_square_meter.
        :type kilograms_per_square_meter: float
        :return: A new instance of AreaDensity.
        :rtype: AreaDensity
        """
        return AreaDensity(kilograms_per_square_meter, AreaDensityUnits.KilogramPerSquareMeter)

    
    @staticmethod
    def from_grams_per_square_meter(grams_per_square_meter: float):
        """
        Create a new instance of AreaDensity from a value in grams_per_square_meter.

        Also known as grammage for paper industry. In fiber industry used with abbreviation 'gsm'.

        :param meters: The AreaDensity value in grams_per_square_meter.
        :type grams_per_square_meter: float
        :return: A new instance of AreaDensity.
        :rtype: AreaDensity
        """
        return AreaDensity(grams_per_square_meter, AreaDensityUnits.GramPerSquareMeter)

    
    @staticmethod
    def from_milligrams_per_square_meter(milligrams_per_square_meter: float):
        """
        Create a new instance of AreaDensity from a value in milligrams_per_square_meter.

        

        :param meters: The AreaDensity value in milligrams_per_square_meter.
        :type milligrams_per_square_meter: float
        :return: A new instance of AreaDensity.
        :rtype: AreaDensity
        """
        return AreaDensity(milligrams_per_square_meter, AreaDensityUnits.MilligramPerSquareMeter)

    
    @property
    def kilograms_per_square_meter(self) -> float:
        """
        
        """
        if self.__kilograms_per_square_meter != None:
            return self.__kilograms_per_square_meter
        self.__kilograms_per_square_meter = self.__convert_from_base(AreaDensityUnits.KilogramPerSquareMeter)
        return self.__kilograms_per_square_meter

    
    @property
    def grams_per_square_meter(self) -> float:
        """
        Also known as grammage for paper industry. In fiber industry used with abbreviation 'gsm'.
        """
        if self.__grams_per_square_meter != None:
            return self.__grams_per_square_meter
        self.__grams_per_square_meter = self.__convert_from_base(AreaDensityUnits.GramPerSquareMeter)
        return self.__grams_per_square_meter

    
    @property
    def milligrams_per_square_meter(self) -> float:
        """
        
        """
        if self.__milligrams_per_square_meter != None:
            return self.__milligrams_per_square_meter
        self.__milligrams_per_square_meter = self.__convert_from_base(AreaDensityUnits.MilligramPerSquareMeter)
        return self.__milligrams_per_square_meter

    
    def to_string(self, unit: AreaDensityUnits = AreaDensityUnits.KilogramPerSquareMeter) -> string:
        """
        Format the AreaDensity to string.
        Note! the default format for AreaDensity is KilogramPerSquareMeter.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == AreaDensityUnits.KilogramPerSquareMeter:
            return f"""{self.kilograms_per_square_meter} kg/m²"""
        
        if unit == AreaDensityUnits.GramPerSquareMeter:
            return f"""{self.grams_per_square_meter} g/m²"""
        
        if unit == AreaDensityUnits.MilligramPerSquareMeter:
            return f"""{self.milligrams_per_square_meter} mg/m²"""
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: AreaDensityUnits = AreaDensityUnits.KilogramPerSquareMeter) -> string:
        """
        Get AreaDensity unit abbreviation.
        Note! the default abbreviation for AreaDensity is KilogramPerSquareMeter.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == AreaDensityUnits.KilogramPerSquareMeter:
            return """kg/m²"""
        
        if unit_abbreviation == AreaDensityUnits.GramPerSquareMeter:
            return """g/m²"""
        
        if unit_abbreviation == AreaDensityUnits.MilligramPerSquareMeter:
            return """mg/m²"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, AreaDensity):
            raise TypeError("unsupported operand type(s) for +: 'AreaDensity' and '{}'".format(type(other).__name__))
        return AreaDensity(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, AreaDensity):
            raise TypeError("unsupported operand type(s) for *: 'AreaDensity' and '{}'".format(type(other).__name__))
        return AreaDensity(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, AreaDensity):
            raise TypeError("unsupported operand type(s) for -: 'AreaDensity' and '{}'".format(type(other).__name__))
        return AreaDensity(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, AreaDensity):
            raise TypeError("unsupported operand type(s) for /: 'AreaDensity' and '{}'".format(type(other).__name__))
        return AreaDensity(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, AreaDensity):
            raise TypeError("unsupported operand type(s) for %: 'AreaDensity' and '{}'".format(type(other).__name__))
        return AreaDensity(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, AreaDensity):
            raise TypeError("unsupported operand type(s) for **: 'AreaDensity' and '{}'".format(type(other).__name__))
        return AreaDensity(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, AreaDensity):
            raise TypeError("unsupported operand type(s) for ==: 'AreaDensity' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, AreaDensity):
            raise TypeError("unsupported operand type(s) for <: 'AreaDensity' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, AreaDensity):
            raise TypeError("unsupported operand type(s) for >: 'AreaDensity' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, AreaDensity):
            raise TypeError("unsupported operand type(s) for <=: 'AreaDensity' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, AreaDensity):
            raise TypeError("unsupported operand type(s) for >=: 'AreaDensity' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value
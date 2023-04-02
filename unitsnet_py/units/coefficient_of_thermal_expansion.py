from enum import Enum
import math
import string


class CoefficientOfThermalExpansionUnits(Enum):
        """
            CoefficientOfThermalExpansionUnits enumeration
        """
        
        InverseKelvin = 'inverse_kelvin'
        """
            
        """
        
        InverseDegreeCelsius = 'inverse_degree_celsius'
        """
            
        """
        
        InverseDegreeFahrenheit = 'inverse_degree_fahrenheit'
        """
            
        """
        

class CoefficientOfThermalExpansion:
    """
    A unit that represents a fractional change in size in response to a change in temperature.

    Args:
        value (float): The value.
        from_unit (CoefficientOfThermalExpansionUnits): The CoefficientOfThermalExpansion unit to create from, The default unit is InverseKelvin
    """
    def __init__(self, value: float, from_unit: CoefficientOfThermalExpansionUnits = CoefficientOfThermalExpansionUnits.InverseKelvin):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__inverse_kelvin = None
        
        self.__inverse_degree_celsius = None
        
        self.__inverse_degree_fahrenheit = None
        

    def __convert_from_base(self, from_unit: CoefficientOfThermalExpansionUnits) -> float:
        value = self.__value
        
        if from_unit == CoefficientOfThermalExpansionUnits.InverseKelvin:
            return (value)
        
        if from_unit == CoefficientOfThermalExpansionUnits.InverseDegreeCelsius:
            return (value)
        
        if from_unit == CoefficientOfThermalExpansionUnits.InverseDegreeFahrenheit:
            return (value * 5 / 9)
        
        return None


    def __convert_to_base(self, value: float, to_unit: CoefficientOfThermalExpansionUnits) -> float:
        
        if to_unit == CoefficientOfThermalExpansionUnits.InverseKelvin:
            return (value)
        
        if to_unit == CoefficientOfThermalExpansionUnits.InverseDegreeCelsius:
            return (value)
        
        if to_unit == CoefficientOfThermalExpansionUnits.InverseDegreeFahrenheit:
            return (value * 9 / 5)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
    @staticmethod
    def from_inverse_kelvin(inverse_kelvin: float):
        """
        Create a new instance of CoefficientOfThermalExpansion from a value in inverse_kelvin.

        

        :param meters: The CoefficientOfThermalExpansion value in inverse_kelvin.
        :type inverse_kelvin: float
        :return: A new instance of CoefficientOfThermalExpansion.
        :rtype: CoefficientOfThermalExpansion
        """
        return CoefficientOfThermalExpansion(inverse_kelvin, CoefficientOfThermalExpansionUnits.InverseKelvin)

    
    @staticmethod
    def from_inverse_degree_celsius(inverse_degree_celsius: float):
        """
        Create a new instance of CoefficientOfThermalExpansion from a value in inverse_degree_celsius.

        

        :param meters: The CoefficientOfThermalExpansion value in inverse_degree_celsius.
        :type inverse_degree_celsius: float
        :return: A new instance of CoefficientOfThermalExpansion.
        :rtype: CoefficientOfThermalExpansion
        """
        return CoefficientOfThermalExpansion(inverse_degree_celsius, CoefficientOfThermalExpansionUnits.InverseDegreeCelsius)

    
    @staticmethod
    def from_inverse_degree_fahrenheit(inverse_degree_fahrenheit: float):
        """
        Create a new instance of CoefficientOfThermalExpansion from a value in inverse_degree_fahrenheit.

        

        :param meters: The CoefficientOfThermalExpansion value in inverse_degree_fahrenheit.
        :type inverse_degree_fahrenheit: float
        :return: A new instance of CoefficientOfThermalExpansion.
        :rtype: CoefficientOfThermalExpansion
        """
        return CoefficientOfThermalExpansion(inverse_degree_fahrenheit, CoefficientOfThermalExpansionUnits.InverseDegreeFahrenheit)

    
    @property
    def inverse_kelvin(self) -> float:
        """
        
        """
        if self.__inverse_kelvin != None:
            return self.__inverse_kelvin
        self.__inverse_kelvin = self.__convert_from_base(CoefficientOfThermalExpansionUnits.InverseKelvin)
        return self.__inverse_kelvin

    
    @property
    def inverse_degree_celsius(self) -> float:
        """
        
        """
        if self.__inverse_degree_celsius != None:
            return self.__inverse_degree_celsius
        self.__inverse_degree_celsius = self.__convert_from_base(CoefficientOfThermalExpansionUnits.InverseDegreeCelsius)
        return self.__inverse_degree_celsius

    
    @property
    def inverse_degree_fahrenheit(self) -> float:
        """
        
        """
        if self.__inverse_degree_fahrenheit != None:
            return self.__inverse_degree_fahrenheit
        self.__inverse_degree_fahrenheit = self.__convert_from_base(CoefficientOfThermalExpansionUnits.InverseDegreeFahrenheit)
        return self.__inverse_degree_fahrenheit

    
    def to_string(self, unit: CoefficientOfThermalExpansionUnits = CoefficientOfThermalExpansionUnits.InverseKelvin) -> string:
        """
        Format the CoefficientOfThermalExpansion to string.
        Note! the default format for CoefficientOfThermalExpansion is InverseKelvin.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == CoefficientOfThermalExpansionUnits.InverseKelvin:
            return f"""{self.inverse_kelvin} K⁻¹"""
        
        if unit == CoefficientOfThermalExpansionUnits.InverseDegreeCelsius:
            return f"""{self.inverse_degree_celsius} °C⁻¹"""
        
        if unit == CoefficientOfThermalExpansionUnits.InverseDegreeFahrenheit:
            return f"""{self.inverse_degree_fahrenheit} °F⁻¹"""
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: CoefficientOfThermalExpansionUnits = CoefficientOfThermalExpansionUnits.InverseKelvin) -> string:
        """
        Get CoefficientOfThermalExpansion unit abbreviation.
        Note! the default abbreviation for CoefficientOfThermalExpansion is InverseKelvin.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == CoefficientOfThermalExpansionUnits.InverseKelvin:
            return """K⁻¹"""
        
        if unit_abbreviation == CoefficientOfThermalExpansionUnits.InverseDegreeCelsius:
            return """°C⁻¹"""
        
        if unit_abbreviation == CoefficientOfThermalExpansionUnits.InverseDegreeFahrenheit:
            return """°F⁻¹"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, CoefficientOfThermalExpansion):
            raise TypeError("unsupported operand type(s) for +: 'CoefficientOfThermalExpansion' and '{}'".format(type(other).__name__))
        return CoefficientOfThermalExpansion(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, CoefficientOfThermalExpansion):
            raise TypeError("unsupported operand type(s) for *: 'CoefficientOfThermalExpansion' and '{}'".format(type(other).__name__))
        return CoefficientOfThermalExpansion(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, CoefficientOfThermalExpansion):
            raise TypeError("unsupported operand type(s) for -: 'CoefficientOfThermalExpansion' and '{}'".format(type(other).__name__))
        return CoefficientOfThermalExpansion(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, CoefficientOfThermalExpansion):
            raise TypeError("unsupported operand type(s) for /: 'CoefficientOfThermalExpansion' and '{}'".format(type(other).__name__))
        return CoefficientOfThermalExpansion(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, CoefficientOfThermalExpansion):
            raise TypeError("unsupported operand type(s) for %: 'CoefficientOfThermalExpansion' and '{}'".format(type(other).__name__))
        return CoefficientOfThermalExpansion(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, CoefficientOfThermalExpansion):
            raise TypeError("unsupported operand type(s) for **: 'CoefficientOfThermalExpansion' and '{}'".format(type(other).__name__))
        return CoefficientOfThermalExpansion(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, CoefficientOfThermalExpansion):
            raise TypeError("unsupported operand type(s) for ==: 'CoefficientOfThermalExpansion' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, CoefficientOfThermalExpansion):
            raise TypeError("unsupported operand type(s) for <: 'CoefficientOfThermalExpansion' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, CoefficientOfThermalExpansion):
            raise TypeError("unsupported operand type(s) for >: 'CoefficientOfThermalExpansion' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, CoefficientOfThermalExpansion):
            raise TypeError("unsupported operand type(s) for <=: 'CoefficientOfThermalExpansion' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, CoefficientOfThermalExpansion):
            raise TypeError("unsupported operand type(s) for >=: 'CoefficientOfThermalExpansion' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value
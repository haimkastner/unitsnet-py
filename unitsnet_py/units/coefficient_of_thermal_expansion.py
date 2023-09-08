from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class CoefficientOfThermalExpansionUnits(Enum):
        """
            CoefficientOfThermalExpansionUnits enumeration
        """
        
        PerKelvin = 'per_kelvin'
        """
            
        """
        
        PerDegreeCelsius = 'per_degree_celsius'
        """
            
        """
        
        PerDegreeFahrenheit = 'per_degree_fahrenheit'
        """
            
        """
        
        PpmPerKelvin = 'ppm_per_kelvin'
        """
            
        """
        
        PpmPerDegreeCelsius = 'ppm_per_degree_celsius'
        """
            
        """
        
        PpmPerDegreeFahrenheit = 'ppm_per_degree_fahrenheit'
        """
            
        """
        

class CoefficientOfThermalExpansion(AbstractMeasure):
    """
    A unit that represents a fractional change in size in response to a change in temperature.

    Args:
        value (float): The value.
        from_unit (CoefficientOfThermalExpansionUnits): The CoefficientOfThermalExpansion unit to create from, The default unit is PerKelvin
    """
    def __init__(self, value: float, from_unit: CoefficientOfThermalExpansionUnits = CoefficientOfThermalExpansionUnits.PerKelvin):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__per_kelvin = None
        
        self.__per_degree_celsius = None
        
        self.__per_degree_fahrenheit = None
        
        self.__ppm_per_kelvin = None
        
        self.__ppm_per_degree_celsius = None
        
        self.__ppm_per_degree_fahrenheit = None
        

    def convert(self, unit: CoefficientOfThermalExpansionUnits) -> float:
        return self.__convert_from_base(unit)

    def __convert_from_base(self, from_unit: CoefficientOfThermalExpansionUnits) -> float:
        value = self._value
        
        if from_unit == CoefficientOfThermalExpansionUnits.PerKelvin:
            return (value)
        
        if from_unit == CoefficientOfThermalExpansionUnits.PerDegreeCelsius:
            return (value)
        
        if from_unit == CoefficientOfThermalExpansionUnits.PerDegreeFahrenheit:
            return (value * 5 / 9)
        
        if from_unit == CoefficientOfThermalExpansionUnits.PpmPerKelvin:
            return (value * 1e6)
        
        if from_unit == CoefficientOfThermalExpansionUnits.PpmPerDegreeCelsius:
            return (value * 1e6)
        
        if from_unit == CoefficientOfThermalExpansionUnits.PpmPerDegreeFahrenheit:
            return (value * 5e6 / 9)
        
        return None


    def __convert_to_base(self, value: float, to_unit: CoefficientOfThermalExpansionUnits) -> float:
        
        if to_unit == CoefficientOfThermalExpansionUnits.PerKelvin:
            return (value)
        
        if to_unit == CoefficientOfThermalExpansionUnits.PerDegreeCelsius:
            return (value)
        
        if to_unit == CoefficientOfThermalExpansionUnits.PerDegreeFahrenheit:
            return (value * 9 / 5)
        
        if to_unit == CoefficientOfThermalExpansionUnits.PpmPerKelvin:
            return (value / 1e6)
        
        if to_unit == CoefficientOfThermalExpansionUnits.PpmPerDegreeCelsius:
            return (value / 1e6)
        
        if to_unit == CoefficientOfThermalExpansionUnits.PpmPerDegreeFahrenheit:
            return (value * 9 / 5e6)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_per_kelvin(per_kelvin: float):
        """
        Create a new instance of CoefficientOfThermalExpansion from a value in per_kelvin.

        

        :param meters: The CoefficientOfThermalExpansion value in per_kelvin.
        :type per_kelvin: float
        :return: A new instance of CoefficientOfThermalExpansion.
        :rtype: CoefficientOfThermalExpansion
        """
        return CoefficientOfThermalExpansion(per_kelvin, CoefficientOfThermalExpansionUnits.PerKelvin)

    
    @staticmethod
    def from_per_degree_celsius(per_degree_celsius: float):
        """
        Create a new instance of CoefficientOfThermalExpansion from a value in per_degree_celsius.

        

        :param meters: The CoefficientOfThermalExpansion value in per_degree_celsius.
        :type per_degree_celsius: float
        :return: A new instance of CoefficientOfThermalExpansion.
        :rtype: CoefficientOfThermalExpansion
        """
        return CoefficientOfThermalExpansion(per_degree_celsius, CoefficientOfThermalExpansionUnits.PerDegreeCelsius)

    
    @staticmethod
    def from_per_degree_fahrenheit(per_degree_fahrenheit: float):
        """
        Create a new instance of CoefficientOfThermalExpansion from a value in per_degree_fahrenheit.

        

        :param meters: The CoefficientOfThermalExpansion value in per_degree_fahrenheit.
        :type per_degree_fahrenheit: float
        :return: A new instance of CoefficientOfThermalExpansion.
        :rtype: CoefficientOfThermalExpansion
        """
        return CoefficientOfThermalExpansion(per_degree_fahrenheit, CoefficientOfThermalExpansionUnits.PerDegreeFahrenheit)

    
    @staticmethod
    def from_ppm_per_kelvin(ppm_per_kelvin: float):
        """
        Create a new instance of CoefficientOfThermalExpansion from a value in ppm_per_kelvin.

        

        :param meters: The CoefficientOfThermalExpansion value in ppm_per_kelvin.
        :type ppm_per_kelvin: float
        :return: A new instance of CoefficientOfThermalExpansion.
        :rtype: CoefficientOfThermalExpansion
        """
        return CoefficientOfThermalExpansion(ppm_per_kelvin, CoefficientOfThermalExpansionUnits.PpmPerKelvin)

    
    @staticmethod
    def from_ppm_per_degree_celsius(ppm_per_degree_celsius: float):
        """
        Create a new instance of CoefficientOfThermalExpansion from a value in ppm_per_degree_celsius.

        

        :param meters: The CoefficientOfThermalExpansion value in ppm_per_degree_celsius.
        :type ppm_per_degree_celsius: float
        :return: A new instance of CoefficientOfThermalExpansion.
        :rtype: CoefficientOfThermalExpansion
        """
        return CoefficientOfThermalExpansion(ppm_per_degree_celsius, CoefficientOfThermalExpansionUnits.PpmPerDegreeCelsius)

    
    @staticmethod
    def from_ppm_per_degree_fahrenheit(ppm_per_degree_fahrenheit: float):
        """
        Create a new instance of CoefficientOfThermalExpansion from a value in ppm_per_degree_fahrenheit.

        

        :param meters: The CoefficientOfThermalExpansion value in ppm_per_degree_fahrenheit.
        :type ppm_per_degree_fahrenheit: float
        :return: A new instance of CoefficientOfThermalExpansion.
        :rtype: CoefficientOfThermalExpansion
        """
        return CoefficientOfThermalExpansion(ppm_per_degree_fahrenheit, CoefficientOfThermalExpansionUnits.PpmPerDegreeFahrenheit)

    
    @property
    def per_kelvin(self) -> float:
        """
        
        """
        if self.__per_kelvin != None:
            return self.__per_kelvin
        self.__per_kelvin = self.__convert_from_base(CoefficientOfThermalExpansionUnits.PerKelvin)
        return self.__per_kelvin

    
    @property
    def per_degree_celsius(self) -> float:
        """
        
        """
        if self.__per_degree_celsius != None:
            return self.__per_degree_celsius
        self.__per_degree_celsius = self.__convert_from_base(CoefficientOfThermalExpansionUnits.PerDegreeCelsius)
        return self.__per_degree_celsius

    
    @property
    def per_degree_fahrenheit(self) -> float:
        """
        
        """
        if self.__per_degree_fahrenheit != None:
            return self.__per_degree_fahrenheit
        self.__per_degree_fahrenheit = self.__convert_from_base(CoefficientOfThermalExpansionUnits.PerDegreeFahrenheit)
        return self.__per_degree_fahrenheit

    
    @property
    def ppm_per_kelvin(self) -> float:
        """
        
        """
        if self.__ppm_per_kelvin != None:
            return self.__ppm_per_kelvin
        self.__ppm_per_kelvin = self.__convert_from_base(CoefficientOfThermalExpansionUnits.PpmPerKelvin)
        return self.__ppm_per_kelvin

    
    @property
    def ppm_per_degree_celsius(self) -> float:
        """
        
        """
        if self.__ppm_per_degree_celsius != None:
            return self.__ppm_per_degree_celsius
        self.__ppm_per_degree_celsius = self.__convert_from_base(CoefficientOfThermalExpansionUnits.PpmPerDegreeCelsius)
        return self.__ppm_per_degree_celsius

    
    @property
    def ppm_per_degree_fahrenheit(self) -> float:
        """
        
        """
        if self.__ppm_per_degree_fahrenheit != None:
            return self.__ppm_per_degree_fahrenheit
        self.__ppm_per_degree_fahrenheit = self.__convert_from_base(CoefficientOfThermalExpansionUnits.PpmPerDegreeFahrenheit)
        return self.__ppm_per_degree_fahrenheit

    
    def to_string(self, unit: CoefficientOfThermalExpansionUnits = CoefficientOfThermalExpansionUnits.PerKelvin) -> str:
        """
        Format the CoefficientOfThermalExpansion to string.
        Note! the default format for CoefficientOfThermalExpansion is PerKelvin.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == CoefficientOfThermalExpansionUnits.PerKelvin:
            return f"""{self.per_kelvin} K⁻¹"""
        
        if unit == CoefficientOfThermalExpansionUnits.PerDegreeCelsius:
            return f"""{self.per_degree_celsius} °C⁻¹"""
        
        if unit == CoefficientOfThermalExpansionUnits.PerDegreeFahrenheit:
            return f"""{self.per_degree_fahrenheit} °F⁻¹"""
        
        if unit == CoefficientOfThermalExpansionUnits.PpmPerKelvin:
            return f"""{self.ppm_per_kelvin} ppm/K"""
        
        if unit == CoefficientOfThermalExpansionUnits.PpmPerDegreeCelsius:
            return f"""{self.ppm_per_degree_celsius} ppm/°C"""
        
        if unit == CoefficientOfThermalExpansionUnits.PpmPerDegreeFahrenheit:
            return f"""{self.ppm_per_degree_fahrenheit} ppm/°F"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: CoefficientOfThermalExpansionUnits = CoefficientOfThermalExpansionUnits.PerKelvin) -> str:
        """
        Get CoefficientOfThermalExpansion unit abbreviation.
        Note! the default abbreviation for CoefficientOfThermalExpansion is PerKelvin.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == CoefficientOfThermalExpansionUnits.PerKelvin:
            return """K⁻¹"""
        
        if unit_abbreviation == CoefficientOfThermalExpansionUnits.PerDegreeCelsius:
            return """°C⁻¹"""
        
        if unit_abbreviation == CoefficientOfThermalExpansionUnits.PerDegreeFahrenheit:
            return """°F⁻¹"""
        
        if unit_abbreviation == CoefficientOfThermalExpansionUnits.PpmPerKelvin:
            return """ppm/K"""
        
        if unit_abbreviation == CoefficientOfThermalExpansionUnits.PpmPerDegreeCelsius:
            return """ppm/°C"""
        
        if unit_abbreviation == CoefficientOfThermalExpansionUnits.PpmPerDegreeFahrenheit:
            return """ppm/°F"""
        
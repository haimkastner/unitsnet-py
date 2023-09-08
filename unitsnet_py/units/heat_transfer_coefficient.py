from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class HeatTransferCoefficientUnits(Enum):
        """
            HeatTransferCoefficientUnits enumeration
        """
        
        WattPerSquareMeterKelvin = 'watt_per_square_meter_kelvin'
        """
            
        """
        
        WattPerSquareMeterCelsius = 'watt_per_square_meter_celsius'
        """
            
        """
        
        BtuPerHourSquareFootDegreeFahrenheit = 'btu_per_hour_square_foot_degree_fahrenheit'
        """
            
        """
        
        CaloriePerHourSquareMeterDegreeCelsius = 'calorie_per_hour_square_meter_degree_celsius'
        """
            
        """
        
        KilocaloriePerHourSquareMeterDegreeCelsius = 'kilocalorie_per_hour_square_meter_degree_celsius'
        """
            
        """
        

class HeatTransferCoefficient(AbstractMeasure):
    """
    The heat transfer coefficient or film coefficient, or film effectiveness, in thermodynamics and in mechanics is the proportionality constant between the heat flux and the thermodynamic driving force for the flow of heat (i.e., the temperature difference, ΔT)

    Args:
        value (float): The value.
        from_unit (HeatTransferCoefficientUnits): The HeatTransferCoefficient unit to create from, The default unit is WattPerSquareMeterKelvin
    """
    def __init__(self, value: float, from_unit: HeatTransferCoefficientUnits = HeatTransferCoefficientUnits.WattPerSquareMeterKelvin):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__watts_per_square_meter_kelvin = None
        
        self.__watts_per_square_meter_celsius = None
        
        self.__btus_per_hour_square_foot_degree_fahrenheit = None
        
        self.__calories_per_hour_square_meter_degree_celsius = None
        
        self.__kilocalories_per_hour_square_meter_degree_celsius = None
        

    def convert(self, unit: HeatTransferCoefficientUnits) -> float:
        return self.__convert_from_base(unit)

    def __convert_from_base(self, from_unit: HeatTransferCoefficientUnits) -> float:
        value = self._value
        
        if from_unit == HeatTransferCoefficientUnits.WattPerSquareMeterKelvin:
            return (value)
        
        if from_unit == HeatTransferCoefficientUnits.WattPerSquareMeterCelsius:
            return (value)
        
        if from_unit == HeatTransferCoefficientUnits.BtuPerHourSquareFootDegreeFahrenheit:
            return (value / 5.6782633411134878)
        
        if from_unit == HeatTransferCoefficientUnits.CaloriePerHourSquareMeterDegreeCelsius:
            return ((value / 4.1868) * 3600)
        
        if from_unit == HeatTransferCoefficientUnits.KilocaloriePerHourSquareMeterDegreeCelsius:
            return (((value / 4.1868) * 3600) / 1000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: HeatTransferCoefficientUnits) -> float:
        
        if to_unit == HeatTransferCoefficientUnits.WattPerSquareMeterKelvin:
            return (value)
        
        if to_unit == HeatTransferCoefficientUnits.WattPerSquareMeterCelsius:
            return (value)
        
        if to_unit == HeatTransferCoefficientUnits.BtuPerHourSquareFootDegreeFahrenheit:
            return (value * 5.6782633411134878)
        
        if to_unit == HeatTransferCoefficientUnits.CaloriePerHourSquareMeterDegreeCelsius:
            return ((value * 4.1868) / 3600)
        
        if to_unit == HeatTransferCoefficientUnits.KilocaloriePerHourSquareMeterDegreeCelsius:
            return (((value * 4.1868) / 3600) * 1000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_watts_per_square_meter_kelvin(watts_per_square_meter_kelvin: float):
        """
        Create a new instance of HeatTransferCoefficient from a value in watts_per_square_meter_kelvin.

        

        :param meters: The HeatTransferCoefficient value in watts_per_square_meter_kelvin.
        :type watts_per_square_meter_kelvin: float
        :return: A new instance of HeatTransferCoefficient.
        :rtype: HeatTransferCoefficient
        """
        return HeatTransferCoefficient(watts_per_square_meter_kelvin, HeatTransferCoefficientUnits.WattPerSquareMeterKelvin)

    
    @staticmethod
    def from_watts_per_square_meter_celsius(watts_per_square_meter_celsius: float):
        """
        Create a new instance of HeatTransferCoefficient from a value in watts_per_square_meter_celsius.

        

        :param meters: The HeatTransferCoefficient value in watts_per_square_meter_celsius.
        :type watts_per_square_meter_celsius: float
        :return: A new instance of HeatTransferCoefficient.
        :rtype: HeatTransferCoefficient
        """
        return HeatTransferCoefficient(watts_per_square_meter_celsius, HeatTransferCoefficientUnits.WattPerSquareMeterCelsius)

    
    @staticmethod
    def from_btus_per_hour_square_foot_degree_fahrenheit(btus_per_hour_square_foot_degree_fahrenheit: float):
        """
        Create a new instance of HeatTransferCoefficient from a value in btus_per_hour_square_foot_degree_fahrenheit.

        

        :param meters: The HeatTransferCoefficient value in btus_per_hour_square_foot_degree_fahrenheit.
        :type btus_per_hour_square_foot_degree_fahrenheit: float
        :return: A new instance of HeatTransferCoefficient.
        :rtype: HeatTransferCoefficient
        """
        return HeatTransferCoefficient(btus_per_hour_square_foot_degree_fahrenheit, HeatTransferCoefficientUnits.BtuPerHourSquareFootDegreeFahrenheit)

    
    @staticmethod
    def from_calories_per_hour_square_meter_degree_celsius(calories_per_hour_square_meter_degree_celsius: float):
        """
        Create a new instance of HeatTransferCoefficient from a value in calories_per_hour_square_meter_degree_celsius.

        

        :param meters: The HeatTransferCoefficient value in calories_per_hour_square_meter_degree_celsius.
        :type calories_per_hour_square_meter_degree_celsius: float
        :return: A new instance of HeatTransferCoefficient.
        :rtype: HeatTransferCoefficient
        """
        return HeatTransferCoefficient(calories_per_hour_square_meter_degree_celsius, HeatTransferCoefficientUnits.CaloriePerHourSquareMeterDegreeCelsius)

    
    @staticmethod
    def from_kilocalories_per_hour_square_meter_degree_celsius(kilocalories_per_hour_square_meter_degree_celsius: float):
        """
        Create a new instance of HeatTransferCoefficient from a value in kilocalories_per_hour_square_meter_degree_celsius.

        

        :param meters: The HeatTransferCoefficient value in kilocalories_per_hour_square_meter_degree_celsius.
        :type kilocalories_per_hour_square_meter_degree_celsius: float
        :return: A new instance of HeatTransferCoefficient.
        :rtype: HeatTransferCoefficient
        """
        return HeatTransferCoefficient(kilocalories_per_hour_square_meter_degree_celsius, HeatTransferCoefficientUnits.KilocaloriePerHourSquareMeterDegreeCelsius)

    
    @property
    def watts_per_square_meter_kelvin(self) -> float:
        """
        
        """
        if self.__watts_per_square_meter_kelvin != None:
            return self.__watts_per_square_meter_kelvin
        self.__watts_per_square_meter_kelvin = self.__convert_from_base(HeatTransferCoefficientUnits.WattPerSquareMeterKelvin)
        return self.__watts_per_square_meter_kelvin

    
    @property
    def watts_per_square_meter_celsius(self) -> float:
        """
        
        """
        if self.__watts_per_square_meter_celsius != None:
            return self.__watts_per_square_meter_celsius
        self.__watts_per_square_meter_celsius = self.__convert_from_base(HeatTransferCoefficientUnits.WattPerSquareMeterCelsius)
        return self.__watts_per_square_meter_celsius

    
    @property
    def btus_per_hour_square_foot_degree_fahrenheit(self) -> float:
        """
        
        """
        if self.__btus_per_hour_square_foot_degree_fahrenheit != None:
            return self.__btus_per_hour_square_foot_degree_fahrenheit
        self.__btus_per_hour_square_foot_degree_fahrenheit = self.__convert_from_base(HeatTransferCoefficientUnits.BtuPerHourSquareFootDegreeFahrenheit)
        return self.__btus_per_hour_square_foot_degree_fahrenheit

    
    @property
    def calories_per_hour_square_meter_degree_celsius(self) -> float:
        """
        
        """
        if self.__calories_per_hour_square_meter_degree_celsius != None:
            return self.__calories_per_hour_square_meter_degree_celsius
        self.__calories_per_hour_square_meter_degree_celsius = self.__convert_from_base(HeatTransferCoefficientUnits.CaloriePerHourSquareMeterDegreeCelsius)
        return self.__calories_per_hour_square_meter_degree_celsius

    
    @property
    def kilocalories_per_hour_square_meter_degree_celsius(self) -> float:
        """
        
        """
        if self.__kilocalories_per_hour_square_meter_degree_celsius != None:
            return self.__kilocalories_per_hour_square_meter_degree_celsius
        self.__kilocalories_per_hour_square_meter_degree_celsius = self.__convert_from_base(HeatTransferCoefficientUnits.KilocaloriePerHourSquareMeterDegreeCelsius)
        return self.__kilocalories_per_hour_square_meter_degree_celsius

    
    def to_string(self, unit: HeatTransferCoefficientUnits = HeatTransferCoefficientUnits.WattPerSquareMeterKelvin) -> str:
        """
        Format the HeatTransferCoefficient to string.
        Note! the default format for HeatTransferCoefficient is WattPerSquareMeterKelvin.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == HeatTransferCoefficientUnits.WattPerSquareMeterKelvin:
            return f"""{self.watts_per_square_meter_kelvin} W/m²·K"""
        
        if unit == HeatTransferCoefficientUnits.WattPerSquareMeterCelsius:
            return f"""{self.watts_per_square_meter_celsius} W/m²·°C"""
        
        if unit == HeatTransferCoefficientUnits.BtuPerHourSquareFootDegreeFahrenheit:
            return f"""{self.btus_per_hour_square_foot_degree_fahrenheit} Btu/h·ft²·°F"""
        
        if unit == HeatTransferCoefficientUnits.CaloriePerHourSquareMeterDegreeCelsius:
            return f"""{self.calories_per_hour_square_meter_degree_celsius} kcal/h·m²·°C"""
        
        if unit == HeatTransferCoefficientUnits.KilocaloriePerHourSquareMeterDegreeCelsius:
            return f"""{self.kilocalories_per_hour_square_meter_degree_celsius} kkcal/h·m²·°C"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: HeatTransferCoefficientUnits = HeatTransferCoefficientUnits.WattPerSquareMeterKelvin) -> str:
        """
        Get HeatTransferCoefficient unit abbreviation.
        Note! the default abbreviation for HeatTransferCoefficient is WattPerSquareMeterKelvin.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == HeatTransferCoefficientUnits.WattPerSquareMeterKelvin:
            return """W/m²·K"""
        
        if unit_abbreviation == HeatTransferCoefficientUnits.WattPerSquareMeterCelsius:
            return """W/m²·°C"""
        
        if unit_abbreviation == HeatTransferCoefficientUnits.BtuPerHourSquareFootDegreeFahrenheit:
            return """Btu/h·ft²·°F"""
        
        if unit_abbreviation == HeatTransferCoefficientUnits.CaloriePerHourSquareMeterDegreeCelsius:
            return """kcal/h·m²·°C"""
        
        if unit_abbreviation == HeatTransferCoefficientUnits.KilocaloriePerHourSquareMeterDegreeCelsius:
            return """kkcal/h·m²·°C"""
        
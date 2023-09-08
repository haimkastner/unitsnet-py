from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class VolumetricHeatCapacityUnits(Enum):
        """
            VolumetricHeatCapacityUnits enumeration
        """
        
        JoulePerCubicMeterKelvin = 'joule_per_cubic_meter_kelvin'
        """
            
        """
        
        JoulePerCubicMeterDegreeCelsius = 'joule_per_cubic_meter_degree_celsius'
        """
            
        """
        
        CaloriePerCubicCentimeterDegreeCelsius = 'calorie_per_cubic_centimeter_degree_celsius'
        """
            
        """
        
        BtuPerCubicFootDegreeFahrenheit = 'btu_per_cubic_foot_degree_fahrenheit'
        """
            
        """
        
        KilojoulePerCubicMeterKelvin = 'kilojoule_per_cubic_meter_kelvin'
        """
            
        """
        
        MegajoulePerCubicMeterKelvin = 'megajoule_per_cubic_meter_kelvin'
        """
            
        """
        
        KilojoulePerCubicMeterDegreeCelsius = 'kilojoule_per_cubic_meter_degree_celsius'
        """
            
        """
        
        MegajoulePerCubicMeterDegreeCelsius = 'megajoule_per_cubic_meter_degree_celsius'
        """
            
        """
        
        KilocaloriePerCubicCentimeterDegreeCelsius = 'kilocalorie_per_cubic_centimeter_degree_celsius'
        """
            
        """
        

class VolumetricHeatCapacity(AbstractMeasure):
    """
    The volumetric heat capacity is the amount of energy that must be added, in the form of heat, to one unit of volume of the material in order to cause an increase of one unit in its temperature.

    Args:
        value (float): The value.
        from_unit (VolumetricHeatCapacityUnits): The VolumetricHeatCapacity unit to create from, The default unit is JoulePerCubicMeterKelvin
    """
    def __init__(self, value: float, from_unit: VolumetricHeatCapacityUnits = VolumetricHeatCapacityUnits.JoulePerCubicMeterKelvin):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__joules_per_cubic_meter_kelvin = None
        
        self.__joules_per_cubic_meter_degree_celsius = None
        
        self.__calories_per_cubic_centimeter_degree_celsius = None
        
        self.__btus_per_cubic_foot_degree_fahrenheit = None
        
        self.__kilojoules_per_cubic_meter_kelvin = None
        
        self.__megajoules_per_cubic_meter_kelvin = None
        
        self.__kilojoules_per_cubic_meter_degree_celsius = None
        
        self.__megajoules_per_cubic_meter_degree_celsius = None
        
        self.__kilocalories_per_cubic_centimeter_degree_celsius = None
        

    def convert(self, unit: VolumetricHeatCapacityUnits) -> float:
        return self.__convert_from_base(unit)

    def __convert_from_base(self, from_unit: VolumetricHeatCapacityUnits) -> float:
        value = self._value
        
        if from_unit == VolumetricHeatCapacityUnits.JoulePerCubicMeterKelvin:
            return (value)
        
        if from_unit == VolumetricHeatCapacityUnits.JoulePerCubicMeterDegreeCelsius:
            return (value)
        
        if from_unit == VolumetricHeatCapacityUnits.CaloriePerCubicCentimeterDegreeCelsius:
            return (value * 2.388459e-7)
        
        if from_unit == VolumetricHeatCapacityUnits.BtuPerCubicFootDegreeFahrenheit:
            return (value * 1.4910660e-5)
        
        if from_unit == VolumetricHeatCapacityUnits.KilojoulePerCubicMeterKelvin:
            return ((value) / 1000.0)
        
        if from_unit == VolumetricHeatCapacityUnits.MegajoulePerCubicMeterKelvin:
            return ((value) / 1000000.0)
        
        if from_unit == VolumetricHeatCapacityUnits.KilojoulePerCubicMeterDegreeCelsius:
            return ((value) / 1000.0)
        
        if from_unit == VolumetricHeatCapacityUnits.MegajoulePerCubicMeterDegreeCelsius:
            return ((value) / 1000000.0)
        
        if from_unit == VolumetricHeatCapacityUnits.KilocaloriePerCubicCentimeterDegreeCelsius:
            return ((value * 2.388459e-7) / 1000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: VolumetricHeatCapacityUnits) -> float:
        
        if to_unit == VolumetricHeatCapacityUnits.JoulePerCubicMeterKelvin:
            return (value)
        
        if to_unit == VolumetricHeatCapacityUnits.JoulePerCubicMeterDegreeCelsius:
            return (value)
        
        if to_unit == VolumetricHeatCapacityUnits.CaloriePerCubicCentimeterDegreeCelsius:
            return (value / 2.388459e-7)
        
        if to_unit == VolumetricHeatCapacityUnits.BtuPerCubicFootDegreeFahrenheit:
            return (value / 1.4910660e-5)
        
        if to_unit == VolumetricHeatCapacityUnits.KilojoulePerCubicMeterKelvin:
            return ((value) * 1000.0)
        
        if to_unit == VolumetricHeatCapacityUnits.MegajoulePerCubicMeterKelvin:
            return ((value) * 1000000.0)
        
        if to_unit == VolumetricHeatCapacityUnits.KilojoulePerCubicMeterDegreeCelsius:
            return ((value) * 1000.0)
        
        if to_unit == VolumetricHeatCapacityUnits.MegajoulePerCubicMeterDegreeCelsius:
            return ((value) * 1000000.0)
        
        if to_unit == VolumetricHeatCapacityUnits.KilocaloriePerCubicCentimeterDegreeCelsius:
            return ((value / 2.388459e-7) * 1000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_joules_per_cubic_meter_kelvin(joules_per_cubic_meter_kelvin: float):
        """
        Create a new instance of VolumetricHeatCapacity from a value in joules_per_cubic_meter_kelvin.

        

        :param meters: The VolumetricHeatCapacity value in joules_per_cubic_meter_kelvin.
        :type joules_per_cubic_meter_kelvin: float
        :return: A new instance of VolumetricHeatCapacity.
        :rtype: VolumetricHeatCapacity
        """
        return VolumetricHeatCapacity(joules_per_cubic_meter_kelvin, VolumetricHeatCapacityUnits.JoulePerCubicMeterKelvin)

    
    @staticmethod
    def from_joules_per_cubic_meter_degree_celsius(joules_per_cubic_meter_degree_celsius: float):
        """
        Create a new instance of VolumetricHeatCapacity from a value in joules_per_cubic_meter_degree_celsius.

        

        :param meters: The VolumetricHeatCapacity value in joules_per_cubic_meter_degree_celsius.
        :type joules_per_cubic_meter_degree_celsius: float
        :return: A new instance of VolumetricHeatCapacity.
        :rtype: VolumetricHeatCapacity
        """
        return VolumetricHeatCapacity(joules_per_cubic_meter_degree_celsius, VolumetricHeatCapacityUnits.JoulePerCubicMeterDegreeCelsius)

    
    @staticmethod
    def from_calories_per_cubic_centimeter_degree_celsius(calories_per_cubic_centimeter_degree_celsius: float):
        """
        Create a new instance of VolumetricHeatCapacity from a value in calories_per_cubic_centimeter_degree_celsius.

        

        :param meters: The VolumetricHeatCapacity value in calories_per_cubic_centimeter_degree_celsius.
        :type calories_per_cubic_centimeter_degree_celsius: float
        :return: A new instance of VolumetricHeatCapacity.
        :rtype: VolumetricHeatCapacity
        """
        return VolumetricHeatCapacity(calories_per_cubic_centimeter_degree_celsius, VolumetricHeatCapacityUnits.CaloriePerCubicCentimeterDegreeCelsius)

    
    @staticmethod
    def from_btus_per_cubic_foot_degree_fahrenheit(btus_per_cubic_foot_degree_fahrenheit: float):
        """
        Create a new instance of VolumetricHeatCapacity from a value in btus_per_cubic_foot_degree_fahrenheit.

        

        :param meters: The VolumetricHeatCapacity value in btus_per_cubic_foot_degree_fahrenheit.
        :type btus_per_cubic_foot_degree_fahrenheit: float
        :return: A new instance of VolumetricHeatCapacity.
        :rtype: VolumetricHeatCapacity
        """
        return VolumetricHeatCapacity(btus_per_cubic_foot_degree_fahrenheit, VolumetricHeatCapacityUnits.BtuPerCubicFootDegreeFahrenheit)

    
    @staticmethod
    def from_kilojoules_per_cubic_meter_kelvin(kilojoules_per_cubic_meter_kelvin: float):
        """
        Create a new instance of VolumetricHeatCapacity from a value in kilojoules_per_cubic_meter_kelvin.

        

        :param meters: The VolumetricHeatCapacity value in kilojoules_per_cubic_meter_kelvin.
        :type kilojoules_per_cubic_meter_kelvin: float
        :return: A new instance of VolumetricHeatCapacity.
        :rtype: VolumetricHeatCapacity
        """
        return VolumetricHeatCapacity(kilojoules_per_cubic_meter_kelvin, VolumetricHeatCapacityUnits.KilojoulePerCubicMeterKelvin)

    
    @staticmethod
    def from_megajoules_per_cubic_meter_kelvin(megajoules_per_cubic_meter_kelvin: float):
        """
        Create a new instance of VolumetricHeatCapacity from a value in megajoules_per_cubic_meter_kelvin.

        

        :param meters: The VolumetricHeatCapacity value in megajoules_per_cubic_meter_kelvin.
        :type megajoules_per_cubic_meter_kelvin: float
        :return: A new instance of VolumetricHeatCapacity.
        :rtype: VolumetricHeatCapacity
        """
        return VolumetricHeatCapacity(megajoules_per_cubic_meter_kelvin, VolumetricHeatCapacityUnits.MegajoulePerCubicMeterKelvin)

    
    @staticmethod
    def from_kilojoules_per_cubic_meter_degree_celsius(kilojoules_per_cubic_meter_degree_celsius: float):
        """
        Create a new instance of VolumetricHeatCapacity from a value in kilojoules_per_cubic_meter_degree_celsius.

        

        :param meters: The VolumetricHeatCapacity value in kilojoules_per_cubic_meter_degree_celsius.
        :type kilojoules_per_cubic_meter_degree_celsius: float
        :return: A new instance of VolumetricHeatCapacity.
        :rtype: VolumetricHeatCapacity
        """
        return VolumetricHeatCapacity(kilojoules_per_cubic_meter_degree_celsius, VolumetricHeatCapacityUnits.KilojoulePerCubicMeterDegreeCelsius)

    
    @staticmethod
    def from_megajoules_per_cubic_meter_degree_celsius(megajoules_per_cubic_meter_degree_celsius: float):
        """
        Create a new instance of VolumetricHeatCapacity from a value in megajoules_per_cubic_meter_degree_celsius.

        

        :param meters: The VolumetricHeatCapacity value in megajoules_per_cubic_meter_degree_celsius.
        :type megajoules_per_cubic_meter_degree_celsius: float
        :return: A new instance of VolumetricHeatCapacity.
        :rtype: VolumetricHeatCapacity
        """
        return VolumetricHeatCapacity(megajoules_per_cubic_meter_degree_celsius, VolumetricHeatCapacityUnits.MegajoulePerCubicMeterDegreeCelsius)

    
    @staticmethod
    def from_kilocalories_per_cubic_centimeter_degree_celsius(kilocalories_per_cubic_centimeter_degree_celsius: float):
        """
        Create a new instance of VolumetricHeatCapacity from a value in kilocalories_per_cubic_centimeter_degree_celsius.

        

        :param meters: The VolumetricHeatCapacity value in kilocalories_per_cubic_centimeter_degree_celsius.
        :type kilocalories_per_cubic_centimeter_degree_celsius: float
        :return: A new instance of VolumetricHeatCapacity.
        :rtype: VolumetricHeatCapacity
        """
        return VolumetricHeatCapacity(kilocalories_per_cubic_centimeter_degree_celsius, VolumetricHeatCapacityUnits.KilocaloriePerCubicCentimeterDegreeCelsius)

    
    @property
    def joules_per_cubic_meter_kelvin(self) -> float:
        """
        
        """
        if self.__joules_per_cubic_meter_kelvin != None:
            return self.__joules_per_cubic_meter_kelvin
        self.__joules_per_cubic_meter_kelvin = self.__convert_from_base(VolumetricHeatCapacityUnits.JoulePerCubicMeterKelvin)
        return self.__joules_per_cubic_meter_kelvin

    
    @property
    def joules_per_cubic_meter_degree_celsius(self) -> float:
        """
        
        """
        if self.__joules_per_cubic_meter_degree_celsius != None:
            return self.__joules_per_cubic_meter_degree_celsius
        self.__joules_per_cubic_meter_degree_celsius = self.__convert_from_base(VolumetricHeatCapacityUnits.JoulePerCubicMeterDegreeCelsius)
        return self.__joules_per_cubic_meter_degree_celsius

    
    @property
    def calories_per_cubic_centimeter_degree_celsius(self) -> float:
        """
        
        """
        if self.__calories_per_cubic_centimeter_degree_celsius != None:
            return self.__calories_per_cubic_centimeter_degree_celsius
        self.__calories_per_cubic_centimeter_degree_celsius = self.__convert_from_base(VolumetricHeatCapacityUnits.CaloriePerCubicCentimeterDegreeCelsius)
        return self.__calories_per_cubic_centimeter_degree_celsius

    
    @property
    def btus_per_cubic_foot_degree_fahrenheit(self) -> float:
        """
        
        """
        if self.__btus_per_cubic_foot_degree_fahrenheit != None:
            return self.__btus_per_cubic_foot_degree_fahrenheit
        self.__btus_per_cubic_foot_degree_fahrenheit = self.__convert_from_base(VolumetricHeatCapacityUnits.BtuPerCubicFootDegreeFahrenheit)
        return self.__btus_per_cubic_foot_degree_fahrenheit

    
    @property
    def kilojoules_per_cubic_meter_kelvin(self) -> float:
        """
        
        """
        if self.__kilojoules_per_cubic_meter_kelvin != None:
            return self.__kilojoules_per_cubic_meter_kelvin
        self.__kilojoules_per_cubic_meter_kelvin = self.__convert_from_base(VolumetricHeatCapacityUnits.KilojoulePerCubicMeterKelvin)
        return self.__kilojoules_per_cubic_meter_kelvin

    
    @property
    def megajoules_per_cubic_meter_kelvin(self) -> float:
        """
        
        """
        if self.__megajoules_per_cubic_meter_kelvin != None:
            return self.__megajoules_per_cubic_meter_kelvin
        self.__megajoules_per_cubic_meter_kelvin = self.__convert_from_base(VolumetricHeatCapacityUnits.MegajoulePerCubicMeterKelvin)
        return self.__megajoules_per_cubic_meter_kelvin

    
    @property
    def kilojoules_per_cubic_meter_degree_celsius(self) -> float:
        """
        
        """
        if self.__kilojoules_per_cubic_meter_degree_celsius != None:
            return self.__kilojoules_per_cubic_meter_degree_celsius
        self.__kilojoules_per_cubic_meter_degree_celsius = self.__convert_from_base(VolumetricHeatCapacityUnits.KilojoulePerCubicMeterDegreeCelsius)
        return self.__kilojoules_per_cubic_meter_degree_celsius

    
    @property
    def megajoules_per_cubic_meter_degree_celsius(self) -> float:
        """
        
        """
        if self.__megajoules_per_cubic_meter_degree_celsius != None:
            return self.__megajoules_per_cubic_meter_degree_celsius
        self.__megajoules_per_cubic_meter_degree_celsius = self.__convert_from_base(VolumetricHeatCapacityUnits.MegajoulePerCubicMeterDegreeCelsius)
        return self.__megajoules_per_cubic_meter_degree_celsius

    
    @property
    def kilocalories_per_cubic_centimeter_degree_celsius(self) -> float:
        """
        
        """
        if self.__kilocalories_per_cubic_centimeter_degree_celsius != None:
            return self.__kilocalories_per_cubic_centimeter_degree_celsius
        self.__kilocalories_per_cubic_centimeter_degree_celsius = self.__convert_from_base(VolumetricHeatCapacityUnits.KilocaloriePerCubicCentimeterDegreeCelsius)
        return self.__kilocalories_per_cubic_centimeter_degree_celsius

    
    def to_string(self, unit: VolumetricHeatCapacityUnits = VolumetricHeatCapacityUnits.JoulePerCubicMeterKelvin) -> str:
        """
        Format the VolumetricHeatCapacity to string.
        Note! the default format for VolumetricHeatCapacity is JoulePerCubicMeterKelvin.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == VolumetricHeatCapacityUnits.JoulePerCubicMeterKelvin:
            return f"""{self.joules_per_cubic_meter_kelvin} J/m³·K"""
        
        if unit == VolumetricHeatCapacityUnits.JoulePerCubicMeterDegreeCelsius:
            return f"""{self.joules_per_cubic_meter_degree_celsius} J/m³·°C"""
        
        if unit == VolumetricHeatCapacityUnits.CaloriePerCubicCentimeterDegreeCelsius:
            return f"""{self.calories_per_cubic_centimeter_degree_celsius} cal/cm³·°C"""
        
        if unit == VolumetricHeatCapacityUnits.BtuPerCubicFootDegreeFahrenheit:
            return f"""{self.btus_per_cubic_foot_degree_fahrenheit} BTU/ft³·°F"""
        
        if unit == VolumetricHeatCapacityUnits.KilojoulePerCubicMeterKelvin:
            return f"""{self.kilojoules_per_cubic_meter_kelvin} kJ/m³·K"""
        
        if unit == VolumetricHeatCapacityUnits.MegajoulePerCubicMeterKelvin:
            return f"""{self.megajoules_per_cubic_meter_kelvin} MJ/m³·K"""
        
        if unit == VolumetricHeatCapacityUnits.KilojoulePerCubicMeterDegreeCelsius:
            return f"""{self.kilojoules_per_cubic_meter_degree_celsius} kJ/m³·°C"""
        
        if unit == VolumetricHeatCapacityUnits.MegajoulePerCubicMeterDegreeCelsius:
            return f"""{self.megajoules_per_cubic_meter_degree_celsius} MJ/m³·°C"""
        
        if unit == VolumetricHeatCapacityUnits.KilocaloriePerCubicCentimeterDegreeCelsius:
            return f"""{self.kilocalories_per_cubic_centimeter_degree_celsius} kcal/cm³·°C"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: VolumetricHeatCapacityUnits = VolumetricHeatCapacityUnits.JoulePerCubicMeterKelvin) -> str:
        """
        Get VolumetricHeatCapacity unit abbreviation.
        Note! the default abbreviation for VolumetricHeatCapacity is JoulePerCubicMeterKelvin.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == VolumetricHeatCapacityUnits.JoulePerCubicMeterKelvin:
            return """J/m³·K"""
        
        if unit_abbreviation == VolumetricHeatCapacityUnits.JoulePerCubicMeterDegreeCelsius:
            return """J/m³·°C"""
        
        if unit_abbreviation == VolumetricHeatCapacityUnits.CaloriePerCubicCentimeterDegreeCelsius:
            return """cal/cm³·°C"""
        
        if unit_abbreviation == VolumetricHeatCapacityUnits.BtuPerCubicFootDegreeFahrenheit:
            return """BTU/ft³·°F"""
        
        if unit_abbreviation == VolumetricHeatCapacityUnits.KilojoulePerCubicMeterKelvin:
            return """kJ/m³·K"""
        
        if unit_abbreviation == VolumetricHeatCapacityUnits.MegajoulePerCubicMeterKelvin:
            return """MJ/m³·K"""
        
        if unit_abbreviation == VolumetricHeatCapacityUnits.KilojoulePerCubicMeterDegreeCelsius:
            return """kJ/m³·°C"""
        
        if unit_abbreviation == VolumetricHeatCapacityUnits.MegajoulePerCubicMeterDegreeCelsius:
            return """MJ/m³·°C"""
        
        if unit_abbreviation == VolumetricHeatCapacityUnits.KilocaloriePerCubicCentimeterDegreeCelsius:
            return """kcal/cm³·°C"""
        
from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class SpecificEntropyUnits(Enum):
        """
            SpecificEntropyUnits enumeration
        """
        
        JoulePerKilogramKelvin = 'joule_per_kilogram_kelvin'
        """
            
        """
        
        JoulePerKilogramDegreeCelsius = 'joule_per_kilogram_degree_celsius'
        """
            
        """
        
        CaloriePerGramKelvin = 'calorie_per_gram_kelvin'
        """
            
        """
        
        BtuPerPoundFahrenheit = 'btu_per_pound_fahrenheit'
        """
            
        """
        
        KilojoulePerKilogramKelvin = 'kilojoule_per_kilogram_kelvin'
        """
            
        """
        
        MegajoulePerKilogramKelvin = 'megajoule_per_kilogram_kelvin'
        """
            
        """
        
        KilojoulePerKilogramDegreeCelsius = 'kilojoule_per_kilogram_degree_celsius'
        """
            
        """
        
        MegajoulePerKilogramDegreeCelsius = 'megajoule_per_kilogram_degree_celsius'
        """
            
        """
        
        KilocaloriePerGramKelvin = 'kilocalorie_per_gram_kelvin'
        """
            
        """
        

class SpecificEntropy(AbstractMeasure):
    """
    Specific entropy is an amount of energy required to raise temperature of a substance by 1 Kelvin per unit mass.

    Args:
        value (float): The value.
        from_unit (SpecificEntropyUnits): The SpecificEntropy unit to create from, The default unit is JoulePerKilogramKelvin
    """
    def __init__(self, value: float, from_unit: SpecificEntropyUnits = SpecificEntropyUnits.JoulePerKilogramKelvin):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__joules_per_kilogram_kelvin = None
        
        self.__joules_per_kilogram_degree_celsius = None
        
        self.__calories_per_gram_kelvin = None
        
        self.__btus_per_pound_fahrenheit = None
        
        self.__kilojoules_per_kilogram_kelvin = None
        
        self.__megajoules_per_kilogram_kelvin = None
        
        self.__kilojoules_per_kilogram_degree_celsius = None
        
        self.__megajoules_per_kilogram_degree_celsius = None
        
        self.__kilocalories_per_gram_kelvin = None
        

    def convert(self, unit: SpecificEntropyUnits) -> float:
        return self.__convert_from_base(unit)

    def __convert_from_base(self, from_unit: SpecificEntropyUnits) -> float:
        value = self._value
        
        if from_unit == SpecificEntropyUnits.JoulePerKilogramKelvin:
            return (value)
        
        if from_unit == SpecificEntropyUnits.JoulePerKilogramDegreeCelsius:
            return (value)
        
        if from_unit == SpecificEntropyUnits.CaloriePerGramKelvin:
            return (value / 4.184e3)
        
        if from_unit == SpecificEntropyUnits.BtuPerPoundFahrenheit:
            return (value / 4.1868e3)
        
        if from_unit == SpecificEntropyUnits.KilojoulePerKilogramKelvin:
            return ((value) / 1000.0)
        
        if from_unit == SpecificEntropyUnits.MegajoulePerKilogramKelvin:
            return ((value) / 1000000.0)
        
        if from_unit == SpecificEntropyUnits.KilojoulePerKilogramDegreeCelsius:
            return ((value) / 1000.0)
        
        if from_unit == SpecificEntropyUnits.MegajoulePerKilogramDegreeCelsius:
            return ((value) / 1000000.0)
        
        if from_unit == SpecificEntropyUnits.KilocaloriePerGramKelvin:
            return ((value / 4.184e3) / 1000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: SpecificEntropyUnits) -> float:
        
        if to_unit == SpecificEntropyUnits.JoulePerKilogramKelvin:
            return (value)
        
        if to_unit == SpecificEntropyUnits.JoulePerKilogramDegreeCelsius:
            return (value)
        
        if to_unit == SpecificEntropyUnits.CaloriePerGramKelvin:
            return (value * 4.184e3)
        
        if to_unit == SpecificEntropyUnits.BtuPerPoundFahrenheit:
            return (value * 4.1868e3)
        
        if to_unit == SpecificEntropyUnits.KilojoulePerKilogramKelvin:
            return ((value) * 1000.0)
        
        if to_unit == SpecificEntropyUnits.MegajoulePerKilogramKelvin:
            return ((value) * 1000000.0)
        
        if to_unit == SpecificEntropyUnits.KilojoulePerKilogramDegreeCelsius:
            return ((value) * 1000.0)
        
        if to_unit == SpecificEntropyUnits.MegajoulePerKilogramDegreeCelsius:
            return ((value) * 1000000.0)
        
        if to_unit == SpecificEntropyUnits.KilocaloriePerGramKelvin:
            return ((value * 4.184e3) * 1000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_joules_per_kilogram_kelvin(joules_per_kilogram_kelvin: float):
        """
        Create a new instance of SpecificEntropy from a value in joules_per_kilogram_kelvin.

        

        :param meters: The SpecificEntropy value in joules_per_kilogram_kelvin.
        :type joules_per_kilogram_kelvin: float
        :return: A new instance of SpecificEntropy.
        :rtype: SpecificEntropy
        """
        return SpecificEntropy(joules_per_kilogram_kelvin, SpecificEntropyUnits.JoulePerKilogramKelvin)

    
    @staticmethod
    def from_joules_per_kilogram_degree_celsius(joules_per_kilogram_degree_celsius: float):
        """
        Create a new instance of SpecificEntropy from a value in joules_per_kilogram_degree_celsius.

        

        :param meters: The SpecificEntropy value in joules_per_kilogram_degree_celsius.
        :type joules_per_kilogram_degree_celsius: float
        :return: A new instance of SpecificEntropy.
        :rtype: SpecificEntropy
        """
        return SpecificEntropy(joules_per_kilogram_degree_celsius, SpecificEntropyUnits.JoulePerKilogramDegreeCelsius)

    
    @staticmethod
    def from_calories_per_gram_kelvin(calories_per_gram_kelvin: float):
        """
        Create a new instance of SpecificEntropy from a value in calories_per_gram_kelvin.

        

        :param meters: The SpecificEntropy value in calories_per_gram_kelvin.
        :type calories_per_gram_kelvin: float
        :return: A new instance of SpecificEntropy.
        :rtype: SpecificEntropy
        """
        return SpecificEntropy(calories_per_gram_kelvin, SpecificEntropyUnits.CaloriePerGramKelvin)

    
    @staticmethod
    def from_btus_per_pound_fahrenheit(btus_per_pound_fahrenheit: float):
        """
        Create a new instance of SpecificEntropy from a value in btus_per_pound_fahrenheit.

        

        :param meters: The SpecificEntropy value in btus_per_pound_fahrenheit.
        :type btus_per_pound_fahrenheit: float
        :return: A new instance of SpecificEntropy.
        :rtype: SpecificEntropy
        """
        return SpecificEntropy(btus_per_pound_fahrenheit, SpecificEntropyUnits.BtuPerPoundFahrenheit)

    
    @staticmethod
    def from_kilojoules_per_kilogram_kelvin(kilojoules_per_kilogram_kelvin: float):
        """
        Create a new instance of SpecificEntropy from a value in kilojoules_per_kilogram_kelvin.

        

        :param meters: The SpecificEntropy value in kilojoules_per_kilogram_kelvin.
        :type kilojoules_per_kilogram_kelvin: float
        :return: A new instance of SpecificEntropy.
        :rtype: SpecificEntropy
        """
        return SpecificEntropy(kilojoules_per_kilogram_kelvin, SpecificEntropyUnits.KilojoulePerKilogramKelvin)

    
    @staticmethod
    def from_megajoules_per_kilogram_kelvin(megajoules_per_kilogram_kelvin: float):
        """
        Create a new instance of SpecificEntropy from a value in megajoules_per_kilogram_kelvin.

        

        :param meters: The SpecificEntropy value in megajoules_per_kilogram_kelvin.
        :type megajoules_per_kilogram_kelvin: float
        :return: A new instance of SpecificEntropy.
        :rtype: SpecificEntropy
        """
        return SpecificEntropy(megajoules_per_kilogram_kelvin, SpecificEntropyUnits.MegajoulePerKilogramKelvin)

    
    @staticmethod
    def from_kilojoules_per_kilogram_degree_celsius(kilojoules_per_kilogram_degree_celsius: float):
        """
        Create a new instance of SpecificEntropy from a value in kilojoules_per_kilogram_degree_celsius.

        

        :param meters: The SpecificEntropy value in kilojoules_per_kilogram_degree_celsius.
        :type kilojoules_per_kilogram_degree_celsius: float
        :return: A new instance of SpecificEntropy.
        :rtype: SpecificEntropy
        """
        return SpecificEntropy(kilojoules_per_kilogram_degree_celsius, SpecificEntropyUnits.KilojoulePerKilogramDegreeCelsius)

    
    @staticmethod
    def from_megajoules_per_kilogram_degree_celsius(megajoules_per_kilogram_degree_celsius: float):
        """
        Create a new instance of SpecificEntropy from a value in megajoules_per_kilogram_degree_celsius.

        

        :param meters: The SpecificEntropy value in megajoules_per_kilogram_degree_celsius.
        :type megajoules_per_kilogram_degree_celsius: float
        :return: A new instance of SpecificEntropy.
        :rtype: SpecificEntropy
        """
        return SpecificEntropy(megajoules_per_kilogram_degree_celsius, SpecificEntropyUnits.MegajoulePerKilogramDegreeCelsius)

    
    @staticmethod
    def from_kilocalories_per_gram_kelvin(kilocalories_per_gram_kelvin: float):
        """
        Create a new instance of SpecificEntropy from a value in kilocalories_per_gram_kelvin.

        

        :param meters: The SpecificEntropy value in kilocalories_per_gram_kelvin.
        :type kilocalories_per_gram_kelvin: float
        :return: A new instance of SpecificEntropy.
        :rtype: SpecificEntropy
        """
        return SpecificEntropy(kilocalories_per_gram_kelvin, SpecificEntropyUnits.KilocaloriePerGramKelvin)

    
    @property
    def joules_per_kilogram_kelvin(self) -> float:
        """
        
        """
        if self.__joules_per_kilogram_kelvin != None:
            return self.__joules_per_kilogram_kelvin
        self.__joules_per_kilogram_kelvin = self.__convert_from_base(SpecificEntropyUnits.JoulePerKilogramKelvin)
        return self.__joules_per_kilogram_kelvin

    
    @property
    def joules_per_kilogram_degree_celsius(self) -> float:
        """
        
        """
        if self.__joules_per_kilogram_degree_celsius != None:
            return self.__joules_per_kilogram_degree_celsius
        self.__joules_per_kilogram_degree_celsius = self.__convert_from_base(SpecificEntropyUnits.JoulePerKilogramDegreeCelsius)
        return self.__joules_per_kilogram_degree_celsius

    
    @property
    def calories_per_gram_kelvin(self) -> float:
        """
        
        """
        if self.__calories_per_gram_kelvin != None:
            return self.__calories_per_gram_kelvin
        self.__calories_per_gram_kelvin = self.__convert_from_base(SpecificEntropyUnits.CaloriePerGramKelvin)
        return self.__calories_per_gram_kelvin

    
    @property
    def btus_per_pound_fahrenheit(self) -> float:
        """
        
        """
        if self.__btus_per_pound_fahrenheit != None:
            return self.__btus_per_pound_fahrenheit
        self.__btus_per_pound_fahrenheit = self.__convert_from_base(SpecificEntropyUnits.BtuPerPoundFahrenheit)
        return self.__btus_per_pound_fahrenheit

    
    @property
    def kilojoules_per_kilogram_kelvin(self) -> float:
        """
        
        """
        if self.__kilojoules_per_kilogram_kelvin != None:
            return self.__kilojoules_per_kilogram_kelvin
        self.__kilojoules_per_kilogram_kelvin = self.__convert_from_base(SpecificEntropyUnits.KilojoulePerKilogramKelvin)
        return self.__kilojoules_per_kilogram_kelvin

    
    @property
    def megajoules_per_kilogram_kelvin(self) -> float:
        """
        
        """
        if self.__megajoules_per_kilogram_kelvin != None:
            return self.__megajoules_per_kilogram_kelvin
        self.__megajoules_per_kilogram_kelvin = self.__convert_from_base(SpecificEntropyUnits.MegajoulePerKilogramKelvin)
        return self.__megajoules_per_kilogram_kelvin

    
    @property
    def kilojoules_per_kilogram_degree_celsius(self) -> float:
        """
        
        """
        if self.__kilojoules_per_kilogram_degree_celsius != None:
            return self.__kilojoules_per_kilogram_degree_celsius
        self.__kilojoules_per_kilogram_degree_celsius = self.__convert_from_base(SpecificEntropyUnits.KilojoulePerKilogramDegreeCelsius)
        return self.__kilojoules_per_kilogram_degree_celsius

    
    @property
    def megajoules_per_kilogram_degree_celsius(self) -> float:
        """
        
        """
        if self.__megajoules_per_kilogram_degree_celsius != None:
            return self.__megajoules_per_kilogram_degree_celsius
        self.__megajoules_per_kilogram_degree_celsius = self.__convert_from_base(SpecificEntropyUnits.MegajoulePerKilogramDegreeCelsius)
        return self.__megajoules_per_kilogram_degree_celsius

    
    @property
    def kilocalories_per_gram_kelvin(self) -> float:
        """
        
        """
        if self.__kilocalories_per_gram_kelvin != None:
            return self.__kilocalories_per_gram_kelvin
        self.__kilocalories_per_gram_kelvin = self.__convert_from_base(SpecificEntropyUnits.KilocaloriePerGramKelvin)
        return self.__kilocalories_per_gram_kelvin

    
    def to_string(self, unit: SpecificEntropyUnits = SpecificEntropyUnits.JoulePerKilogramKelvin) -> str:
        """
        Format the SpecificEntropy to string.
        Note! the default format for SpecificEntropy is JoulePerKilogramKelvin.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == SpecificEntropyUnits.JoulePerKilogramKelvin:
            return f"""{self.joules_per_kilogram_kelvin} J/kg.K"""
        
        if unit == SpecificEntropyUnits.JoulePerKilogramDegreeCelsius:
            return f"""{self.joules_per_kilogram_degree_celsius} J/kg.C"""
        
        if unit == SpecificEntropyUnits.CaloriePerGramKelvin:
            return f"""{self.calories_per_gram_kelvin} cal/g.K"""
        
        if unit == SpecificEntropyUnits.BtuPerPoundFahrenheit:
            return f"""{self.btus_per_pound_fahrenheit} BTU/lb·°F"""
        
        if unit == SpecificEntropyUnits.KilojoulePerKilogramKelvin:
            return f"""{self.kilojoules_per_kilogram_kelvin} kJ/kg.K"""
        
        if unit == SpecificEntropyUnits.MegajoulePerKilogramKelvin:
            return f"""{self.megajoules_per_kilogram_kelvin} MJ/kg.K"""
        
        if unit == SpecificEntropyUnits.KilojoulePerKilogramDegreeCelsius:
            return f"""{self.kilojoules_per_kilogram_degree_celsius} kJ/kg.C"""
        
        if unit == SpecificEntropyUnits.MegajoulePerKilogramDegreeCelsius:
            return f"""{self.megajoules_per_kilogram_degree_celsius} MJ/kg.C"""
        
        if unit == SpecificEntropyUnits.KilocaloriePerGramKelvin:
            return f"""{self.kilocalories_per_gram_kelvin} kcal/g.K"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: SpecificEntropyUnits = SpecificEntropyUnits.JoulePerKilogramKelvin) -> str:
        """
        Get SpecificEntropy unit abbreviation.
        Note! the default abbreviation for SpecificEntropy is JoulePerKilogramKelvin.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == SpecificEntropyUnits.JoulePerKilogramKelvin:
            return """J/kg.K"""
        
        if unit_abbreviation == SpecificEntropyUnits.JoulePerKilogramDegreeCelsius:
            return """J/kg.C"""
        
        if unit_abbreviation == SpecificEntropyUnits.CaloriePerGramKelvin:
            return """cal/g.K"""
        
        if unit_abbreviation == SpecificEntropyUnits.BtuPerPoundFahrenheit:
            return """BTU/lb·°F"""
        
        if unit_abbreviation == SpecificEntropyUnits.KilojoulePerKilogramKelvin:
            return """kJ/kg.K"""
        
        if unit_abbreviation == SpecificEntropyUnits.MegajoulePerKilogramKelvin:
            return """MJ/kg.K"""
        
        if unit_abbreviation == SpecificEntropyUnits.KilojoulePerKilogramDegreeCelsius:
            return """kJ/kg.C"""
        
        if unit_abbreviation == SpecificEntropyUnits.MegajoulePerKilogramDegreeCelsius:
            return """MJ/kg.C"""
        
        if unit_abbreviation == SpecificEntropyUnits.KilocaloriePerGramKelvin:
            return """kcal/g.K"""
        
from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class EntropyUnits(Enum):
        """
            EntropyUnits enumeration
        """
        
        JoulePerKelvin = 'joule_per_kelvin'
        """
            
        """
        
        CaloriePerKelvin = 'calorie_per_kelvin'
        """
            
        """
        
        JoulePerDegreeCelsius = 'joule_per_degree_celsius'
        """
            
        """
        
        KilojoulePerKelvin = 'kilojoule_per_kelvin'
        """
            
        """
        
        MegajoulePerKelvin = 'megajoule_per_kelvin'
        """
            
        """
        
        KilocaloriePerKelvin = 'kilocalorie_per_kelvin'
        """
            
        """
        
        KilojoulePerDegreeCelsius = 'kilojoule_per_degree_celsius'
        """
            
        """
        

class Entropy(AbstractMeasure):
    """
    Entropy is an important concept in the branch of science known as thermodynamics. The idea of "irreversibility" is central to the understanding of entropy.  It is often said that entropy is an expression of the disorder, or randomness of a system, or of our lack of information about it. Entropy is an extensive property. It has the dimension of energy divided by temperature, which has a unit of joules per kelvin (J/K) in the International System of Units

    Args:
        value (float): The value.
        from_unit (EntropyUnits): The Entropy unit to create from, The default unit is JoulePerKelvin
    """
    def __init__(self, value: float, from_unit: EntropyUnits = EntropyUnits.JoulePerKelvin):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__joules_per_kelvin = None
        
        self.__calories_per_kelvin = None
        
        self.__joules_per_degree_celsius = None
        
        self.__kilojoules_per_kelvin = None
        
        self.__megajoules_per_kelvin = None
        
        self.__kilocalories_per_kelvin = None
        
        self.__kilojoules_per_degree_celsius = None
        

    def convert(self, unit: EntropyUnits) -> float:
        return self.__convert_from_base(unit)

    def __convert_from_base(self, from_unit: EntropyUnits) -> float:
        value = self._value
        
        if from_unit == EntropyUnits.JoulePerKelvin:
            return (value)
        
        if from_unit == EntropyUnits.CaloriePerKelvin:
            return (value / 4.184)
        
        if from_unit == EntropyUnits.JoulePerDegreeCelsius:
            return (value)
        
        if from_unit == EntropyUnits.KilojoulePerKelvin:
            return ((value) / 1000.0)
        
        if from_unit == EntropyUnits.MegajoulePerKelvin:
            return ((value) / 1000000.0)
        
        if from_unit == EntropyUnits.KilocaloriePerKelvin:
            return ((value / 4.184) / 1000.0)
        
        if from_unit == EntropyUnits.KilojoulePerDegreeCelsius:
            return ((value) / 1000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: EntropyUnits) -> float:
        
        if to_unit == EntropyUnits.JoulePerKelvin:
            return (value)
        
        if to_unit == EntropyUnits.CaloriePerKelvin:
            return (value * 4.184)
        
        if to_unit == EntropyUnits.JoulePerDegreeCelsius:
            return (value)
        
        if to_unit == EntropyUnits.KilojoulePerKelvin:
            return ((value) * 1000.0)
        
        if to_unit == EntropyUnits.MegajoulePerKelvin:
            return ((value) * 1000000.0)
        
        if to_unit == EntropyUnits.KilocaloriePerKelvin:
            return ((value * 4.184) * 1000.0)
        
        if to_unit == EntropyUnits.KilojoulePerDegreeCelsius:
            return ((value) * 1000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_joules_per_kelvin(joules_per_kelvin: float):
        """
        Create a new instance of Entropy from a value in joules_per_kelvin.

        

        :param meters: The Entropy value in joules_per_kelvin.
        :type joules_per_kelvin: float
        :return: A new instance of Entropy.
        :rtype: Entropy
        """
        return Entropy(joules_per_kelvin, EntropyUnits.JoulePerKelvin)

    
    @staticmethod
    def from_calories_per_kelvin(calories_per_kelvin: float):
        """
        Create a new instance of Entropy from a value in calories_per_kelvin.

        

        :param meters: The Entropy value in calories_per_kelvin.
        :type calories_per_kelvin: float
        :return: A new instance of Entropy.
        :rtype: Entropy
        """
        return Entropy(calories_per_kelvin, EntropyUnits.CaloriePerKelvin)

    
    @staticmethod
    def from_joules_per_degree_celsius(joules_per_degree_celsius: float):
        """
        Create a new instance of Entropy from a value in joules_per_degree_celsius.

        

        :param meters: The Entropy value in joules_per_degree_celsius.
        :type joules_per_degree_celsius: float
        :return: A new instance of Entropy.
        :rtype: Entropy
        """
        return Entropy(joules_per_degree_celsius, EntropyUnits.JoulePerDegreeCelsius)

    
    @staticmethod
    def from_kilojoules_per_kelvin(kilojoules_per_kelvin: float):
        """
        Create a new instance of Entropy from a value in kilojoules_per_kelvin.

        

        :param meters: The Entropy value in kilojoules_per_kelvin.
        :type kilojoules_per_kelvin: float
        :return: A new instance of Entropy.
        :rtype: Entropy
        """
        return Entropy(kilojoules_per_kelvin, EntropyUnits.KilojoulePerKelvin)

    
    @staticmethod
    def from_megajoules_per_kelvin(megajoules_per_kelvin: float):
        """
        Create a new instance of Entropy from a value in megajoules_per_kelvin.

        

        :param meters: The Entropy value in megajoules_per_kelvin.
        :type megajoules_per_kelvin: float
        :return: A new instance of Entropy.
        :rtype: Entropy
        """
        return Entropy(megajoules_per_kelvin, EntropyUnits.MegajoulePerKelvin)

    
    @staticmethod
    def from_kilocalories_per_kelvin(kilocalories_per_kelvin: float):
        """
        Create a new instance of Entropy from a value in kilocalories_per_kelvin.

        

        :param meters: The Entropy value in kilocalories_per_kelvin.
        :type kilocalories_per_kelvin: float
        :return: A new instance of Entropy.
        :rtype: Entropy
        """
        return Entropy(kilocalories_per_kelvin, EntropyUnits.KilocaloriePerKelvin)

    
    @staticmethod
    def from_kilojoules_per_degree_celsius(kilojoules_per_degree_celsius: float):
        """
        Create a new instance of Entropy from a value in kilojoules_per_degree_celsius.

        

        :param meters: The Entropy value in kilojoules_per_degree_celsius.
        :type kilojoules_per_degree_celsius: float
        :return: A new instance of Entropy.
        :rtype: Entropy
        """
        return Entropy(kilojoules_per_degree_celsius, EntropyUnits.KilojoulePerDegreeCelsius)

    
    @property
    def joules_per_kelvin(self) -> float:
        """
        
        """
        if self.__joules_per_kelvin != None:
            return self.__joules_per_kelvin
        self.__joules_per_kelvin = self.__convert_from_base(EntropyUnits.JoulePerKelvin)
        return self.__joules_per_kelvin

    
    @property
    def calories_per_kelvin(self) -> float:
        """
        
        """
        if self.__calories_per_kelvin != None:
            return self.__calories_per_kelvin
        self.__calories_per_kelvin = self.__convert_from_base(EntropyUnits.CaloriePerKelvin)
        return self.__calories_per_kelvin

    
    @property
    def joules_per_degree_celsius(self) -> float:
        """
        
        """
        if self.__joules_per_degree_celsius != None:
            return self.__joules_per_degree_celsius
        self.__joules_per_degree_celsius = self.__convert_from_base(EntropyUnits.JoulePerDegreeCelsius)
        return self.__joules_per_degree_celsius

    
    @property
    def kilojoules_per_kelvin(self) -> float:
        """
        
        """
        if self.__kilojoules_per_kelvin != None:
            return self.__kilojoules_per_kelvin
        self.__kilojoules_per_kelvin = self.__convert_from_base(EntropyUnits.KilojoulePerKelvin)
        return self.__kilojoules_per_kelvin

    
    @property
    def megajoules_per_kelvin(self) -> float:
        """
        
        """
        if self.__megajoules_per_kelvin != None:
            return self.__megajoules_per_kelvin
        self.__megajoules_per_kelvin = self.__convert_from_base(EntropyUnits.MegajoulePerKelvin)
        return self.__megajoules_per_kelvin

    
    @property
    def kilocalories_per_kelvin(self) -> float:
        """
        
        """
        if self.__kilocalories_per_kelvin != None:
            return self.__kilocalories_per_kelvin
        self.__kilocalories_per_kelvin = self.__convert_from_base(EntropyUnits.KilocaloriePerKelvin)
        return self.__kilocalories_per_kelvin

    
    @property
    def kilojoules_per_degree_celsius(self) -> float:
        """
        
        """
        if self.__kilojoules_per_degree_celsius != None:
            return self.__kilojoules_per_degree_celsius
        self.__kilojoules_per_degree_celsius = self.__convert_from_base(EntropyUnits.KilojoulePerDegreeCelsius)
        return self.__kilojoules_per_degree_celsius

    
    def to_string(self, unit: EntropyUnits = EntropyUnits.JoulePerKelvin) -> str:
        """
        Format the Entropy to string.
        Note! the default format for Entropy is JoulePerKelvin.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == EntropyUnits.JoulePerKelvin:
            return f"""{self.joules_per_kelvin} J/K"""
        
        if unit == EntropyUnits.CaloriePerKelvin:
            return f"""{self.calories_per_kelvin} cal/K"""
        
        if unit == EntropyUnits.JoulePerDegreeCelsius:
            return f"""{self.joules_per_degree_celsius} J/C"""
        
        if unit == EntropyUnits.KilojoulePerKelvin:
            return f"""{self.kilojoules_per_kelvin} kJ/K"""
        
        if unit == EntropyUnits.MegajoulePerKelvin:
            return f"""{self.megajoules_per_kelvin} MJ/K"""
        
        if unit == EntropyUnits.KilocaloriePerKelvin:
            return f"""{self.kilocalories_per_kelvin} kcal/K"""
        
        if unit == EntropyUnits.KilojoulePerDegreeCelsius:
            return f"""{self.kilojoules_per_degree_celsius} kJ/C"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: EntropyUnits = EntropyUnits.JoulePerKelvin) -> str:
        """
        Get Entropy unit abbreviation.
        Note! the default abbreviation for Entropy is JoulePerKelvin.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == EntropyUnits.JoulePerKelvin:
            return """J/K"""
        
        if unit_abbreviation == EntropyUnits.CaloriePerKelvin:
            return """cal/K"""
        
        if unit_abbreviation == EntropyUnits.JoulePerDegreeCelsius:
            return """J/C"""
        
        if unit_abbreviation == EntropyUnits.KilojoulePerKelvin:
            return """kJ/K"""
        
        if unit_abbreviation == EntropyUnits.MegajoulePerKelvin:
            return """MJ/K"""
        
        if unit_abbreviation == EntropyUnits.KilocaloriePerKelvin:
            return """kcal/K"""
        
        if unit_abbreviation == EntropyUnits.KilojoulePerDegreeCelsius:
            return """kJ/C"""
        
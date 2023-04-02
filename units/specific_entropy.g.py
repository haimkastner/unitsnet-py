from enum import Enum
import math
import string


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
        
        KiloJoulePerKilogramKelvin = 'kilo_joule_per_kilogram_kelvin'
        """
            
        """
        
        MegaJoulePerKilogramKelvin = 'mega_joule_per_kilogram_kelvin'
        """
            
        """
        
        KiloJoulePerKilogramDegreeCelsius = 'kilo_joule_per_kilogram_degree_celsius'
        """
            
        """
        
        MegaJoulePerKilogramDegreeCelsius = 'mega_joule_per_kilogram_degree_celsius'
        """
            
        """
        
        KiloCaloriePerGramKelvin = 'kilo_calorie_per_gram_kelvin'
        """
            
        """
        
    
class SpecificEntropy:
    """
    Specific entropy is an amount of energy required to raise temperature of a substance by 1 Kelvin per unit mass.

    Args:
        value (float): The value.
        from_unit (SpecificEntropyUnits): The SpecificEntropy unit to create from, The default unit is JoulePerKilogramKelvin
    """
    def __init__(self, value: float, from_unit: SpecificEntropyUnits = SpecificEntropyUnits.JoulePerKilogramKelvin):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__joules_per_kilogram_kelvin = None
        
        self.__joules_per_kilogram_degree_celsius = None
        
        self.__calories_per_gram_kelvin = None
        
        self.__btus_per_pound_fahrenheit = None
        
        self.__kilo_joules_per_kilogram_kelvin = None
        
        self.__mega_joules_per_kilogram_kelvin = None
        
        self.__kilo_joules_per_kilogram_degree_celsius = None
        
        self.__mega_joules_per_kilogram_degree_celsius = None
        
        self.__kilo_calories_per_gram_kelvin = None
        

    def __convert_from_base(self, from_unit: SpecificEntropyUnits) -> float:
        value = self.__value
        
        if from_unit == SpecificEntropyUnits.JoulePerKilogramKelvin:
            return (value)
        
        if from_unit == SpecificEntropyUnits.JoulePerKilogramDegreeCelsius:
            return (value)
        
        if from_unit == SpecificEntropyUnits.CaloriePerGramKelvin:
            return (value / 4.184e3)
        
        if from_unit == SpecificEntropyUnits.BtuPerPoundFahrenheit:
            return (value / 4.1868e3)
        
        if from_unit == SpecificEntropyUnits.KiloJoulePerKilogramKelvin:
            return ((value) / 1000.0)
        
        if from_unit == SpecificEntropyUnits.MegaJoulePerKilogramKelvin:
            return ((value) / 1000000.0)
        
        if from_unit == SpecificEntropyUnits.KiloJoulePerKilogramDegreeCelsius:
            return ((value) / 1000.0)
        
        if from_unit == SpecificEntropyUnits.MegaJoulePerKilogramDegreeCelsius:
            return ((value) / 1000000.0)
        
        if from_unit == SpecificEntropyUnits.KiloCaloriePerGramKelvin:
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
        
        if to_unit == SpecificEntropyUnits.KiloJoulePerKilogramKelvin:
            return ((value) * 1000.0)
        
        if to_unit == SpecificEntropyUnits.MegaJoulePerKilogramKelvin:
            return ((value) * 1000000.0)
        
        if to_unit == SpecificEntropyUnits.KiloJoulePerKilogramDegreeCelsius:
            return ((value) * 1000.0)
        
        if to_unit == SpecificEntropyUnits.MegaJoulePerKilogramDegreeCelsius:
            return ((value) * 1000000.0)
        
        if to_unit == SpecificEntropyUnits.KiloCaloriePerGramKelvin:
            return ((value * 4.184e3) * 1000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
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
    def from_kilo_joules_per_kilogram_kelvin(kilo_joules_per_kilogram_kelvin: float):
        """
        Create a new instance of SpecificEntropy from a value in kilo_joules_per_kilogram_kelvin.

        

        :param meters: The SpecificEntropy value in kilo_joules_per_kilogram_kelvin.
        :type kilo_joules_per_kilogram_kelvin: float
        :return: A new instance of SpecificEntropy.
        :rtype: SpecificEntropy
        """
        return SpecificEntropy(kilo_joules_per_kilogram_kelvin, SpecificEntropyUnits.KiloJoulePerKilogramKelvin)

    
    @staticmethod
    def from_mega_joules_per_kilogram_kelvin(mega_joules_per_kilogram_kelvin: float):
        """
        Create a new instance of SpecificEntropy from a value in mega_joules_per_kilogram_kelvin.

        

        :param meters: The SpecificEntropy value in mega_joules_per_kilogram_kelvin.
        :type mega_joules_per_kilogram_kelvin: float
        :return: A new instance of SpecificEntropy.
        :rtype: SpecificEntropy
        """
        return SpecificEntropy(mega_joules_per_kilogram_kelvin, SpecificEntropyUnits.MegaJoulePerKilogramKelvin)

    
    @staticmethod
    def from_kilo_joules_per_kilogram_degree_celsius(kilo_joules_per_kilogram_degree_celsius: float):
        """
        Create a new instance of SpecificEntropy from a value in kilo_joules_per_kilogram_degree_celsius.

        

        :param meters: The SpecificEntropy value in kilo_joules_per_kilogram_degree_celsius.
        :type kilo_joules_per_kilogram_degree_celsius: float
        :return: A new instance of SpecificEntropy.
        :rtype: SpecificEntropy
        """
        return SpecificEntropy(kilo_joules_per_kilogram_degree_celsius, SpecificEntropyUnits.KiloJoulePerKilogramDegreeCelsius)

    
    @staticmethod
    def from_mega_joules_per_kilogram_degree_celsius(mega_joules_per_kilogram_degree_celsius: float):
        """
        Create a new instance of SpecificEntropy from a value in mega_joules_per_kilogram_degree_celsius.

        

        :param meters: The SpecificEntropy value in mega_joules_per_kilogram_degree_celsius.
        :type mega_joules_per_kilogram_degree_celsius: float
        :return: A new instance of SpecificEntropy.
        :rtype: SpecificEntropy
        """
        return SpecificEntropy(mega_joules_per_kilogram_degree_celsius, SpecificEntropyUnits.MegaJoulePerKilogramDegreeCelsius)

    
    @staticmethod
    def from_kilo_calories_per_gram_kelvin(kilo_calories_per_gram_kelvin: float):
        """
        Create a new instance of SpecificEntropy from a value in kilo_calories_per_gram_kelvin.

        

        :param meters: The SpecificEntropy value in kilo_calories_per_gram_kelvin.
        :type kilo_calories_per_gram_kelvin: float
        :return: A new instance of SpecificEntropy.
        :rtype: SpecificEntropy
        """
        return SpecificEntropy(kilo_calories_per_gram_kelvin, SpecificEntropyUnits.KiloCaloriePerGramKelvin)

    
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
    def kilo_joules_per_kilogram_kelvin(self) -> float:
        """
        
        """
        if self.__kilo_joules_per_kilogram_kelvin != None:
            return self.__kilo_joules_per_kilogram_kelvin
        self.__kilo_joules_per_kilogram_kelvin = self.__convert_from_base(SpecificEntropyUnits.KiloJoulePerKilogramKelvin)
        return self.__kilo_joules_per_kilogram_kelvin

    
    @property
    def mega_joules_per_kilogram_kelvin(self) -> float:
        """
        
        """
        if self.__mega_joules_per_kilogram_kelvin != None:
            return self.__mega_joules_per_kilogram_kelvin
        self.__mega_joules_per_kilogram_kelvin = self.__convert_from_base(SpecificEntropyUnits.MegaJoulePerKilogramKelvin)
        return self.__mega_joules_per_kilogram_kelvin

    
    @property
    def kilo_joules_per_kilogram_degree_celsius(self) -> float:
        """
        
        """
        if self.__kilo_joules_per_kilogram_degree_celsius != None:
            return self.__kilo_joules_per_kilogram_degree_celsius
        self.__kilo_joules_per_kilogram_degree_celsius = self.__convert_from_base(SpecificEntropyUnits.KiloJoulePerKilogramDegreeCelsius)
        return self.__kilo_joules_per_kilogram_degree_celsius

    
    @property
    def mega_joules_per_kilogram_degree_celsius(self) -> float:
        """
        
        """
        if self.__mega_joules_per_kilogram_degree_celsius != None:
            return self.__mega_joules_per_kilogram_degree_celsius
        self.__mega_joules_per_kilogram_degree_celsius = self.__convert_from_base(SpecificEntropyUnits.MegaJoulePerKilogramDegreeCelsius)
        return self.__mega_joules_per_kilogram_degree_celsius

    
    @property
    def kilo_calories_per_gram_kelvin(self) -> float:
        """
        
        """
        if self.__kilo_calories_per_gram_kelvin != None:
            return self.__kilo_calories_per_gram_kelvin
        self.__kilo_calories_per_gram_kelvin = self.__convert_from_base(SpecificEntropyUnits.KiloCaloriePerGramKelvin)
        return self.__kilo_calories_per_gram_kelvin

    
    def to_string(self, unit: SpecificEntropyUnits = SpecificEntropyUnits.JoulePerKilogramKelvin) -> string:
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
        
        if unit == SpecificEntropyUnits.KiloJoulePerKilogramKelvin:
            return f"""{self.kilo_joules_per_kilogram_kelvin} """
        
        if unit == SpecificEntropyUnits.MegaJoulePerKilogramKelvin:
            return f"""{self.mega_joules_per_kilogram_kelvin} """
        
        if unit == SpecificEntropyUnits.KiloJoulePerKilogramDegreeCelsius:
            return f"""{self.kilo_joules_per_kilogram_degree_celsius} """
        
        if unit == SpecificEntropyUnits.MegaJoulePerKilogramDegreeCelsius:
            return f"""{self.mega_joules_per_kilogram_degree_celsius} """
        
        if unit == SpecificEntropyUnits.KiloCaloriePerGramKelvin:
            return f"""{self.kilo_calories_per_gram_kelvin} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: SpecificEntropyUnits = SpecificEntropyUnits.JoulePerKilogramKelvin) -> string:
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
        
        if unit_abbreviation == SpecificEntropyUnits.KiloJoulePerKilogramKelvin:
            return """"""
        
        if unit_abbreviation == SpecificEntropyUnits.MegaJoulePerKilogramKelvin:
            return """"""
        
        if unit_abbreviation == SpecificEntropyUnits.KiloJoulePerKilogramDegreeCelsius:
            return """"""
        
        if unit_abbreviation == SpecificEntropyUnits.MegaJoulePerKilogramDegreeCelsius:
            return """"""
        
        if unit_abbreviation == SpecificEntropyUnits.KiloCaloriePerGramKelvin:
            return """"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, SpecificEntropy):
            raise TypeError("unsupported operand type(s) for +: 'SpecificEntropy' and '{}'".format(type(other).__name__))
        return SpecificEntropy(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, SpecificEntropy):
            raise TypeError("unsupported operand type(s) for *: 'SpecificEntropy' and '{}'".format(type(other).__name__))
        return SpecificEntropy(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, SpecificEntropy):
            raise TypeError("unsupported operand type(s) for -: 'SpecificEntropy' and '{}'".format(type(other).__name__))
        return SpecificEntropy(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, SpecificEntropy):
            raise TypeError("unsupported operand type(s) for /: 'SpecificEntropy' and '{}'".format(type(other).__name__))
        return SpecificEntropy(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, SpecificEntropy):
            raise TypeError("unsupported operand type(s) for %: 'SpecificEntropy' and '{}'".format(type(other).__name__))
        return SpecificEntropy(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, SpecificEntropy):
            raise TypeError("unsupported operand type(s) for **: 'SpecificEntropy' and '{}'".format(type(other).__name__))
        return SpecificEntropy(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, SpecificEntropy):
            raise TypeError("unsupported operand type(s) for ==: 'SpecificEntropy' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, SpecificEntropy):
            raise TypeError("unsupported operand type(s) for <: 'SpecificEntropy' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, SpecificEntropy):
            raise TypeError("unsupported operand type(s) for >: 'SpecificEntropy' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, SpecificEntropy):
            raise TypeError("unsupported operand type(s) for <=: 'SpecificEntropy' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, SpecificEntropy):
            raise TypeError("unsupported operand type(s) for >=: 'SpecificEntropy' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value
from enum import Enum
import math
import string


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
        
        KiloJoulePerKelvin = 'kilo_joule_per_kelvin'
        """
            
        """
        
        MegaJoulePerKelvin = 'mega_joule_per_kelvin'
        """
            
        """
        
        KiloCaloriePerKelvin = 'kilo_calorie_per_kelvin'
        """
            
        """
        
        KiloJoulePerDegreeCelsius = 'kilo_joule_per_degree_celsius'
        """
            
        """
        
    
class Entropy:
    """
    Entropy is an important concept in the branch of science known as thermodynamics. The idea of "irreversibility" is central to the understanding of entropy.  It is often said that entropy is an expression of the disorder, or randomness of a system, or of our lack of information about it. Entropy is an extensive property. It has the dimension of energy divided by temperature, which has a unit of joules per kelvin (J/K) in the International System of Units

    Args:
        value (float): The value.
        from_unit (EntropyUnits): The Entropy unit to create from, The default unit is JoulePerKelvin
    """
    def __init__(self, value: float, from_unit: EntropyUnits = EntropyUnits.JoulePerKelvin):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__joules_per_kelvin = None
        
        self.__calories_per_kelvin = None
        
        self.__joules_per_degree_celsius = None
        
        self.__kilo_joules_per_kelvin = None
        
        self.__mega_joules_per_kelvin = None
        
        self.__kilo_calories_per_kelvin = None
        
        self.__kilo_joules_per_degree_celsius = None
        

    def __convert_from_base(self, from_unit: EntropyUnits) -> float:
        value = self.__value
        
        if from_unit == EntropyUnits.JoulePerKelvin:
            return (value)
        
        if from_unit == EntropyUnits.CaloriePerKelvin:
            return (value / 4.184)
        
        if from_unit == EntropyUnits.JoulePerDegreeCelsius:
            return (value)
        
        if from_unit == EntropyUnits.KiloJoulePerKelvin:
            return ((value) / 1000.0)
        
        if from_unit == EntropyUnits.MegaJoulePerKelvin:
            return ((value) / 1000000.0)
        
        if from_unit == EntropyUnits.KiloCaloriePerKelvin:
            return ((value / 4.184) / 1000.0)
        
        if from_unit == EntropyUnits.KiloJoulePerDegreeCelsius:
            return ((value) / 1000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: EntropyUnits) -> float:
        
        if to_unit == EntropyUnits.JoulePerKelvin:
            return (value)
        
        if to_unit == EntropyUnits.CaloriePerKelvin:
            return (value * 4.184)
        
        if to_unit == EntropyUnits.JoulePerDegreeCelsius:
            return (value)
        
        if to_unit == EntropyUnits.KiloJoulePerKelvin:
            return ((value) * 1000.0)
        
        if to_unit == EntropyUnits.MegaJoulePerKelvin:
            return ((value) * 1000000.0)
        
        if to_unit == EntropyUnits.KiloCaloriePerKelvin:
            return ((value * 4.184) * 1000.0)
        
        if to_unit == EntropyUnits.KiloJoulePerDegreeCelsius:
            return ((value) * 1000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
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
    def from_kilo_joules_per_kelvin(kilo_joules_per_kelvin: float):
        """
        Create a new instance of Entropy from a value in kilo_joules_per_kelvin.

        

        :param meters: The Entropy value in kilo_joules_per_kelvin.
        :type kilo_joules_per_kelvin: float
        :return: A new instance of Entropy.
        :rtype: Entropy
        """
        return Entropy(kilo_joules_per_kelvin, EntropyUnits.KiloJoulePerKelvin)

    
    @staticmethod
    def from_mega_joules_per_kelvin(mega_joules_per_kelvin: float):
        """
        Create a new instance of Entropy from a value in mega_joules_per_kelvin.

        

        :param meters: The Entropy value in mega_joules_per_kelvin.
        :type mega_joules_per_kelvin: float
        :return: A new instance of Entropy.
        :rtype: Entropy
        """
        return Entropy(mega_joules_per_kelvin, EntropyUnits.MegaJoulePerKelvin)

    
    @staticmethod
    def from_kilo_calories_per_kelvin(kilo_calories_per_kelvin: float):
        """
        Create a new instance of Entropy from a value in kilo_calories_per_kelvin.

        

        :param meters: The Entropy value in kilo_calories_per_kelvin.
        :type kilo_calories_per_kelvin: float
        :return: A new instance of Entropy.
        :rtype: Entropy
        """
        return Entropy(kilo_calories_per_kelvin, EntropyUnits.KiloCaloriePerKelvin)

    
    @staticmethod
    def from_kilo_joules_per_degree_celsius(kilo_joules_per_degree_celsius: float):
        """
        Create a new instance of Entropy from a value in kilo_joules_per_degree_celsius.

        

        :param meters: The Entropy value in kilo_joules_per_degree_celsius.
        :type kilo_joules_per_degree_celsius: float
        :return: A new instance of Entropy.
        :rtype: Entropy
        """
        return Entropy(kilo_joules_per_degree_celsius, EntropyUnits.KiloJoulePerDegreeCelsius)

    
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
    def kilo_joules_per_kelvin(self) -> float:
        """
        
        """
        if self.__kilo_joules_per_kelvin != None:
            return self.__kilo_joules_per_kelvin
        self.__kilo_joules_per_kelvin = self.__convert_from_base(EntropyUnits.KiloJoulePerKelvin)
        return self.__kilo_joules_per_kelvin

    
    @property
    def mega_joules_per_kelvin(self) -> float:
        """
        
        """
        if self.__mega_joules_per_kelvin != None:
            return self.__mega_joules_per_kelvin
        self.__mega_joules_per_kelvin = self.__convert_from_base(EntropyUnits.MegaJoulePerKelvin)
        return self.__mega_joules_per_kelvin

    
    @property
    def kilo_calories_per_kelvin(self) -> float:
        """
        
        """
        if self.__kilo_calories_per_kelvin != None:
            return self.__kilo_calories_per_kelvin
        self.__kilo_calories_per_kelvin = self.__convert_from_base(EntropyUnits.KiloCaloriePerKelvin)
        return self.__kilo_calories_per_kelvin

    
    @property
    def kilo_joules_per_degree_celsius(self) -> float:
        """
        
        """
        if self.__kilo_joules_per_degree_celsius != None:
            return self.__kilo_joules_per_degree_celsius
        self.__kilo_joules_per_degree_celsius = self.__convert_from_base(EntropyUnits.KiloJoulePerDegreeCelsius)
        return self.__kilo_joules_per_degree_celsius

    
    def to_string(self, unit: EntropyUnits = EntropyUnits.JoulePerKelvin) -> string:
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
        
        if unit == EntropyUnits.KiloJoulePerKelvin:
            return f"""{self.kilo_joules_per_kelvin} """
        
        if unit == EntropyUnits.MegaJoulePerKelvin:
            return f"""{self.mega_joules_per_kelvin} """
        
        if unit == EntropyUnits.KiloCaloriePerKelvin:
            return f"""{self.kilo_calories_per_kelvin} """
        
        if unit == EntropyUnits.KiloJoulePerDegreeCelsius:
            return f"""{self.kilo_joules_per_degree_celsius} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: EntropyUnits = EntropyUnits.JoulePerKelvin) -> string:
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
        
        if unit_abbreviation == EntropyUnits.KiloJoulePerKelvin:
            return """"""
        
        if unit_abbreviation == EntropyUnits.MegaJoulePerKelvin:
            return """"""
        
        if unit_abbreviation == EntropyUnits.KiloCaloriePerKelvin:
            return """"""
        
        if unit_abbreviation == EntropyUnits.KiloJoulePerDegreeCelsius:
            return """"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, Entropy):
            raise TypeError("unsupported operand type(s) for +: 'Entropy' and '{}'".format(type(other).__name__))
        return Entropy(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, Entropy):
            raise TypeError("unsupported operand type(s) for *: 'Entropy' and '{}'".format(type(other).__name__))
        return Entropy(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, Entropy):
            raise TypeError("unsupported operand type(s) for -: 'Entropy' and '{}'".format(type(other).__name__))
        return Entropy(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, Entropy):
            raise TypeError("unsupported operand type(s) for /: 'Entropy' and '{}'".format(type(other).__name__))
        return Entropy(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, Entropy):
            raise TypeError("unsupported operand type(s) for %: 'Entropy' and '{}'".format(type(other).__name__))
        return Entropy(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, Entropy):
            raise TypeError("unsupported operand type(s) for **: 'Entropy' and '{}'".format(type(other).__name__))
        return Entropy(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, Entropy):
            raise TypeError("unsupported operand type(s) for ==: 'Entropy' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, Entropy):
            raise TypeError("unsupported operand type(s) for <: 'Entropy' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, Entropy):
            raise TypeError("unsupported operand type(s) for >: 'Entropy' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, Entropy):
            raise TypeError("unsupported operand type(s) for <=: 'Entropy' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, Entropy):
            raise TypeError("unsupported operand type(s) for >=: 'Entropy' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value
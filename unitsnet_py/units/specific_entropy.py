from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class SpecificEntropyUnits(Enum):
        """
            SpecificEntropyUnits enumeration
        """
        
        JoulePerKilogramKelvin = 'JoulePerKilogramKelvin'
        """
            
        """
        
        JoulePerKilogramDegreeCelsius = 'JoulePerKilogramDegreeCelsius'
        """
            
        """
        
        CaloriePerGramKelvin = 'CaloriePerGramKelvin'
        """
            
        """
        
        BtuPerPoundFahrenheit = 'BtuPerPoundFahrenheit'
        """
            
        """
        
        KilojoulePerKilogramKelvin = 'KilojoulePerKilogramKelvin'
        """
            
        """
        
        MegajoulePerKilogramKelvin = 'MegajoulePerKilogramKelvin'
        """
            
        """
        
        KilojoulePerKilogramDegreeCelsius = 'KilojoulePerKilogramDegreeCelsius'
        """
            
        """
        
        MegajoulePerKilogramDegreeCelsius = 'MegajoulePerKilogramDegreeCelsius'
        """
            
        """
        
        KilocaloriePerGramKelvin = 'KilocaloriePerGramKelvin'
        """
            
        """
        

class SpecificEntropyDto:
    """
    A DTO representation of a SpecificEntropy

    Attributes:
        value (float): The value of the SpecificEntropy.
        unit (SpecificEntropyUnits): The specific unit that the SpecificEntropy value is representing.
    """

    def __init__(self, value: float, unit: SpecificEntropyUnits):
        """
        Create a new DTO representation of a SpecificEntropy

        Parameters:
            value (float): The value of the SpecificEntropy.
            unit (SpecificEntropyUnits): The specific unit that the SpecificEntropy value is representing.
        """
        self.value: float = value
        """
        The value of the SpecificEntropy
        """
        self.unit: SpecificEntropyUnits = unit
        """
        The specific unit that the SpecificEntropy value is representing
        """

    def to_json(self):
        """
        Get a SpecificEntropy DTO JSON object representing the current unit.

        :return: JSON object represents SpecificEntropy DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "JoulePerKilogramKelvin"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of SpecificEntropy DTO from a json representation.

        :param data: The SpecificEntropy DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "JoulePerKilogramKelvin"}
        :return: A new instance of SpecificEntropyDto.
        :rtype: SpecificEntropyDto
        """
        return SpecificEntropyDto(value=data["value"], unit=SpecificEntropyUnits(data["unit"]))


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

    def to_dto(self, hold_in_unit: SpecificEntropyUnits = SpecificEntropyUnits.JoulePerKilogramKelvin) -> SpecificEntropyDto:
        """
        Get a new instance of SpecificEntropy DTO representing the current unit.

        :param hold_in_unit: The specific SpecificEntropy unit to store the SpecificEntropy value in the DTO representation.
        :type hold_in_unit: SpecificEntropyUnits
        :return: A new instance of SpecificEntropyDto.
        :rtype: SpecificEntropyDto
        """
        return SpecificEntropyDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: SpecificEntropyUnits = SpecificEntropyUnits.JoulePerKilogramKelvin):
        """
        Get a SpecificEntropy DTO JSON object representing the current unit.

        :param hold_in_unit: The specific SpecificEntropy unit to store the SpecificEntropy value in the DTO representation.
        :type hold_in_unit: SpecificEntropyUnits
        :return: JSON object represents SpecificEntropy DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "JoulePerKilogramKelvin"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(specific_entropy_dto: SpecificEntropyDto):
        """
        Obtain a new instance of SpecificEntropy from a DTO unit object.

        :param specific_entropy_dto: The SpecificEntropy DTO representation.
        :type specific_entropy_dto: SpecificEntropyDto
        :return: A new instance of SpecificEntropy.
        :rtype: SpecificEntropy
        """
        return SpecificEntropy(specific_entropy_dto.value, specific_entropy_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of SpecificEntropy from a DTO unit json representation.

        :param data: The SpecificEntropy DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "JoulePerKilogramKelvin"}
        :return: A new instance of SpecificEntropy.
        :rtype: SpecificEntropy
        """
        return SpecificEntropy.from_dto(SpecificEntropyDto.from_json(data))

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

    
    def to_string(self, unit: SpecificEntropyUnits = SpecificEntropyUnits.JoulePerKilogramKelvin, fractional_digits: int = None) -> str:
        """
        Format the SpecificEntropy to a string.
        
        Note: the default format for SpecificEntropy is JoulePerKilogramKelvin.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the SpecificEntropy. Default is 'JoulePerKilogramKelvin'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == SpecificEntropyUnits.JoulePerKilogramKelvin:
            return f"""{super()._truncate_fraction_digits(self.joules_per_kilogram_kelvin, fractional_digits)} J/kg.K"""
        
        if unit == SpecificEntropyUnits.JoulePerKilogramDegreeCelsius:
            return f"""{super()._truncate_fraction_digits(self.joules_per_kilogram_degree_celsius, fractional_digits)} J/kg.C"""
        
        if unit == SpecificEntropyUnits.CaloriePerGramKelvin:
            return f"""{super()._truncate_fraction_digits(self.calories_per_gram_kelvin, fractional_digits)} cal/g.K"""
        
        if unit == SpecificEntropyUnits.BtuPerPoundFahrenheit:
            return f"""{super()._truncate_fraction_digits(self.btus_per_pound_fahrenheit, fractional_digits)} BTU/lb·°F"""
        
        if unit == SpecificEntropyUnits.KilojoulePerKilogramKelvin:
            return f"""{super()._truncate_fraction_digits(self.kilojoules_per_kilogram_kelvin, fractional_digits)} kJ/kg.K"""
        
        if unit == SpecificEntropyUnits.MegajoulePerKilogramKelvin:
            return f"""{super()._truncate_fraction_digits(self.megajoules_per_kilogram_kelvin, fractional_digits)} MJ/kg.K"""
        
        if unit == SpecificEntropyUnits.KilojoulePerKilogramDegreeCelsius:
            return f"""{super()._truncate_fraction_digits(self.kilojoules_per_kilogram_degree_celsius, fractional_digits)} kJ/kg.C"""
        
        if unit == SpecificEntropyUnits.MegajoulePerKilogramDegreeCelsius:
            return f"""{super()._truncate_fraction_digits(self.megajoules_per_kilogram_degree_celsius, fractional_digits)} MJ/kg.C"""
        
        if unit == SpecificEntropyUnits.KilocaloriePerGramKelvin:
            return f"""{super()._truncate_fraction_digits(self.kilocalories_per_gram_kelvin, fractional_digits)} kcal/g.K"""
        
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
        
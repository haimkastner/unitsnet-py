from enum import Enum
import math
import string


class FuelEfficiencyUnits(Enum):
        """
            FuelEfficiencyUnits enumeration
        """
        
        LiterPer100Kilometers = 'liter_per100_kilometers'
        """
            
        """
        
        MilePerUsGallon = 'mile_per_us_gallon'
        """
            
        """
        
        MilePerUkGallon = 'mile_per_uk_gallon'
        """
            
        """
        
        KilometerPerLiter = 'kilometer_per_liter'
        """
            
        """
        

class FuelEfficiency:
    """
    Fuel efficiency is a form of thermal efficiency, meaning the ratio from effort to result of a process that converts chemical potential energy contained in a carrier (fuel) into kinetic energy or work. Fuel economy is stated as "fuel consumption" in liters per 100 kilometers (L/100 km). In countries using non-metric system, fuel economy is expressed in miles per gallon (mpg) (imperial galon or US galon).

    Args:
        value (float): The value.
        from_unit (FuelEfficiencyUnits): The FuelEfficiency unit to create from, The default unit is LiterPer100Kilometers
    """
    def __init__(self, value: float, from_unit: FuelEfficiencyUnits = FuelEfficiencyUnits.LiterPer100Kilometers):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__liters_per100_kilometers = None
        
        self.__miles_per_us_gallon = None
        
        self.__miles_per_uk_gallon = None
        
        self.__kilometers_per_liters = None
        

    def __convert_from_base(self, from_unit: FuelEfficiencyUnits) -> float:
        value = self.__value
        
        if from_unit == FuelEfficiencyUnits.LiterPer100Kilometers:
            return (value)
        
        if from_unit == FuelEfficiencyUnits.MilePerUsGallon:
            return ((100 * 3.785411784) / (1.609344 * value))
        
        if from_unit == FuelEfficiencyUnits.MilePerUkGallon:
            return ((100 * 4.54609188) / (1.609344 * value))
        
        if from_unit == FuelEfficiencyUnits.KilometerPerLiter:
            return (100 / value)
        
        return None


    def __convert_to_base(self, value: float, to_unit: FuelEfficiencyUnits) -> float:
        
        if to_unit == FuelEfficiencyUnits.LiterPer100Kilometers:
            return (value)
        
        if to_unit == FuelEfficiencyUnits.MilePerUsGallon:
            return ((100 * 3.785411784) / (1.609344 * value))
        
        if to_unit == FuelEfficiencyUnits.MilePerUkGallon:
            return ((100 * 4.54609188) / (1.609344 * value))
        
        if to_unit == FuelEfficiencyUnits.KilometerPerLiter:
            return (100 / value)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
    @staticmethod
    def from_liters_per100_kilometers(liters_per100_kilometers: float):
        """
        Create a new instance of FuelEfficiency from a value in liters_per100_kilometers.

        

        :param meters: The FuelEfficiency value in liters_per100_kilometers.
        :type liters_per100_kilometers: float
        :return: A new instance of FuelEfficiency.
        :rtype: FuelEfficiency
        """
        return FuelEfficiency(liters_per100_kilometers, FuelEfficiencyUnits.LiterPer100Kilometers)

    
    @staticmethod
    def from_miles_per_us_gallon(miles_per_us_gallon: float):
        """
        Create a new instance of FuelEfficiency from a value in miles_per_us_gallon.

        

        :param meters: The FuelEfficiency value in miles_per_us_gallon.
        :type miles_per_us_gallon: float
        :return: A new instance of FuelEfficiency.
        :rtype: FuelEfficiency
        """
        return FuelEfficiency(miles_per_us_gallon, FuelEfficiencyUnits.MilePerUsGallon)

    
    @staticmethod
    def from_miles_per_uk_gallon(miles_per_uk_gallon: float):
        """
        Create a new instance of FuelEfficiency from a value in miles_per_uk_gallon.

        

        :param meters: The FuelEfficiency value in miles_per_uk_gallon.
        :type miles_per_uk_gallon: float
        :return: A new instance of FuelEfficiency.
        :rtype: FuelEfficiency
        """
        return FuelEfficiency(miles_per_uk_gallon, FuelEfficiencyUnits.MilePerUkGallon)

    
    @staticmethod
    def from_kilometers_per_liters(kilometers_per_liters: float):
        """
        Create a new instance of FuelEfficiency from a value in kilometers_per_liters.

        

        :param meters: The FuelEfficiency value in kilometers_per_liters.
        :type kilometers_per_liters: float
        :return: A new instance of FuelEfficiency.
        :rtype: FuelEfficiency
        """
        return FuelEfficiency(kilometers_per_liters, FuelEfficiencyUnits.KilometerPerLiter)

    
    @property
    def liters_per100_kilometers(self) -> float:
        """
        
        """
        if self.__liters_per100_kilometers != None:
            return self.__liters_per100_kilometers
        self.__liters_per100_kilometers = self.__convert_from_base(FuelEfficiencyUnits.LiterPer100Kilometers)
        return self.__liters_per100_kilometers

    
    @property
    def miles_per_us_gallon(self) -> float:
        """
        
        """
        if self.__miles_per_us_gallon != None:
            return self.__miles_per_us_gallon
        self.__miles_per_us_gallon = self.__convert_from_base(FuelEfficiencyUnits.MilePerUsGallon)
        return self.__miles_per_us_gallon

    
    @property
    def miles_per_uk_gallon(self) -> float:
        """
        
        """
        if self.__miles_per_uk_gallon != None:
            return self.__miles_per_uk_gallon
        self.__miles_per_uk_gallon = self.__convert_from_base(FuelEfficiencyUnits.MilePerUkGallon)
        return self.__miles_per_uk_gallon

    
    @property
    def kilometers_per_liters(self) -> float:
        """
        
        """
        if self.__kilometers_per_liters != None:
            return self.__kilometers_per_liters
        self.__kilometers_per_liters = self.__convert_from_base(FuelEfficiencyUnits.KilometerPerLiter)
        return self.__kilometers_per_liters

    
    def to_string(self, unit: FuelEfficiencyUnits = FuelEfficiencyUnits.LiterPer100Kilometers) -> string:
        """
        Format the FuelEfficiency to string.
        Note! the default format for FuelEfficiency is LiterPer100Kilometers.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == FuelEfficiencyUnits.LiterPer100Kilometers:
            return f"""{self.liters_per100_kilometers} L/100km"""
        
        if unit == FuelEfficiencyUnits.MilePerUsGallon:
            return f"""{self.miles_per_us_gallon} mpg (U.S.)"""
        
        if unit == FuelEfficiencyUnits.MilePerUkGallon:
            return f"""{self.miles_per_uk_gallon} mpg (imp.)"""
        
        if unit == FuelEfficiencyUnits.KilometerPerLiter:
            return f"""{self.kilometers_per_liters} km/L"""
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: FuelEfficiencyUnits = FuelEfficiencyUnits.LiterPer100Kilometers) -> string:
        """
        Get FuelEfficiency unit abbreviation.
        Note! the default abbreviation for FuelEfficiency is LiterPer100Kilometers.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == FuelEfficiencyUnits.LiterPer100Kilometers:
            return """L/100km"""
        
        if unit_abbreviation == FuelEfficiencyUnits.MilePerUsGallon:
            return """mpg (U.S.)"""
        
        if unit_abbreviation == FuelEfficiencyUnits.MilePerUkGallon:
            return """mpg (imp.)"""
        
        if unit_abbreviation == FuelEfficiencyUnits.KilometerPerLiter:
            return """km/L"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, FuelEfficiency):
            raise TypeError("unsupported operand type(s) for +: 'FuelEfficiency' and '{}'".format(type(other).__name__))
        return FuelEfficiency(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, FuelEfficiency):
            raise TypeError("unsupported operand type(s) for *: 'FuelEfficiency' and '{}'".format(type(other).__name__))
        return FuelEfficiency(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, FuelEfficiency):
            raise TypeError("unsupported operand type(s) for -: 'FuelEfficiency' and '{}'".format(type(other).__name__))
        return FuelEfficiency(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, FuelEfficiency):
            raise TypeError("unsupported operand type(s) for /: 'FuelEfficiency' and '{}'".format(type(other).__name__))
        return FuelEfficiency(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, FuelEfficiency):
            raise TypeError("unsupported operand type(s) for %: 'FuelEfficiency' and '{}'".format(type(other).__name__))
        return FuelEfficiency(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, FuelEfficiency):
            raise TypeError("unsupported operand type(s) for **: 'FuelEfficiency' and '{}'".format(type(other).__name__))
        return FuelEfficiency(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, FuelEfficiency):
            raise TypeError("unsupported operand type(s) for ==: 'FuelEfficiency' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, FuelEfficiency):
            raise TypeError("unsupported operand type(s) for <: 'FuelEfficiency' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, FuelEfficiency):
            raise TypeError("unsupported operand type(s) for >: 'FuelEfficiency' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, FuelEfficiency):
            raise TypeError("unsupported operand type(s) for <=: 'FuelEfficiency' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, FuelEfficiency):
            raise TypeError("unsupported operand type(s) for >=: 'FuelEfficiency' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value
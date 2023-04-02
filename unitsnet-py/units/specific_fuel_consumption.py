from enum import Enum
import math
import string


class SpecificFuelConsumptionUnits(Enum):
        """
            SpecificFuelConsumptionUnits enumeration
        """
        
        PoundMassPerPoundForceHour = 'pound_mass_per_pound_force_hour'
        """
            
        """
        
        KilogramPerKilogramForceHour = 'kilogram_per_kilogram_force_hour'
        """
            
        """
        
        GramPerKiloNewtonSecond = 'gram_per_kilo_newton_second'
        """
            
        """
        
        KilogramPerKiloNewtonSecond = 'kilogram_per_kilo_newton_second'
        """
            
        """
        

class SpecificFuelConsumption:
    """
    SFC is the fuel efficiency of an engine design with respect to thrust output

    Args:
        value (float): The value.
        from_unit (SpecificFuelConsumptionUnits): The SpecificFuelConsumption unit to create from, The default unit is GramPerKiloNewtonSecond
    """
    def __init__(self, value: float, from_unit: SpecificFuelConsumptionUnits = SpecificFuelConsumptionUnits.GramPerKiloNewtonSecond):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__pounds_mass_per_pound_force_hour = None
        
        self.__kilograms_per_kilogram_force_hour = None
        
        self.__grams_per_kilo_newton_second = None
        
        self.__kilograms_per_kilo_newton_second = None
        

    def __convert_from_base(self, from_unit: SpecificFuelConsumptionUnits) -> float:
        value = self.__value
        
        if from_unit == SpecificFuelConsumptionUnits.PoundMassPerPoundForceHour:
            return (value / 28.33)
        
        if from_unit == SpecificFuelConsumptionUnits.KilogramPerKilogramForceHour:
            return (value / 28.33)
        
        if from_unit == SpecificFuelConsumptionUnits.GramPerKiloNewtonSecond:
            return (value)
        
        if from_unit == SpecificFuelConsumptionUnits.KilogramPerKiloNewtonSecond:
            return ((value) / 1000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: SpecificFuelConsumptionUnits) -> float:
        
        if to_unit == SpecificFuelConsumptionUnits.PoundMassPerPoundForceHour:
            return (value * 28.33)
        
        if to_unit == SpecificFuelConsumptionUnits.KilogramPerKilogramForceHour:
            return (value * 28.33)
        
        if to_unit == SpecificFuelConsumptionUnits.GramPerKiloNewtonSecond:
            return (value)
        
        if to_unit == SpecificFuelConsumptionUnits.KilogramPerKiloNewtonSecond:
            return ((value) * 1000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
    @staticmethod
    def from_pounds_mass_per_pound_force_hour(pounds_mass_per_pound_force_hour: float):
        """
        Create a new instance of SpecificFuelConsumption from a value in pounds_mass_per_pound_force_hour.

        

        :param meters: The SpecificFuelConsumption value in pounds_mass_per_pound_force_hour.
        :type pounds_mass_per_pound_force_hour: float
        :return: A new instance of SpecificFuelConsumption.
        :rtype: SpecificFuelConsumption
        """
        return SpecificFuelConsumption(pounds_mass_per_pound_force_hour, SpecificFuelConsumptionUnits.PoundMassPerPoundForceHour)

    
    @staticmethod
    def from_kilograms_per_kilogram_force_hour(kilograms_per_kilogram_force_hour: float):
        """
        Create a new instance of SpecificFuelConsumption from a value in kilograms_per_kilogram_force_hour.

        

        :param meters: The SpecificFuelConsumption value in kilograms_per_kilogram_force_hour.
        :type kilograms_per_kilogram_force_hour: float
        :return: A new instance of SpecificFuelConsumption.
        :rtype: SpecificFuelConsumption
        """
        return SpecificFuelConsumption(kilograms_per_kilogram_force_hour, SpecificFuelConsumptionUnits.KilogramPerKilogramForceHour)

    
    @staticmethod
    def from_grams_per_kilo_newton_second(grams_per_kilo_newton_second: float):
        """
        Create a new instance of SpecificFuelConsumption from a value in grams_per_kilo_newton_second.

        

        :param meters: The SpecificFuelConsumption value in grams_per_kilo_newton_second.
        :type grams_per_kilo_newton_second: float
        :return: A new instance of SpecificFuelConsumption.
        :rtype: SpecificFuelConsumption
        """
        return SpecificFuelConsumption(grams_per_kilo_newton_second, SpecificFuelConsumptionUnits.GramPerKiloNewtonSecond)

    
    @staticmethod
    def from_kilograms_per_kilo_newton_second(kilograms_per_kilo_newton_second: float):
        """
        Create a new instance of SpecificFuelConsumption from a value in kilograms_per_kilo_newton_second.

        

        :param meters: The SpecificFuelConsumption value in kilograms_per_kilo_newton_second.
        :type kilograms_per_kilo_newton_second: float
        :return: A new instance of SpecificFuelConsumption.
        :rtype: SpecificFuelConsumption
        """
        return SpecificFuelConsumption(kilograms_per_kilo_newton_second, SpecificFuelConsumptionUnits.KilogramPerKiloNewtonSecond)

    
    @property
    def pounds_mass_per_pound_force_hour(self) -> float:
        """
        
        """
        if self.__pounds_mass_per_pound_force_hour != None:
            return self.__pounds_mass_per_pound_force_hour
        self.__pounds_mass_per_pound_force_hour = self.__convert_from_base(SpecificFuelConsumptionUnits.PoundMassPerPoundForceHour)
        return self.__pounds_mass_per_pound_force_hour

    
    @property
    def kilograms_per_kilogram_force_hour(self) -> float:
        """
        
        """
        if self.__kilograms_per_kilogram_force_hour != None:
            return self.__kilograms_per_kilogram_force_hour
        self.__kilograms_per_kilogram_force_hour = self.__convert_from_base(SpecificFuelConsumptionUnits.KilogramPerKilogramForceHour)
        return self.__kilograms_per_kilogram_force_hour

    
    @property
    def grams_per_kilo_newton_second(self) -> float:
        """
        
        """
        if self.__grams_per_kilo_newton_second != None:
            return self.__grams_per_kilo_newton_second
        self.__grams_per_kilo_newton_second = self.__convert_from_base(SpecificFuelConsumptionUnits.GramPerKiloNewtonSecond)
        return self.__grams_per_kilo_newton_second

    
    @property
    def kilograms_per_kilo_newton_second(self) -> float:
        """
        
        """
        if self.__kilograms_per_kilo_newton_second != None:
            return self.__kilograms_per_kilo_newton_second
        self.__kilograms_per_kilo_newton_second = self.__convert_from_base(SpecificFuelConsumptionUnits.KilogramPerKiloNewtonSecond)
        return self.__kilograms_per_kilo_newton_second

    
    def to_string(self, unit: SpecificFuelConsumptionUnits = SpecificFuelConsumptionUnits.GramPerKiloNewtonSecond) -> string:
        """
        Format the SpecificFuelConsumption to string.
        Note! the default format for SpecificFuelConsumption is GramPerKiloNewtonSecond.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == SpecificFuelConsumptionUnits.PoundMassPerPoundForceHour:
            return f"""{self.pounds_mass_per_pound_force_hour} lb/(lbf·h)"""
        
        if unit == SpecificFuelConsumptionUnits.KilogramPerKilogramForceHour:
            return f"""{self.kilograms_per_kilogram_force_hour} kg/(kgf�h)"""
        
        if unit == SpecificFuelConsumptionUnits.GramPerKiloNewtonSecond:
            return f"""{self.grams_per_kilo_newton_second} g/(kN�s)"""
        
        if unit == SpecificFuelConsumptionUnits.KilogramPerKiloNewtonSecond:
            return f"""{self.kilograms_per_kilo_newton_second} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: SpecificFuelConsumptionUnits = SpecificFuelConsumptionUnits.GramPerKiloNewtonSecond) -> string:
        """
        Get SpecificFuelConsumption unit abbreviation.
        Note! the default abbreviation for SpecificFuelConsumption is GramPerKiloNewtonSecond.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == SpecificFuelConsumptionUnits.PoundMassPerPoundForceHour:
            return """lb/(lbf·h)"""
        
        if unit_abbreviation == SpecificFuelConsumptionUnits.KilogramPerKilogramForceHour:
            return """kg/(kgf�h)"""
        
        if unit_abbreviation == SpecificFuelConsumptionUnits.GramPerKiloNewtonSecond:
            return """g/(kN�s)"""
        
        if unit_abbreviation == SpecificFuelConsumptionUnits.KilogramPerKiloNewtonSecond:
            return """"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, SpecificFuelConsumption):
            raise TypeError("unsupported operand type(s) for +: 'SpecificFuelConsumption' and '{}'".format(type(other).__name__))
        return SpecificFuelConsumption(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, SpecificFuelConsumption):
            raise TypeError("unsupported operand type(s) for *: 'SpecificFuelConsumption' and '{}'".format(type(other).__name__))
        return SpecificFuelConsumption(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, SpecificFuelConsumption):
            raise TypeError("unsupported operand type(s) for -: 'SpecificFuelConsumption' and '{}'".format(type(other).__name__))
        return SpecificFuelConsumption(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, SpecificFuelConsumption):
            raise TypeError("unsupported operand type(s) for /: 'SpecificFuelConsumption' and '{}'".format(type(other).__name__))
        return SpecificFuelConsumption(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, SpecificFuelConsumption):
            raise TypeError("unsupported operand type(s) for %: 'SpecificFuelConsumption' and '{}'".format(type(other).__name__))
        return SpecificFuelConsumption(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, SpecificFuelConsumption):
            raise TypeError("unsupported operand type(s) for **: 'SpecificFuelConsumption' and '{}'".format(type(other).__name__))
        return SpecificFuelConsumption(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, SpecificFuelConsumption):
            raise TypeError("unsupported operand type(s) for ==: 'SpecificFuelConsumption' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, SpecificFuelConsumption):
            raise TypeError("unsupported operand type(s) for <: 'SpecificFuelConsumption' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, SpecificFuelConsumption):
            raise TypeError("unsupported operand type(s) for >: 'SpecificFuelConsumption' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, SpecificFuelConsumption):
            raise TypeError("unsupported operand type(s) for <=: 'SpecificFuelConsumption' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, SpecificFuelConsumption):
            raise TypeError("unsupported operand type(s) for >=: 'SpecificFuelConsumption' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value
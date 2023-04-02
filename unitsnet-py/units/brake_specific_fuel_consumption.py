from enum import Enum
import math
import string


class BrakeSpecificFuelConsumptionUnits(Enum):
        """
            BrakeSpecificFuelConsumptionUnits enumeration
        """
        
        GramPerKiloWattHour = 'gram_per_kilo_watt_hour'
        """
            
        """
        
        KilogramPerJoule = 'kilogram_per_joule'
        """
            
        """
        
        PoundPerMechanicalHorsepowerHour = 'pound_per_mechanical_horsepower_hour'
        """
            The pound per horse power hour uses mechanical horse power and the imperial pound
        """
        

class BrakeSpecificFuelConsumption:
    """
    Brake specific fuel consumption (BSFC) is a measure of the fuel efficiency of any prime mover that burns fuel and produces rotational, or shaft, power. It is typically used for comparing the efficiency of internal combustion engines with a shaft output.

    Args:
        value (float): The value.
        from_unit (BrakeSpecificFuelConsumptionUnits): The BrakeSpecificFuelConsumption unit to create from, The default unit is KilogramPerJoule
    """
    def __init__(self, value: float, from_unit: BrakeSpecificFuelConsumptionUnits = BrakeSpecificFuelConsumptionUnits.KilogramPerJoule):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__grams_per_kilo_watt_hour = None
        
        self.__kilograms_per_joule = None
        
        self.__pounds_per_mechanical_horsepower_hour = None
        

    def __convert_from_base(self, from_unit: BrakeSpecificFuelConsumptionUnits) -> float:
        value = self.__value
        
        if from_unit == BrakeSpecificFuelConsumptionUnits.GramPerKiloWattHour:
            return (value * 3.6e9)
        
        if from_unit == BrakeSpecificFuelConsumptionUnits.KilogramPerJoule:
            return (value)
        
        if from_unit == BrakeSpecificFuelConsumptionUnits.PoundPerMechanicalHorsepowerHour:
            return (value / 1.689659410672e-7)
        
        return None


    def __convert_to_base(self, value: float, to_unit: BrakeSpecificFuelConsumptionUnits) -> float:
        
        if to_unit == BrakeSpecificFuelConsumptionUnits.GramPerKiloWattHour:
            return (value / 3.6e9)
        
        if to_unit == BrakeSpecificFuelConsumptionUnits.KilogramPerJoule:
            return (value)
        
        if to_unit == BrakeSpecificFuelConsumptionUnits.PoundPerMechanicalHorsepowerHour:
            return (value * 1.689659410672e-7)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
    @staticmethod
    def from_grams_per_kilo_watt_hour(grams_per_kilo_watt_hour: float):
        """
        Create a new instance of BrakeSpecificFuelConsumption from a value in grams_per_kilo_watt_hour.

        

        :param meters: The BrakeSpecificFuelConsumption value in grams_per_kilo_watt_hour.
        :type grams_per_kilo_watt_hour: float
        :return: A new instance of BrakeSpecificFuelConsumption.
        :rtype: BrakeSpecificFuelConsumption
        """
        return BrakeSpecificFuelConsumption(grams_per_kilo_watt_hour, BrakeSpecificFuelConsumptionUnits.GramPerKiloWattHour)

    
    @staticmethod
    def from_kilograms_per_joule(kilograms_per_joule: float):
        """
        Create a new instance of BrakeSpecificFuelConsumption from a value in kilograms_per_joule.

        

        :param meters: The BrakeSpecificFuelConsumption value in kilograms_per_joule.
        :type kilograms_per_joule: float
        :return: A new instance of BrakeSpecificFuelConsumption.
        :rtype: BrakeSpecificFuelConsumption
        """
        return BrakeSpecificFuelConsumption(kilograms_per_joule, BrakeSpecificFuelConsumptionUnits.KilogramPerJoule)

    
    @staticmethod
    def from_pounds_per_mechanical_horsepower_hour(pounds_per_mechanical_horsepower_hour: float):
        """
        Create a new instance of BrakeSpecificFuelConsumption from a value in pounds_per_mechanical_horsepower_hour.

        The pound per horse power hour uses mechanical horse power and the imperial pound

        :param meters: The BrakeSpecificFuelConsumption value in pounds_per_mechanical_horsepower_hour.
        :type pounds_per_mechanical_horsepower_hour: float
        :return: A new instance of BrakeSpecificFuelConsumption.
        :rtype: BrakeSpecificFuelConsumption
        """
        return BrakeSpecificFuelConsumption(pounds_per_mechanical_horsepower_hour, BrakeSpecificFuelConsumptionUnits.PoundPerMechanicalHorsepowerHour)

    
    @property
    def grams_per_kilo_watt_hour(self) -> float:
        """
        
        """
        if self.__grams_per_kilo_watt_hour != None:
            return self.__grams_per_kilo_watt_hour
        self.__grams_per_kilo_watt_hour = self.__convert_from_base(BrakeSpecificFuelConsumptionUnits.GramPerKiloWattHour)
        return self.__grams_per_kilo_watt_hour

    
    @property
    def kilograms_per_joule(self) -> float:
        """
        
        """
        if self.__kilograms_per_joule != None:
            return self.__kilograms_per_joule
        self.__kilograms_per_joule = self.__convert_from_base(BrakeSpecificFuelConsumptionUnits.KilogramPerJoule)
        return self.__kilograms_per_joule

    
    @property
    def pounds_per_mechanical_horsepower_hour(self) -> float:
        """
        The pound per horse power hour uses mechanical horse power and the imperial pound
        """
        if self.__pounds_per_mechanical_horsepower_hour != None:
            return self.__pounds_per_mechanical_horsepower_hour
        self.__pounds_per_mechanical_horsepower_hour = self.__convert_from_base(BrakeSpecificFuelConsumptionUnits.PoundPerMechanicalHorsepowerHour)
        return self.__pounds_per_mechanical_horsepower_hour

    
    def to_string(self, unit: BrakeSpecificFuelConsumptionUnits = BrakeSpecificFuelConsumptionUnits.KilogramPerJoule) -> string:
        """
        Format the BrakeSpecificFuelConsumption to string.
        Note! the default format for BrakeSpecificFuelConsumption is KilogramPerJoule.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == BrakeSpecificFuelConsumptionUnits.GramPerKiloWattHour:
            return f"""{self.grams_per_kilo_watt_hour} g/kWh"""
        
        if unit == BrakeSpecificFuelConsumptionUnits.KilogramPerJoule:
            return f"""{self.kilograms_per_joule} kg/J"""
        
        if unit == BrakeSpecificFuelConsumptionUnits.PoundPerMechanicalHorsepowerHour:
            return f"""{self.pounds_per_mechanical_horsepower_hour} lb/hph"""
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: BrakeSpecificFuelConsumptionUnits = BrakeSpecificFuelConsumptionUnits.KilogramPerJoule) -> string:
        """
        Get BrakeSpecificFuelConsumption unit abbreviation.
        Note! the default abbreviation for BrakeSpecificFuelConsumption is KilogramPerJoule.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == BrakeSpecificFuelConsumptionUnits.GramPerKiloWattHour:
            return """g/kWh"""
        
        if unit_abbreviation == BrakeSpecificFuelConsumptionUnits.KilogramPerJoule:
            return """kg/J"""
        
        if unit_abbreviation == BrakeSpecificFuelConsumptionUnits.PoundPerMechanicalHorsepowerHour:
            return """lb/hph"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, BrakeSpecificFuelConsumption):
            raise TypeError("unsupported operand type(s) for +: 'BrakeSpecificFuelConsumption' and '{}'".format(type(other).__name__))
        return BrakeSpecificFuelConsumption(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, BrakeSpecificFuelConsumption):
            raise TypeError("unsupported operand type(s) for *: 'BrakeSpecificFuelConsumption' and '{}'".format(type(other).__name__))
        return BrakeSpecificFuelConsumption(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, BrakeSpecificFuelConsumption):
            raise TypeError("unsupported operand type(s) for -: 'BrakeSpecificFuelConsumption' and '{}'".format(type(other).__name__))
        return BrakeSpecificFuelConsumption(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, BrakeSpecificFuelConsumption):
            raise TypeError("unsupported operand type(s) for /: 'BrakeSpecificFuelConsumption' and '{}'".format(type(other).__name__))
        return BrakeSpecificFuelConsumption(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, BrakeSpecificFuelConsumption):
            raise TypeError("unsupported operand type(s) for %: 'BrakeSpecificFuelConsumption' and '{}'".format(type(other).__name__))
        return BrakeSpecificFuelConsumption(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, BrakeSpecificFuelConsumption):
            raise TypeError("unsupported operand type(s) for **: 'BrakeSpecificFuelConsumption' and '{}'".format(type(other).__name__))
        return BrakeSpecificFuelConsumption(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, BrakeSpecificFuelConsumption):
            raise TypeError("unsupported operand type(s) for ==: 'BrakeSpecificFuelConsumption' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, BrakeSpecificFuelConsumption):
            raise TypeError("unsupported operand type(s) for <: 'BrakeSpecificFuelConsumption' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, BrakeSpecificFuelConsumption):
            raise TypeError("unsupported operand type(s) for >: 'BrakeSpecificFuelConsumption' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, BrakeSpecificFuelConsumption):
            raise TypeError("unsupported operand type(s) for <=: 'BrakeSpecificFuelConsumption' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, BrakeSpecificFuelConsumption):
            raise TypeError("unsupported operand type(s) for >=: 'BrakeSpecificFuelConsumption' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value
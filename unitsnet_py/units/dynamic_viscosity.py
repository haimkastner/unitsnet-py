from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class DynamicViscosityUnits(Enum):
        """
            DynamicViscosityUnits enumeration
        """
        
        NewtonSecondPerMeterSquared = 'newton_second_per_meter_squared'
        """
            
        """
        
        PascalSecond = 'pascal_second'
        """
            
        """
        
        Poise = 'poise'
        """
            
        """
        
        Reyn = 'reyn'
        """
            
        """
        
        PoundForceSecondPerSquareInch = 'pound_force_second_per_square_inch'
        """
            
        """
        
        PoundForceSecondPerSquareFoot = 'pound_force_second_per_square_foot'
        """
            
        """
        
        PoundPerFootSecond = 'pound_per_foot_second'
        """
            
        """
        
        MillipascalSecond = 'millipascal_second'
        """
            
        """
        
        MicropascalSecond = 'micropascal_second'
        """
            
        """
        
        Centipoise = 'centipoise'
        """
            
        """
        

class DynamicViscosity(AbstractMeasure):
    """
    The dynamic (shear) viscosity of a fluid expresses its resistance to shearing flows, where adjacent layers move parallel to each other with different speeds

    Args:
        value (float): The value.
        from_unit (DynamicViscosityUnits): The DynamicViscosity unit to create from, The default unit is NewtonSecondPerMeterSquared
    """
    def __init__(self, value: float, from_unit: DynamicViscosityUnits = DynamicViscosityUnits.NewtonSecondPerMeterSquared):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__newton_seconds_per_meter_squared = None
        
        self.__pascal_seconds = None
        
        self.__poise = None
        
        self.__reyns = None
        
        self.__pounds_force_second_per_square_inch = None
        
        self.__pounds_force_second_per_square_foot = None
        
        self.__pounds_per_foot_second = None
        
        self.__millipascal_seconds = None
        
        self.__micropascal_seconds = None
        
        self.__centipoise = None
        

    def convert(self, unit: DynamicViscosityUnits) -> float:
        return self.__convert_from_base(unit)

    def __convert_from_base(self, from_unit: DynamicViscosityUnits) -> float:
        value = self._value
        
        if from_unit == DynamicViscosityUnits.NewtonSecondPerMeterSquared:
            return (value)
        
        if from_unit == DynamicViscosityUnits.PascalSecond:
            return (value)
        
        if from_unit == DynamicViscosityUnits.Poise:
            return (value * 10)
        
        if from_unit == DynamicViscosityUnits.Reyn:
            return (value / 6.8947572931683613e3)
        
        if from_unit == DynamicViscosityUnits.PoundForceSecondPerSquareInch:
            return (value / 6.8947572931683613e3)
        
        if from_unit == DynamicViscosityUnits.PoundForceSecondPerSquareFoot:
            return (value / 4.7880258980335843e1)
        
        if from_unit == DynamicViscosityUnits.PoundPerFootSecond:
            return (value / 1.4881639)
        
        if from_unit == DynamicViscosityUnits.MillipascalSecond:
            return ((value) / 0.001)
        
        if from_unit == DynamicViscosityUnits.MicropascalSecond:
            return ((value) / 1e-06)
        
        if from_unit == DynamicViscosityUnits.Centipoise:
            return ((value * 10) / 0.01)
        
        return None


    def __convert_to_base(self, value: float, to_unit: DynamicViscosityUnits) -> float:
        
        if to_unit == DynamicViscosityUnits.NewtonSecondPerMeterSquared:
            return (value)
        
        if to_unit == DynamicViscosityUnits.PascalSecond:
            return (value)
        
        if to_unit == DynamicViscosityUnits.Poise:
            return (value / 10)
        
        if to_unit == DynamicViscosityUnits.Reyn:
            return (value * 6.8947572931683613e3)
        
        if to_unit == DynamicViscosityUnits.PoundForceSecondPerSquareInch:
            return (value * 6.8947572931683613e3)
        
        if to_unit == DynamicViscosityUnits.PoundForceSecondPerSquareFoot:
            return (value * 4.7880258980335843e1)
        
        if to_unit == DynamicViscosityUnits.PoundPerFootSecond:
            return (value * 1.4881639)
        
        if to_unit == DynamicViscosityUnits.MillipascalSecond:
            return ((value) * 0.001)
        
        if to_unit == DynamicViscosityUnits.MicropascalSecond:
            return ((value) * 1e-06)
        
        if to_unit == DynamicViscosityUnits.Centipoise:
            return ((value / 10) * 0.01)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_newton_seconds_per_meter_squared(newton_seconds_per_meter_squared: float):
        """
        Create a new instance of DynamicViscosity from a value in newton_seconds_per_meter_squared.

        

        :param meters: The DynamicViscosity value in newton_seconds_per_meter_squared.
        :type newton_seconds_per_meter_squared: float
        :return: A new instance of DynamicViscosity.
        :rtype: DynamicViscosity
        """
        return DynamicViscosity(newton_seconds_per_meter_squared, DynamicViscosityUnits.NewtonSecondPerMeterSquared)

    
    @staticmethod
    def from_pascal_seconds(pascal_seconds: float):
        """
        Create a new instance of DynamicViscosity from a value in pascal_seconds.

        

        :param meters: The DynamicViscosity value in pascal_seconds.
        :type pascal_seconds: float
        :return: A new instance of DynamicViscosity.
        :rtype: DynamicViscosity
        """
        return DynamicViscosity(pascal_seconds, DynamicViscosityUnits.PascalSecond)

    
    @staticmethod
    def from_poise(poise: float):
        """
        Create a new instance of DynamicViscosity from a value in poise.

        

        :param meters: The DynamicViscosity value in poise.
        :type poise: float
        :return: A new instance of DynamicViscosity.
        :rtype: DynamicViscosity
        """
        return DynamicViscosity(poise, DynamicViscosityUnits.Poise)

    
    @staticmethod
    def from_reyns(reyns: float):
        """
        Create a new instance of DynamicViscosity from a value in reyns.

        

        :param meters: The DynamicViscosity value in reyns.
        :type reyns: float
        :return: A new instance of DynamicViscosity.
        :rtype: DynamicViscosity
        """
        return DynamicViscosity(reyns, DynamicViscosityUnits.Reyn)

    
    @staticmethod
    def from_pounds_force_second_per_square_inch(pounds_force_second_per_square_inch: float):
        """
        Create a new instance of DynamicViscosity from a value in pounds_force_second_per_square_inch.

        

        :param meters: The DynamicViscosity value in pounds_force_second_per_square_inch.
        :type pounds_force_second_per_square_inch: float
        :return: A new instance of DynamicViscosity.
        :rtype: DynamicViscosity
        """
        return DynamicViscosity(pounds_force_second_per_square_inch, DynamicViscosityUnits.PoundForceSecondPerSquareInch)

    
    @staticmethod
    def from_pounds_force_second_per_square_foot(pounds_force_second_per_square_foot: float):
        """
        Create a new instance of DynamicViscosity from a value in pounds_force_second_per_square_foot.

        

        :param meters: The DynamicViscosity value in pounds_force_second_per_square_foot.
        :type pounds_force_second_per_square_foot: float
        :return: A new instance of DynamicViscosity.
        :rtype: DynamicViscosity
        """
        return DynamicViscosity(pounds_force_second_per_square_foot, DynamicViscosityUnits.PoundForceSecondPerSquareFoot)

    
    @staticmethod
    def from_pounds_per_foot_second(pounds_per_foot_second: float):
        """
        Create a new instance of DynamicViscosity from a value in pounds_per_foot_second.

        

        :param meters: The DynamicViscosity value in pounds_per_foot_second.
        :type pounds_per_foot_second: float
        :return: A new instance of DynamicViscosity.
        :rtype: DynamicViscosity
        """
        return DynamicViscosity(pounds_per_foot_second, DynamicViscosityUnits.PoundPerFootSecond)

    
    @staticmethod
    def from_millipascal_seconds(millipascal_seconds: float):
        """
        Create a new instance of DynamicViscosity from a value in millipascal_seconds.

        

        :param meters: The DynamicViscosity value in millipascal_seconds.
        :type millipascal_seconds: float
        :return: A new instance of DynamicViscosity.
        :rtype: DynamicViscosity
        """
        return DynamicViscosity(millipascal_seconds, DynamicViscosityUnits.MillipascalSecond)

    
    @staticmethod
    def from_micropascal_seconds(micropascal_seconds: float):
        """
        Create a new instance of DynamicViscosity from a value in micropascal_seconds.

        

        :param meters: The DynamicViscosity value in micropascal_seconds.
        :type micropascal_seconds: float
        :return: A new instance of DynamicViscosity.
        :rtype: DynamicViscosity
        """
        return DynamicViscosity(micropascal_seconds, DynamicViscosityUnits.MicropascalSecond)

    
    @staticmethod
    def from_centipoise(centipoise: float):
        """
        Create a new instance of DynamicViscosity from a value in centipoise.

        

        :param meters: The DynamicViscosity value in centipoise.
        :type centipoise: float
        :return: A new instance of DynamicViscosity.
        :rtype: DynamicViscosity
        """
        return DynamicViscosity(centipoise, DynamicViscosityUnits.Centipoise)

    
    @property
    def newton_seconds_per_meter_squared(self) -> float:
        """
        
        """
        if self.__newton_seconds_per_meter_squared != None:
            return self.__newton_seconds_per_meter_squared
        self.__newton_seconds_per_meter_squared = self.__convert_from_base(DynamicViscosityUnits.NewtonSecondPerMeterSquared)
        return self.__newton_seconds_per_meter_squared

    
    @property
    def pascal_seconds(self) -> float:
        """
        
        """
        if self.__pascal_seconds != None:
            return self.__pascal_seconds
        self.__pascal_seconds = self.__convert_from_base(DynamicViscosityUnits.PascalSecond)
        return self.__pascal_seconds

    
    @property
    def poise(self) -> float:
        """
        
        """
        if self.__poise != None:
            return self.__poise
        self.__poise = self.__convert_from_base(DynamicViscosityUnits.Poise)
        return self.__poise

    
    @property
    def reyns(self) -> float:
        """
        
        """
        if self.__reyns != None:
            return self.__reyns
        self.__reyns = self.__convert_from_base(DynamicViscosityUnits.Reyn)
        return self.__reyns

    
    @property
    def pounds_force_second_per_square_inch(self) -> float:
        """
        
        """
        if self.__pounds_force_second_per_square_inch != None:
            return self.__pounds_force_second_per_square_inch
        self.__pounds_force_second_per_square_inch = self.__convert_from_base(DynamicViscosityUnits.PoundForceSecondPerSquareInch)
        return self.__pounds_force_second_per_square_inch

    
    @property
    def pounds_force_second_per_square_foot(self) -> float:
        """
        
        """
        if self.__pounds_force_second_per_square_foot != None:
            return self.__pounds_force_second_per_square_foot
        self.__pounds_force_second_per_square_foot = self.__convert_from_base(DynamicViscosityUnits.PoundForceSecondPerSquareFoot)
        return self.__pounds_force_second_per_square_foot

    
    @property
    def pounds_per_foot_second(self) -> float:
        """
        
        """
        if self.__pounds_per_foot_second != None:
            return self.__pounds_per_foot_second
        self.__pounds_per_foot_second = self.__convert_from_base(DynamicViscosityUnits.PoundPerFootSecond)
        return self.__pounds_per_foot_second

    
    @property
    def millipascal_seconds(self) -> float:
        """
        
        """
        if self.__millipascal_seconds != None:
            return self.__millipascal_seconds
        self.__millipascal_seconds = self.__convert_from_base(DynamicViscosityUnits.MillipascalSecond)
        return self.__millipascal_seconds

    
    @property
    def micropascal_seconds(self) -> float:
        """
        
        """
        if self.__micropascal_seconds != None:
            return self.__micropascal_seconds
        self.__micropascal_seconds = self.__convert_from_base(DynamicViscosityUnits.MicropascalSecond)
        return self.__micropascal_seconds

    
    @property
    def centipoise(self) -> float:
        """
        
        """
        if self.__centipoise != None:
            return self.__centipoise
        self.__centipoise = self.__convert_from_base(DynamicViscosityUnits.Centipoise)
        return self.__centipoise

    
    def to_string(self, unit: DynamicViscosityUnits = DynamicViscosityUnits.NewtonSecondPerMeterSquared) -> str:
        """
        Format the DynamicViscosity to string.
        Note! the default format for DynamicViscosity is NewtonSecondPerMeterSquared.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == DynamicViscosityUnits.NewtonSecondPerMeterSquared:
            return f"""{self.newton_seconds_per_meter_squared} Ns/m²"""
        
        if unit == DynamicViscosityUnits.PascalSecond:
            return f"""{self.pascal_seconds} Pa·s"""
        
        if unit == DynamicViscosityUnits.Poise:
            return f"""{self.poise} P"""
        
        if unit == DynamicViscosityUnits.Reyn:
            return f"""{self.reyns} reyn"""
        
        if unit == DynamicViscosityUnits.PoundForceSecondPerSquareInch:
            return f"""{self.pounds_force_second_per_square_inch} lbf·s/in²"""
        
        if unit == DynamicViscosityUnits.PoundForceSecondPerSquareFoot:
            return f"""{self.pounds_force_second_per_square_foot} lbf·s/ft²"""
        
        if unit == DynamicViscosityUnits.PoundPerFootSecond:
            return f"""{self.pounds_per_foot_second} lb/ft·s"""
        
        if unit == DynamicViscosityUnits.MillipascalSecond:
            return f"""{self.millipascal_seconds} mPa·s"""
        
        if unit == DynamicViscosityUnits.MicropascalSecond:
            return f"""{self.micropascal_seconds} μPa·s"""
        
        if unit == DynamicViscosityUnits.Centipoise:
            return f"""{self.centipoise} cP"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: DynamicViscosityUnits = DynamicViscosityUnits.NewtonSecondPerMeterSquared) -> str:
        """
        Get DynamicViscosity unit abbreviation.
        Note! the default abbreviation for DynamicViscosity is NewtonSecondPerMeterSquared.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == DynamicViscosityUnits.NewtonSecondPerMeterSquared:
            return """Ns/m²"""
        
        if unit_abbreviation == DynamicViscosityUnits.PascalSecond:
            return """Pa·s"""
        
        if unit_abbreviation == DynamicViscosityUnits.Poise:
            return """P"""
        
        if unit_abbreviation == DynamicViscosityUnits.Reyn:
            return """reyn"""
        
        if unit_abbreviation == DynamicViscosityUnits.PoundForceSecondPerSquareInch:
            return """lbf·s/in²"""
        
        if unit_abbreviation == DynamicViscosityUnits.PoundForceSecondPerSquareFoot:
            return """lbf·s/ft²"""
        
        if unit_abbreviation == DynamicViscosityUnits.PoundPerFootSecond:
            return """lb/ft·s"""
        
        if unit_abbreviation == DynamicViscosityUnits.MillipascalSecond:
            return """mPa·s"""
        
        if unit_abbreviation == DynamicViscosityUnits.MicropascalSecond:
            return """μPa·s"""
        
        if unit_abbreviation == DynamicViscosityUnits.Centipoise:
            return """cP"""
        
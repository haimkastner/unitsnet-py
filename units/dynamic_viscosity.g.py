from enum import Enum
import math
import string


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
        
        MilliPascalSecond = 'milli_pascal_second'
        """
            
        """
        
        MicroPascalSecond = 'micro_pascal_second'
        """
            
        """
        
        CentiPoise = 'centi_poise'
        """
            
        """
        
    
class DynamicViscosity:
    """
    The dynamic (shear) viscosity of a fluid expresses its resistance to shearing flows, where adjacent layers move parallel to each other with different speeds

    Args:
        value (float): The value.
        from_unit (DynamicViscosityUnits): The DynamicViscosity unit to create from, The default unit is NewtonSecondPerMeterSquared
    """
    def __init__(self, value: float, from_unit: DynamicViscosityUnits = DynamicViscosityUnits.NewtonSecondPerMeterSquared):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__newton_seconds_per_meter_squared = None
        
        self.__pascal_seconds = None
        
        self.__poise = None
        
        self.__reyns = None
        
        self.__pounds_force_second_per_square_inch = None
        
        self.__pounds_force_second_per_square_foot = None
        
        self.__pounds_per_foot_second = None
        
        self.__milli_pascal_seconds = None
        
        self.__micro_pascal_seconds = None
        
        self.__centi_poise = None
        

    def __convert_from_base(self, from_unit: DynamicViscosityUnits) -> float:
        value = self.__value
        
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
        
        if from_unit == DynamicViscosityUnits.MilliPascalSecond:
            return ((value) / 0.001)
        
        if from_unit == DynamicViscosityUnits.MicroPascalSecond:
            return ((value) / 1e-06)
        
        if from_unit == DynamicViscosityUnits.CentiPoise:
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
        
        if to_unit == DynamicViscosityUnits.MilliPascalSecond:
            return ((value) * 0.001)
        
        if to_unit == DynamicViscosityUnits.MicroPascalSecond:
            return ((value) * 1e-06)
        
        if to_unit == DynamicViscosityUnits.CentiPoise:
            return ((value / 10) * 0.01)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
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
    def from_milli_pascal_seconds(milli_pascal_seconds: float):
        """
        Create a new instance of DynamicViscosity from a value in milli_pascal_seconds.

        

        :param meters: The DynamicViscosity value in milli_pascal_seconds.
        :type milli_pascal_seconds: float
        :return: A new instance of DynamicViscosity.
        :rtype: DynamicViscosity
        """
        return DynamicViscosity(milli_pascal_seconds, DynamicViscosityUnits.MilliPascalSecond)

    
    @staticmethod
    def from_micro_pascal_seconds(micro_pascal_seconds: float):
        """
        Create a new instance of DynamicViscosity from a value in micro_pascal_seconds.

        

        :param meters: The DynamicViscosity value in micro_pascal_seconds.
        :type micro_pascal_seconds: float
        :return: A new instance of DynamicViscosity.
        :rtype: DynamicViscosity
        """
        return DynamicViscosity(micro_pascal_seconds, DynamicViscosityUnits.MicroPascalSecond)

    
    @staticmethod
    def from_centi_poise(centi_poise: float):
        """
        Create a new instance of DynamicViscosity from a value in centi_poise.

        

        :param meters: The DynamicViscosity value in centi_poise.
        :type centi_poise: float
        :return: A new instance of DynamicViscosity.
        :rtype: DynamicViscosity
        """
        return DynamicViscosity(centi_poise, DynamicViscosityUnits.CentiPoise)

    
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
    def milli_pascal_seconds(self) -> float:
        """
        
        """
        if self.__milli_pascal_seconds != None:
            return self.__milli_pascal_seconds
        self.__milli_pascal_seconds = self.__convert_from_base(DynamicViscosityUnits.MilliPascalSecond)
        return self.__milli_pascal_seconds

    
    @property
    def micro_pascal_seconds(self) -> float:
        """
        
        """
        if self.__micro_pascal_seconds != None:
            return self.__micro_pascal_seconds
        self.__micro_pascal_seconds = self.__convert_from_base(DynamicViscosityUnits.MicroPascalSecond)
        return self.__micro_pascal_seconds

    
    @property
    def centi_poise(self) -> float:
        """
        
        """
        if self.__centi_poise != None:
            return self.__centi_poise
        self.__centi_poise = self.__convert_from_base(DynamicViscosityUnits.CentiPoise)
        return self.__centi_poise

    
    def to_string(self, unit: DynamicViscosityUnits = DynamicViscosityUnits.NewtonSecondPerMeterSquared) -> string:
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
        
        if unit == DynamicViscosityUnits.MilliPascalSecond:
            return f"""{self.milli_pascal_seconds} """
        
        if unit == DynamicViscosityUnits.MicroPascalSecond:
            return f"""{self.micro_pascal_seconds} """
        
        if unit == DynamicViscosityUnits.CentiPoise:
            return f"""{self.centi_poise} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: DynamicViscosityUnits = DynamicViscosityUnits.NewtonSecondPerMeterSquared) -> string:
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
        
        if unit_abbreviation == DynamicViscosityUnits.MilliPascalSecond:
            return """"""
        
        if unit_abbreviation == DynamicViscosityUnits.MicroPascalSecond:
            return """"""
        
        if unit_abbreviation == DynamicViscosityUnits.CentiPoise:
            return """"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, DynamicViscosity):
            raise TypeError("unsupported operand type(s) for +: 'DynamicViscosity' and '{}'".format(type(other).__name__))
        return DynamicViscosity(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, DynamicViscosity):
            raise TypeError("unsupported operand type(s) for *: 'DynamicViscosity' and '{}'".format(type(other).__name__))
        return DynamicViscosity(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, DynamicViscosity):
            raise TypeError("unsupported operand type(s) for -: 'DynamicViscosity' and '{}'".format(type(other).__name__))
        return DynamicViscosity(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, DynamicViscosity):
            raise TypeError("unsupported operand type(s) for /: 'DynamicViscosity' and '{}'".format(type(other).__name__))
        return DynamicViscosity(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, DynamicViscosity):
            raise TypeError("unsupported operand type(s) for %: 'DynamicViscosity' and '{}'".format(type(other).__name__))
        return DynamicViscosity(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, DynamicViscosity):
            raise TypeError("unsupported operand type(s) for **: 'DynamicViscosity' and '{}'".format(type(other).__name__))
        return DynamicViscosity(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, DynamicViscosity):
            raise TypeError("unsupported operand type(s) for ==: 'DynamicViscosity' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, DynamicViscosity):
            raise TypeError("unsupported operand type(s) for <: 'DynamicViscosity' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, DynamicViscosity):
            raise TypeError("unsupported operand type(s) for >: 'DynamicViscosity' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, DynamicViscosity):
            raise TypeError("unsupported operand type(s) for <=: 'DynamicViscosity' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, DynamicViscosity):
            raise TypeError("unsupported operand type(s) for >=: 'DynamicViscosity' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value
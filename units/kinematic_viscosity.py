from enum import Enum
import math
import string


class KinematicViscosityUnits(Enum):
        """
            KinematicViscosityUnits enumeration
        """
        
        SquareMeterPerSecond = 'square_meter_per_second'
        """
            
        """
        
        Stokes = 'stokes'
        """
            
        """
        
        SquareFootPerSecond = 'square_foot_per_second'
        """
            
        """
        
        NanoStokes = 'nano_stokes'
        """
            
        """
        
        MicroStokes = 'micro_stokes'
        """
            
        """
        
        MilliStokes = 'milli_stokes'
        """
            
        """
        
        CentiStokes = 'centi_stokes'
        """
            
        """
        
        DeciStokes = 'deci_stokes'
        """
            
        """
        
        KiloStokes = 'kilo_stokes'
        """
            
        """
        

class KinematicViscosity:
    """
    The viscosity of a fluid is a measure of its resistance to gradual deformation by shear stress or tensile stress.

    Args:
        value (float): The value.
        from_unit (KinematicViscosityUnits): The KinematicViscosity unit to create from, The default unit is SquareMeterPerSecond
    """
    def __init__(self, value: float, from_unit: KinematicViscosityUnits = KinematicViscosityUnits.SquareMeterPerSecond):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__square_meters_per_second = None
        
        self.__stokes = None
        
        self.__square_feet_per_second = None
        
        self.__nano_stokes = None
        
        self.__micro_stokes = None
        
        self.__milli_stokes = None
        
        self.__centi_stokes = None
        
        self.__deci_stokes = None
        
        self.__kilo_stokes = None
        

    def __convert_from_base(self, from_unit: KinematicViscosityUnits) -> float:
        value = self.__value
        
        if from_unit == KinematicViscosityUnits.SquareMeterPerSecond:
            return (value)
        
        if from_unit == KinematicViscosityUnits.Stokes:
            return (value * 1e4)
        
        if from_unit == KinematicViscosityUnits.SquareFootPerSecond:
            return (value * 10.7639)
        
        if from_unit == KinematicViscosityUnits.NanoStokes:
            return ((value * 1e4) / 1e-09)
        
        if from_unit == KinematicViscosityUnits.MicroStokes:
            return ((value * 1e4) / 1e-06)
        
        if from_unit == KinematicViscosityUnits.MilliStokes:
            return ((value * 1e4) / 0.001)
        
        if from_unit == KinematicViscosityUnits.CentiStokes:
            return ((value * 1e4) / 0.01)
        
        if from_unit == KinematicViscosityUnits.DeciStokes:
            return ((value * 1e4) / 0.1)
        
        if from_unit == KinematicViscosityUnits.KiloStokes:
            return ((value * 1e4) / 1000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: KinematicViscosityUnits) -> float:
        
        if to_unit == KinematicViscosityUnits.SquareMeterPerSecond:
            return (value)
        
        if to_unit == KinematicViscosityUnits.Stokes:
            return (value / 1e4)
        
        if to_unit == KinematicViscosityUnits.SquareFootPerSecond:
            return (value / 10.7639)
        
        if to_unit == KinematicViscosityUnits.NanoStokes:
            return ((value / 1e4) * 1e-09)
        
        if to_unit == KinematicViscosityUnits.MicroStokes:
            return ((value / 1e4) * 1e-06)
        
        if to_unit == KinematicViscosityUnits.MilliStokes:
            return ((value / 1e4) * 0.001)
        
        if to_unit == KinematicViscosityUnits.CentiStokes:
            return ((value / 1e4) * 0.01)
        
        if to_unit == KinematicViscosityUnits.DeciStokes:
            return ((value / 1e4) * 0.1)
        
        if to_unit == KinematicViscosityUnits.KiloStokes:
            return ((value / 1e4) * 1000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
    @staticmethod
    def from_square_meters_per_second(square_meters_per_second: float):
        """
        Create a new instance of KinematicViscosity from a value in square_meters_per_second.

        

        :param meters: The KinematicViscosity value in square_meters_per_second.
        :type square_meters_per_second: float
        :return: A new instance of KinematicViscosity.
        :rtype: KinematicViscosity
        """
        return KinematicViscosity(square_meters_per_second, KinematicViscosityUnits.SquareMeterPerSecond)

    
    @staticmethod
    def from_stokes(stokes: float):
        """
        Create a new instance of KinematicViscosity from a value in stokes.

        

        :param meters: The KinematicViscosity value in stokes.
        :type stokes: float
        :return: A new instance of KinematicViscosity.
        :rtype: KinematicViscosity
        """
        return KinematicViscosity(stokes, KinematicViscosityUnits.Stokes)

    
    @staticmethod
    def from_square_feet_per_second(square_feet_per_second: float):
        """
        Create a new instance of KinematicViscosity from a value in square_feet_per_second.

        

        :param meters: The KinematicViscosity value in square_feet_per_second.
        :type square_feet_per_second: float
        :return: A new instance of KinematicViscosity.
        :rtype: KinematicViscosity
        """
        return KinematicViscosity(square_feet_per_second, KinematicViscosityUnits.SquareFootPerSecond)

    
    @staticmethod
    def from_nano_stokes(nano_stokes: float):
        """
        Create a new instance of KinematicViscosity from a value in nano_stokes.

        

        :param meters: The KinematicViscosity value in nano_stokes.
        :type nano_stokes: float
        :return: A new instance of KinematicViscosity.
        :rtype: KinematicViscosity
        """
        return KinematicViscosity(nano_stokes, KinematicViscosityUnits.NanoStokes)

    
    @staticmethod
    def from_micro_stokes(micro_stokes: float):
        """
        Create a new instance of KinematicViscosity from a value in micro_stokes.

        

        :param meters: The KinematicViscosity value in micro_stokes.
        :type micro_stokes: float
        :return: A new instance of KinematicViscosity.
        :rtype: KinematicViscosity
        """
        return KinematicViscosity(micro_stokes, KinematicViscosityUnits.MicroStokes)

    
    @staticmethod
    def from_milli_stokes(milli_stokes: float):
        """
        Create a new instance of KinematicViscosity from a value in milli_stokes.

        

        :param meters: The KinematicViscosity value in milli_stokes.
        :type milli_stokes: float
        :return: A new instance of KinematicViscosity.
        :rtype: KinematicViscosity
        """
        return KinematicViscosity(milli_stokes, KinematicViscosityUnits.MilliStokes)

    
    @staticmethod
    def from_centi_stokes(centi_stokes: float):
        """
        Create a new instance of KinematicViscosity from a value in centi_stokes.

        

        :param meters: The KinematicViscosity value in centi_stokes.
        :type centi_stokes: float
        :return: A new instance of KinematicViscosity.
        :rtype: KinematicViscosity
        """
        return KinematicViscosity(centi_stokes, KinematicViscosityUnits.CentiStokes)

    
    @staticmethod
    def from_deci_stokes(deci_stokes: float):
        """
        Create a new instance of KinematicViscosity from a value in deci_stokes.

        

        :param meters: The KinematicViscosity value in deci_stokes.
        :type deci_stokes: float
        :return: A new instance of KinematicViscosity.
        :rtype: KinematicViscosity
        """
        return KinematicViscosity(deci_stokes, KinematicViscosityUnits.DeciStokes)

    
    @staticmethod
    def from_kilo_stokes(kilo_stokes: float):
        """
        Create a new instance of KinematicViscosity from a value in kilo_stokes.

        

        :param meters: The KinematicViscosity value in kilo_stokes.
        :type kilo_stokes: float
        :return: A new instance of KinematicViscosity.
        :rtype: KinematicViscosity
        """
        return KinematicViscosity(kilo_stokes, KinematicViscosityUnits.KiloStokes)

    
    @property
    def square_meters_per_second(self) -> float:
        """
        
        """
        if self.__square_meters_per_second != None:
            return self.__square_meters_per_second
        self.__square_meters_per_second = self.__convert_from_base(KinematicViscosityUnits.SquareMeterPerSecond)
        return self.__square_meters_per_second

    
    @property
    def stokes(self) -> float:
        """
        
        """
        if self.__stokes != None:
            return self.__stokes
        self.__stokes = self.__convert_from_base(KinematicViscosityUnits.Stokes)
        return self.__stokes

    
    @property
    def square_feet_per_second(self) -> float:
        """
        
        """
        if self.__square_feet_per_second != None:
            return self.__square_feet_per_second
        self.__square_feet_per_second = self.__convert_from_base(KinematicViscosityUnits.SquareFootPerSecond)
        return self.__square_feet_per_second

    
    @property
    def nano_stokes(self) -> float:
        """
        
        """
        if self.__nano_stokes != None:
            return self.__nano_stokes
        self.__nano_stokes = self.__convert_from_base(KinematicViscosityUnits.NanoStokes)
        return self.__nano_stokes

    
    @property
    def micro_stokes(self) -> float:
        """
        
        """
        if self.__micro_stokes != None:
            return self.__micro_stokes
        self.__micro_stokes = self.__convert_from_base(KinematicViscosityUnits.MicroStokes)
        return self.__micro_stokes

    
    @property
    def milli_stokes(self) -> float:
        """
        
        """
        if self.__milli_stokes != None:
            return self.__milli_stokes
        self.__milli_stokes = self.__convert_from_base(KinematicViscosityUnits.MilliStokes)
        return self.__milli_stokes

    
    @property
    def centi_stokes(self) -> float:
        """
        
        """
        if self.__centi_stokes != None:
            return self.__centi_stokes
        self.__centi_stokes = self.__convert_from_base(KinematicViscosityUnits.CentiStokes)
        return self.__centi_stokes

    
    @property
    def deci_stokes(self) -> float:
        """
        
        """
        if self.__deci_stokes != None:
            return self.__deci_stokes
        self.__deci_stokes = self.__convert_from_base(KinematicViscosityUnits.DeciStokes)
        return self.__deci_stokes

    
    @property
    def kilo_stokes(self) -> float:
        """
        
        """
        if self.__kilo_stokes != None:
            return self.__kilo_stokes
        self.__kilo_stokes = self.__convert_from_base(KinematicViscosityUnits.KiloStokes)
        return self.__kilo_stokes

    
    def to_string(self, unit: KinematicViscosityUnits = KinematicViscosityUnits.SquareMeterPerSecond) -> string:
        """
        Format the KinematicViscosity to string.
        Note! the default format for KinematicViscosity is SquareMeterPerSecond.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == KinematicViscosityUnits.SquareMeterPerSecond:
            return f"""{self.square_meters_per_second} m²/s"""
        
        if unit == KinematicViscosityUnits.Stokes:
            return f"""{self.stokes} St"""
        
        if unit == KinematicViscosityUnits.SquareFootPerSecond:
            return f"""{self.square_feet_per_second} ft²/s"""
        
        if unit == KinematicViscosityUnits.NanoStokes:
            return f"""{self.nano_stokes} """
        
        if unit == KinematicViscosityUnits.MicroStokes:
            return f"""{self.micro_stokes} """
        
        if unit == KinematicViscosityUnits.MilliStokes:
            return f"""{self.milli_stokes} """
        
        if unit == KinematicViscosityUnits.CentiStokes:
            return f"""{self.centi_stokes} """
        
        if unit == KinematicViscosityUnits.DeciStokes:
            return f"""{self.deci_stokes} """
        
        if unit == KinematicViscosityUnits.KiloStokes:
            return f"""{self.kilo_stokes} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: KinematicViscosityUnits = KinematicViscosityUnits.SquareMeterPerSecond) -> string:
        """
        Get KinematicViscosity unit abbreviation.
        Note! the default abbreviation for KinematicViscosity is SquareMeterPerSecond.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == KinematicViscosityUnits.SquareMeterPerSecond:
            return """m²/s"""
        
        if unit_abbreviation == KinematicViscosityUnits.Stokes:
            return """St"""
        
        if unit_abbreviation == KinematicViscosityUnits.SquareFootPerSecond:
            return """ft²/s"""
        
        if unit_abbreviation == KinematicViscosityUnits.NanoStokes:
            return """"""
        
        if unit_abbreviation == KinematicViscosityUnits.MicroStokes:
            return """"""
        
        if unit_abbreviation == KinematicViscosityUnits.MilliStokes:
            return """"""
        
        if unit_abbreviation == KinematicViscosityUnits.CentiStokes:
            return """"""
        
        if unit_abbreviation == KinematicViscosityUnits.DeciStokes:
            return """"""
        
        if unit_abbreviation == KinematicViscosityUnits.KiloStokes:
            return """"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, KinematicViscosity):
            raise TypeError("unsupported operand type(s) for +: 'KinematicViscosity' and '{}'".format(type(other).__name__))
        return KinematicViscosity(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, KinematicViscosity):
            raise TypeError("unsupported operand type(s) for *: 'KinematicViscosity' and '{}'".format(type(other).__name__))
        return KinematicViscosity(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, KinematicViscosity):
            raise TypeError("unsupported operand type(s) for -: 'KinematicViscosity' and '{}'".format(type(other).__name__))
        return KinematicViscosity(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, KinematicViscosity):
            raise TypeError("unsupported operand type(s) for /: 'KinematicViscosity' and '{}'".format(type(other).__name__))
        return KinematicViscosity(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, KinematicViscosity):
            raise TypeError("unsupported operand type(s) for %: 'KinematicViscosity' and '{}'".format(type(other).__name__))
        return KinematicViscosity(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, KinematicViscosity):
            raise TypeError("unsupported operand type(s) for **: 'KinematicViscosity' and '{}'".format(type(other).__name__))
        return KinematicViscosity(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, KinematicViscosity):
            raise TypeError("unsupported operand type(s) for ==: 'KinematicViscosity' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, KinematicViscosity):
            raise TypeError("unsupported operand type(s) for <: 'KinematicViscosity' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, KinematicViscosity):
            raise TypeError("unsupported operand type(s) for >: 'KinematicViscosity' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, KinematicViscosity):
            raise TypeError("unsupported operand type(s) for <=: 'KinematicViscosity' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, KinematicViscosity):
            raise TypeError("unsupported operand type(s) for >=: 'KinematicViscosity' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value
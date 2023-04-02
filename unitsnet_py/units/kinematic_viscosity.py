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
        
        Nanostokes = 'nanostokes'
        """
            
        """
        
        Microstokes = 'microstokes'
        """
            
        """
        
        Millistokes = 'millistokes'
        """
            
        """
        
        Centistokes = 'centistokes'
        """
            
        """
        
        Decistokes = 'decistokes'
        """
            
        """
        
        Kilostokes = 'kilostokes'
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
        
        self.__nanostokes = None
        
        self.__microstokes = None
        
        self.__millistokes = None
        
        self.__centistokes = None
        
        self.__decistokes = None
        
        self.__kilostokes = None
        

    def __convert_from_base(self, from_unit: KinematicViscosityUnits) -> float:
        value = self.__value
        
        if from_unit == KinematicViscosityUnits.SquareMeterPerSecond:
            return (value)
        
        if from_unit == KinematicViscosityUnits.Stokes:
            return (value * 1e4)
        
        if from_unit == KinematicViscosityUnits.SquareFootPerSecond:
            return (value * 10.7639)
        
        if from_unit == KinematicViscosityUnits.Nanostokes:
            return ((value * 1e4) / 1e-09)
        
        if from_unit == KinematicViscosityUnits.Microstokes:
            return ((value * 1e4) / 1e-06)
        
        if from_unit == KinematicViscosityUnits.Millistokes:
            return ((value * 1e4) / 0.001)
        
        if from_unit == KinematicViscosityUnits.Centistokes:
            return ((value * 1e4) / 0.01)
        
        if from_unit == KinematicViscosityUnits.Decistokes:
            return ((value * 1e4) / 0.1)
        
        if from_unit == KinematicViscosityUnits.Kilostokes:
            return ((value * 1e4) / 1000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: KinematicViscosityUnits) -> float:
        
        if to_unit == KinematicViscosityUnits.SquareMeterPerSecond:
            return (value)
        
        if to_unit == KinematicViscosityUnits.Stokes:
            return (value / 1e4)
        
        if to_unit == KinematicViscosityUnits.SquareFootPerSecond:
            return (value / 10.7639)
        
        if to_unit == KinematicViscosityUnits.Nanostokes:
            return ((value / 1e4) * 1e-09)
        
        if to_unit == KinematicViscosityUnits.Microstokes:
            return ((value / 1e4) * 1e-06)
        
        if to_unit == KinematicViscosityUnits.Millistokes:
            return ((value / 1e4) * 0.001)
        
        if to_unit == KinematicViscosityUnits.Centistokes:
            return ((value / 1e4) * 0.01)
        
        if to_unit == KinematicViscosityUnits.Decistokes:
            return ((value / 1e4) * 0.1)
        
        if to_unit == KinematicViscosityUnits.Kilostokes:
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
    def from_nanostokes(nanostokes: float):
        """
        Create a new instance of KinematicViscosity from a value in nanostokes.

        

        :param meters: The KinematicViscosity value in nanostokes.
        :type nanostokes: float
        :return: A new instance of KinematicViscosity.
        :rtype: KinematicViscosity
        """
        return KinematicViscosity(nanostokes, KinematicViscosityUnits.Nanostokes)

    
    @staticmethod
    def from_microstokes(microstokes: float):
        """
        Create a new instance of KinematicViscosity from a value in microstokes.

        

        :param meters: The KinematicViscosity value in microstokes.
        :type microstokes: float
        :return: A new instance of KinematicViscosity.
        :rtype: KinematicViscosity
        """
        return KinematicViscosity(microstokes, KinematicViscosityUnits.Microstokes)

    
    @staticmethod
    def from_millistokes(millistokes: float):
        """
        Create a new instance of KinematicViscosity from a value in millistokes.

        

        :param meters: The KinematicViscosity value in millistokes.
        :type millistokes: float
        :return: A new instance of KinematicViscosity.
        :rtype: KinematicViscosity
        """
        return KinematicViscosity(millistokes, KinematicViscosityUnits.Millistokes)

    
    @staticmethod
    def from_centistokes(centistokes: float):
        """
        Create a new instance of KinematicViscosity from a value in centistokes.

        

        :param meters: The KinematicViscosity value in centistokes.
        :type centistokes: float
        :return: A new instance of KinematicViscosity.
        :rtype: KinematicViscosity
        """
        return KinematicViscosity(centistokes, KinematicViscosityUnits.Centistokes)

    
    @staticmethod
    def from_decistokes(decistokes: float):
        """
        Create a new instance of KinematicViscosity from a value in decistokes.

        

        :param meters: The KinematicViscosity value in decistokes.
        :type decistokes: float
        :return: A new instance of KinematicViscosity.
        :rtype: KinematicViscosity
        """
        return KinematicViscosity(decistokes, KinematicViscosityUnits.Decistokes)

    
    @staticmethod
    def from_kilostokes(kilostokes: float):
        """
        Create a new instance of KinematicViscosity from a value in kilostokes.

        

        :param meters: The KinematicViscosity value in kilostokes.
        :type kilostokes: float
        :return: A new instance of KinematicViscosity.
        :rtype: KinematicViscosity
        """
        return KinematicViscosity(kilostokes, KinematicViscosityUnits.Kilostokes)

    
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
    def nanostokes(self) -> float:
        """
        
        """
        if self.__nanostokes != None:
            return self.__nanostokes
        self.__nanostokes = self.__convert_from_base(KinematicViscosityUnits.Nanostokes)
        return self.__nanostokes

    
    @property
    def microstokes(self) -> float:
        """
        
        """
        if self.__microstokes != None:
            return self.__microstokes
        self.__microstokes = self.__convert_from_base(KinematicViscosityUnits.Microstokes)
        return self.__microstokes

    
    @property
    def millistokes(self) -> float:
        """
        
        """
        if self.__millistokes != None:
            return self.__millistokes
        self.__millistokes = self.__convert_from_base(KinematicViscosityUnits.Millistokes)
        return self.__millistokes

    
    @property
    def centistokes(self) -> float:
        """
        
        """
        if self.__centistokes != None:
            return self.__centistokes
        self.__centistokes = self.__convert_from_base(KinematicViscosityUnits.Centistokes)
        return self.__centistokes

    
    @property
    def decistokes(self) -> float:
        """
        
        """
        if self.__decistokes != None:
            return self.__decistokes
        self.__decistokes = self.__convert_from_base(KinematicViscosityUnits.Decistokes)
        return self.__decistokes

    
    @property
    def kilostokes(self) -> float:
        """
        
        """
        if self.__kilostokes != None:
            return self.__kilostokes
        self.__kilostokes = self.__convert_from_base(KinematicViscosityUnits.Kilostokes)
        return self.__kilostokes

    
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
        
        if unit == KinematicViscosityUnits.Nanostokes:
            return f"""{self.nanostokes} """
        
        if unit == KinematicViscosityUnits.Microstokes:
            return f"""{self.microstokes} """
        
        if unit == KinematicViscosityUnits.Millistokes:
            return f"""{self.millistokes} """
        
        if unit == KinematicViscosityUnits.Centistokes:
            return f"""{self.centistokes} """
        
        if unit == KinematicViscosityUnits.Decistokes:
            return f"""{self.decistokes} """
        
        if unit == KinematicViscosityUnits.Kilostokes:
            return f"""{self.kilostokes} """
        
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
        
        if unit_abbreviation == KinematicViscosityUnits.Nanostokes:
            return """"""
        
        if unit_abbreviation == KinematicViscosityUnits.Microstokes:
            return """"""
        
        if unit_abbreviation == KinematicViscosityUnits.Millistokes:
            return """"""
        
        if unit_abbreviation == KinematicViscosityUnits.Centistokes:
            return """"""
        
        if unit_abbreviation == KinematicViscosityUnits.Decistokes:
            return """"""
        
        if unit_abbreviation == KinematicViscosityUnits.Kilostokes:
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
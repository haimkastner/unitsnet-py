from enum import Enum
import math
import string


class AngleUnits(Enum):
        """
            AngleUnits enumeration
        """
        
        Radian = 'radian'
        """
            
        """
        
        Degree = 'degree'
        """
            
        """
        
        Arcminute = 'arcminute'
        """
            
        """
        
        Arcsecond = 'arcsecond'
        """
            
        """
        
        Gradian = 'gradian'
        """
            
        """
        
        NatoMil = 'nato_mil'
        """
            
        """
        
        Revolution = 'revolution'
        """
            
        """
        
        Tilt = 'tilt'
        """
            
        """
        
        NanoRadian = 'nano_radian'
        """
            
        """
        
        MicroRadian = 'micro_radian'
        """
            
        """
        
        MilliRadian = 'milli_radian'
        """
            
        """
        
        CentiRadian = 'centi_radian'
        """
            
        """
        
        DeciRadian = 'deci_radian'
        """
            
        """
        
        NanoDegree = 'nano_degree'
        """
            
        """
        
        MicroDegree = 'micro_degree'
        """
            
        """
        
        MilliDegree = 'milli_degree'
        """
            
        """
        
    
class Angle:
    """
    In geometry, an angle is the figure formed by two rays, called the sides of the angle, sharing a common endpoint, called the vertex of the angle.

    Args:
        value (float): The value.
        from_unit (AngleUnits): The Angle unit to create from, The default unit is Degree
    """
    def __init__(self, value: float, from_unit: AngleUnits = AngleUnits.Degree):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__radians = None
        
        self.__degrees = None
        
        self.__arcminutes = None
        
        self.__arcseconds = None
        
        self.__gradians = None
        
        self.__nato_mils = None
        
        self.__revolutions = None
        
        self.__tilt = None
        
        self.__nano_radians = None
        
        self.__micro_radians = None
        
        self.__milli_radians = None
        
        self.__centi_radians = None
        
        self.__deci_radians = None
        
        self.__nano_degrees = None
        
        self.__micro_degrees = None
        
        self.__milli_degrees = None
        

    def __convert_from_base(self, from_unit: AngleUnits) -> float:
        value = self.__value
        
        if from_unit == AngleUnits.Radian:
            return (value / 180 * math.pi)
        
        if from_unit == AngleUnits.Degree:
            return (value)
        
        if from_unit == AngleUnits.Arcminute:
            return (value * 60)
        
        if from_unit == AngleUnits.Arcsecond:
            return (value * 3600)
        
        if from_unit == AngleUnits.Gradian:
            return (value / 0.9)
        
        if from_unit == AngleUnits.NatoMil:
            return (value * 160 / 9)
        
        if from_unit == AngleUnits.Revolution:
            return (value / 360)
        
        if from_unit == AngleUnits.Tilt:
            return (math.sin(value / 180 * math.pi))
        
        if from_unit == AngleUnits.NanoRadian:
            return ((value / 180 * math.pi) / 1e-09)
        
        if from_unit == AngleUnits.MicroRadian:
            return ((value / 180 * math.pi) / 1e-06)
        
        if from_unit == AngleUnits.MilliRadian:
            return ((value / 180 * math.pi) / 0.001)
        
        if from_unit == AngleUnits.CentiRadian:
            return ((value / 180 * math.pi) / 0.01)
        
        if from_unit == AngleUnits.DeciRadian:
            return ((value / 180 * math.pi) / 0.1)
        
        if from_unit == AngleUnits.NanoDegree:
            return ((value) / 1e-09)
        
        if from_unit == AngleUnits.MicroDegree:
            return ((value) / 1e-06)
        
        if from_unit == AngleUnits.MilliDegree:
            return ((value) / 0.001)
        
        return None


    def __convert_to_base(self, value: float, to_unit: AngleUnits) -> float:
        
        if to_unit == AngleUnits.Radian:
            return (value * 180 / math.pi)
        
        if to_unit == AngleUnits.Degree:
            return (value)
        
        if to_unit == AngleUnits.Arcminute:
            return (value / 60)
        
        if to_unit == AngleUnits.Arcsecond:
            return (value / 3600)
        
        if to_unit == AngleUnits.Gradian:
            return (value * 0.9)
        
        if to_unit == AngleUnits.NatoMil:
            return (value * 9 / 160)
        
        if to_unit == AngleUnits.Revolution:
            return (value * 360)
        
        if to_unit == AngleUnits.Tilt:
            return (math.asin(value) * 180 / math.pi)
        
        if to_unit == AngleUnits.NanoRadian:
            return ((value * 180 / math.pi) * 1e-09)
        
        if to_unit == AngleUnits.MicroRadian:
            return ((value * 180 / math.pi) * 1e-06)
        
        if to_unit == AngleUnits.MilliRadian:
            return ((value * 180 / math.pi) * 0.001)
        
        if to_unit == AngleUnits.CentiRadian:
            return ((value * 180 / math.pi) * 0.01)
        
        if to_unit == AngleUnits.DeciRadian:
            return ((value * 180 / math.pi) * 0.1)
        
        if to_unit == AngleUnits.NanoDegree:
            return ((value) * 1e-09)
        
        if to_unit == AngleUnits.MicroDegree:
            return ((value) * 1e-06)
        
        if to_unit == AngleUnits.MilliDegree:
            return ((value) * 0.001)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
    @staticmethod
    def from_radians(radians: float):
        """
        Create a new instance of Angle from a value in radians.

        

        :param meters: The Angle value in radians.
        :type radians: float
        :return: A new instance of Angle.
        :rtype: Angle
        """
        return Angle(radians, AngleUnits.Radian)

    
    @staticmethod
    def from_degrees(degrees: float):
        """
        Create a new instance of Angle from a value in degrees.

        

        :param meters: The Angle value in degrees.
        :type degrees: float
        :return: A new instance of Angle.
        :rtype: Angle
        """
        return Angle(degrees, AngleUnits.Degree)

    
    @staticmethod
    def from_arcminutes(arcminutes: float):
        """
        Create a new instance of Angle from a value in arcminutes.

        

        :param meters: The Angle value in arcminutes.
        :type arcminutes: float
        :return: A new instance of Angle.
        :rtype: Angle
        """
        return Angle(arcminutes, AngleUnits.Arcminute)

    
    @staticmethod
    def from_arcseconds(arcseconds: float):
        """
        Create a new instance of Angle from a value in arcseconds.

        

        :param meters: The Angle value in arcseconds.
        :type arcseconds: float
        :return: A new instance of Angle.
        :rtype: Angle
        """
        return Angle(arcseconds, AngleUnits.Arcsecond)

    
    @staticmethod
    def from_gradians(gradians: float):
        """
        Create a new instance of Angle from a value in gradians.

        

        :param meters: The Angle value in gradians.
        :type gradians: float
        :return: A new instance of Angle.
        :rtype: Angle
        """
        return Angle(gradians, AngleUnits.Gradian)

    
    @staticmethod
    def from_nato_mils(nato_mils: float):
        """
        Create a new instance of Angle from a value in nato_mils.

        

        :param meters: The Angle value in nato_mils.
        :type nato_mils: float
        :return: A new instance of Angle.
        :rtype: Angle
        """
        return Angle(nato_mils, AngleUnits.NatoMil)

    
    @staticmethod
    def from_revolutions(revolutions: float):
        """
        Create a new instance of Angle from a value in revolutions.

        

        :param meters: The Angle value in revolutions.
        :type revolutions: float
        :return: A new instance of Angle.
        :rtype: Angle
        """
        return Angle(revolutions, AngleUnits.Revolution)

    
    @staticmethod
    def from_tilt(tilt: float):
        """
        Create a new instance of Angle from a value in tilt.

        

        :param meters: The Angle value in tilt.
        :type tilt: float
        :return: A new instance of Angle.
        :rtype: Angle
        """
        return Angle(tilt, AngleUnits.Tilt)

    
    @staticmethod
    def from_nano_radians(nano_radians: float):
        """
        Create a new instance of Angle from a value in nano_radians.

        

        :param meters: The Angle value in nano_radians.
        :type nano_radians: float
        :return: A new instance of Angle.
        :rtype: Angle
        """
        return Angle(nano_radians, AngleUnits.NanoRadian)

    
    @staticmethod
    def from_micro_radians(micro_radians: float):
        """
        Create a new instance of Angle from a value in micro_radians.

        

        :param meters: The Angle value in micro_radians.
        :type micro_radians: float
        :return: A new instance of Angle.
        :rtype: Angle
        """
        return Angle(micro_radians, AngleUnits.MicroRadian)

    
    @staticmethod
    def from_milli_radians(milli_radians: float):
        """
        Create a new instance of Angle from a value in milli_radians.

        

        :param meters: The Angle value in milli_radians.
        :type milli_radians: float
        :return: A new instance of Angle.
        :rtype: Angle
        """
        return Angle(milli_radians, AngleUnits.MilliRadian)

    
    @staticmethod
    def from_centi_radians(centi_radians: float):
        """
        Create a new instance of Angle from a value in centi_radians.

        

        :param meters: The Angle value in centi_radians.
        :type centi_radians: float
        :return: A new instance of Angle.
        :rtype: Angle
        """
        return Angle(centi_radians, AngleUnits.CentiRadian)

    
    @staticmethod
    def from_deci_radians(deci_radians: float):
        """
        Create a new instance of Angle from a value in deci_radians.

        

        :param meters: The Angle value in deci_radians.
        :type deci_radians: float
        :return: A new instance of Angle.
        :rtype: Angle
        """
        return Angle(deci_radians, AngleUnits.DeciRadian)

    
    @staticmethod
    def from_nano_degrees(nano_degrees: float):
        """
        Create a new instance of Angle from a value in nano_degrees.

        

        :param meters: The Angle value in nano_degrees.
        :type nano_degrees: float
        :return: A new instance of Angle.
        :rtype: Angle
        """
        return Angle(nano_degrees, AngleUnits.NanoDegree)

    
    @staticmethod
    def from_micro_degrees(micro_degrees: float):
        """
        Create a new instance of Angle from a value in micro_degrees.

        

        :param meters: The Angle value in micro_degrees.
        :type micro_degrees: float
        :return: A new instance of Angle.
        :rtype: Angle
        """
        return Angle(micro_degrees, AngleUnits.MicroDegree)

    
    @staticmethod
    def from_milli_degrees(milli_degrees: float):
        """
        Create a new instance of Angle from a value in milli_degrees.

        

        :param meters: The Angle value in milli_degrees.
        :type milli_degrees: float
        :return: A new instance of Angle.
        :rtype: Angle
        """
        return Angle(milli_degrees, AngleUnits.MilliDegree)

    
    @property
    def radians(self) -> float:
        """
        
        """
        if self.__radians != None:
            return self.__radians
        self.__radians = self.__convert_from_base(AngleUnits.Radian)
        return self.__radians

    
    @property
    def degrees(self) -> float:
        """
        
        """
        if self.__degrees != None:
            return self.__degrees
        self.__degrees = self.__convert_from_base(AngleUnits.Degree)
        return self.__degrees

    
    @property
    def arcminutes(self) -> float:
        """
        
        """
        if self.__arcminutes != None:
            return self.__arcminutes
        self.__arcminutes = self.__convert_from_base(AngleUnits.Arcminute)
        return self.__arcminutes

    
    @property
    def arcseconds(self) -> float:
        """
        
        """
        if self.__arcseconds != None:
            return self.__arcseconds
        self.__arcseconds = self.__convert_from_base(AngleUnits.Arcsecond)
        return self.__arcseconds

    
    @property
    def gradians(self) -> float:
        """
        
        """
        if self.__gradians != None:
            return self.__gradians
        self.__gradians = self.__convert_from_base(AngleUnits.Gradian)
        return self.__gradians

    
    @property
    def nato_mils(self) -> float:
        """
        
        """
        if self.__nato_mils != None:
            return self.__nato_mils
        self.__nato_mils = self.__convert_from_base(AngleUnits.NatoMil)
        return self.__nato_mils

    
    @property
    def revolutions(self) -> float:
        """
        
        """
        if self.__revolutions != None:
            return self.__revolutions
        self.__revolutions = self.__convert_from_base(AngleUnits.Revolution)
        return self.__revolutions

    
    @property
    def tilt(self) -> float:
        """
        
        """
        if self.__tilt != None:
            return self.__tilt
        self.__tilt = self.__convert_from_base(AngleUnits.Tilt)
        return self.__tilt

    
    @property
    def nano_radians(self) -> float:
        """
        
        """
        if self.__nano_radians != None:
            return self.__nano_radians
        self.__nano_radians = self.__convert_from_base(AngleUnits.NanoRadian)
        return self.__nano_radians

    
    @property
    def micro_radians(self) -> float:
        """
        
        """
        if self.__micro_radians != None:
            return self.__micro_radians
        self.__micro_radians = self.__convert_from_base(AngleUnits.MicroRadian)
        return self.__micro_radians

    
    @property
    def milli_radians(self) -> float:
        """
        
        """
        if self.__milli_radians != None:
            return self.__milli_radians
        self.__milli_radians = self.__convert_from_base(AngleUnits.MilliRadian)
        return self.__milli_radians

    
    @property
    def centi_radians(self) -> float:
        """
        
        """
        if self.__centi_radians != None:
            return self.__centi_radians
        self.__centi_radians = self.__convert_from_base(AngleUnits.CentiRadian)
        return self.__centi_radians

    
    @property
    def deci_radians(self) -> float:
        """
        
        """
        if self.__deci_radians != None:
            return self.__deci_radians
        self.__deci_radians = self.__convert_from_base(AngleUnits.DeciRadian)
        return self.__deci_radians

    
    @property
    def nano_degrees(self) -> float:
        """
        
        """
        if self.__nano_degrees != None:
            return self.__nano_degrees
        self.__nano_degrees = self.__convert_from_base(AngleUnits.NanoDegree)
        return self.__nano_degrees

    
    @property
    def micro_degrees(self) -> float:
        """
        
        """
        if self.__micro_degrees != None:
            return self.__micro_degrees
        self.__micro_degrees = self.__convert_from_base(AngleUnits.MicroDegree)
        return self.__micro_degrees

    
    @property
    def milli_degrees(self) -> float:
        """
        
        """
        if self.__milli_degrees != None:
            return self.__milli_degrees
        self.__milli_degrees = self.__convert_from_base(AngleUnits.MilliDegree)
        return self.__milli_degrees

    
    def to_string(self, unit: AngleUnits = AngleUnits.Degree) -> string:
        """
        Format the Angle to string.
        Note! the default format for Angle is Degree.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == AngleUnits.Radian:
            return f"""{self.radians} rad"""
        
        if unit == AngleUnits.Degree:
            return f"""{self.degrees} °"""
        
        if unit == AngleUnits.Arcminute:
            return f"""{self.arcminutes} '"""
        
        if unit == AngleUnits.Arcsecond:
            return f"""{self.arcseconds} ″"""
        
        if unit == AngleUnits.Gradian:
            return f"""{self.gradians} g"""
        
        if unit == AngleUnits.NatoMil:
            return f"""{self.nato_mils} mil"""
        
        if unit == AngleUnits.Revolution:
            return f"""{self.revolutions} r"""
        
        if unit == AngleUnits.Tilt:
            return f"""{self.tilt} sin(θ)"""
        
        if unit == AngleUnits.NanoRadian:
            return f"""{self.nano_radians} """
        
        if unit == AngleUnits.MicroRadian:
            return f"""{self.micro_radians} """
        
        if unit == AngleUnits.MilliRadian:
            return f"""{self.milli_radians} """
        
        if unit == AngleUnits.CentiRadian:
            return f"""{self.centi_radians} """
        
        if unit == AngleUnits.DeciRadian:
            return f"""{self.deci_radians} """
        
        if unit == AngleUnits.NanoDegree:
            return f"""{self.nano_degrees} """
        
        if unit == AngleUnits.MicroDegree:
            return f"""{self.micro_degrees} """
        
        if unit == AngleUnits.MilliDegree:
            return f"""{self.milli_degrees} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: AngleUnits = AngleUnits.Degree) -> string:
        """
        Get Angle unit abbreviation.
        Note! the default abbreviation for Angle is Degree.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == AngleUnits.Radian:
            return """rad"""
        
        if unit_abbreviation == AngleUnits.Degree:
            return """°"""
        
        if unit_abbreviation == AngleUnits.Arcminute:
            return """'"""
        
        if unit_abbreviation == AngleUnits.Arcsecond:
            return """″"""
        
        if unit_abbreviation == AngleUnits.Gradian:
            return """g"""
        
        if unit_abbreviation == AngleUnits.NatoMil:
            return """mil"""
        
        if unit_abbreviation == AngleUnits.Revolution:
            return """r"""
        
        if unit_abbreviation == AngleUnits.Tilt:
            return """sin(θ)"""
        
        if unit_abbreviation == AngleUnits.NanoRadian:
            return """"""
        
        if unit_abbreviation == AngleUnits.MicroRadian:
            return """"""
        
        if unit_abbreviation == AngleUnits.MilliRadian:
            return """"""
        
        if unit_abbreviation == AngleUnits.CentiRadian:
            return """"""
        
        if unit_abbreviation == AngleUnits.DeciRadian:
            return """"""
        
        if unit_abbreviation == AngleUnits.NanoDegree:
            return """"""
        
        if unit_abbreviation == AngleUnits.MicroDegree:
            return """"""
        
        if unit_abbreviation == AngleUnits.MilliDegree:
            return """"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, Angle):
            raise TypeError("unsupported operand type(s) for +: 'Angle' and '{}'".format(type(other).__name__))
        return Angle(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, Angle):
            raise TypeError("unsupported operand type(s) for *: 'Angle' and '{}'".format(type(other).__name__))
        return Angle(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, Angle):
            raise TypeError("unsupported operand type(s) for -: 'Angle' and '{}'".format(type(other).__name__))
        return Angle(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, Angle):
            raise TypeError("unsupported operand type(s) for /: 'Angle' and '{}'".format(type(other).__name__))
        return Angle(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, Angle):
            raise TypeError("unsupported operand type(s) for %: 'Angle' and '{}'".format(type(other).__name__))
        return Angle(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, Angle):
            raise TypeError("unsupported operand type(s) for **: 'Angle' and '{}'".format(type(other).__name__))
        return Angle(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, Angle):
            raise TypeError("unsupported operand type(s) for ==: 'Angle' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, Angle):
            raise TypeError("unsupported operand type(s) for <: 'Angle' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, Angle):
            raise TypeError("unsupported operand type(s) for >: 'Angle' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, Angle):
            raise TypeError("unsupported operand type(s) for <=: 'Angle' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, Angle):
            raise TypeError("unsupported operand type(s) for >=: 'Angle' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value
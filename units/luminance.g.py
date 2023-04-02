from enum import Enum
import math
import string


class LuminanceUnits(Enum):
        """
            LuminanceUnits enumeration
        """
        
        CandelaPerSquareMeter = 'candela_per_square_meter'
        """
            
        """
        
        CandelaPerSquareFoot = 'candela_per_square_foot'
        """
            
        """
        
        CandelaPerSquareInch = 'candela_per_square_inch'
        """
            
        """
        
        Nit = 'nit'
        """
            
        """
        
        NanoCandelaPerSquareMeter = 'nano_candela_per_square_meter'
        """
            
        """
        
        MicroCandelaPerSquareMeter = 'micro_candela_per_square_meter'
        """
            
        """
        
        MilliCandelaPerSquareMeter = 'milli_candela_per_square_meter'
        """
            
        """
        
        CentiCandelaPerSquareMeter = 'centi_candela_per_square_meter'
        """
            
        """
        
        DeciCandelaPerSquareMeter = 'deci_candela_per_square_meter'
        """
            
        """
        
        KiloCandelaPerSquareMeter = 'kilo_candela_per_square_meter'
        """
            
        """
        
    
class Luminance:
    """
    None

    Args:
        value (float): The value.
        from_unit (LuminanceUnits): The Luminance unit to create from, The default unit is CandelaPerSquareMeter
    """
    def __init__(self, value: float, from_unit: LuminanceUnits = LuminanceUnits.CandelaPerSquareMeter):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__candelas_per_square_meter = None
        
        self.__candelas_per_square_foot = None
        
        self.__candelas_per_square_inch = None
        
        self.__nits = None
        
        self.__nano_candelas_per_square_meter = None
        
        self.__micro_candelas_per_square_meter = None
        
        self.__milli_candelas_per_square_meter = None
        
        self.__centi_candelas_per_square_meter = None
        
        self.__deci_candelas_per_square_meter = None
        
        self.__kilo_candelas_per_square_meter = None
        

    def __convert_from_base(self, from_unit: LuminanceUnits) -> float:
        value = self.__value
        
        if from_unit == LuminanceUnits.CandelaPerSquareMeter:
            return (value)
        
        if from_unit == LuminanceUnits.CandelaPerSquareFoot:
            return (value/ 1.07639e1)
        
        if from_unit == LuminanceUnits.CandelaPerSquareInch:
            return (value/ 1.5500031e3)
        
        if from_unit == LuminanceUnits.Nit:
            return (value)
        
        if from_unit == LuminanceUnits.NanoCandelaPerSquareMeter:
            return ((value) / 1e-09)
        
        if from_unit == LuminanceUnits.MicroCandelaPerSquareMeter:
            return ((value) / 1e-06)
        
        if from_unit == LuminanceUnits.MilliCandelaPerSquareMeter:
            return ((value) / 0.001)
        
        if from_unit == LuminanceUnits.CentiCandelaPerSquareMeter:
            return ((value) / 0.01)
        
        if from_unit == LuminanceUnits.DeciCandelaPerSquareMeter:
            return ((value) / 0.1)
        
        if from_unit == LuminanceUnits.KiloCandelaPerSquareMeter:
            return ((value) / 1000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: LuminanceUnits) -> float:
        
        if to_unit == LuminanceUnits.CandelaPerSquareMeter:
            return (value)
        
        if to_unit == LuminanceUnits.CandelaPerSquareFoot:
            return (value* 1.07639e1)
        
        if to_unit == LuminanceUnits.CandelaPerSquareInch:
            return (value* 1.5500031e3)
        
        if to_unit == LuminanceUnits.Nit:
            return (value)
        
        if to_unit == LuminanceUnits.NanoCandelaPerSquareMeter:
            return ((value) * 1e-09)
        
        if to_unit == LuminanceUnits.MicroCandelaPerSquareMeter:
            return ((value) * 1e-06)
        
        if to_unit == LuminanceUnits.MilliCandelaPerSquareMeter:
            return ((value) * 0.001)
        
        if to_unit == LuminanceUnits.CentiCandelaPerSquareMeter:
            return ((value) * 0.01)
        
        if to_unit == LuminanceUnits.DeciCandelaPerSquareMeter:
            return ((value) * 0.1)
        
        if to_unit == LuminanceUnits.KiloCandelaPerSquareMeter:
            return ((value) * 1000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
    @staticmethod
    def from_candelas_per_square_meter(candelas_per_square_meter: float):
        """
        Create a new instance of Luminance from a value in candelas_per_square_meter.

        

        :param meters: The Luminance value in candelas_per_square_meter.
        :type candelas_per_square_meter: float
        :return: A new instance of Luminance.
        :rtype: Luminance
        """
        return Luminance(candelas_per_square_meter, LuminanceUnits.CandelaPerSquareMeter)

    
    @staticmethod
    def from_candelas_per_square_foot(candelas_per_square_foot: float):
        """
        Create a new instance of Luminance from a value in candelas_per_square_foot.

        

        :param meters: The Luminance value in candelas_per_square_foot.
        :type candelas_per_square_foot: float
        :return: A new instance of Luminance.
        :rtype: Luminance
        """
        return Luminance(candelas_per_square_foot, LuminanceUnits.CandelaPerSquareFoot)

    
    @staticmethod
    def from_candelas_per_square_inch(candelas_per_square_inch: float):
        """
        Create a new instance of Luminance from a value in candelas_per_square_inch.

        

        :param meters: The Luminance value in candelas_per_square_inch.
        :type candelas_per_square_inch: float
        :return: A new instance of Luminance.
        :rtype: Luminance
        """
        return Luminance(candelas_per_square_inch, LuminanceUnits.CandelaPerSquareInch)

    
    @staticmethod
    def from_nits(nits: float):
        """
        Create a new instance of Luminance from a value in nits.

        

        :param meters: The Luminance value in nits.
        :type nits: float
        :return: A new instance of Luminance.
        :rtype: Luminance
        """
        return Luminance(nits, LuminanceUnits.Nit)

    
    @staticmethod
    def from_nano_candelas_per_square_meter(nano_candelas_per_square_meter: float):
        """
        Create a new instance of Luminance from a value in nano_candelas_per_square_meter.

        

        :param meters: The Luminance value in nano_candelas_per_square_meter.
        :type nano_candelas_per_square_meter: float
        :return: A new instance of Luminance.
        :rtype: Luminance
        """
        return Luminance(nano_candelas_per_square_meter, LuminanceUnits.NanoCandelaPerSquareMeter)

    
    @staticmethod
    def from_micro_candelas_per_square_meter(micro_candelas_per_square_meter: float):
        """
        Create a new instance of Luminance from a value in micro_candelas_per_square_meter.

        

        :param meters: The Luminance value in micro_candelas_per_square_meter.
        :type micro_candelas_per_square_meter: float
        :return: A new instance of Luminance.
        :rtype: Luminance
        """
        return Luminance(micro_candelas_per_square_meter, LuminanceUnits.MicroCandelaPerSquareMeter)

    
    @staticmethod
    def from_milli_candelas_per_square_meter(milli_candelas_per_square_meter: float):
        """
        Create a new instance of Luminance from a value in milli_candelas_per_square_meter.

        

        :param meters: The Luminance value in milli_candelas_per_square_meter.
        :type milli_candelas_per_square_meter: float
        :return: A new instance of Luminance.
        :rtype: Luminance
        """
        return Luminance(milli_candelas_per_square_meter, LuminanceUnits.MilliCandelaPerSquareMeter)

    
    @staticmethod
    def from_centi_candelas_per_square_meter(centi_candelas_per_square_meter: float):
        """
        Create a new instance of Luminance from a value in centi_candelas_per_square_meter.

        

        :param meters: The Luminance value in centi_candelas_per_square_meter.
        :type centi_candelas_per_square_meter: float
        :return: A new instance of Luminance.
        :rtype: Luminance
        """
        return Luminance(centi_candelas_per_square_meter, LuminanceUnits.CentiCandelaPerSquareMeter)

    
    @staticmethod
    def from_deci_candelas_per_square_meter(deci_candelas_per_square_meter: float):
        """
        Create a new instance of Luminance from a value in deci_candelas_per_square_meter.

        

        :param meters: The Luminance value in deci_candelas_per_square_meter.
        :type deci_candelas_per_square_meter: float
        :return: A new instance of Luminance.
        :rtype: Luminance
        """
        return Luminance(deci_candelas_per_square_meter, LuminanceUnits.DeciCandelaPerSquareMeter)

    
    @staticmethod
    def from_kilo_candelas_per_square_meter(kilo_candelas_per_square_meter: float):
        """
        Create a new instance of Luminance from a value in kilo_candelas_per_square_meter.

        

        :param meters: The Luminance value in kilo_candelas_per_square_meter.
        :type kilo_candelas_per_square_meter: float
        :return: A new instance of Luminance.
        :rtype: Luminance
        """
        return Luminance(kilo_candelas_per_square_meter, LuminanceUnits.KiloCandelaPerSquareMeter)

    
    @property
    def candelas_per_square_meter(self) -> float:
        """
        
        """
        if self.__candelas_per_square_meter != None:
            return self.__candelas_per_square_meter
        self.__candelas_per_square_meter = self.__convert_from_base(LuminanceUnits.CandelaPerSquareMeter)
        return self.__candelas_per_square_meter

    
    @property
    def candelas_per_square_foot(self) -> float:
        """
        
        """
        if self.__candelas_per_square_foot != None:
            return self.__candelas_per_square_foot
        self.__candelas_per_square_foot = self.__convert_from_base(LuminanceUnits.CandelaPerSquareFoot)
        return self.__candelas_per_square_foot

    
    @property
    def candelas_per_square_inch(self) -> float:
        """
        
        """
        if self.__candelas_per_square_inch != None:
            return self.__candelas_per_square_inch
        self.__candelas_per_square_inch = self.__convert_from_base(LuminanceUnits.CandelaPerSquareInch)
        return self.__candelas_per_square_inch

    
    @property
    def nits(self) -> float:
        """
        
        """
        if self.__nits != None:
            return self.__nits
        self.__nits = self.__convert_from_base(LuminanceUnits.Nit)
        return self.__nits

    
    @property
    def nano_candelas_per_square_meter(self) -> float:
        """
        
        """
        if self.__nano_candelas_per_square_meter != None:
            return self.__nano_candelas_per_square_meter
        self.__nano_candelas_per_square_meter = self.__convert_from_base(LuminanceUnits.NanoCandelaPerSquareMeter)
        return self.__nano_candelas_per_square_meter

    
    @property
    def micro_candelas_per_square_meter(self) -> float:
        """
        
        """
        if self.__micro_candelas_per_square_meter != None:
            return self.__micro_candelas_per_square_meter
        self.__micro_candelas_per_square_meter = self.__convert_from_base(LuminanceUnits.MicroCandelaPerSquareMeter)
        return self.__micro_candelas_per_square_meter

    
    @property
    def milli_candelas_per_square_meter(self) -> float:
        """
        
        """
        if self.__milli_candelas_per_square_meter != None:
            return self.__milli_candelas_per_square_meter
        self.__milli_candelas_per_square_meter = self.__convert_from_base(LuminanceUnits.MilliCandelaPerSquareMeter)
        return self.__milli_candelas_per_square_meter

    
    @property
    def centi_candelas_per_square_meter(self) -> float:
        """
        
        """
        if self.__centi_candelas_per_square_meter != None:
            return self.__centi_candelas_per_square_meter
        self.__centi_candelas_per_square_meter = self.__convert_from_base(LuminanceUnits.CentiCandelaPerSquareMeter)
        return self.__centi_candelas_per_square_meter

    
    @property
    def deci_candelas_per_square_meter(self) -> float:
        """
        
        """
        if self.__deci_candelas_per_square_meter != None:
            return self.__deci_candelas_per_square_meter
        self.__deci_candelas_per_square_meter = self.__convert_from_base(LuminanceUnits.DeciCandelaPerSquareMeter)
        return self.__deci_candelas_per_square_meter

    
    @property
    def kilo_candelas_per_square_meter(self) -> float:
        """
        
        """
        if self.__kilo_candelas_per_square_meter != None:
            return self.__kilo_candelas_per_square_meter
        self.__kilo_candelas_per_square_meter = self.__convert_from_base(LuminanceUnits.KiloCandelaPerSquareMeter)
        return self.__kilo_candelas_per_square_meter

    
    def to_string(self, unit: LuminanceUnits = LuminanceUnits.CandelaPerSquareMeter) -> string:
        """
        Format the Luminance to string.
        Note! the default format for Luminance is CandelaPerSquareMeter.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == LuminanceUnits.CandelaPerSquareMeter:
            return f"""{self.candelas_per_square_meter} Cd/m²"""
        
        if unit == LuminanceUnits.CandelaPerSquareFoot:
            return f"""{self.candelas_per_square_foot} Cd/ft²"""
        
        if unit == LuminanceUnits.CandelaPerSquareInch:
            return f"""{self.candelas_per_square_inch} Cd/in²"""
        
        if unit == LuminanceUnits.Nit:
            return f"""{self.nits} nt"""
        
        if unit == LuminanceUnits.NanoCandelaPerSquareMeter:
            return f"""{self.nano_candelas_per_square_meter} """
        
        if unit == LuminanceUnits.MicroCandelaPerSquareMeter:
            return f"""{self.micro_candelas_per_square_meter} """
        
        if unit == LuminanceUnits.MilliCandelaPerSquareMeter:
            return f"""{self.milli_candelas_per_square_meter} """
        
        if unit == LuminanceUnits.CentiCandelaPerSquareMeter:
            return f"""{self.centi_candelas_per_square_meter} """
        
        if unit == LuminanceUnits.DeciCandelaPerSquareMeter:
            return f"""{self.deci_candelas_per_square_meter} """
        
        if unit == LuminanceUnits.KiloCandelaPerSquareMeter:
            return f"""{self.kilo_candelas_per_square_meter} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: LuminanceUnits = LuminanceUnits.CandelaPerSquareMeter) -> string:
        """
        Get Luminance unit abbreviation.
        Note! the default abbreviation for Luminance is CandelaPerSquareMeter.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == LuminanceUnits.CandelaPerSquareMeter:
            return """Cd/m²"""
        
        if unit_abbreviation == LuminanceUnits.CandelaPerSquareFoot:
            return """Cd/ft²"""
        
        if unit_abbreviation == LuminanceUnits.CandelaPerSquareInch:
            return """Cd/in²"""
        
        if unit_abbreviation == LuminanceUnits.Nit:
            return """nt"""
        
        if unit_abbreviation == LuminanceUnits.NanoCandelaPerSquareMeter:
            return """"""
        
        if unit_abbreviation == LuminanceUnits.MicroCandelaPerSquareMeter:
            return """"""
        
        if unit_abbreviation == LuminanceUnits.MilliCandelaPerSquareMeter:
            return """"""
        
        if unit_abbreviation == LuminanceUnits.CentiCandelaPerSquareMeter:
            return """"""
        
        if unit_abbreviation == LuminanceUnits.DeciCandelaPerSquareMeter:
            return """"""
        
        if unit_abbreviation == LuminanceUnits.KiloCandelaPerSquareMeter:
            return """"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, Luminance):
            raise TypeError("unsupported operand type(s) for +: 'Luminance' and '{}'".format(type(other).__name__))
        return Luminance(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, Luminance):
            raise TypeError("unsupported operand type(s) for *: 'Luminance' and '{}'".format(type(other).__name__))
        return Luminance(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, Luminance):
            raise TypeError("unsupported operand type(s) for -: 'Luminance' and '{}'".format(type(other).__name__))
        return Luminance(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, Luminance):
            raise TypeError("unsupported operand type(s) for /: 'Luminance' and '{}'".format(type(other).__name__))
        return Luminance(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, Luminance):
            raise TypeError("unsupported operand type(s) for %: 'Luminance' and '{}'".format(type(other).__name__))
        return Luminance(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, Luminance):
            raise TypeError("unsupported operand type(s) for **: 'Luminance' and '{}'".format(type(other).__name__))
        return Luminance(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, Luminance):
            raise TypeError("unsupported operand type(s) for ==: 'Luminance' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, Luminance):
            raise TypeError("unsupported operand type(s) for <: 'Luminance' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, Luminance):
            raise TypeError("unsupported operand type(s) for >: 'Luminance' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, Luminance):
            raise TypeError("unsupported operand type(s) for <=: 'Luminance' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, Luminance):
            raise TypeError("unsupported operand type(s) for >=: 'Luminance' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value
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
        
        NanocandelaPerSquareMeter = 'nanocandela_per_square_meter'
        """
            
        """
        
        MicrocandelaPerSquareMeter = 'microcandela_per_square_meter'
        """
            
        """
        
        MillicandelaPerSquareMeter = 'millicandela_per_square_meter'
        """
            
        """
        
        CenticandelaPerSquareMeter = 'centicandela_per_square_meter'
        """
            
        """
        
        DecicandelaPerSquareMeter = 'decicandela_per_square_meter'
        """
            
        """
        
        KilocandelaPerSquareMeter = 'kilocandela_per_square_meter'
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
        
        self.__nanocandelas_per_square_meter = None
        
        self.__microcandelas_per_square_meter = None
        
        self.__millicandelas_per_square_meter = None
        
        self.__centicandelas_per_square_meter = None
        
        self.__decicandelas_per_square_meter = None
        
        self.__kilocandelas_per_square_meter = None
        

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
        
        if from_unit == LuminanceUnits.NanocandelaPerSquareMeter:
            return ((value) / 1e-09)
        
        if from_unit == LuminanceUnits.MicrocandelaPerSquareMeter:
            return ((value) / 1e-06)
        
        if from_unit == LuminanceUnits.MillicandelaPerSquareMeter:
            return ((value) / 0.001)
        
        if from_unit == LuminanceUnits.CenticandelaPerSquareMeter:
            return ((value) / 0.01)
        
        if from_unit == LuminanceUnits.DecicandelaPerSquareMeter:
            return ((value) / 0.1)
        
        if from_unit == LuminanceUnits.KilocandelaPerSquareMeter:
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
        
        if to_unit == LuminanceUnits.NanocandelaPerSquareMeter:
            return ((value) * 1e-09)
        
        if to_unit == LuminanceUnits.MicrocandelaPerSquareMeter:
            return ((value) * 1e-06)
        
        if to_unit == LuminanceUnits.MillicandelaPerSquareMeter:
            return ((value) * 0.001)
        
        if to_unit == LuminanceUnits.CenticandelaPerSquareMeter:
            return ((value) * 0.01)
        
        if to_unit == LuminanceUnits.DecicandelaPerSquareMeter:
            return ((value) * 0.1)
        
        if to_unit == LuminanceUnits.KilocandelaPerSquareMeter:
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
    def from_nanocandelas_per_square_meter(nanocandelas_per_square_meter: float):
        """
        Create a new instance of Luminance from a value in nanocandelas_per_square_meter.

        

        :param meters: The Luminance value in nanocandelas_per_square_meter.
        :type nanocandelas_per_square_meter: float
        :return: A new instance of Luminance.
        :rtype: Luminance
        """
        return Luminance(nanocandelas_per_square_meter, LuminanceUnits.NanocandelaPerSquareMeter)

    
    @staticmethod
    def from_microcandelas_per_square_meter(microcandelas_per_square_meter: float):
        """
        Create a new instance of Luminance from a value in microcandelas_per_square_meter.

        

        :param meters: The Luminance value in microcandelas_per_square_meter.
        :type microcandelas_per_square_meter: float
        :return: A new instance of Luminance.
        :rtype: Luminance
        """
        return Luminance(microcandelas_per_square_meter, LuminanceUnits.MicrocandelaPerSquareMeter)

    
    @staticmethod
    def from_millicandelas_per_square_meter(millicandelas_per_square_meter: float):
        """
        Create a new instance of Luminance from a value in millicandelas_per_square_meter.

        

        :param meters: The Luminance value in millicandelas_per_square_meter.
        :type millicandelas_per_square_meter: float
        :return: A new instance of Luminance.
        :rtype: Luminance
        """
        return Luminance(millicandelas_per_square_meter, LuminanceUnits.MillicandelaPerSquareMeter)

    
    @staticmethod
    def from_centicandelas_per_square_meter(centicandelas_per_square_meter: float):
        """
        Create a new instance of Luminance from a value in centicandelas_per_square_meter.

        

        :param meters: The Luminance value in centicandelas_per_square_meter.
        :type centicandelas_per_square_meter: float
        :return: A new instance of Luminance.
        :rtype: Luminance
        """
        return Luminance(centicandelas_per_square_meter, LuminanceUnits.CenticandelaPerSquareMeter)

    
    @staticmethod
    def from_decicandelas_per_square_meter(decicandelas_per_square_meter: float):
        """
        Create a new instance of Luminance from a value in decicandelas_per_square_meter.

        

        :param meters: The Luminance value in decicandelas_per_square_meter.
        :type decicandelas_per_square_meter: float
        :return: A new instance of Luminance.
        :rtype: Luminance
        """
        return Luminance(decicandelas_per_square_meter, LuminanceUnits.DecicandelaPerSquareMeter)

    
    @staticmethod
    def from_kilocandelas_per_square_meter(kilocandelas_per_square_meter: float):
        """
        Create a new instance of Luminance from a value in kilocandelas_per_square_meter.

        

        :param meters: The Luminance value in kilocandelas_per_square_meter.
        :type kilocandelas_per_square_meter: float
        :return: A new instance of Luminance.
        :rtype: Luminance
        """
        return Luminance(kilocandelas_per_square_meter, LuminanceUnits.KilocandelaPerSquareMeter)

    
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
    def nanocandelas_per_square_meter(self) -> float:
        """
        
        """
        if self.__nanocandelas_per_square_meter != None:
            return self.__nanocandelas_per_square_meter
        self.__nanocandelas_per_square_meter = self.__convert_from_base(LuminanceUnits.NanocandelaPerSquareMeter)
        return self.__nanocandelas_per_square_meter

    
    @property
    def microcandelas_per_square_meter(self) -> float:
        """
        
        """
        if self.__microcandelas_per_square_meter != None:
            return self.__microcandelas_per_square_meter
        self.__microcandelas_per_square_meter = self.__convert_from_base(LuminanceUnits.MicrocandelaPerSquareMeter)
        return self.__microcandelas_per_square_meter

    
    @property
    def millicandelas_per_square_meter(self) -> float:
        """
        
        """
        if self.__millicandelas_per_square_meter != None:
            return self.__millicandelas_per_square_meter
        self.__millicandelas_per_square_meter = self.__convert_from_base(LuminanceUnits.MillicandelaPerSquareMeter)
        return self.__millicandelas_per_square_meter

    
    @property
    def centicandelas_per_square_meter(self) -> float:
        """
        
        """
        if self.__centicandelas_per_square_meter != None:
            return self.__centicandelas_per_square_meter
        self.__centicandelas_per_square_meter = self.__convert_from_base(LuminanceUnits.CenticandelaPerSquareMeter)
        return self.__centicandelas_per_square_meter

    
    @property
    def decicandelas_per_square_meter(self) -> float:
        """
        
        """
        if self.__decicandelas_per_square_meter != None:
            return self.__decicandelas_per_square_meter
        self.__decicandelas_per_square_meter = self.__convert_from_base(LuminanceUnits.DecicandelaPerSquareMeter)
        return self.__decicandelas_per_square_meter

    
    @property
    def kilocandelas_per_square_meter(self) -> float:
        """
        
        """
        if self.__kilocandelas_per_square_meter != None:
            return self.__kilocandelas_per_square_meter
        self.__kilocandelas_per_square_meter = self.__convert_from_base(LuminanceUnits.KilocandelaPerSquareMeter)
        return self.__kilocandelas_per_square_meter

    
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
        
        if unit == LuminanceUnits.NanocandelaPerSquareMeter:
            return f"""{self.nanocandelas_per_square_meter} """
        
        if unit == LuminanceUnits.MicrocandelaPerSquareMeter:
            return f"""{self.microcandelas_per_square_meter} """
        
        if unit == LuminanceUnits.MillicandelaPerSquareMeter:
            return f"""{self.millicandelas_per_square_meter} """
        
        if unit == LuminanceUnits.CenticandelaPerSquareMeter:
            return f"""{self.centicandelas_per_square_meter} """
        
        if unit == LuminanceUnits.DecicandelaPerSquareMeter:
            return f"""{self.decicandelas_per_square_meter} """
        
        if unit == LuminanceUnits.KilocandelaPerSquareMeter:
            return f"""{self.kilocandelas_per_square_meter} """
        
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
        
        if unit_abbreviation == LuminanceUnits.NanocandelaPerSquareMeter:
            return """"""
        
        if unit_abbreviation == LuminanceUnits.MicrocandelaPerSquareMeter:
            return """"""
        
        if unit_abbreviation == LuminanceUnits.MillicandelaPerSquareMeter:
            return """"""
        
        if unit_abbreviation == LuminanceUnits.CenticandelaPerSquareMeter:
            return """"""
        
        if unit_abbreviation == LuminanceUnits.DecicandelaPerSquareMeter:
            return """"""
        
        if unit_abbreviation == LuminanceUnits.KilocandelaPerSquareMeter:
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
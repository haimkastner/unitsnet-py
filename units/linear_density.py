from enum import Enum
import math
import string


class LinearDensityUnits(Enum):
        """
            LinearDensityUnits enumeration
        """
        
        GramPerMillimeter = 'gram_per_millimeter'
        """
            
        """
        
        GramPerCentimeter = 'gram_per_centimeter'
        """
            
        """
        
        GramPerMeter = 'gram_per_meter'
        """
            
        """
        
        PoundPerInch = 'pound_per_inch'
        """
            
        """
        
        PoundPerFoot = 'pound_per_foot'
        """
            
        """
        
        MicroGramPerMillimeter = 'micro_gram_per_millimeter'
        """
            
        """
        
        MilliGramPerMillimeter = 'milli_gram_per_millimeter'
        """
            
        """
        
        KiloGramPerMillimeter = 'kilo_gram_per_millimeter'
        """
            
        """
        
        MicroGramPerCentimeter = 'micro_gram_per_centimeter'
        """
            
        """
        
        MilliGramPerCentimeter = 'milli_gram_per_centimeter'
        """
            
        """
        
        KiloGramPerCentimeter = 'kilo_gram_per_centimeter'
        """
            
        """
        
        MicroGramPerMeter = 'micro_gram_per_meter'
        """
            
        """
        
        MilliGramPerMeter = 'milli_gram_per_meter'
        """
            
        """
        
        KiloGramPerMeter = 'kilo_gram_per_meter'
        """
            
        """
        

class LinearDensity:
    """
    The Linear Density, or more precisely, the linear mass density, of a substance is its mass per unit length.  The term linear density is most often used when describing the characteristics of one-dimensional objects, although linear density can also be used to describe the density of a three-dimensional quantity along one particular dimension.

    Args:
        value (float): The value.
        from_unit (LinearDensityUnits): The LinearDensity unit to create from, The default unit is KilogramPerMeter
    """
    def __init__(self, value: float, from_unit: LinearDensityUnits = LinearDensityUnits.KilogramPerMeter):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__grams_per_millimeter = None
        
        self.__grams_per_centimeter = None
        
        self.__grams_per_meter = None
        
        self.__pounds_per_inch = None
        
        self.__pounds_per_foot = None
        
        self.__micro_grams_per_millimeter = None
        
        self.__milli_grams_per_millimeter = None
        
        self.__kilo_grams_per_millimeter = None
        
        self.__micro_grams_per_centimeter = None
        
        self.__milli_grams_per_centimeter = None
        
        self.__kilo_grams_per_centimeter = None
        
        self.__micro_grams_per_meter = None
        
        self.__milli_grams_per_meter = None
        
        self.__kilo_grams_per_meter = None
        

    def __convert_from_base(self, from_unit: LinearDensityUnits) -> float:
        value = self.__value
        
        if from_unit == LinearDensityUnits.GramPerMillimeter:
            return (value)
        
        if from_unit == LinearDensityUnits.GramPerCentimeter:
            return (value / 1e-1)
        
        if from_unit == LinearDensityUnits.GramPerMeter:
            return (value / 1e-3)
        
        if from_unit == LinearDensityUnits.PoundPerInch:
            return (value * 5.5997415e-2)
        
        if from_unit == LinearDensityUnits.PoundPerFoot:
            return (value / 1.48816394)
        
        if from_unit == LinearDensityUnits.MicroGramPerMillimeter:
            return ((value) / 1e-06)
        
        if from_unit == LinearDensityUnits.MilliGramPerMillimeter:
            return ((value) / 0.001)
        
        if from_unit == LinearDensityUnits.KiloGramPerMillimeter:
            return ((value) / 1000.0)
        
        if from_unit == LinearDensityUnits.MicroGramPerCentimeter:
            return ((value / 1e-1) / 1e-06)
        
        if from_unit == LinearDensityUnits.MilliGramPerCentimeter:
            return ((value / 1e-1) / 0.001)
        
        if from_unit == LinearDensityUnits.KiloGramPerCentimeter:
            return ((value / 1e-1) / 1000.0)
        
        if from_unit == LinearDensityUnits.MicroGramPerMeter:
            return ((value / 1e-3) / 1e-06)
        
        if from_unit == LinearDensityUnits.MilliGramPerMeter:
            return ((value / 1e-3) / 0.001)
        
        if from_unit == LinearDensityUnits.KiloGramPerMeter:
            return ((value / 1e-3) / 1000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: LinearDensityUnits) -> float:
        
        if to_unit == LinearDensityUnits.GramPerMillimeter:
            return (value)
        
        if to_unit == LinearDensityUnits.GramPerCentimeter:
            return (value * 1e-1)
        
        if to_unit == LinearDensityUnits.GramPerMeter:
            return (value * 1e-3)
        
        if to_unit == LinearDensityUnits.PoundPerInch:
            return (value / 5.5997415e-2)
        
        if to_unit == LinearDensityUnits.PoundPerFoot:
            return (value * 1.48816394)
        
        if to_unit == LinearDensityUnits.MicroGramPerMillimeter:
            return ((value) * 1e-06)
        
        if to_unit == LinearDensityUnits.MilliGramPerMillimeter:
            return ((value) * 0.001)
        
        if to_unit == LinearDensityUnits.KiloGramPerMillimeter:
            return ((value) * 1000.0)
        
        if to_unit == LinearDensityUnits.MicroGramPerCentimeter:
            return ((value * 1e-1) * 1e-06)
        
        if to_unit == LinearDensityUnits.MilliGramPerCentimeter:
            return ((value * 1e-1) * 0.001)
        
        if to_unit == LinearDensityUnits.KiloGramPerCentimeter:
            return ((value * 1e-1) * 1000.0)
        
        if to_unit == LinearDensityUnits.MicroGramPerMeter:
            return ((value * 1e-3) * 1e-06)
        
        if to_unit == LinearDensityUnits.MilliGramPerMeter:
            return ((value * 1e-3) * 0.001)
        
        if to_unit == LinearDensityUnits.KiloGramPerMeter:
            return ((value * 1e-3) * 1000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
    @staticmethod
    def from_grams_per_millimeter(grams_per_millimeter: float):
        """
        Create a new instance of LinearDensity from a value in grams_per_millimeter.

        

        :param meters: The LinearDensity value in grams_per_millimeter.
        :type grams_per_millimeter: float
        :return: A new instance of LinearDensity.
        :rtype: LinearDensity
        """
        return LinearDensity(grams_per_millimeter, LinearDensityUnits.GramPerMillimeter)

    
    @staticmethod
    def from_grams_per_centimeter(grams_per_centimeter: float):
        """
        Create a new instance of LinearDensity from a value in grams_per_centimeter.

        

        :param meters: The LinearDensity value in grams_per_centimeter.
        :type grams_per_centimeter: float
        :return: A new instance of LinearDensity.
        :rtype: LinearDensity
        """
        return LinearDensity(grams_per_centimeter, LinearDensityUnits.GramPerCentimeter)

    
    @staticmethod
    def from_grams_per_meter(grams_per_meter: float):
        """
        Create a new instance of LinearDensity from a value in grams_per_meter.

        

        :param meters: The LinearDensity value in grams_per_meter.
        :type grams_per_meter: float
        :return: A new instance of LinearDensity.
        :rtype: LinearDensity
        """
        return LinearDensity(grams_per_meter, LinearDensityUnits.GramPerMeter)

    
    @staticmethod
    def from_pounds_per_inch(pounds_per_inch: float):
        """
        Create a new instance of LinearDensity from a value in pounds_per_inch.

        

        :param meters: The LinearDensity value in pounds_per_inch.
        :type pounds_per_inch: float
        :return: A new instance of LinearDensity.
        :rtype: LinearDensity
        """
        return LinearDensity(pounds_per_inch, LinearDensityUnits.PoundPerInch)

    
    @staticmethod
    def from_pounds_per_foot(pounds_per_foot: float):
        """
        Create a new instance of LinearDensity from a value in pounds_per_foot.

        

        :param meters: The LinearDensity value in pounds_per_foot.
        :type pounds_per_foot: float
        :return: A new instance of LinearDensity.
        :rtype: LinearDensity
        """
        return LinearDensity(pounds_per_foot, LinearDensityUnits.PoundPerFoot)

    
    @staticmethod
    def from_micro_grams_per_millimeter(micro_grams_per_millimeter: float):
        """
        Create a new instance of LinearDensity from a value in micro_grams_per_millimeter.

        

        :param meters: The LinearDensity value in micro_grams_per_millimeter.
        :type micro_grams_per_millimeter: float
        :return: A new instance of LinearDensity.
        :rtype: LinearDensity
        """
        return LinearDensity(micro_grams_per_millimeter, LinearDensityUnits.MicroGramPerMillimeter)

    
    @staticmethod
    def from_milli_grams_per_millimeter(milli_grams_per_millimeter: float):
        """
        Create a new instance of LinearDensity from a value in milli_grams_per_millimeter.

        

        :param meters: The LinearDensity value in milli_grams_per_millimeter.
        :type milli_grams_per_millimeter: float
        :return: A new instance of LinearDensity.
        :rtype: LinearDensity
        """
        return LinearDensity(milli_grams_per_millimeter, LinearDensityUnits.MilliGramPerMillimeter)

    
    @staticmethod
    def from_kilo_grams_per_millimeter(kilo_grams_per_millimeter: float):
        """
        Create a new instance of LinearDensity from a value in kilo_grams_per_millimeter.

        

        :param meters: The LinearDensity value in kilo_grams_per_millimeter.
        :type kilo_grams_per_millimeter: float
        :return: A new instance of LinearDensity.
        :rtype: LinearDensity
        """
        return LinearDensity(kilo_grams_per_millimeter, LinearDensityUnits.KiloGramPerMillimeter)

    
    @staticmethod
    def from_micro_grams_per_centimeter(micro_grams_per_centimeter: float):
        """
        Create a new instance of LinearDensity from a value in micro_grams_per_centimeter.

        

        :param meters: The LinearDensity value in micro_grams_per_centimeter.
        :type micro_grams_per_centimeter: float
        :return: A new instance of LinearDensity.
        :rtype: LinearDensity
        """
        return LinearDensity(micro_grams_per_centimeter, LinearDensityUnits.MicroGramPerCentimeter)

    
    @staticmethod
    def from_milli_grams_per_centimeter(milli_grams_per_centimeter: float):
        """
        Create a new instance of LinearDensity from a value in milli_grams_per_centimeter.

        

        :param meters: The LinearDensity value in milli_grams_per_centimeter.
        :type milli_grams_per_centimeter: float
        :return: A new instance of LinearDensity.
        :rtype: LinearDensity
        """
        return LinearDensity(milli_grams_per_centimeter, LinearDensityUnits.MilliGramPerCentimeter)

    
    @staticmethod
    def from_kilo_grams_per_centimeter(kilo_grams_per_centimeter: float):
        """
        Create a new instance of LinearDensity from a value in kilo_grams_per_centimeter.

        

        :param meters: The LinearDensity value in kilo_grams_per_centimeter.
        :type kilo_grams_per_centimeter: float
        :return: A new instance of LinearDensity.
        :rtype: LinearDensity
        """
        return LinearDensity(kilo_grams_per_centimeter, LinearDensityUnits.KiloGramPerCentimeter)

    
    @staticmethod
    def from_micro_grams_per_meter(micro_grams_per_meter: float):
        """
        Create a new instance of LinearDensity from a value in micro_grams_per_meter.

        

        :param meters: The LinearDensity value in micro_grams_per_meter.
        :type micro_grams_per_meter: float
        :return: A new instance of LinearDensity.
        :rtype: LinearDensity
        """
        return LinearDensity(micro_grams_per_meter, LinearDensityUnits.MicroGramPerMeter)

    
    @staticmethod
    def from_milli_grams_per_meter(milli_grams_per_meter: float):
        """
        Create a new instance of LinearDensity from a value in milli_grams_per_meter.

        

        :param meters: The LinearDensity value in milli_grams_per_meter.
        :type milli_grams_per_meter: float
        :return: A new instance of LinearDensity.
        :rtype: LinearDensity
        """
        return LinearDensity(milli_grams_per_meter, LinearDensityUnits.MilliGramPerMeter)

    
    @staticmethod
    def from_kilo_grams_per_meter(kilo_grams_per_meter: float):
        """
        Create a new instance of LinearDensity from a value in kilo_grams_per_meter.

        

        :param meters: The LinearDensity value in kilo_grams_per_meter.
        :type kilo_grams_per_meter: float
        :return: A new instance of LinearDensity.
        :rtype: LinearDensity
        """
        return LinearDensity(kilo_grams_per_meter, LinearDensityUnits.KiloGramPerMeter)

    
    @property
    def grams_per_millimeter(self) -> float:
        """
        
        """
        if self.__grams_per_millimeter != None:
            return self.__grams_per_millimeter
        self.__grams_per_millimeter = self.__convert_from_base(LinearDensityUnits.GramPerMillimeter)
        return self.__grams_per_millimeter

    
    @property
    def grams_per_centimeter(self) -> float:
        """
        
        """
        if self.__grams_per_centimeter != None:
            return self.__grams_per_centimeter
        self.__grams_per_centimeter = self.__convert_from_base(LinearDensityUnits.GramPerCentimeter)
        return self.__grams_per_centimeter

    
    @property
    def grams_per_meter(self) -> float:
        """
        
        """
        if self.__grams_per_meter != None:
            return self.__grams_per_meter
        self.__grams_per_meter = self.__convert_from_base(LinearDensityUnits.GramPerMeter)
        return self.__grams_per_meter

    
    @property
    def pounds_per_inch(self) -> float:
        """
        
        """
        if self.__pounds_per_inch != None:
            return self.__pounds_per_inch
        self.__pounds_per_inch = self.__convert_from_base(LinearDensityUnits.PoundPerInch)
        return self.__pounds_per_inch

    
    @property
    def pounds_per_foot(self) -> float:
        """
        
        """
        if self.__pounds_per_foot != None:
            return self.__pounds_per_foot
        self.__pounds_per_foot = self.__convert_from_base(LinearDensityUnits.PoundPerFoot)
        return self.__pounds_per_foot

    
    @property
    def micro_grams_per_millimeter(self) -> float:
        """
        
        """
        if self.__micro_grams_per_millimeter != None:
            return self.__micro_grams_per_millimeter
        self.__micro_grams_per_millimeter = self.__convert_from_base(LinearDensityUnits.MicroGramPerMillimeter)
        return self.__micro_grams_per_millimeter

    
    @property
    def milli_grams_per_millimeter(self) -> float:
        """
        
        """
        if self.__milli_grams_per_millimeter != None:
            return self.__milli_grams_per_millimeter
        self.__milli_grams_per_millimeter = self.__convert_from_base(LinearDensityUnits.MilliGramPerMillimeter)
        return self.__milli_grams_per_millimeter

    
    @property
    def kilo_grams_per_millimeter(self) -> float:
        """
        
        """
        if self.__kilo_grams_per_millimeter != None:
            return self.__kilo_grams_per_millimeter
        self.__kilo_grams_per_millimeter = self.__convert_from_base(LinearDensityUnits.KiloGramPerMillimeter)
        return self.__kilo_grams_per_millimeter

    
    @property
    def micro_grams_per_centimeter(self) -> float:
        """
        
        """
        if self.__micro_grams_per_centimeter != None:
            return self.__micro_grams_per_centimeter
        self.__micro_grams_per_centimeter = self.__convert_from_base(LinearDensityUnits.MicroGramPerCentimeter)
        return self.__micro_grams_per_centimeter

    
    @property
    def milli_grams_per_centimeter(self) -> float:
        """
        
        """
        if self.__milli_grams_per_centimeter != None:
            return self.__milli_grams_per_centimeter
        self.__milli_grams_per_centimeter = self.__convert_from_base(LinearDensityUnits.MilliGramPerCentimeter)
        return self.__milli_grams_per_centimeter

    
    @property
    def kilo_grams_per_centimeter(self) -> float:
        """
        
        """
        if self.__kilo_grams_per_centimeter != None:
            return self.__kilo_grams_per_centimeter
        self.__kilo_grams_per_centimeter = self.__convert_from_base(LinearDensityUnits.KiloGramPerCentimeter)
        return self.__kilo_grams_per_centimeter

    
    @property
    def micro_grams_per_meter(self) -> float:
        """
        
        """
        if self.__micro_grams_per_meter != None:
            return self.__micro_grams_per_meter
        self.__micro_grams_per_meter = self.__convert_from_base(LinearDensityUnits.MicroGramPerMeter)
        return self.__micro_grams_per_meter

    
    @property
    def milli_grams_per_meter(self) -> float:
        """
        
        """
        if self.__milli_grams_per_meter != None:
            return self.__milli_grams_per_meter
        self.__milli_grams_per_meter = self.__convert_from_base(LinearDensityUnits.MilliGramPerMeter)
        return self.__milli_grams_per_meter

    
    @property
    def kilo_grams_per_meter(self) -> float:
        """
        
        """
        if self.__kilo_grams_per_meter != None:
            return self.__kilo_grams_per_meter
        self.__kilo_grams_per_meter = self.__convert_from_base(LinearDensityUnits.KiloGramPerMeter)
        return self.__kilo_grams_per_meter

    
    def to_string(self, unit: LinearDensityUnits = LinearDensityUnits.KilogramPerMeter) -> string:
        """
        Format the LinearDensity to string.
        Note! the default format for LinearDensity is KilogramPerMeter.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == LinearDensityUnits.GramPerMillimeter:
            return f"""{self.grams_per_millimeter} g/mm"""
        
        if unit == LinearDensityUnits.GramPerCentimeter:
            return f"""{self.grams_per_centimeter} g/cm"""
        
        if unit == LinearDensityUnits.GramPerMeter:
            return f"""{self.grams_per_meter} g/m"""
        
        if unit == LinearDensityUnits.PoundPerInch:
            return f"""{self.pounds_per_inch} lb/in"""
        
        if unit == LinearDensityUnits.PoundPerFoot:
            return f"""{self.pounds_per_foot} lb/ft"""
        
        if unit == LinearDensityUnits.MicroGramPerMillimeter:
            return f"""{self.micro_grams_per_millimeter} """
        
        if unit == LinearDensityUnits.MilliGramPerMillimeter:
            return f"""{self.milli_grams_per_millimeter} """
        
        if unit == LinearDensityUnits.KiloGramPerMillimeter:
            return f"""{self.kilo_grams_per_millimeter} """
        
        if unit == LinearDensityUnits.MicroGramPerCentimeter:
            return f"""{self.micro_grams_per_centimeter} """
        
        if unit == LinearDensityUnits.MilliGramPerCentimeter:
            return f"""{self.milli_grams_per_centimeter} """
        
        if unit == LinearDensityUnits.KiloGramPerCentimeter:
            return f"""{self.kilo_grams_per_centimeter} """
        
        if unit == LinearDensityUnits.MicroGramPerMeter:
            return f"""{self.micro_grams_per_meter} """
        
        if unit == LinearDensityUnits.MilliGramPerMeter:
            return f"""{self.milli_grams_per_meter} """
        
        if unit == LinearDensityUnits.KiloGramPerMeter:
            return f"""{self.kilo_grams_per_meter} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: LinearDensityUnits = LinearDensityUnits.KilogramPerMeter) -> string:
        """
        Get LinearDensity unit abbreviation.
        Note! the default abbreviation for LinearDensity is KilogramPerMeter.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == LinearDensityUnits.GramPerMillimeter:
            return """g/mm"""
        
        if unit_abbreviation == LinearDensityUnits.GramPerCentimeter:
            return """g/cm"""
        
        if unit_abbreviation == LinearDensityUnits.GramPerMeter:
            return """g/m"""
        
        if unit_abbreviation == LinearDensityUnits.PoundPerInch:
            return """lb/in"""
        
        if unit_abbreviation == LinearDensityUnits.PoundPerFoot:
            return """lb/ft"""
        
        if unit_abbreviation == LinearDensityUnits.MicroGramPerMillimeter:
            return """"""
        
        if unit_abbreviation == LinearDensityUnits.MilliGramPerMillimeter:
            return """"""
        
        if unit_abbreviation == LinearDensityUnits.KiloGramPerMillimeter:
            return """"""
        
        if unit_abbreviation == LinearDensityUnits.MicroGramPerCentimeter:
            return """"""
        
        if unit_abbreviation == LinearDensityUnits.MilliGramPerCentimeter:
            return """"""
        
        if unit_abbreviation == LinearDensityUnits.KiloGramPerCentimeter:
            return """"""
        
        if unit_abbreviation == LinearDensityUnits.MicroGramPerMeter:
            return """"""
        
        if unit_abbreviation == LinearDensityUnits.MilliGramPerMeter:
            return """"""
        
        if unit_abbreviation == LinearDensityUnits.KiloGramPerMeter:
            return """"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, LinearDensity):
            raise TypeError("unsupported operand type(s) for +: 'LinearDensity' and '{}'".format(type(other).__name__))
        return LinearDensity(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, LinearDensity):
            raise TypeError("unsupported operand type(s) for *: 'LinearDensity' and '{}'".format(type(other).__name__))
        return LinearDensity(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, LinearDensity):
            raise TypeError("unsupported operand type(s) for -: 'LinearDensity' and '{}'".format(type(other).__name__))
        return LinearDensity(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, LinearDensity):
            raise TypeError("unsupported operand type(s) for /: 'LinearDensity' and '{}'".format(type(other).__name__))
        return LinearDensity(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, LinearDensity):
            raise TypeError("unsupported operand type(s) for %: 'LinearDensity' and '{}'".format(type(other).__name__))
        return LinearDensity(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, LinearDensity):
            raise TypeError("unsupported operand type(s) for **: 'LinearDensity' and '{}'".format(type(other).__name__))
        return LinearDensity(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, LinearDensity):
            raise TypeError("unsupported operand type(s) for ==: 'LinearDensity' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, LinearDensity):
            raise TypeError("unsupported operand type(s) for <: 'LinearDensity' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, LinearDensity):
            raise TypeError("unsupported operand type(s) for >: 'LinearDensity' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, LinearDensity):
            raise TypeError("unsupported operand type(s) for <=: 'LinearDensity' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, LinearDensity):
            raise TypeError("unsupported operand type(s) for >=: 'LinearDensity' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value
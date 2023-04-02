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
        
        MicrogramPerMillimeter = 'microgram_per_millimeter'
        """
            
        """
        
        MilligramPerMillimeter = 'milligram_per_millimeter'
        """
            
        """
        
        KilogramPerMillimeter = 'kilogram_per_millimeter'
        """
            
        """
        
        MicrogramPerCentimeter = 'microgram_per_centimeter'
        """
            
        """
        
        MilligramPerCentimeter = 'milligram_per_centimeter'
        """
            
        """
        
        KilogramPerCentimeter = 'kilogram_per_centimeter'
        """
            
        """
        
        MicrogramPerMeter = 'microgram_per_meter'
        """
            
        """
        
        MilligramPerMeter = 'milligram_per_meter'
        """
            
        """
        
        KilogramPerMeter = 'kilogram_per_meter'
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
        
        self.__micrograms_per_millimeter = None
        
        self.__milligrams_per_millimeter = None
        
        self.__kilograms_per_millimeter = None
        
        self.__micrograms_per_centimeter = None
        
        self.__milligrams_per_centimeter = None
        
        self.__kilograms_per_centimeter = None
        
        self.__micrograms_per_meter = None
        
        self.__milligrams_per_meter = None
        
        self.__kilograms_per_meter = None
        

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
        
        if from_unit == LinearDensityUnits.MicrogramPerMillimeter:
            return ((value) / 1e-06)
        
        if from_unit == LinearDensityUnits.MilligramPerMillimeter:
            return ((value) / 0.001)
        
        if from_unit == LinearDensityUnits.KilogramPerMillimeter:
            return ((value) / 1000.0)
        
        if from_unit == LinearDensityUnits.MicrogramPerCentimeter:
            return ((value / 1e-1) / 1e-06)
        
        if from_unit == LinearDensityUnits.MilligramPerCentimeter:
            return ((value / 1e-1) / 0.001)
        
        if from_unit == LinearDensityUnits.KilogramPerCentimeter:
            return ((value / 1e-1) / 1000.0)
        
        if from_unit == LinearDensityUnits.MicrogramPerMeter:
            return ((value / 1e-3) / 1e-06)
        
        if from_unit == LinearDensityUnits.MilligramPerMeter:
            return ((value / 1e-3) / 0.001)
        
        if from_unit == LinearDensityUnits.KilogramPerMeter:
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
        
        if to_unit == LinearDensityUnits.MicrogramPerMillimeter:
            return ((value) * 1e-06)
        
        if to_unit == LinearDensityUnits.MilligramPerMillimeter:
            return ((value) * 0.001)
        
        if to_unit == LinearDensityUnits.KilogramPerMillimeter:
            return ((value) * 1000.0)
        
        if to_unit == LinearDensityUnits.MicrogramPerCentimeter:
            return ((value * 1e-1) * 1e-06)
        
        if to_unit == LinearDensityUnits.MilligramPerCentimeter:
            return ((value * 1e-1) * 0.001)
        
        if to_unit == LinearDensityUnits.KilogramPerCentimeter:
            return ((value * 1e-1) * 1000.0)
        
        if to_unit == LinearDensityUnits.MicrogramPerMeter:
            return ((value * 1e-3) * 1e-06)
        
        if to_unit == LinearDensityUnits.MilligramPerMeter:
            return ((value * 1e-3) * 0.001)
        
        if to_unit == LinearDensityUnits.KilogramPerMeter:
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
    def from_micrograms_per_millimeter(micrograms_per_millimeter: float):
        """
        Create a new instance of LinearDensity from a value in micrograms_per_millimeter.

        

        :param meters: The LinearDensity value in micrograms_per_millimeter.
        :type micrograms_per_millimeter: float
        :return: A new instance of LinearDensity.
        :rtype: LinearDensity
        """
        return LinearDensity(micrograms_per_millimeter, LinearDensityUnits.MicrogramPerMillimeter)

    
    @staticmethod
    def from_milligrams_per_millimeter(milligrams_per_millimeter: float):
        """
        Create a new instance of LinearDensity from a value in milligrams_per_millimeter.

        

        :param meters: The LinearDensity value in milligrams_per_millimeter.
        :type milligrams_per_millimeter: float
        :return: A new instance of LinearDensity.
        :rtype: LinearDensity
        """
        return LinearDensity(milligrams_per_millimeter, LinearDensityUnits.MilligramPerMillimeter)

    
    @staticmethod
    def from_kilograms_per_millimeter(kilograms_per_millimeter: float):
        """
        Create a new instance of LinearDensity from a value in kilograms_per_millimeter.

        

        :param meters: The LinearDensity value in kilograms_per_millimeter.
        :type kilograms_per_millimeter: float
        :return: A new instance of LinearDensity.
        :rtype: LinearDensity
        """
        return LinearDensity(kilograms_per_millimeter, LinearDensityUnits.KilogramPerMillimeter)

    
    @staticmethod
    def from_micrograms_per_centimeter(micrograms_per_centimeter: float):
        """
        Create a new instance of LinearDensity from a value in micrograms_per_centimeter.

        

        :param meters: The LinearDensity value in micrograms_per_centimeter.
        :type micrograms_per_centimeter: float
        :return: A new instance of LinearDensity.
        :rtype: LinearDensity
        """
        return LinearDensity(micrograms_per_centimeter, LinearDensityUnits.MicrogramPerCentimeter)

    
    @staticmethod
    def from_milligrams_per_centimeter(milligrams_per_centimeter: float):
        """
        Create a new instance of LinearDensity from a value in milligrams_per_centimeter.

        

        :param meters: The LinearDensity value in milligrams_per_centimeter.
        :type milligrams_per_centimeter: float
        :return: A new instance of LinearDensity.
        :rtype: LinearDensity
        """
        return LinearDensity(milligrams_per_centimeter, LinearDensityUnits.MilligramPerCentimeter)

    
    @staticmethod
    def from_kilograms_per_centimeter(kilograms_per_centimeter: float):
        """
        Create a new instance of LinearDensity from a value in kilograms_per_centimeter.

        

        :param meters: The LinearDensity value in kilograms_per_centimeter.
        :type kilograms_per_centimeter: float
        :return: A new instance of LinearDensity.
        :rtype: LinearDensity
        """
        return LinearDensity(kilograms_per_centimeter, LinearDensityUnits.KilogramPerCentimeter)

    
    @staticmethod
    def from_micrograms_per_meter(micrograms_per_meter: float):
        """
        Create a new instance of LinearDensity from a value in micrograms_per_meter.

        

        :param meters: The LinearDensity value in micrograms_per_meter.
        :type micrograms_per_meter: float
        :return: A new instance of LinearDensity.
        :rtype: LinearDensity
        """
        return LinearDensity(micrograms_per_meter, LinearDensityUnits.MicrogramPerMeter)

    
    @staticmethod
    def from_milligrams_per_meter(milligrams_per_meter: float):
        """
        Create a new instance of LinearDensity from a value in milligrams_per_meter.

        

        :param meters: The LinearDensity value in milligrams_per_meter.
        :type milligrams_per_meter: float
        :return: A new instance of LinearDensity.
        :rtype: LinearDensity
        """
        return LinearDensity(milligrams_per_meter, LinearDensityUnits.MilligramPerMeter)

    
    @staticmethod
    def from_kilograms_per_meter(kilograms_per_meter: float):
        """
        Create a new instance of LinearDensity from a value in kilograms_per_meter.

        

        :param meters: The LinearDensity value in kilograms_per_meter.
        :type kilograms_per_meter: float
        :return: A new instance of LinearDensity.
        :rtype: LinearDensity
        """
        return LinearDensity(kilograms_per_meter, LinearDensityUnits.KilogramPerMeter)

    
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
    def micrograms_per_millimeter(self) -> float:
        """
        
        """
        if self.__micrograms_per_millimeter != None:
            return self.__micrograms_per_millimeter
        self.__micrograms_per_millimeter = self.__convert_from_base(LinearDensityUnits.MicrogramPerMillimeter)
        return self.__micrograms_per_millimeter

    
    @property
    def milligrams_per_millimeter(self) -> float:
        """
        
        """
        if self.__milligrams_per_millimeter != None:
            return self.__milligrams_per_millimeter
        self.__milligrams_per_millimeter = self.__convert_from_base(LinearDensityUnits.MilligramPerMillimeter)
        return self.__milligrams_per_millimeter

    
    @property
    def kilograms_per_millimeter(self) -> float:
        """
        
        """
        if self.__kilograms_per_millimeter != None:
            return self.__kilograms_per_millimeter
        self.__kilograms_per_millimeter = self.__convert_from_base(LinearDensityUnits.KilogramPerMillimeter)
        return self.__kilograms_per_millimeter

    
    @property
    def micrograms_per_centimeter(self) -> float:
        """
        
        """
        if self.__micrograms_per_centimeter != None:
            return self.__micrograms_per_centimeter
        self.__micrograms_per_centimeter = self.__convert_from_base(LinearDensityUnits.MicrogramPerCentimeter)
        return self.__micrograms_per_centimeter

    
    @property
    def milligrams_per_centimeter(self) -> float:
        """
        
        """
        if self.__milligrams_per_centimeter != None:
            return self.__milligrams_per_centimeter
        self.__milligrams_per_centimeter = self.__convert_from_base(LinearDensityUnits.MilligramPerCentimeter)
        return self.__milligrams_per_centimeter

    
    @property
    def kilograms_per_centimeter(self) -> float:
        """
        
        """
        if self.__kilograms_per_centimeter != None:
            return self.__kilograms_per_centimeter
        self.__kilograms_per_centimeter = self.__convert_from_base(LinearDensityUnits.KilogramPerCentimeter)
        return self.__kilograms_per_centimeter

    
    @property
    def micrograms_per_meter(self) -> float:
        """
        
        """
        if self.__micrograms_per_meter != None:
            return self.__micrograms_per_meter
        self.__micrograms_per_meter = self.__convert_from_base(LinearDensityUnits.MicrogramPerMeter)
        return self.__micrograms_per_meter

    
    @property
    def milligrams_per_meter(self) -> float:
        """
        
        """
        if self.__milligrams_per_meter != None:
            return self.__milligrams_per_meter
        self.__milligrams_per_meter = self.__convert_from_base(LinearDensityUnits.MilligramPerMeter)
        return self.__milligrams_per_meter

    
    @property
    def kilograms_per_meter(self) -> float:
        """
        
        """
        if self.__kilograms_per_meter != None:
            return self.__kilograms_per_meter
        self.__kilograms_per_meter = self.__convert_from_base(LinearDensityUnits.KilogramPerMeter)
        return self.__kilograms_per_meter

    
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
        
        if unit == LinearDensityUnits.MicrogramPerMillimeter:
            return f"""{self.micrograms_per_millimeter} """
        
        if unit == LinearDensityUnits.MilligramPerMillimeter:
            return f"""{self.milligrams_per_millimeter} """
        
        if unit == LinearDensityUnits.KilogramPerMillimeter:
            return f"""{self.kilograms_per_millimeter} """
        
        if unit == LinearDensityUnits.MicrogramPerCentimeter:
            return f"""{self.micrograms_per_centimeter} """
        
        if unit == LinearDensityUnits.MilligramPerCentimeter:
            return f"""{self.milligrams_per_centimeter} """
        
        if unit == LinearDensityUnits.KilogramPerCentimeter:
            return f"""{self.kilograms_per_centimeter} """
        
        if unit == LinearDensityUnits.MicrogramPerMeter:
            return f"""{self.micrograms_per_meter} """
        
        if unit == LinearDensityUnits.MilligramPerMeter:
            return f"""{self.milligrams_per_meter} """
        
        if unit == LinearDensityUnits.KilogramPerMeter:
            return f"""{self.kilograms_per_meter} """
        
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
        
        if unit_abbreviation == LinearDensityUnits.MicrogramPerMillimeter:
            return """"""
        
        if unit_abbreviation == LinearDensityUnits.MilligramPerMillimeter:
            return """"""
        
        if unit_abbreviation == LinearDensityUnits.KilogramPerMillimeter:
            return """"""
        
        if unit_abbreviation == LinearDensityUnits.MicrogramPerCentimeter:
            return """"""
        
        if unit_abbreviation == LinearDensityUnits.MilligramPerCentimeter:
            return """"""
        
        if unit_abbreviation == LinearDensityUnits.KilogramPerCentimeter:
            return """"""
        
        if unit_abbreviation == LinearDensityUnits.MicrogramPerMeter:
            return """"""
        
        if unit_abbreviation == LinearDensityUnits.MilligramPerMeter:
            return """"""
        
        if unit_abbreviation == LinearDensityUnits.KilogramPerMeter:
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
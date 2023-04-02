from enum import Enum
import math
import string


class MassFluxUnits(Enum):
        """
            MassFluxUnits enumeration
        """
        
        GramPerSecondPerSquareMeter = 'gram_per_second_per_square_meter'
        """
            
        """
        
        GramPerSecondPerSquareCentimeter = 'gram_per_second_per_square_centimeter'
        """
            
        """
        
        GramPerSecondPerSquareMillimeter = 'gram_per_second_per_square_millimeter'
        """
            
        """
        
        GramPerHourPerSquareMeter = 'gram_per_hour_per_square_meter'
        """
            
        """
        
        GramPerHourPerSquareCentimeter = 'gram_per_hour_per_square_centimeter'
        """
            
        """
        
        GramPerHourPerSquareMillimeter = 'gram_per_hour_per_square_millimeter'
        """
            
        """
        
        KiloGramPerSecondPerSquareMeter = 'kilo_gram_per_second_per_square_meter'
        """
            
        """
        
        KiloGramPerSecondPerSquareCentimeter = 'kilo_gram_per_second_per_square_centimeter'
        """
            
        """
        
        KiloGramPerSecondPerSquareMillimeter = 'kilo_gram_per_second_per_square_millimeter'
        """
            
        """
        
        KiloGramPerHourPerSquareMeter = 'kilo_gram_per_hour_per_square_meter'
        """
            
        """
        
        KiloGramPerHourPerSquareCentimeter = 'kilo_gram_per_hour_per_square_centimeter'
        """
            
        """
        
        KiloGramPerHourPerSquareMillimeter = 'kilo_gram_per_hour_per_square_millimeter'
        """
            
        """
        
    
class MassFlux:
    """
    Mass flux is the mass flow rate per unit area.

    Args:
        value (float): The value.
        from_unit (MassFluxUnits): The MassFlux unit to create from, The default unit is KilogramPerSecondPerSquareMeter
    """
    def __init__(self, value: float, from_unit: MassFluxUnits = MassFluxUnits.KilogramPerSecondPerSquareMeter):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__grams_per_second_per_square_meter = None
        
        self.__grams_per_second_per_square_centimeter = None
        
        self.__grams_per_second_per_square_millimeter = None
        
        self.__grams_per_hour_per_square_meter = None
        
        self.__grams_per_hour_per_square_centimeter = None
        
        self.__grams_per_hour_per_square_millimeter = None
        
        self.__kilo_grams_per_second_per_square_meter = None
        
        self.__kilo_grams_per_second_per_square_centimeter = None
        
        self.__kilo_grams_per_second_per_square_millimeter = None
        
        self.__kilo_grams_per_hour_per_square_meter = None
        
        self.__kilo_grams_per_hour_per_square_centimeter = None
        
        self.__kilo_grams_per_hour_per_square_millimeter = None
        

    def __convert_from_base(self, from_unit: MassFluxUnits) -> float:
        value = self.__value
        
        if from_unit == MassFluxUnits.GramPerSecondPerSquareMeter:
            return (value * 1e3)
        
        if from_unit == MassFluxUnits.GramPerSecondPerSquareCentimeter:
            return (value * 1e-1)
        
        if from_unit == MassFluxUnits.GramPerSecondPerSquareMillimeter:
            return (value * 1e-3)
        
        if from_unit == MassFluxUnits.GramPerHourPerSquareMeter:
            return (value * 3.6e6)
        
        if from_unit == MassFluxUnits.GramPerHourPerSquareCentimeter:
            return (value * 3.6e2)
        
        if from_unit == MassFluxUnits.GramPerHourPerSquareMillimeter:
            return (value * 3.6e0)
        
        if from_unit == MassFluxUnits.KiloGramPerSecondPerSquareMeter:
            return ((value * 1e3) / 1000.0)
        
        if from_unit == MassFluxUnits.KiloGramPerSecondPerSquareCentimeter:
            return ((value * 1e-1) / 1000.0)
        
        if from_unit == MassFluxUnits.KiloGramPerSecondPerSquareMillimeter:
            return ((value * 1e-3) / 1000.0)
        
        if from_unit == MassFluxUnits.KiloGramPerHourPerSquareMeter:
            return ((value * 3.6e6) / 1000.0)
        
        if from_unit == MassFluxUnits.KiloGramPerHourPerSquareCentimeter:
            return ((value * 3.6e2) / 1000.0)
        
        if from_unit == MassFluxUnits.KiloGramPerHourPerSquareMillimeter:
            return ((value * 3.6e0) / 1000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: MassFluxUnits) -> float:
        
        if to_unit == MassFluxUnits.GramPerSecondPerSquareMeter:
            return (value / 1e3)
        
        if to_unit == MassFluxUnits.GramPerSecondPerSquareCentimeter:
            return (value / 1e-1)
        
        if to_unit == MassFluxUnits.GramPerSecondPerSquareMillimeter:
            return (value / 1e-3)
        
        if to_unit == MassFluxUnits.GramPerHourPerSquareMeter:
            return (value / 3.6e6)
        
        if to_unit == MassFluxUnits.GramPerHourPerSquareCentimeter:
            return (value / 3.6e2)
        
        if to_unit == MassFluxUnits.GramPerHourPerSquareMillimeter:
            return (value / 3.6e0)
        
        if to_unit == MassFluxUnits.KiloGramPerSecondPerSquareMeter:
            return ((value / 1e3) * 1000.0)
        
        if to_unit == MassFluxUnits.KiloGramPerSecondPerSquareCentimeter:
            return ((value / 1e-1) * 1000.0)
        
        if to_unit == MassFluxUnits.KiloGramPerSecondPerSquareMillimeter:
            return ((value / 1e-3) * 1000.0)
        
        if to_unit == MassFluxUnits.KiloGramPerHourPerSquareMeter:
            return ((value / 3.6e6) * 1000.0)
        
        if to_unit == MassFluxUnits.KiloGramPerHourPerSquareCentimeter:
            return ((value / 3.6e2) * 1000.0)
        
        if to_unit == MassFluxUnits.KiloGramPerHourPerSquareMillimeter:
            return ((value / 3.6e0) * 1000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
    @staticmethod
    def from_grams_per_second_per_square_meter(grams_per_second_per_square_meter: float):
        """
        Create a new instance of MassFlux from a value in grams_per_second_per_square_meter.

        

        :param meters: The MassFlux value in grams_per_second_per_square_meter.
        :type grams_per_second_per_square_meter: float
        :return: A new instance of MassFlux.
        :rtype: MassFlux
        """
        return MassFlux(grams_per_second_per_square_meter, MassFluxUnits.GramPerSecondPerSquareMeter)

    
    @staticmethod
    def from_grams_per_second_per_square_centimeter(grams_per_second_per_square_centimeter: float):
        """
        Create a new instance of MassFlux from a value in grams_per_second_per_square_centimeter.

        

        :param meters: The MassFlux value in grams_per_second_per_square_centimeter.
        :type grams_per_second_per_square_centimeter: float
        :return: A new instance of MassFlux.
        :rtype: MassFlux
        """
        return MassFlux(grams_per_second_per_square_centimeter, MassFluxUnits.GramPerSecondPerSquareCentimeter)

    
    @staticmethod
    def from_grams_per_second_per_square_millimeter(grams_per_second_per_square_millimeter: float):
        """
        Create a new instance of MassFlux from a value in grams_per_second_per_square_millimeter.

        

        :param meters: The MassFlux value in grams_per_second_per_square_millimeter.
        :type grams_per_second_per_square_millimeter: float
        :return: A new instance of MassFlux.
        :rtype: MassFlux
        """
        return MassFlux(grams_per_second_per_square_millimeter, MassFluxUnits.GramPerSecondPerSquareMillimeter)

    
    @staticmethod
    def from_grams_per_hour_per_square_meter(grams_per_hour_per_square_meter: float):
        """
        Create a new instance of MassFlux from a value in grams_per_hour_per_square_meter.

        

        :param meters: The MassFlux value in grams_per_hour_per_square_meter.
        :type grams_per_hour_per_square_meter: float
        :return: A new instance of MassFlux.
        :rtype: MassFlux
        """
        return MassFlux(grams_per_hour_per_square_meter, MassFluxUnits.GramPerHourPerSquareMeter)

    
    @staticmethod
    def from_grams_per_hour_per_square_centimeter(grams_per_hour_per_square_centimeter: float):
        """
        Create a new instance of MassFlux from a value in grams_per_hour_per_square_centimeter.

        

        :param meters: The MassFlux value in grams_per_hour_per_square_centimeter.
        :type grams_per_hour_per_square_centimeter: float
        :return: A new instance of MassFlux.
        :rtype: MassFlux
        """
        return MassFlux(grams_per_hour_per_square_centimeter, MassFluxUnits.GramPerHourPerSquareCentimeter)

    
    @staticmethod
    def from_grams_per_hour_per_square_millimeter(grams_per_hour_per_square_millimeter: float):
        """
        Create a new instance of MassFlux from a value in grams_per_hour_per_square_millimeter.

        

        :param meters: The MassFlux value in grams_per_hour_per_square_millimeter.
        :type grams_per_hour_per_square_millimeter: float
        :return: A new instance of MassFlux.
        :rtype: MassFlux
        """
        return MassFlux(grams_per_hour_per_square_millimeter, MassFluxUnits.GramPerHourPerSquareMillimeter)

    
    @staticmethod
    def from_kilo_grams_per_second_per_square_meter(kilo_grams_per_second_per_square_meter: float):
        """
        Create a new instance of MassFlux from a value in kilo_grams_per_second_per_square_meter.

        

        :param meters: The MassFlux value in kilo_grams_per_second_per_square_meter.
        :type kilo_grams_per_second_per_square_meter: float
        :return: A new instance of MassFlux.
        :rtype: MassFlux
        """
        return MassFlux(kilo_grams_per_second_per_square_meter, MassFluxUnits.KiloGramPerSecondPerSquareMeter)

    
    @staticmethod
    def from_kilo_grams_per_second_per_square_centimeter(kilo_grams_per_second_per_square_centimeter: float):
        """
        Create a new instance of MassFlux from a value in kilo_grams_per_second_per_square_centimeter.

        

        :param meters: The MassFlux value in kilo_grams_per_second_per_square_centimeter.
        :type kilo_grams_per_second_per_square_centimeter: float
        :return: A new instance of MassFlux.
        :rtype: MassFlux
        """
        return MassFlux(kilo_grams_per_second_per_square_centimeter, MassFluxUnits.KiloGramPerSecondPerSquareCentimeter)

    
    @staticmethod
    def from_kilo_grams_per_second_per_square_millimeter(kilo_grams_per_second_per_square_millimeter: float):
        """
        Create a new instance of MassFlux from a value in kilo_grams_per_second_per_square_millimeter.

        

        :param meters: The MassFlux value in kilo_grams_per_second_per_square_millimeter.
        :type kilo_grams_per_second_per_square_millimeter: float
        :return: A new instance of MassFlux.
        :rtype: MassFlux
        """
        return MassFlux(kilo_grams_per_second_per_square_millimeter, MassFluxUnits.KiloGramPerSecondPerSquareMillimeter)

    
    @staticmethod
    def from_kilo_grams_per_hour_per_square_meter(kilo_grams_per_hour_per_square_meter: float):
        """
        Create a new instance of MassFlux from a value in kilo_grams_per_hour_per_square_meter.

        

        :param meters: The MassFlux value in kilo_grams_per_hour_per_square_meter.
        :type kilo_grams_per_hour_per_square_meter: float
        :return: A new instance of MassFlux.
        :rtype: MassFlux
        """
        return MassFlux(kilo_grams_per_hour_per_square_meter, MassFluxUnits.KiloGramPerHourPerSquareMeter)

    
    @staticmethod
    def from_kilo_grams_per_hour_per_square_centimeter(kilo_grams_per_hour_per_square_centimeter: float):
        """
        Create a new instance of MassFlux from a value in kilo_grams_per_hour_per_square_centimeter.

        

        :param meters: The MassFlux value in kilo_grams_per_hour_per_square_centimeter.
        :type kilo_grams_per_hour_per_square_centimeter: float
        :return: A new instance of MassFlux.
        :rtype: MassFlux
        """
        return MassFlux(kilo_grams_per_hour_per_square_centimeter, MassFluxUnits.KiloGramPerHourPerSquareCentimeter)

    
    @staticmethod
    def from_kilo_grams_per_hour_per_square_millimeter(kilo_grams_per_hour_per_square_millimeter: float):
        """
        Create a new instance of MassFlux from a value in kilo_grams_per_hour_per_square_millimeter.

        

        :param meters: The MassFlux value in kilo_grams_per_hour_per_square_millimeter.
        :type kilo_grams_per_hour_per_square_millimeter: float
        :return: A new instance of MassFlux.
        :rtype: MassFlux
        """
        return MassFlux(kilo_grams_per_hour_per_square_millimeter, MassFluxUnits.KiloGramPerHourPerSquareMillimeter)

    
    @property
    def grams_per_second_per_square_meter(self) -> float:
        """
        
        """
        if self.__grams_per_second_per_square_meter != None:
            return self.__grams_per_second_per_square_meter
        self.__grams_per_second_per_square_meter = self.__convert_from_base(MassFluxUnits.GramPerSecondPerSquareMeter)
        return self.__grams_per_second_per_square_meter

    
    @property
    def grams_per_second_per_square_centimeter(self) -> float:
        """
        
        """
        if self.__grams_per_second_per_square_centimeter != None:
            return self.__grams_per_second_per_square_centimeter
        self.__grams_per_second_per_square_centimeter = self.__convert_from_base(MassFluxUnits.GramPerSecondPerSquareCentimeter)
        return self.__grams_per_second_per_square_centimeter

    
    @property
    def grams_per_second_per_square_millimeter(self) -> float:
        """
        
        """
        if self.__grams_per_second_per_square_millimeter != None:
            return self.__grams_per_second_per_square_millimeter
        self.__grams_per_second_per_square_millimeter = self.__convert_from_base(MassFluxUnits.GramPerSecondPerSquareMillimeter)
        return self.__grams_per_second_per_square_millimeter

    
    @property
    def grams_per_hour_per_square_meter(self) -> float:
        """
        
        """
        if self.__grams_per_hour_per_square_meter != None:
            return self.__grams_per_hour_per_square_meter
        self.__grams_per_hour_per_square_meter = self.__convert_from_base(MassFluxUnits.GramPerHourPerSquareMeter)
        return self.__grams_per_hour_per_square_meter

    
    @property
    def grams_per_hour_per_square_centimeter(self) -> float:
        """
        
        """
        if self.__grams_per_hour_per_square_centimeter != None:
            return self.__grams_per_hour_per_square_centimeter
        self.__grams_per_hour_per_square_centimeter = self.__convert_from_base(MassFluxUnits.GramPerHourPerSquareCentimeter)
        return self.__grams_per_hour_per_square_centimeter

    
    @property
    def grams_per_hour_per_square_millimeter(self) -> float:
        """
        
        """
        if self.__grams_per_hour_per_square_millimeter != None:
            return self.__grams_per_hour_per_square_millimeter
        self.__grams_per_hour_per_square_millimeter = self.__convert_from_base(MassFluxUnits.GramPerHourPerSquareMillimeter)
        return self.__grams_per_hour_per_square_millimeter

    
    @property
    def kilo_grams_per_second_per_square_meter(self) -> float:
        """
        
        """
        if self.__kilo_grams_per_second_per_square_meter != None:
            return self.__kilo_grams_per_second_per_square_meter
        self.__kilo_grams_per_second_per_square_meter = self.__convert_from_base(MassFluxUnits.KiloGramPerSecondPerSquareMeter)
        return self.__kilo_grams_per_second_per_square_meter

    
    @property
    def kilo_grams_per_second_per_square_centimeter(self) -> float:
        """
        
        """
        if self.__kilo_grams_per_second_per_square_centimeter != None:
            return self.__kilo_grams_per_second_per_square_centimeter
        self.__kilo_grams_per_second_per_square_centimeter = self.__convert_from_base(MassFluxUnits.KiloGramPerSecondPerSquareCentimeter)
        return self.__kilo_grams_per_second_per_square_centimeter

    
    @property
    def kilo_grams_per_second_per_square_millimeter(self) -> float:
        """
        
        """
        if self.__kilo_grams_per_second_per_square_millimeter != None:
            return self.__kilo_grams_per_second_per_square_millimeter
        self.__kilo_grams_per_second_per_square_millimeter = self.__convert_from_base(MassFluxUnits.KiloGramPerSecondPerSquareMillimeter)
        return self.__kilo_grams_per_second_per_square_millimeter

    
    @property
    def kilo_grams_per_hour_per_square_meter(self) -> float:
        """
        
        """
        if self.__kilo_grams_per_hour_per_square_meter != None:
            return self.__kilo_grams_per_hour_per_square_meter
        self.__kilo_grams_per_hour_per_square_meter = self.__convert_from_base(MassFluxUnits.KiloGramPerHourPerSquareMeter)
        return self.__kilo_grams_per_hour_per_square_meter

    
    @property
    def kilo_grams_per_hour_per_square_centimeter(self) -> float:
        """
        
        """
        if self.__kilo_grams_per_hour_per_square_centimeter != None:
            return self.__kilo_grams_per_hour_per_square_centimeter
        self.__kilo_grams_per_hour_per_square_centimeter = self.__convert_from_base(MassFluxUnits.KiloGramPerHourPerSquareCentimeter)
        return self.__kilo_grams_per_hour_per_square_centimeter

    
    @property
    def kilo_grams_per_hour_per_square_millimeter(self) -> float:
        """
        
        """
        if self.__kilo_grams_per_hour_per_square_millimeter != None:
            return self.__kilo_grams_per_hour_per_square_millimeter
        self.__kilo_grams_per_hour_per_square_millimeter = self.__convert_from_base(MassFluxUnits.KiloGramPerHourPerSquareMillimeter)
        return self.__kilo_grams_per_hour_per_square_millimeter

    
    def to_string(self, unit: MassFluxUnits = MassFluxUnits.KilogramPerSecondPerSquareMeter) -> string:
        """
        Format the MassFlux to string.
        Note! the default format for MassFlux is KilogramPerSecondPerSquareMeter.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == MassFluxUnits.GramPerSecondPerSquareMeter:
            return f"""{self.grams_per_second_per_square_meter} g·s⁻¹·m⁻²"""
        
        if unit == MassFluxUnits.GramPerSecondPerSquareCentimeter:
            return f"""{self.grams_per_second_per_square_centimeter} g·s⁻¹·cm⁻²"""
        
        if unit == MassFluxUnits.GramPerSecondPerSquareMillimeter:
            return f"""{self.grams_per_second_per_square_millimeter} g·s⁻¹·mm⁻²"""
        
        if unit == MassFluxUnits.GramPerHourPerSquareMeter:
            return f"""{self.grams_per_hour_per_square_meter} g·h⁻¹·m⁻²"""
        
        if unit == MassFluxUnits.GramPerHourPerSquareCentimeter:
            return f"""{self.grams_per_hour_per_square_centimeter} g·h⁻¹·cm⁻²"""
        
        if unit == MassFluxUnits.GramPerHourPerSquareMillimeter:
            return f"""{self.grams_per_hour_per_square_millimeter} g·h⁻¹·mm⁻²"""
        
        if unit == MassFluxUnits.KiloGramPerSecondPerSquareMeter:
            return f"""{self.kilo_grams_per_second_per_square_meter} """
        
        if unit == MassFluxUnits.KiloGramPerSecondPerSquareCentimeter:
            return f"""{self.kilo_grams_per_second_per_square_centimeter} """
        
        if unit == MassFluxUnits.KiloGramPerSecondPerSquareMillimeter:
            return f"""{self.kilo_grams_per_second_per_square_millimeter} """
        
        if unit == MassFluxUnits.KiloGramPerHourPerSquareMeter:
            return f"""{self.kilo_grams_per_hour_per_square_meter} """
        
        if unit == MassFluxUnits.KiloGramPerHourPerSquareCentimeter:
            return f"""{self.kilo_grams_per_hour_per_square_centimeter} """
        
        if unit == MassFluxUnits.KiloGramPerHourPerSquareMillimeter:
            return f"""{self.kilo_grams_per_hour_per_square_millimeter} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: MassFluxUnits = MassFluxUnits.KilogramPerSecondPerSquareMeter) -> string:
        """
        Get MassFlux unit abbreviation.
        Note! the default abbreviation for MassFlux is KilogramPerSecondPerSquareMeter.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == MassFluxUnits.GramPerSecondPerSquareMeter:
            return """g·s⁻¹·m⁻²"""
        
        if unit_abbreviation == MassFluxUnits.GramPerSecondPerSquareCentimeter:
            return """g·s⁻¹·cm⁻²"""
        
        if unit_abbreviation == MassFluxUnits.GramPerSecondPerSquareMillimeter:
            return """g·s⁻¹·mm⁻²"""
        
        if unit_abbreviation == MassFluxUnits.GramPerHourPerSquareMeter:
            return """g·h⁻¹·m⁻²"""
        
        if unit_abbreviation == MassFluxUnits.GramPerHourPerSquareCentimeter:
            return """g·h⁻¹·cm⁻²"""
        
        if unit_abbreviation == MassFluxUnits.GramPerHourPerSquareMillimeter:
            return """g·h⁻¹·mm⁻²"""
        
        if unit_abbreviation == MassFluxUnits.KiloGramPerSecondPerSquareMeter:
            return """"""
        
        if unit_abbreviation == MassFluxUnits.KiloGramPerSecondPerSquareCentimeter:
            return """"""
        
        if unit_abbreviation == MassFluxUnits.KiloGramPerSecondPerSquareMillimeter:
            return """"""
        
        if unit_abbreviation == MassFluxUnits.KiloGramPerHourPerSquareMeter:
            return """"""
        
        if unit_abbreviation == MassFluxUnits.KiloGramPerHourPerSquareCentimeter:
            return """"""
        
        if unit_abbreviation == MassFluxUnits.KiloGramPerHourPerSquareMillimeter:
            return """"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, MassFlux):
            raise TypeError("unsupported operand type(s) for +: 'MassFlux' and '{}'".format(type(other).__name__))
        return MassFlux(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, MassFlux):
            raise TypeError("unsupported operand type(s) for *: 'MassFlux' and '{}'".format(type(other).__name__))
        return MassFlux(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, MassFlux):
            raise TypeError("unsupported operand type(s) for -: 'MassFlux' and '{}'".format(type(other).__name__))
        return MassFlux(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, MassFlux):
            raise TypeError("unsupported operand type(s) for /: 'MassFlux' and '{}'".format(type(other).__name__))
        return MassFlux(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, MassFlux):
            raise TypeError("unsupported operand type(s) for %: 'MassFlux' and '{}'".format(type(other).__name__))
        return MassFlux(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, MassFlux):
            raise TypeError("unsupported operand type(s) for **: 'MassFlux' and '{}'".format(type(other).__name__))
        return MassFlux(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, MassFlux):
            raise TypeError("unsupported operand type(s) for ==: 'MassFlux' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, MassFlux):
            raise TypeError("unsupported operand type(s) for <: 'MassFlux' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, MassFlux):
            raise TypeError("unsupported operand type(s) for >: 'MassFlux' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, MassFlux):
            raise TypeError("unsupported operand type(s) for <=: 'MassFlux' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, MassFlux):
            raise TypeError("unsupported operand type(s) for >=: 'MassFlux' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value
from enum import Enum
import math
import string


class IrradiationUnits(Enum):
        """
            IrradiationUnits enumeration
        """
        
        JoulePerSquareMeter = 'joule_per_square_meter'
        """
            
        """
        
        JoulePerSquareCentimeter = 'joule_per_square_centimeter'
        """
            
        """
        
        JoulePerSquareMillimeter = 'joule_per_square_millimeter'
        """
            
        """
        
        WattHourPerSquareMeter = 'watt_hour_per_square_meter'
        """
            
        """
        
        KiloJoulePerSquareMeter = 'kilo_joule_per_square_meter'
        """
            
        """
        
        MilliJoulePerSquareCentimeter = 'milli_joule_per_square_centimeter'
        """
            
        """
        
        KiloWattHourPerSquareMeter = 'kilo_watt_hour_per_square_meter'
        """
            
        """
        
    
class Irradiation:
    """
    Irradiation is the process by which an object is exposed to radiation. The exposure can originate from various sources, including natural sources.

    Args:
        value (float): The value.
        from_unit (IrradiationUnits): The Irradiation unit to create from, The default unit is JoulePerSquareMeter
    """
    def __init__(self, value: float, from_unit: IrradiationUnits = IrradiationUnits.JoulePerSquareMeter):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__joules_per_square_meter = None
        
        self.__joules_per_square_centimeter = None
        
        self.__joules_per_square_millimeter = None
        
        self.__watt_hours_per_square_meter = None
        
        self.__kilo_joules_per_square_meter = None
        
        self.__milli_joules_per_square_centimeter = None
        
        self.__kilo_watt_hours_per_square_meter = None
        

    def __convert_from_base(self, from_unit: IrradiationUnits) -> float:
        value = self.__value
        
        if from_unit == IrradiationUnits.JoulePerSquareMeter:
            return (value)
        
        if from_unit == IrradiationUnits.JoulePerSquareCentimeter:
            return (value / 1e4)
        
        if from_unit == IrradiationUnits.JoulePerSquareMillimeter:
            return (value / 1e6)
        
        if from_unit == IrradiationUnits.WattHourPerSquareMeter:
            return (value / 3600)
        
        if from_unit == IrradiationUnits.KiloJoulePerSquareMeter:
            return ((value) / 1000.0)
        
        if from_unit == IrradiationUnits.MilliJoulePerSquareCentimeter:
            return ((value / 1e4) / 0.001)
        
        if from_unit == IrradiationUnits.KiloWattHourPerSquareMeter:
            return ((value / 3600) / 1000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: IrradiationUnits) -> float:
        
        if to_unit == IrradiationUnits.JoulePerSquareMeter:
            return (value)
        
        if to_unit == IrradiationUnits.JoulePerSquareCentimeter:
            return (value * 1e4)
        
        if to_unit == IrradiationUnits.JoulePerSquareMillimeter:
            return (value * 1e6)
        
        if to_unit == IrradiationUnits.WattHourPerSquareMeter:
            return (value * 3600)
        
        if to_unit == IrradiationUnits.KiloJoulePerSquareMeter:
            return ((value) * 1000.0)
        
        if to_unit == IrradiationUnits.MilliJoulePerSquareCentimeter:
            return ((value * 1e4) * 0.001)
        
        if to_unit == IrradiationUnits.KiloWattHourPerSquareMeter:
            return ((value * 3600) * 1000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
    @staticmethod
    def from_joules_per_square_meter(joules_per_square_meter: float):
        """
        Create a new instance of Irradiation from a value in joules_per_square_meter.

        

        :param meters: The Irradiation value in joules_per_square_meter.
        :type joules_per_square_meter: float
        :return: A new instance of Irradiation.
        :rtype: Irradiation
        """
        return Irradiation(joules_per_square_meter, IrradiationUnits.JoulePerSquareMeter)

    
    @staticmethod
    def from_joules_per_square_centimeter(joules_per_square_centimeter: float):
        """
        Create a new instance of Irradiation from a value in joules_per_square_centimeter.

        

        :param meters: The Irradiation value in joules_per_square_centimeter.
        :type joules_per_square_centimeter: float
        :return: A new instance of Irradiation.
        :rtype: Irradiation
        """
        return Irradiation(joules_per_square_centimeter, IrradiationUnits.JoulePerSquareCentimeter)

    
    @staticmethod
    def from_joules_per_square_millimeter(joules_per_square_millimeter: float):
        """
        Create a new instance of Irradiation from a value in joules_per_square_millimeter.

        

        :param meters: The Irradiation value in joules_per_square_millimeter.
        :type joules_per_square_millimeter: float
        :return: A new instance of Irradiation.
        :rtype: Irradiation
        """
        return Irradiation(joules_per_square_millimeter, IrradiationUnits.JoulePerSquareMillimeter)

    
    @staticmethod
    def from_watt_hours_per_square_meter(watt_hours_per_square_meter: float):
        """
        Create a new instance of Irradiation from a value in watt_hours_per_square_meter.

        

        :param meters: The Irradiation value in watt_hours_per_square_meter.
        :type watt_hours_per_square_meter: float
        :return: A new instance of Irradiation.
        :rtype: Irradiation
        """
        return Irradiation(watt_hours_per_square_meter, IrradiationUnits.WattHourPerSquareMeter)

    
    @staticmethod
    def from_kilo_joules_per_square_meter(kilo_joules_per_square_meter: float):
        """
        Create a new instance of Irradiation from a value in kilo_joules_per_square_meter.

        

        :param meters: The Irradiation value in kilo_joules_per_square_meter.
        :type kilo_joules_per_square_meter: float
        :return: A new instance of Irradiation.
        :rtype: Irradiation
        """
        return Irradiation(kilo_joules_per_square_meter, IrradiationUnits.KiloJoulePerSquareMeter)

    
    @staticmethod
    def from_milli_joules_per_square_centimeter(milli_joules_per_square_centimeter: float):
        """
        Create a new instance of Irradiation from a value in milli_joules_per_square_centimeter.

        

        :param meters: The Irradiation value in milli_joules_per_square_centimeter.
        :type milli_joules_per_square_centimeter: float
        :return: A new instance of Irradiation.
        :rtype: Irradiation
        """
        return Irradiation(milli_joules_per_square_centimeter, IrradiationUnits.MilliJoulePerSquareCentimeter)

    
    @staticmethod
    def from_kilo_watt_hours_per_square_meter(kilo_watt_hours_per_square_meter: float):
        """
        Create a new instance of Irradiation from a value in kilo_watt_hours_per_square_meter.

        

        :param meters: The Irradiation value in kilo_watt_hours_per_square_meter.
        :type kilo_watt_hours_per_square_meter: float
        :return: A new instance of Irradiation.
        :rtype: Irradiation
        """
        return Irradiation(kilo_watt_hours_per_square_meter, IrradiationUnits.KiloWattHourPerSquareMeter)

    
    @property
    def joules_per_square_meter(self) -> float:
        """
        
        """
        if self.__joules_per_square_meter != None:
            return self.__joules_per_square_meter
        self.__joules_per_square_meter = self.__convert_from_base(IrradiationUnits.JoulePerSquareMeter)
        return self.__joules_per_square_meter

    
    @property
    def joules_per_square_centimeter(self) -> float:
        """
        
        """
        if self.__joules_per_square_centimeter != None:
            return self.__joules_per_square_centimeter
        self.__joules_per_square_centimeter = self.__convert_from_base(IrradiationUnits.JoulePerSquareCentimeter)
        return self.__joules_per_square_centimeter

    
    @property
    def joules_per_square_millimeter(self) -> float:
        """
        
        """
        if self.__joules_per_square_millimeter != None:
            return self.__joules_per_square_millimeter
        self.__joules_per_square_millimeter = self.__convert_from_base(IrradiationUnits.JoulePerSquareMillimeter)
        return self.__joules_per_square_millimeter

    
    @property
    def watt_hours_per_square_meter(self) -> float:
        """
        
        """
        if self.__watt_hours_per_square_meter != None:
            return self.__watt_hours_per_square_meter
        self.__watt_hours_per_square_meter = self.__convert_from_base(IrradiationUnits.WattHourPerSquareMeter)
        return self.__watt_hours_per_square_meter

    
    @property
    def kilo_joules_per_square_meter(self) -> float:
        """
        
        """
        if self.__kilo_joules_per_square_meter != None:
            return self.__kilo_joules_per_square_meter
        self.__kilo_joules_per_square_meter = self.__convert_from_base(IrradiationUnits.KiloJoulePerSquareMeter)
        return self.__kilo_joules_per_square_meter

    
    @property
    def milli_joules_per_square_centimeter(self) -> float:
        """
        
        """
        if self.__milli_joules_per_square_centimeter != None:
            return self.__milli_joules_per_square_centimeter
        self.__milli_joules_per_square_centimeter = self.__convert_from_base(IrradiationUnits.MilliJoulePerSquareCentimeter)
        return self.__milli_joules_per_square_centimeter

    
    @property
    def kilo_watt_hours_per_square_meter(self) -> float:
        """
        
        """
        if self.__kilo_watt_hours_per_square_meter != None:
            return self.__kilo_watt_hours_per_square_meter
        self.__kilo_watt_hours_per_square_meter = self.__convert_from_base(IrradiationUnits.KiloWattHourPerSquareMeter)
        return self.__kilo_watt_hours_per_square_meter

    
    def to_string(self, unit: IrradiationUnits = IrradiationUnits.JoulePerSquareMeter) -> string:
        """
        Format the Irradiation to string.
        Note! the default format for Irradiation is JoulePerSquareMeter.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == IrradiationUnits.JoulePerSquareMeter:
            return f"""{self.joules_per_square_meter} J/m²"""
        
        if unit == IrradiationUnits.JoulePerSquareCentimeter:
            return f"""{self.joules_per_square_centimeter} J/cm²"""
        
        if unit == IrradiationUnits.JoulePerSquareMillimeter:
            return f"""{self.joules_per_square_millimeter} J/mm²"""
        
        if unit == IrradiationUnits.WattHourPerSquareMeter:
            return f"""{self.watt_hours_per_square_meter} Wh/m²"""
        
        if unit == IrradiationUnits.KiloJoulePerSquareMeter:
            return f"""{self.kilo_joules_per_square_meter} """
        
        if unit == IrradiationUnits.MilliJoulePerSquareCentimeter:
            return f"""{self.milli_joules_per_square_centimeter} """
        
        if unit == IrradiationUnits.KiloWattHourPerSquareMeter:
            return f"""{self.kilo_watt_hours_per_square_meter} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: IrradiationUnits = IrradiationUnits.JoulePerSquareMeter) -> string:
        """
        Get Irradiation unit abbreviation.
        Note! the default abbreviation for Irradiation is JoulePerSquareMeter.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == IrradiationUnits.JoulePerSquareMeter:
            return """J/m²"""
        
        if unit_abbreviation == IrradiationUnits.JoulePerSquareCentimeter:
            return """J/cm²"""
        
        if unit_abbreviation == IrradiationUnits.JoulePerSquareMillimeter:
            return """J/mm²"""
        
        if unit_abbreviation == IrradiationUnits.WattHourPerSquareMeter:
            return """Wh/m²"""
        
        if unit_abbreviation == IrradiationUnits.KiloJoulePerSquareMeter:
            return """"""
        
        if unit_abbreviation == IrradiationUnits.MilliJoulePerSquareCentimeter:
            return """"""
        
        if unit_abbreviation == IrradiationUnits.KiloWattHourPerSquareMeter:
            return """"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, Irradiation):
            raise TypeError("unsupported operand type(s) for +: 'Irradiation' and '{}'".format(type(other).__name__))
        return Irradiation(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, Irradiation):
            raise TypeError("unsupported operand type(s) for *: 'Irradiation' and '{}'".format(type(other).__name__))
        return Irradiation(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, Irradiation):
            raise TypeError("unsupported operand type(s) for -: 'Irradiation' and '{}'".format(type(other).__name__))
        return Irradiation(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, Irradiation):
            raise TypeError("unsupported operand type(s) for /: 'Irradiation' and '{}'".format(type(other).__name__))
        return Irradiation(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, Irradiation):
            raise TypeError("unsupported operand type(s) for %: 'Irradiation' and '{}'".format(type(other).__name__))
        return Irradiation(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, Irradiation):
            raise TypeError("unsupported operand type(s) for **: 'Irradiation' and '{}'".format(type(other).__name__))
        return Irradiation(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, Irradiation):
            raise TypeError("unsupported operand type(s) for ==: 'Irradiation' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, Irradiation):
            raise TypeError("unsupported operand type(s) for <: 'Irradiation' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, Irradiation):
            raise TypeError("unsupported operand type(s) for >: 'Irradiation' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, Irradiation):
            raise TypeError("unsupported operand type(s) for <=: 'Irradiation' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, Irradiation):
            raise TypeError("unsupported operand type(s) for >=: 'Irradiation' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value
from enum import Enum
import math
import string


class JerkUnits(Enum):
        """
            JerkUnits enumeration
        """
        
        MeterPerSecondCubed = 'meter_per_second_cubed'
        """
            
        """
        
        InchPerSecondCubed = 'inch_per_second_cubed'
        """
            
        """
        
        FootPerSecondCubed = 'foot_per_second_cubed'
        """
            
        """
        
        StandardGravitiesPerSecond = 'standard_gravities_per_second'
        """
            
        """
        
        NanoMeterPerSecondCubed = 'nano_meter_per_second_cubed'
        """
            
        """
        
        MicroMeterPerSecondCubed = 'micro_meter_per_second_cubed'
        """
            
        """
        
        MilliMeterPerSecondCubed = 'milli_meter_per_second_cubed'
        """
            
        """
        
        CentiMeterPerSecondCubed = 'centi_meter_per_second_cubed'
        """
            
        """
        
        DeciMeterPerSecondCubed = 'deci_meter_per_second_cubed'
        """
            
        """
        
        KiloMeterPerSecondCubed = 'kilo_meter_per_second_cubed'
        """
            
        """
        
        MilliStandardGravitiesPerSecond = 'milli_standard_gravities_per_second'
        """
            
        """
        

class Jerk:
    """
    None

    Args:
        value (float): The value.
        from_unit (JerkUnits): The Jerk unit to create from, The default unit is MeterPerSecondCubed
    """
    def __init__(self, value: float, from_unit: JerkUnits = JerkUnits.MeterPerSecondCubed):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__meters_per_second_cubed = None
        
        self.__inches_per_second_cubed = None
        
        self.__feet_per_second_cubed = None
        
        self.__standard_gravities_per_second = None
        
        self.__nano_meters_per_second_cubed = None
        
        self.__micro_meters_per_second_cubed = None
        
        self.__milli_meters_per_second_cubed = None
        
        self.__centi_meters_per_second_cubed = None
        
        self.__deci_meters_per_second_cubed = None
        
        self.__kilo_meters_per_second_cubed = None
        
        self.__milli_standard_gravities_per_second = None
        

    def __convert_from_base(self, from_unit: JerkUnits) -> float:
        value = self.__value
        
        if from_unit == JerkUnits.MeterPerSecondCubed:
            return (value)
        
        if from_unit == JerkUnits.InchPerSecondCubed:
            return (value / 0.0254)
        
        if from_unit == JerkUnits.FootPerSecondCubed:
            return (value / 0.304800)
        
        if from_unit == JerkUnits.StandardGravitiesPerSecond:
            return (value / 9.80665)
        
        if from_unit == JerkUnits.NanoMeterPerSecondCubed:
            return ((value) / 1e-09)
        
        if from_unit == JerkUnits.MicroMeterPerSecondCubed:
            return ((value) / 1e-06)
        
        if from_unit == JerkUnits.MilliMeterPerSecondCubed:
            return ((value) / 0.001)
        
        if from_unit == JerkUnits.CentiMeterPerSecondCubed:
            return ((value) / 0.01)
        
        if from_unit == JerkUnits.DeciMeterPerSecondCubed:
            return ((value) / 0.1)
        
        if from_unit == JerkUnits.KiloMeterPerSecondCubed:
            return ((value) / 1000.0)
        
        if from_unit == JerkUnits.MilliStandardGravitiesPerSecond:
            return ((value / 9.80665) / 0.001)
        
        return None


    def __convert_to_base(self, value: float, to_unit: JerkUnits) -> float:
        
        if to_unit == JerkUnits.MeterPerSecondCubed:
            return (value)
        
        if to_unit == JerkUnits.InchPerSecondCubed:
            return (value * 0.0254)
        
        if to_unit == JerkUnits.FootPerSecondCubed:
            return (value * 0.304800)
        
        if to_unit == JerkUnits.StandardGravitiesPerSecond:
            return (value * 9.80665)
        
        if to_unit == JerkUnits.NanoMeterPerSecondCubed:
            return ((value) * 1e-09)
        
        if to_unit == JerkUnits.MicroMeterPerSecondCubed:
            return ((value) * 1e-06)
        
        if to_unit == JerkUnits.MilliMeterPerSecondCubed:
            return ((value) * 0.001)
        
        if to_unit == JerkUnits.CentiMeterPerSecondCubed:
            return ((value) * 0.01)
        
        if to_unit == JerkUnits.DeciMeterPerSecondCubed:
            return ((value) * 0.1)
        
        if to_unit == JerkUnits.KiloMeterPerSecondCubed:
            return ((value) * 1000.0)
        
        if to_unit == JerkUnits.MilliStandardGravitiesPerSecond:
            return ((value * 9.80665) * 0.001)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
    @staticmethod
    def from_meters_per_second_cubed(meters_per_second_cubed: float):
        """
        Create a new instance of Jerk from a value in meters_per_second_cubed.

        

        :param meters: The Jerk value in meters_per_second_cubed.
        :type meters_per_second_cubed: float
        :return: A new instance of Jerk.
        :rtype: Jerk
        """
        return Jerk(meters_per_second_cubed, JerkUnits.MeterPerSecondCubed)

    
    @staticmethod
    def from_inches_per_second_cubed(inches_per_second_cubed: float):
        """
        Create a new instance of Jerk from a value in inches_per_second_cubed.

        

        :param meters: The Jerk value in inches_per_second_cubed.
        :type inches_per_second_cubed: float
        :return: A new instance of Jerk.
        :rtype: Jerk
        """
        return Jerk(inches_per_second_cubed, JerkUnits.InchPerSecondCubed)

    
    @staticmethod
    def from_feet_per_second_cubed(feet_per_second_cubed: float):
        """
        Create a new instance of Jerk from a value in feet_per_second_cubed.

        

        :param meters: The Jerk value in feet_per_second_cubed.
        :type feet_per_second_cubed: float
        :return: A new instance of Jerk.
        :rtype: Jerk
        """
        return Jerk(feet_per_second_cubed, JerkUnits.FootPerSecondCubed)

    
    @staticmethod
    def from_standard_gravities_per_second(standard_gravities_per_second: float):
        """
        Create a new instance of Jerk from a value in standard_gravities_per_second.

        

        :param meters: The Jerk value in standard_gravities_per_second.
        :type standard_gravities_per_second: float
        :return: A new instance of Jerk.
        :rtype: Jerk
        """
        return Jerk(standard_gravities_per_second, JerkUnits.StandardGravitiesPerSecond)

    
    @staticmethod
    def from_nano_meters_per_second_cubed(nano_meters_per_second_cubed: float):
        """
        Create a new instance of Jerk from a value in nano_meters_per_second_cubed.

        

        :param meters: The Jerk value in nano_meters_per_second_cubed.
        :type nano_meters_per_second_cubed: float
        :return: A new instance of Jerk.
        :rtype: Jerk
        """
        return Jerk(nano_meters_per_second_cubed, JerkUnits.NanoMeterPerSecondCubed)

    
    @staticmethod
    def from_micro_meters_per_second_cubed(micro_meters_per_second_cubed: float):
        """
        Create a new instance of Jerk from a value in micro_meters_per_second_cubed.

        

        :param meters: The Jerk value in micro_meters_per_second_cubed.
        :type micro_meters_per_second_cubed: float
        :return: A new instance of Jerk.
        :rtype: Jerk
        """
        return Jerk(micro_meters_per_second_cubed, JerkUnits.MicroMeterPerSecondCubed)

    
    @staticmethod
    def from_milli_meters_per_second_cubed(milli_meters_per_second_cubed: float):
        """
        Create a new instance of Jerk from a value in milli_meters_per_second_cubed.

        

        :param meters: The Jerk value in milli_meters_per_second_cubed.
        :type milli_meters_per_second_cubed: float
        :return: A new instance of Jerk.
        :rtype: Jerk
        """
        return Jerk(milli_meters_per_second_cubed, JerkUnits.MilliMeterPerSecondCubed)

    
    @staticmethod
    def from_centi_meters_per_second_cubed(centi_meters_per_second_cubed: float):
        """
        Create a new instance of Jerk from a value in centi_meters_per_second_cubed.

        

        :param meters: The Jerk value in centi_meters_per_second_cubed.
        :type centi_meters_per_second_cubed: float
        :return: A new instance of Jerk.
        :rtype: Jerk
        """
        return Jerk(centi_meters_per_second_cubed, JerkUnits.CentiMeterPerSecondCubed)

    
    @staticmethod
    def from_deci_meters_per_second_cubed(deci_meters_per_second_cubed: float):
        """
        Create a new instance of Jerk from a value in deci_meters_per_second_cubed.

        

        :param meters: The Jerk value in deci_meters_per_second_cubed.
        :type deci_meters_per_second_cubed: float
        :return: A new instance of Jerk.
        :rtype: Jerk
        """
        return Jerk(deci_meters_per_second_cubed, JerkUnits.DeciMeterPerSecondCubed)

    
    @staticmethod
    def from_kilo_meters_per_second_cubed(kilo_meters_per_second_cubed: float):
        """
        Create a new instance of Jerk from a value in kilo_meters_per_second_cubed.

        

        :param meters: The Jerk value in kilo_meters_per_second_cubed.
        :type kilo_meters_per_second_cubed: float
        :return: A new instance of Jerk.
        :rtype: Jerk
        """
        return Jerk(kilo_meters_per_second_cubed, JerkUnits.KiloMeterPerSecondCubed)

    
    @staticmethod
    def from_milli_standard_gravities_per_second(milli_standard_gravities_per_second: float):
        """
        Create a new instance of Jerk from a value in milli_standard_gravities_per_second.

        

        :param meters: The Jerk value in milli_standard_gravities_per_second.
        :type milli_standard_gravities_per_second: float
        :return: A new instance of Jerk.
        :rtype: Jerk
        """
        return Jerk(milli_standard_gravities_per_second, JerkUnits.MilliStandardGravitiesPerSecond)

    
    @property
    def meters_per_second_cubed(self) -> float:
        """
        
        """
        if self.__meters_per_second_cubed != None:
            return self.__meters_per_second_cubed
        self.__meters_per_second_cubed = self.__convert_from_base(JerkUnits.MeterPerSecondCubed)
        return self.__meters_per_second_cubed

    
    @property
    def inches_per_second_cubed(self) -> float:
        """
        
        """
        if self.__inches_per_second_cubed != None:
            return self.__inches_per_second_cubed
        self.__inches_per_second_cubed = self.__convert_from_base(JerkUnits.InchPerSecondCubed)
        return self.__inches_per_second_cubed

    
    @property
    def feet_per_second_cubed(self) -> float:
        """
        
        """
        if self.__feet_per_second_cubed != None:
            return self.__feet_per_second_cubed
        self.__feet_per_second_cubed = self.__convert_from_base(JerkUnits.FootPerSecondCubed)
        return self.__feet_per_second_cubed

    
    @property
    def standard_gravities_per_second(self) -> float:
        """
        
        """
        if self.__standard_gravities_per_second != None:
            return self.__standard_gravities_per_second
        self.__standard_gravities_per_second = self.__convert_from_base(JerkUnits.StandardGravitiesPerSecond)
        return self.__standard_gravities_per_second

    
    @property
    def nano_meters_per_second_cubed(self) -> float:
        """
        
        """
        if self.__nano_meters_per_second_cubed != None:
            return self.__nano_meters_per_second_cubed
        self.__nano_meters_per_second_cubed = self.__convert_from_base(JerkUnits.NanoMeterPerSecondCubed)
        return self.__nano_meters_per_second_cubed

    
    @property
    def micro_meters_per_second_cubed(self) -> float:
        """
        
        """
        if self.__micro_meters_per_second_cubed != None:
            return self.__micro_meters_per_second_cubed
        self.__micro_meters_per_second_cubed = self.__convert_from_base(JerkUnits.MicroMeterPerSecondCubed)
        return self.__micro_meters_per_second_cubed

    
    @property
    def milli_meters_per_second_cubed(self) -> float:
        """
        
        """
        if self.__milli_meters_per_second_cubed != None:
            return self.__milli_meters_per_second_cubed
        self.__milli_meters_per_second_cubed = self.__convert_from_base(JerkUnits.MilliMeterPerSecondCubed)
        return self.__milli_meters_per_second_cubed

    
    @property
    def centi_meters_per_second_cubed(self) -> float:
        """
        
        """
        if self.__centi_meters_per_second_cubed != None:
            return self.__centi_meters_per_second_cubed
        self.__centi_meters_per_second_cubed = self.__convert_from_base(JerkUnits.CentiMeterPerSecondCubed)
        return self.__centi_meters_per_second_cubed

    
    @property
    def deci_meters_per_second_cubed(self) -> float:
        """
        
        """
        if self.__deci_meters_per_second_cubed != None:
            return self.__deci_meters_per_second_cubed
        self.__deci_meters_per_second_cubed = self.__convert_from_base(JerkUnits.DeciMeterPerSecondCubed)
        return self.__deci_meters_per_second_cubed

    
    @property
    def kilo_meters_per_second_cubed(self) -> float:
        """
        
        """
        if self.__kilo_meters_per_second_cubed != None:
            return self.__kilo_meters_per_second_cubed
        self.__kilo_meters_per_second_cubed = self.__convert_from_base(JerkUnits.KiloMeterPerSecondCubed)
        return self.__kilo_meters_per_second_cubed

    
    @property
    def milli_standard_gravities_per_second(self) -> float:
        """
        
        """
        if self.__milli_standard_gravities_per_second != None:
            return self.__milli_standard_gravities_per_second
        self.__milli_standard_gravities_per_second = self.__convert_from_base(JerkUnits.MilliStandardGravitiesPerSecond)
        return self.__milli_standard_gravities_per_second

    
    def to_string(self, unit: JerkUnits = JerkUnits.MeterPerSecondCubed) -> string:
        """
        Format the Jerk to string.
        Note! the default format for Jerk is MeterPerSecondCubed.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == JerkUnits.MeterPerSecondCubed:
            return f"""{self.meters_per_second_cubed} m/s³"""
        
        if unit == JerkUnits.InchPerSecondCubed:
            return f"""{self.inches_per_second_cubed} in/s³"""
        
        if unit == JerkUnits.FootPerSecondCubed:
            return f"""{self.feet_per_second_cubed} ft/s³"""
        
        if unit == JerkUnits.StandardGravitiesPerSecond:
            return f"""{self.standard_gravities_per_second} g/s"""
        
        if unit == JerkUnits.NanoMeterPerSecondCubed:
            return f"""{self.nano_meters_per_second_cubed} """
        
        if unit == JerkUnits.MicroMeterPerSecondCubed:
            return f"""{self.micro_meters_per_second_cubed} """
        
        if unit == JerkUnits.MilliMeterPerSecondCubed:
            return f"""{self.milli_meters_per_second_cubed} """
        
        if unit == JerkUnits.CentiMeterPerSecondCubed:
            return f"""{self.centi_meters_per_second_cubed} """
        
        if unit == JerkUnits.DeciMeterPerSecondCubed:
            return f"""{self.deci_meters_per_second_cubed} """
        
        if unit == JerkUnits.KiloMeterPerSecondCubed:
            return f"""{self.kilo_meters_per_second_cubed} """
        
        if unit == JerkUnits.MilliStandardGravitiesPerSecond:
            return f"""{self.milli_standard_gravities_per_second} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: JerkUnits = JerkUnits.MeterPerSecondCubed) -> string:
        """
        Get Jerk unit abbreviation.
        Note! the default abbreviation for Jerk is MeterPerSecondCubed.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == JerkUnits.MeterPerSecondCubed:
            return """m/s³"""
        
        if unit_abbreviation == JerkUnits.InchPerSecondCubed:
            return """in/s³"""
        
        if unit_abbreviation == JerkUnits.FootPerSecondCubed:
            return """ft/s³"""
        
        if unit_abbreviation == JerkUnits.StandardGravitiesPerSecond:
            return """g/s"""
        
        if unit_abbreviation == JerkUnits.NanoMeterPerSecondCubed:
            return """"""
        
        if unit_abbreviation == JerkUnits.MicroMeterPerSecondCubed:
            return """"""
        
        if unit_abbreviation == JerkUnits.MilliMeterPerSecondCubed:
            return """"""
        
        if unit_abbreviation == JerkUnits.CentiMeterPerSecondCubed:
            return """"""
        
        if unit_abbreviation == JerkUnits.DeciMeterPerSecondCubed:
            return """"""
        
        if unit_abbreviation == JerkUnits.KiloMeterPerSecondCubed:
            return """"""
        
        if unit_abbreviation == JerkUnits.MilliStandardGravitiesPerSecond:
            return """"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, Jerk):
            raise TypeError("unsupported operand type(s) for +: 'Jerk' and '{}'".format(type(other).__name__))
        return Jerk(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, Jerk):
            raise TypeError("unsupported operand type(s) for *: 'Jerk' and '{}'".format(type(other).__name__))
        return Jerk(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, Jerk):
            raise TypeError("unsupported operand type(s) for -: 'Jerk' and '{}'".format(type(other).__name__))
        return Jerk(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, Jerk):
            raise TypeError("unsupported operand type(s) for /: 'Jerk' and '{}'".format(type(other).__name__))
        return Jerk(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, Jerk):
            raise TypeError("unsupported operand type(s) for %: 'Jerk' and '{}'".format(type(other).__name__))
        return Jerk(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, Jerk):
            raise TypeError("unsupported operand type(s) for **: 'Jerk' and '{}'".format(type(other).__name__))
        return Jerk(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, Jerk):
            raise TypeError("unsupported operand type(s) for ==: 'Jerk' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, Jerk):
            raise TypeError("unsupported operand type(s) for <: 'Jerk' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, Jerk):
            raise TypeError("unsupported operand type(s) for >: 'Jerk' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, Jerk):
            raise TypeError("unsupported operand type(s) for <=: 'Jerk' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, Jerk):
            raise TypeError("unsupported operand type(s) for >=: 'Jerk' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value
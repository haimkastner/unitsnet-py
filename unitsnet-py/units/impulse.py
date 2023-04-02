from enum import Enum
import math
import string


class ImpulseUnits(Enum):
        """
            ImpulseUnits enumeration
        """
        
        KilogramMeterPerSecond = 'kilogram_meter_per_second'
        """
            
        """
        
        NewtonSecond = 'newton_second'
        """
            
        """
        
        PoundFootPerSecond = 'pound_foot_per_second'
        """
            
        """
        
        PoundForceSecond = 'pound_force_second'
        """
            
        """
        
        SlugFootPerSecond = 'slug_foot_per_second'
        """
            
        """
        
        NanoNewtonSecond = 'nano_newton_second'
        """
            
        """
        
        MicroNewtonSecond = 'micro_newton_second'
        """
            
        """
        
        MilliNewtonSecond = 'milli_newton_second'
        """
            
        """
        
        CentiNewtonSecond = 'centi_newton_second'
        """
            
        """
        
        DeciNewtonSecond = 'deci_newton_second'
        """
            
        """
        
        DecaNewtonSecond = 'deca_newton_second'
        """
            
        """
        
        KiloNewtonSecond = 'kilo_newton_second'
        """
            
        """
        
        MegaNewtonSecond = 'mega_newton_second'
        """
            
        """
        

class Impulse:
    """
    In classical mechanics, impulse is the integral of a force, F, over the time interval, t, for which it acts. Impulse applied to an object produces an equivalent vector change in its linear momentum, also in the resultant direction.

    Args:
        value (float): The value.
        from_unit (ImpulseUnits): The Impulse unit to create from, The default unit is NewtonSecond
    """
    def __init__(self, value: float, from_unit: ImpulseUnits = ImpulseUnits.NewtonSecond):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__kilogram_meters_per_second = None
        
        self.__newton_seconds = None
        
        self.__pound_feet_per_second = None
        
        self.__pound_force_seconds = None
        
        self.__slug_feet_per_second = None
        
        self.__nano_newton_seconds = None
        
        self.__micro_newton_seconds = None
        
        self.__milli_newton_seconds = None
        
        self.__centi_newton_seconds = None
        
        self.__deci_newton_seconds = None
        
        self.__deca_newton_seconds = None
        
        self.__kilo_newton_seconds = None
        
        self.__mega_newton_seconds = None
        

    def __convert_from_base(self, from_unit: ImpulseUnits) -> float:
        value = self.__value
        
        if from_unit == ImpulseUnits.KilogramMeterPerSecond:
            return (value)
        
        if from_unit == ImpulseUnits.NewtonSecond:
            return (value)
        
        if from_unit == ImpulseUnits.PoundFootPerSecond:
            return (value * 7.230657989877)
        
        if from_unit == ImpulseUnits.PoundForceSecond:
            return (value * 0.2248089430997)
        
        if from_unit == ImpulseUnits.SlugFootPerSecond:
            return (value * 0.224735720691)
        
        if from_unit == ImpulseUnits.NanoNewtonSecond:
            return ((value) / 1e-09)
        
        if from_unit == ImpulseUnits.MicroNewtonSecond:
            return ((value) / 1e-06)
        
        if from_unit == ImpulseUnits.MilliNewtonSecond:
            return ((value) / 0.001)
        
        if from_unit == ImpulseUnits.CentiNewtonSecond:
            return ((value) / 0.01)
        
        if from_unit == ImpulseUnits.DeciNewtonSecond:
            return ((value) / 0.1)
        
        if from_unit == ImpulseUnits.DecaNewtonSecond:
            return ((value) / 10.0)
        
        if from_unit == ImpulseUnits.KiloNewtonSecond:
            return ((value) / 1000.0)
        
        if from_unit == ImpulseUnits.MegaNewtonSecond:
            return ((value) / 1000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: ImpulseUnits) -> float:
        
        if to_unit == ImpulseUnits.KilogramMeterPerSecond:
            return (value)
        
        if to_unit == ImpulseUnits.NewtonSecond:
            return (value)
        
        if to_unit == ImpulseUnits.PoundFootPerSecond:
            return (value / 7.230657989877)
        
        if to_unit == ImpulseUnits.PoundForceSecond:
            return (value / 0.2248089430997)
        
        if to_unit == ImpulseUnits.SlugFootPerSecond:
            return (value / 0.224735720691)
        
        if to_unit == ImpulseUnits.NanoNewtonSecond:
            return ((value) * 1e-09)
        
        if to_unit == ImpulseUnits.MicroNewtonSecond:
            return ((value) * 1e-06)
        
        if to_unit == ImpulseUnits.MilliNewtonSecond:
            return ((value) * 0.001)
        
        if to_unit == ImpulseUnits.CentiNewtonSecond:
            return ((value) * 0.01)
        
        if to_unit == ImpulseUnits.DeciNewtonSecond:
            return ((value) * 0.1)
        
        if to_unit == ImpulseUnits.DecaNewtonSecond:
            return ((value) * 10.0)
        
        if to_unit == ImpulseUnits.KiloNewtonSecond:
            return ((value) * 1000.0)
        
        if to_unit == ImpulseUnits.MegaNewtonSecond:
            return ((value) * 1000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
    @staticmethod
    def from_kilogram_meters_per_second(kilogram_meters_per_second: float):
        """
        Create a new instance of Impulse from a value in kilogram_meters_per_second.

        

        :param meters: The Impulse value in kilogram_meters_per_second.
        :type kilogram_meters_per_second: float
        :return: A new instance of Impulse.
        :rtype: Impulse
        """
        return Impulse(kilogram_meters_per_second, ImpulseUnits.KilogramMeterPerSecond)

    
    @staticmethod
    def from_newton_seconds(newton_seconds: float):
        """
        Create a new instance of Impulse from a value in newton_seconds.

        

        :param meters: The Impulse value in newton_seconds.
        :type newton_seconds: float
        :return: A new instance of Impulse.
        :rtype: Impulse
        """
        return Impulse(newton_seconds, ImpulseUnits.NewtonSecond)

    
    @staticmethod
    def from_pound_feet_per_second(pound_feet_per_second: float):
        """
        Create a new instance of Impulse from a value in pound_feet_per_second.

        

        :param meters: The Impulse value in pound_feet_per_second.
        :type pound_feet_per_second: float
        :return: A new instance of Impulse.
        :rtype: Impulse
        """
        return Impulse(pound_feet_per_second, ImpulseUnits.PoundFootPerSecond)

    
    @staticmethod
    def from_pound_force_seconds(pound_force_seconds: float):
        """
        Create a new instance of Impulse from a value in pound_force_seconds.

        

        :param meters: The Impulse value in pound_force_seconds.
        :type pound_force_seconds: float
        :return: A new instance of Impulse.
        :rtype: Impulse
        """
        return Impulse(pound_force_seconds, ImpulseUnits.PoundForceSecond)

    
    @staticmethod
    def from_slug_feet_per_second(slug_feet_per_second: float):
        """
        Create a new instance of Impulse from a value in slug_feet_per_second.

        

        :param meters: The Impulse value in slug_feet_per_second.
        :type slug_feet_per_second: float
        :return: A new instance of Impulse.
        :rtype: Impulse
        """
        return Impulse(slug_feet_per_second, ImpulseUnits.SlugFootPerSecond)

    
    @staticmethod
    def from_nano_newton_seconds(nano_newton_seconds: float):
        """
        Create a new instance of Impulse from a value in nano_newton_seconds.

        

        :param meters: The Impulse value in nano_newton_seconds.
        :type nano_newton_seconds: float
        :return: A new instance of Impulse.
        :rtype: Impulse
        """
        return Impulse(nano_newton_seconds, ImpulseUnits.NanoNewtonSecond)

    
    @staticmethod
    def from_micro_newton_seconds(micro_newton_seconds: float):
        """
        Create a new instance of Impulse from a value in micro_newton_seconds.

        

        :param meters: The Impulse value in micro_newton_seconds.
        :type micro_newton_seconds: float
        :return: A new instance of Impulse.
        :rtype: Impulse
        """
        return Impulse(micro_newton_seconds, ImpulseUnits.MicroNewtonSecond)

    
    @staticmethod
    def from_milli_newton_seconds(milli_newton_seconds: float):
        """
        Create a new instance of Impulse from a value in milli_newton_seconds.

        

        :param meters: The Impulse value in milli_newton_seconds.
        :type milli_newton_seconds: float
        :return: A new instance of Impulse.
        :rtype: Impulse
        """
        return Impulse(milli_newton_seconds, ImpulseUnits.MilliNewtonSecond)

    
    @staticmethod
    def from_centi_newton_seconds(centi_newton_seconds: float):
        """
        Create a new instance of Impulse from a value in centi_newton_seconds.

        

        :param meters: The Impulse value in centi_newton_seconds.
        :type centi_newton_seconds: float
        :return: A new instance of Impulse.
        :rtype: Impulse
        """
        return Impulse(centi_newton_seconds, ImpulseUnits.CentiNewtonSecond)

    
    @staticmethod
    def from_deci_newton_seconds(deci_newton_seconds: float):
        """
        Create a new instance of Impulse from a value in deci_newton_seconds.

        

        :param meters: The Impulse value in deci_newton_seconds.
        :type deci_newton_seconds: float
        :return: A new instance of Impulse.
        :rtype: Impulse
        """
        return Impulse(deci_newton_seconds, ImpulseUnits.DeciNewtonSecond)

    
    @staticmethod
    def from_deca_newton_seconds(deca_newton_seconds: float):
        """
        Create a new instance of Impulse from a value in deca_newton_seconds.

        

        :param meters: The Impulse value in deca_newton_seconds.
        :type deca_newton_seconds: float
        :return: A new instance of Impulse.
        :rtype: Impulse
        """
        return Impulse(deca_newton_seconds, ImpulseUnits.DecaNewtonSecond)

    
    @staticmethod
    def from_kilo_newton_seconds(kilo_newton_seconds: float):
        """
        Create a new instance of Impulse from a value in kilo_newton_seconds.

        

        :param meters: The Impulse value in kilo_newton_seconds.
        :type kilo_newton_seconds: float
        :return: A new instance of Impulse.
        :rtype: Impulse
        """
        return Impulse(kilo_newton_seconds, ImpulseUnits.KiloNewtonSecond)

    
    @staticmethod
    def from_mega_newton_seconds(mega_newton_seconds: float):
        """
        Create a new instance of Impulse from a value in mega_newton_seconds.

        

        :param meters: The Impulse value in mega_newton_seconds.
        :type mega_newton_seconds: float
        :return: A new instance of Impulse.
        :rtype: Impulse
        """
        return Impulse(mega_newton_seconds, ImpulseUnits.MegaNewtonSecond)

    
    @property
    def kilogram_meters_per_second(self) -> float:
        """
        
        """
        if self.__kilogram_meters_per_second != None:
            return self.__kilogram_meters_per_second
        self.__kilogram_meters_per_second = self.__convert_from_base(ImpulseUnits.KilogramMeterPerSecond)
        return self.__kilogram_meters_per_second

    
    @property
    def newton_seconds(self) -> float:
        """
        
        """
        if self.__newton_seconds != None:
            return self.__newton_seconds
        self.__newton_seconds = self.__convert_from_base(ImpulseUnits.NewtonSecond)
        return self.__newton_seconds

    
    @property
    def pound_feet_per_second(self) -> float:
        """
        
        """
        if self.__pound_feet_per_second != None:
            return self.__pound_feet_per_second
        self.__pound_feet_per_second = self.__convert_from_base(ImpulseUnits.PoundFootPerSecond)
        return self.__pound_feet_per_second

    
    @property
    def pound_force_seconds(self) -> float:
        """
        
        """
        if self.__pound_force_seconds != None:
            return self.__pound_force_seconds
        self.__pound_force_seconds = self.__convert_from_base(ImpulseUnits.PoundForceSecond)
        return self.__pound_force_seconds

    
    @property
    def slug_feet_per_second(self) -> float:
        """
        
        """
        if self.__slug_feet_per_second != None:
            return self.__slug_feet_per_second
        self.__slug_feet_per_second = self.__convert_from_base(ImpulseUnits.SlugFootPerSecond)
        return self.__slug_feet_per_second

    
    @property
    def nano_newton_seconds(self) -> float:
        """
        
        """
        if self.__nano_newton_seconds != None:
            return self.__nano_newton_seconds
        self.__nano_newton_seconds = self.__convert_from_base(ImpulseUnits.NanoNewtonSecond)
        return self.__nano_newton_seconds

    
    @property
    def micro_newton_seconds(self) -> float:
        """
        
        """
        if self.__micro_newton_seconds != None:
            return self.__micro_newton_seconds
        self.__micro_newton_seconds = self.__convert_from_base(ImpulseUnits.MicroNewtonSecond)
        return self.__micro_newton_seconds

    
    @property
    def milli_newton_seconds(self) -> float:
        """
        
        """
        if self.__milli_newton_seconds != None:
            return self.__milli_newton_seconds
        self.__milli_newton_seconds = self.__convert_from_base(ImpulseUnits.MilliNewtonSecond)
        return self.__milli_newton_seconds

    
    @property
    def centi_newton_seconds(self) -> float:
        """
        
        """
        if self.__centi_newton_seconds != None:
            return self.__centi_newton_seconds
        self.__centi_newton_seconds = self.__convert_from_base(ImpulseUnits.CentiNewtonSecond)
        return self.__centi_newton_seconds

    
    @property
    def deci_newton_seconds(self) -> float:
        """
        
        """
        if self.__deci_newton_seconds != None:
            return self.__deci_newton_seconds
        self.__deci_newton_seconds = self.__convert_from_base(ImpulseUnits.DeciNewtonSecond)
        return self.__deci_newton_seconds

    
    @property
    def deca_newton_seconds(self) -> float:
        """
        
        """
        if self.__deca_newton_seconds != None:
            return self.__deca_newton_seconds
        self.__deca_newton_seconds = self.__convert_from_base(ImpulseUnits.DecaNewtonSecond)
        return self.__deca_newton_seconds

    
    @property
    def kilo_newton_seconds(self) -> float:
        """
        
        """
        if self.__kilo_newton_seconds != None:
            return self.__kilo_newton_seconds
        self.__kilo_newton_seconds = self.__convert_from_base(ImpulseUnits.KiloNewtonSecond)
        return self.__kilo_newton_seconds

    
    @property
    def mega_newton_seconds(self) -> float:
        """
        
        """
        if self.__mega_newton_seconds != None:
            return self.__mega_newton_seconds
        self.__mega_newton_seconds = self.__convert_from_base(ImpulseUnits.MegaNewtonSecond)
        return self.__mega_newton_seconds

    
    def to_string(self, unit: ImpulseUnits = ImpulseUnits.NewtonSecond) -> string:
        """
        Format the Impulse to string.
        Note! the default format for Impulse is NewtonSecond.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == ImpulseUnits.KilogramMeterPerSecond:
            return f"""{self.kilogram_meters_per_second} kg·m/s"""
        
        if unit == ImpulseUnits.NewtonSecond:
            return f"""{self.newton_seconds} N·s"""
        
        if unit == ImpulseUnits.PoundFootPerSecond:
            return f"""{self.pound_feet_per_second} lb·ft/s"""
        
        if unit == ImpulseUnits.PoundForceSecond:
            return f"""{self.pound_force_seconds} lbf·s"""
        
        if unit == ImpulseUnits.SlugFootPerSecond:
            return f"""{self.slug_feet_per_second} slug·ft/s"""
        
        if unit == ImpulseUnits.NanoNewtonSecond:
            return f"""{self.nano_newton_seconds} """
        
        if unit == ImpulseUnits.MicroNewtonSecond:
            return f"""{self.micro_newton_seconds} """
        
        if unit == ImpulseUnits.MilliNewtonSecond:
            return f"""{self.milli_newton_seconds} """
        
        if unit == ImpulseUnits.CentiNewtonSecond:
            return f"""{self.centi_newton_seconds} """
        
        if unit == ImpulseUnits.DeciNewtonSecond:
            return f"""{self.deci_newton_seconds} """
        
        if unit == ImpulseUnits.DecaNewtonSecond:
            return f"""{self.deca_newton_seconds} """
        
        if unit == ImpulseUnits.KiloNewtonSecond:
            return f"""{self.kilo_newton_seconds} """
        
        if unit == ImpulseUnits.MegaNewtonSecond:
            return f"""{self.mega_newton_seconds} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: ImpulseUnits = ImpulseUnits.NewtonSecond) -> string:
        """
        Get Impulse unit abbreviation.
        Note! the default abbreviation for Impulse is NewtonSecond.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == ImpulseUnits.KilogramMeterPerSecond:
            return """kg·m/s"""
        
        if unit_abbreviation == ImpulseUnits.NewtonSecond:
            return """N·s"""
        
        if unit_abbreviation == ImpulseUnits.PoundFootPerSecond:
            return """lb·ft/s"""
        
        if unit_abbreviation == ImpulseUnits.PoundForceSecond:
            return """lbf·s"""
        
        if unit_abbreviation == ImpulseUnits.SlugFootPerSecond:
            return """slug·ft/s"""
        
        if unit_abbreviation == ImpulseUnits.NanoNewtonSecond:
            return """"""
        
        if unit_abbreviation == ImpulseUnits.MicroNewtonSecond:
            return """"""
        
        if unit_abbreviation == ImpulseUnits.MilliNewtonSecond:
            return """"""
        
        if unit_abbreviation == ImpulseUnits.CentiNewtonSecond:
            return """"""
        
        if unit_abbreviation == ImpulseUnits.DeciNewtonSecond:
            return """"""
        
        if unit_abbreviation == ImpulseUnits.DecaNewtonSecond:
            return """"""
        
        if unit_abbreviation == ImpulseUnits.KiloNewtonSecond:
            return """"""
        
        if unit_abbreviation == ImpulseUnits.MegaNewtonSecond:
            return """"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, Impulse):
            raise TypeError("unsupported operand type(s) for +: 'Impulse' and '{}'".format(type(other).__name__))
        return Impulse(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, Impulse):
            raise TypeError("unsupported operand type(s) for *: 'Impulse' and '{}'".format(type(other).__name__))
        return Impulse(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, Impulse):
            raise TypeError("unsupported operand type(s) for -: 'Impulse' and '{}'".format(type(other).__name__))
        return Impulse(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, Impulse):
            raise TypeError("unsupported operand type(s) for /: 'Impulse' and '{}'".format(type(other).__name__))
        return Impulse(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, Impulse):
            raise TypeError("unsupported operand type(s) for %: 'Impulse' and '{}'".format(type(other).__name__))
        return Impulse(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, Impulse):
            raise TypeError("unsupported operand type(s) for **: 'Impulse' and '{}'".format(type(other).__name__))
        return Impulse(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, Impulse):
            raise TypeError("unsupported operand type(s) for ==: 'Impulse' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, Impulse):
            raise TypeError("unsupported operand type(s) for <: 'Impulse' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, Impulse):
            raise TypeError("unsupported operand type(s) for >: 'Impulse' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, Impulse):
            raise TypeError("unsupported operand type(s) for <=: 'Impulse' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, Impulse):
            raise TypeError("unsupported operand type(s) for >=: 'Impulse' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value
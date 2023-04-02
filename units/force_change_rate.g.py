from enum import Enum
import math
import string


class ForceChangeRateUnits(Enum):
        """
            ForceChangeRateUnits enumeration
        """
        
        NewtonPerMinute = 'newton_per_minute'
        """
            
        """
        
        NewtonPerSecond = 'newton_per_second'
        """
            
        """
        
        PoundForcePerMinute = 'pound_force_per_minute'
        """
            
        """
        
        PoundForcePerSecond = 'pound_force_per_second'
        """
            
        """
        
        DecaNewtonPerMinute = 'deca_newton_per_minute'
        """
            
        """
        
        KiloNewtonPerMinute = 'kilo_newton_per_minute'
        """
            
        """
        
        NanoNewtonPerSecond = 'nano_newton_per_second'
        """
            
        """
        
        MicroNewtonPerSecond = 'micro_newton_per_second'
        """
            
        """
        
        MilliNewtonPerSecond = 'milli_newton_per_second'
        """
            
        """
        
        CentiNewtonPerSecond = 'centi_newton_per_second'
        """
            
        """
        
        DeciNewtonPerSecond = 'deci_newton_per_second'
        """
            
        """
        
        DecaNewtonPerSecond = 'deca_newton_per_second'
        """
            
        """
        
        KiloNewtonPerSecond = 'kilo_newton_per_second'
        """
            
        """
        
        KiloPoundForcePerMinute = 'kilo_pound_force_per_minute'
        """
            
        """
        
        KiloPoundForcePerSecond = 'kilo_pound_force_per_second'
        """
            
        """
        
    
class ForceChangeRate:
    """
    Force change rate is the ratio of the force change to the time during which the change occurred (value of force changes per unit time).

    Args:
        value (float): The value.
        from_unit (ForceChangeRateUnits): The ForceChangeRate unit to create from, The default unit is NewtonPerSecond
    """
    def __init__(self, value: float, from_unit: ForceChangeRateUnits = ForceChangeRateUnits.NewtonPerSecond):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__newtons_per_minute = None
        
        self.__newtons_per_second = None
        
        self.__pounds_force_per_minute = None
        
        self.__pounds_force_per_second = None
        
        self.__deca_newtons_per_minute = None
        
        self.__kilo_newtons_per_minute = None
        
        self.__nano_newtons_per_second = None
        
        self.__micro_newtons_per_second = None
        
        self.__milli_newtons_per_second = None
        
        self.__centi_newtons_per_second = None
        
        self.__deci_newtons_per_second = None
        
        self.__deca_newtons_per_second = None
        
        self.__kilo_newtons_per_second = None
        
        self.__kilo_pounds_force_per_minute = None
        
        self.__kilo_pounds_force_per_second = None
        

    def __convert_from_base(self, from_unit: ForceChangeRateUnits) -> float:
        value = self.__value
        
        if from_unit == ForceChangeRateUnits.NewtonPerMinute:
            return (value * 60)
        
        if from_unit == ForceChangeRateUnits.NewtonPerSecond:
            return (value)
        
        if from_unit == ForceChangeRateUnits.PoundForcePerMinute:
            return (value / 4.4482216152605095551842641431421 * 60)
        
        if from_unit == ForceChangeRateUnits.PoundForcePerSecond:
            return (value / 4.4482216152605095551842641431421)
        
        if from_unit == ForceChangeRateUnits.DecaNewtonPerMinute:
            return ((value * 60) / 10.0)
        
        if from_unit == ForceChangeRateUnits.KiloNewtonPerMinute:
            return ((value * 60) / 1000.0)
        
        if from_unit == ForceChangeRateUnits.NanoNewtonPerSecond:
            return ((value) / 1e-09)
        
        if from_unit == ForceChangeRateUnits.MicroNewtonPerSecond:
            return ((value) / 1e-06)
        
        if from_unit == ForceChangeRateUnits.MilliNewtonPerSecond:
            return ((value) / 0.001)
        
        if from_unit == ForceChangeRateUnits.CentiNewtonPerSecond:
            return ((value) / 0.01)
        
        if from_unit == ForceChangeRateUnits.DeciNewtonPerSecond:
            return ((value) / 0.1)
        
        if from_unit == ForceChangeRateUnits.DecaNewtonPerSecond:
            return ((value) / 10.0)
        
        if from_unit == ForceChangeRateUnits.KiloNewtonPerSecond:
            return ((value) / 1000.0)
        
        if from_unit == ForceChangeRateUnits.KiloPoundForcePerMinute:
            return ((value / 4.4482216152605095551842641431421 * 60) / 1000.0)
        
        if from_unit == ForceChangeRateUnits.KiloPoundForcePerSecond:
            return ((value / 4.4482216152605095551842641431421) / 1000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: ForceChangeRateUnits) -> float:
        
        if to_unit == ForceChangeRateUnits.NewtonPerMinute:
            return (value / 60)
        
        if to_unit == ForceChangeRateUnits.NewtonPerSecond:
            return (value)
        
        if to_unit == ForceChangeRateUnits.PoundForcePerMinute:
            return (value * 4.4482216152605095551842641431421 / 60)
        
        if to_unit == ForceChangeRateUnits.PoundForcePerSecond:
            return (value * 4.4482216152605095551842641431421)
        
        if to_unit == ForceChangeRateUnits.DecaNewtonPerMinute:
            return ((value / 60) * 10.0)
        
        if to_unit == ForceChangeRateUnits.KiloNewtonPerMinute:
            return ((value / 60) * 1000.0)
        
        if to_unit == ForceChangeRateUnits.NanoNewtonPerSecond:
            return ((value) * 1e-09)
        
        if to_unit == ForceChangeRateUnits.MicroNewtonPerSecond:
            return ((value) * 1e-06)
        
        if to_unit == ForceChangeRateUnits.MilliNewtonPerSecond:
            return ((value) * 0.001)
        
        if to_unit == ForceChangeRateUnits.CentiNewtonPerSecond:
            return ((value) * 0.01)
        
        if to_unit == ForceChangeRateUnits.DeciNewtonPerSecond:
            return ((value) * 0.1)
        
        if to_unit == ForceChangeRateUnits.DecaNewtonPerSecond:
            return ((value) * 10.0)
        
        if to_unit == ForceChangeRateUnits.KiloNewtonPerSecond:
            return ((value) * 1000.0)
        
        if to_unit == ForceChangeRateUnits.KiloPoundForcePerMinute:
            return ((value * 4.4482216152605095551842641431421 / 60) * 1000.0)
        
        if to_unit == ForceChangeRateUnits.KiloPoundForcePerSecond:
            return ((value * 4.4482216152605095551842641431421) * 1000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
    @staticmethod
    def from_newtons_per_minute(newtons_per_minute: float):
        """
        Create a new instance of ForceChangeRate from a value in newtons_per_minute.

        

        :param meters: The ForceChangeRate value in newtons_per_minute.
        :type newtons_per_minute: float
        :return: A new instance of ForceChangeRate.
        :rtype: ForceChangeRate
        """
        return ForceChangeRate(newtons_per_minute, ForceChangeRateUnits.NewtonPerMinute)

    
    @staticmethod
    def from_newtons_per_second(newtons_per_second: float):
        """
        Create a new instance of ForceChangeRate from a value in newtons_per_second.

        

        :param meters: The ForceChangeRate value in newtons_per_second.
        :type newtons_per_second: float
        :return: A new instance of ForceChangeRate.
        :rtype: ForceChangeRate
        """
        return ForceChangeRate(newtons_per_second, ForceChangeRateUnits.NewtonPerSecond)

    
    @staticmethod
    def from_pounds_force_per_minute(pounds_force_per_minute: float):
        """
        Create a new instance of ForceChangeRate from a value in pounds_force_per_minute.

        

        :param meters: The ForceChangeRate value in pounds_force_per_minute.
        :type pounds_force_per_minute: float
        :return: A new instance of ForceChangeRate.
        :rtype: ForceChangeRate
        """
        return ForceChangeRate(pounds_force_per_minute, ForceChangeRateUnits.PoundForcePerMinute)

    
    @staticmethod
    def from_pounds_force_per_second(pounds_force_per_second: float):
        """
        Create a new instance of ForceChangeRate from a value in pounds_force_per_second.

        

        :param meters: The ForceChangeRate value in pounds_force_per_second.
        :type pounds_force_per_second: float
        :return: A new instance of ForceChangeRate.
        :rtype: ForceChangeRate
        """
        return ForceChangeRate(pounds_force_per_second, ForceChangeRateUnits.PoundForcePerSecond)

    
    @staticmethod
    def from_deca_newtons_per_minute(deca_newtons_per_minute: float):
        """
        Create a new instance of ForceChangeRate from a value in deca_newtons_per_minute.

        

        :param meters: The ForceChangeRate value in deca_newtons_per_minute.
        :type deca_newtons_per_minute: float
        :return: A new instance of ForceChangeRate.
        :rtype: ForceChangeRate
        """
        return ForceChangeRate(deca_newtons_per_minute, ForceChangeRateUnits.DecaNewtonPerMinute)

    
    @staticmethod
    def from_kilo_newtons_per_minute(kilo_newtons_per_minute: float):
        """
        Create a new instance of ForceChangeRate from a value in kilo_newtons_per_minute.

        

        :param meters: The ForceChangeRate value in kilo_newtons_per_minute.
        :type kilo_newtons_per_minute: float
        :return: A new instance of ForceChangeRate.
        :rtype: ForceChangeRate
        """
        return ForceChangeRate(kilo_newtons_per_minute, ForceChangeRateUnits.KiloNewtonPerMinute)

    
    @staticmethod
    def from_nano_newtons_per_second(nano_newtons_per_second: float):
        """
        Create a new instance of ForceChangeRate from a value in nano_newtons_per_second.

        

        :param meters: The ForceChangeRate value in nano_newtons_per_second.
        :type nano_newtons_per_second: float
        :return: A new instance of ForceChangeRate.
        :rtype: ForceChangeRate
        """
        return ForceChangeRate(nano_newtons_per_second, ForceChangeRateUnits.NanoNewtonPerSecond)

    
    @staticmethod
    def from_micro_newtons_per_second(micro_newtons_per_second: float):
        """
        Create a new instance of ForceChangeRate from a value in micro_newtons_per_second.

        

        :param meters: The ForceChangeRate value in micro_newtons_per_second.
        :type micro_newtons_per_second: float
        :return: A new instance of ForceChangeRate.
        :rtype: ForceChangeRate
        """
        return ForceChangeRate(micro_newtons_per_second, ForceChangeRateUnits.MicroNewtonPerSecond)

    
    @staticmethod
    def from_milli_newtons_per_second(milli_newtons_per_second: float):
        """
        Create a new instance of ForceChangeRate from a value in milli_newtons_per_second.

        

        :param meters: The ForceChangeRate value in milli_newtons_per_second.
        :type milli_newtons_per_second: float
        :return: A new instance of ForceChangeRate.
        :rtype: ForceChangeRate
        """
        return ForceChangeRate(milli_newtons_per_second, ForceChangeRateUnits.MilliNewtonPerSecond)

    
    @staticmethod
    def from_centi_newtons_per_second(centi_newtons_per_second: float):
        """
        Create a new instance of ForceChangeRate from a value in centi_newtons_per_second.

        

        :param meters: The ForceChangeRate value in centi_newtons_per_second.
        :type centi_newtons_per_second: float
        :return: A new instance of ForceChangeRate.
        :rtype: ForceChangeRate
        """
        return ForceChangeRate(centi_newtons_per_second, ForceChangeRateUnits.CentiNewtonPerSecond)

    
    @staticmethod
    def from_deci_newtons_per_second(deci_newtons_per_second: float):
        """
        Create a new instance of ForceChangeRate from a value in deci_newtons_per_second.

        

        :param meters: The ForceChangeRate value in deci_newtons_per_second.
        :type deci_newtons_per_second: float
        :return: A new instance of ForceChangeRate.
        :rtype: ForceChangeRate
        """
        return ForceChangeRate(deci_newtons_per_second, ForceChangeRateUnits.DeciNewtonPerSecond)

    
    @staticmethod
    def from_deca_newtons_per_second(deca_newtons_per_second: float):
        """
        Create a new instance of ForceChangeRate from a value in deca_newtons_per_second.

        

        :param meters: The ForceChangeRate value in deca_newtons_per_second.
        :type deca_newtons_per_second: float
        :return: A new instance of ForceChangeRate.
        :rtype: ForceChangeRate
        """
        return ForceChangeRate(deca_newtons_per_second, ForceChangeRateUnits.DecaNewtonPerSecond)

    
    @staticmethod
    def from_kilo_newtons_per_second(kilo_newtons_per_second: float):
        """
        Create a new instance of ForceChangeRate from a value in kilo_newtons_per_second.

        

        :param meters: The ForceChangeRate value in kilo_newtons_per_second.
        :type kilo_newtons_per_second: float
        :return: A new instance of ForceChangeRate.
        :rtype: ForceChangeRate
        """
        return ForceChangeRate(kilo_newtons_per_second, ForceChangeRateUnits.KiloNewtonPerSecond)

    
    @staticmethod
    def from_kilo_pounds_force_per_minute(kilo_pounds_force_per_minute: float):
        """
        Create a new instance of ForceChangeRate from a value in kilo_pounds_force_per_minute.

        

        :param meters: The ForceChangeRate value in kilo_pounds_force_per_minute.
        :type kilo_pounds_force_per_minute: float
        :return: A new instance of ForceChangeRate.
        :rtype: ForceChangeRate
        """
        return ForceChangeRate(kilo_pounds_force_per_minute, ForceChangeRateUnits.KiloPoundForcePerMinute)

    
    @staticmethod
    def from_kilo_pounds_force_per_second(kilo_pounds_force_per_second: float):
        """
        Create a new instance of ForceChangeRate from a value in kilo_pounds_force_per_second.

        

        :param meters: The ForceChangeRate value in kilo_pounds_force_per_second.
        :type kilo_pounds_force_per_second: float
        :return: A new instance of ForceChangeRate.
        :rtype: ForceChangeRate
        """
        return ForceChangeRate(kilo_pounds_force_per_second, ForceChangeRateUnits.KiloPoundForcePerSecond)

    
    @property
    def newtons_per_minute(self) -> float:
        """
        
        """
        if self.__newtons_per_minute != None:
            return self.__newtons_per_minute
        self.__newtons_per_minute = self.__convert_from_base(ForceChangeRateUnits.NewtonPerMinute)
        return self.__newtons_per_minute

    
    @property
    def newtons_per_second(self) -> float:
        """
        
        """
        if self.__newtons_per_second != None:
            return self.__newtons_per_second
        self.__newtons_per_second = self.__convert_from_base(ForceChangeRateUnits.NewtonPerSecond)
        return self.__newtons_per_second

    
    @property
    def pounds_force_per_minute(self) -> float:
        """
        
        """
        if self.__pounds_force_per_minute != None:
            return self.__pounds_force_per_minute
        self.__pounds_force_per_minute = self.__convert_from_base(ForceChangeRateUnits.PoundForcePerMinute)
        return self.__pounds_force_per_minute

    
    @property
    def pounds_force_per_second(self) -> float:
        """
        
        """
        if self.__pounds_force_per_second != None:
            return self.__pounds_force_per_second
        self.__pounds_force_per_second = self.__convert_from_base(ForceChangeRateUnits.PoundForcePerSecond)
        return self.__pounds_force_per_second

    
    @property
    def deca_newtons_per_minute(self) -> float:
        """
        
        """
        if self.__deca_newtons_per_minute != None:
            return self.__deca_newtons_per_minute
        self.__deca_newtons_per_minute = self.__convert_from_base(ForceChangeRateUnits.DecaNewtonPerMinute)
        return self.__deca_newtons_per_minute

    
    @property
    def kilo_newtons_per_minute(self) -> float:
        """
        
        """
        if self.__kilo_newtons_per_minute != None:
            return self.__kilo_newtons_per_minute
        self.__kilo_newtons_per_minute = self.__convert_from_base(ForceChangeRateUnits.KiloNewtonPerMinute)
        return self.__kilo_newtons_per_minute

    
    @property
    def nano_newtons_per_second(self) -> float:
        """
        
        """
        if self.__nano_newtons_per_second != None:
            return self.__nano_newtons_per_second
        self.__nano_newtons_per_second = self.__convert_from_base(ForceChangeRateUnits.NanoNewtonPerSecond)
        return self.__nano_newtons_per_second

    
    @property
    def micro_newtons_per_second(self) -> float:
        """
        
        """
        if self.__micro_newtons_per_second != None:
            return self.__micro_newtons_per_second
        self.__micro_newtons_per_second = self.__convert_from_base(ForceChangeRateUnits.MicroNewtonPerSecond)
        return self.__micro_newtons_per_second

    
    @property
    def milli_newtons_per_second(self) -> float:
        """
        
        """
        if self.__milli_newtons_per_second != None:
            return self.__milli_newtons_per_second
        self.__milli_newtons_per_second = self.__convert_from_base(ForceChangeRateUnits.MilliNewtonPerSecond)
        return self.__milli_newtons_per_second

    
    @property
    def centi_newtons_per_second(self) -> float:
        """
        
        """
        if self.__centi_newtons_per_second != None:
            return self.__centi_newtons_per_second
        self.__centi_newtons_per_second = self.__convert_from_base(ForceChangeRateUnits.CentiNewtonPerSecond)
        return self.__centi_newtons_per_second

    
    @property
    def deci_newtons_per_second(self) -> float:
        """
        
        """
        if self.__deci_newtons_per_second != None:
            return self.__deci_newtons_per_second
        self.__deci_newtons_per_second = self.__convert_from_base(ForceChangeRateUnits.DeciNewtonPerSecond)
        return self.__deci_newtons_per_second

    
    @property
    def deca_newtons_per_second(self) -> float:
        """
        
        """
        if self.__deca_newtons_per_second != None:
            return self.__deca_newtons_per_second
        self.__deca_newtons_per_second = self.__convert_from_base(ForceChangeRateUnits.DecaNewtonPerSecond)
        return self.__deca_newtons_per_second

    
    @property
    def kilo_newtons_per_second(self) -> float:
        """
        
        """
        if self.__kilo_newtons_per_second != None:
            return self.__kilo_newtons_per_second
        self.__kilo_newtons_per_second = self.__convert_from_base(ForceChangeRateUnits.KiloNewtonPerSecond)
        return self.__kilo_newtons_per_second

    
    @property
    def kilo_pounds_force_per_minute(self) -> float:
        """
        
        """
        if self.__kilo_pounds_force_per_minute != None:
            return self.__kilo_pounds_force_per_minute
        self.__kilo_pounds_force_per_minute = self.__convert_from_base(ForceChangeRateUnits.KiloPoundForcePerMinute)
        return self.__kilo_pounds_force_per_minute

    
    @property
    def kilo_pounds_force_per_second(self) -> float:
        """
        
        """
        if self.__kilo_pounds_force_per_second != None:
            return self.__kilo_pounds_force_per_second
        self.__kilo_pounds_force_per_second = self.__convert_from_base(ForceChangeRateUnits.KiloPoundForcePerSecond)
        return self.__kilo_pounds_force_per_second

    
    def to_string(self, unit: ForceChangeRateUnits = ForceChangeRateUnits.NewtonPerSecond) -> string:
        """
        Format the ForceChangeRate to string.
        Note! the default format for ForceChangeRate is NewtonPerSecond.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == ForceChangeRateUnits.NewtonPerMinute:
            return f"""{self.newtons_per_minute} N/min"""
        
        if unit == ForceChangeRateUnits.NewtonPerSecond:
            return f"""{self.newtons_per_second} N/s"""
        
        if unit == ForceChangeRateUnits.PoundForcePerMinute:
            return f"""{self.pounds_force_per_minute} lbf/min"""
        
        if unit == ForceChangeRateUnits.PoundForcePerSecond:
            return f"""{self.pounds_force_per_second} lbf/s"""
        
        if unit == ForceChangeRateUnits.DecaNewtonPerMinute:
            return f"""{self.deca_newtons_per_minute} """
        
        if unit == ForceChangeRateUnits.KiloNewtonPerMinute:
            return f"""{self.kilo_newtons_per_minute} """
        
        if unit == ForceChangeRateUnits.NanoNewtonPerSecond:
            return f"""{self.nano_newtons_per_second} """
        
        if unit == ForceChangeRateUnits.MicroNewtonPerSecond:
            return f"""{self.micro_newtons_per_second} """
        
        if unit == ForceChangeRateUnits.MilliNewtonPerSecond:
            return f"""{self.milli_newtons_per_second} """
        
        if unit == ForceChangeRateUnits.CentiNewtonPerSecond:
            return f"""{self.centi_newtons_per_second} """
        
        if unit == ForceChangeRateUnits.DeciNewtonPerSecond:
            return f"""{self.deci_newtons_per_second} """
        
        if unit == ForceChangeRateUnits.DecaNewtonPerSecond:
            return f"""{self.deca_newtons_per_second} """
        
        if unit == ForceChangeRateUnits.KiloNewtonPerSecond:
            return f"""{self.kilo_newtons_per_second} """
        
        if unit == ForceChangeRateUnits.KiloPoundForcePerMinute:
            return f"""{self.kilo_pounds_force_per_minute} """
        
        if unit == ForceChangeRateUnits.KiloPoundForcePerSecond:
            return f"""{self.kilo_pounds_force_per_second} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: ForceChangeRateUnits = ForceChangeRateUnits.NewtonPerSecond) -> string:
        """
        Get ForceChangeRate unit abbreviation.
        Note! the default abbreviation for ForceChangeRate is NewtonPerSecond.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == ForceChangeRateUnits.NewtonPerMinute:
            return """N/min"""
        
        if unit_abbreviation == ForceChangeRateUnits.NewtonPerSecond:
            return """N/s"""
        
        if unit_abbreviation == ForceChangeRateUnits.PoundForcePerMinute:
            return """lbf/min"""
        
        if unit_abbreviation == ForceChangeRateUnits.PoundForcePerSecond:
            return """lbf/s"""
        
        if unit_abbreviation == ForceChangeRateUnits.DecaNewtonPerMinute:
            return """"""
        
        if unit_abbreviation == ForceChangeRateUnits.KiloNewtonPerMinute:
            return """"""
        
        if unit_abbreviation == ForceChangeRateUnits.NanoNewtonPerSecond:
            return """"""
        
        if unit_abbreviation == ForceChangeRateUnits.MicroNewtonPerSecond:
            return """"""
        
        if unit_abbreviation == ForceChangeRateUnits.MilliNewtonPerSecond:
            return """"""
        
        if unit_abbreviation == ForceChangeRateUnits.CentiNewtonPerSecond:
            return """"""
        
        if unit_abbreviation == ForceChangeRateUnits.DeciNewtonPerSecond:
            return """"""
        
        if unit_abbreviation == ForceChangeRateUnits.DecaNewtonPerSecond:
            return """"""
        
        if unit_abbreviation == ForceChangeRateUnits.KiloNewtonPerSecond:
            return """"""
        
        if unit_abbreviation == ForceChangeRateUnits.KiloPoundForcePerMinute:
            return """"""
        
        if unit_abbreviation == ForceChangeRateUnits.KiloPoundForcePerSecond:
            return """"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, ForceChangeRate):
            raise TypeError("unsupported operand type(s) for +: 'ForceChangeRate' and '{}'".format(type(other).__name__))
        return ForceChangeRate(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, ForceChangeRate):
            raise TypeError("unsupported operand type(s) for *: 'ForceChangeRate' and '{}'".format(type(other).__name__))
        return ForceChangeRate(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, ForceChangeRate):
            raise TypeError("unsupported operand type(s) for -: 'ForceChangeRate' and '{}'".format(type(other).__name__))
        return ForceChangeRate(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, ForceChangeRate):
            raise TypeError("unsupported operand type(s) for /: 'ForceChangeRate' and '{}'".format(type(other).__name__))
        return ForceChangeRate(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, ForceChangeRate):
            raise TypeError("unsupported operand type(s) for %: 'ForceChangeRate' and '{}'".format(type(other).__name__))
        return ForceChangeRate(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, ForceChangeRate):
            raise TypeError("unsupported operand type(s) for **: 'ForceChangeRate' and '{}'".format(type(other).__name__))
        return ForceChangeRate(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, ForceChangeRate):
            raise TypeError("unsupported operand type(s) for ==: 'ForceChangeRate' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, ForceChangeRate):
            raise TypeError("unsupported operand type(s) for <: 'ForceChangeRate' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, ForceChangeRate):
            raise TypeError("unsupported operand type(s) for >: 'ForceChangeRate' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, ForceChangeRate):
            raise TypeError("unsupported operand type(s) for <=: 'ForceChangeRate' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, ForceChangeRate):
            raise TypeError("unsupported operand type(s) for >=: 'ForceChangeRate' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value
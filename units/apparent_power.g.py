from enum import Enum
import math
import string


class ApparentPowerUnits(Enum):
        """
            ApparentPowerUnits enumeration
        """
        
        Voltampere = 'voltampere'
        """
            
        """
        
        MicroVoltampere = 'micro_voltampere'
        """
            
        """
        
        MilliVoltampere = 'milli_voltampere'
        """
            
        """
        
        KiloVoltampere = 'kilo_voltampere'
        """
            
        """
        
        MegaVoltampere = 'mega_voltampere'
        """
            
        """
        
        GigaVoltampere = 'giga_voltampere'
        """
            
        """
        
    
class ApparentPower:
    """
    Power engineers measure apparent power as the magnitude of the vector sum of active and reactive power. Apparent power is the product of the root-mean-square of voltage and current.

    Args:
        value (float): The value.
        from_unit (ApparentPowerUnits): The ApparentPower unit to create from, The default unit is Voltampere
    """
    def __init__(self, value: float, from_unit: ApparentPowerUnits = ApparentPowerUnits.Voltampere):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__voltamperes = None
        
        self.__micro_voltamperes = None
        
        self.__milli_voltamperes = None
        
        self.__kilo_voltamperes = None
        
        self.__mega_voltamperes = None
        
        self.__giga_voltamperes = None
        

    def __convert_from_base(self, from_unit: ApparentPowerUnits) -> float:
        value = self.__value
        
        if from_unit == ApparentPowerUnits.Voltampere:
            return (value)
        
        if from_unit == ApparentPowerUnits.MicroVoltampere:
            return ((value) / 1e-06)
        
        if from_unit == ApparentPowerUnits.MilliVoltampere:
            return ((value) / 0.001)
        
        if from_unit == ApparentPowerUnits.KiloVoltampere:
            return ((value) / 1000.0)
        
        if from_unit == ApparentPowerUnits.MegaVoltampere:
            return ((value) / 1000000.0)
        
        if from_unit == ApparentPowerUnits.GigaVoltampere:
            return ((value) / 1000000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: ApparentPowerUnits) -> float:
        
        if to_unit == ApparentPowerUnits.Voltampere:
            return (value)
        
        if to_unit == ApparentPowerUnits.MicroVoltampere:
            return ((value) * 1e-06)
        
        if to_unit == ApparentPowerUnits.MilliVoltampere:
            return ((value) * 0.001)
        
        if to_unit == ApparentPowerUnits.KiloVoltampere:
            return ((value) * 1000.0)
        
        if to_unit == ApparentPowerUnits.MegaVoltampere:
            return ((value) * 1000000.0)
        
        if to_unit == ApparentPowerUnits.GigaVoltampere:
            return ((value) * 1000000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
    @staticmethod
    def from_voltamperes(voltamperes: float):
        """
        Create a new instance of ApparentPower from a value in voltamperes.

        

        :param meters: The ApparentPower value in voltamperes.
        :type voltamperes: float
        :return: A new instance of ApparentPower.
        :rtype: ApparentPower
        """
        return ApparentPower(voltamperes, ApparentPowerUnits.Voltampere)

    
    @staticmethod
    def from_micro_voltamperes(micro_voltamperes: float):
        """
        Create a new instance of ApparentPower from a value in micro_voltamperes.

        

        :param meters: The ApparentPower value in micro_voltamperes.
        :type micro_voltamperes: float
        :return: A new instance of ApparentPower.
        :rtype: ApparentPower
        """
        return ApparentPower(micro_voltamperes, ApparentPowerUnits.MicroVoltampere)

    
    @staticmethod
    def from_milli_voltamperes(milli_voltamperes: float):
        """
        Create a new instance of ApparentPower from a value in milli_voltamperes.

        

        :param meters: The ApparentPower value in milli_voltamperes.
        :type milli_voltamperes: float
        :return: A new instance of ApparentPower.
        :rtype: ApparentPower
        """
        return ApparentPower(milli_voltamperes, ApparentPowerUnits.MilliVoltampere)

    
    @staticmethod
    def from_kilo_voltamperes(kilo_voltamperes: float):
        """
        Create a new instance of ApparentPower from a value in kilo_voltamperes.

        

        :param meters: The ApparentPower value in kilo_voltamperes.
        :type kilo_voltamperes: float
        :return: A new instance of ApparentPower.
        :rtype: ApparentPower
        """
        return ApparentPower(kilo_voltamperes, ApparentPowerUnits.KiloVoltampere)

    
    @staticmethod
    def from_mega_voltamperes(mega_voltamperes: float):
        """
        Create a new instance of ApparentPower from a value in mega_voltamperes.

        

        :param meters: The ApparentPower value in mega_voltamperes.
        :type mega_voltamperes: float
        :return: A new instance of ApparentPower.
        :rtype: ApparentPower
        """
        return ApparentPower(mega_voltamperes, ApparentPowerUnits.MegaVoltampere)

    
    @staticmethod
    def from_giga_voltamperes(giga_voltamperes: float):
        """
        Create a new instance of ApparentPower from a value in giga_voltamperes.

        

        :param meters: The ApparentPower value in giga_voltamperes.
        :type giga_voltamperes: float
        :return: A new instance of ApparentPower.
        :rtype: ApparentPower
        """
        return ApparentPower(giga_voltamperes, ApparentPowerUnits.GigaVoltampere)

    
    @property
    def voltamperes(self) -> float:
        """
        
        """
        if self.__voltamperes != None:
            return self.__voltamperes
        self.__voltamperes = self.__convert_from_base(ApparentPowerUnits.Voltampere)
        return self.__voltamperes

    
    @property
    def micro_voltamperes(self) -> float:
        """
        
        """
        if self.__micro_voltamperes != None:
            return self.__micro_voltamperes
        self.__micro_voltamperes = self.__convert_from_base(ApparentPowerUnits.MicroVoltampere)
        return self.__micro_voltamperes

    
    @property
    def milli_voltamperes(self) -> float:
        """
        
        """
        if self.__milli_voltamperes != None:
            return self.__milli_voltamperes
        self.__milli_voltamperes = self.__convert_from_base(ApparentPowerUnits.MilliVoltampere)
        return self.__milli_voltamperes

    
    @property
    def kilo_voltamperes(self) -> float:
        """
        
        """
        if self.__kilo_voltamperes != None:
            return self.__kilo_voltamperes
        self.__kilo_voltamperes = self.__convert_from_base(ApparentPowerUnits.KiloVoltampere)
        return self.__kilo_voltamperes

    
    @property
    def mega_voltamperes(self) -> float:
        """
        
        """
        if self.__mega_voltamperes != None:
            return self.__mega_voltamperes
        self.__mega_voltamperes = self.__convert_from_base(ApparentPowerUnits.MegaVoltampere)
        return self.__mega_voltamperes

    
    @property
    def giga_voltamperes(self) -> float:
        """
        
        """
        if self.__giga_voltamperes != None:
            return self.__giga_voltamperes
        self.__giga_voltamperes = self.__convert_from_base(ApparentPowerUnits.GigaVoltampere)
        return self.__giga_voltamperes

    
    def to_string(self, unit: ApparentPowerUnits = ApparentPowerUnits.Voltampere) -> string:
        """
        Format the ApparentPower to string.
        Note! the default format for ApparentPower is Voltampere.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == ApparentPowerUnits.Voltampere:
            return f"""{self.voltamperes} VA"""
        
        if unit == ApparentPowerUnits.MicroVoltampere:
            return f"""{self.micro_voltamperes} """
        
        if unit == ApparentPowerUnits.MilliVoltampere:
            return f"""{self.milli_voltamperes} """
        
        if unit == ApparentPowerUnits.KiloVoltampere:
            return f"""{self.kilo_voltamperes} """
        
        if unit == ApparentPowerUnits.MegaVoltampere:
            return f"""{self.mega_voltamperes} """
        
        if unit == ApparentPowerUnits.GigaVoltampere:
            return f"""{self.giga_voltamperes} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: ApparentPowerUnits = ApparentPowerUnits.Voltampere) -> string:
        """
        Get ApparentPower unit abbreviation.
        Note! the default abbreviation for ApparentPower is Voltampere.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == ApparentPowerUnits.Voltampere:
            return """VA"""
        
        if unit_abbreviation == ApparentPowerUnits.MicroVoltampere:
            return """"""
        
        if unit_abbreviation == ApparentPowerUnits.MilliVoltampere:
            return """"""
        
        if unit_abbreviation == ApparentPowerUnits.KiloVoltampere:
            return """"""
        
        if unit_abbreviation == ApparentPowerUnits.MegaVoltampere:
            return """"""
        
        if unit_abbreviation == ApparentPowerUnits.GigaVoltampere:
            return """"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, ApparentPower):
            raise TypeError("unsupported operand type(s) for +: 'ApparentPower' and '{}'".format(type(other).__name__))
        return ApparentPower(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, ApparentPower):
            raise TypeError("unsupported operand type(s) for *: 'ApparentPower' and '{}'".format(type(other).__name__))
        return ApparentPower(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, ApparentPower):
            raise TypeError("unsupported operand type(s) for -: 'ApparentPower' and '{}'".format(type(other).__name__))
        return ApparentPower(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, ApparentPower):
            raise TypeError("unsupported operand type(s) for /: 'ApparentPower' and '{}'".format(type(other).__name__))
        return ApparentPower(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, ApparentPower):
            raise TypeError("unsupported operand type(s) for %: 'ApparentPower' and '{}'".format(type(other).__name__))
        return ApparentPower(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, ApparentPower):
            raise TypeError("unsupported operand type(s) for **: 'ApparentPower' and '{}'".format(type(other).__name__))
        return ApparentPower(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, ApparentPower):
            raise TypeError("unsupported operand type(s) for ==: 'ApparentPower' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, ApparentPower):
            raise TypeError("unsupported operand type(s) for <: 'ApparentPower' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, ApparentPower):
            raise TypeError("unsupported operand type(s) for >: 'ApparentPower' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, ApparentPower):
            raise TypeError("unsupported operand type(s) for <=: 'ApparentPower' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, ApparentPower):
            raise TypeError("unsupported operand type(s) for >=: 'ApparentPower' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value
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
        
        Microvoltampere = 'microvoltampere'
        """
            
        """
        
        Millivoltampere = 'millivoltampere'
        """
            
        """
        
        Kilovoltampere = 'kilovoltampere'
        """
            
        """
        
        Megavoltampere = 'megavoltampere'
        """
            
        """
        
        Gigavoltampere = 'gigavoltampere'
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
        
        self.__microvoltamperes = None
        
        self.__millivoltamperes = None
        
        self.__kilovoltamperes = None
        
        self.__megavoltamperes = None
        
        self.__gigavoltamperes = None
        

    def __convert_from_base(self, from_unit: ApparentPowerUnits) -> float:
        value = self.__value
        
        if from_unit == ApparentPowerUnits.Voltampere:
            return (value)
        
        if from_unit == ApparentPowerUnits.Microvoltampere:
            return ((value) / 1e-06)
        
        if from_unit == ApparentPowerUnits.Millivoltampere:
            return ((value) / 0.001)
        
        if from_unit == ApparentPowerUnits.Kilovoltampere:
            return ((value) / 1000.0)
        
        if from_unit == ApparentPowerUnits.Megavoltampere:
            return ((value) / 1000000.0)
        
        if from_unit == ApparentPowerUnits.Gigavoltampere:
            return ((value) / 1000000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: ApparentPowerUnits) -> float:
        
        if to_unit == ApparentPowerUnits.Voltampere:
            return (value)
        
        if to_unit == ApparentPowerUnits.Microvoltampere:
            return ((value) * 1e-06)
        
        if to_unit == ApparentPowerUnits.Millivoltampere:
            return ((value) * 0.001)
        
        if to_unit == ApparentPowerUnits.Kilovoltampere:
            return ((value) * 1000.0)
        
        if to_unit == ApparentPowerUnits.Megavoltampere:
            return ((value) * 1000000.0)
        
        if to_unit == ApparentPowerUnits.Gigavoltampere:
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
    def from_microvoltamperes(microvoltamperes: float):
        """
        Create a new instance of ApparentPower from a value in microvoltamperes.

        

        :param meters: The ApparentPower value in microvoltamperes.
        :type microvoltamperes: float
        :return: A new instance of ApparentPower.
        :rtype: ApparentPower
        """
        return ApparentPower(microvoltamperes, ApparentPowerUnits.Microvoltampere)

    
    @staticmethod
    def from_millivoltamperes(millivoltamperes: float):
        """
        Create a new instance of ApparentPower from a value in millivoltamperes.

        

        :param meters: The ApparentPower value in millivoltamperes.
        :type millivoltamperes: float
        :return: A new instance of ApparentPower.
        :rtype: ApparentPower
        """
        return ApparentPower(millivoltamperes, ApparentPowerUnits.Millivoltampere)

    
    @staticmethod
    def from_kilovoltamperes(kilovoltamperes: float):
        """
        Create a new instance of ApparentPower from a value in kilovoltamperes.

        

        :param meters: The ApparentPower value in kilovoltamperes.
        :type kilovoltamperes: float
        :return: A new instance of ApparentPower.
        :rtype: ApparentPower
        """
        return ApparentPower(kilovoltamperes, ApparentPowerUnits.Kilovoltampere)

    
    @staticmethod
    def from_megavoltamperes(megavoltamperes: float):
        """
        Create a new instance of ApparentPower from a value in megavoltamperes.

        

        :param meters: The ApparentPower value in megavoltamperes.
        :type megavoltamperes: float
        :return: A new instance of ApparentPower.
        :rtype: ApparentPower
        """
        return ApparentPower(megavoltamperes, ApparentPowerUnits.Megavoltampere)

    
    @staticmethod
    def from_gigavoltamperes(gigavoltamperes: float):
        """
        Create a new instance of ApparentPower from a value in gigavoltamperes.

        

        :param meters: The ApparentPower value in gigavoltamperes.
        :type gigavoltamperes: float
        :return: A new instance of ApparentPower.
        :rtype: ApparentPower
        """
        return ApparentPower(gigavoltamperes, ApparentPowerUnits.Gigavoltampere)

    
    @property
    def voltamperes(self) -> float:
        """
        
        """
        if self.__voltamperes != None:
            return self.__voltamperes
        self.__voltamperes = self.__convert_from_base(ApparentPowerUnits.Voltampere)
        return self.__voltamperes

    
    @property
    def microvoltamperes(self) -> float:
        """
        
        """
        if self.__microvoltamperes != None:
            return self.__microvoltamperes
        self.__microvoltamperes = self.__convert_from_base(ApparentPowerUnits.Microvoltampere)
        return self.__microvoltamperes

    
    @property
    def millivoltamperes(self) -> float:
        """
        
        """
        if self.__millivoltamperes != None:
            return self.__millivoltamperes
        self.__millivoltamperes = self.__convert_from_base(ApparentPowerUnits.Millivoltampere)
        return self.__millivoltamperes

    
    @property
    def kilovoltamperes(self) -> float:
        """
        
        """
        if self.__kilovoltamperes != None:
            return self.__kilovoltamperes
        self.__kilovoltamperes = self.__convert_from_base(ApparentPowerUnits.Kilovoltampere)
        return self.__kilovoltamperes

    
    @property
    def megavoltamperes(self) -> float:
        """
        
        """
        if self.__megavoltamperes != None:
            return self.__megavoltamperes
        self.__megavoltamperes = self.__convert_from_base(ApparentPowerUnits.Megavoltampere)
        return self.__megavoltamperes

    
    @property
    def gigavoltamperes(self) -> float:
        """
        
        """
        if self.__gigavoltamperes != None:
            return self.__gigavoltamperes
        self.__gigavoltamperes = self.__convert_from_base(ApparentPowerUnits.Gigavoltampere)
        return self.__gigavoltamperes

    
    def to_string(self, unit: ApparentPowerUnits = ApparentPowerUnits.Voltampere) -> string:
        """
        Format the ApparentPower to string.
        Note! the default format for ApparentPower is Voltampere.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == ApparentPowerUnits.Voltampere:
            return f"""{self.voltamperes} VA"""
        
        if unit == ApparentPowerUnits.Microvoltampere:
            return f"""{self.microvoltamperes} """
        
        if unit == ApparentPowerUnits.Millivoltampere:
            return f"""{self.millivoltamperes} """
        
        if unit == ApparentPowerUnits.Kilovoltampere:
            return f"""{self.kilovoltamperes} """
        
        if unit == ApparentPowerUnits.Megavoltampere:
            return f"""{self.megavoltamperes} """
        
        if unit == ApparentPowerUnits.Gigavoltampere:
            return f"""{self.gigavoltamperes} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: ApparentPowerUnits = ApparentPowerUnits.Voltampere) -> string:
        """
        Get ApparentPower unit abbreviation.
        Note! the default abbreviation for ApparentPower is Voltampere.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == ApparentPowerUnits.Voltampere:
            return """VA"""
        
        if unit_abbreviation == ApparentPowerUnits.Microvoltampere:
            return """"""
        
        if unit_abbreviation == ApparentPowerUnits.Millivoltampere:
            return """"""
        
        if unit_abbreviation == ApparentPowerUnits.Kilovoltampere:
            return """"""
        
        if unit_abbreviation == ApparentPowerUnits.Megavoltampere:
            return """"""
        
        if unit_abbreviation == ApparentPowerUnits.Gigavoltampere:
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
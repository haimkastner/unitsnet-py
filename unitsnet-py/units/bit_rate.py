from enum import Enum
import math
import string


class BitRateUnits(Enum):
        """
            BitRateUnits enumeration
        """
        
        BitPerSecond = 'bit_per_second'
        """
            
        """
        
        BytePerSecond = 'byte_per_second'
        """
            
        """
        
        KilobitPerSecond = 'kilobit_per_second'
        """
            
        """
        
        MegabitPerSecond = 'megabit_per_second'
        """
            
        """
        
        GigabitPerSecond = 'gigabit_per_second'
        """
            
        """
        
        TerabitPerSecond = 'terabit_per_second'
        """
            
        """
        
        PetabitPerSecond = 'petabit_per_second'
        """
            
        """
        
        ExabitPerSecond = 'exabit_per_second'
        """
            
        """
        
        KilobytePerSecond = 'kilobyte_per_second'
        """
            
        """
        
        MegabytePerSecond = 'megabyte_per_second'
        """
            
        """
        
        GigabytePerSecond = 'gigabyte_per_second'
        """
            
        """
        
        TerabytePerSecond = 'terabyte_per_second'
        """
            
        """
        
        PetabytePerSecond = 'petabyte_per_second'
        """
            
        """
        
        ExabytePerSecond = 'exabyte_per_second'
        """
            
        """
        

class BitRate:
    """
    In telecommunications and computing, bit rate is the number of bits that are conveyed or processed per unit of time.

    Args:
        value (float): The value.
        from_unit (BitRateUnits): The BitRate unit to create from, The default unit is BitPerSecond
    """
    def __init__(self, value: float, from_unit: BitRateUnits = BitRateUnits.BitPerSecond):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__bits_per_second = None
        
        self.__bytes_per_second = None
        
        self.__kilobits_per_second = None
        
        self.__megabits_per_second = None
        
        self.__gigabits_per_second = None
        
        self.__terabits_per_second = None
        
        self.__petabits_per_second = None
        
        self.__exabits_per_second = None
        
        self.__kilobytes_per_second = None
        
        self.__megabytes_per_second = None
        
        self.__gigabytes_per_second = None
        
        self.__terabytes_per_second = None
        
        self.__petabytes_per_second = None
        
        self.__exabytes_per_second = None
        

    def __convert_from_base(self, from_unit: BitRateUnits) -> float:
        value = self.__value
        
        if from_unit == BitRateUnits.BitPerSecond:
            return (value)
        
        if from_unit == BitRateUnits.BytePerSecond:
            return (value / 8)
        
        if from_unit == BitRateUnits.KilobitPerSecond:
            return ((value) / 1000.0)
        
        if from_unit == BitRateUnits.MegabitPerSecond:
            return ((value) / 1000000.0)
        
        if from_unit == BitRateUnits.GigabitPerSecond:
            return ((value) / 1000000000.0)
        
        if from_unit == BitRateUnits.TerabitPerSecond:
            return ((value) / 1000000000000.0)
        
        if from_unit == BitRateUnits.PetabitPerSecond:
            return ((value) / 1000000000000000.0)
        
        if from_unit == BitRateUnits.ExabitPerSecond:
            return ((value) / 1e+18)
        
        if from_unit == BitRateUnits.KilobytePerSecond:
            return ((value / 8) / 1000.0)
        
        if from_unit == BitRateUnits.MegabytePerSecond:
            return ((value / 8) / 1000000.0)
        
        if from_unit == BitRateUnits.GigabytePerSecond:
            return ((value / 8) / 1000000000.0)
        
        if from_unit == BitRateUnits.TerabytePerSecond:
            return ((value / 8) / 1000000000000.0)
        
        if from_unit == BitRateUnits.PetabytePerSecond:
            return ((value / 8) / 1000000000000000.0)
        
        if from_unit == BitRateUnits.ExabytePerSecond:
            return ((value / 8) / 1e+18)
        
        return None


    def __convert_to_base(self, value: float, to_unit: BitRateUnits) -> float:
        
        if to_unit == BitRateUnits.BitPerSecond:
            return (value)
        
        if to_unit == BitRateUnits.BytePerSecond:
            return (value * 8)
        
        if to_unit == BitRateUnits.KilobitPerSecond:
            return ((value) * 1000.0)
        
        if to_unit == BitRateUnits.MegabitPerSecond:
            return ((value) * 1000000.0)
        
        if to_unit == BitRateUnits.GigabitPerSecond:
            return ((value) * 1000000000.0)
        
        if to_unit == BitRateUnits.TerabitPerSecond:
            return ((value) * 1000000000000.0)
        
        if to_unit == BitRateUnits.PetabitPerSecond:
            return ((value) * 1000000000000000.0)
        
        if to_unit == BitRateUnits.ExabitPerSecond:
            return ((value) * 1e+18)
        
        if to_unit == BitRateUnits.KilobytePerSecond:
            return ((value * 8) * 1000.0)
        
        if to_unit == BitRateUnits.MegabytePerSecond:
            return ((value * 8) * 1000000.0)
        
        if to_unit == BitRateUnits.GigabytePerSecond:
            return ((value * 8) * 1000000000.0)
        
        if to_unit == BitRateUnits.TerabytePerSecond:
            return ((value * 8) * 1000000000000.0)
        
        if to_unit == BitRateUnits.PetabytePerSecond:
            return ((value * 8) * 1000000000000000.0)
        
        if to_unit == BitRateUnits.ExabytePerSecond:
            return ((value * 8) * 1e+18)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
    @staticmethod
    def from_bits_per_second(bits_per_second: float):
        """
        Create a new instance of BitRate from a value in bits_per_second.

        

        :param meters: The BitRate value in bits_per_second.
        :type bits_per_second: float
        :return: A new instance of BitRate.
        :rtype: BitRate
        """
        return BitRate(bits_per_second, BitRateUnits.BitPerSecond)

    
    @staticmethod
    def from_bytes_per_second(bytes_per_second: float):
        """
        Create a new instance of BitRate from a value in bytes_per_second.

        

        :param meters: The BitRate value in bytes_per_second.
        :type bytes_per_second: float
        :return: A new instance of BitRate.
        :rtype: BitRate
        """
        return BitRate(bytes_per_second, BitRateUnits.BytePerSecond)

    
    @staticmethod
    def from_kilobits_per_second(kilobits_per_second: float):
        """
        Create a new instance of BitRate from a value in kilobits_per_second.

        

        :param meters: The BitRate value in kilobits_per_second.
        :type kilobits_per_second: float
        :return: A new instance of BitRate.
        :rtype: BitRate
        """
        return BitRate(kilobits_per_second, BitRateUnits.KilobitPerSecond)

    
    @staticmethod
    def from_megabits_per_second(megabits_per_second: float):
        """
        Create a new instance of BitRate from a value in megabits_per_second.

        

        :param meters: The BitRate value in megabits_per_second.
        :type megabits_per_second: float
        :return: A new instance of BitRate.
        :rtype: BitRate
        """
        return BitRate(megabits_per_second, BitRateUnits.MegabitPerSecond)

    
    @staticmethod
    def from_gigabits_per_second(gigabits_per_second: float):
        """
        Create a new instance of BitRate from a value in gigabits_per_second.

        

        :param meters: The BitRate value in gigabits_per_second.
        :type gigabits_per_second: float
        :return: A new instance of BitRate.
        :rtype: BitRate
        """
        return BitRate(gigabits_per_second, BitRateUnits.GigabitPerSecond)

    
    @staticmethod
    def from_terabits_per_second(terabits_per_second: float):
        """
        Create a new instance of BitRate from a value in terabits_per_second.

        

        :param meters: The BitRate value in terabits_per_second.
        :type terabits_per_second: float
        :return: A new instance of BitRate.
        :rtype: BitRate
        """
        return BitRate(terabits_per_second, BitRateUnits.TerabitPerSecond)

    
    @staticmethod
    def from_petabits_per_second(petabits_per_second: float):
        """
        Create a new instance of BitRate from a value in petabits_per_second.

        

        :param meters: The BitRate value in petabits_per_second.
        :type petabits_per_second: float
        :return: A new instance of BitRate.
        :rtype: BitRate
        """
        return BitRate(petabits_per_second, BitRateUnits.PetabitPerSecond)

    
    @staticmethod
    def from_exabits_per_second(exabits_per_second: float):
        """
        Create a new instance of BitRate from a value in exabits_per_second.

        

        :param meters: The BitRate value in exabits_per_second.
        :type exabits_per_second: float
        :return: A new instance of BitRate.
        :rtype: BitRate
        """
        return BitRate(exabits_per_second, BitRateUnits.ExabitPerSecond)

    
    @staticmethod
    def from_kilobytes_per_second(kilobytes_per_second: float):
        """
        Create a new instance of BitRate from a value in kilobytes_per_second.

        

        :param meters: The BitRate value in kilobytes_per_second.
        :type kilobytes_per_second: float
        :return: A new instance of BitRate.
        :rtype: BitRate
        """
        return BitRate(kilobytes_per_second, BitRateUnits.KilobytePerSecond)

    
    @staticmethod
    def from_megabytes_per_second(megabytes_per_second: float):
        """
        Create a new instance of BitRate from a value in megabytes_per_second.

        

        :param meters: The BitRate value in megabytes_per_second.
        :type megabytes_per_second: float
        :return: A new instance of BitRate.
        :rtype: BitRate
        """
        return BitRate(megabytes_per_second, BitRateUnits.MegabytePerSecond)

    
    @staticmethod
    def from_gigabytes_per_second(gigabytes_per_second: float):
        """
        Create a new instance of BitRate from a value in gigabytes_per_second.

        

        :param meters: The BitRate value in gigabytes_per_second.
        :type gigabytes_per_second: float
        :return: A new instance of BitRate.
        :rtype: BitRate
        """
        return BitRate(gigabytes_per_second, BitRateUnits.GigabytePerSecond)

    
    @staticmethod
    def from_terabytes_per_second(terabytes_per_second: float):
        """
        Create a new instance of BitRate from a value in terabytes_per_second.

        

        :param meters: The BitRate value in terabytes_per_second.
        :type terabytes_per_second: float
        :return: A new instance of BitRate.
        :rtype: BitRate
        """
        return BitRate(terabytes_per_second, BitRateUnits.TerabytePerSecond)

    
    @staticmethod
    def from_petabytes_per_second(petabytes_per_second: float):
        """
        Create a new instance of BitRate from a value in petabytes_per_second.

        

        :param meters: The BitRate value in petabytes_per_second.
        :type petabytes_per_second: float
        :return: A new instance of BitRate.
        :rtype: BitRate
        """
        return BitRate(petabytes_per_second, BitRateUnits.PetabytePerSecond)

    
    @staticmethod
    def from_exabytes_per_second(exabytes_per_second: float):
        """
        Create a new instance of BitRate from a value in exabytes_per_second.

        

        :param meters: The BitRate value in exabytes_per_second.
        :type exabytes_per_second: float
        :return: A new instance of BitRate.
        :rtype: BitRate
        """
        return BitRate(exabytes_per_second, BitRateUnits.ExabytePerSecond)

    
    @property
    def bits_per_second(self) -> float:
        """
        
        """
        if self.__bits_per_second != None:
            return self.__bits_per_second
        self.__bits_per_second = self.__convert_from_base(BitRateUnits.BitPerSecond)
        return self.__bits_per_second

    
    @property
    def bytes_per_second(self) -> float:
        """
        
        """
        if self.__bytes_per_second != None:
            return self.__bytes_per_second
        self.__bytes_per_second = self.__convert_from_base(BitRateUnits.BytePerSecond)
        return self.__bytes_per_second

    
    @property
    def kilobits_per_second(self) -> float:
        """
        
        """
        if self.__kilobits_per_second != None:
            return self.__kilobits_per_second
        self.__kilobits_per_second = self.__convert_from_base(BitRateUnits.KilobitPerSecond)
        return self.__kilobits_per_second

    
    @property
    def megabits_per_second(self) -> float:
        """
        
        """
        if self.__megabits_per_second != None:
            return self.__megabits_per_second
        self.__megabits_per_second = self.__convert_from_base(BitRateUnits.MegabitPerSecond)
        return self.__megabits_per_second

    
    @property
    def gigabits_per_second(self) -> float:
        """
        
        """
        if self.__gigabits_per_second != None:
            return self.__gigabits_per_second
        self.__gigabits_per_second = self.__convert_from_base(BitRateUnits.GigabitPerSecond)
        return self.__gigabits_per_second

    
    @property
    def terabits_per_second(self) -> float:
        """
        
        """
        if self.__terabits_per_second != None:
            return self.__terabits_per_second
        self.__terabits_per_second = self.__convert_from_base(BitRateUnits.TerabitPerSecond)
        return self.__terabits_per_second

    
    @property
    def petabits_per_second(self) -> float:
        """
        
        """
        if self.__petabits_per_second != None:
            return self.__petabits_per_second
        self.__petabits_per_second = self.__convert_from_base(BitRateUnits.PetabitPerSecond)
        return self.__petabits_per_second

    
    @property
    def exabits_per_second(self) -> float:
        """
        
        """
        if self.__exabits_per_second != None:
            return self.__exabits_per_second
        self.__exabits_per_second = self.__convert_from_base(BitRateUnits.ExabitPerSecond)
        return self.__exabits_per_second

    
    @property
    def kilobytes_per_second(self) -> float:
        """
        
        """
        if self.__kilobytes_per_second != None:
            return self.__kilobytes_per_second
        self.__kilobytes_per_second = self.__convert_from_base(BitRateUnits.KilobytePerSecond)
        return self.__kilobytes_per_second

    
    @property
    def megabytes_per_second(self) -> float:
        """
        
        """
        if self.__megabytes_per_second != None:
            return self.__megabytes_per_second
        self.__megabytes_per_second = self.__convert_from_base(BitRateUnits.MegabytePerSecond)
        return self.__megabytes_per_second

    
    @property
    def gigabytes_per_second(self) -> float:
        """
        
        """
        if self.__gigabytes_per_second != None:
            return self.__gigabytes_per_second
        self.__gigabytes_per_second = self.__convert_from_base(BitRateUnits.GigabytePerSecond)
        return self.__gigabytes_per_second

    
    @property
    def terabytes_per_second(self) -> float:
        """
        
        """
        if self.__terabytes_per_second != None:
            return self.__terabytes_per_second
        self.__terabytes_per_second = self.__convert_from_base(BitRateUnits.TerabytePerSecond)
        return self.__terabytes_per_second

    
    @property
    def petabytes_per_second(self) -> float:
        """
        
        """
        if self.__petabytes_per_second != None:
            return self.__petabytes_per_second
        self.__petabytes_per_second = self.__convert_from_base(BitRateUnits.PetabytePerSecond)
        return self.__petabytes_per_second

    
    @property
    def exabytes_per_second(self) -> float:
        """
        
        """
        if self.__exabytes_per_second != None:
            return self.__exabytes_per_second
        self.__exabytes_per_second = self.__convert_from_base(BitRateUnits.ExabytePerSecond)
        return self.__exabytes_per_second

    
    def to_string(self, unit: BitRateUnits = BitRateUnits.BitPerSecond) -> string:
        """
        Format the BitRate to string.
        Note! the default format for BitRate is BitPerSecond.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == BitRateUnits.BitPerSecond:
            return f"""{self.bits_per_second} bit/s"""
        
        if unit == BitRateUnits.BytePerSecond:
            return f"""{self.bytes_per_second} B/s"""
        
        if unit == BitRateUnits.KilobitPerSecond:
            return f"""{self.kilobits_per_second} """
        
        if unit == BitRateUnits.MegabitPerSecond:
            return f"""{self.megabits_per_second} """
        
        if unit == BitRateUnits.GigabitPerSecond:
            return f"""{self.gigabits_per_second} """
        
        if unit == BitRateUnits.TerabitPerSecond:
            return f"""{self.terabits_per_second} """
        
        if unit == BitRateUnits.PetabitPerSecond:
            return f"""{self.petabits_per_second} """
        
        if unit == BitRateUnits.ExabitPerSecond:
            return f"""{self.exabits_per_second} """
        
        if unit == BitRateUnits.KilobytePerSecond:
            return f"""{self.kilobytes_per_second} """
        
        if unit == BitRateUnits.MegabytePerSecond:
            return f"""{self.megabytes_per_second} """
        
        if unit == BitRateUnits.GigabytePerSecond:
            return f"""{self.gigabytes_per_second} """
        
        if unit == BitRateUnits.TerabytePerSecond:
            return f"""{self.terabytes_per_second} """
        
        if unit == BitRateUnits.PetabytePerSecond:
            return f"""{self.petabytes_per_second} """
        
        if unit == BitRateUnits.ExabytePerSecond:
            return f"""{self.exabytes_per_second} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: BitRateUnits = BitRateUnits.BitPerSecond) -> string:
        """
        Get BitRate unit abbreviation.
        Note! the default abbreviation for BitRate is BitPerSecond.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == BitRateUnits.BitPerSecond:
            return """bit/s"""
        
        if unit_abbreviation == BitRateUnits.BytePerSecond:
            return """B/s"""
        
        if unit_abbreviation == BitRateUnits.KilobitPerSecond:
            return """"""
        
        if unit_abbreviation == BitRateUnits.MegabitPerSecond:
            return """"""
        
        if unit_abbreviation == BitRateUnits.GigabitPerSecond:
            return """"""
        
        if unit_abbreviation == BitRateUnits.TerabitPerSecond:
            return """"""
        
        if unit_abbreviation == BitRateUnits.PetabitPerSecond:
            return """"""
        
        if unit_abbreviation == BitRateUnits.ExabitPerSecond:
            return """"""
        
        if unit_abbreviation == BitRateUnits.KilobytePerSecond:
            return """"""
        
        if unit_abbreviation == BitRateUnits.MegabytePerSecond:
            return """"""
        
        if unit_abbreviation == BitRateUnits.GigabytePerSecond:
            return """"""
        
        if unit_abbreviation == BitRateUnits.TerabytePerSecond:
            return """"""
        
        if unit_abbreviation == BitRateUnits.PetabytePerSecond:
            return """"""
        
        if unit_abbreviation == BitRateUnits.ExabytePerSecond:
            return """"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, BitRate):
            raise TypeError("unsupported operand type(s) for +: 'BitRate' and '{}'".format(type(other).__name__))
        return BitRate(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, BitRate):
            raise TypeError("unsupported operand type(s) for *: 'BitRate' and '{}'".format(type(other).__name__))
        return BitRate(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, BitRate):
            raise TypeError("unsupported operand type(s) for -: 'BitRate' and '{}'".format(type(other).__name__))
        return BitRate(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, BitRate):
            raise TypeError("unsupported operand type(s) for /: 'BitRate' and '{}'".format(type(other).__name__))
        return BitRate(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, BitRate):
            raise TypeError("unsupported operand type(s) for %: 'BitRate' and '{}'".format(type(other).__name__))
        return BitRate(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, BitRate):
            raise TypeError("unsupported operand type(s) for **: 'BitRate' and '{}'".format(type(other).__name__))
        return BitRate(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, BitRate):
            raise TypeError("unsupported operand type(s) for ==: 'BitRate' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, BitRate):
            raise TypeError("unsupported operand type(s) for <: 'BitRate' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, BitRate):
            raise TypeError("unsupported operand type(s) for >: 'BitRate' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, BitRate):
            raise TypeError("unsupported operand type(s) for <=: 'BitRate' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, BitRate):
            raise TypeError("unsupported operand type(s) for >=: 'BitRate' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value
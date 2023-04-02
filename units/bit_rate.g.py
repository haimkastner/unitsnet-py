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
        
        KiloBitPerSecond = 'kilo_bit_per_second'
        """
            
        """
        
        MegaBitPerSecond = 'mega_bit_per_second'
        """
            
        """
        
        GigaBitPerSecond = 'giga_bit_per_second'
        """
            
        """
        
        TeraBitPerSecond = 'tera_bit_per_second'
        """
            
        """
        
        PetaBitPerSecond = 'peta_bit_per_second'
        """
            
        """
        
        ExaBitPerSecond = 'exa_bit_per_second'
        """
            
        """
        
        KiloBytePerSecond = 'kilo_byte_per_second'
        """
            
        """
        
        MegaBytePerSecond = 'mega_byte_per_second'
        """
            
        """
        
        GigaBytePerSecond = 'giga_byte_per_second'
        """
            
        """
        
        TeraBytePerSecond = 'tera_byte_per_second'
        """
            
        """
        
        PetaBytePerSecond = 'peta_byte_per_second'
        """
            
        """
        
        ExaBytePerSecond = 'exa_byte_per_second'
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
        
        self.__kilo_bits_per_second = None
        
        self.__mega_bits_per_second = None
        
        self.__giga_bits_per_second = None
        
        self.__tera_bits_per_second = None
        
        self.__peta_bits_per_second = None
        
        self.__exa_bits_per_second = None
        
        self.__kilo_bytes_per_second = None
        
        self.__mega_bytes_per_second = None
        
        self.__giga_bytes_per_second = None
        
        self.__tera_bytes_per_second = None
        
        self.__peta_bytes_per_second = None
        
        self.__exa_bytes_per_second = None
        

    def __convert_from_base(self, from_unit: BitRateUnits) -> float:
        value = self.__value
        
        if from_unit == BitRateUnits.BitPerSecond:
            return (value)
        
        if from_unit == BitRateUnits.BytePerSecond:
            return (value / 8)
        
        if from_unit == BitRateUnits.KiloBitPerSecond:
            return ((value) / 1000.0)
        
        if from_unit == BitRateUnits.MegaBitPerSecond:
            return ((value) / 1000000.0)
        
        if from_unit == BitRateUnits.GigaBitPerSecond:
            return ((value) / 1000000000.0)
        
        if from_unit == BitRateUnits.TeraBitPerSecond:
            return ((value) / 1000000000000.0)
        
        if from_unit == BitRateUnits.PetaBitPerSecond:
            return ((value) / 1000000000000000.0)
        
        if from_unit == BitRateUnits.ExaBitPerSecond:
            return ((value) / 1e+18)
        
        if from_unit == BitRateUnits.KiloBytePerSecond:
            return ((value / 8) / 1000.0)
        
        if from_unit == BitRateUnits.MegaBytePerSecond:
            return ((value / 8) / 1000000.0)
        
        if from_unit == BitRateUnits.GigaBytePerSecond:
            return ((value / 8) / 1000000000.0)
        
        if from_unit == BitRateUnits.TeraBytePerSecond:
            return ((value / 8) / 1000000000000.0)
        
        if from_unit == BitRateUnits.PetaBytePerSecond:
            return ((value / 8) / 1000000000000000.0)
        
        if from_unit == BitRateUnits.ExaBytePerSecond:
            return ((value / 8) / 1e+18)
        
        return None


    def __convert_to_base(self, value: float, to_unit: BitRateUnits) -> float:
        
        if to_unit == BitRateUnits.BitPerSecond:
            return (value)
        
        if to_unit == BitRateUnits.BytePerSecond:
            return (value * 8)
        
        if to_unit == BitRateUnits.KiloBitPerSecond:
            return ((value) * 1000.0)
        
        if to_unit == BitRateUnits.MegaBitPerSecond:
            return ((value) * 1000000.0)
        
        if to_unit == BitRateUnits.GigaBitPerSecond:
            return ((value) * 1000000000.0)
        
        if to_unit == BitRateUnits.TeraBitPerSecond:
            return ((value) * 1000000000000.0)
        
        if to_unit == BitRateUnits.PetaBitPerSecond:
            return ((value) * 1000000000000000.0)
        
        if to_unit == BitRateUnits.ExaBitPerSecond:
            return ((value) * 1e+18)
        
        if to_unit == BitRateUnits.KiloBytePerSecond:
            return ((value * 8) * 1000.0)
        
        if to_unit == BitRateUnits.MegaBytePerSecond:
            return ((value * 8) * 1000000.0)
        
        if to_unit == BitRateUnits.GigaBytePerSecond:
            return ((value * 8) * 1000000000.0)
        
        if to_unit == BitRateUnits.TeraBytePerSecond:
            return ((value * 8) * 1000000000000.0)
        
        if to_unit == BitRateUnits.PetaBytePerSecond:
            return ((value * 8) * 1000000000000000.0)
        
        if to_unit == BitRateUnits.ExaBytePerSecond:
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
    def from_kilo_bits_per_second(kilo_bits_per_second: float):
        """
        Create a new instance of BitRate from a value in kilo_bits_per_second.

        

        :param meters: The BitRate value in kilo_bits_per_second.
        :type kilo_bits_per_second: float
        :return: A new instance of BitRate.
        :rtype: BitRate
        """
        return BitRate(kilo_bits_per_second, BitRateUnits.KiloBitPerSecond)

    
    @staticmethod
    def from_mega_bits_per_second(mega_bits_per_second: float):
        """
        Create a new instance of BitRate from a value in mega_bits_per_second.

        

        :param meters: The BitRate value in mega_bits_per_second.
        :type mega_bits_per_second: float
        :return: A new instance of BitRate.
        :rtype: BitRate
        """
        return BitRate(mega_bits_per_second, BitRateUnits.MegaBitPerSecond)

    
    @staticmethod
    def from_giga_bits_per_second(giga_bits_per_second: float):
        """
        Create a new instance of BitRate from a value in giga_bits_per_second.

        

        :param meters: The BitRate value in giga_bits_per_second.
        :type giga_bits_per_second: float
        :return: A new instance of BitRate.
        :rtype: BitRate
        """
        return BitRate(giga_bits_per_second, BitRateUnits.GigaBitPerSecond)

    
    @staticmethod
    def from_tera_bits_per_second(tera_bits_per_second: float):
        """
        Create a new instance of BitRate from a value in tera_bits_per_second.

        

        :param meters: The BitRate value in tera_bits_per_second.
        :type tera_bits_per_second: float
        :return: A new instance of BitRate.
        :rtype: BitRate
        """
        return BitRate(tera_bits_per_second, BitRateUnits.TeraBitPerSecond)

    
    @staticmethod
    def from_peta_bits_per_second(peta_bits_per_second: float):
        """
        Create a new instance of BitRate from a value in peta_bits_per_second.

        

        :param meters: The BitRate value in peta_bits_per_second.
        :type peta_bits_per_second: float
        :return: A new instance of BitRate.
        :rtype: BitRate
        """
        return BitRate(peta_bits_per_second, BitRateUnits.PetaBitPerSecond)

    
    @staticmethod
    def from_exa_bits_per_second(exa_bits_per_second: float):
        """
        Create a new instance of BitRate from a value in exa_bits_per_second.

        

        :param meters: The BitRate value in exa_bits_per_second.
        :type exa_bits_per_second: float
        :return: A new instance of BitRate.
        :rtype: BitRate
        """
        return BitRate(exa_bits_per_second, BitRateUnits.ExaBitPerSecond)

    
    @staticmethod
    def from_kilo_bytes_per_second(kilo_bytes_per_second: float):
        """
        Create a new instance of BitRate from a value in kilo_bytes_per_second.

        

        :param meters: The BitRate value in kilo_bytes_per_second.
        :type kilo_bytes_per_second: float
        :return: A new instance of BitRate.
        :rtype: BitRate
        """
        return BitRate(kilo_bytes_per_second, BitRateUnits.KiloBytePerSecond)

    
    @staticmethod
    def from_mega_bytes_per_second(mega_bytes_per_second: float):
        """
        Create a new instance of BitRate from a value in mega_bytes_per_second.

        

        :param meters: The BitRate value in mega_bytes_per_second.
        :type mega_bytes_per_second: float
        :return: A new instance of BitRate.
        :rtype: BitRate
        """
        return BitRate(mega_bytes_per_second, BitRateUnits.MegaBytePerSecond)

    
    @staticmethod
    def from_giga_bytes_per_second(giga_bytes_per_second: float):
        """
        Create a new instance of BitRate from a value in giga_bytes_per_second.

        

        :param meters: The BitRate value in giga_bytes_per_second.
        :type giga_bytes_per_second: float
        :return: A new instance of BitRate.
        :rtype: BitRate
        """
        return BitRate(giga_bytes_per_second, BitRateUnits.GigaBytePerSecond)

    
    @staticmethod
    def from_tera_bytes_per_second(tera_bytes_per_second: float):
        """
        Create a new instance of BitRate from a value in tera_bytes_per_second.

        

        :param meters: The BitRate value in tera_bytes_per_second.
        :type tera_bytes_per_second: float
        :return: A new instance of BitRate.
        :rtype: BitRate
        """
        return BitRate(tera_bytes_per_second, BitRateUnits.TeraBytePerSecond)

    
    @staticmethod
    def from_peta_bytes_per_second(peta_bytes_per_second: float):
        """
        Create a new instance of BitRate from a value in peta_bytes_per_second.

        

        :param meters: The BitRate value in peta_bytes_per_second.
        :type peta_bytes_per_second: float
        :return: A new instance of BitRate.
        :rtype: BitRate
        """
        return BitRate(peta_bytes_per_second, BitRateUnits.PetaBytePerSecond)

    
    @staticmethod
    def from_exa_bytes_per_second(exa_bytes_per_second: float):
        """
        Create a new instance of BitRate from a value in exa_bytes_per_second.

        

        :param meters: The BitRate value in exa_bytes_per_second.
        :type exa_bytes_per_second: float
        :return: A new instance of BitRate.
        :rtype: BitRate
        """
        return BitRate(exa_bytes_per_second, BitRateUnits.ExaBytePerSecond)

    
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
    def kilo_bits_per_second(self) -> float:
        """
        
        """
        if self.__kilo_bits_per_second != None:
            return self.__kilo_bits_per_second
        self.__kilo_bits_per_second = self.__convert_from_base(BitRateUnits.KiloBitPerSecond)
        return self.__kilo_bits_per_second

    
    @property
    def mega_bits_per_second(self) -> float:
        """
        
        """
        if self.__mega_bits_per_second != None:
            return self.__mega_bits_per_second
        self.__mega_bits_per_second = self.__convert_from_base(BitRateUnits.MegaBitPerSecond)
        return self.__mega_bits_per_second

    
    @property
    def giga_bits_per_second(self) -> float:
        """
        
        """
        if self.__giga_bits_per_second != None:
            return self.__giga_bits_per_second
        self.__giga_bits_per_second = self.__convert_from_base(BitRateUnits.GigaBitPerSecond)
        return self.__giga_bits_per_second

    
    @property
    def tera_bits_per_second(self) -> float:
        """
        
        """
        if self.__tera_bits_per_second != None:
            return self.__tera_bits_per_second
        self.__tera_bits_per_second = self.__convert_from_base(BitRateUnits.TeraBitPerSecond)
        return self.__tera_bits_per_second

    
    @property
    def peta_bits_per_second(self) -> float:
        """
        
        """
        if self.__peta_bits_per_second != None:
            return self.__peta_bits_per_second
        self.__peta_bits_per_second = self.__convert_from_base(BitRateUnits.PetaBitPerSecond)
        return self.__peta_bits_per_second

    
    @property
    def exa_bits_per_second(self) -> float:
        """
        
        """
        if self.__exa_bits_per_second != None:
            return self.__exa_bits_per_second
        self.__exa_bits_per_second = self.__convert_from_base(BitRateUnits.ExaBitPerSecond)
        return self.__exa_bits_per_second

    
    @property
    def kilo_bytes_per_second(self) -> float:
        """
        
        """
        if self.__kilo_bytes_per_second != None:
            return self.__kilo_bytes_per_second
        self.__kilo_bytes_per_second = self.__convert_from_base(BitRateUnits.KiloBytePerSecond)
        return self.__kilo_bytes_per_second

    
    @property
    def mega_bytes_per_second(self) -> float:
        """
        
        """
        if self.__mega_bytes_per_second != None:
            return self.__mega_bytes_per_second
        self.__mega_bytes_per_second = self.__convert_from_base(BitRateUnits.MegaBytePerSecond)
        return self.__mega_bytes_per_second

    
    @property
    def giga_bytes_per_second(self) -> float:
        """
        
        """
        if self.__giga_bytes_per_second != None:
            return self.__giga_bytes_per_second
        self.__giga_bytes_per_second = self.__convert_from_base(BitRateUnits.GigaBytePerSecond)
        return self.__giga_bytes_per_second

    
    @property
    def tera_bytes_per_second(self) -> float:
        """
        
        """
        if self.__tera_bytes_per_second != None:
            return self.__tera_bytes_per_second
        self.__tera_bytes_per_second = self.__convert_from_base(BitRateUnits.TeraBytePerSecond)
        return self.__tera_bytes_per_second

    
    @property
    def peta_bytes_per_second(self) -> float:
        """
        
        """
        if self.__peta_bytes_per_second != None:
            return self.__peta_bytes_per_second
        self.__peta_bytes_per_second = self.__convert_from_base(BitRateUnits.PetaBytePerSecond)
        return self.__peta_bytes_per_second

    
    @property
    def exa_bytes_per_second(self) -> float:
        """
        
        """
        if self.__exa_bytes_per_second != None:
            return self.__exa_bytes_per_second
        self.__exa_bytes_per_second = self.__convert_from_base(BitRateUnits.ExaBytePerSecond)
        return self.__exa_bytes_per_second

    
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
        
        if unit == BitRateUnits.KiloBitPerSecond:
            return f"""{self.kilo_bits_per_second} """
        
        if unit == BitRateUnits.MegaBitPerSecond:
            return f"""{self.mega_bits_per_second} """
        
        if unit == BitRateUnits.GigaBitPerSecond:
            return f"""{self.giga_bits_per_second} """
        
        if unit == BitRateUnits.TeraBitPerSecond:
            return f"""{self.tera_bits_per_second} """
        
        if unit == BitRateUnits.PetaBitPerSecond:
            return f"""{self.peta_bits_per_second} """
        
        if unit == BitRateUnits.ExaBitPerSecond:
            return f"""{self.exa_bits_per_second} """
        
        if unit == BitRateUnits.KiloBytePerSecond:
            return f"""{self.kilo_bytes_per_second} """
        
        if unit == BitRateUnits.MegaBytePerSecond:
            return f"""{self.mega_bytes_per_second} """
        
        if unit == BitRateUnits.GigaBytePerSecond:
            return f"""{self.giga_bytes_per_second} """
        
        if unit == BitRateUnits.TeraBytePerSecond:
            return f"""{self.tera_bytes_per_second} """
        
        if unit == BitRateUnits.PetaBytePerSecond:
            return f"""{self.peta_bytes_per_second} """
        
        if unit == BitRateUnits.ExaBytePerSecond:
            return f"""{self.exa_bytes_per_second} """
        
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
        
        if unit_abbreviation == BitRateUnits.KiloBitPerSecond:
            return """"""
        
        if unit_abbreviation == BitRateUnits.MegaBitPerSecond:
            return """"""
        
        if unit_abbreviation == BitRateUnits.GigaBitPerSecond:
            return """"""
        
        if unit_abbreviation == BitRateUnits.TeraBitPerSecond:
            return """"""
        
        if unit_abbreviation == BitRateUnits.PetaBitPerSecond:
            return """"""
        
        if unit_abbreviation == BitRateUnits.ExaBitPerSecond:
            return """"""
        
        if unit_abbreviation == BitRateUnits.KiloBytePerSecond:
            return """"""
        
        if unit_abbreviation == BitRateUnits.MegaBytePerSecond:
            return """"""
        
        if unit_abbreviation == BitRateUnits.GigaBytePerSecond:
            return """"""
        
        if unit_abbreviation == BitRateUnits.TeraBytePerSecond:
            return """"""
        
        if unit_abbreviation == BitRateUnits.PetaBytePerSecond:
            return """"""
        
        if unit_abbreviation == BitRateUnits.ExaBytePerSecond:
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
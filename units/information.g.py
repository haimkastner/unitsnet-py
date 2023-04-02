from enum import Enum
import math
import string


class InformationUnits(Enum):
        """
            InformationUnits enumeration
        """
        
        Byte = 'byte'
        """
            
        """
        
        Bit = 'bit'
        """
            
        """
        
        KiloByte = 'kilo_byte'
        """
            
        """
        
        MegaByte = 'mega_byte'
        """
            
        """
        
        GigaByte = 'giga_byte'
        """
            
        """
        
        TeraByte = 'tera_byte'
        """
            
        """
        
        PetaByte = 'peta_byte'
        """
            
        """
        
        ExaByte = 'exa_byte'
        """
            
        """
        
        KiloBit = 'kilo_bit'
        """
            
        """
        
        MegaBit = 'mega_bit'
        """
            
        """
        
        GigaBit = 'giga_bit'
        """
            
        """
        
        TeraBit = 'tera_bit'
        """
            
        """
        
        PetaBit = 'peta_bit'
        """
            
        """
        
        ExaBit = 'exa_bit'
        """
            
        """
        
    
class Information:
    """
    In computing and telecommunications, a unit of information is the capacity of some standard data storage system or communication channel, used to measure the capacities of other systems and channels. In information theory, units of information are also used to measure the information contents or entropy of random variables.

    Args:
        value (float): The value.
        from_unit (InformationUnits): The Information unit to create from, The default unit is Bit
    """
    def __init__(self, value: float, from_unit: InformationUnits = InformationUnits.Bit):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__bytes = None
        
        self.__bits = None
        
        self.__kilo_bytes = None
        
        self.__mega_bytes = None
        
        self.__giga_bytes = None
        
        self.__tera_bytes = None
        
        self.__peta_bytes = None
        
        self.__exa_bytes = None
        
        self.__kilo_bits = None
        
        self.__mega_bits = None
        
        self.__giga_bits = None
        
        self.__tera_bits = None
        
        self.__peta_bits = None
        
        self.__exa_bits = None
        

    def __convert_from_base(self, from_unit: InformationUnits) -> float:
        value = self.__value
        
        if from_unit == InformationUnits.Byte:
            return (value / 8)
        
        if from_unit == InformationUnits.Bit:
            return (value)
        
        if from_unit == InformationUnits.KiloByte:
            return ((value / 8) / 1000.0)
        
        if from_unit == InformationUnits.MegaByte:
            return ((value / 8) / 1000000.0)
        
        if from_unit == InformationUnits.GigaByte:
            return ((value / 8) / 1000000000.0)
        
        if from_unit == InformationUnits.TeraByte:
            return ((value / 8) / 1000000000000.0)
        
        if from_unit == InformationUnits.PetaByte:
            return ((value / 8) / 1000000000000000.0)
        
        if from_unit == InformationUnits.ExaByte:
            return ((value / 8) / 1e+18)
        
        if from_unit == InformationUnits.KiloBit:
            return ((value) / 1000.0)
        
        if from_unit == InformationUnits.MegaBit:
            return ((value) / 1000000.0)
        
        if from_unit == InformationUnits.GigaBit:
            return ((value) / 1000000000.0)
        
        if from_unit == InformationUnits.TeraBit:
            return ((value) / 1000000000000.0)
        
        if from_unit == InformationUnits.PetaBit:
            return ((value) / 1000000000000000.0)
        
        if from_unit == InformationUnits.ExaBit:
            return ((value) / 1e+18)
        
        return None


    def __convert_to_base(self, value: float, to_unit: InformationUnits) -> float:
        
        if to_unit == InformationUnits.Byte:
            return (value * 8)
        
        if to_unit == InformationUnits.Bit:
            return (value)
        
        if to_unit == InformationUnits.KiloByte:
            return ((value * 8) * 1000.0)
        
        if to_unit == InformationUnits.MegaByte:
            return ((value * 8) * 1000000.0)
        
        if to_unit == InformationUnits.GigaByte:
            return ((value * 8) * 1000000000.0)
        
        if to_unit == InformationUnits.TeraByte:
            return ((value * 8) * 1000000000000.0)
        
        if to_unit == InformationUnits.PetaByte:
            return ((value * 8) * 1000000000000000.0)
        
        if to_unit == InformationUnits.ExaByte:
            return ((value * 8) * 1e+18)
        
        if to_unit == InformationUnits.KiloBit:
            return ((value) * 1000.0)
        
        if to_unit == InformationUnits.MegaBit:
            return ((value) * 1000000.0)
        
        if to_unit == InformationUnits.GigaBit:
            return ((value) * 1000000000.0)
        
        if to_unit == InformationUnits.TeraBit:
            return ((value) * 1000000000000.0)
        
        if to_unit == InformationUnits.PetaBit:
            return ((value) * 1000000000000000.0)
        
        if to_unit == InformationUnits.ExaBit:
            return ((value) * 1e+18)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
    @staticmethod
    def from_bytes(bytes: float):
        """
        Create a new instance of Information from a value in bytes.

        

        :param meters: The Information value in bytes.
        :type bytes: float
        :return: A new instance of Information.
        :rtype: Information
        """
        return Information(bytes, InformationUnits.Byte)

    
    @staticmethod
    def from_bits(bits: float):
        """
        Create a new instance of Information from a value in bits.

        

        :param meters: The Information value in bits.
        :type bits: float
        :return: A new instance of Information.
        :rtype: Information
        """
        return Information(bits, InformationUnits.Bit)

    
    @staticmethod
    def from_kilo_bytes(kilo_bytes: float):
        """
        Create a new instance of Information from a value in kilo_bytes.

        

        :param meters: The Information value in kilo_bytes.
        :type kilo_bytes: float
        :return: A new instance of Information.
        :rtype: Information
        """
        return Information(kilo_bytes, InformationUnits.KiloByte)

    
    @staticmethod
    def from_mega_bytes(mega_bytes: float):
        """
        Create a new instance of Information from a value in mega_bytes.

        

        :param meters: The Information value in mega_bytes.
        :type mega_bytes: float
        :return: A new instance of Information.
        :rtype: Information
        """
        return Information(mega_bytes, InformationUnits.MegaByte)

    
    @staticmethod
    def from_giga_bytes(giga_bytes: float):
        """
        Create a new instance of Information from a value in giga_bytes.

        

        :param meters: The Information value in giga_bytes.
        :type giga_bytes: float
        :return: A new instance of Information.
        :rtype: Information
        """
        return Information(giga_bytes, InformationUnits.GigaByte)

    
    @staticmethod
    def from_tera_bytes(tera_bytes: float):
        """
        Create a new instance of Information from a value in tera_bytes.

        

        :param meters: The Information value in tera_bytes.
        :type tera_bytes: float
        :return: A new instance of Information.
        :rtype: Information
        """
        return Information(tera_bytes, InformationUnits.TeraByte)

    
    @staticmethod
    def from_peta_bytes(peta_bytes: float):
        """
        Create a new instance of Information from a value in peta_bytes.

        

        :param meters: The Information value in peta_bytes.
        :type peta_bytes: float
        :return: A new instance of Information.
        :rtype: Information
        """
        return Information(peta_bytes, InformationUnits.PetaByte)

    
    @staticmethod
    def from_exa_bytes(exa_bytes: float):
        """
        Create a new instance of Information from a value in exa_bytes.

        

        :param meters: The Information value in exa_bytes.
        :type exa_bytes: float
        :return: A new instance of Information.
        :rtype: Information
        """
        return Information(exa_bytes, InformationUnits.ExaByte)

    
    @staticmethod
    def from_kilo_bits(kilo_bits: float):
        """
        Create a new instance of Information from a value in kilo_bits.

        

        :param meters: The Information value in kilo_bits.
        :type kilo_bits: float
        :return: A new instance of Information.
        :rtype: Information
        """
        return Information(kilo_bits, InformationUnits.KiloBit)

    
    @staticmethod
    def from_mega_bits(mega_bits: float):
        """
        Create a new instance of Information from a value in mega_bits.

        

        :param meters: The Information value in mega_bits.
        :type mega_bits: float
        :return: A new instance of Information.
        :rtype: Information
        """
        return Information(mega_bits, InformationUnits.MegaBit)

    
    @staticmethod
    def from_giga_bits(giga_bits: float):
        """
        Create a new instance of Information from a value in giga_bits.

        

        :param meters: The Information value in giga_bits.
        :type giga_bits: float
        :return: A new instance of Information.
        :rtype: Information
        """
        return Information(giga_bits, InformationUnits.GigaBit)

    
    @staticmethod
    def from_tera_bits(tera_bits: float):
        """
        Create a new instance of Information from a value in tera_bits.

        

        :param meters: The Information value in tera_bits.
        :type tera_bits: float
        :return: A new instance of Information.
        :rtype: Information
        """
        return Information(tera_bits, InformationUnits.TeraBit)

    
    @staticmethod
    def from_peta_bits(peta_bits: float):
        """
        Create a new instance of Information from a value in peta_bits.

        

        :param meters: The Information value in peta_bits.
        :type peta_bits: float
        :return: A new instance of Information.
        :rtype: Information
        """
        return Information(peta_bits, InformationUnits.PetaBit)

    
    @staticmethod
    def from_exa_bits(exa_bits: float):
        """
        Create a new instance of Information from a value in exa_bits.

        

        :param meters: The Information value in exa_bits.
        :type exa_bits: float
        :return: A new instance of Information.
        :rtype: Information
        """
        return Information(exa_bits, InformationUnits.ExaBit)

    
    @property
    def bytes(self) -> float:
        """
        
        """
        if self.__bytes != None:
            return self.__bytes
        self.__bytes = self.__convert_from_base(InformationUnits.Byte)
        return self.__bytes

    
    @property
    def bits(self) -> float:
        """
        
        """
        if self.__bits != None:
            return self.__bits
        self.__bits = self.__convert_from_base(InformationUnits.Bit)
        return self.__bits

    
    @property
    def kilo_bytes(self) -> float:
        """
        
        """
        if self.__kilo_bytes != None:
            return self.__kilo_bytes
        self.__kilo_bytes = self.__convert_from_base(InformationUnits.KiloByte)
        return self.__kilo_bytes

    
    @property
    def mega_bytes(self) -> float:
        """
        
        """
        if self.__mega_bytes != None:
            return self.__mega_bytes
        self.__mega_bytes = self.__convert_from_base(InformationUnits.MegaByte)
        return self.__mega_bytes

    
    @property
    def giga_bytes(self) -> float:
        """
        
        """
        if self.__giga_bytes != None:
            return self.__giga_bytes
        self.__giga_bytes = self.__convert_from_base(InformationUnits.GigaByte)
        return self.__giga_bytes

    
    @property
    def tera_bytes(self) -> float:
        """
        
        """
        if self.__tera_bytes != None:
            return self.__tera_bytes
        self.__tera_bytes = self.__convert_from_base(InformationUnits.TeraByte)
        return self.__tera_bytes

    
    @property
    def peta_bytes(self) -> float:
        """
        
        """
        if self.__peta_bytes != None:
            return self.__peta_bytes
        self.__peta_bytes = self.__convert_from_base(InformationUnits.PetaByte)
        return self.__peta_bytes

    
    @property
    def exa_bytes(self) -> float:
        """
        
        """
        if self.__exa_bytes != None:
            return self.__exa_bytes
        self.__exa_bytes = self.__convert_from_base(InformationUnits.ExaByte)
        return self.__exa_bytes

    
    @property
    def kilo_bits(self) -> float:
        """
        
        """
        if self.__kilo_bits != None:
            return self.__kilo_bits
        self.__kilo_bits = self.__convert_from_base(InformationUnits.KiloBit)
        return self.__kilo_bits

    
    @property
    def mega_bits(self) -> float:
        """
        
        """
        if self.__mega_bits != None:
            return self.__mega_bits
        self.__mega_bits = self.__convert_from_base(InformationUnits.MegaBit)
        return self.__mega_bits

    
    @property
    def giga_bits(self) -> float:
        """
        
        """
        if self.__giga_bits != None:
            return self.__giga_bits
        self.__giga_bits = self.__convert_from_base(InformationUnits.GigaBit)
        return self.__giga_bits

    
    @property
    def tera_bits(self) -> float:
        """
        
        """
        if self.__tera_bits != None:
            return self.__tera_bits
        self.__tera_bits = self.__convert_from_base(InformationUnits.TeraBit)
        return self.__tera_bits

    
    @property
    def peta_bits(self) -> float:
        """
        
        """
        if self.__peta_bits != None:
            return self.__peta_bits
        self.__peta_bits = self.__convert_from_base(InformationUnits.PetaBit)
        return self.__peta_bits

    
    @property
    def exa_bits(self) -> float:
        """
        
        """
        if self.__exa_bits != None:
            return self.__exa_bits
        self.__exa_bits = self.__convert_from_base(InformationUnits.ExaBit)
        return self.__exa_bits

    
    def to_string(self, unit: InformationUnits = InformationUnits.Bit) -> string:
        """
        Format the Information to string.
        Note! the default format for Information is Bit.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == InformationUnits.Byte:
            return f"""{self.bytes} B"""
        
        if unit == InformationUnits.Bit:
            return f"""{self.bits} b"""
        
        if unit == InformationUnits.KiloByte:
            return f"""{self.kilo_bytes} """
        
        if unit == InformationUnits.MegaByte:
            return f"""{self.mega_bytes} """
        
        if unit == InformationUnits.GigaByte:
            return f"""{self.giga_bytes} """
        
        if unit == InformationUnits.TeraByte:
            return f"""{self.tera_bytes} """
        
        if unit == InformationUnits.PetaByte:
            return f"""{self.peta_bytes} """
        
        if unit == InformationUnits.ExaByte:
            return f"""{self.exa_bytes} """
        
        if unit == InformationUnits.KiloBit:
            return f"""{self.kilo_bits} """
        
        if unit == InformationUnits.MegaBit:
            return f"""{self.mega_bits} """
        
        if unit == InformationUnits.GigaBit:
            return f"""{self.giga_bits} """
        
        if unit == InformationUnits.TeraBit:
            return f"""{self.tera_bits} """
        
        if unit == InformationUnits.PetaBit:
            return f"""{self.peta_bits} """
        
        if unit == InformationUnits.ExaBit:
            return f"""{self.exa_bits} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: InformationUnits = InformationUnits.Bit) -> string:
        """
        Get Information unit abbreviation.
        Note! the default abbreviation for Information is Bit.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == InformationUnits.Byte:
            return """B"""
        
        if unit_abbreviation == InformationUnits.Bit:
            return """b"""
        
        if unit_abbreviation == InformationUnits.KiloByte:
            return """"""
        
        if unit_abbreviation == InformationUnits.MegaByte:
            return """"""
        
        if unit_abbreviation == InformationUnits.GigaByte:
            return """"""
        
        if unit_abbreviation == InformationUnits.TeraByte:
            return """"""
        
        if unit_abbreviation == InformationUnits.PetaByte:
            return """"""
        
        if unit_abbreviation == InformationUnits.ExaByte:
            return """"""
        
        if unit_abbreviation == InformationUnits.KiloBit:
            return """"""
        
        if unit_abbreviation == InformationUnits.MegaBit:
            return """"""
        
        if unit_abbreviation == InformationUnits.GigaBit:
            return """"""
        
        if unit_abbreviation == InformationUnits.TeraBit:
            return """"""
        
        if unit_abbreviation == InformationUnits.PetaBit:
            return """"""
        
        if unit_abbreviation == InformationUnits.ExaBit:
            return """"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, Information):
            raise TypeError("unsupported operand type(s) for +: 'Information' and '{}'".format(type(other).__name__))
        return Information(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, Information):
            raise TypeError("unsupported operand type(s) for *: 'Information' and '{}'".format(type(other).__name__))
        return Information(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, Information):
            raise TypeError("unsupported operand type(s) for -: 'Information' and '{}'".format(type(other).__name__))
        return Information(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, Information):
            raise TypeError("unsupported operand type(s) for /: 'Information' and '{}'".format(type(other).__name__))
        return Information(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, Information):
            raise TypeError("unsupported operand type(s) for %: 'Information' and '{}'".format(type(other).__name__))
        return Information(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, Information):
            raise TypeError("unsupported operand type(s) for **: 'Information' and '{}'".format(type(other).__name__))
        return Information(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, Information):
            raise TypeError("unsupported operand type(s) for ==: 'Information' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, Information):
            raise TypeError("unsupported operand type(s) for <: 'Information' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, Information):
            raise TypeError("unsupported operand type(s) for >: 'Information' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, Information):
            raise TypeError("unsupported operand type(s) for <=: 'Information' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, Information):
            raise TypeError("unsupported operand type(s) for >=: 'Information' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value
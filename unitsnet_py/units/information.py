from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



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
        
        Kilobyte = 'kilobyte'
        """
            
        """
        
        Megabyte = 'megabyte'
        """
            
        """
        
        Gigabyte = 'gigabyte'
        """
            
        """
        
        Terabyte = 'terabyte'
        """
            
        """
        
        Petabyte = 'petabyte'
        """
            
        """
        
        Exabyte = 'exabyte'
        """
            
        """
        
        Kilobit = 'kilobit'
        """
            
        """
        
        Megabit = 'megabit'
        """
            
        """
        
        Gigabit = 'gigabit'
        """
            
        """
        
        Terabit = 'terabit'
        """
            
        """
        
        Petabit = 'petabit'
        """
            
        """
        
        Exabit = 'exabit'
        """
            
        """
        

class Information(AbstractMeasure):
    """
    In computing and telecommunications, a unit of information is the capacity of some standard data storage system or communication channel, used to measure the capacities of other systems and channels. In information theory, units of information are also used to measure the information contents or entropy of random variables.

    Args:
        value (float): The value.
        from_unit (InformationUnits): The Information unit to create from, The default unit is Bit
    """
    def __init__(self, value: float, from_unit: InformationUnits = InformationUnits.Bit):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__bytes = None
        
        self.__bits = None
        
        self.__kilobytes = None
        
        self.__megabytes = None
        
        self.__gigabytes = None
        
        self.__terabytes = None
        
        self.__petabytes = None
        
        self.__exabytes = None
        
        self.__kilobits = None
        
        self.__megabits = None
        
        self.__gigabits = None
        
        self.__terabits = None
        
        self.__petabits = None
        
        self.__exabits = None
        

    def convert(self, unit: InformationUnits) -> float:
        return self.__convert_from_base(unit)

    def __convert_from_base(self, from_unit: InformationUnits) -> float:
        value = self._value
        
        if from_unit == InformationUnits.Byte:
            return (value / 8)
        
        if from_unit == InformationUnits.Bit:
            return (value)
        
        if from_unit == InformationUnits.Kilobyte:
            return ((value / 8) / 1000.0)
        
        if from_unit == InformationUnits.Megabyte:
            return ((value / 8) / 1000000.0)
        
        if from_unit == InformationUnits.Gigabyte:
            return ((value / 8) / 1000000000.0)
        
        if from_unit == InformationUnits.Terabyte:
            return ((value / 8) / 1000000000000.0)
        
        if from_unit == InformationUnits.Petabyte:
            return ((value / 8) / 1000000000000000.0)
        
        if from_unit == InformationUnits.Exabyte:
            return ((value / 8) / 1e+18)
        
        if from_unit == InformationUnits.Kilobit:
            return ((value) / 1000.0)
        
        if from_unit == InformationUnits.Megabit:
            return ((value) / 1000000.0)
        
        if from_unit == InformationUnits.Gigabit:
            return ((value) / 1000000000.0)
        
        if from_unit == InformationUnits.Terabit:
            return ((value) / 1000000000000.0)
        
        if from_unit == InformationUnits.Petabit:
            return ((value) / 1000000000000000.0)
        
        if from_unit == InformationUnits.Exabit:
            return ((value) / 1e+18)
        
        return None


    def __convert_to_base(self, value: float, to_unit: InformationUnits) -> float:
        
        if to_unit == InformationUnits.Byte:
            return (value * 8)
        
        if to_unit == InformationUnits.Bit:
            return (value)
        
        if to_unit == InformationUnits.Kilobyte:
            return ((value * 8) * 1000.0)
        
        if to_unit == InformationUnits.Megabyte:
            return ((value * 8) * 1000000.0)
        
        if to_unit == InformationUnits.Gigabyte:
            return ((value * 8) * 1000000000.0)
        
        if to_unit == InformationUnits.Terabyte:
            return ((value * 8) * 1000000000000.0)
        
        if to_unit == InformationUnits.Petabyte:
            return ((value * 8) * 1000000000000000.0)
        
        if to_unit == InformationUnits.Exabyte:
            return ((value * 8) * 1e+18)
        
        if to_unit == InformationUnits.Kilobit:
            return ((value) * 1000.0)
        
        if to_unit == InformationUnits.Megabit:
            return ((value) * 1000000.0)
        
        if to_unit == InformationUnits.Gigabit:
            return ((value) * 1000000000.0)
        
        if to_unit == InformationUnits.Terabit:
            return ((value) * 1000000000000.0)
        
        if to_unit == InformationUnits.Petabit:
            return ((value) * 1000000000000000.0)
        
        if to_unit == InformationUnits.Exabit:
            return ((value) * 1e+18)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
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
    def from_kilobytes(kilobytes: float):
        """
        Create a new instance of Information from a value in kilobytes.

        

        :param meters: The Information value in kilobytes.
        :type kilobytes: float
        :return: A new instance of Information.
        :rtype: Information
        """
        return Information(kilobytes, InformationUnits.Kilobyte)

    
    @staticmethod
    def from_megabytes(megabytes: float):
        """
        Create a new instance of Information from a value in megabytes.

        

        :param meters: The Information value in megabytes.
        :type megabytes: float
        :return: A new instance of Information.
        :rtype: Information
        """
        return Information(megabytes, InformationUnits.Megabyte)

    
    @staticmethod
    def from_gigabytes(gigabytes: float):
        """
        Create a new instance of Information from a value in gigabytes.

        

        :param meters: The Information value in gigabytes.
        :type gigabytes: float
        :return: A new instance of Information.
        :rtype: Information
        """
        return Information(gigabytes, InformationUnits.Gigabyte)

    
    @staticmethod
    def from_terabytes(terabytes: float):
        """
        Create a new instance of Information from a value in terabytes.

        

        :param meters: The Information value in terabytes.
        :type terabytes: float
        :return: A new instance of Information.
        :rtype: Information
        """
        return Information(terabytes, InformationUnits.Terabyte)

    
    @staticmethod
    def from_petabytes(petabytes: float):
        """
        Create a new instance of Information from a value in petabytes.

        

        :param meters: The Information value in petabytes.
        :type petabytes: float
        :return: A new instance of Information.
        :rtype: Information
        """
        return Information(petabytes, InformationUnits.Petabyte)

    
    @staticmethod
    def from_exabytes(exabytes: float):
        """
        Create a new instance of Information from a value in exabytes.

        

        :param meters: The Information value in exabytes.
        :type exabytes: float
        :return: A new instance of Information.
        :rtype: Information
        """
        return Information(exabytes, InformationUnits.Exabyte)

    
    @staticmethod
    def from_kilobits(kilobits: float):
        """
        Create a new instance of Information from a value in kilobits.

        

        :param meters: The Information value in kilobits.
        :type kilobits: float
        :return: A new instance of Information.
        :rtype: Information
        """
        return Information(kilobits, InformationUnits.Kilobit)

    
    @staticmethod
    def from_megabits(megabits: float):
        """
        Create a new instance of Information from a value in megabits.

        

        :param meters: The Information value in megabits.
        :type megabits: float
        :return: A new instance of Information.
        :rtype: Information
        """
        return Information(megabits, InformationUnits.Megabit)

    
    @staticmethod
    def from_gigabits(gigabits: float):
        """
        Create a new instance of Information from a value in gigabits.

        

        :param meters: The Information value in gigabits.
        :type gigabits: float
        :return: A new instance of Information.
        :rtype: Information
        """
        return Information(gigabits, InformationUnits.Gigabit)

    
    @staticmethod
    def from_terabits(terabits: float):
        """
        Create a new instance of Information from a value in terabits.

        

        :param meters: The Information value in terabits.
        :type terabits: float
        :return: A new instance of Information.
        :rtype: Information
        """
        return Information(terabits, InformationUnits.Terabit)

    
    @staticmethod
    def from_petabits(petabits: float):
        """
        Create a new instance of Information from a value in petabits.

        

        :param meters: The Information value in petabits.
        :type petabits: float
        :return: A new instance of Information.
        :rtype: Information
        """
        return Information(petabits, InformationUnits.Petabit)

    
    @staticmethod
    def from_exabits(exabits: float):
        """
        Create a new instance of Information from a value in exabits.

        

        :param meters: The Information value in exabits.
        :type exabits: float
        :return: A new instance of Information.
        :rtype: Information
        """
        return Information(exabits, InformationUnits.Exabit)

    
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
    def kilobytes(self) -> float:
        """
        
        """
        if self.__kilobytes != None:
            return self.__kilobytes
        self.__kilobytes = self.__convert_from_base(InformationUnits.Kilobyte)
        return self.__kilobytes

    
    @property
    def megabytes(self) -> float:
        """
        
        """
        if self.__megabytes != None:
            return self.__megabytes
        self.__megabytes = self.__convert_from_base(InformationUnits.Megabyte)
        return self.__megabytes

    
    @property
    def gigabytes(self) -> float:
        """
        
        """
        if self.__gigabytes != None:
            return self.__gigabytes
        self.__gigabytes = self.__convert_from_base(InformationUnits.Gigabyte)
        return self.__gigabytes

    
    @property
    def terabytes(self) -> float:
        """
        
        """
        if self.__terabytes != None:
            return self.__terabytes
        self.__terabytes = self.__convert_from_base(InformationUnits.Terabyte)
        return self.__terabytes

    
    @property
    def petabytes(self) -> float:
        """
        
        """
        if self.__petabytes != None:
            return self.__petabytes
        self.__petabytes = self.__convert_from_base(InformationUnits.Petabyte)
        return self.__petabytes

    
    @property
    def exabytes(self) -> float:
        """
        
        """
        if self.__exabytes != None:
            return self.__exabytes
        self.__exabytes = self.__convert_from_base(InformationUnits.Exabyte)
        return self.__exabytes

    
    @property
    def kilobits(self) -> float:
        """
        
        """
        if self.__kilobits != None:
            return self.__kilobits
        self.__kilobits = self.__convert_from_base(InformationUnits.Kilobit)
        return self.__kilobits

    
    @property
    def megabits(self) -> float:
        """
        
        """
        if self.__megabits != None:
            return self.__megabits
        self.__megabits = self.__convert_from_base(InformationUnits.Megabit)
        return self.__megabits

    
    @property
    def gigabits(self) -> float:
        """
        
        """
        if self.__gigabits != None:
            return self.__gigabits
        self.__gigabits = self.__convert_from_base(InformationUnits.Gigabit)
        return self.__gigabits

    
    @property
    def terabits(self) -> float:
        """
        
        """
        if self.__terabits != None:
            return self.__terabits
        self.__terabits = self.__convert_from_base(InformationUnits.Terabit)
        return self.__terabits

    
    @property
    def petabits(self) -> float:
        """
        
        """
        if self.__petabits != None:
            return self.__petabits
        self.__petabits = self.__convert_from_base(InformationUnits.Petabit)
        return self.__petabits

    
    @property
    def exabits(self) -> float:
        """
        
        """
        if self.__exabits != None:
            return self.__exabits
        self.__exabits = self.__convert_from_base(InformationUnits.Exabit)
        return self.__exabits

    
    def to_string(self, unit: InformationUnits = InformationUnits.Bit) -> str:
        """
        Format the Information to string.
        Note! the default format for Information is Bit.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == InformationUnits.Byte:
            return f"""{self.bytes} B"""
        
        if unit == InformationUnits.Bit:
            return f"""{self.bits} b"""
        
        if unit == InformationUnits.Kilobyte:
            return f"""{self.kilobytes} kB"""
        
        if unit == InformationUnits.Megabyte:
            return f"""{self.megabytes} MB"""
        
        if unit == InformationUnits.Gigabyte:
            return f"""{self.gigabytes} GB"""
        
        if unit == InformationUnits.Terabyte:
            return f"""{self.terabytes} TB"""
        
        if unit == InformationUnits.Petabyte:
            return f"""{self.petabytes} PB"""
        
        if unit == InformationUnits.Exabyte:
            return f"""{self.exabytes} EB"""
        
        if unit == InformationUnits.Kilobit:
            return f"""{self.kilobits} kb"""
        
        if unit == InformationUnits.Megabit:
            return f"""{self.megabits} Mb"""
        
        if unit == InformationUnits.Gigabit:
            return f"""{self.gigabits} Gb"""
        
        if unit == InformationUnits.Terabit:
            return f"""{self.terabits} Tb"""
        
        if unit == InformationUnits.Petabit:
            return f"""{self.petabits} Pb"""
        
        if unit == InformationUnits.Exabit:
            return f"""{self.exabits} Eb"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: InformationUnits = InformationUnits.Bit) -> str:
        """
        Get Information unit abbreviation.
        Note! the default abbreviation for Information is Bit.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == InformationUnits.Byte:
            return """B"""
        
        if unit_abbreviation == InformationUnits.Bit:
            return """b"""
        
        if unit_abbreviation == InformationUnits.Kilobyte:
            return """kB"""
        
        if unit_abbreviation == InformationUnits.Megabyte:
            return """MB"""
        
        if unit_abbreviation == InformationUnits.Gigabyte:
            return """GB"""
        
        if unit_abbreviation == InformationUnits.Terabyte:
            return """TB"""
        
        if unit_abbreviation == InformationUnits.Petabyte:
            return """PB"""
        
        if unit_abbreviation == InformationUnits.Exabyte:
            return """EB"""
        
        if unit_abbreviation == InformationUnits.Kilobit:
            return """kb"""
        
        if unit_abbreviation == InformationUnits.Megabit:
            return """Mb"""
        
        if unit_abbreviation == InformationUnits.Gigabit:
            return """Gb"""
        
        if unit_abbreviation == InformationUnits.Terabit:
            return """Tb"""
        
        if unit_abbreviation == InformationUnits.Petabit:
            return """Pb"""
        
        if unit_abbreviation == InformationUnits.Exabit:
            return """Eb"""
        
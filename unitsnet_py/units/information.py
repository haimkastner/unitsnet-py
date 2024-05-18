from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class InformationUnits(Enum):
        """
            InformationUnits enumeration
        """
        
        Byte = 'Byte'
        """
            
        """
        
        Bit = 'Bit'
        """
            
        """
        
        Kilobyte = 'Kilobyte'
        """
            
        """
        
        Megabyte = 'Megabyte'
        """
            
        """
        
        Gigabyte = 'Gigabyte'
        """
            
        """
        
        Terabyte = 'Terabyte'
        """
            
        """
        
        Petabyte = 'Petabyte'
        """
            
        """
        
        Exabyte = 'Exabyte'
        """
            
        """
        
        Kibibyte = 'Kibibyte'
        """
            
        """
        
        Mebibyte = 'Mebibyte'
        """
            
        """
        
        Gibibyte = 'Gibibyte'
        """
            
        """
        
        Tebibyte = 'Tebibyte'
        """
            
        """
        
        Pebibyte = 'Pebibyte'
        """
            
        """
        
        Exbibyte = 'Exbibyte'
        """
            
        """
        
        Kilobit = 'Kilobit'
        """
            
        """
        
        Megabit = 'Megabit'
        """
            
        """
        
        Gigabit = 'Gigabit'
        """
            
        """
        
        Terabit = 'Terabit'
        """
            
        """
        
        Petabit = 'Petabit'
        """
            
        """
        
        Exabit = 'Exabit'
        """
            
        """
        
        Kibibit = 'Kibibit'
        """
            
        """
        
        Mebibit = 'Mebibit'
        """
            
        """
        
        Gibibit = 'Gibibit'
        """
            
        """
        
        Tebibit = 'Tebibit'
        """
            
        """
        
        Pebibit = 'Pebibit'
        """
            
        """
        
        Exbibit = 'Exbibit'
        """
            
        """
        

class InformationDto:
    """
    A DTO representation of a Information

    Attributes:
        value (float): The value of the Information.
        unit (InformationUnits): The specific unit that the Information value is representing.
    """

    def __init__(self, value: float, unit: InformationUnits):
        """
        Create a new DTO representation of a Information

        Parameters:
            value (float): The value of the Information.
            unit (InformationUnits): The specific unit that the Information value is representing.
        """
        self.value: float = value
        """
        The value of the Information
        """
        self.unit: InformationUnits = unit
        """
        The specific unit that the Information value is representing
        """

    def to_json(self):
        """
        Get a Information DTO JSON object representing the current unit.

        :return: JSON object represents Information DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "Bit"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of Information DTO from a json representation.

        :param data: The Information DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "Bit"}
        :return: A new instance of InformationDto.
        :rtype: InformationDto
        """
        return InformationDto(value=data["value"], unit=InformationUnits(data["unit"]))


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
        
        self.__kibibytes = None
        
        self.__mebibytes = None
        
        self.__gibibytes = None
        
        self.__tebibytes = None
        
        self.__pebibytes = None
        
        self.__exbibytes = None
        
        self.__kilobits = None
        
        self.__megabits = None
        
        self.__gigabits = None
        
        self.__terabits = None
        
        self.__petabits = None
        
        self.__exabits = None
        
        self.__kibibits = None
        
        self.__mebibits = None
        
        self.__gibibits = None
        
        self.__tebibits = None
        
        self.__pebibits = None
        
        self.__exbibits = None
        

    def convert(self, unit: InformationUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: InformationUnits = InformationUnits.Bit) -> InformationDto:
        """
        Get a new instance of Information DTO representing the current unit.

        :param hold_in_unit: The specific Information unit to store the Information value in the DTO representation.
        :type hold_in_unit: InformationUnits
        :return: A new instance of InformationDto.
        :rtype: InformationDto
        """
        return InformationDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: InformationUnits = InformationUnits.Bit):
        """
        Get a Information DTO JSON object representing the current unit.

        :param hold_in_unit: The specific Information unit to store the Information value in the DTO representation.
        :type hold_in_unit: InformationUnits
        :return: JSON object represents Information DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "Bit"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(information_dto: InformationDto):
        """
        Obtain a new instance of Information from a DTO unit object.

        :param information_dto: The Information DTO representation.
        :type information_dto: InformationDto
        :return: A new instance of Information.
        :rtype: Information
        """
        return Information(information_dto.value, information_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of Information from a DTO unit json representation.

        :param data: The Information DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "Bit"}
        :return: A new instance of Information.
        :rtype: Information
        """
        return Information.from_dto(InformationDto.from_json(data))

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
        
        if from_unit == InformationUnits.Kibibyte:
            return ((value / 8) / 1024)
        
        if from_unit == InformationUnits.Mebibyte:
            return ((value / 8) / 1048576)
        
        if from_unit == InformationUnits.Gibibyte:
            return ((value / 8) / 1073741824)
        
        if from_unit == InformationUnits.Tebibyte:
            return ((value / 8) / 1099511627776)
        
        if from_unit == InformationUnits.Pebibyte:
            return ((value / 8) / 1125899906842624)
        
        if from_unit == InformationUnits.Exbibyte:
            return ((value / 8) / 1152921504606846976)
        
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
        
        if from_unit == InformationUnits.Kibibit:
            return ((value) / 1024)
        
        if from_unit == InformationUnits.Mebibit:
            return ((value) / 1048576)
        
        if from_unit == InformationUnits.Gibibit:
            return ((value) / 1073741824)
        
        if from_unit == InformationUnits.Tebibit:
            return ((value) / 1099511627776)
        
        if from_unit == InformationUnits.Pebibit:
            return ((value) / 1125899906842624)
        
        if from_unit == InformationUnits.Exbibit:
            return ((value) / 1152921504606846976)
        
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
        
        if to_unit == InformationUnits.Kibibyte:
            return ((value * 8) * 1024)
        
        if to_unit == InformationUnits.Mebibyte:
            return ((value * 8) * 1048576)
        
        if to_unit == InformationUnits.Gibibyte:
            return ((value * 8) * 1073741824)
        
        if to_unit == InformationUnits.Tebibyte:
            return ((value * 8) * 1099511627776)
        
        if to_unit == InformationUnits.Pebibyte:
            return ((value * 8) * 1125899906842624)
        
        if to_unit == InformationUnits.Exbibyte:
            return ((value * 8) * 1152921504606846976)
        
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
        
        if to_unit == InformationUnits.Kibibit:
            return ((value) * 1024)
        
        if to_unit == InformationUnits.Mebibit:
            return ((value) * 1048576)
        
        if to_unit == InformationUnits.Gibibit:
            return ((value) * 1073741824)
        
        if to_unit == InformationUnits.Tebibit:
            return ((value) * 1099511627776)
        
        if to_unit == InformationUnits.Pebibit:
            return ((value) * 1125899906842624)
        
        if to_unit == InformationUnits.Exbibit:
            return ((value) * 1152921504606846976)
        
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
    def from_kibibytes(kibibytes: float):
        """
        Create a new instance of Information from a value in kibibytes.

        

        :param meters: The Information value in kibibytes.
        :type kibibytes: float
        :return: A new instance of Information.
        :rtype: Information
        """
        return Information(kibibytes, InformationUnits.Kibibyte)

    
    @staticmethod
    def from_mebibytes(mebibytes: float):
        """
        Create a new instance of Information from a value in mebibytes.

        

        :param meters: The Information value in mebibytes.
        :type mebibytes: float
        :return: A new instance of Information.
        :rtype: Information
        """
        return Information(mebibytes, InformationUnits.Mebibyte)

    
    @staticmethod
    def from_gibibytes(gibibytes: float):
        """
        Create a new instance of Information from a value in gibibytes.

        

        :param meters: The Information value in gibibytes.
        :type gibibytes: float
        :return: A new instance of Information.
        :rtype: Information
        """
        return Information(gibibytes, InformationUnits.Gibibyte)

    
    @staticmethod
    def from_tebibytes(tebibytes: float):
        """
        Create a new instance of Information from a value in tebibytes.

        

        :param meters: The Information value in tebibytes.
        :type tebibytes: float
        :return: A new instance of Information.
        :rtype: Information
        """
        return Information(tebibytes, InformationUnits.Tebibyte)

    
    @staticmethod
    def from_pebibytes(pebibytes: float):
        """
        Create a new instance of Information from a value in pebibytes.

        

        :param meters: The Information value in pebibytes.
        :type pebibytes: float
        :return: A new instance of Information.
        :rtype: Information
        """
        return Information(pebibytes, InformationUnits.Pebibyte)

    
    @staticmethod
    def from_exbibytes(exbibytes: float):
        """
        Create a new instance of Information from a value in exbibytes.

        

        :param meters: The Information value in exbibytes.
        :type exbibytes: float
        :return: A new instance of Information.
        :rtype: Information
        """
        return Information(exbibytes, InformationUnits.Exbibyte)

    
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

    
    @staticmethod
    def from_kibibits(kibibits: float):
        """
        Create a new instance of Information from a value in kibibits.

        

        :param meters: The Information value in kibibits.
        :type kibibits: float
        :return: A new instance of Information.
        :rtype: Information
        """
        return Information(kibibits, InformationUnits.Kibibit)

    
    @staticmethod
    def from_mebibits(mebibits: float):
        """
        Create a new instance of Information from a value in mebibits.

        

        :param meters: The Information value in mebibits.
        :type mebibits: float
        :return: A new instance of Information.
        :rtype: Information
        """
        return Information(mebibits, InformationUnits.Mebibit)

    
    @staticmethod
    def from_gibibits(gibibits: float):
        """
        Create a new instance of Information from a value in gibibits.

        

        :param meters: The Information value in gibibits.
        :type gibibits: float
        :return: A new instance of Information.
        :rtype: Information
        """
        return Information(gibibits, InformationUnits.Gibibit)

    
    @staticmethod
    def from_tebibits(tebibits: float):
        """
        Create a new instance of Information from a value in tebibits.

        

        :param meters: The Information value in tebibits.
        :type tebibits: float
        :return: A new instance of Information.
        :rtype: Information
        """
        return Information(tebibits, InformationUnits.Tebibit)

    
    @staticmethod
    def from_pebibits(pebibits: float):
        """
        Create a new instance of Information from a value in pebibits.

        

        :param meters: The Information value in pebibits.
        :type pebibits: float
        :return: A new instance of Information.
        :rtype: Information
        """
        return Information(pebibits, InformationUnits.Pebibit)

    
    @staticmethod
    def from_exbibits(exbibits: float):
        """
        Create a new instance of Information from a value in exbibits.

        

        :param meters: The Information value in exbibits.
        :type exbibits: float
        :return: A new instance of Information.
        :rtype: Information
        """
        return Information(exbibits, InformationUnits.Exbibit)

    
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
    def kibibytes(self) -> float:
        """
        
        """
        if self.__kibibytes != None:
            return self.__kibibytes
        self.__kibibytes = self.__convert_from_base(InformationUnits.Kibibyte)
        return self.__kibibytes

    
    @property
    def mebibytes(self) -> float:
        """
        
        """
        if self.__mebibytes != None:
            return self.__mebibytes
        self.__mebibytes = self.__convert_from_base(InformationUnits.Mebibyte)
        return self.__mebibytes

    
    @property
    def gibibytes(self) -> float:
        """
        
        """
        if self.__gibibytes != None:
            return self.__gibibytes
        self.__gibibytes = self.__convert_from_base(InformationUnits.Gibibyte)
        return self.__gibibytes

    
    @property
    def tebibytes(self) -> float:
        """
        
        """
        if self.__tebibytes != None:
            return self.__tebibytes
        self.__tebibytes = self.__convert_from_base(InformationUnits.Tebibyte)
        return self.__tebibytes

    
    @property
    def pebibytes(self) -> float:
        """
        
        """
        if self.__pebibytes != None:
            return self.__pebibytes
        self.__pebibytes = self.__convert_from_base(InformationUnits.Pebibyte)
        return self.__pebibytes

    
    @property
    def exbibytes(self) -> float:
        """
        
        """
        if self.__exbibytes != None:
            return self.__exbibytes
        self.__exbibytes = self.__convert_from_base(InformationUnits.Exbibyte)
        return self.__exbibytes

    
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

    
    @property
    def kibibits(self) -> float:
        """
        
        """
        if self.__kibibits != None:
            return self.__kibibits
        self.__kibibits = self.__convert_from_base(InformationUnits.Kibibit)
        return self.__kibibits

    
    @property
    def mebibits(self) -> float:
        """
        
        """
        if self.__mebibits != None:
            return self.__mebibits
        self.__mebibits = self.__convert_from_base(InformationUnits.Mebibit)
        return self.__mebibits

    
    @property
    def gibibits(self) -> float:
        """
        
        """
        if self.__gibibits != None:
            return self.__gibibits
        self.__gibibits = self.__convert_from_base(InformationUnits.Gibibit)
        return self.__gibibits

    
    @property
    def tebibits(self) -> float:
        """
        
        """
        if self.__tebibits != None:
            return self.__tebibits
        self.__tebibits = self.__convert_from_base(InformationUnits.Tebibit)
        return self.__tebibits

    
    @property
    def pebibits(self) -> float:
        """
        
        """
        if self.__pebibits != None:
            return self.__pebibits
        self.__pebibits = self.__convert_from_base(InformationUnits.Pebibit)
        return self.__pebibits

    
    @property
    def exbibits(self) -> float:
        """
        
        """
        if self.__exbibits != None:
            return self.__exbibits
        self.__exbibits = self.__convert_from_base(InformationUnits.Exbibit)
        return self.__exbibits

    
    def to_string(self, unit: InformationUnits = InformationUnits.Bit, fractional_digits: int = None) -> str:
        """
        Format the Information to a string.
        
        Note: the default format for Information is Bit.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the Information. Default is 'Bit'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == InformationUnits.Byte:
            return f"""{super()._truncate_fraction_digits(self.bytes, fractional_digits)} B"""
        
        if unit == InformationUnits.Bit:
            return f"""{super()._truncate_fraction_digits(self.bits, fractional_digits)} b"""
        
        if unit == InformationUnits.Kilobyte:
            return f"""{super()._truncate_fraction_digits(self.kilobytes, fractional_digits)} kB"""
        
        if unit == InformationUnits.Megabyte:
            return f"""{super()._truncate_fraction_digits(self.megabytes, fractional_digits)} MB"""
        
        if unit == InformationUnits.Gigabyte:
            return f"""{super()._truncate_fraction_digits(self.gigabytes, fractional_digits)} GB"""
        
        if unit == InformationUnits.Terabyte:
            return f"""{super()._truncate_fraction_digits(self.terabytes, fractional_digits)} TB"""
        
        if unit == InformationUnits.Petabyte:
            return f"""{super()._truncate_fraction_digits(self.petabytes, fractional_digits)} PB"""
        
        if unit == InformationUnits.Exabyte:
            return f"""{super()._truncate_fraction_digits(self.exabytes, fractional_digits)} EB"""
        
        if unit == InformationUnits.Kibibyte:
            return f"""{super()._truncate_fraction_digits(self.kibibytes, fractional_digits)} KiBB"""
        
        if unit == InformationUnits.Mebibyte:
            return f"""{super()._truncate_fraction_digits(self.mebibytes, fractional_digits)} MiBB"""
        
        if unit == InformationUnits.Gibibyte:
            return f"""{super()._truncate_fraction_digits(self.gibibytes, fractional_digits)} GiBB"""
        
        if unit == InformationUnits.Tebibyte:
            return f"""{super()._truncate_fraction_digits(self.tebibytes, fractional_digits)} TiBB"""
        
        if unit == InformationUnits.Pebibyte:
            return f"""{super()._truncate_fraction_digits(self.pebibytes, fractional_digits)} PiBB"""
        
        if unit == InformationUnits.Exbibyte:
            return f"""{super()._truncate_fraction_digits(self.exbibytes, fractional_digits)} EiBB"""
        
        if unit == InformationUnits.Kilobit:
            return f"""{super()._truncate_fraction_digits(self.kilobits, fractional_digits)} kb"""
        
        if unit == InformationUnits.Megabit:
            return f"""{super()._truncate_fraction_digits(self.megabits, fractional_digits)} Mb"""
        
        if unit == InformationUnits.Gigabit:
            return f"""{super()._truncate_fraction_digits(self.gigabits, fractional_digits)} Gb"""
        
        if unit == InformationUnits.Terabit:
            return f"""{super()._truncate_fraction_digits(self.terabits, fractional_digits)} Tb"""
        
        if unit == InformationUnits.Petabit:
            return f"""{super()._truncate_fraction_digits(self.petabits, fractional_digits)} Pb"""
        
        if unit == InformationUnits.Exabit:
            return f"""{super()._truncate_fraction_digits(self.exabits, fractional_digits)} Eb"""
        
        if unit == InformationUnits.Kibibit:
            return f"""{super()._truncate_fraction_digits(self.kibibits, fractional_digits)} KiBb"""
        
        if unit == InformationUnits.Mebibit:
            return f"""{super()._truncate_fraction_digits(self.mebibits, fractional_digits)} MiBb"""
        
        if unit == InformationUnits.Gibibit:
            return f"""{super()._truncate_fraction_digits(self.gibibits, fractional_digits)} GiBb"""
        
        if unit == InformationUnits.Tebibit:
            return f"""{super()._truncate_fraction_digits(self.tebibits, fractional_digits)} TiBb"""
        
        if unit == InformationUnits.Pebibit:
            return f"""{super()._truncate_fraction_digits(self.pebibits, fractional_digits)} PiBb"""
        
        if unit == InformationUnits.Exbibit:
            return f"""{super()._truncate_fraction_digits(self.exbibits, fractional_digits)} EiBb"""
        
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
        
        if unit_abbreviation == InformationUnits.Kibibyte:
            return """KiBB"""
        
        if unit_abbreviation == InformationUnits.Mebibyte:
            return """MiBB"""
        
        if unit_abbreviation == InformationUnits.Gibibyte:
            return """GiBB"""
        
        if unit_abbreviation == InformationUnits.Tebibyte:
            return """TiBB"""
        
        if unit_abbreviation == InformationUnits.Pebibyte:
            return """PiBB"""
        
        if unit_abbreviation == InformationUnits.Exbibyte:
            return """EiBB"""
        
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
        
        if unit_abbreviation == InformationUnits.Kibibit:
            return """KiBb"""
        
        if unit_abbreviation == InformationUnits.Mebibit:
            return """MiBb"""
        
        if unit_abbreviation == InformationUnits.Gibibit:
            return """GiBb"""
        
        if unit_abbreviation == InformationUnits.Tebibit:
            return """TiBb"""
        
        if unit_abbreviation == InformationUnits.Pebibit:
            return """PiBb"""
        
        if unit_abbreviation == InformationUnits.Exbibit:
            return """EiBb"""
        
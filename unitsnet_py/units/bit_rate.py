from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class BitRateUnits(Enum):
        """
            BitRateUnits enumeration
        """
        
        BitPerSecond = 'BitPerSecond'
        """
            
        """
        
        BytePerSecond = 'BytePerSecond'
        """
            
        """
        
        KilobitPerSecond = 'KilobitPerSecond'
        """
            
        """
        
        MegabitPerSecond = 'MegabitPerSecond'
        """
            
        """
        
        GigabitPerSecond = 'GigabitPerSecond'
        """
            
        """
        
        TerabitPerSecond = 'TerabitPerSecond'
        """
            
        """
        
        PetabitPerSecond = 'PetabitPerSecond'
        """
            
        """
        
        ExabitPerSecond = 'ExabitPerSecond'
        """
            
        """
        
        KibibitPerSecond = 'KibibitPerSecond'
        """
            
        """
        
        MebibitPerSecond = 'MebibitPerSecond'
        """
            
        """
        
        GibibitPerSecond = 'GibibitPerSecond'
        """
            
        """
        
        TebibitPerSecond = 'TebibitPerSecond'
        """
            
        """
        
        PebibitPerSecond = 'PebibitPerSecond'
        """
            
        """
        
        ExbibitPerSecond = 'ExbibitPerSecond'
        """
            
        """
        
        KilobytePerSecond = 'KilobytePerSecond'
        """
            
        """
        
        MegabytePerSecond = 'MegabytePerSecond'
        """
            
        """
        
        GigabytePerSecond = 'GigabytePerSecond'
        """
            
        """
        
        TerabytePerSecond = 'TerabytePerSecond'
        """
            
        """
        
        PetabytePerSecond = 'PetabytePerSecond'
        """
            
        """
        
        ExabytePerSecond = 'ExabytePerSecond'
        """
            
        """
        
        KibibytePerSecond = 'KibibytePerSecond'
        """
            
        """
        
        MebibytePerSecond = 'MebibytePerSecond'
        """
            
        """
        
        GibibytePerSecond = 'GibibytePerSecond'
        """
            
        """
        
        TebibytePerSecond = 'TebibytePerSecond'
        """
            
        """
        
        PebibytePerSecond = 'PebibytePerSecond'
        """
            
        """
        
        ExbibytePerSecond = 'ExbibytePerSecond'
        """
            
        """
        

class BitRateDto:
    """
    A DTO representation of a BitRate

    Attributes:
        value (float): The value of the BitRate.
        unit (BitRateUnits): The specific unit that the BitRate value is representing.
    """

    def __init__(self, value: float, unit: BitRateUnits):
        """
        Create a new DTO representation of a BitRate

        Parameters:
            value (float): The value of the BitRate.
            unit (BitRateUnits): The specific unit that the BitRate value is representing.
        """
        self.value: float = value
        """
        The value of the BitRate
        """
        self.unit: BitRateUnits = unit
        """
        The specific unit that the BitRate value is representing
        """

    def to_json(self):
        """
        Get a BitRate DTO JSON object representing the current unit.

        :return: JSON object represents BitRate DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "BitPerSecond"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of BitRate DTO from a json representation.

        :param data: The BitRate DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "BitPerSecond"}
        :return: A new instance of BitRateDto.
        :rtype: BitRateDto
        """
        return BitRateDto(value=data["value"], unit=BitRateUnits(data["unit"]))


class BitRate(AbstractMeasure):
    """
    In telecommunications and computing, bit rate is the number of bits that are conveyed or processed per unit of time.

    Args:
        value (float): The value.
        from_unit (BitRateUnits): The BitRate unit to create from, The default unit is BitPerSecond
    """
    def __init__(self, value: float, from_unit: BitRateUnits = BitRateUnits.BitPerSecond):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__bits_per_second = None
        
        self.__bytes_per_second = None
        
        self.__kilobits_per_second = None
        
        self.__megabits_per_second = None
        
        self.__gigabits_per_second = None
        
        self.__terabits_per_second = None
        
        self.__petabits_per_second = None
        
        self.__exabits_per_second = None
        
        self.__kibibits_per_second = None
        
        self.__mebibits_per_second = None
        
        self.__gibibits_per_second = None
        
        self.__tebibits_per_second = None
        
        self.__pebibits_per_second = None
        
        self.__exbibits_per_second = None
        
        self.__kilobytes_per_second = None
        
        self.__megabytes_per_second = None
        
        self.__gigabytes_per_second = None
        
        self.__terabytes_per_second = None
        
        self.__petabytes_per_second = None
        
        self.__exabytes_per_second = None
        
        self.__kibibytes_per_second = None
        
        self.__mebibytes_per_second = None
        
        self.__gibibytes_per_second = None
        
        self.__tebibytes_per_second = None
        
        self.__pebibytes_per_second = None
        
        self.__exbibytes_per_second = None
        

    def convert(self, unit: BitRateUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: BitRateUnits = BitRateUnits.BitPerSecond) -> BitRateDto:
        """
        Get a new instance of BitRate DTO representing the current unit.

        :param hold_in_unit: The specific BitRate unit to store the BitRate value in the DTO representation.
        :type hold_in_unit: BitRateUnits
        :return: A new instance of BitRateDto.
        :rtype: BitRateDto
        """
        return BitRateDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: BitRateUnits = BitRateUnits.BitPerSecond):
        """
        Get a BitRate DTO JSON object representing the current unit.

        :param hold_in_unit: The specific BitRate unit to store the BitRate value in the DTO representation.
        :type hold_in_unit: BitRateUnits
        :return: JSON object represents BitRate DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "BitPerSecond"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(bit_rate_dto: BitRateDto):
        """
        Obtain a new instance of BitRate from a DTO unit object.

        :param bit_rate_dto: The BitRate DTO representation.
        :type bit_rate_dto: BitRateDto
        :return: A new instance of BitRate.
        :rtype: BitRate
        """
        return BitRate(bit_rate_dto.value, bit_rate_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of BitRate from a DTO unit json representation.

        :param data: The BitRate DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "BitPerSecond"}
        :return: A new instance of BitRate.
        :rtype: BitRate
        """
        return BitRate.from_dto(BitRateDto.from_json(data))

    def __convert_from_base(self, from_unit: BitRateUnits) -> float:
        value = self._value
        
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
        
        if from_unit == BitRateUnits.KibibitPerSecond:
            return ((value) / 1024)
        
        if from_unit == BitRateUnits.MebibitPerSecond:
            return ((value) / 1048576)
        
        if from_unit == BitRateUnits.GibibitPerSecond:
            return ((value) / 1073741824)
        
        if from_unit == BitRateUnits.TebibitPerSecond:
            return ((value) / 1099511627776)
        
        if from_unit == BitRateUnits.PebibitPerSecond:
            return ((value) / 1125899906842624)
        
        if from_unit == BitRateUnits.ExbibitPerSecond:
            return ((value) / 1152921504606846976)
        
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
        
        if from_unit == BitRateUnits.KibibytePerSecond:
            return ((value / 8) / 1024)
        
        if from_unit == BitRateUnits.MebibytePerSecond:
            return ((value / 8) / 1048576)
        
        if from_unit == BitRateUnits.GibibytePerSecond:
            return ((value / 8) / 1073741824)
        
        if from_unit == BitRateUnits.TebibytePerSecond:
            return ((value / 8) / 1099511627776)
        
        if from_unit == BitRateUnits.PebibytePerSecond:
            return ((value / 8) / 1125899906842624)
        
        if from_unit == BitRateUnits.ExbibytePerSecond:
            return ((value / 8) / 1152921504606846976)
        
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
        
        if to_unit == BitRateUnits.KibibitPerSecond:
            return ((value) * 1024)
        
        if to_unit == BitRateUnits.MebibitPerSecond:
            return ((value) * 1048576)
        
        if to_unit == BitRateUnits.GibibitPerSecond:
            return ((value) * 1073741824)
        
        if to_unit == BitRateUnits.TebibitPerSecond:
            return ((value) * 1099511627776)
        
        if to_unit == BitRateUnits.PebibitPerSecond:
            return ((value) * 1125899906842624)
        
        if to_unit == BitRateUnits.ExbibitPerSecond:
            return ((value) * 1152921504606846976)
        
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
        
        if to_unit == BitRateUnits.KibibytePerSecond:
            return ((value * 8) * 1024)
        
        if to_unit == BitRateUnits.MebibytePerSecond:
            return ((value * 8) * 1048576)
        
        if to_unit == BitRateUnits.GibibytePerSecond:
            return ((value * 8) * 1073741824)
        
        if to_unit == BitRateUnits.TebibytePerSecond:
            return ((value * 8) * 1099511627776)
        
        if to_unit == BitRateUnits.PebibytePerSecond:
            return ((value * 8) * 1125899906842624)
        
        if to_unit == BitRateUnits.ExbibytePerSecond:
            return ((value * 8) * 1152921504606846976)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
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
    def from_kibibits_per_second(kibibits_per_second: float):
        """
        Create a new instance of BitRate from a value in kibibits_per_second.

        

        :param meters: The BitRate value in kibibits_per_second.
        :type kibibits_per_second: float
        :return: A new instance of BitRate.
        :rtype: BitRate
        """
        return BitRate(kibibits_per_second, BitRateUnits.KibibitPerSecond)

    
    @staticmethod
    def from_mebibits_per_second(mebibits_per_second: float):
        """
        Create a new instance of BitRate from a value in mebibits_per_second.

        

        :param meters: The BitRate value in mebibits_per_second.
        :type mebibits_per_second: float
        :return: A new instance of BitRate.
        :rtype: BitRate
        """
        return BitRate(mebibits_per_second, BitRateUnits.MebibitPerSecond)

    
    @staticmethod
    def from_gibibits_per_second(gibibits_per_second: float):
        """
        Create a new instance of BitRate from a value in gibibits_per_second.

        

        :param meters: The BitRate value in gibibits_per_second.
        :type gibibits_per_second: float
        :return: A new instance of BitRate.
        :rtype: BitRate
        """
        return BitRate(gibibits_per_second, BitRateUnits.GibibitPerSecond)

    
    @staticmethod
    def from_tebibits_per_second(tebibits_per_second: float):
        """
        Create a new instance of BitRate from a value in tebibits_per_second.

        

        :param meters: The BitRate value in tebibits_per_second.
        :type tebibits_per_second: float
        :return: A new instance of BitRate.
        :rtype: BitRate
        """
        return BitRate(tebibits_per_second, BitRateUnits.TebibitPerSecond)

    
    @staticmethod
    def from_pebibits_per_second(pebibits_per_second: float):
        """
        Create a new instance of BitRate from a value in pebibits_per_second.

        

        :param meters: The BitRate value in pebibits_per_second.
        :type pebibits_per_second: float
        :return: A new instance of BitRate.
        :rtype: BitRate
        """
        return BitRate(pebibits_per_second, BitRateUnits.PebibitPerSecond)

    
    @staticmethod
    def from_exbibits_per_second(exbibits_per_second: float):
        """
        Create a new instance of BitRate from a value in exbibits_per_second.

        

        :param meters: The BitRate value in exbibits_per_second.
        :type exbibits_per_second: float
        :return: A new instance of BitRate.
        :rtype: BitRate
        """
        return BitRate(exbibits_per_second, BitRateUnits.ExbibitPerSecond)

    
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

    
    @staticmethod
    def from_kibibytes_per_second(kibibytes_per_second: float):
        """
        Create a new instance of BitRate from a value in kibibytes_per_second.

        

        :param meters: The BitRate value in kibibytes_per_second.
        :type kibibytes_per_second: float
        :return: A new instance of BitRate.
        :rtype: BitRate
        """
        return BitRate(kibibytes_per_second, BitRateUnits.KibibytePerSecond)

    
    @staticmethod
    def from_mebibytes_per_second(mebibytes_per_second: float):
        """
        Create a new instance of BitRate from a value in mebibytes_per_second.

        

        :param meters: The BitRate value in mebibytes_per_second.
        :type mebibytes_per_second: float
        :return: A new instance of BitRate.
        :rtype: BitRate
        """
        return BitRate(mebibytes_per_second, BitRateUnits.MebibytePerSecond)

    
    @staticmethod
    def from_gibibytes_per_second(gibibytes_per_second: float):
        """
        Create a new instance of BitRate from a value in gibibytes_per_second.

        

        :param meters: The BitRate value in gibibytes_per_second.
        :type gibibytes_per_second: float
        :return: A new instance of BitRate.
        :rtype: BitRate
        """
        return BitRate(gibibytes_per_second, BitRateUnits.GibibytePerSecond)

    
    @staticmethod
    def from_tebibytes_per_second(tebibytes_per_second: float):
        """
        Create a new instance of BitRate from a value in tebibytes_per_second.

        

        :param meters: The BitRate value in tebibytes_per_second.
        :type tebibytes_per_second: float
        :return: A new instance of BitRate.
        :rtype: BitRate
        """
        return BitRate(tebibytes_per_second, BitRateUnits.TebibytePerSecond)

    
    @staticmethod
    def from_pebibytes_per_second(pebibytes_per_second: float):
        """
        Create a new instance of BitRate from a value in pebibytes_per_second.

        

        :param meters: The BitRate value in pebibytes_per_second.
        :type pebibytes_per_second: float
        :return: A new instance of BitRate.
        :rtype: BitRate
        """
        return BitRate(pebibytes_per_second, BitRateUnits.PebibytePerSecond)

    
    @staticmethod
    def from_exbibytes_per_second(exbibytes_per_second: float):
        """
        Create a new instance of BitRate from a value in exbibytes_per_second.

        

        :param meters: The BitRate value in exbibytes_per_second.
        :type exbibytes_per_second: float
        :return: A new instance of BitRate.
        :rtype: BitRate
        """
        return BitRate(exbibytes_per_second, BitRateUnits.ExbibytePerSecond)

    
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
    def kibibits_per_second(self) -> float:
        """
        
        """
        if self.__kibibits_per_second != None:
            return self.__kibibits_per_second
        self.__kibibits_per_second = self.__convert_from_base(BitRateUnits.KibibitPerSecond)
        return self.__kibibits_per_second

    
    @property
    def mebibits_per_second(self) -> float:
        """
        
        """
        if self.__mebibits_per_second != None:
            return self.__mebibits_per_second
        self.__mebibits_per_second = self.__convert_from_base(BitRateUnits.MebibitPerSecond)
        return self.__mebibits_per_second

    
    @property
    def gibibits_per_second(self) -> float:
        """
        
        """
        if self.__gibibits_per_second != None:
            return self.__gibibits_per_second
        self.__gibibits_per_second = self.__convert_from_base(BitRateUnits.GibibitPerSecond)
        return self.__gibibits_per_second

    
    @property
    def tebibits_per_second(self) -> float:
        """
        
        """
        if self.__tebibits_per_second != None:
            return self.__tebibits_per_second
        self.__tebibits_per_second = self.__convert_from_base(BitRateUnits.TebibitPerSecond)
        return self.__tebibits_per_second

    
    @property
    def pebibits_per_second(self) -> float:
        """
        
        """
        if self.__pebibits_per_second != None:
            return self.__pebibits_per_second
        self.__pebibits_per_second = self.__convert_from_base(BitRateUnits.PebibitPerSecond)
        return self.__pebibits_per_second

    
    @property
    def exbibits_per_second(self) -> float:
        """
        
        """
        if self.__exbibits_per_second != None:
            return self.__exbibits_per_second
        self.__exbibits_per_second = self.__convert_from_base(BitRateUnits.ExbibitPerSecond)
        return self.__exbibits_per_second

    
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

    
    @property
    def kibibytes_per_second(self) -> float:
        """
        
        """
        if self.__kibibytes_per_second != None:
            return self.__kibibytes_per_second
        self.__kibibytes_per_second = self.__convert_from_base(BitRateUnits.KibibytePerSecond)
        return self.__kibibytes_per_second

    
    @property
    def mebibytes_per_second(self) -> float:
        """
        
        """
        if self.__mebibytes_per_second != None:
            return self.__mebibytes_per_second
        self.__mebibytes_per_second = self.__convert_from_base(BitRateUnits.MebibytePerSecond)
        return self.__mebibytes_per_second

    
    @property
    def gibibytes_per_second(self) -> float:
        """
        
        """
        if self.__gibibytes_per_second != None:
            return self.__gibibytes_per_second
        self.__gibibytes_per_second = self.__convert_from_base(BitRateUnits.GibibytePerSecond)
        return self.__gibibytes_per_second

    
    @property
    def tebibytes_per_second(self) -> float:
        """
        
        """
        if self.__tebibytes_per_second != None:
            return self.__tebibytes_per_second
        self.__tebibytes_per_second = self.__convert_from_base(BitRateUnits.TebibytePerSecond)
        return self.__tebibytes_per_second

    
    @property
    def pebibytes_per_second(self) -> float:
        """
        
        """
        if self.__pebibytes_per_second != None:
            return self.__pebibytes_per_second
        self.__pebibytes_per_second = self.__convert_from_base(BitRateUnits.PebibytePerSecond)
        return self.__pebibytes_per_second

    
    @property
    def exbibytes_per_second(self) -> float:
        """
        
        """
        if self.__exbibytes_per_second != None:
            return self.__exbibytes_per_second
        self.__exbibytes_per_second = self.__convert_from_base(BitRateUnits.ExbibytePerSecond)
        return self.__exbibytes_per_second

    
    def to_string(self, unit: BitRateUnits = BitRateUnits.BitPerSecond, fractional_digits: int = None) -> str:
        """
        Format the BitRate to a string.
        
        Note: the default format for BitRate is BitPerSecond.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the BitRate. Default is 'BitPerSecond'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == BitRateUnits.BitPerSecond:
            return f"""{super()._truncate_fraction_digits(self.bits_per_second, fractional_digits)} bit/s"""
        
        if unit == BitRateUnits.BytePerSecond:
            return f"""{super()._truncate_fraction_digits(self.bytes_per_second, fractional_digits)} B/s"""
        
        if unit == BitRateUnits.KilobitPerSecond:
            return f"""{super()._truncate_fraction_digits(self.kilobits_per_second, fractional_digits)} kbit/s"""
        
        if unit == BitRateUnits.MegabitPerSecond:
            return f"""{super()._truncate_fraction_digits(self.megabits_per_second, fractional_digits)} Mbit/s"""
        
        if unit == BitRateUnits.GigabitPerSecond:
            return f"""{super()._truncate_fraction_digits(self.gigabits_per_second, fractional_digits)} Gbit/s"""
        
        if unit == BitRateUnits.TerabitPerSecond:
            return f"""{super()._truncate_fraction_digits(self.terabits_per_second, fractional_digits)} Tbit/s"""
        
        if unit == BitRateUnits.PetabitPerSecond:
            return f"""{super()._truncate_fraction_digits(self.petabits_per_second, fractional_digits)} Pbit/s"""
        
        if unit == BitRateUnits.ExabitPerSecond:
            return f"""{super()._truncate_fraction_digits(self.exabits_per_second, fractional_digits)} Ebit/s"""
        
        if unit == BitRateUnits.KibibitPerSecond:
            return f"""{super()._truncate_fraction_digits(self.kibibits_per_second, fractional_digits)} KiBbit/s"""
        
        if unit == BitRateUnits.MebibitPerSecond:
            return f"""{super()._truncate_fraction_digits(self.mebibits_per_second, fractional_digits)} MiBbit/s"""
        
        if unit == BitRateUnits.GibibitPerSecond:
            return f"""{super()._truncate_fraction_digits(self.gibibits_per_second, fractional_digits)} GiBbit/s"""
        
        if unit == BitRateUnits.TebibitPerSecond:
            return f"""{super()._truncate_fraction_digits(self.tebibits_per_second, fractional_digits)} TiBbit/s"""
        
        if unit == BitRateUnits.PebibitPerSecond:
            return f"""{super()._truncate_fraction_digits(self.pebibits_per_second, fractional_digits)} PiBbit/s"""
        
        if unit == BitRateUnits.ExbibitPerSecond:
            return f"""{super()._truncate_fraction_digits(self.exbibits_per_second, fractional_digits)} EiBbit/s"""
        
        if unit == BitRateUnits.KilobytePerSecond:
            return f"""{super()._truncate_fraction_digits(self.kilobytes_per_second, fractional_digits)} kB/s"""
        
        if unit == BitRateUnits.MegabytePerSecond:
            return f"""{super()._truncate_fraction_digits(self.megabytes_per_second, fractional_digits)} MB/s"""
        
        if unit == BitRateUnits.GigabytePerSecond:
            return f"""{super()._truncate_fraction_digits(self.gigabytes_per_second, fractional_digits)} GB/s"""
        
        if unit == BitRateUnits.TerabytePerSecond:
            return f"""{super()._truncate_fraction_digits(self.terabytes_per_second, fractional_digits)} TB/s"""
        
        if unit == BitRateUnits.PetabytePerSecond:
            return f"""{super()._truncate_fraction_digits(self.petabytes_per_second, fractional_digits)} PB/s"""
        
        if unit == BitRateUnits.ExabytePerSecond:
            return f"""{super()._truncate_fraction_digits(self.exabytes_per_second, fractional_digits)} EB/s"""
        
        if unit == BitRateUnits.KibibytePerSecond:
            return f"""{super()._truncate_fraction_digits(self.kibibytes_per_second, fractional_digits)} KiBB/s"""
        
        if unit == BitRateUnits.MebibytePerSecond:
            return f"""{super()._truncate_fraction_digits(self.mebibytes_per_second, fractional_digits)} MiBB/s"""
        
        if unit == BitRateUnits.GibibytePerSecond:
            return f"""{super()._truncate_fraction_digits(self.gibibytes_per_second, fractional_digits)} GiBB/s"""
        
        if unit == BitRateUnits.TebibytePerSecond:
            return f"""{super()._truncate_fraction_digits(self.tebibytes_per_second, fractional_digits)} TiBB/s"""
        
        if unit == BitRateUnits.PebibytePerSecond:
            return f"""{super()._truncate_fraction_digits(self.pebibytes_per_second, fractional_digits)} PiBB/s"""
        
        if unit == BitRateUnits.ExbibytePerSecond:
            return f"""{super()._truncate_fraction_digits(self.exbibytes_per_second, fractional_digits)} EiBB/s"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: BitRateUnits = BitRateUnits.BitPerSecond) -> str:
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
            return """kbit/s"""
        
        if unit_abbreviation == BitRateUnits.MegabitPerSecond:
            return """Mbit/s"""
        
        if unit_abbreviation == BitRateUnits.GigabitPerSecond:
            return """Gbit/s"""
        
        if unit_abbreviation == BitRateUnits.TerabitPerSecond:
            return """Tbit/s"""
        
        if unit_abbreviation == BitRateUnits.PetabitPerSecond:
            return """Pbit/s"""
        
        if unit_abbreviation == BitRateUnits.ExabitPerSecond:
            return """Ebit/s"""
        
        if unit_abbreviation == BitRateUnits.KibibitPerSecond:
            return """KiBbit/s"""
        
        if unit_abbreviation == BitRateUnits.MebibitPerSecond:
            return """MiBbit/s"""
        
        if unit_abbreviation == BitRateUnits.GibibitPerSecond:
            return """GiBbit/s"""
        
        if unit_abbreviation == BitRateUnits.TebibitPerSecond:
            return """TiBbit/s"""
        
        if unit_abbreviation == BitRateUnits.PebibitPerSecond:
            return """PiBbit/s"""
        
        if unit_abbreviation == BitRateUnits.ExbibitPerSecond:
            return """EiBbit/s"""
        
        if unit_abbreviation == BitRateUnits.KilobytePerSecond:
            return """kB/s"""
        
        if unit_abbreviation == BitRateUnits.MegabytePerSecond:
            return """MB/s"""
        
        if unit_abbreviation == BitRateUnits.GigabytePerSecond:
            return """GB/s"""
        
        if unit_abbreviation == BitRateUnits.TerabytePerSecond:
            return """TB/s"""
        
        if unit_abbreviation == BitRateUnits.PetabytePerSecond:
            return """PB/s"""
        
        if unit_abbreviation == BitRateUnits.ExabytePerSecond:
            return """EB/s"""
        
        if unit_abbreviation == BitRateUnits.KibibytePerSecond:
            return """KiBB/s"""
        
        if unit_abbreviation == BitRateUnits.MebibytePerSecond:
            return """MiBB/s"""
        
        if unit_abbreviation == BitRateUnits.GibibytePerSecond:
            return """GiBB/s"""
        
        if unit_abbreviation == BitRateUnits.TebibytePerSecond:
            return """TiBB/s"""
        
        if unit_abbreviation == BitRateUnits.PebibytePerSecond:
            return """PiBB/s"""
        
        if unit_abbreviation == BitRateUnits.ExbibytePerSecond:
            return """EiBB/s"""
        
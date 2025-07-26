from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class ElectricPotentialChangeRateUnits(Enum):
        """
            ElectricPotentialChangeRateUnits enumeration
        """
        
        VoltPerSecond = 'VoltPerSecond'
        """
            
        """
        
        VoltPerMicrosecond = 'VoltPerMicrosecond'
        """
            
        """
        
        VoltPerMinute = 'VoltPerMinute'
        """
            
        """
        
        VoltPerHour = 'VoltPerHour'
        """
            
        """
        
        MicrovoltPerSecond = 'MicrovoltPerSecond'
        """
            
        """
        
        MillivoltPerSecond = 'MillivoltPerSecond'
        """
            
        """
        
        KilovoltPerSecond = 'KilovoltPerSecond'
        """
            
        """
        
        MegavoltPerSecond = 'MegavoltPerSecond'
        """
            
        """
        
        MicrovoltPerMicrosecond = 'MicrovoltPerMicrosecond'
        """
            
        """
        
        MillivoltPerMicrosecond = 'MillivoltPerMicrosecond'
        """
            
        """
        
        KilovoltPerMicrosecond = 'KilovoltPerMicrosecond'
        """
            
        """
        
        MegavoltPerMicrosecond = 'MegavoltPerMicrosecond'
        """
            
        """
        
        MicrovoltPerMinute = 'MicrovoltPerMinute'
        """
            
        """
        
        MillivoltPerMinute = 'MillivoltPerMinute'
        """
            
        """
        
        KilovoltPerMinute = 'KilovoltPerMinute'
        """
            
        """
        
        MegavoltPerMinute = 'MegavoltPerMinute'
        """
            
        """
        
        MicrovoltPerHour = 'MicrovoltPerHour'
        """
            
        """
        
        MillivoltPerHour = 'MillivoltPerHour'
        """
            
        """
        
        KilovoltPerHour = 'KilovoltPerHour'
        """
            
        """
        
        MegavoltPerHour = 'MegavoltPerHour'
        """
            
        """
        

class ElectricPotentialChangeRateDto:
    """
    A DTO representation of a ElectricPotentialChangeRate

    Attributes:
        value (float): The value of the ElectricPotentialChangeRate.
        unit (ElectricPotentialChangeRateUnits): The specific unit that the ElectricPotentialChangeRate value is representing.
    """

    def __init__(self, value: float, unit: ElectricPotentialChangeRateUnits):
        """
        Create a new DTO representation of a ElectricPotentialChangeRate

        Parameters:
            value (float): The value of the ElectricPotentialChangeRate.
            unit (ElectricPotentialChangeRateUnits): The specific unit that the ElectricPotentialChangeRate value is representing.
        """
        self.value: float = value
        """
        The value of the ElectricPotentialChangeRate
        """
        self.unit: ElectricPotentialChangeRateUnits = unit
        """
        The specific unit that the ElectricPotentialChangeRate value is representing
        """

    def to_json(self):
        """
        Get a ElectricPotentialChangeRate DTO JSON object representing the current unit.

        :return: JSON object represents ElectricPotentialChangeRate DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "VoltPerSecond"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of ElectricPotentialChangeRate DTO from a json representation.

        :param data: The ElectricPotentialChangeRate DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "VoltPerSecond"}
        :return: A new instance of ElectricPotentialChangeRateDto.
        :rtype: ElectricPotentialChangeRateDto
        """
        return ElectricPotentialChangeRateDto(value=data["value"], unit=ElectricPotentialChangeRateUnits(data["unit"]))


class ElectricPotentialChangeRate(AbstractMeasure):
    """
    ElectricPotential change rate is the ratio of the electric potential change to the time during which the change occurred (value of electric potential changes per unit time).

    Args:
        value (float): The value.
        from_unit (ElectricPotentialChangeRateUnits): The ElectricPotentialChangeRate unit to create from, The default unit is VoltPerSecond
    """
    def __init__(self, value: float, from_unit: ElectricPotentialChangeRateUnits = ElectricPotentialChangeRateUnits.VoltPerSecond):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__volts_per_second = None
        
        self.__volts_per_microsecond = None
        
        self.__volts_per_minute = None
        
        self.__volts_per_hour = None
        
        self.__microvolts_per_second = None
        
        self.__millivolts_per_second = None
        
        self.__kilovolts_per_second = None
        
        self.__megavolts_per_second = None
        
        self.__microvolts_per_microsecond = None
        
        self.__millivolts_per_microsecond = None
        
        self.__kilovolts_per_microsecond = None
        
        self.__megavolts_per_microsecond = None
        
        self.__microvolts_per_minute = None
        
        self.__millivolts_per_minute = None
        
        self.__kilovolts_per_minute = None
        
        self.__megavolts_per_minute = None
        
        self.__microvolts_per_hour = None
        
        self.__millivolts_per_hour = None
        
        self.__kilovolts_per_hour = None
        
        self.__megavolts_per_hour = None
        

    def convert(self, unit: ElectricPotentialChangeRateUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: ElectricPotentialChangeRateUnits = ElectricPotentialChangeRateUnits.VoltPerSecond) -> ElectricPotentialChangeRateDto:
        """
        Get a new instance of ElectricPotentialChangeRate DTO representing the current unit.

        :param hold_in_unit: The specific ElectricPotentialChangeRate unit to store the ElectricPotentialChangeRate value in the DTO representation.
        :type hold_in_unit: ElectricPotentialChangeRateUnits
        :return: A new instance of ElectricPotentialChangeRateDto.
        :rtype: ElectricPotentialChangeRateDto
        """
        return ElectricPotentialChangeRateDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: ElectricPotentialChangeRateUnits = ElectricPotentialChangeRateUnits.VoltPerSecond):
        """
        Get a ElectricPotentialChangeRate DTO JSON object representing the current unit.

        :param hold_in_unit: The specific ElectricPotentialChangeRate unit to store the ElectricPotentialChangeRate value in the DTO representation.
        :type hold_in_unit: ElectricPotentialChangeRateUnits
        :return: JSON object represents ElectricPotentialChangeRate DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "VoltPerSecond"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(electric_potential_change_rate_dto: ElectricPotentialChangeRateDto):
        """
        Obtain a new instance of ElectricPotentialChangeRate from a DTO unit object.

        :param electric_potential_change_rate_dto: The ElectricPotentialChangeRate DTO representation.
        :type electric_potential_change_rate_dto: ElectricPotentialChangeRateDto
        :return: A new instance of ElectricPotentialChangeRate.
        :rtype: ElectricPotentialChangeRate
        """
        return ElectricPotentialChangeRate(electric_potential_change_rate_dto.value, electric_potential_change_rate_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of ElectricPotentialChangeRate from a DTO unit json representation.

        :param data: The ElectricPotentialChangeRate DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "VoltPerSecond"}
        :return: A new instance of ElectricPotentialChangeRate.
        :rtype: ElectricPotentialChangeRate
        """
        return ElectricPotentialChangeRate.from_dto(ElectricPotentialChangeRateDto.from_json(data))

    def __convert_from_base(self, from_unit: ElectricPotentialChangeRateUnits) -> float:
        value = self._value
        
        if from_unit == ElectricPotentialChangeRateUnits.VoltPerSecond:
            return (value)
        
        if from_unit == ElectricPotentialChangeRateUnits.VoltPerMicrosecond:
            return (value / 1e6)
        
        if from_unit == ElectricPotentialChangeRateUnits.VoltPerMinute:
            return (value * 60)
        
        if from_unit == ElectricPotentialChangeRateUnits.VoltPerHour:
            return (value * 3600)
        
        if from_unit == ElectricPotentialChangeRateUnits.MicrovoltPerSecond:
            return ((value) / 1e-06)
        
        if from_unit == ElectricPotentialChangeRateUnits.MillivoltPerSecond:
            return ((value) / 0.001)
        
        if from_unit == ElectricPotentialChangeRateUnits.KilovoltPerSecond:
            return ((value) / 1000.0)
        
        if from_unit == ElectricPotentialChangeRateUnits.MegavoltPerSecond:
            return ((value) / 1000000.0)
        
        if from_unit == ElectricPotentialChangeRateUnits.MicrovoltPerMicrosecond:
            return ((value / 1e6) / 1e-06)
        
        if from_unit == ElectricPotentialChangeRateUnits.MillivoltPerMicrosecond:
            return ((value / 1e6) / 0.001)
        
        if from_unit == ElectricPotentialChangeRateUnits.KilovoltPerMicrosecond:
            return ((value / 1e6) / 1000.0)
        
        if from_unit == ElectricPotentialChangeRateUnits.MegavoltPerMicrosecond:
            return ((value / 1e6) / 1000000.0)
        
        if from_unit == ElectricPotentialChangeRateUnits.MicrovoltPerMinute:
            return ((value * 60) / 1e-06)
        
        if from_unit == ElectricPotentialChangeRateUnits.MillivoltPerMinute:
            return ((value * 60) / 0.001)
        
        if from_unit == ElectricPotentialChangeRateUnits.KilovoltPerMinute:
            return ((value * 60) / 1000.0)
        
        if from_unit == ElectricPotentialChangeRateUnits.MegavoltPerMinute:
            return ((value * 60) / 1000000.0)
        
        if from_unit == ElectricPotentialChangeRateUnits.MicrovoltPerHour:
            return ((value * 3600) / 1e-06)
        
        if from_unit == ElectricPotentialChangeRateUnits.MillivoltPerHour:
            return ((value * 3600) / 0.001)
        
        if from_unit == ElectricPotentialChangeRateUnits.KilovoltPerHour:
            return ((value * 3600) / 1000.0)
        
        if from_unit == ElectricPotentialChangeRateUnits.MegavoltPerHour:
            return ((value * 3600) / 1000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: ElectricPotentialChangeRateUnits) -> float:
        
        if to_unit == ElectricPotentialChangeRateUnits.VoltPerSecond:
            return (value)
        
        if to_unit == ElectricPotentialChangeRateUnits.VoltPerMicrosecond:
            return (value * 1e6)
        
        if to_unit == ElectricPotentialChangeRateUnits.VoltPerMinute:
            return (value / 60)
        
        if to_unit == ElectricPotentialChangeRateUnits.VoltPerHour:
            return (value / 3600)
        
        if to_unit == ElectricPotentialChangeRateUnits.MicrovoltPerSecond:
            return ((value) * 1e-06)
        
        if to_unit == ElectricPotentialChangeRateUnits.MillivoltPerSecond:
            return ((value) * 0.001)
        
        if to_unit == ElectricPotentialChangeRateUnits.KilovoltPerSecond:
            return ((value) * 1000.0)
        
        if to_unit == ElectricPotentialChangeRateUnits.MegavoltPerSecond:
            return ((value) * 1000000.0)
        
        if to_unit == ElectricPotentialChangeRateUnits.MicrovoltPerMicrosecond:
            return ((value * 1e6) * 1e-06)
        
        if to_unit == ElectricPotentialChangeRateUnits.MillivoltPerMicrosecond:
            return ((value * 1e6) * 0.001)
        
        if to_unit == ElectricPotentialChangeRateUnits.KilovoltPerMicrosecond:
            return ((value * 1e6) * 1000.0)
        
        if to_unit == ElectricPotentialChangeRateUnits.MegavoltPerMicrosecond:
            return ((value * 1e6) * 1000000.0)
        
        if to_unit == ElectricPotentialChangeRateUnits.MicrovoltPerMinute:
            return ((value / 60) * 1e-06)
        
        if to_unit == ElectricPotentialChangeRateUnits.MillivoltPerMinute:
            return ((value / 60) * 0.001)
        
        if to_unit == ElectricPotentialChangeRateUnits.KilovoltPerMinute:
            return ((value / 60) * 1000.0)
        
        if to_unit == ElectricPotentialChangeRateUnits.MegavoltPerMinute:
            return ((value / 60) * 1000000.0)
        
        if to_unit == ElectricPotentialChangeRateUnits.MicrovoltPerHour:
            return ((value / 3600) * 1e-06)
        
        if to_unit == ElectricPotentialChangeRateUnits.MillivoltPerHour:
            return ((value / 3600) * 0.001)
        
        if to_unit == ElectricPotentialChangeRateUnits.KilovoltPerHour:
            return ((value / 3600) * 1000.0)
        
        if to_unit == ElectricPotentialChangeRateUnits.MegavoltPerHour:
            return ((value / 3600) * 1000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_volts_per_second(volts_per_second: float):
        """
        Create a new instance of ElectricPotentialChangeRate from a value in volts_per_second.

        

        :param meters: The ElectricPotentialChangeRate value in volts_per_second.
        :type volts_per_second: float
        :return: A new instance of ElectricPotentialChangeRate.
        :rtype: ElectricPotentialChangeRate
        """
        return ElectricPotentialChangeRate(volts_per_second, ElectricPotentialChangeRateUnits.VoltPerSecond)

    
    @staticmethod
    def from_volts_per_microsecond(volts_per_microsecond: float):
        """
        Create a new instance of ElectricPotentialChangeRate from a value in volts_per_microsecond.

        

        :param meters: The ElectricPotentialChangeRate value in volts_per_microsecond.
        :type volts_per_microsecond: float
        :return: A new instance of ElectricPotentialChangeRate.
        :rtype: ElectricPotentialChangeRate
        """
        return ElectricPotentialChangeRate(volts_per_microsecond, ElectricPotentialChangeRateUnits.VoltPerMicrosecond)

    
    @staticmethod
    def from_volts_per_minute(volts_per_minute: float):
        """
        Create a new instance of ElectricPotentialChangeRate from a value in volts_per_minute.

        

        :param meters: The ElectricPotentialChangeRate value in volts_per_minute.
        :type volts_per_minute: float
        :return: A new instance of ElectricPotentialChangeRate.
        :rtype: ElectricPotentialChangeRate
        """
        return ElectricPotentialChangeRate(volts_per_minute, ElectricPotentialChangeRateUnits.VoltPerMinute)

    
    @staticmethod
    def from_volts_per_hour(volts_per_hour: float):
        """
        Create a new instance of ElectricPotentialChangeRate from a value in volts_per_hour.

        

        :param meters: The ElectricPotentialChangeRate value in volts_per_hour.
        :type volts_per_hour: float
        :return: A new instance of ElectricPotentialChangeRate.
        :rtype: ElectricPotentialChangeRate
        """
        return ElectricPotentialChangeRate(volts_per_hour, ElectricPotentialChangeRateUnits.VoltPerHour)

    
    @staticmethod
    def from_microvolts_per_second(microvolts_per_second: float):
        """
        Create a new instance of ElectricPotentialChangeRate from a value in microvolts_per_second.

        

        :param meters: The ElectricPotentialChangeRate value in microvolts_per_second.
        :type microvolts_per_second: float
        :return: A new instance of ElectricPotentialChangeRate.
        :rtype: ElectricPotentialChangeRate
        """
        return ElectricPotentialChangeRate(microvolts_per_second, ElectricPotentialChangeRateUnits.MicrovoltPerSecond)

    
    @staticmethod
    def from_millivolts_per_second(millivolts_per_second: float):
        """
        Create a new instance of ElectricPotentialChangeRate from a value in millivolts_per_second.

        

        :param meters: The ElectricPotentialChangeRate value in millivolts_per_second.
        :type millivolts_per_second: float
        :return: A new instance of ElectricPotentialChangeRate.
        :rtype: ElectricPotentialChangeRate
        """
        return ElectricPotentialChangeRate(millivolts_per_second, ElectricPotentialChangeRateUnits.MillivoltPerSecond)

    
    @staticmethod
    def from_kilovolts_per_second(kilovolts_per_second: float):
        """
        Create a new instance of ElectricPotentialChangeRate from a value in kilovolts_per_second.

        

        :param meters: The ElectricPotentialChangeRate value in kilovolts_per_second.
        :type kilovolts_per_second: float
        :return: A new instance of ElectricPotentialChangeRate.
        :rtype: ElectricPotentialChangeRate
        """
        return ElectricPotentialChangeRate(kilovolts_per_second, ElectricPotentialChangeRateUnits.KilovoltPerSecond)

    
    @staticmethod
    def from_megavolts_per_second(megavolts_per_second: float):
        """
        Create a new instance of ElectricPotentialChangeRate from a value in megavolts_per_second.

        

        :param meters: The ElectricPotentialChangeRate value in megavolts_per_second.
        :type megavolts_per_second: float
        :return: A new instance of ElectricPotentialChangeRate.
        :rtype: ElectricPotentialChangeRate
        """
        return ElectricPotentialChangeRate(megavolts_per_second, ElectricPotentialChangeRateUnits.MegavoltPerSecond)

    
    @staticmethod
    def from_microvolts_per_microsecond(microvolts_per_microsecond: float):
        """
        Create a new instance of ElectricPotentialChangeRate from a value in microvolts_per_microsecond.

        

        :param meters: The ElectricPotentialChangeRate value in microvolts_per_microsecond.
        :type microvolts_per_microsecond: float
        :return: A new instance of ElectricPotentialChangeRate.
        :rtype: ElectricPotentialChangeRate
        """
        return ElectricPotentialChangeRate(microvolts_per_microsecond, ElectricPotentialChangeRateUnits.MicrovoltPerMicrosecond)

    
    @staticmethod
    def from_millivolts_per_microsecond(millivolts_per_microsecond: float):
        """
        Create a new instance of ElectricPotentialChangeRate from a value in millivolts_per_microsecond.

        

        :param meters: The ElectricPotentialChangeRate value in millivolts_per_microsecond.
        :type millivolts_per_microsecond: float
        :return: A new instance of ElectricPotentialChangeRate.
        :rtype: ElectricPotentialChangeRate
        """
        return ElectricPotentialChangeRate(millivolts_per_microsecond, ElectricPotentialChangeRateUnits.MillivoltPerMicrosecond)

    
    @staticmethod
    def from_kilovolts_per_microsecond(kilovolts_per_microsecond: float):
        """
        Create a new instance of ElectricPotentialChangeRate from a value in kilovolts_per_microsecond.

        

        :param meters: The ElectricPotentialChangeRate value in kilovolts_per_microsecond.
        :type kilovolts_per_microsecond: float
        :return: A new instance of ElectricPotentialChangeRate.
        :rtype: ElectricPotentialChangeRate
        """
        return ElectricPotentialChangeRate(kilovolts_per_microsecond, ElectricPotentialChangeRateUnits.KilovoltPerMicrosecond)

    
    @staticmethod
    def from_megavolts_per_microsecond(megavolts_per_microsecond: float):
        """
        Create a new instance of ElectricPotentialChangeRate from a value in megavolts_per_microsecond.

        

        :param meters: The ElectricPotentialChangeRate value in megavolts_per_microsecond.
        :type megavolts_per_microsecond: float
        :return: A new instance of ElectricPotentialChangeRate.
        :rtype: ElectricPotentialChangeRate
        """
        return ElectricPotentialChangeRate(megavolts_per_microsecond, ElectricPotentialChangeRateUnits.MegavoltPerMicrosecond)

    
    @staticmethod
    def from_microvolts_per_minute(microvolts_per_minute: float):
        """
        Create a new instance of ElectricPotentialChangeRate from a value in microvolts_per_minute.

        

        :param meters: The ElectricPotentialChangeRate value in microvolts_per_minute.
        :type microvolts_per_minute: float
        :return: A new instance of ElectricPotentialChangeRate.
        :rtype: ElectricPotentialChangeRate
        """
        return ElectricPotentialChangeRate(microvolts_per_minute, ElectricPotentialChangeRateUnits.MicrovoltPerMinute)

    
    @staticmethod
    def from_millivolts_per_minute(millivolts_per_minute: float):
        """
        Create a new instance of ElectricPotentialChangeRate from a value in millivolts_per_minute.

        

        :param meters: The ElectricPotentialChangeRate value in millivolts_per_minute.
        :type millivolts_per_minute: float
        :return: A new instance of ElectricPotentialChangeRate.
        :rtype: ElectricPotentialChangeRate
        """
        return ElectricPotentialChangeRate(millivolts_per_minute, ElectricPotentialChangeRateUnits.MillivoltPerMinute)

    
    @staticmethod
    def from_kilovolts_per_minute(kilovolts_per_minute: float):
        """
        Create a new instance of ElectricPotentialChangeRate from a value in kilovolts_per_minute.

        

        :param meters: The ElectricPotentialChangeRate value in kilovolts_per_minute.
        :type kilovolts_per_minute: float
        :return: A new instance of ElectricPotentialChangeRate.
        :rtype: ElectricPotentialChangeRate
        """
        return ElectricPotentialChangeRate(kilovolts_per_minute, ElectricPotentialChangeRateUnits.KilovoltPerMinute)

    
    @staticmethod
    def from_megavolts_per_minute(megavolts_per_minute: float):
        """
        Create a new instance of ElectricPotentialChangeRate from a value in megavolts_per_minute.

        

        :param meters: The ElectricPotentialChangeRate value in megavolts_per_minute.
        :type megavolts_per_minute: float
        :return: A new instance of ElectricPotentialChangeRate.
        :rtype: ElectricPotentialChangeRate
        """
        return ElectricPotentialChangeRate(megavolts_per_minute, ElectricPotentialChangeRateUnits.MegavoltPerMinute)

    
    @staticmethod
    def from_microvolts_per_hour(microvolts_per_hour: float):
        """
        Create a new instance of ElectricPotentialChangeRate from a value in microvolts_per_hour.

        

        :param meters: The ElectricPotentialChangeRate value in microvolts_per_hour.
        :type microvolts_per_hour: float
        :return: A new instance of ElectricPotentialChangeRate.
        :rtype: ElectricPotentialChangeRate
        """
        return ElectricPotentialChangeRate(microvolts_per_hour, ElectricPotentialChangeRateUnits.MicrovoltPerHour)

    
    @staticmethod
    def from_millivolts_per_hour(millivolts_per_hour: float):
        """
        Create a new instance of ElectricPotentialChangeRate from a value in millivolts_per_hour.

        

        :param meters: The ElectricPotentialChangeRate value in millivolts_per_hour.
        :type millivolts_per_hour: float
        :return: A new instance of ElectricPotentialChangeRate.
        :rtype: ElectricPotentialChangeRate
        """
        return ElectricPotentialChangeRate(millivolts_per_hour, ElectricPotentialChangeRateUnits.MillivoltPerHour)

    
    @staticmethod
    def from_kilovolts_per_hour(kilovolts_per_hour: float):
        """
        Create a new instance of ElectricPotentialChangeRate from a value in kilovolts_per_hour.

        

        :param meters: The ElectricPotentialChangeRate value in kilovolts_per_hour.
        :type kilovolts_per_hour: float
        :return: A new instance of ElectricPotentialChangeRate.
        :rtype: ElectricPotentialChangeRate
        """
        return ElectricPotentialChangeRate(kilovolts_per_hour, ElectricPotentialChangeRateUnits.KilovoltPerHour)

    
    @staticmethod
    def from_megavolts_per_hour(megavolts_per_hour: float):
        """
        Create a new instance of ElectricPotentialChangeRate from a value in megavolts_per_hour.

        

        :param meters: The ElectricPotentialChangeRate value in megavolts_per_hour.
        :type megavolts_per_hour: float
        :return: A new instance of ElectricPotentialChangeRate.
        :rtype: ElectricPotentialChangeRate
        """
        return ElectricPotentialChangeRate(megavolts_per_hour, ElectricPotentialChangeRateUnits.MegavoltPerHour)

    
    @property
    def volts_per_second(self) -> float:
        """
        
        """
        if self.__volts_per_second != None:
            return self.__volts_per_second
        self.__volts_per_second = self.__convert_from_base(ElectricPotentialChangeRateUnits.VoltPerSecond)
        return self.__volts_per_second

    
    @property
    def volts_per_microsecond(self) -> float:
        """
        
        """
        if self.__volts_per_microsecond != None:
            return self.__volts_per_microsecond
        self.__volts_per_microsecond = self.__convert_from_base(ElectricPotentialChangeRateUnits.VoltPerMicrosecond)
        return self.__volts_per_microsecond

    
    @property
    def volts_per_minute(self) -> float:
        """
        
        """
        if self.__volts_per_minute != None:
            return self.__volts_per_minute
        self.__volts_per_minute = self.__convert_from_base(ElectricPotentialChangeRateUnits.VoltPerMinute)
        return self.__volts_per_minute

    
    @property
    def volts_per_hour(self) -> float:
        """
        
        """
        if self.__volts_per_hour != None:
            return self.__volts_per_hour
        self.__volts_per_hour = self.__convert_from_base(ElectricPotentialChangeRateUnits.VoltPerHour)
        return self.__volts_per_hour

    
    @property
    def microvolts_per_second(self) -> float:
        """
        
        """
        if self.__microvolts_per_second != None:
            return self.__microvolts_per_second
        self.__microvolts_per_second = self.__convert_from_base(ElectricPotentialChangeRateUnits.MicrovoltPerSecond)
        return self.__microvolts_per_second

    
    @property
    def millivolts_per_second(self) -> float:
        """
        
        """
        if self.__millivolts_per_second != None:
            return self.__millivolts_per_second
        self.__millivolts_per_second = self.__convert_from_base(ElectricPotentialChangeRateUnits.MillivoltPerSecond)
        return self.__millivolts_per_second

    
    @property
    def kilovolts_per_second(self) -> float:
        """
        
        """
        if self.__kilovolts_per_second != None:
            return self.__kilovolts_per_second
        self.__kilovolts_per_second = self.__convert_from_base(ElectricPotentialChangeRateUnits.KilovoltPerSecond)
        return self.__kilovolts_per_second

    
    @property
    def megavolts_per_second(self) -> float:
        """
        
        """
        if self.__megavolts_per_second != None:
            return self.__megavolts_per_second
        self.__megavolts_per_second = self.__convert_from_base(ElectricPotentialChangeRateUnits.MegavoltPerSecond)
        return self.__megavolts_per_second

    
    @property
    def microvolts_per_microsecond(self) -> float:
        """
        
        """
        if self.__microvolts_per_microsecond != None:
            return self.__microvolts_per_microsecond
        self.__microvolts_per_microsecond = self.__convert_from_base(ElectricPotentialChangeRateUnits.MicrovoltPerMicrosecond)
        return self.__microvolts_per_microsecond

    
    @property
    def millivolts_per_microsecond(self) -> float:
        """
        
        """
        if self.__millivolts_per_microsecond != None:
            return self.__millivolts_per_microsecond
        self.__millivolts_per_microsecond = self.__convert_from_base(ElectricPotentialChangeRateUnits.MillivoltPerMicrosecond)
        return self.__millivolts_per_microsecond

    
    @property
    def kilovolts_per_microsecond(self) -> float:
        """
        
        """
        if self.__kilovolts_per_microsecond != None:
            return self.__kilovolts_per_microsecond
        self.__kilovolts_per_microsecond = self.__convert_from_base(ElectricPotentialChangeRateUnits.KilovoltPerMicrosecond)
        return self.__kilovolts_per_microsecond

    
    @property
    def megavolts_per_microsecond(self) -> float:
        """
        
        """
        if self.__megavolts_per_microsecond != None:
            return self.__megavolts_per_microsecond
        self.__megavolts_per_microsecond = self.__convert_from_base(ElectricPotentialChangeRateUnits.MegavoltPerMicrosecond)
        return self.__megavolts_per_microsecond

    
    @property
    def microvolts_per_minute(self) -> float:
        """
        
        """
        if self.__microvolts_per_minute != None:
            return self.__microvolts_per_minute
        self.__microvolts_per_minute = self.__convert_from_base(ElectricPotentialChangeRateUnits.MicrovoltPerMinute)
        return self.__microvolts_per_minute

    
    @property
    def millivolts_per_minute(self) -> float:
        """
        
        """
        if self.__millivolts_per_minute != None:
            return self.__millivolts_per_minute
        self.__millivolts_per_minute = self.__convert_from_base(ElectricPotentialChangeRateUnits.MillivoltPerMinute)
        return self.__millivolts_per_minute

    
    @property
    def kilovolts_per_minute(self) -> float:
        """
        
        """
        if self.__kilovolts_per_minute != None:
            return self.__kilovolts_per_minute
        self.__kilovolts_per_minute = self.__convert_from_base(ElectricPotentialChangeRateUnits.KilovoltPerMinute)
        return self.__kilovolts_per_minute

    
    @property
    def megavolts_per_minute(self) -> float:
        """
        
        """
        if self.__megavolts_per_minute != None:
            return self.__megavolts_per_minute
        self.__megavolts_per_minute = self.__convert_from_base(ElectricPotentialChangeRateUnits.MegavoltPerMinute)
        return self.__megavolts_per_minute

    
    @property
    def microvolts_per_hour(self) -> float:
        """
        
        """
        if self.__microvolts_per_hour != None:
            return self.__microvolts_per_hour
        self.__microvolts_per_hour = self.__convert_from_base(ElectricPotentialChangeRateUnits.MicrovoltPerHour)
        return self.__microvolts_per_hour

    
    @property
    def millivolts_per_hour(self) -> float:
        """
        
        """
        if self.__millivolts_per_hour != None:
            return self.__millivolts_per_hour
        self.__millivolts_per_hour = self.__convert_from_base(ElectricPotentialChangeRateUnits.MillivoltPerHour)
        return self.__millivolts_per_hour

    
    @property
    def kilovolts_per_hour(self) -> float:
        """
        
        """
        if self.__kilovolts_per_hour != None:
            return self.__kilovolts_per_hour
        self.__kilovolts_per_hour = self.__convert_from_base(ElectricPotentialChangeRateUnits.KilovoltPerHour)
        return self.__kilovolts_per_hour

    
    @property
    def megavolts_per_hour(self) -> float:
        """
        
        """
        if self.__megavolts_per_hour != None:
            return self.__megavolts_per_hour
        self.__megavolts_per_hour = self.__convert_from_base(ElectricPotentialChangeRateUnits.MegavoltPerHour)
        return self.__megavolts_per_hour

    
    def to_string(self, unit: ElectricPotentialChangeRateUnits = ElectricPotentialChangeRateUnits.VoltPerSecond, fractional_digits: int = None) -> str:
        """
        Format the ElectricPotentialChangeRate to a string.
        
        Note: the default format for ElectricPotentialChangeRate is VoltPerSecond.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the ElectricPotentialChangeRate. Default is 'VoltPerSecond'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == ElectricPotentialChangeRateUnits.VoltPerSecond:
            return f"""{super()._truncate_fraction_digits(self.volts_per_second, fractional_digits)} V/s"""
        
        if unit == ElectricPotentialChangeRateUnits.VoltPerMicrosecond:
            return f"""{super()._truncate_fraction_digits(self.volts_per_microsecond, fractional_digits)} V/μs"""
        
        if unit == ElectricPotentialChangeRateUnits.VoltPerMinute:
            return f"""{super()._truncate_fraction_digits(self.volts_per_minute, fractional_digits)} V/min"""
        
        if unit == ElectricPotentialChangeRateUnits.VoltPerHour:
            return f"""{super()._truncate_fraction_digits(self.volts_per_hour, fractional_digits)} V/h"""
        
        if unit == ElectricPotentialChangeRateUnits.MicrovoltPerSecond:
            return f"""{super()._truncate_fraction_digits(self.microvolts_per_second, fractional_digits)} μV/s"""
        
        if unit == ElectricPotentialChangeRateUnits.MillivoltPerSecond:
            return f"""{super()._truncate_fraction_digits(self.millivolts_per_second, fractional_digits)} mV/s"""
        
        if unit == ElectricPotentialChangeRateUnits.KilovoltPerSecond:
            return f"""{super()._truncate_fraction_digits(self.kilovolts_per_second, fractional_digits)} kV/s"""
        
        if unit == ElectricPotentialChangeRateUnits.MegavoltPerSecond:
            return f"""{super()._truncate_fraction_digits(self.megavolts_per_second, fractional_digits)} MV/s"""
        
        if unit == ElectricPotentialChangeRateUnits.MicrovoltPerMicrosecond:
            return f"""{super()._truncate_fraction_digits(self.microvolts_per_microsecond, fractional_digits)} μV/μs"""
        
        if unit == ElectricPotentialChangeRateUnits.MillivoltPerMicrosecond:
            return f"""{super()._truncate_fraction_digits(self.millivolts_per_microsecond, fractional_digits)} mV/μs"""
        
        if unit == ElectricPotentialChangeRateUnits.KilovoltPerMicrosecond:
            return f"""{super()._truncate_fraction_digits(self.kilovolts_per_microsecond, fractional_digits)} kV/μs"""
        
        if unit == ElectricPotentialChangeRateUnits.MegavoltPerMicrosecond:
            return f"""{super()._truncate_fraction_digits(self.megavolts_per_microsecond, fractional_digits)} MV/μs"""
        
        if unit == ElectricPotentialChangeRateUnits.MicrovoltPerMinute:
            return f"""{super()._truncate_fraction_digits(self.microvolts_per_minute, fractional_digits)} μV/min"""
        
        if unit == ElectricPotentialChangeRateUnits.MillivoltPerMinute:
            return f"""{super()._truncate_fraction_digits(self.millivolts_per_minute, fractional_digits)} mV/min"""
        
        if unit == ElectricPotentialChangeRateUnits.KilovoltPerMinute:
            return f"""{super()._truncate_fraction_digits(self.kilovolts_per_minute, fractional_digits)} kV/min"""
        
        if unit == ElectricPotentialChangeRateUnits.MegavoltPerMinute:
            return f"""{super()._truncate_fraction_digits(self.megavolts_per_minute, fractional_digits)} MV/min"""
        
        if unit == ElectricPotentialChangeRateUnits.MicrovoltPerHour:
            return f"""{super()._truncate_fraction_digits(self.microvolts_per_hour, fractional_digits)} μV/h"""
        
        if unit == ElectricPotentialChangeRateUnits.MillivoltPerHour:
            return f"""{super()._truncate_fraction_digits(self.millivolts_per_hour, fractional_digits)} mV/h"""
        
        if unit == ElectricPotentialChangeRateUnits.KilovoltPerHour:
            return f"""{super()._truncate_fraction_digits(self.kilovolts_per_hour, fractional_digits)} kV/h"""
        
        if unit == ElectricPotentialChangeRateUnits.MegavoltPerHour:
            return f"""{super()._truncate_fraction_digits(self.megavolts_per_hour, fractional_digits)} MV/h"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: ElectricPotentialChangeRateUnits = ElectricPotentialChangeRateUnits.VoltPerSecond) -> str:
        """
        Get ElectricPotentialChangeRate unit abbreviation.
        Note! the default abbreviation for ElectricPotentialChangeRate is VoltPerSecond.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == ElectricPotentialChangeRateUnits.VoltPerSecond:
            return """V/s"""
        
        if unit_abbreviation == ElectricPotentialChangeRateUnits.VoltPerMicrosecond:
            return """V/μs"""
        
        if unit_abbreviation == ElectricPotentialChangeRateUnits.VoltPerMinute:
            return """V/min"""
        
        if unit_abbreviation == ElectricPotentialChangeRateUnits.VoltPerHour:
            return """V/h"""
        
        if unit_abbreviation == ElectricPotentialChangeRateUnits.MicrovoltPerSecond:
            return """μV/s"""
        
        if unit_abbreviation == ElectricPotentialChangeRateUnits.MillivoltPerSecond:
            return """mV/s"""
        
        if unit_abbreviation == ElectricPotentialChangeRateUnits.KilovoltPerSecond:
            return """kV/s"""
        
        if unit_abbreviation == ElectricPotentialChangeRateUnits.MegavoltPerSecond:
            return """MV/s"""
        
        if unit_abbreviation == ElectricPotentialChangeRateUnits.MicrovoltPerMicrosecond:
            return """μV/μs"""
        
        if unit_abbreviation == ElectricPotentialChangeRateUnits.MillivoltPerMicrosecond:
            return """mV/μs"""
        
        if unit_abbreviation == ElectricPotentialChangeRateUnits.KilovoltPerMicrosecond:
            return """kV/μs"""
        
        if unit_abbreviation == ElectricPotentialChangeRateUnits.MegavoltPerMicrosecond:
            return """MV/μs"""
        
        if unit_abbreviation == ElectricPotentialChangeRateUnits.MicrovoltPerMinute:
            return """μV/min"""
        
        if unit_abbreviation == ElectricPotentialChangeRateUnits.MillivoltPerMinute:
            return """mV/min"""
        
        if unit_abbreviation == ElectricPotentialChangeRateUnits.KilovoltPerMinute:
            return """kV/min"""
        
        if unit_abbreviation == ElectricPotentialChangeRateUnits.MegavoltPerMinute:
            return """MV/min"""
        
        if unit_abbreviation == ElectricPotentialChangeRateUnits.MicrovoltPerHour:
            return """μV/h"""
        
        if unit_abbreviation == ElectricPotentialChangeRateUnits.MillivoltPerHour:
            return """mV/h"""
        
        if unit_abbreviation == ElectricPotentialChangeRateUnits.KilovoltPerHour:
            return """kV/h"""
        
        if unit_abbreviation == ElectricPotentialChangeRateUnits.MegavoltPerHour:
            return """MV/h"""
        
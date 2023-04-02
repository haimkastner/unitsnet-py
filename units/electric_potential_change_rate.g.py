from enum import Enum
import math
import string


class ElectricPotentialChangeRateUnits(Enum):
        """
            ElectricPotentialChangeRateUnits enumeration
        """
        
        VoltPerSecond = 'volt_per_second'
        """
            
        """
        
        VoltPerMicrosecond = 'volt_per_microsecond'
        """
            
        """
        
        VoltPerMinute = 'volt_per_minute'
        """
            
        """
        
        VoltPerHour = 'volt_per_hour'
        """
            
        """
        
        MicroVoltPerSecond = 'micro_volt_per_second'
        """
            
        """
        
        MilliVoltPerSecond = 'milli_volt_per_second'
        """
            
        """
        
        KiloVoltPerSecond = 'kilo_volt_per_second'
        """
            
        """
        
        MegaVoltPerSecond = 'mega_volt_per_second'
        """
            
        """
        
        MicroVoltPerMicrosecond = 'micro_volt_per_microsecond'
        """
            
        """
        
        MilliVoltPerMicrosecond = 'milli_volt_per_microsecond'
        """
            
        """
        
        KiloVoltPerMicrosecond = 'kilo_volt_per_microsecond'
        """
            
        """
        
        MegaVoltPerMicrosecond = 'mega_volt_per_microsecond'
        """
            
        """
        
        MicroVoltPerMinute = 'micro_volt_per_minute'
        """
            
        """
        
        MilliVoltPerMinute = 'milli_volt_per_minute'
        """
            
        """
        
        KiloVoltPerMinute = 'kilo_volt_per_minute'
        """
            
        """
        
        MegaVoltPerMinute = 'mega_volt_per_minute'
        """
            
        """
        
        MicroVoltPerHour = 'micro_volt_per_hour'
        """
            
        """
        
        MilliVoltPerHour = 'milli_volt_per_hour'
        """
            
        """
        
        KiloVoltPerHour = 'kilo_volt_per_hour'
        """
            
        """
        
        MegaVoltPerHour = 'mega_volt_per_hour'
        """
            
        """
        
    
class ElectricPotentialChangeRate:
    """
    ElectricPotential change rate is the ratio of the electric potential change to the time during which the change occurred (value of electric potential changes per unit time).

    Args:
        value (float): The value.
        from_unit (ElectricPotentialChangeRateUnits): The ElectricPotentialChangeRate unit to create from, The default unit is VoltPerSecond
    """
    def __init__(self, value: float, from_unit: ElectricPotentialChangeRateUnits = ElectricPotentialChangeRateUnits.VoltPerSecond):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__volts_per_seconds = None
        
        self.__volts_per_microseconds = None
        
        self.__volts_per_minutes = None
        
        self.__volts_per_hours = None
        
        self.__micro_volts_per_seconds = None
        
        self.__milli_volts_per_seconds = None
        
        self.__kilo_volts_per_seconds = None
        
        self.__mega_volts_per_seconds = None
        
        self.__micro_volts_per_microseconds = None
        
        self.__milli_volts_per_microseconds = None
        
        self.__kilo_volts_per_microseconds = None
        
        self.__mega_volts_per_microseconds = None
        
        self.__micro_volts_per_minutes = None
        
        self.__milli_volts_per_minutes = None
        
        self.__kilo_volts_per_minutes = None
        
        self.__mega_volts_per_minutes = None
        
        self.__micro_volts_per_hours = None
        
        self.__milli_volts_per_hours = None
        
        self.__kilo_volts_per_hours = None
        
        self.__mega_volts_per_hours = None
        

    def __convert_from_base(self, from_unit: ElectricPotentialChangeRateUnits) -> float:
        value = self.__value
        
        if from_unit == ElectricPotentialChangeRateUnits.VoltPerSecond:
            return (value)
        
        if from_unit == ElectricPotentialChangeRateUnits.VoltPerMicrosecond:
            return (value / 1e6)
        
        if from_unit == ElectricPotentialChangeRateUnits.VoltPerMinute:
            return (value * 60)
        
        if from_unit == ElectricPotentialChangeRateUnits.VoltPerHour:
            return (value * 3600)
        
        if from_unit == ElectricPotentialChangeRateUnits.MicroVoltPerSecond:
            return ((value) / 1e-06)
        
        if from_unit == ElectricPotentialChangeRateUnits.MilliVoltPerSecond:
            return ((value) / 0.001)
        
        if from_unit == ElectricPotentialChangeRateUnits.KiloVoltPerSecond:
            return ((value) / 1000.0)
        
        if from_unit == ElectricPotentialChangeRateUnits.MegaVoltPerSecond:
            return ((value) / 1000000.0)
        
        if from_unit == ElectricPotentialChangeRateUnits.MicroVoltPerMicrosecond:
            return ((value / 1e6) / 1e-06)
        
        if from_unit == ElectricPotentialChangeRateUnits.MilliVoltPerMicrosecond:
            return ((value / 1e6) / 0.001)
        
        if from_unit == ElectricPotentialChangeRateUnits.KiloVoltPerMicrosecond:
            return ((value / 1e6) / 1000.0)
        
        if from_unit == ElectricPotentialChangeRateUnits.MegaVoltPerMicrosecond:
            return ((value / 1e6) / 1000000.0)
        
        if from_unit == ElectricPotentialChangeRateUnits.MicroVoltPerMinute:
            return ((value * 60) / 1e-06)
        
        if from_unit == ElectricPotentialChangeRateUnits.MilliVoltPerMinute:
            return ((value * 60) / 0.001)
        
        if from_unit == ElectricPotentialChangeRateUnits.KiloVoltPerMinute:
            return ((value * 60) / 1000.0)
        
        if from_unit == ElectricPotentialChangeRateUnits.MegaVoltPerMinute:
            return ((value * 60) / 1000000.0)
        
        if from_unit == ElectricPotentialChangeRateUnits.MicroVoltPerHour:
            return ((value * 3600) / 1e-06)
        
        if from_unit == ElectricPotentialChangeRateUnits.MilliVoltPerHour:
            return ((value * 3600) / 0.001)
        
        if from_unit == ElectricPotentialChangeRateUnits.KiloVoltPerHour:
            return ((value * 3600) / 1000.0)
        
        if from_unit == ElectricPotentialChangeRateUnits.MegaVoltPerHour:
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
        
        if to_unit == ElectricPotentialChangeRateUnits.MicroVoltPerSecond:
            return ((value) * 1e-06)
        
        if to_unit == ElectricPotentialChangeRateUnits.MilliVoltPerSecond:
            return ((value) * 0.001)
        
        if to_unit == ElectricPotentialChangeRateUnits.KiloVoltPerSecond:
            return ((value) * 1000.0)
        
        if to_unit == ElectricPotentialChangeRateUnits.MegaVoltPerSecond:
            return ((value) * 1000000.0)
        
        if to_unit == ElectricPotentialChangeRateUnits.MicroVoltPerMicrosecond:
            return ((value * 1e6) * 1e-06)
        
        if to_unit == ElectricPotentialChangeRateUnits.MilliVoltPerMicrosecond:
            return ((value * 1e6) * 0.001)
        
        if to_unit == ElectricPotentialChangeRateUnits.KiloVoltPerMicrosecond:
            return ((value * 1e6) * 1000.0)
        
        if to_unit == ElectricPotentialChangeRateUnits.MegaVoltPerMicrosecond:
            return ((value * 1e6) * 1000000.0)
        
        if to_unit == ElectricPotentialChangeRateUnits.MicroVoltPerMinute:
            return ((value / 60) * 1e-06)
        
        if to_unit == ElectricPotentialChangeRateUnits.MilliVoltPerMinute:
            return ((value / 60) * 0.001)
        
        if to_unit == ElectricPotentialChangeRateUnits.KiloVoltPerMinute:
            return ((value / 60) * 1000.0)
        
        if to_unit == ElectricPotentialChangeRateUnits.MegaVoltPerMinute:
            return ((value / 60) * 1000000.0)
        
        if to_unit == ElectricPotentialChangeRateUnits.MicroVoltPerHour:
            return ((value / 3600) * 1e-06)
        
        if to_unit == ElectricPotentialChangeRateUnits.MilliVoltPerHour:
            return ((value / 3600) * 0.001)
        
        if to_unit == ElectricPotentialChangeRateUnits.KiloVoltPerHour:
            return ((value / 3600) * 1000.0)
        
        if to_unit == ElectricPotentialChangeRateUnits.MegaVoltPerHour:
            return ((value / 3600) * 1000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
    @staticmethod
    def from_volts_per_seconds(volts_per_seconds: float):
        """
        Create a new instance of ElectricPotentialChangeRate from a value in volts_per_seconds.

        

        :param meters: The ElectricPotentialChangeRate value in volts_per_seconds.
        :type volts_per_seconds: float
        :return: A new instance of ElectricPotentialChangeRate.
        :rtype: ElectricPotentialChangeRate
        """
        return ElectricPotentialChangeRate(volts_per_seconds, ElectricPotentialChangeRateUnits.VoltPerSecond)

    
    @staticmethod
    def from_volts_per_microseconds(volts_per_microseconds: float):
        """
        Create a new instance of ElectricPotentialChangeRate from a value in volts_per_microseconds.

        

        :param meters: The ElectricPotentialChangeRate value in volts_per_microseconds.
        :type volts_per_microseconds: float
        :return: A new instance of ElectricPotentialChangeRate.
        :rtype: ElectricPotentialChangeRate
        """
        return ElectricPotentialChangeRate(volts_per_microseconds, ElectricPotentialChangeRateUnits.VoltPerMicrosecond)

    
    @staticmethod
    def from_volts_per_minutes(volts_per_minutes: float):
        """
        Create a new instance of ElectricPotentialChangeRate from a value in volts_per_minutes.

        

        :param meters: The ElectricPotentialChangeRate value in volts_per_minutes.
        :type volts_per_minutes: float
        :return: A new instance of ElectricPotentialChangeRate.
        :rtype: ElectricPotentialChangeRate
        """
        return ElectricPotentialChangeRate(volts_per_minutes, ElectricPotentialChangeRateUnits.VoltPerMinute)

    
    @staticmethod
    def from_volts_per_hours(volts_per_hours: float):
        """
        Create a new instance of ElectricPotentialChangeRate from a value in volts_per_hours.

        

        :param meters: The ElectricPotentialChangeRate value in volts_per_hours.
        :type volts_per_hours: float
        :return: A new instance of ElectricPotentialChangeRate.
        :rtype: ElectricPotentialChangeRate
        """
        return ElectricPotentialChangeRate(volts_per_hours, ElectricPotentialChangeRateUnits.VoltPerHour)

    
    @staticmethod
    def from_micro_volts_per_seconds(micro_volts_per_seconds: float):
        """
        Create a new instance of ElectricPotentialChangeRate from a value in micro_volts_per_seconds.

        

        :param meters: The ElectricPotentialChangeRate value in micro_volts_per_seconds.
        :type micro_volts_per_seconds: float
        :return: A new instance of ElectricPotentialChangeRate.
        :rtype: ElectricPotentialChangeRate
        """
        return ElectricPotentialChangeRate(micro_volts_per_seconds, ElectricPotentialChangeRateUnits.MicroVoltPerSecond)

    
    @staticmethod
    def from_milli_volts_per_seconds(milli_volts_per_seconds: float):
        """
        Create a new instance of ElectricPotentialChangeRate from a value in milli_volts_per_seconds.

        

        :param meters: The ElectricPotentialChangeRate value in milli_volts_per_seconds.
        :type milli_volts_per_seconds: float
        :return: A new instance of ElectricPotentialChangeRate.
        :rtype: ElectricPotentialChangeRate
        """
        return ElectricPotentialChangeRate(milli_volts_per_seconds, ElectricPotentialChangeRateUnits.MilliVoltPerSecond)

    
    @staticmethod
    def from_kilo_volts_per_seconds(kilo_volts_per_seconds: float):
        """
        Create a new instance of ElectricPotentialChangeRate from a value in kilo_volts_per_seconds.

        

        :param meters: The ElectricPotentialChangeRate value in kilo_volts_per_seconds.
        :type kilo_volts_per_seconds: float
        :return: A new instance of ElectricPotentialChangeRate.
        :rtype: ElectricPotentialChangeRate
        """
        return ElectricPotentialChangeRate(kilo_volts_per_seconds, ElectricPotentialChangeRateUnits.KiloVoltPerSecond)

    
    @staticmethod
    def from_mega_volts_per_seconds(mega_volts_per_seconds: float):
        """
        Create a new instance of ElectricPotentialChangeRate from a value in mega_volts_per_seconds.

        

        :param meters: The ElectricPotentialChangeRate value in mega_volts_per_seconds.
        :type mega_volts_per_seconds: float
        :return: A new instance of ElectricPotentialChangeRate.
        :rtype: ElectricPotentialChangeRate
        """
        return ElectricPotentialChangeRate(mega_volts_per_seconds, ElectricPotentialChangeRateUnits.MegaVoltPerSecond)

    
    @staticmethod
    def from_micro_volts_per_microseconds(micro_volts_per_microseconds: float):
        """
        Create a new instance of ElectricPotentialChangeRate from a value in micro_volts_per_microseconds.

        

        :param meters: The ElectricPotentialChangeRate value in micro_volts_per_microseconds.
        :type micro_volts_per_microseconds: float
        :return: A new instance of ElectricPotentialChangeRate.
        :rtype: ElectricPotentialChangeRate
        """
        return ElectricPotentialChangeRate(micro_volts_per_microseconds, ElectricPotentialChangeRateUnits.MicroVoltPerMicrosecond)

    
    @staticmethod
    def from_milli_volts_per_microseconds(milli_volts_per_microseconds: float):
        """
        Create a new instance of ElectricPotentialChangeRate from a value in milli_volts_per_microseconds.

        

        :param meters: The ElectricPotentialChangeRate value in milli_volts_per_microseconds.
        :type milli_volts_per_microseconds: float
        :return: A new instance of ElectricPotentialChangeRate.
        :rtype: ElectricPotentialChangeRate
        """
        return ElectricPotentialChangeRate(milli_volts_per_microseconds, ElectricPotentialChangeRateUnits.MilliVoltPerMicrosecond)

    
    @staticmethod
    def from_kilo_volts_per_microseconds(kilo_volts_per_microseconds: float):
        """
        Create a new instance of ElectricPotentialChangeRate from a value in kilo_volts_per_microseconds.

        

        :param meters: The ElectricPotentialChangeRate value in kilo_volts_per_microseconds.
        :type kilo_volts_per_microseconds: float
        :return: A new instance of ElectricPotentialChangeRate.
        :rtype: ElectricPotentialChangeRate
        """
        return ElectricPotentialChangeRate(kilo_volts_per_microseconds, ElectricPotentialChangeRateUnits.KiloVoltPerMicrosecond)

    
    @staticmethod
    def from_mega_volts_per_microseconds(mega_volts_per_microseconds: float):
        """
        Create a new instance of ElectricPotentialChangeRate from a value in mega_volts_per_microseconds.

        

        :param meters: The ElectricPotentialChangeRate value in mega_volts_per_microseconds.
        :type mega_volts_per_microseconds: float
        :return: A new instance of ElectricPotentialChangeRate.
        :rtype: ElectricPotentialChangeRate
        """
        return ElectricPotentialChangeRate(mega_volts_per_microseconds, ElectricPotentialChangeRateUnits.MegaVoltPerMicrosecond)

    
    @staticmethod
    def from_micro_volts_per_minutes(micro_volts_per_minutes: float):
        """
        Create a new instance of ElectricPotentialChangeRate from a value in micro_volts_per_minutes.

        

        :param meters: The ElectricPotentialChangeRate value in micro_volts_per_minutes.
        :type micro_volts_per_minutes: float
        :return: A new instance of ElectricPotentialChangeRate.
        :rtype: ElectricPotentialChangeRate
        """
        return ElectricPotentialChangeRate(micro_volts_per_minutes, ElectricPotentialChangeRateUnits.MicroVoltPerMinute)

    
    @staticmethod
    def from_milli_volts_per_minutes(milli_volts_per_minutes: float):
        """
        Create a new instance of ElectricPotentialChangeRate from a value in milli_volts_per_minutes.

        

        :param meters: The ElectricPotentialChangeRate value in milli_volts_per_minutes.
        :type milli_volts_per_minutes: float
        :return: A new instance of ElectricPotentialChangeRate.
        :rtype: ElectricPotentialChangeRate
        """
        return ElectricPotentialChangeRate(milli_volts_per_minutes, ElectricPotentialChangeRateUnits.MilliVoltPerMinute)

    
    @staticmethod
    def from_kilo_volts_per_minutes(kilo_volts_per_minutes: float):
        """
        Create a new instance of ElectricPotentialChangeRate from a value in kilo_volts_per_minutes.

        

        :param meters: The ElectricPotentialChangeRate value in kilo_volts_per_minutes.
        :type kilo_volts_per_minutes: float
        :return: A new instance of ElectricPotentialChangeRate.
        :rtype: ElectricPotentialChangeRate
        """
        return ElectricPotentialChangeRate(kilo_volts_per_minutes, ElectricPotentialChangeRateUnits.KiloVoltPerMinute)

    
    @staticmethod
    def from_mega_volts_per_minutes(mega_volts_per_minutes: float):
        """
        Create a new instance of ElectricPotentialChangeRate from a value in mega_volts_per_minutes.

        

        :param meters: The ElectricPotentialChangeRate value in mega_volts_per_minutes.
        :type mega_volts_per_minutes: float
        :return: A new instance of ElectricPotentialChangeRate.
        :rtype: ElectricPotentialChangeRate
        """
        return ElectricPotentialChangeRate(mega_volts_per_minutes, ElectricPotentialChangeRateUnits.MegaVoltPerMinute)

    
    @staticmethod
    def from_micro_volts_per_hours(micro_volts_per_hours: float):
        """
        Create a new instance of ElectricPotentialChangeRate from a value in micro_volts_per_hours.

        

        :param meters: The ElectricPotentialChangeRate value in micro_volts_per_hours.
        :type micro_volts_per_hours: float
        :return: A new instance of ElectricPotentialChangeRate.
        :rtype: ElectricPotentialChangeRate
        """
        return ElectricPotentialChangeRate(micro_volts_per_hours, ElectricPotentialChangeRateUnits.MicroVoltPerHour)

    
    @staticmethod
    def from_milli_volts_per_hours(milli_volts_per_hours: float):
        """
        Create a new instance of ElectricPotentialChangeRate from a value in milli_volts_per_hours.

        

        :param meters: The ElectricPotentialChangeRate value in milli_volts_per_hours.
        :type milli_volts_per_hours: float
        :return: A new instance of ElectricPotentialChangeRate.
        :rtype: ElectricPotentialChangeRate
        """
        return ElectricPotentialChangeRate(milli_volts_per_hours, ElectricPotentialChangeRateUnits.MilliVoltPerHour)

    
    @staticmethod
    def from_kilo_volts_per_hours(kilo_volts_per_hours: float):
        """
        Create a new instance of ElectricPotentialChangeRate from a value in kilo_volts_per_hours.

        

        :param meters: The ElectricPotentialChangeRate value in kilo_volts_per_hours.
        :type kilo_volts_per_hours: float
        :return: A new instance of ElectricPotentialChangeRate.
        :rtype: ElectricPotentialChangeRate
        """
        return ElectricPotentialChangeRate(kilo_volts_per_hours, ElectricPotentialChangeRateUnits.KiloVoltPerHour)

    
    @staticmethod
    def from_mega_volts_per_hours(mega_volts_per_hours: float):
        """
        Create a new instance of ElectricPotentialChangeRate from a value in mega_volts_per_hours.

        

        :param meters: The ElectricPotentialChangeRate value in mega_volts_per_hours.
        :type mega_volts_per_hours: float
        :return: A new instance of ElectricPotentialChangeRate.
        :rtype: ElectricPotentialChangeRate
        """
        return ElectricPotentialChangeRate(mega_volts_per_hours, ElectricPotentialChangeRateUnits.MegaVoltPerHour)

    
    @property
    def volts_per_seconds(self) -> float:
        """
        
        """
        if self.__volts_per_seconds != None:
            return self.__volts_per_seconds
        self.__volts_per_seconds = self.__convert_from_base(ElectricPotentialChangeRateUnits.VoltPerSecond)
        return self.__volts_per_seconds

    
    @property
    def volts_per_microseconds(self) -> float:
        """
        
        """
        if self.__volts_per_microseconds != None:
            return self.__volts_per_microseconds
        self.__volts_per_microseconds = self.__convert_from_base(ElectricPotentialChangeRateUnits.VoltPerMicrosecond)
        return self.__volts_per_microseconds

    
    @property
    def volts_per_minutes(self) -> float:
        """
        
        """
        if self.__volts_per_minutes != None:
            return self.__volts_per_minutes
        self.__volts_per_minutes = self.__convert_from_base(ElectricPotentialChangeRateUnits.VoltPerMinute)
        return self.__volts_per_minutes

    
    @property
    def volts_per_hours(self) -> float:
        """
        
        """
        if self.__volts_per_hours != None:
            return self.__volts_per_hours
        self.__volts_per_hours = self.__convert_from_base(ElectricPotentialChangeRateUnits.VoltPerHour)
        return self.__volts_per_hours

    
    @property
    def micro_volts_per_seconds(self) -> float:
        """
        
        """
        if self.__micro_volts_per_seconds != None:
            return self.__micro_volts_per_seconds
        self.__micro_volts_per_seconds = self.__convert_from_base(ElectricPotentialChangeRateUnits.MicroVoltPerSecond)
        return self.__micro_volts_per_seconds

    
    @property
    def milli_volts_per_seconds(self) -> float:
        """
        
        """
        if self.__milli_volts_per_seconds != None:
            return self.__milli_volts_per_seconds
        self.__milli_volts_per_seconds = self.__convert_from_base(ElectricPotentialChangeRateUnits.MilliVoltPerSecond)
        return self.__milli_volts_per_seconds

    
    @property
    def kilo_volts_per_seconds(self) -> float:
        """
        
        """
        if self.__kilo_volts_per_seconds != None:
            return self.__kilo_volts_per_seconds
        self.__kilo_volts_per_seconds = self.__convert_from_base(ElectricPotentialChangeRateUnits.KiloVoltPerSecond)
        return self.__kilo_volts_per_seconds

    
    @property
    def mega_volts_per_seconds(self) -> float:
        """
        
        """
        if self.__mega_volts_per_seconds != None:
            return self.__mega_volts_per_seconds
        self.__mega_volts_per_seconds = self.__convert_from_base(ElectricPotentialChangeRateUnits.MegaVoltPerSecond)
        return self.__mega_volts_per_seconds

    
    @property
    def micro_volts_per_microseconds(self) -> float:
        """
        
        """
        if self.__micro_volts_per_microseconds != None:
            return self.__micro_volts_per_microseconds
        self.__micro_volts_per_microseconds = self.__convert_from_base(ElectricPotentialChangeRateUnits.MicroVoltPerMicrosecond)
        return self.__micro_volts_per_microseconds

    
    @property
    def milli_volts_per_microseconds(self) -> float:
        """
        
        """
        if self.__milli_volts_per_microseconds != None:
            return self.__milli_volts_per_microseconds
        self.__milli_volts_per_microseconds = self.__convert_from_base(ElectricPotentialChangeRateUnits.MilliVoltPerMicrosecond)
        return self.__milli_volts_per_microseconds

    
    @property
    def kilo_volts_per_microseconds(self) -> float:
        """
        
        """
        if self.__kilo_volts_per_microseconds != None:
            return self.__kilo_volts_per_microseconds
        self.__kilo_volts_per_microseconds = self.__convert_from_base(ElectricPotentialChangeRateUnits.KiloVoltPerMicrosecond)
        return self.__kilo_volts_per_microseconds

    
    @property
    def mega_volts_per_microseconds(self) -> float:
        """
        
        """
        if self.__mega_volts_per_microseconds != None:
            return self.__mega_volts_per_microseconds
        self.__mega_volts_per_microseconds = self.__convert_from_base(ElectricPotentialChangeRateUnits.MegaVoltPerMicrosecond)
        return self.__mega_volts_per_microseconds

    
    @property
    def micro_volts_per_minutes(self) -> float:
        """
        
        """
        if self.__micro_volts_per_minutes != None:
            return self.__micro_volts_per_minutes
        self.__micro_volts_per_minutes = self.__convert_from_base(ElectricPotentialChangeRateUnits.MicroVoltPerMinute)
        return self.__micro_volts_per_minutes

    
    @property
    def milli_volts_per_minutes(self) -> float:
        """
        
        """
        if self.__milli_volts_per_minutes != None:
            return self.__milli_volts_per_minutes
        self.__milli_volts_per_minutes = self.__convert_from_base(ElectricPotentialChangeRateUnits.MilliVoltPerMinute)
        return self.__milli_volts_per_minutes

    
    @property
    def kilo_volts_per_minutes(self) -> float:
        """
        
        """
        if self.__kilo_volts_per_minutes != None:
            return self.__kilo_volts_per_minutes
        self.__kilo_volts_per_minutes = self.__convert_from_base(ElectricPotentialChangeRateUnits.KiloVoltPerMinute)
        return self.__kilo_volts_per_minutes

    
    @property
    def mega_volts_per_minutes(self) -> float:
        """
        
        """
        if self.__mega_volts_per_minutes != None:
            return self.__mega_volts_per_minutes
        self.__mega_volts_per_minutes = self.__convert_from_base(ElectricPotentialChangeRateUnits.MegaVoltPerMinute)
        return self.__mega_volts_per_minutes

    
    @property
    def micro_volts_per_hours(self) -> float:
        """
        
        """
        if self.__micro_volts_per_hours != None:
            return self.__micro_volts_per_hours
        self.__micro_volts_per_hours = self.__convert_from_base(ElectricPotentialChangeRateUnits.MicroVoltPerHour)
        return self.__micro_volts_per_hours

    
    @property
    def milli_volts_per_hours(self) -> float:
        """
        
        """
        if self.__milli_volts_per_hours != None:
            return self.__milli_volts_per_hours
        self.__milli_volts_per_hours = self.__convert_from_base(ElectricPotentialChangeRateUnits.MilliVoltPerHour)
        return self.__milli_volts_per_hours

    
    @property
    def kilo_volts_per_hours(self) -> float:
        """
        
        """
        if self.__kilo_volts_per_hours != None:
            return self.__kilo_volts_per_hours
        self.__kilo_volts_per_hours = self.__convert_from_base(ElectricPotentialChangeRateUnits.KiloVoltPerHour)
        return self.__kilo_volts_per_hours

    
    @property
    def mega_volts_per_hours(self) -> float:
        """
        
        """
        if self.__mega_volts_per_hours != None:
            return self.__mega_volts_per_hours
        self.__mega_volts_per_hours = self.__convert_from_base(ElectricPotentialChangeRateUnits.MegaVoltPerHour)
        return self.__mega_volts_per_hours

    
    def to_string(self, unit: ElectricPotentialChangeRateUnits = ElectricPotentialChangeRateUnits.VoltPerSecond) -> string:
        """
        Format the ElectricPotentialChangeRate to string.
        Note! the default format for ElectricPotentialChangeRate is VoltPerSecond.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == ElectricPotentialChangeRateUnits.VoltPerSecond:
            return f"""{self.volts_per_seconds} V/s"""
        
        if unit == ElectricPotentialChangeRateUnits.VoltPerMicrosecond:
            return f"""{self.volts_per_microseconds} V/μs"""
        
        if unit == ElectricPotentialChangeRateUnits.VoltPerMinute:
            return f"""{self.volts_per_minutes} V/min"""
        
        if unit == ElectricPotentialChangeRateUnits.VoltPerHour:
            return f"""{self.volts_per_hours} V/h"""
        
        if unit == ElectricPotentialChangeRateUnits.MicroVoltPerSecond:
            return f"""{self.micro_volts_per_seconds} """
        
        if unit == ElectricPotentialChangeRateUnits.MilliVoltPerSecond:
            return f"""{self.milli_volts_per_seconds} """
        
        if unit == ElectricPotentialChangeRateUnits.KiloVoltPerSecond:
            return f"""{self.kilo_volts_per_seconds} """
        
        if unit == ElectricPotentialChangeRateUnits.MegaVoltPerSecond:
            return f"""{self.mega_volts_per_seconds} """
        
        if unit == ElectricPotentialChangeRateUnits.MicroVoltPerMicrosecond:
            return f"""{self.micro_volts_per_microseconds} """
        
        if unit == ElectricPotentialChangeRateUnits.MilliVoltPerMicrosecond:
            return f"""{self.milli_volts_per_microseconds} """
        
        if unit == ElectricPotentialChangeRateUnits.KiloVoltPerMicrosecond:
            return f"""{self.kilo_volts_per_microseconds} """
        
        if unit == ElectricPotentialChangeRateUnits.MegaVoltPerMicrosecond:
            return f"""{self.mega_volts_per_microseconds} """
        
        if unit == ElectricPotentialChangeRateUnits.MicroVoltPerMinute:
            return f"""{self.micro_volts_per_minutes} """
        
        if unit == ElectricPotentialChangeRateUnits.MilliVoltPerMinute:
            return f"""{self.milli_volts_per_minutes} """
        
        if unit == ElectricPotentialChangeRateUnits.KiloVoltPerMinute:
            return f"""{self.kilo_volts_per_minutes} """
        
        if unit == ElectricPotentialChangeRateUnits.MegaVoltPerMinute:
            return f"""{self.mega_volts_per_minutes} """
        
        if unit == ElectricPotentialChangeRateUnits.MicroVoltPerHour:
            return f"""{self.micro_volts_per_hours} """
        
        if unit == ElectricPotentialChangeRateUnits.MilliVoltPerHour:
            return f"""{self.milli_volts_per_hours} """
        
        if unit == ElectricPotentialChangeRateUnits.KiloVoltPerHour:
            return f"""{self.kilo_volts_per_hours} """
        
        if unit == ElectricPotentialChangeRateUnits.MegaVoltPerHour:
            return f"""{self.mega_volts_per_hours} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: ElectricPotentialChangeRateUnits = ElectricPotentialChangeRateUnits.VoltPerSecond) -> string:
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
        
        if unit_abbreviation == ElectricPotentialChangeRateUnits.MicroVoltPerSecond:
            return """"""
        
        if unit_abbreviation == ElectricPotentialChangeRateUnits.MilliVoltPerSecond:
            return """"""
        
        if unit_abbreviation == ElectricPotentialChangeRateUnits.KiloVoltPerSecond:
            return """"""
        
        if unit_abbreviation == ElectricPotentialChangeRateUnits.MegaVoltPerSecond:
            return """"""
        
        if unit_abbreviation == ElectricPotentialChangeRateUnits.MicroVoltPerMicrosecond:
            return """"""
        
        if unit_abbreviation == ElectricPotentialChangeRateUnits.MilliVoltPerMicrosecond:
            return """"""
        
        if unit_abbreviation == ElectricPotentialChangeRateUnits.KiloVoltPerMicrosecond:
            return """"""
        
        if unit_abbreviation == ElectricPotentialChangeRateUnits.MegaVoltPerMicrosecond:
            return """"""
        
        if unit_abbreviation == ElectricPotentialChangeRateUnits.MicroVoltPerMinute:
            return """"""
        
        if unit_abbreviation == ElectricPotentialChangeRateUnits.MilliVoltPerMinute:
            return """"""
        
        if unit_abbreviation == ElectricPotentialChangeRateUnits.KiloVoltPerMinute:
            return """"""
        
        if unit_abbreviation == ElectricPotentialChangeRateUnits.MegaVoltPerMinute:
            return """"""
        
        if unit_abbreviation == ElectricPotentialChangeRateUnits.MicroVoltPerHour:
            return """"""
        
        if unit_abbreviation == ElectricPotentialChangeRateUnits.MilliVoltPerHour:
            return """"""
        
        if unit_abbreviation == ElectricPotentialChangeRateUnits.KiloVoltPerHour:
            return """"""
        
        if unit_abbreviation == ElectricPotentialChangeRateUnits.MegaVoltPerHour:
            return """"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, ElectricPotentialChangeRate):
            raise TypeError("unsupported operand type(s) for +: 'ElectricPotentialChangeRate' and '{}'".format(type(other).__name__))
        return ElectricPotentialChangeRate(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, ElectricPotentialChangeRate):
            raise TypeError("unsupported operand type(s) for *: 'ElectricPotentialChangeRate' and '{}'".format(type(other).__name__))
        return ElectricPotentialChangeRate(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, ElectricPotentialChangeRate):
            raise TypeError("unsupported operand type(s) for -: 'ElectricPotentialChangeRate' and '{}'".format(type(other).__name__))
        return ElectricPotentialChangeRate(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, ElectricPotentialChangeRate):
            raise TypeError("unsupported operand type(s) for /: 'ElectricPotentialChangeRate' and '{}'".format(type(other).__name__))
        return ElectricPotentialChangeRate(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, ElectricPotentialChangeRate):
            raise TypeError("unsupported operand type(s) for %: 'ElectricPotentialChangeRate' and '{}'".format(type(other).__name__))
        return ElectricPotentialChangeRate(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, ElectricPotentialChangeRate):
            raise TypeError("unsupported operand type(s) for **: 'ElectricPotentialChangeRate' and '{}'".format(type(other).__name__))
        return ElectricPotentialChangeRate(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, ElectricPotentialChangeRate):
            raise TypeError("unsupported operand type(s) for ==: 'ElectricPotentialChangeRate' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, ElectricPotentialChangeRate):
            raise TypeError("unsupported operand type(s) for <: 'ElectricPotentialChangeRate' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, ElectricPotentialChangeRate):
            raise TypeError("unsupported operand type(s) for >: 'ElectricPotentialChangeRate' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, ElectricPotentialChangeRate):
            raise TypeError("unsupported operand type(s) for <=: 'ElectricPotentialChangeRate' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, ElectricPotentialChangeRate):
            raise TypeError("unsupported operand type(s) for >=: 'ElectricPotentialChangeRate' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value
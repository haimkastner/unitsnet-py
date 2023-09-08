from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class ForceChangeRateUnits(Enum):
        """
            ForceChangeRateUnits enumeration
        """
        
        NewtonPerMinute = 'newton_per_minute'
        """
            
        """
        
        NewtonPerSecond = 'newton_per_second'
        """
            
        """
        
        PoundForcePerMinute = 'pound_force_per_minute'
        """
            
        """
        
        PoundForcePerSecond = 'pound_force_per_second'
        """
            
        """
        
        DecanewtonPerMinute = 'decanewton_per_minute'
        """
            
        """
        
        KilonewtonPerMinute = 'kilonewton_per_minute'
        """
            
        """
        
        NanonewtonPerSecond = 'nanonewton_per_second'
        """
            
        """
        
        MicronewtonPerSecond = 'micronewton_per_second'
        """
            
        """
        
        MillinewtonPerSecond = 'millinewton_per_second'
        """
            
        """
        
        CentinewtonPerSecond = 'centinewton_per_second'
        """
            
        """
        
        DecinewtonPerSecond = 'decinewton_per_second'
        """
            
        """
        
        DecanewtonPerSecond = 'decanewton_per_second'
        """
            
        """
        
        KilonewtonPerSecond = 'kilonewton_per_second'
        """
            
        """
        
        KilopoundForcePerMinute = 'kilopound_force_per_minute'
        """
            
        """
        
        KilopoundForcePerSecond = 'kilopound_force_per_second'
        """
            
        """
        

class ForceChangeRate(AbstractMeasure):
    """
    Force change rate is the ratio of the force change to the time during which the change occurred (value of force changes per unit time).

    Args:
        value (float): The value.
        from_unit (ForceChangeRateUnits): The ForceChangeRate unit to create from, The default unit is NewtonPerSecond
    """
    def __init__(self, value: float, from_unit: ForceChangeRateUnits = ForceChangeRateUnits.NewtonPerSecond):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__newtons_per_minute = None
        
        self.__newtons_per_second = None
        
        self.__pounds_force_per_minute = None
        
        self.__pounds_force_per_second = None
        
        self.__decanewtons_per_minute = None
        
        self.__kilonewtons_per_minute = None
        
        self.__nanonewtons_per_second = None
        
        self.__micronewtons_per_second = None
        
        self.__millinewtons_per_second = None
        
        self.__centinewtons_per_second = None
        
        self.__decinewtons_per_second = None
        
        self.__decanewtons_per_second = None
        
        self.__kilonewtons_per_second = None
        
        self.__kilopounds_force_per_minute = None
        
        self.__kilopounds_force_per_second = None
        

    def convert(self, unit: ForceChangeRateUnits) -> float:
        return self.__convert_from_base(unit)

    def __convert_from_base(self, from_unit: ForceChangeRateUnits) -> float:
        value = self._value
        
        if from_unit == ForceChangeRateUnits.NewtonPerMinute:
            return (value * 60)
        
        if from_unit == ForceChangeRateUnits.NewtonPerSecond:
            return (value)
        
        if from_unit == ForceChangeRateUnits.PoundForcePerMinute:
            return (value / 4.4482216152605095551842641431421 * 60)
        
        if from_unit == ForceChangeRateUnits.PoundForcePerSecond:
            return (value / 4.4482216152605095551842641431421)
        
        if from_unit == ForceChangeRateUnits.DecanewtonPerMinute:
            return ((value * 60) / 10.0)
        
        if from_unit == ForceChangeRateUnits.KilonewtonPerMinute:
            return ((value * 60) / 1000.0)
        
        if from_unit == ForceChangeRateUnits.NanonewtonPerSecond:
            return ((value) / 1e-09)
        
        if from_unit == ForceChangeRateUnits.MicronewtonPerSecond:
            return ((value) / 1e-06)
        
        if from_unit == ForceChangeRateUnits.MillinewtonPerSecond:
            return ((value) / 0.001)
        
        if from_unit == ForceChangeRateUnits.CentinewtonPerSecond:
            return ((value) / 0.01)
        
        if from_unit == ForceChangeRateUnits.DecinewtonPerSecond:
            return ((value) / 0.1)
        
        if from_unit == ForceChangeRateUnits.DecanewtonPerSecond:
            return ((value) / 10.0)
        
        if from_unit == ForceChangeRateUnits.KilonewtonPerSecond:
            return ((value) / 1000.0)
        
        if from_unit == ForceChangeRateUnits.KilopoundForcePerMinute:
            return ((value / 4.4482216152605095551842641431421 * 60) / 1000.0)
        
        if from_unit == ForceChangeRateUnits.KilopoundForcePerSecond:
            return ((value / 4.4482216152605095551842641431421) / 1000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: ForceChangeRateUnits) -> float:
        
        if to_unit == ForceChangeRateUnits.NewtonPerMinute:
            return (value / 60)
        
        if to_unit == ForceChangeRateUnits.NewtonPerSecond:
            return (value)
        
        if to_unit == ForceChangeRateUnits.PoundForcePerMinute:
            return (value * 4.4482216152605095551842641431421 / 60)
        
        if to_unit == ForceChangeRateUnits.PoundForcePerSecond:
            return (value * 4.4482216152605095551842641431421)
        
        if to_unit == ForceChangeRateUnits.DecanewtonPerMinute:
            return ((value / 60) * 10.0)
        
        if to_unit == ForceChangeRateUnits.KilonewtonPerMinute:
            return ((value / 60) * 1000.0)
        
        if to_unit == ForceChangeRateUnits.NanonewtonPerSecond:
            return ((value) * 1e-09)
        
        if to_unit == ForceChangeRateUnits.MicronewtonPerSecond:
            return ((value) * 1e-06)
        
        if to_unit == ForceChangeRateUnits.MillinewtonPerSecond:
            return ((value) * 0.001)
        
        if to_unit == ForceChangeRateUnits.CentinewtonPerSecond:
            return ((value) * 0.01)
        
        if to_unit == ForceChangeRateUnits.DecinewtonPerSecond:
            return ((value) * 0.1)
        
        if to_unit == ForceChangeRateUnits.DecanewtonPerSecond:
            return ((value) * 10.0)
        
        if to_unit == ForceChangeRateUnits.KilonewtonPerSecond:
            return ((value) * 1000.0)
        
        if to_unit == ForceChangeRateUnits.KilopoundForcePerMinute:
            return ((value * 4.4482216152605095551842641431421 / 60) * 1000.0)
        
        if to_unit == ForceChangeRateUnits.KilopoundForcePerSecond:
            return ((value * 4.4482216152605095551842641431421) * 1000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_newtons_per_minute(newtons_per_minute: float):
        """
        Create a new instance of ForceChangeRate from a value in newtons_per_minute.

        

        :param meters: The ForceChangeRate value in newtons_per_minute.
        :type newtons_per_minute: float
        :return: A new instance of ForceChangeRate.
        :rtype: ForceChangeRate
        """
        return ForceChangeRate(newtons_per_minute, ForceChangeRateUnits.NewtonPerMinute)

    
    @staticmethod
    def from_newtons_per_second(newtons_per_second: float):
        """
        Create a new instance of ForceChangeRate from a value in newtons_per_second.

        

        :param meters: The ForceChangeRate value in newtons_per_second.
        :type newtons_per_second: float
        :return: A new instance of ForceChangeRate.
        :rtype: ForceChangeRate
        """
        return ForceChangeRate(newtons_per_second, ForceChangeRateUnits.NewtonPerSecond)

    
    @staticmethod
    def from_pounds_force_per_minute(pounds_force_per_minute: float):
        """
        Create a new instance of ForceChangeRate from a value in pounds_force_per_minute.

        

        :param meters: The ForceChangeRate value in pounds_force_per_minute.
        :type pounds_force_per_minute: float
        :return: A new instance of ForceChangeRate.
        :rtype: ForceChangeRate
        """
        return ForceChangeRate(pounds_force_per_minute, ForceChangeRateUnits.PoundForcePerMinute)

    
    @staticmethod
    def from_pounds_force_per_second(pounds_force_per_second: float):
        """
        Create a new instance of ForceChangeRate from a value in pounds_force_per_second.

        

        :param meters: The ForceChangeRate value in pounds_force_per_second.
        :type pounds_force_per_second: float
        :return: A new instance of ForceChangeRate.
        :rtype: ForceChangeRate
        """
        return ForceChangeRate(pounds_force_per_second, ForceChangeRateUnits.PoundForcePerSecond)

    
    @staticmethod
    def from_decanewtons_per_minute(decanewtons_per_minute: float):
        """
        Create a new instance of ForceChangeRate from a value in decanewtons_per_minute.

        

        :param meters: The ForceChangeRate value in decanewtons_per_minute.
        :type decanewtons_per_minute: float
        :return: A new instance of ForceChangeRate.
        :rtype: ForceChangeRate
        """
        return ForceChangeRate(decanewtons_per_minute, ForceChangeRateUnits.DecanewtonPerMinute)

    
    @staticmethod
    def from_kilonewtons_per_minute(kilonewtons_per_minute: float):
        """
        Create a new instance of ForceChangeRate from a value in kilonewtons_per_minute.

        

        :param meters: The ForceChangeRate value in kilonewtons_per_minute.
        :type kilonewtons_per_minute: float
        :return: A new instance of ForceChangeRate.
        :rtype: ForceChangeRate
        """
        return ForceChangeRate(kilonewtons_per_minute, ForceChangeRateUnits.KilonewtonPerMinute)

    
    @staticmethod
    def from_nanonewtons_per_second(nanonewtons_per_second: float):
        """
        Create a new instance of ForceChangeRate from a value in nanonewtons_per_second.

        

        :param meters: The ForceChangeRate value in nanonewtons_per_second.
        :type nanonewtons_per_second: float
        :return: A new instance of ForceChangeRate.
        :rtype: ForceChangeRate
        """
        return ForceChangeRate(nanonewtons_per_second, ForceChangeRateUnits.NanonewtonPerSecond)

    
    @staticmethod
    def from_micronewtons_per_second(micronewtons_per_second: float):
        """
        Create a new instance of ForceChangeRate from a value in micronewtons_per_second.

        

        :param meters: The ForceChangeRate value in micronewtons_per_second.
        :type micronewtons_per_second: float
        :return: A new instance of ForceChangeRate.
        :rtype: ForceChangeRate
        """
        return ForceChangeRate(micronewtons_per_second, ForceChangeRateUnits.MicronewtonPerSecond)

    
    @staticmethod
    def from_millinewtons_per_second(millinewtons_per_second: float):
        """
        Create a new instance of ForceChangeRate from a value in millinewtons_per_second.

        

        :param meters: The ForceChangeRate value in millinewtons_per_second.
        :type millinewtons_per_second: float
        :return: A new instance of ForceChangeRate.
        :rtype: ForceChangeRate
        """
        return ForceChangeRate(millinewtons_per_second, ForceChangeRateUnits.MillinewtonPerSecond)

    
    @staticmethod
    def from_centinewtons_per_second(centinewtons_per_second: float):
        """
        Create a new instance of ForceChangeRate from a value in centinewtons_per_second.

        

        :param meters: The ForceChangeRate value in centinewtons_per_second.
        :type centinewtons_per_second: float
        :return: A new instance of ForceChangeRate.
        :rtype: ForceChangeRate
        """
        return ForceChangeRate(centinewtons_per_second, ForceChangeRateUnits.CentinewtonPerSecond)

    
    @staticmethod
    def from_decinewtons_per_second(decinewtons_per_second: float):
        """
        Create a new instance of ForceChangeRate from a value in decinewtons_per_second.

        

        :param meters: The ForceChangeRate value in decinewtons_per_second.
        :type decinewtons_per_second: float
        :return: A new instance of ForceChangeRate.
        :rtype: ForceChangeRate
        """
        return ForceChangeRate(decinewtons_per_second, ForceChangeRateUnits.DecinewtonPerSecond)

    
    @staticmethod
    def from_decanewtons_per_second(decanewtons_per_second: float):
        """
        Create a new instance of ForceChangeRate from a value in decanewtons_per_second.

        

        :param meters: The ForceChangeRate value in decanewtons_per_second.
        :type decanewtons_per_second: float
        :return: A new instance of ForceChangeRate.
        :rtype: ForceChangeRate
        """
        return ForceChangeRate(decanewtons_per_second, ForceChangeRateUnits.DecanewtonPerSecond)

    
    @staticmethod
    def from_kilonewtons_per_second(kilonewtons_per_second: float):
        """
        Create a new instance of ForceChangeRate from a value in kilonewtons_per_second.

        

        :param meters: The ForceChangeRate value in kilonewtons_per_second.
        :type kilonewtons_per_second: float
        :return: A new instance of ForceChangeRate.
        :rtype: ForceChangeRate
        """
        return ForceChangeRate(kilonewtons_per_second, ForceChangeRateUnits.KilonewtonPerSecond)

    
    @staticmethod
    def from_kilopounds_force_per_minute(kilopounds_force_per_minute: float):
        """
        Create a new instance of ForceChangeRate from a value in kilopounds_force_per_minute.

        

        :param meters: The ForceChangeRate value in kilopounds_force_per_minute.
        :type kilopounds_force_per_minute: float
        :return: A new instance of ForceChangeRate.
        :rtype: ForceChangeRate
        """
        return ForceChangeRate(kilopounds_force_per_minute, ForceChangeRateUnits.KilopoundForcePerMinute)

    
    @staticmethod
    def from_kilopounds_force_per_second(kilopounds_force_per_second: float):
        """
        Create a new instance of ForceChangeRate from a value in kilopounds_force_per_second.

        

        :param meters: The ForceChangeRate value in kilopounds_force_per_second.
        :type kilopounds_force_per_second: float
        :return: A new instance of ForceChangeRate.
        :rtype: ForceChangeRate
        """
        return ForceChangeRate(kilopounds_force_per_second, ForceChangeRateUnits.KilopoundForcePerSecond)

    
    @property
    def newtons_per_minute(self) -> float:
        """
        
        """
        if self.__newtons_per_minute != None:
            return self.__newtons_per_minute
        self.__newtons_per_minute = self.__convert_from_base(ForceChangeRateUnits.NewtonPerMinute)
        return self.__newtons_per_minute

    
    @property
    def newtons_per_second(self) -> float:
        """
        
        """
        if self.__newtons_per_second != None:
            return self.__newtons_per_second
        self.__newtons_per_second = self.__convert_from_base(ForceChangeRateUnits.NewtonPerSecond)
        return self.__newtons_per_second

    
    @property
    def pounds_force_per_minute(self) -> float:
        """
        
        """
        if self.__pounds_force_per_minute != None:
            return self.__pounds_force_per_minute
        self.__pounds_force_per_minute = self.__convert_from_base(ForceChangeRateUnits.PoundForcePerMinute)
        return self.__pounds_force_per_minute

    
    @property
    def pounds_force_per_second(self) -> float:
        """
        
        """
        if self.__pounds_force_per_second != None:
            return self.__pounds_force_per_second
        self.__pounds_force_per_second = self.__convert_from_base(ForceChangeRateUnits.PoundForcePerSecond)
        return self.__pounds_force_per_second

    
    @property
    def decanewtons_per_minute(self) -> float:
        """
        
        """
        if self.__decanewtons_per_minute != None:
            return self.__decanewtons_per_minute
        self.__decanewtons_per_minute = self.__convert_from_base(ForceChangeRateUnits.DecanewtonPerMinute)
        return self.__decanewtons_per_minute

    
    @property
    def kilonewtons_per_minute(self) -> float:
        """
        
        """
        if self.__kilonewtons_per_minute != None:
            return self.__kilonewtons_per_minute
        self.__kilonewtons_per_minute = self.__convert_from_base(ForceChangeRateUnits.KilonewtonPerMinute)
        return self.__kilonewtons_per_minute

    
    @property
    def nanonewtons_per_second(self) -> float:
        """
        
        """
        if self.__nanonewtons_per_second != None:
            return self.__nanonewtons_per_second
        self.__nanonewtons_per_second = self.__convert_from_base(ForceChangeRateUnits.NanonewtonPerSecond)
        return self.__nanonewtons_per_second

    
    @property
    def micronewtons_per_second(self) -> float:
        """
        
        """
        if self.__micronewtons_per_second != None:
            return self.__micronewtons_per_second
        self.__micronewtons_per_second = self.__convert_from_base(ForceChangeRateUnits.MicronewtonPerSecond)
        return self.__micronewtons_per_second

    
    @property
    def millinewtons_per_second(self) -> float:
        """
        
        """
        if self.__millinewtons_per_second != None:
            return self.__millinewtons_per_second
        self.__millinewtons_per_second = self.__convert_from_base(ForceChangeRateUnits.MillinewtonPerSecond)
        return self.__millinewtons_per_second

    
    @property
    def centinewtons_per_second(self) -> float:
        """
        
        """
        if self.__centinewtons_per_second != None:
            return self.__centinewtons_per_second
        self.__centinewtons_per_second = self.__convert_from_base(ForceChangeRateUnits.CentinewtonPerSecond)
        return self.__centinewtons_per_second

    
    @property
    def decinewtons_per_second(self) -> float:
        """
        
        """
        if self.__decinewtons_per_second != None:
            return self.__decinewtons_per_second
        self.__decinewtons_per_second = self.__convert_from_base(ForceChangeRateUnits.DecinewtonPerSecond)
        return self.__decinewtons_per_second

    
    @property
    def decanewtons_per_second(self) -> float:
        """
        
        """
        if self.__decanewtons_per_second != None:
            return self.__decanewtons_per_second
        self.__decanewtons_per_second = self.__convert_from_base(ForceChangeRateUnits.DecanewtonPerSecond)
        return self.__decanewtons_per_second

    
    @property
    def kilonewtons_per_second(self) -> float:
        """
        
        """
        if self.__kilonewtons_per_second != None:
            return self.__kilonewtons_per_second
        self.__kilonewtons_per_second = self.__convert_from_base(ForceChangeRateUnits.KilonewtonPerSecond)
        return self.__kilonewtons_per_second

    
    @property
    def kilopounds_force_per_minute(self) -> float:
        """
        
        """
        if self.__kilopounds_force_per_minute != None:
            return self.__kilopounds_force_per_minute
        self.__kilopounds_force_per_minute = self.__convert_from_base(ForceChangeRateUnits.KilopoundForcePerMinute)
        return self.__kilopounds_force_per_minute

    
    @property
    def kilopounds_force_per_second(self) -> float:
        """
        
        """
        if self.__kilopounds_force_per_second != None:
            return self.__kilopounds_force_per_second
        self.__kilopounds_force_per_second = self.__convert_from_base(ForceChangeRateUnits.KilopoundForcePerSecond)
        return self.__kilopounds_force_per_second

    
    def to_string(self, unit: ForceChangeRateUnits = ForceChangeRateUnits.NewtonPerSecond) -> str:
        """
        Format the ForceChangeRate to string.
        Note! the default format for ForceChangeRate is NewtonPerSecond.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == ForceChangeRateUnits.NewtonPerMinute:
            return f"""{self.newtons_per_minute} N/min"""
        
        if unit == ForceChangeRateUnits.NewtonPerSecond:
            return f"""{self.newtons_per_second} N/s"""
        
        if unit == ForceChangeRateUnits.PoundForcePerMinute:
            return f"""{self.pounds_force_per_minute} lbf/min"""
        
        if unit == ForceChangeRateUnits.PoundForcePerSecond:
            return f"""{self.pounds_force_per_second} lbf/s"""
        
        if unit == ForceChangeRateUnits.DecanewtonPerMinute:
            return f"""{self.decanewtons_per_minute} daN/min"""
        
        if unit == ForceChangeRateUnits.KilonewtonPerMinute:
            return f"""{self.kilonewtons_per_minute} kN/min"""
        
        if unit == ForceChangeRateUnits.NanonewtonPerSecond:
            return f"""{self.nanonewtons_per_second} nN/s"""
        
        if unit == ForceChangeRateUnits.MicronewtonPerSecond:
            return f"""{self.micronewtons_per_second} μN/s"""
        
        if unit == ForceChangeRateUnits.MillinewtonPerSecond:
            return f"""{self.millinewtons_per_second} mN/s"""
        
        if unit == ForceChangeRateUnits.CentinewtonPerSecond:
            return f"""{self.centinewtons_per_second} cN/s"""
        
        if unit == ForceChangeRateUnits.DecinewtonPerSecond:
            return f"""{self.decinewtons_per_second} dN/s"""
        
        if unit == ForceChangeRateUnits.DecanewtonPerSecond:
            return f"""{self.decanewtons_per_second} daN/s"""
        
        if unit == ForceChangeRateUnits.KilonewtonPerSecond:
            return f"""{self.kilonewtons_per_second} kN/s"""
        
        if unit == ForceChangeRateUnits.KilopoundForcePerMinute:
            return f"""{self.kilopounds_force_per_minute} klbf/min"""
        
        if unit == ForceChangeRateUnits.KilopoundForcePerSecond:
            return f"""{self.kilopounds_force_per_second} klbf/s"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: ForceChangeRateUnits = ForceChangeRateUnits.NewtonPerSecond) -> str:
        """
        Get ForceChangeRate unit abbreviation.
        Note! the default abbreviation for ForceChangeRate is NewtonPerSecond.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == ForceChangeRateUnits.NewtonPerMinute:
            return """N/min"""
        
        if unit_abbreviation == ForceChangeRateUnits.NewtonPerSecond:
            return """N/s"""
        
        if unit_abbreviation == ForceChangeRateUnits.PoundForcePerMinute:
            return """lbf/min"""
        
        if unit_abbreviation == ForceChangeRateUnits.PoundForcePerSecond:
            return """lbf/s"""
        
        if unit_abbreviation == ForceChangeRateUnits.DecanewtonPerMinute:
            return """daN/min"""
        
        if unit_abbreviation == ForceChangeRateUnits.KilonewtonPerMinute:
            return """kN/min"""
        
        if unit_abbreviation == ForceChangeRateUnits.NanonewtonPerSecond:
            return """nN/s"""
        
        if unit_abbreviation == ForceChangeRateUnits.MicronewtonPerSecond:
            return """μN/s"""
        
        if unit_abbreviation == ForceChangeRateUnits.MillinewtonPerSecond:
            return """mN/s"""
        
        if unit_abbreviation == ForceChangeRateUnits.CentinewtonPerSecond:
            return """cN/s"""
        
        if unit_abbreviation == ForceChangeRateUnits.DecinewtonPerSecond:
            return """dN/s"""
        
        if unit_abbreviation == ForceChangeRateUnits.DecanewtonPerSecond:
            return """daN/s"""
        
        if unit_abbreviation == ForceChangeRateUnits.KilonewtonPerSecond:
            return """kN/s"""
        
        if unit_abbreviation == ForceChangeRateUnits.KilopoundForcePerMinute:
            return """klbf/min"""
        
        if unit_abbreviation == ForceChangeRateUnits.KilopoundForcePerSecond:
            return """klbf/s"""
        
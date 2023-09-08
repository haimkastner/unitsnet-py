from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class MolarFlowUnits(Enum):
        """
            MolarFlowUnits enumeration
        """
        
        MolePerSecond = 'mole_per_second'
        """
            
        """
        
        MolePerMinute = 'mole_per_minute'
        """
            
        """
        
        MolePerHour = 'mole_per_hour'
        """
            
        """
        
        PoundMolePerSecond = 'pound_mole_per_second'
        """
            
        """
        
        PoundMolePerMinute = 'pound_mole_per_minute'
        """
            
        """
        
        PoundMolePerHour = 'pound_mole_per_hour'
        """
            
        """
        
        KilomolePerSecond = 'kilomole_per_second'
        """
            
        """
        
        KilomolePerMinute = 'kilomole_per_minute'
        """
            
        """
        
        KilomolePerHour = 'kilomole_per_hour'
        """
            
        """
        

class MolarFlow(AbstractMeasure):
    """
    Molar flow is the ratio of the amount of substance change to the time during which the change occurred (value of amount of substance changes per unit time).

    Args:
        value (float): The value.
        from_unit (MolarFlowUnits): The MolarFlow unit to create from, The default unit is MolePerSecond
    """
    def __init__(self, value: float, from_unit: MolarFlowUnits = MolarFlowUnits.MolePerSecond):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__moles_per_second = None
        
        self.__moles_per_minute = None
        
        self.__moles_per_hour = None
        
        self.__pound_moles_per_second = None
        
        self.__pound_moles_per_minute = None
        
        self.__pound_moles_per_hour = None
        
        self.__kilomoles_per_second = None
        
        self.__kilomoles_per_minute = None
        
        self.__kilomoles_per_hour = None
        

    def convert(self, unit: MolarFlowUnits) -> float:
        return self.__convert_from_base(unit)

    def __convert_from_base(self, from_unit: MolarFlowUnits) -> float:
        value = self._value
        
        if from_unit == MolarFlowUnits.MolePerSecond:
            return (value)
        
        if from_unit == MolarFlowUnits.MolePerMinute:
            return (value * 60)
        
        if from_unit == MolarFlowUnits.MolePerHour:
            return (value * 3600)
        
        if from_unit == MolarFlowUnits.PoundMolePerSecond:
            return (value / 453.59237)
        
        if from_unit == MolarFlowUnits.PoundMolePerMinute:
            return ((value / 453.59237) * 60)
        
        if from_unit == MolarFlowUnits.PoundMolePerHour:
            return ((value / 453.59237) * 3600)
        
        if from_unit == MolarFlowUnits.KilomolePerSecond:
            return ((value) / 1000.0)
        
        if from_unit == MolarFlowUnits.KilomolePerMinute:
            return ((value * 60) / 1000.0)
        
        if from_unit == MolarFlowUnits.KilomolePerHour:
            return ((value * 3600) / 1000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: MolarFlowUnits) -> float:
        
        if to_unit == MolarFlowUnits.MolePerSecond:
            return (value)
        
        if to_unit == MolarFlowUnits.MolePerMinute:
            return (value / 60)
        
        if to_unit == MolarFlowUnits.MolePerHour:
            return (value / 3600)
        
        if to_unit == MolarFlowUnits.PoundMolePerSecond:
            return (value * 453.59237)
        
        if to_unit == MolarFlowUnits.PoundMolePerMinute:
            return ((value * 453.59237) / 60)
        
        if to_unit == MolarFlowUnits.PoundMolePerHour:
            return ((value * 453.59237) / 3600)
        
        if to_unit == MolarFlowUnits.KilomolePerSecond:
            return ((value) * 1000.0)
        
        if to_unit == MolarFlowUnits.KilomolePerMinute:
            return ((value / 60) * 1000.0)
        
        if to_unit == MolarFlowUnits.KilomolePerHour:
            return ((value / 3600) * 1000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_moles_per_second(moles_per_second: float):
        """
        Create a new instance of MolarFlow from a value in moles_per_second.

        

        :param meters: The MolarFlow value in moles_per_second.
        :type moles_per_second: float
        :return: A new instance of MolarFlow.
        :rtype: MolarFlow
        """
        return MolarFlow(moles_per_second, MolarFlowUnits.MolePerSecond)

    
    @staticmethod
    def from_moles_per_minute(moles_per_minute: float):
        """
        Create a new instance of MolarFlow from a value in moles_per_minute.

        

        :param meters: The MolarFlow value in moles_per_minute.
        :type moles_per_minute: float
        :return: A new instance of MolarFlow.
        :rtype: MolarFlow
        """
        return MolarFlow(moles_per_minute, MolarFlowUnits.MolePerMinute)

    
    @staticmethod
    def from_moles_per_hour(moles_per_hour: float):
        """
        Create a new instance of MolarFlow from a value in moles_per_hour.

        

        :param meters: The MolarFlow value in moles_per_hour.
        :type moles_per_hour: float
        :return: A new instance of MolarFlow.
        :rtype: MolarFlow
        """
        return MolarFlow(moles_per_hour, MolarFlowUnits.MolePerHour)

    
    @staticmethod
    def from_pound_moles_per_second(pound_moles_per_second: float):
        """
        Create a new instance of MolarFlow from a value in pound_moles_per_second.

        

        :param meters: The MolarFlow value in pound_moles_per_second.
        :type pound_moles_per_second: float
        :return: A new instance of MolarFlow.
        :rtype: MolarFlow
        """
        return MolarFlow(pound_moles_per_second, MolarFlowUnits.PoundMolePerSecond)

    
    @staticmethod
    def from_pound_moles_per_minute(pound_moles_per_minute: float):
        """
        Create a new instance of MolarFlow from a value in pound_moles_per_minute.

        

        :param meters: The MolarFlow value in pound_moles_per_minute.
        :type pound_moles_per_minute: float
        :return: A new instance of MolarFlow.
        :rtype: MolarFlow
        """
        return MolarFlow(pound_moles_per_minute, MolarFlowUnits.PoundMolePerMinute)

    
    @staticmethod
    def from_pound_moles_per_hour(pound_moles_per_hour: float):
        """
        Create a new instance of MolarFlow from a value in pound_moles_per_hour.

        

        :param meters: The MolarFlow value in pound_moles_per_hour.
        :type pound_moles_per_hour: float
        :return: A new instance of MolarFlow.
        :rtype: MolarFlow
        """
        return MolarFlow(pound_moles_per_hour, MolarFlowUnits.PoundMolePerHour)

    
    @staticmethod
    def from_kilomoles_per_second(kilomoles_per_second: float):
        """
        Create a new instance of MolarFlow from a value in kilomoles_per_second.

        

        :param meters: The MolarFlow value in kilomoles_per_second.
        :type kilomoles_per_second: float
        :return: A new instance of MolarFlow.
        :rtype: MolarFlow
        """
        return MolarFlow(kilomoles_per_second, MolarFlowUnits.KilomolePerSecond)

    
    @staticmethod
    def from_kilomoles_per_minute(kilomoles_per_minute: float):
        """
        Create a new instance of MolarFlow from a value in kilomoles_per_minute.

        

        :param meters: The MolarFlow value in kilomoles_per_minute.
        :type kilomoles_per_minute: float
        :return: A new instance of MolarFlow.
        :rtype: MolarFlow
        """
        return MolarFlow(kilomoles_per_minute, MolarFlowUnits.KilomolePerMinute)

    
    @staticmethod
    def from_kilomoles_per_hour(kilomoles_per_hour: float):
        """
        Create a new instance of MolarFlow from a value in kilomoles_per_hour.

        

        :param meters: The MolarFlow value in kilomoles_per_hour.
        :type kilomoles_per_hour: float
        :return: A new instance of MolarFlow.
        :rtype: MolarFlow
        """
        return MolarFlow(kilomoles_per_hour, MolarFlowUnits.KilomolePerHour)

    
    @property
    def moles_per_second(self) -> float:
        """
        
        """
        if self.__moles_per_second != None:
            return self.__moles_per_second
        self.__moles_per_second = self.__convert_from_base(MolarFlowUnits.MolePerSecond)
        return self.__moles_per_second

    
    @property
    def moles_per_minute(self) -> float:
        """
        
        """
        if self.__moles_per_minute != None:
            return self.__moles_per_minute
        self.__moles_per_minute = self.__convert_from_base(MolarFlowUnits.MolePerMinute)
        return self.__moles_per_minute

    
    @property
    def moles_per_hour(self) -> float:
        """
        
        """
        if self.__moles_per_hour != None:
            return self.__moles_per_hour
        self.__moles_per_hour = self.__convert_from_base(MolarFlowUnits.MolePerHour)
        return self.__moles_per_hour

    
    @property
    def pound_moles_per_second(self) -> float:
        """
        
        """
        if self.__pound_moles_per_second != None:
            return self.__pound_moles_per_second
        self.__pound_moles_per_second = self.__convert_from_base(MolarFlowUnits.PoundMolePerSecond)
        return self.__pound_moles_per_second

    
    @property
    def pound_moles_per_minute(self) -> float:
        """
        
        """
        if self.__pound_moles_per_minute != None:
            return self.__pound_moles_per_minute
        self.__pound_moles_per_minute = self.__convert_from_base(MolarFlowUnits.PoundMolePerMinute)
        return self.__pound_moles_per_minute

    
    @property
    def pound_moles_per_hour(self) -> float:
        """
        
        """
        if self.__pound_moles_per_hour != None:
            return self.__pound_moles_per_hour
        self.__pound_moles_per_hour = self.__convert_from_base(MolarFlowUnits.PoundMolePerHour)
        return self.__pound_moles_per_hour

    
    @property
    def kilomoles_per_second(self) -> float:
        """
        
        """
        if self.__kilomoles_per_second != None:
            return self.__kilomoles_per_second
        self.__kilomoles_per_second = self.__convert_from_base(MolarFlowUnits.KilomolePerSecond)
        return self.__kilomoles_per_second

    
    @property
    def kilomoles_per_minute(self) -> float:
        """
        
        """
        if self.__kilomoles_per_minute != None:
            return self.__kilomoles_per_minute
        self.__kilomoles_per_minute = self.__convert_from_base(MolarFlowUnits.KilomolePerMinute)
        return self.__kilomoles_per_minute

    
    @property
    def kilomoles_per_hour(self) -> float:
        """
        
        """
        if self.__kilomoles_per_hour != None:
            return self.__kilomoles_per_hour
        self.__kilomoles_per_hour = self.__convert_from_base(MolarFlowUnits.KilomolePerHour)
        return self.__kilomoles_per_hour

    
    def to_string(self, unit: MolarFlowUnits = MolarFlowUnits.MolePerSecond) -> str:
        """
        Format the MolarFlow to string.
        Note! the default format for MolarFlow is MolePerSecond.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == MolarFlowUnits.MolePerSecond:
            return f"""{self.moles_per_second} mol/s"""
        
        if unit == MolarFlowUnits.MolePerMinute:
            return f"""{self.moles_per_minute} mol/min"""
        
        if unit == MolarFlowUnits.MolePerHour:
            return f"""{self.moles_per_hour} kmol/h"""
        
        if unit == MolarFlowUnits.PoundMolePerSecond:
            return f"""{self.pound_moles_per_second} lbmol/s"""
        
        if unit == MolarFlowUnits.PoundMolePerMinute:
            return f"""{self.pound_moles_per_minute} lbmol/min"""
        
        if unit == MolarFlowUnits.PoundMolePerHour:
            return f"""{self.pound_moles_per_hour} lbmol/h"""
        
        if unit == MolarFlowUnits.KilomolePerSecond:
            return f"""{self.kilomoles_per_second} kmol/s"""
        
        if unit == MolarFlowUnits.KilomolePerMinute:
            return f"""{self.kilomoles_per_minute} kmol/min"""
        
        if unit == MolarFlowUnits.KilomolePerHour:
            return f"""{self.kilomoles_per_hour} kkmol/h"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: MolarFlowUnits = MolarFlowUnits.MolePerSecond) -> str:
        """
        Get MolarFlow unit abbreviation.
        Note! the default abbreviation for MolarFlow is MolePerSecond.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == MolarFlowUnits.MolePerSecond:
            return """mol/s"""
        
        if unit_abbreviation == MolarFlowUnits.MolePerMinute:
            return """mol/min"""
        
        if unit_abbreviation == MolarFlowUnits.MolePerHour:
            return """kmol/h"""
        
        if unit_abbreviation == MolarFlowUnits.PoundMolePerSecond:
            return """lbmol/s"""
        
        if unit_abbreviation == MolarFlowUnits.PoundMolePerMinute:
            return """lbmol/min"""
        
        if unit_abbreviation == MolarFlowUnits.PoundMolePerHour:
            return """lbmol/h"""
        
        if unit_abbreviation == MolarFlowUnits.KilomolePerSecond:
            return """kmol/s"""
        
        if unit_abbreviation == MolarFlowUnits.KilomolePerMinute:
            return """kmol/min"""
        
        if unit_abbreviation == MolarFlowUnits.KilomolePerHour:
            return """kkmol/h"""
        
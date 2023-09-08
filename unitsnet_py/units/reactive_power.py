from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class ReactivePowerUnits(Enum):
        """
            ReactivePowerUnits enumeration
        """
        
        VoltampereReactive = 'voltampere_reactive'
        """
            
        """
        
        KilovoltampereReactive = 'kilovoltampere_reactive'
        """
            
        """
        
        MegavoltampereReactive = 'megavoltampere_reactive'
        """
            
        """
        
        GigavoltampereReactive = 'gigavoltampere_reactive'
        """
            
        """
        

class ReactivePower(AbstractMeasure):
    """
    Volt-ampere reactive (var) is a unit by which reactive power is expressed in an AC electric power system. Reactive power exists in an AC circuit when the current and voltage are not in phase.

    Args:
        value (float): The value.
        from_unit (ReactivePowerUnits): The ReactivePower unit to create from, The default unit is VoltampereReactive
    """
    def __init__(self, value: float, from_unit: ReactivePowerUnits = ReactivePowerUnits.VoltampereReactive):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__voltamperes_reactive = None
        
        self.__kilovoltamperes_reactive = None
        
        self.__megavoltamperes_reactive = None
        
        self.__gigavoltamperes_reactive = None
        

    def convert(self, unit: ReactivePowerUnits) -> float:
        return self.__convert_from_base(unit)

    def __convert_from_base(self, from_unit: ReactivePowerUnits) -> float:
        value = self._value
        
        if from_unit == ReactivePowerUnits.VoltampereReactive:
            return (value)
        
        if from_unit == ReactivePowerUnits.KilovoltampereReactive:
            return ((value) / 1000.0)
        
        if from_unit == ReactivePowerUnits.MegavoltampereReactive:
            return ((value) / 1000000.0)
        
        if from_unit == ReactivePowerUnits.GigavoltampereReactive:
            return ((value) / 1000000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: ReactivePowerUnits) -> float:
        
        if to_unit == ReactivePowerUnits.VoltampereReactive:
            return (value)
        
        if to_unit == ReactivePowerUnits.KilovoltampereReactive:
            return ((value) * 1000.0)
        
        if to_unit == ReactivePowerUnits.MegavoltampereReactive:
            return ((value) * 1000000.0)
        
        if to_unit == ReactivePowerUnits.GigavoltampereReactive:
            return ((value) * 1000000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_voltamperes_reactive(voltamperes_reactive: float):
        """
        Create a new instance of ReactivePower from a value in voltamperes_reactive.

        

        :param meters: The ReactivePower value in voltamperes_reactive.
        :type voltamperes_reactive: float
        :return: A new instance of ReactivePower.
        :rtype: ReactivePower
        """
        return ReactivePower(voltamperes_reactive, ReactivePowerUnits.VoltampereReactive)

    
    @staticmethod
    def from_kilovoltamperes_reactive(kilovoltamperes_reactive: float):
        """
        Create a new instance of ReactivePower from a value in kilovoltamperes_reactive.

        

        :param meters: The ReactivePower value in kilovoltamperes_reactive.
        :type kilovoltamperes_reactive: float
        :return: A new instance of ReactivePower.
        :rtype: ReactivePower
        """
        return ReactivePower(kilovoltamperes_reactive, ReactivePowerUnits.KilovoltampereReactive)

    
    @staticmethod
    def from_megavoltamperes_reactive(megavoltamperes_reactive: float):
        """
        Create a new instance of ReactivePower from a value in megavoltamperes_reactive.

        

        :param meters: The ReactivePower value in megavoltamperes_reactive.
        :type megavoltamperes_reactive: float
        :return: A new instance of ReactivePower.
        :rtype: ReactivePower
        """
        return ReactivePower(megavoltamperes_reactive, ReactivePowerUnits.MegavoltampereReactive)

    
    @staticmethod
    def from_gigavoltamperes_reactive(gigavoltamperes_reactive: float):
        """
        Create a new instance of ReactivePower from a value in gigavoltamperes_reactive.

        

        :param meters: The ReactivePower value in gigavoltamperes_reactive.
        :type gigavoltamperes_reactive: float
        :return: A new instance of ReactivePower.
        :rtype: ReactivePower
        """
        return ReactivePower(gigavoltamperes_reactive, ReactivePowerUnits.GigavoltampereReactive)

    
    @property
    def voltamperes_reactive(self) -> float:
        """
        
        """
        if self.__voltamperes_reactive != None:
            return self.__voltamperes_reactive
        self.__voltamperes_reactive = self.__convert_from_base(ReactivePowerUnits.VoltampereReactive)
        return self.__voltamperes_reactive

    
    @property
    def kilovoltamperes_reactive(self) -> float:
        """
        
        """
        if self.__kilovoltamperes_reactive != None:
            return self.__kilovoltamperes_reactive
        self.__kilovoltamperes_reactive = self.__convert_from_base(ReactivePowerUnits.KilovoltampereReactive)
        return self.__kilovoltamperes_reactive

    
    @property
    def megavoltamperes_reactive(self) -> float:
        """
        
        """
        if self.__megavoltamperes_reactive != None:
            return self.__megavoltamperes_reactive
        self.__megavoltamperes_reactive = self.__convert_from_base(ReactivePowerUnits.MegavoltampereReactive)
        return self.__megavoltamperes_reactive

    
    @property
    def gigavoltamperes_reactive(self) -> float:
        """
        
        """
        if self.__gigavoltamperes_reactive != None:
            return self.__gigavoltamperes_reactive
        self.__gigavoltamperes_reactive = self.__convert_from_base(ReactivePowerUnits.GigavoltampereReactive)
        return self.__gigavoltamperes_reactive

    
    def to_string(self, unit: ReactivePowerUnits = ReactivePowerUnits.VoltampereReactive) -> str:
        """
        Format the ReactivePower to string.
        Note! the default format for ReactivePower is VoltampereReactive.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == ReactivePowerUnits.VoltampereReactive:
            return f"""{self.voltamperes_reactive} var"""
        
        if unit == ReactivePowerUnits.KilovoltampereReactive:
            return f"""{self.kilovoltamperes_reactive} kvar"""
        
        if unit == ReactivePowerUnits.MegavoltampereReactive:
            return f"""{self.megavoltamperes_reactive} Mvar"""
        
        if unit == ReactivePowerUnits.GigavoltampereReactive:
            return f"""{self.gigavoltamperes_reactive} Gvar"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: ReactivePowerUnits = ReactivePowerUnits.VoltampereReactive) -> str:
        """
        Get ReactivePower unit abbreviation.
        Note! the default abbreviation for ReactivePower is VoltampereReactive.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == ReactivePowerUnits.VoltampereReactive:
            return """var"""
        
        if unit_abbreviation == ReactivePowerUnits.KilovoltampereReactive:
            return """kvar"""
        
        if unit_abbreviation == ReactivePowerUnits.MegavoltampereReactive:
            return """Mvar"""
        
        if unit_abbreviation == ReactivePowerUnits.GigavoltampereReactive:
            return """Gvar"""
        
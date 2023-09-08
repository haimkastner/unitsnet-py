from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class ReactiveEnergyUnits(Enum):
        """
            ReactiveEnergyUnits enumeration
        """
        
        VoltampereReactiveHour = 'voltampere_reactive_hour'
        """
            
        """
        
        KilovoltampereReactiveHour = 'kilovoltampere_reactive_hour'
        """
            
        """
        
        MegavoltampereReactiveHour = 'megavoltampere_reactive_hour'
        """
            
        """
        

class ReactiveEnergy(AbstractMeasure):
    """
    The Volt-ampere reactive hour (expressed as varh) is the reactive power of one Volt-ampere reactive produced in one hour.

    Args:
        value (float): The value.
        from_unit (ReactiveEnergyUnits): The ReactiveEnergy unit to create from, The default unit is VoltampereReactiveHour
    """
    def __init__(self, value: float, from_unit: ReactiveEnergyUnits = ReactiveEnergyUnits.VoltampereReactiveHour):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__voltampere_reactive_hours = None
        
        self.__kilovoltampere_reactive_hours = None
        
        self.__megavoltampere_reactive_hours = None
        

    def convert(self, unit: ReactiveEnergyUnits) -> float:
        return self.__convert_from_base(unit)

    def __convert_from_base(self, from_unit: ReactiveEnergyUnits) -> float:
        value = self._value
        
        if from_unit == ReactiveEnergyUnits.VoltampereReactiveHour:
            return (value)
        
        if from_unit == ReactiveEnergyUnits.KilovoltampereReactiveHour:
            return ((value) / 1000.0)
        
        if from_unit == ReactiveEnergyUnits.MegavoltampereReactiveHour:
            return ((value) / 1000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: ReactiveEnergyUnits) -> float:
        
        if to_unit == ReactiveEnergyUnits.VoltampereReactiveHour:
            return (value)
        
        if to_unit == ReactiveEnergyUnits.KilovoltampereReactiveHour:
            return ((value) * 1000.0)
        
        if to_unit == ReactiveEnergyUnits.MegavoltampereReactiveHour:
            return ((value) * 1000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_voltampere_reactive_hours(voltampere_reactive_hours: float):
        """
        Create a new instance of ReactiveEnergy from a value in voltampere_reactive_hours.

        

        :param meters: The ReactiveEnergy value in voltampere_reactive_hours.
        :type voltampere_reactive_hours: float
        :return: A new instance of ReactiveEnergy.
        :rtype: ReactiveEnergy
        """
        return ReactiveEnergy(voltampere_reactive_hours, ReactiveEnergyUnits.VoltampereReactiveHour)

    
    @staticmethod
    def from_kilovoltampere_reactive_hours(kilovoltampere_reactive_hours: float):
        """
        Create a new instance of ReactiveEnergy from a value in kilovoltampere_reactive_hours.

        

        :param meters: The ReactiveEnergy value in kilovoltampere_reactive_hours.
        :type kilovoltampere_reactive_hours: float
        :return: A new instance of ReactiveEnergy.
        :rtype: ReactiveEnergy
        """
        return ReactiveEnergy(kilovoltampere_reactive_hours, ReactiveEnergyUnits.KilovoltampereReactiveHour)

    
    @staticmethod
    def from_megavoltampere_reactive_hours(megavoltampere_reactive_hours: float):
        """
        Create a new instance of ReactiveEnergy from a value in megavoltampere_reactive_hours.

        

        :param meters: The ReactiveEnergy value in megavoltampere_reactive_hours.
        :type megavoltampere_reactive_hours: float
        :return: A new instance of ReactiveEnergy.
        :rtype: ReactiveEnergy
        """
        return ReactiveEnergy(megavoltampere_reactive_hours, ReactiveEnergyUnits.MegavoltampereReactiveHour)

    
    @property
    def voltampere_reactive_hours(self) -> float:
        """
        
        """
        if self.__voltampere_reactive_hours != None:
            return self.__voltampere_reactive_hours
        self.__voltampere_reactive_hours = self.__convert_from_base(ReactiveEnergyUnits.VoltampereReactiveHour)
        return self.__voltampere_reactive_hours

    
    @property
    def kilovoltampere_reactive_hours(self) -> float:
        """
        
        """
        if self.__kilovoltampere_reactive_hours != None:
            return self.__kilovoltampere_reactive_hours
        self.__kilovoltampere_reactive_hours = self.__convert_from_base(ReactiveEnergyUnits.KilovoltampereReactiveHour)
        return self.__kilovoltampere_reactive_hours

    
    @property
    def megavoltampere_reactive_hours(self) -> float:
        """
        
        """
        if self.__megavoltampere_reactive_hours != None:
            return self.__megavoltampere_reactive_hours
        self.__megavoltampere_reactive_hours = self.__convert_from_base(ReactiveEnergyUnits.MegavoltampereReactiveHour)
        return self.__megavoltampere_reactive_hours

    
    def to_string(self, unit: ReactiveEnergyUnits = ReactiveEnergyUnits.VoltampereReactiveHour) -> str:
        """
        Format the ReactiveEnergy to string.
        Note! the default format for ReactiveEnergy is VoltampereReactiveHour.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == ReactiveEnergyUnits.VoltampereReactiveHour:
            return f"""{self.voltampere_reactive_hours} varh"""
        
        if unit == ReactiveEnergyUnits.KilovoltampereReactiveHour:
            return f"""{self.kilovoltampere_reactive_hours} kvarh"""
        
        if unit == ReactiveEnergyUnits.MegavoltampereReactiveHour:
            return f"""{self.megavoltampere_reactive_hours} Mvarh"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: ReactiveEnergyUnits = ReactiveEnergyUnits.VoltampereReactiveHour) -> str:
        """
        Get ReactiveEnergy unit abbreviation.
        Note! the default abbreviation for ReactiveEnergy is VoltampereReactiveHour.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == ReactiveEnergyUnits.VoltampereReactiveHour:
            return """varh"""
        
        if unit_abbreviation == ReactiveEnergyUnits.KilovoltampereReactiveHour:
            return """kvarh"""
        
        if unit_abbreviation == ReactiveEnergyUnits.MegavoltampereReactiveHour:
            return """Mvarh"""
        
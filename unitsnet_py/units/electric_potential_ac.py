from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class ElectricPotentialAcUnits(Enum):
        """
            ElectricPotentialAcUnits enumeration
        """
        
        VoltAc = 'volt_ac'
        """
            
        """
        
        MicrovoltAc = 'microvolt_ac'
        """
            
        """
        
        MillivoltAc = 'millivolt_ac'
        """
            
        """
        
        KilovoltAc = 'kilovolt_ac'
        """
            
        """
        
        MegavoltAc = 'megavolt_ac'
        """
            
        """
        

class ElectricPotentialAc(AbstractMeasure):
    """
    The Electric Potential of a system known to use Alternating Current.

    Args:
        value (float): The value.
        from_unit (ElectricPotentialAcUnits): The ElectricPotentialAc unit to create from, The default unit is VoltAc
    """
    def __init__(self, value: float, from_unit: ElectricPotentialAcUnits = ElectricPotentialAcUnits.VoltAc):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__volts_ac = None
        
        self.__microvolts_ac = None
        
        self.__millivolts_ac = None
        
        self.__kilovolts_ac = None
        
        self.__megavolts_ac = None
        

    def convert(self, unit: ElectricPotentialAcUnits) -> float:
        return self.__convert_from_base(unit)

    def __convert_from_base(self, from_unit: ElectricPotentialAcUnits) -> float:
        value = self._value
        
        if from_unit == ElectricPotentialAcUnits.VoltAc:
            return (value)
        
        if from_unit == ElectricPotentialAcUnits.MicrovoltAc:
            return ((value) / 1e-06)
        
        if from_unit == ElectricPotentialAcUnits.MillivoltAc:
            return ((value) / 0.001)
        
        if from_unit == ElectricPotentialAcUnits.KilovoltAc:
            return ((value) / 1000.0)
        
        if from_unit == ElectricPotentialAcUnits.MegavoltAc:
            return ((value) / 1000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: ElectricPotentialAcUnits) -> float:
        
        if to_unit == ElectricPotentialAcUnits.VoltAc:
            return (value)
        
        if to_unit == ElectricPotentialAcUnits.MicrovoltAc:
            return ((value) * 1e-06)
        
        if to_unit == ElectricPotentialAcUnits.MillivoltAc:
            return ((value) * 0.001)
        
        if to_unit == ElectricPotentialAcUnits.KilovoltAc:
            return ((value) * 1000.0)
        
        if to_unit == ElectricPotentialAcUnits.MegavoltAc:
            return ((value) * 1000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_volts_ac(volts_ac: float):
        """
        Create a new instance of ElectricPotentialAc from a value in volts_ac.

        

        :param meters: The ElectricPotentialAc value in volts_ac.
        :type volts_ac: float
        :return: A new instance of ElectricPotentialAc.
        :rtype: ElectricPotentialAc
        """
        return ElectricPotentialAc(volts_ac, ElectricPotentialAcUnits.VoltAc)

    
    @staticmethod
    def from_microvolts_ac(microvolts_ac: float):
        """
        Create a new instance of ElectricPotentialAc from a value in microvolts_ac.

        

        :param meters: The ElectricPotentialAc value in microvolts_ac.
        :type microvolts_ac: float
        :return: A new instance of ElectricPotentialAc.
        :rtype: ElectricPotentialAc
        """
        return ElectricPotentialAc(microvolts_ac, ElectricPotentialAcUnits.MicrovoltAc)

    
    @staticmethod
    def from_millivolts_ac(millivolts_ac: float):
        """
        Create a new instance of ElectricPotentialAc from a value in millivolts_ac.

        

        :param meters: The ElectricPotentialAc value in millivolts_ac.
        :type millivolts_ac: float
        :return: A new instance of ElectricPotentialAc.
        :rtype: ElectricPotentialAc
        """
        return ElectricPotentialAc(millivolts_ac, ElectricPotentialAcUnits.MillivoltAc)

    
    @staticmethod
    def from_kilovolts_ac(kilovolts_ac: float):
        """
        Create a new instance of ElectricPotentialAc from a value in kilovolts_ac.

        

        :param meters: The ElectricPotentialAc value in kilovolts_ac.
        :type kilovolts_ac: float
        :return: A new instance of ElectricPotentialAc.
        :rtype: ElectricPotentialAc
        """
        return ElectricPotentialAc(kilovolts_ac, ElectricPotentialAcUnits.KilovoltAc)

    
    @staticmethod
    def from_megavolts_ac(megavolts_ac: float):
        """
        Create a new instance of ElectricPotentialAc from a value in megavolts_ac.

        

        :param meters: The ElectricPotentialAc value in megavolts_ac.
        :type megavolts_ac: float
        :return: A new instance of ElectricPotentialAc.
        :rtype: ElectricPotentialAc
        """
        return ElectricPotentialAc(megavolts_ac, ElectricPotentialAcUnits.MegavoltAc)

    
    @property
    def volts_ac(self) -> float:
        """
        
        """
        if self.__volts_ac != None:
            return self.__volts_ac
        self.__volts_ac = self.__convert_from_base(ElectricPotentialAcUnits.VoltAc)
        return self.__volts_ac

    
    @property
    def microvolts_ac(self) -> float:
        """
        
        """
        if self.__microvolts_ac != None:
            return self.__microvolts_ac
        self.__microvolts_ac = self.__convert_from_base(ElectricPotentialAcUnits.MicrovoltAc)
        return self.__microvolts_ac

    
    @property
    def millivolts_ac(self) -> float:
        """
        
        """
        if self.__millivolts_ac != None:
            return self.__millivolts_ac
        self.__millivolts_ac = self.__convert_from_base(ElectricPotentialAcUnits.MillivoltAc)
        return self.__millivolts_ac

    
    @property
    def kilovolts_ac(self) -> float:
        """
        
        """
        if self.__kilovolts_ac != None:
            return self.__kilovolts_ac
        self.__kilovolts_ac = self.__convert_from_base(ElectricPotentialAcUnits.KilovoltAc)
        return self.__kilovolts_ac

    
    @property
    def megavolts_ac(self) -> float:
        """
        
        """
        if self.__megavolts_ac != None:
            return self.__megavolts_ac
        self.__megavolts_ac = self.__convert_from_base(ElectricPotentialAcUnits.MegavoltAc)
        return self.__megavolts_ac

    
    def to_string(self, unit: ElectricPotentialAcUnits = ElectricPotentialAcUnits.VoltAc) -> str:
        """
        Format the ElectricPotentialAc to string.
        Note! the default format for ElectricPotentialAc is VoltAc.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == ElectricPotentialAcUnits.VoltAc:
            return f"""{self.volts_ac} Vac"""
        
        if unit == ElectricPotentialAcUnits.MicrovoltAc:
            return f"""{self.microvolts_ac} μVac"""
        
        if unit == ElectricPotentialAcUnits.MillivoltAc:
            return f"""{self.millivolts_ac} mVac"""
        
        if unit == ElectricPotentialAcUnits.KilovoltAc:
            return f"""{self.kilovolts_ac} kVac"""
        
        if unit == ElectricPotentialAcUnits.MegavoltAc:
            return f"""{self.megavolts_ac} MVac"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: ElectricPotentialAcUnits = ElectricPotentialAcUnits.VoltAc) -> str:
        """
        Get ElectricPotentialAc unit abbreviation.
        Note! the default abbreviation for ElectricPotentialAc is VoltAc.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == ElectricPotentialAcUnits.VoltAc:
            return """Vac"""
        
        if unit_abbreviation == ElectricPotentialAcUnits.MicrovoltAc:
            return """μVac"""
        
        if unit_abbreviation == ElectricPotentialAcUnits.MillivoltAc:
            return """mVac"""
        
        if unit_abbreviation == ElectricPotentialAcUnits.KilovoltAc:
            return """kVac"""
        
        if unit_abbreviation == ElectricPotentialAcUnits.MegavoltAc:
            return """MVac"""
        
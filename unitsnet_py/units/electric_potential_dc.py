from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class ElectricPotentialDcUnits(Enum):
        """
            ElectricPotentialDcUnits enumeration
        """
        
        VoltDc = 'volt_dc'
        """
            
        """
        
        MicrovoltDc = 'microvolt_dc'
        """
            
        """
        
        MillivoltDc = 'millivolt_dc'
        """
            
        """
        
        KilovoltDc = 'kilovolt_dc'
        """
            
        """
        
        MegavoltDc = 'megavolt_dc'
        """
            
        """
        

class ElectricPotentialDc(AbstractMeasure):
    """
    The Electric Potential of a system known to use Direct Current.

    Args:
        value (float): The value.
        from_unit (ElectricPotentialDcUnits): The ElectricPotentialDc unit to create from, The default unit is VoltDc
    """
    def __init__(self, value: float, from_unit: ElectricPotentialDcUnits = ElectricPotentialDcUnits.VoltDc):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__volts_dc = None
        
        self.__microvolts_dc = None
        
        self.__millivolts_dc = None
        
        self.__kilovolts_dc = None
        
        self.__megavolts_dc = None
        

    def convert(self, unit: ElectricPotentialDcUnits) -> float:
        return self.__convert_from_base(unit)

    def __convert_from_base(self, from_unit: ElectricPotentialDcUnits) -> float:
        value = self._value
        
        if from_unit == ElectricPotentialDcUnits.VoltDc:
            return (value)
        
        if from_unit == ElectricPotentialDcUnits.MicrovoltDc:
            return ((value) / 1e-06)
        
        if from_unit == ElectricPotentialDcUnits.MillivoltDc:
            return ((value) / 0.001)
        
        if from_unit == ElectricPotentialDcUnits.KilovoltDc:
            return ((value) / 1000.0)
        
        if from_unit == ElectricPotentialDcUnits.MegavoltDc:
            return ((value) / 1000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: ElectricPotentialDcUnits) -> float:
        
        if to_unit == ElectricPotentialDcUnits.VoltDc:
            return (value)
        
        if to_unit == ElectricPotentialDcUnits.MicrovoltDc:
            return ((value) * 1e-06)
        
        if to_unit == ElectricPotentialDcUnits.MillivoltDc:
            return ((value) * 0.001)
        
        if to_unit == ElectricPotentialDcUnits.KilovoltDc:
            return ((value) * 1000.0)
        
        if to_unit == ElectricPotentialDcUnits.MegavoltDc:
            return ((value) * 1000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_volts_dc(volts_dc: float):
        """
        Create a new instance of ElectricPotentialDc from a value in volts_dc.

        

        :param meters: The ElectricPotentialDc value in volts_dc.
        :type volts_dc: float
        :return: A new instance of ElectricPotentialDc.
        :rtype: ElectricPotentialDc
        """
        return ElectricPotentialDc(volts_dc, ElectricPotentialDcUnits.VoltDc)

    
    @staticmethod
    def from_microvolts_dc(microvolts_dc: float):
        """
        Create a new instance of ElectricPotentialDc from a value in microvolts_dc.

        

        :param meters: The ElectricPotentialDc value in microvolts_dc.
        :type microvolts_dc: float
        :return: A new instance of ElectricPotentialDc.
        :rtype: ElectricPotentialDc
        """
        return ElectricPotentialDc(microvolts_dc, ElectricPotentialDcUnits.MicrovoltDc)

    
    @staticmethod
    def from_millivolts_dc(millivolts_dc: float):
        """
        Create a new instance of ElectricPotentialDc from a value in millivolts_dc.

        

        :param meters: The ElectricPotentialDc value in millivolts_dc.
        :type millivolts_dc: float
        :return: A new instance of ElectricPotentialDc.
        :rtype: ElectricPotentialDc
        """
        return ElectricPotentialDc(millivolts_dc, ElectricPotentialDcUnits.MillivoltDc)

    
    @staticmethod
    def from_kilovolts_dc(kilovolts_dc: float):
        """
        Create a new instance of ElectricPotentialDc from a value in kilovolts_dc.

        

        :param meters: The ElectricPotentialDc value in kilovolts_dc.
        :type kilovolts_dc: float
        :return: A new instance of ElectricPotentialDc.
        :rtype: ElectricPotentialDc
        """
        return ElectricPotentialDc(kilovolts_dc, ElectricPotentialDcUnits.KilovoltDc)

    
    @staticmethod
    def from_megavolts_dc(megavolts_dc: float):
        """
        Create a new instance of ElectricPotentialDc from a value in megavolts_dc.

        

        :param meters: The ElectricPotentialDc value in megavolts_dc.
        :type megavolts_dc: float
        :return: A new instance of ElectricPotentialDc.
        :rtype: ElectricPotentialDc
        """
        return ElectricPotentialDc(megavolts_dc, ElectricPotentialDcUnits.MegavoltDc)

    
    @property
    def volts_dc(self) -> float:
        """
        
        """
        if self.__volts_dc != None:
            return self.__volts_dc
        self.__volts_dc = self.__convert_from_base(ElectricPotentialDcUnits.VoltDc)
        return self.__volts_dc

    
    @property
    def microvolts_dc(self) -> float:
        """
        
        """
        if self.__microvolts_dc != None:
            return self.__microvolts_dc
        self.__microvolts_dc = self.__convert_from_base(ElectricPotentialDcUnits.MicrovoltDc)
        return self.__microvolts_dc

    
    @property
    def millivolts_dc(self) -> float:
        """
        
        """
        if self.__millivolts_dc != None:
            return self.__millivolts_dc
        self.__millivolts_dc = self.__convert_from_base(ElectricPotentialDcUnits.MillivoltDc)
        return self.__millivolts_dc

    
    @property
    def kilovolts_dc(self) -> float:
        """
        
        """
        if self.__kilovolts_dc != None:
            return self.__kilovolts_dc
        self.__kilovolts_dc = self.__convert_from_base(ElectricPotentialDcUnits.KilovoltDc)
        return self.__kilovolts_dc

    
    @property
    def megavolts_dc(self) -> float:
        """
        
        """
        if self.__megavolts_dc != None:
            return self.__megavolts_dc
        self.__megavolts_dc = self.__convert_from_base(ElectricPotentialDcUnits.MegavoltDc)
        return self.__megavolts_dc

    
    def to_string(self, unit: ElectricPotentialDcUnits = ElectricPotentialDcUnits.VoltDc) -> str:
        """
        Format the ElectricPotentialDc to string.
        Note! the default format for ElectricPotentialDc is VoltDc.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == ElectricPotentialDcUnits.VoltDc:
            return f"""{self.volts_dc} Vdc"""
        
        if unit == ElectricPotentialDcUnits.MicrovoltDc:
            return f"""{self.microvolts_dc} μVdc"""
        
        if unit == ElectricPotentialDcUnits.MillivoltDc:
            return f"""{self.millivolts_dc} mVdc"""
        
        if unit == ElectricPotentialDcUnits.KilovoltDc:
            return f"""{self.kilovolts_dc} kVdc"""
        
        if unit == ElectricPotentialDcUnits.MegavoltDc:
            return f"""{self.megavolts_dc} MVdc"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: ElectricPotentialDcUnits = ElectricPotentialDcUnits.VoltDc) -> str:
        """
        Get ElectricPotentialDc unit abbreviation.
        Note! the default abbreviation for ElectricPotentialDc is VoltDc.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == ElectricPotentialDcUnits.VoltDc:
            return """Vdc"""
        
        if unit_abbreviation == ElectricPotentialDcUnits.MicrovoltDc:
            return """μVdc"""
        
        if unit_abbreviation == ElectricPotentialDcUnits.MillivoltDc:
            return """mVdc"""
        
        if unit_abbreviation == ElectricPotentialDcUnits.KilovoltDc:
            return """kVdc"""
        
        if unit_abbreviation == ElectricPotentialDcUnits.MegavoltDc:
            return """MVdc"""
        
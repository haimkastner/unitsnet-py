from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class ElectricPotentialUnits(Enum):
        """
            ElectricPotentialUnits enumeration
        """
        
        Volt = 'volt'
        """
            
        """
        
        Nanovolt = 'nanovolt'
        """
            
        """
        
        Microvolt = 'microvolt'
        """
            
        """
        
        Millivolt = 'millivolt'
        """
            
        """
        
        Kilovolt = 'kilovolt'
        """
            
        """
        
        Megavolt = 'megavolt'
        """
            
        """
        

class ElectricPotential(AbstractMeasure):
    """
    In classical electromagnetism, the electric potential (a scalar quantity denoted by Φ, ΦE or V and also called the electric field potential or the electrostatic potential) at a point is the amount of electric potential energy that a unitary point charge would have when located at that point.

    Args:
        value (float): The value.
        from_unit (ElectricPotentialUnits): The ElectricPotential unit to create from, The default unit is Volt
    """
    def __init__(self, value: float, from_unit: ElectricPotentialUnits = ElectricPotentialUnits.Volt):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__volts = None
        
        self.__nanovolts = None
        
        self.__microvolts = None
        
        self.__millivolts = None
        
        self.__kilovolts = None
        
        self.__megavolts = None
        

    def convert(self, unit: ElectricPotentialUnits) -> float:
        return self.__convert_from_base(unit)

    def __convert_from_base(self, from_unit: ElectricPotentialUnits) -> float:
        value = self._value
        
        if from_unit == ElectricPotentialUnits.Volt:
            return (value)
        
        if from_unit == ElectricPotentialUnits.Nanovolt:
            return ((value) / 1e-09)
        
        if from_unit == ElectricPotentialUnits.Microvolt:
            return ((value) / 1e-06)
        
        if from_unit == ElectricPotentialUnits.Millivolt:
            return ((value) / 0.001)
        
        if from_unit == ElectricPotentialUnits.Kilovolt:
            return ((value) / 1000.0)
        
        if from_unit == ElectricPotentialUnits.Megavolt:
            return ((value) / 1000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: ElectricPotentialUnits) -> float:
        
        if to_unit == ElectricPotentialUnits.Volt:
            return (value)
        
        if to_unit == ElectricPotentialUnits.Nanovolt:
            return ((value) * 1e-09)
        
        if to_unit == ElectricPotentialUnits.Microvolt:
            return ((value) * 1e-06)
        
        if to_unit == ElectricPotentialUnits.Millivolt:
            return ((value) * 0.001)
        
        if to_unit == ElectricPotentialUnits.Kilovolt:
            return ((value) * 1000.0)
        
        if to_unit == ElectricPotentialUnits.Megavolt:
            return ((value) * 1000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_volts(volts: float):
        """
        Create a new instance of ElectricPotential from a value in volts.

        

        :param meters: The ElectricPotential value in volts.
        :type volts: float
        :return: A new instance of ElectricPotential.
        :rtype: ElectricPotential
        """
        return ElectricPotential(volts, ElectricPotentialUnits.Volt)

    
    @staticmethod
    def from_nanovolts(nanovolts: float):
        """
        Create a new instance of ElectricPotential from a value in nanovolts.

        

        :param meters: The ElectricPotential value in nanovolts.
        :type nanovolts: float
        :return: A new instance of ElectricPotential.
        :rtype: ElectricPotential
        """
        return ElectricPotential(nanovolts, ElectricPotentialUnits.Nanovolt)

    
    @staticmethod
    def from_microvolts(microvolts: float):
        """
        Create a new instance of ElectricPotential from a value in microvolts.

        

        :param meters: The ElectricPotential value in microvolts.
        :type microvolts: float
        :return: A new instance of ElectricPotential.
        :rtype: ElectricPotential
        """
        return ElectricPotential(microvolts, ElectricPotentialUnits.Microvolt)

    
    @staticmethod
    def from_millivolts(millivolts: float):
        """
        Create a new instance of ElectricPotential from a value in millivolts.

        

        :param meters: The ElectricPotential value in millivolts.
        :type millivolts: float
        :return: A new instance of ElectricPotential.
        :rtype: ElectricPotential
        """
        return ElectricPotential(millivolts, ElectricPotentialUnits.Millivolt)

    
    @staticmethod
    def from_kilovolts(kilovolts: float):
        """
        Create a new instance of ElectricPotential from a value in kilovolts.

        

        :param meters: The ElectricPotential value in kilovolts.
        :type kilovolts: float
        :return: A new instance of ElectricPotential.
        :rtype: ElectricPotential
        """
        return ElectricPotential(kilovolts, ElectricPotentialUnits.Kilovolt)

    
    @staticmethod
    def from_megavolts(megavolts: float):
        """
        Create a new instance of ElectricPotential from a value in megavolts.

        

        :param meters: The ElectricPotential value in megavolts.
        :type megavolts: float
        :return: A new instance of ElectricPotential.
        :rtype: ElectricPotential
        """
        return ElectricPotential(megavolts, ElectricPotentialUnits.Megavolt)

    
    @property
    def volts(self) -> float:
        """
        
        """
        if self.__volts != None:
            return self.__volts
        self.__volts = self.__convert_from_base(ElectricPotentialUnits.Volt)
        return self.__volts

    
    @property
    def nanovolts(self) -> float:
        """
        
        """
        if self.__nanovolts != None:
            return self.__nanovolts
        self.__nanovolts = self.__convert_from_base(ElectricPotentialUnits.Nanovolt)
        return self.__nanovolts

    
    @property
    def microvolts(self) -> float:
        """
        
        """
        if self.__microvolts != None:
            return self.__microvolts
        self.__microvolts = self.__convert_from_base(ElectricPotentialUnits.Microvolt)
        return self.__microvolts

    
    @property
    def millivolts(self) -> float:
        """
        
        """
        if self.__millivolts != None:
            return self.__millivolts
        self.__millivolts = self.__convert_from_base(ElectricPotentialUnits.Millivolt)
        return self.__millivolts

    
    @property
    def kilovolts(self) -> float:
        """
        
        """
        if self.__kilovolts != None:
            return self.__kilovolts
        self.__kilovolts = self.__convert_from_base(ElectricPotentialUnits.Kilovolt)
        return self.__kilovolts

    
    @property
    def megavolts(self) -> float:
        """
        
        """
        if self.__megavolts != None:
            return self.__megavolts
        self.__megavolts = self.__convert_from_base(ElectricPotentialUnits.Megavolt)
        return self.__megavolts

    
    def to_string(self, unit: ElectricPotentialUnits = ElectricPotentialUnits.Volt) -> str:
        """
        Format the ElectricPotential to string.
        Note! the default format for ElectricPotential is Volt.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == ElectricPotentialUnits.Volt:
            return f"""{self.volts} V"""
        
        if unit == ElectricPotentialUnits.Nanovolt:
            return f"""{self.nanovolts} nV"""
        
        if unit == ElectricPotentialUnits.Microvolt:
            return f"""{self.microvolts} μV"""
        
        if unit == ElectricPotentialUnits.Millivolt:
            return f"""{self.millivolts} mV"""
        
        if unit == ElectricPotentialUnits.Kilovolt:
            return f"""{self.kilovolts} kV"""
        
        if unit == ElectricPotentialUnits.Megavolt:
            return f"""{self.megavolts} MV"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: ElectricPotentialUnits = ElectricPotentialUnits.Volt) -> str:
        """
        Get ElectricPotential unit abbreviation.
        Note! the default abbreviation for ElectricPotential is Volt.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == ElectricPotentialUnits.Volt:
            return """V"""
        
        if unit_abbreviation == ElectricPotentialUnits.Nanovolt:
            return """nV"""
        
        if unit_abbreviation == ElectricPotentialUnits.Microvolt:
            return """μV"""
        
        if unit_abbreviation == ElectricPotentialUnits.Millivolt:
            return """mV"""
        
        if unit_abbreviation == ElectricPotentialUnits.Kilovolt:
            return """kV"""
        
        if unit_abbreviation == ElectricPotentialUnits.Megavolt:
            return """MV"""
        
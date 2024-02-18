from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class RadiationEquivalentDoseUnits(Enum):
        """
            RadiationEquivalentDoseUnits enumeration
        """
        
        Sievert = 'sievert'
        """
            The sievert is a unit in the International System of Units (SI) intended to represent the stochastic health risk of ionizing radiation, which is defined as the probability of causing radiation-induced cancer and genetic damage.
        """
        
        RoentgenEquivalentMan = 'roentgen_equivalent_man'
        """
            
        """
        
        Nanosievert = 'nanosievert'
        """
            
        """
        
        Microsievert = 'microsievert'
        """
            
        """
        
        Millisievert = 'millisievert'
        """
            
        """
        
        MilliroentgenEquivalentMan = 'milliroentgen_equivalent_man'
        """
            
        """
        

class RadiationEquivalentDose(AbstractMeasure):
    """
    Equivalent dose is a dose quantity representing the stochastic health effects of low levels of ionizing radiation on the human body which represents the probability of radiation-induced cancer and genetic damage.

    Args:
        value (float): The value.
        from_unit (RadiationEquivalentDoseUnits): The RadiationEquivalentDose unit to create from, The default unit is Sievert
    """
    def __init__(self, value: float, from_unit: RadiationEquivalentDoseUnits = RadiationEquivalentDoseUnits.Sievert):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__sieverts = None
        
        self.__roentgens_equivalent_man = None
        
        self.__nanosieverts = None
        
        self.__microsieverts = None
        
        self.__millisieverts = None
        
        self.__milliroentgens_equivalent_man = None
        

    def convert(self, unit: RadiationEquivalentDoseUnits) -> float:
        return self.__convert_from_base(unit)

    def __convert_from_base(self, from_unit: RadiationEquivalentDoseUnits) -> float:
        value = self._value
        
        if from_unit == RadiationEquivalentDoseUnits.Sievert:
            return (value)
        
        if from_unit == RadiationEquivalentDoseUnits.RoentgenEquivalentMan:
            return (value * 100)
        
        if from_unit == RadiationEquivalentDoseUnits.Nanosievert:
            return ((value) / 1e-09)
        
        if from_unit == RadiationEquivalentDoseUnits.Microsievert:
            return ((value) / 1e-06)
        
        if from_unit == RadiationEquivalentDoseUnits.Millisievert:
            return ((value) / 0.001)
        
        if from_unit == RadiationEquivalentDoseUnits.MilliroentgenEquivalentMan:
            return ((value * 100) / 0.001)
        
        return None


    def __convert_to_base(self, value: float, to_unit: RadiationEquivalentDoseUnits) -> float:
        
        if to_unit == RadiationEquivalentDoseUnits.Sievert:
            return (value)
        
        if to_unit == RadiationEquivalentDoseUnits.RoentgenEquivalentMan:
            return (value / 100)
        
        if to_unit == RadiationEquivalentDoseUnits.Nanosievert:
            return ((value) * 1e-09)
        
        if to_unit == RadiationEquivalentDoseUnits.Microsievert:
            return ((value) * 1e-06)
        
        if to_unit == RadiationEquivalentDoseUnits.Millisievert:
            return ((value) * 0.001)
        
        if to_unit == RadiationEquivalentDoseUnits.MilliroentgenEquivalentMan:
            return ((value / 100) * 0.001)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_sieverts(sieverts: float):
        """
        Create a new instance of RadiationEquivalentDose from a value in sieverts.

        The sievert is a unit in the International System of Units (SI) intended to represent the stochastic health risk of ionizing radiation, which is defined as the probability of causing radiation-induced cancer and genetic damage.

        :param meters: The RadiationEquivalentDose value in sieverts.
        :type sieverts: float
        :return: A new instance of RadiationEquivalentDose.
        :rtype: RadiationEquivalentDose
        """
        return RadiationEquivalentDose(sieverts, RadiationEquivalentDoseUnits.Sievert)

    
    @staticmethod
    def from_roentgens_equivalent_man(roentgens_equivalent_man: float):
        """
        Create a new instance of RadiationEquivalentDose from a value in roentgens_equivalent_man.

        

        :param meters: The RadiationEquivalentDose value in roentgens_equivalent_man.
        :type roentgens_equivalent_man: float
        :return: A new instance of RadiationEquivalentDose.
        :rtype: RadiationEquivalentDose
        """
        return RadiationEquivalentDose(roentgens_equivalent_man, RadiationEquivalentDoseUnits.RoentgenEquivalentMan)

    
    @staticmethod
    def from_nanosieverts(nanosieverts: float):
        """
        Create a new instance of RadiationEquivalentDose from a value in nanosieverts.

        

        :param meters: The RadiationEquivalentDose value in nanosieverts.
        :type nanosieverts: float
        :return: A new instance of RadiationEquivalentDose.
        :rtype: RadiationEquivalentDose
        """
        return RadiationEquivalentDose(nanosieverts, RadiationEquivalentDoseUnits.Nanosievert)

    
    @staticmethod
    def from_microsieverts(microsieverts: float):
        """
        Create a new instance of RadiationEquivalentDose from a value in microsieverts.

        

        :param meters: The RadiationEquivalentDose value in microsieverts.
        :type microsieverts: float
        :return: A new instance of RadiationEquivalentDose.
        :rtype: RadiationEquivalentDose
        """
        return RadiationEquivalentDose(microsieverts, RadiationEquivalentDoseUnits.Microsievert)

    
    @staticmethod
    def from_millisieverts(millisieverts: float):
        """
        Create a new instance of RadiationEquivalentDose from a value in millisieverts.

        

        :param meters: The RadiationEquivalentDose value in millisieverts.
        :type millisieverts: float
        :return: A new instance of RadiationEquivalentDose.
        :rtype: RadiationEquivalentDose
        """
        return RadiationEquivalentDose(millisieverts, RadiationEquivalentDoseUnits.Millisievert)

    
    @staticmethod
    def from_milliroentgens_equivalent_man(milliroentgens_equivalent_man: float):
        """
        Create a new instance of RadiationEquivalentDose from a value in milliroentgens_equivalent_man.

        

        :param meters: The RadiationEquivalentDose value in milliroentgens_equivalent_man.
        :type milliroentgens_equivalent_man: float
        :return: A new instance of RadiationEquivalentDose.
        :rtype: RadiationEquivalentDose
        """
        return RadiationEquivalentDose(milliroentgens_equivalent_man, RadiationEquivalentDoseUnits.MilliroentgenEquivalentMan)

    
    @property
    def sieverts(self) -> float:
        """
        The sievert is a unit in the International System of Units (SI) intended to represent the stochastic health risk of ionizing radiation, which is defined as the probability of causing radiation-induced cancer and genetic damage.
        """
        if self.__sieverts != None:
            return self.__sieverts
        self.__sieverts = self.__convert_from_base(RadiationEquivalentDoseUnits.Sievert)
        return self.__sieverts

    
    @property
    def roentgens_equivalent_man(self) -> float:
        """
        
        """
        if self.__roentgens_equivalent_man != None:
            return self.__roentgens_equivalent_man
        self.__roentgens_equivalent_man = self.__convert_from_base(RadiationEquivalentDoseUnits.RoentgenEquivalentMan)
        return self.__roentgens_equivalent_man

    
    @property
    def nanosieverts(self) -> float:
        """
        
        """
        if self.__nanosieverts != None:
            return self.__nanosieverts
        self.__nanosieverts = self.__convert_from_base(RadiationEquivalentDoseUnits.Nanosievert)
        return self.__nanosieverts

    
    @property
    def microsieverts(self) -> float:
        """
        
        """
        if self.__microsieverts != None:
            return self.__microsieverts
        self.__microsieverts = self.__convert_from_base(RadiationEquivalentDoseUnits.Microsievert)
        return self.__microsieverts

    
    @property
    def millisieverts(self) -> float:
        """
        
        """
        if self.__millisieverts != None:
            return self.__millisieverts
        self.__millisieverts = self.__convert_from_base(RadiationEquivalentDoseUnits.Millisievert)
        return self.__millisieverts

    
    @property
    def milliroentgens_equivalent_man(self) -> float:
        """
        
        """
        if self.__milliroentgens_equivalent_man != None:
            return self.__milliroentgens_equivalent_man
        self.__milliroentgens_equivalent_man = self.__convert_from_base(RadiationEquivalentDoseUnits.MilliroentgenEquivalentMan)
        return self.__milliroentgens_equivalent_man

    
    def to_string(self, unit: RadiationEquivalentDoseUnits = RadiationEquivalentDoseUnits.Sievert) -> str:
        """
        Format the RadiationEquivalentDose to string.
        Note! the default format for RadiationEquivalentDose is Sievert.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == RadiationEquivalentDoseUnits.Sievert:
            return f"""{self.sieverts} Sv"""
        
        if unit == RadiationEquivalentDoseUnits.RoentgenEquivalentMan:
            return f"""{self.roentgens_equivalent_man} rem"""
        
        if unit == RadiationEquivalentDoseUnits.Nanosievert:
            return f"""{self.nanosieverts} nSv"""
        
        if unit == RadiationEquivalentDoseUnits.Microsievert:
            return f"""{self.microsieverts} μSv"""
        
        if unit == RadiationEquivalentDoseUnits.Millisievert:
            return f"""{self.millisieverts} mSv"""
        
        if unit == RadiationEquivalentDoseUnits.MilliroentgenEquivalentMan:
            return f"""{self.milliroentgens_equivalent_man} mrem"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: RadiationEquivalentDoseUnits = RadiationEquivalentDoseUnits.Sievert) -> str:
        """
        Get RadiationEquivalentDose unit abbreviation.
        Note! the default abbreviation for RadiationEquivalentDose is Sievert.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == RadiationEquivalentDoseUnits.Sievert:
            return """Sv"""
        
        if unit_abbreviation == RadiationEquivalentDoseUnits.RoentgenEquivalentMan:
            return """rem"""
        
        if unit_abbreviation == RadiationEquivalentDoseUnits.Nanosievert:
            return """nSv"""
        
        if unit_abbreviation == RadiationEquivalentDoseUnits.Microsievert:
            return """μSv"""
        
        if unit_abbreviation == RadiationEquivalentDoseUnits.Millisievert:
            return """mSv"""
        
        if unit_abbreviation == RadiationEquivalentDoseUnits.MilliroentgenEquivalentMan:
            return """mrem"""
        
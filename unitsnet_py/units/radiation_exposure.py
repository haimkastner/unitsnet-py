from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class RadiationExposureUnits(Enum):
        """
            RadiationExposureUnits enumeration
        """
        
        CoulombPerKilogram = 'coulomb_per_kilogram'
        """
            
        """
        
        Roentgen = 'roentgen'
        """
            
        """
        
        PicocoulombPerKilogram = 'picocoulomb_per_kilogram'
        """
            
        """
        
        NanocoulombPerKilogram = 'nanocoulomb_per_kilogram'
        """
            
        """
        
        MicrocoulombPerKilogram = 'microcoulomb_per_kilogram'
        """
            
        """
        
        MillicoulombPerKilogram = 'millicoulomb_per_kilogram'
        """
            
        """
        
        Microroentgen = 'microroentgen'
        """
            
        """
        
        Milliroentgen = 'milliroentgen'
        """
            
        """
        

class RadiationExposure(AbstractMeasure):
    """
    Radiation exposure is a measure of the ionization of air due to ionizing radiation from photons.

    Args:
        value (float): The value.
        from_unit (RadiationExposureUnits): The RadiationExposure unit to create from, The default unit is CoulombPerKilogram
    """
    def __init__(self, value: float, from_unit: RadiationExposureUnits = RadiationExposureUnits.CoulombPerKilogram):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__coulombs_per_kilogram = None
        
        self.__roentgens = None
        
        self.__picocoulombs_per_kilogram = None
        
        self.__nanocoulombs_per_kilogram = None
        
        self.__microcoulombs_per_kilogram = None
        
        self.__millicoulombs_per_kilogram = None
        
        self.__microroentgens = None
        
        self.__milliroentgens = None
        

    def convert(self, unit: RadiationExposureUnits) -> float:
        return self.__convert_from_base(unit)

    def __convert_from_base(self, from_unit: RadiationExposureUnits) -> float:
        value = self._value
        
        if from_unit == RadiationExposureUnits.CoulombPerKilogram:
            return (value)
        
        if from_unit == RadiationExposureUnits.Roentgen:
            return (value / 2.58e-4)
        
        if from_unit == RadiationExposureUnits.PicocoulombPerKilogram:
            return ((value) / 1e-12)
        
        if from_unit == RadiationExposureUnits.NanocoulombPerKilogram:
            return ((value) / 1e-09)
        
        if from_unit == RadiationExposureUnits.MicrocoulombPerKilogram:
            return ((value) / 1e-06)
        
        if from_unit == RadiationExposureUnits.MillicoulombPerKilogram:
            return ((value) / 0.001)
        
        if from_unit == RadiationExposureUnits.Microroentgen:
            return ((value / 2.58e-4) / 1e-06)
        
        if from_unit == RadiationExposureUnits.Milliroentgen:
            return ((value / 2.58e-4) / 0.001)
        
        return None


    def __convert_to_base(self, value: float, to_unit: RadiationExposureUnits) -> float:
        
        if to_unit == RadiationExposureUnits.CoulombPerKilogram:
            return (value)
        
        if to_unit == RadiationExposureUnits.Roentgen:
            return (value * 2.58e-4)
        
        if to_unit == RadiationExposureUnits.PicocoulombPerKilogram:
            return ((value) * 1e-12)
        
        if to_unit == RadiationExposureUnits.NanocoulombPerKilogram:
            return ((value) * 1e-09)
        
        if to_unit == RadiationExposureUnits.MicrocoulombPerKilogram:
            return ((value) * 1e-06)
        
        if to_unit == RadiationExposureUnits.MillicoulombPerKilogram:
            return ((value) * 0.001)
        
        if to_unit == RadiationExposureUnits.Microroentgen:
            return ((value * 2.58e-4) * 1e-06)
        
        if to_unit == RadiationExposureUnits.Milliroentgen:
            return ((value * 2.58e-4) * 0.001)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_coulombs_per_kilogram(coulombs_per_kilogram: float):
        """
        Create a new instance of RadiationExposure from a value in coulombs_per_kilogram.

        

        :param meters: The RadiationExposure value in coulombs_per_kilogram.
        :type coulombs_per_kilogram: float
        :return: A new instance of RadiationExposure.
        :rtype: RadiationExposure
        """
        return RadiationExposure(coulombs_per_kilogram, RadiationExposureUnits.CoulombPerKilogram)

    
    @staticmethod
    def from_roentgens(roentgens: float):
        """
        Create a new instance of RadiationExposure from a value in roentgens.

        

        :param meters: The RadiationExposure value in roentgens.
        :type roentgens: float
        :return: A new instance of RadiationExposure.
        :rtype: RadiationExposure
        """
        return RadiationExposure(roentgens, RadiationExposureUnits.Roentgen)

    
    @staticmethod
    def from_picocoulombs_per_kilogram(picocoulombs_per_kilogram: float):
        """
        Create a new instance of RadiationExposure from a value in picocoulombs_per_kilogram.

        

        :param meters: The RadiationExposure value in picocoulombs_per_kilogram.
        :type picocoulombs_per_kilogram: float
        :return: A new instance of RadiationExposure.
        :rtype: RadiationExposure
        """
        return RadiationExposure(picocoulombs_per_kilogram, RadiationExposureUnits.PicocoulombPerKilogram)

    
    @staticmethod
    def from_nanocoulombs_per_kilogram(nanocoulombs_per_kilogram: float):
        """
        Create a new instance of RadiationExposure from a value in nanocoulombs_per_kilogram.

        

        :param meters: The RadiationExposure value in nanocoulombs_per_kilogram.
        :type nanocoulombs_per_kilogram: float
        :return: A new instance of RadiationExposure.
        :rtype: RadiationExposure
        """
        return RadiationExposure(nanocoulombs_per_kilogram, RadiationExposureUnits.NanocoulombPerKilogram)

    
    @staticmethod
    def from_microcoulombs_per_kilogram(microcoulombs_per_kilogram: float):
        """
        Create a new instance of RadiationExposure from a value in microcoulombs_per_kilogram.

        

        :param meters: The RadiationExposure value in microcoulombs_per_kilogram.
        :type microcoulombs_per_kilogram: float
        :return: A new instance of RadiationExposure.
        :rtype: RadiationExposure
        """
        return RadiationExposure(microcoulombs_per_kilogram, RadiationExposureUnits.MicrocoulombPerKilogram)

    
    @staticmethod
    def from_millicoulombs_per_kilogram(millicoulombs_per_kilogram: float):
        """
        Create a new instance of RadiationExposure from a value in millicoulombs_per_kilogram.

        

        :param meters: The RadiationExposure value in millicoulombs_per_kilogram.
        :type millicoulombs_per_kilogram: float
        :return: A new instance of RadiationExposure.
        :rtype: RadiationExposure
        """
        return RadiationExposure(millicoulombs_per_kilogram, RadiationExposureUnits.MillicoulombPerKilogram)

    
    @staticmethod
    def from_microroentgens(microroentgens: float):
        """
        Create a new instance of RadiationExposure from a value in microroentgens.

        

        :param meters: The RadiationExposure value in microroentgens.
        :type microroentgens: float
        :return: A new instance of RadiationExposure.
        :rtype: RadiationExposure
        """
        return RadiationExposure(microroentgens, RadiationExposureUnits.Microroentgen)

    
    @staticmethod
    def from_milliroentgens(milliroentgens: float):
        """
        Create a new instance of RadiationExposure from a value in milliroentgens.

        

        :param meters: The RadiationExposure value in milliroentgens.
        :type milliroentgens: float
        :return: A new instance of RadiationExposure.
        :rtype: RadiationExposure
        """
        return RadiationExposure(milliroentgens, RadiationExposureUnits.Milliroentgen)

    
    @property
    def coulombs_per_kilogram(self) -> float:
        """
        
        """
        if self.__coulombs_per_kilogram != None:
            return self.__coulombs_per_kilogram
        self.__coulombs_per_kilogram = self.__convert_from_base(RadiationExposureUnits.CoulombPerKilogram)
        return self.__coulombs_per_kilogram

    
    @property
    def roentgens(self) -> float:
        """
        
        """
        if self.__roentgens != None:
            return self.__roentgens
        self.__roentgens = self.__convert_from_base(RadiationExposureUnits.Roentgen)
        return self.__roentgens

    
    @property
    def picocoulombs_per_kilogram(self) -> float:
        """
        
        """
        if self.__picocoulombs_per_kilogram != None:
            return self.__picocoulombs_per_kilogram
        self.__picocoulombs_per_kilogram = self.__convert_from_base(RadiationExposureUnits.PicocoulombPerKilogram)
        return self.__picocoulombs_per_kilogram

    
    @property
    def nanocoulombs_per_kilogram(self) -> float:
        """
        
        """
        if self.__nanocoulombs_per_kilogram != None:
            return self.__nanocoulombs_per_kilogram
        self.__nanocoulombs_per_kilogram = self.__convert_from_base(RadiationExposureUnits.NanocoulombPerKilogram)
        return self.__nanocoulombs_per_kilogram

    
    @property
    def microcoulombs_per_kilogram(self) -> float:
        """
        
        """
        if self.__microcoulombs_per_kilogram != None:
            return self.__microcoulombs_per_kilogram
        self.__microcoulombs_per_kilogram = self.__convert_from_base(RadiationExposureUnits.MicrocoulombPerKilogram)
        return self.__microcoulombs_per_kilogram

    
    @property
    def millicoulombs_per_kilogram(self) -> float:
        """
        
        """
        if self.__millicoulombs_per_kilogram != None:
            return self.__millicoulombs_per_kilogram
        self.__millicoulombs_per_kilogram = self.__convert_from_base(RadiationExposureUnits.MillicoulombPerKilogram)
        return self.__millicoulombs_per_kilogram

    
    @property
    def microroentgens(self) -> float:
        """
        
        """
        if self.__microroentgens != None:
            return self.__microroentgens
        self.__microroentgens = self.__convert_from_base(RadiationExposureUnits.Microroentgen)
        return self.__microroentgens

    
    @property
    def milliroentgens(self) -> float:
        """
        
        """
        if self.__milliroentgens != None:
            return self.__milliroentgens
        self.__milliroentgens = self.__convert_from_base(RadiationExposureUnits.Milliroentgen)
        return self.__milliroentgens

    
    def to_string(self, unit: RadiationExposureUnits = RadiationExposureUnits.CoulombPerKilogram) -> str:
        """
        Format the RadiationExposure to string.
        Note! the default format for RadiationExposure is CoulombPerKilogram.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == RadiationExposureUnits.CoulombPerKilogram:
            return f"""{self.coulombs_per_kilogram} C/kg"""
        
        if unit == RadiationExposureUnits.Roentgen:
            return f"""{self.roentgens} R"""
        
        if unit == RadiationExposureUnits.PicocoulombPerKilogram:
            return f"""{self.picocoulombs_per_kilogram} pC/kg"""
        
        if unit == RadiationExposureUnits.NanocoulombPerKilogram:
            return f"""{self.nanocoulombs_per_kilogram} nC/kg"""
        
        if unit == RadiationExposureUnits.MicrocoulombPerKilogram:
            return f"""{self.microcoulombs_per_kilogram} μC/kg"""
        
        if unit == RadiationExposureUnits.MillicoulombPerKilogram:
            return f"""{self.millicoulombs_per_kilogram} mC/kg"""
        
        if unit == RadiationExposureUnits.Microroentgen:
            return f"""{self.microroentgens} μR"""
        
        if unit == RadiationExposureUnits.Milliroentgen:
            return f"""{self.milliroentgens} mR"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: RadiationExposureUnits = RadiationExposureUnits.CoulombPerKilogram) -> str:
        """
        Get RadiationExposure unit abbreviation.
        Note! the default abbreviation for RadiationExposure is CoulombPerKilogram.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == RadiationExposureUnits.CoulombPerKilogram:
            return """C/kg"""
        
        if unit_abbreviation == RadiationExposureUnits.Roentgen:
            return """R"""
        
        if unit_abbreviation == RadiationExposureUnits.PicocoulombPerKilogram:
            return """pC/kg"""
        
        if unit_abbreviation == RadiationExposureUnits.NanocoulombPerKilogram:
            return """nC/kg"""
        
        if unit_abbreviation == RadiationExposureUnits.MicrocoulombPerKilogram:
            return """μC/kg"""
        
        if unit_abbreviation == RadiationExposureUnits.MillicoulombPerKilogram:
            return """mC/kg"""
        
        if unit_abbreviation == RadiationExposureUnits.Microroentgen:
            return """μR"""
        
        if unit_abbreviation == RadiationExposureUnits.Milliroentgen:
            return """mR"""
        
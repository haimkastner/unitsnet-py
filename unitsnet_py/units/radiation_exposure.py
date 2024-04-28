from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class RadiationExposureUnits(Enum):
        """
            RadiationExposureUnits enumeration
        """
        
        CoulombPerKilogram = 'CoulombPerKilogram'
        """
            
        """
        
        Roentgen = 'Roentgen'
        """
            
        """
        
        PicocoulombPerKilogram = 'PicocoulombPerKilogram'
        """
            
        """
        
        NanocoulombPerKilogram = 'NanocoulombPerKilogram'
        """
            
        """
        
        MicrocoulombPerKilogram = 'MicrocoulombPerKilogram'
        """
            
        """
        
        MillicoulombPerKilogram = 'MillicoulombPerKilogram'
        """
            
        """
        
        Microroentgen = 'Microroentgen'
        """
            
        """
        
        Milliroentgen = 'Milliroentgen'
        """
            
        """
        

class RadiationExposureDto:
    """
    A DTO representation of a RadiationExposure

    Attributes:
        value (float): The value of the RadiationExposure.
        unit (RadiationExposureUnits): The specific unit that the RadiationExposure value is representing.
    """

    def __init__(self, value: float, unit: RadiationExposureUnits):
        """
        Create a new DTO representation of a RadiationExposure

        Parameters:
            value (float): The value of the RadiationExposure.
            unit (RadiationExposureUnits): The specific unit that the RadiationExposure value is representing.
        """
        self.value: float = value
        """
        The value of the RadiationExposure
        """
        self.unit: RadiationExposureUnits = unit
        """
        The specific unit that the RadiationExposure value is representing
        """

    def to_json(self):
        """
        Get a RadiationExposure DTO JSON object representing the current unit.

        :return: JSON object represents RadiationExposure DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "CoulombPerKilogram"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of RadiationExposure DTO from a json representation.

        :param data: The RadiationExposure DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "CoulombPerKilogram"}
        :return: A new instance of RadiationExposureDto.
        :rtype: RadiationExposureDto
        """
        return RadiationExposureDto(value=data["value"], unit=RadiationExposureUnits(data["unit"]))


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

    def to_dto(self, hold_in_unit: RadiationExposureUnits = RadiationExposureUnits.CoulombPerKilogram) -> RadiationExposureDto:
        """
        Get a new instance of RadiationExposure DTO representing the current unit.

        :param hold_in_unit: The specific RadiationExposure unit to store the RadiationExposure value in the DTO representation.
        :type hold_in_unit: RadiationExposureUnits
        :return: A new instance of RadiationExposureDto.
        :rtype: RadiationExposureDto
        """
        return RadiationExposureDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: RadiationExposureUnits = RadiationExposureUnits.CoulombPerKilogram):
        """
        Get a RadiationExposure DTO JSON object representing the current unit.

        :param hold_in_unit: The specific RadiationExposure unit to store the RadiationExposure value in the DTO representation.
        :type hold_in_unit: RadiationExposureUnits
        :return: JSON object represents RadiationExposure DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "CoulombPerKilogram"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(radiation_exposure_dto: RadiationExposureDto):
        """
        Obtain a new instance of RadiationExposure from a DTO unit object.

        :param radiation_exposure_dto: The RadiationExposure DTO representation.
        :type radiation_exposure_dto: RadiationExposureDto
        :return: A new instance of RadiationExposure.
        :rtype: RadiationExposure
        """
        return RadiationExposure(radiation_exposure_dto.value, radiation_exposure_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of RadiationExposure from a DTO unit json representation.

        :param data: The RadiationExposure DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "CoulombPerKilogram"}
        :return: A new instance of RadiationExposure.
        :rtype: RadiationExposure
        """
        return RadiationExposure.from_dto(RadiationExposureDto.from_json(data))

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

    
    def to_string(self, unit: RadiationExposureUnits = RadiationExposureUnits.CoulombPerKilogram, fractional_digits: int = None) -> str:
        """
        Format the RadiationExposure to a string.
        
        Note: the default format for RadiationExposure is CoulombPerKilogram.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the RadiationExposure. Default is 'CoulombPerKilogram'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == RadiationExposureUnits.CoulombPerKilogram:
            return f"""{super()._truncate_fraction_digits(self.coulombs_per_kilogram, fractional_digits)} C/kg"""
        
        if unit == RadiationExposureUnits.Roentgen:
            return f"""{super()._truncate_fraction_digits(self.roentgens, fractional_digits)} R"""
        
        if unit == RadiationExposureUnits.PicocoulombPerKilogram:
            return f"""{super()._truncate_fraction_digits(self.picocoulombs_per_kilogram, fractional_digits)} pC/kg"""
        
        if unit == RadiationExposureUnits.NanocoulombPerKilogram:
            return f"""{super()._truncate_fraction_digits(self.nanocoulombs_per_kilogram, fractional_digits)} nC/kg"""
        
        if unit == RadiationExposureUnits.MicrocoulombPerKilogram:
            return f"""{super()._truncate_fraction_digits(self.microcoulombs_per_kilogram, fractional_digits)} μC/kg"""
        
        if unit == RadiationExposureUnits.MillicoulombPerKilogram:
            return f"""{super()._truncate_fraction_digits(self.millicoulombs_per_kilogram, fractional_digits)} mC/kg"""
        
        if unit == RadiationExposureUnits.Microroentgen:
            return f"""{super()._truncate_fraction_digits(self.microroentgens, fractional_digits)} μR"""
        
        if unit == RadiationExposureUnits.Milliroentgen:
            return f"""{super()._truncate_fraction_digits(self.milliroentgens, fractional_digits)} mR"""
        
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
        
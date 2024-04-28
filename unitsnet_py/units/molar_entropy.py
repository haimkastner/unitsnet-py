from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class MolarEntropyUnits(Enum):
        """
            MolarEntropyUnits enumeration
        """
        
        JoulePerMoleKelvin = 'JoulePerMoleKelvin'
        """
            
        """
        
        KilojoulePerMoleKelvin = 'KilojoulePerMoleKelvin'
        """
            
        """
        
        MegajoulePerMoleKelvin = 'MegajoulePerMoleKelvin'
        """
            
        """
        

class MolarEntropyDto:
    """
    A DTO representation of a MolarEntropy

    Attributes:
        value (float): The value of the MolarEntropy.
        unit (MolarEntropyUnits): The specific unit that the MolarEntropy value is representing.
    """

    def __init__(self, value: float, unit: MolarEntropyUnits):
        """
        Create a new DTO representation of a MolarEntropy

        Parameters:
            value (float): The value of the MolarEntropy.
            unit (MolarEntropyUnits): The specific unit that the MolarEntropy value is representing.
        """
        self.value: float = value
        """
        The value of the MolarEntropy
        """
        self.unit: MolarEntropyUnits = unit
        """
        The specific unit that the MolarEntropy value is representing
        """

    def to_json(self):
        """
        Get a MolarEntropy DTO JSON object representing the current unit.

        :return: JSON object represents MolarEntropy DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "JoulePerMoleKelvin"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of MolarEntropy DTO from a json representation.

        :param data: The MolarEntropy DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "JoulePerMoleKelvin"}
        :return: A new instance of MolarEntropyDto.
        :rtype: MolarEntropyDto
        """
        return MolarEntropyDto(value=data["value"], unit=MolarEntropyUnits(data["unit"]))


class MolarEntropy(AbstractMeasure):
    """
    Molar entropy is amount of energy required to increase temperature of 1 mole substance by 1 Kelvin.

    Args:
        value (float): The value.
        from_unit (MolarEntropyUnits): The MolarEntropy unit to create from, The default unit is JoulePerMoleKelvin
    """
    def __init__(self, value: float, from_unit: MolarEntropyUnits = MolarEntropyUnits.JoulePerMoleKelvin):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__joules_per_mole_kelvin = None
        
        self.__kilojoules_per_mole_kelvin = None
        
        self.__megajoules_per_mole_kelvin = None
        

    def convert(self, unit: MolarEntropyUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: MolarEntropyUnits = MolarEntropyUnits.JoulePerMoleKelvin) -> MolarEntropyDto:
        """
        Get a new instance of MolarEntropy DTO representing the current unit.

        :param hold_in_unit: The specific MolarEntropy unit to store the MolarEntropy value in the DTO representation.
        :type hold_in_unit: MolarEntropyUnits
        :return: A new instance of MolarEntropyDto.
        :rtype: MolarEntropyDto
        """
        return MolarEntropyDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: MolarEntropyUnits = MolarEntropyUnits.JoulePerMoleKelvin):
        """
        Get a MolarEntropy DTO JSON object representing the current unit.

        :param hold_in_unit: The specific MolarEntropy unit to store the MolarEntropy value in the DTO representation.
        :type hold_in_unit: MolarEntropyUnits
        :return: JSON object represents MolarEntropy DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "JoulePerMoleKelvin"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(molar_entropy_dto: MolarEntropyDto):
        """
        Obtain a new instance of MolarEntropy from a DTO unit object.

        :param molar_entropy_dto: The MolarEntropy DTO representation.
        :type molar_entropy_dto: MolarEntropyDto
        :return: A new instance of MolarEntropy.
        :rtype: MolarEntropy
        """
        return MolarEntropy(molar_entropy_dto.value, molar_entropy_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of MolarEntropy from a DTO unit json representation.

        :param data: The MolarEntropy DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "JoulePerMoleKelvin"}
        :return: A new instance of MolarEntropy.
        :rtype: MolarEntropy
        """
        return MolarEntropy.from_dto(MolarEntropyDto.from_json(data))

    def __convert_from_base(self, from_unit: MolarEntropyUnits) -> float:
        value = self._value
        
        if from_unit == MolarEntropyUnits.JoulePerMoleKelvin:
            return (value)
        
        if from_unit == MolarEntropyUnits.KilojoulePerMoleKelvin:
            return ((value) / 1000.0)
        
        if from_unit == MolarEntropyUnits.MegajoulePerMoleKelvin:
            return ((value) / 1000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: MolarEntropyUnits) -> float:
        
        if to_unit == MolarEntropyUnits.JoulePerMoleKelvin:
            return (value)
        
        if to_unit == MolarEntropyUnits.KilojoulePerMoleKelvin:
            return ((value) * 1000.0)
        
        if to_unit == MolarEntropyUnits.MegajoulePerMoleKelvin:
            return ((value) * 1000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_joules_per_mole_kelvin(joules_per_mole_kelvin: float):
        """
        Create a new instance of MolarEntropy from a value in joules_per_mole_kelvin.

        

        :param meters: The MolarEntropy value in joules_per_mole_kelvin.
        :type joules_per_mole_kelvin: float
        :return: A new instance of MolarEntropy.
        :rtype: MolarEntropy
        """
        return MolarEntropy(joules_per_mole_kelvin, MolarEntropyUnits.JoulePerMoleKelvin)

    
    @staticmethod
    def from_kilojoules_per_mole_kelvin(kilojoules_per_mole_kelvin: float):
        """
        Create a new instance of MolarEntropy from a value in kilojoules_per_mole_kelvin.

        

        :param meters: The MolarEntropy value in kilojoules_per_mole_kelvin.
        :type kilojoules_per_mole_kelvin: float
        :return: A new instance of MolarEntropy.
        :rtype: MolarEntropy
        """
        return MolarEntropy(kilojoules_per_mole_kelvin, MolarEntropyUnits.KilojoulePerMoleKelvin)

    
    @staticmethod
    def from_megajoules_per_mole_kelvin(megajoules_per_mole_kelvin: float):
        """
        Create a new instance of MolarEntropy from a value in megajoules_per_mole_kelvin.

        

        :param meters: The MolarEntropy value in megajoules_per_mole_kelvin.
        :type megajoules_per_mole_kelvin: float
        :return: A new instance of MolarEntropy.
        :rtype: MolarEntropy
        """
        return MolarEntropy(megajoules_per_mole_kelvin, MolarEntropyUnits.MegajoulePerMoleKelvin)

    
    @property
    def joules_per_mole_kelvin(self) -> float:
        """
        
        """
        if self.__joules_per_mole_kelvin != None:
            return self.__joules_per_mole_kelvin
        self.__joules_per_mole_kelvin = self.__convert_from_base(MolarEntropyUnits.JoulePerMoleKelvin)
        return self.__joules_per_mole_kelvin

    
    @property
    def kilojoules_per_mole_kelvin(self) -> float:
        """
        
        """
        if self.__kilojoules_per_mole_kelvin != None:
            return self.__kilojoules_per_mole_kelvin
        self.__kilojoules_per_mole_kelvin = self.__convert_from_base(MolarEntropyUnits.KilojoulePerMoleKelvin)
        return self.__kilojoules_per_mole_kelvin

    
    @property
    def megajoules_per_mole_kelvin(self) -> float:
        """
        
        """
        if self.__megajoules_per_mole_kelvin != None:
            return self.__megajoules_per_mole_kelvin
        self.__megajoules_per_mole_kelvin = self.__convert_from_base(MolarEntropyUnits.MegajoulePerMoleKelvin)
        return self.__megajoules_per_mole_kelvin

    
    def to_string(self, unit: MolarEntropyUnits = MolarEntropyUnits.JoulePerMoleKelvin, fractional_digits: int = None) -> str:
        """
        Format the MolarEntropy to a string.
        
        Note: the default format for MolarEntropy is JoulePerMoleKelvin.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the MolarEntropy. Default is 'JoulePerMoleKelvin'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == MolarEntropyUnits.JoulePerMoleKelvin:
            return f"""{super()._truncate_fraction_digits(self.joules_per_mole_kelvin, fractional_digits)} J/(mol*K)"""
        
        if unit == MolarEntropyUnits.KilojoulePerMoleKelvin:
            return f"""{super()._truncate_fraction_digits(self.kilojoules_per_mole_kelvin, fractional_digits)} kJ/(mol*K)"""
        
        if unit == MolarEntropyUnits.MegajoulePerMoleKelvin:
            return f"""{super()._truncate_fraction_digits(self.megajoules_per_mole_kelvin, fractional_digits)} MJ/(mol*K)"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: MolarEntropyUnits = MolarEntropyUnits.JoulePerMoleKelvin) -> str:
        """
        Get MolarEntropy unit abbreviation.
        Note! the default abbreviation for MolarEntropy is JoulePerMoleKelvin.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == MolarEntropyUnits.JoulePerMoleKelvin:
            return """J/(mol*K)"""
        
        if unit_abbreviation == MolarEntropyUnits.KilojoulePerMoleKelvin:
            return """kJ/(mol*K)"""
        
        if unit_abbreviation == MolarEntropyUnits.MegajoulePerMoleKelvin:
            return """MJ/(mol*K)"""
        
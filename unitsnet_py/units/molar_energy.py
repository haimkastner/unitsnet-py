from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class MolarEnergyUnits(Enum):
        """
            MolarEnergyUnits enumeration
        """
        
        JoulePerMole = 'JoulePerMole'
        """
            
        """
        
        KilojoulePerMole = 'KilojoulePerMole'
        """
            
        """
        
        MegajoulePerMole = 'MegajoulePerMole'
        """
            
        """
        

class MolarEnergyDto:
    """
    A DTO representation of a MolarEnergy

    Attributes:
        value (float): The value of the MolarEnergy.
        unit (MolarEnergyUnits): The specific unit that the MolarEnergy value is representing.
    """

    def __init__(self, value: float, unit: MolarEnergyUnits):
        """
        Create a new DTO representation of a MolarEnergy

        Parameters:
            value (float): The value of the MolarEnergy.
            unit (MolarEnergyUnits): The specific unit that the MolarEnergy value is representing.
        """
        self.value: float = value
        """
        The value of the MolarEnergy
        """
        self.unit: MolarEnergyUnits = unit
        """
        The specific unit that the MolarEnergy value is representing
        """

    def to_json(self):
        """
        Get a MolarEnergy DTO JSON object representing the current unit.

        :return: JSON object represents MolarEnergy DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "JoulePerMole"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of MolarEnergy DTO from a json representation.

        :param data: The MolarEnergy DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "JoulePerMole"}
        :return: A new instance of MolarEnergyDto.
        :rtype: MolarEnergyDto
        """
        return MolarEnergyDto(value=data["value"], unit=MolarEnergyUnits(data["unit"]))


class MolarEnergy(AbstractMeasure):
    """
    Molar energy is the amount of energy stored in 1 mole of a substance.

    Args:
        value (float): The value.
        from_unit (MolarEnergyUnits): The MolarEnergy unit to create from, The default unit is JoulePerMole
    """
    def __init__(self, value: float, from_unit: MolarEnergyUnits = MolarEnergyUnits.JoulePerMole):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__joules_per_mole = None
        
        self.__kilojoules_per_mole = None
        
        self.__megajoules_per_mole = None
        

    def convert(self, unit: MolarEnergyUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: MolarEnergyUnits = MolarEnergyUnits.JoulePerMole) -> MolarEnergyDto:
        """
        Get a new instance of MolarEnergy DTO representing the current unit.

        :param hold_in_unit: The specific MolarEnergy unit to store the MolarEnergy value in the DTO representation.
        :type hold_in_unit: MolarEnergyUnits
        :return: A new instance of MolarEnergyDto.
        :rtype: MolarEnergyDto
        """
        return MolarEnergyDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: MolarEnergyUnits = MolarEnergyUnits.JoulePerMole):
        """
        Get a MolarEnergy DTO JSON object representing the current unit.

        :param hold_in_unit: The specific MolarEnergy unit to store the MolarEnergy value in the DTO representation.
        :type hold_in_unit: MolarEnergyUnits
        :return: JSON object represents MolarEnergy DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "JoulePerMole"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(molar_energy_dto: MolarEnergyDto):
        """
        Obtain a new instance of MolarEnergy from a DTO unit object.

        :param molar_energy_dto: The MolarEnergy DTO representation.
        :type molar_energy_dto: MolarEnergyDto
        :return: A new instance of MolarEnergy.
        :rtype: MolarEnergy
        """
        return MolarEnergy(molar_energy_dto.value, molar_energy_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of MolarEnergy from a DTO unit json representation.

        :param data: The MolarEnergy DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "JoulePerMole"}
        :return: A new instance of MolarEnergy.
        :rtype: MolarEnergy
        """
        return MolarEnergy.from_dto(MolarEnergyDto.from_json(data))

    def __convert_from_base(self, from_unit: MolarEnergyUnits) -> float:
        value = self._value
        
        if from_unit == MolarEnergyUnits.JoulePerMole:
            return (value)
        
        if from_unit == MolarEnergyUnits.KilojoulePerMole:
            return ((value) / 1000.0)
        
        if from_unit == MolarEnergyUnits.MegajoulePerMole:
            return ((value) / 1000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: MolarEnergyUnits) -> float:
        
        if to_unit == MolarEnergyUnits.JoulePerMole:
            return (value)
        
        if to_unit == MolarEnergyUnits.KilojoulePerMole:
            return ((value) * 1000.0)
        
        if to_unit == MolarEnergyUnits.MegajoulePerMole:
            return ((value) * 1000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_joules_per_mole(joules_per_mole: float):
        """
        Create a new instance of MolarEnergy from a value in joules_per_mole.

        

        :param meters: The MolarEnergy value in joules_per_mole.
        :type joules_per_mole: float
        :return: A new instance of MolarEnergy.
        :rtype: MolarEnergy
        """
        return MolarEnergy(joules_per_mole, MolarEnergyUnits.JoulePerMole)

    
    @staticmethod
    def from_kilojoules_per_mole(kilojoules_per_mole: float):
        """
        Create a new instance of MolarEnergy from a value in kilojoules_per_mole.

        

        :param meters: The MolarEnergy value in kilojoules_per_mole.
        :type kilojoules_per_mole: float
        :return: A new instance of MolarEnergy.
        :rtype: MolarEnergy
        """
        return MolarEnergy(kilojoules_per_mole, MolarEnergyUnits.KilojoulePerMole)

    
    @staticmethod
    def from_megajoules_per_mole(megajoules_per_mole: float):
        """
        Create a new instance of MolarEnergy from a value in megajoules_per_mole.

        

        :param meters: The MolarEnergy value in megajoules_per_mole.
        :type megajoules_per_mole: float
        :return: A new instance of MolarEnergy.
        :rtype: MolarEnergy
        """
        return MolarEnergy(megajoules_per_mole, MolarEnergyUnits.MegajoulePerMole)

    
    @property
    def joules_per_mole(self) -> float:
        """
        
        """
        if self.__joules_per_mole != None:
            return self.__joules_per_mole
        self.__joules_per_mole = self.__convert_from_base(MolarEnergyUnits.JoulePerMole)
        return self.__joules_per_mole

    
    @property
    def kilojoules_per_mole(self) -> float:
        """
        
        """
        if self.__kilojoules_per_mole != None:
            return self.__kilojoules_per_mole
        self.__kilojoules_per_mole = self.__convert_from_base(MolarEnergyUnits.KilojoulePerMole)
        return self.__kilojoules_per_mole

    
    @property
    def megajoules_per_mole(self) -> float:
        """
        
        """
        if self.__megajoules_per_mole != None:
            return self.__megajoules_per_mole
        self.__megajoules_per_mole = self.__convert_from_base(MolarEnergyUnits.MegajoulePerMole)
        return self.__megajoules_per_mole

    
    def to_string(self, unit: MolarEnergyUnits = MolarEnergyUnits.JoulePerMole, fractional_digits: int = None) -> str:
        """
        Format the MolarEnergy to a string.
        
        Note: the default format for MolarEnergy is JoulePerMole.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the MolarEnergy. Default is 'JoulePerMole'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == MolarEnergyUnits.JoulePerMole:
            return f"""{super()._truncate_fraction_digits(self.joules_per_mole, fractional_digits)} J/mol"""
        
        if unit == MolarEnergyUnits.KilojoulePerMole:
            return f"""{super()._truncate_fraction_digits(self.kilojoules_per_mole, fractional_digits)} kJ/mol"""
        
        if unit == MolarEnergyUnits.MegajoulePerMole:
            return f"""{super()._truncate_fraction_digits(self.megajoules_per_mole, fractional_digits)} MJ/mol"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: MolarEnergyUnits = MolarEnergyUnits.JoulePerMole) -> str:
        """
        Get MolarEnergy unit abbreviation.
        Note! the default abbreviation for MolarEnergy is JoulePerMole.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == MolarEnergyUnits.JoulePerMole:
            return """J/mol"""
        
        if unit_abbreviation == MolarEnergyUnits.KilojoulePerMole:
            return """kJ/mol"""
        
        if unit_abbreviation == MolarEnergyUnits.MegajoulePerMole:
            return """MJ/mol"""
        
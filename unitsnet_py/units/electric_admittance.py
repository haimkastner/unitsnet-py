from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class ElectricAdmittanceUnits(Enum):
        """
            ElectricAdmittanceUnits enumeration
        """
        
        Siemens = 'Siemens'
        """
            
        """
        
        Nanosiemens = 'Nanosiemens'
        """
            
        """
        
        Microsiemens = 'Microsiemens'
        """
            
        """
        
        Millisiemens = 'Millisiemens'
        """
            
        """
        

class ElectricAdmittanceDto:
    """
    A DTO representation of a ElectricAdmittance

    Attributes:
        value (float): The value of the ElectricAdmittance.
        unit (ElectricAdmittanceUnits): The specific unit that the ElectricAdmittance value is representing.
    """

    def __init__(self, value: float, unit: ElectricAdmittanceUnits):
        """
        Create a new DTO representation of a ElectricAdmittance

        Parameters:
            value (float): The value of the ElectricAdmittance.
            unit (ElectricAdmittanceUnits): The specific unit that the ElectricAdmittance value is representing.
        """
        self.value: float = value
        """
        The value of the ElectricAdmittance
        """
        self.unit: ElectricAdmittanceUnits = unit
        """
        The specific unit that the ElectricAdmittance value is representing
        """

    def to_json(self):
        """
        Get a ElectricAdmittance DTO JSON object representing the current unit.

        :return: JSON object represents ElectricAdmittance DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "Siemens"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of ElectricAdmittance DTO from a json representation.

        :param data: The ElectricAdmittance DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "Siemens"}
        :return: A new instance of ElectricAdmittanceDto.
        :rtype: ElectricAdmittanceDto
        """
        return ElectricAdmittanceDto(value=data["value"], unit=ElectricAdmittanceUnits(data["unit"]))


class ElectricAdmittance(AbstractMeasure):
    """
    Electric admittance is a measure of how easily a circuit or device will allow a current to flow. It is defined as the inverse of impedance. The SI unit of admittance is the siemens (symbol S).

    Args:
        value (float): The value.
        from_unit (ElectricAdmittanceUnits): The ElectricAdmittance unit to create from, The default unit is Siemens
    """
    def __init__(self, value: float, from_unit: ElectricAdmittanceUnits = ElectricAdmittanceUnits.Siemens):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__siemens = None
        
        self.__nanosiemens = None
        
        self.__microsiemens = None
        
        self.__millisiemens = None
        

    def convert(self, unit: ElectricAdmittanceUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: ElectricAdmittanceUnits = ElectricAdmittanceUnits.Siemens) -> ElectricAdmittanceDto:
        """
        Get a new instance of ElectricAdmittance DTO representing the current unit.

        :param hold_in_unit: The specific ElectricAdmittance unit to store the ElectricAdmittance value in the DTO representation.
        :type hold_in_unit: ElectricAdmittanceUnits
        :return: A new instance of ElectricAdmittanceDto.
        :rtype: ElectricAdmittanceDto
        """
        return ElectricAdmittanceDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: ElectricAdmittanceUnits = ElectricAdmittanceUnits.Siemens):
        """
        Get a ElectricAdmittance DTO JSON object representing the current unit.

        :param hold_in_unit: The specific ElectricAdmittance unit to store the ElectricAdmittance value in the DTO representation.
        :type hold_in_unit: ElectricAdmittanceUnits
        :return: JSON object represents ElectricAdmittance DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "Siemens"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(electric_admittance_dto: ElectricAdmittanceDto):
        """
        Obtain a new instance of ElectricAdmittance from a DTO unit object.

        :param electric_admittance_dto: The ElectricAdmittance DTO representation.
        :type electric_admittance_dto: ElectricAdmittanceDto
        :return: A new instance of ElectricAdmittance.
        :rtype: ElectricAdmittance
        """
        return ElectricAdmittance(electric_admittance_dto.value, electric_admittance_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of ElectricAdmittance from a DTO unit json representation.

        :param data: The ElectricAdmittance DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "Siemens"}
        :return: A new instance of ElectricAdmittance.
        :rtype: ElectricAdmittance
        """
        return ElectricAdmittance.from_dto(ElectricAdmittanceDto.from_json(data))

    def __convert_from_base(self, from_unit: ElectricAdmittanceUnits) -> float:
        value = self._value
        
        if from_unit == ElectricAdmittanceUnits.Siemens:
            return (value)
        
        if from_unit == ElectricAdmittanceUnits.Nanosiemens:
            return ((value) / 1e-09)
        
        if from_unit == ElectricAdmittanceUnits.Microsiemens:
            return ((value) / 1e-06)
        
        if from_unit == ElectricAdmittanceUnits.Millisiemens:
            return ((value) / 0.001)
        
        return None


    def __convert_to_base(self, value: float, to_unit: ElectricAdmittanceUnits) -> float:
        
        if to_unit == ElectricAdmittanceUnits.Siemens:
            return (value)
        
        if to_unit == ElectricAdmittanceUnits.Nanosiemens:
            return ((value) * 1e-09)
        
        if to_unit == ElectricAdmittanceUnits.Microsiemens:
            return ((value) * 1e-06)
        
        if to_unit == ElectricAdmittanceUnits.Millisiemens:
            return ((value) * 0.001)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_siemens(siemens: float):
        """
        Create a new instance of ElectricAdmittance from a value in siemens.

        

        :param meters: The ElectricAdmittance value in siemens.
        :type siemens: float
        :return: A new instance of ElectricAdmittance.
        :rtype: ElectricAdmittance
        """
        return ElectricAdmittance(siemens, ElectricAdmittanceUnits.Siemens)

    
    @staticmethod
    def from_nanosiemens(nanosiemens: float):
        """
        Create a new instance of ElectricAdmittance from a value in nanosiemens.

        

        :param meters: The ElectricAdmittance value in nanosiemens.
        :type nanosiemens: float
        :return: A new instance of ElectricAdmittance.
        :rtype: ElectricAdmittance
        """
        return ElectricAdmittance(nanosiemens, ElectricAdmittanceUnits.Nanosiemens)

    
    @staticmethod
    def from_microsiemens(microsiemens: float):
        """
        Create a new instance of ElectricAdmittance from a value in microsiemens.

        

        :param meters: The ElectricAdmittance value in microsiemens.
        :type microsiemens: float
        :return: A new instance of ElectricAdmittance.
        :rtype: ElectricAdmittance
        """
        return ElectricAdmittance(microsiemens, ElectricAdmittanceUnits.Microsiemens)

    
    @staticmethod
    def from_millisiemens(millisiemens: float):
        """
        Create a new instance of ElectricAdmittance from a value in millisiemens.

        

        :param meters: The ElectricAdmittance value in millisiemens.
        :type millisiemens: float
        :return: A new instance of ElectricAdmittance.
        :rtype: ElectricAdmittance
        """
        return ElectricAdmittance(millisiemens, ElectricAdmittanceUnits.Millisiemens)

    
    @property
    def siemens(self) -> float:
        """
        
        """
        if self.__siemens != None:
            return self.__siemens
        self.__siemens = self.__convert_from_base(ElectricAdmittanceUnits.Siemens)
        return self.__siemens

    
    @property
    def nanosiemens(self) -> float:
        """
        
        """
        if self.__nanosiemens != None:
            return self.__nanosiemens
        self.__nanosiemens = self.__convert_from_base(ElectricAdmittanceUnits.Nanosiemens)
        return self.__nanosiemens

    
    @property
    def microsiemens(self) -> float:
        """
        
        """
        if self.__microsiemens != None:
            return self.__microsiemens
        self.__microsiemens = self.__convert_from_base(ElectricAdmittanceUnits.Microsiemens)
        return self.__microsiemens

    
    @property
    def millisiemens(self) -> float:
        """
        
        """
        if self.__millisiemens != None:
            return self.__millisiemens
        self.__millisiemens = self.__convert_from_base(ElectricAdmittanceUnits.Millisiemens)
        return self.__millisiemens

    
    def to_string(self, unit: ElectricAdmittanceUnits = ElectricAdmittanceUnits.Siemens, fractional_digits: int = None) -> str:
        """
        Format the ElectricAdmittance to a string.
        
        Note: the default format for ElectricAdmittance is Siemens.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the ElectricAdmittance. Default is 'Siemens'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == ElectricAdmittanceUnits.Siemens:
            return f"""{super()._truncate_fraction_digits(self.siemens, fractional_digits)} S"""
        
        if unit == ElectricAdmittanceUnits.Nanosiemens:
            return f"""{super()._truncate_fraction_digits(self.nanosiemens, fractional_digits)} nS"""
        
        if unit == ElectricAdmittanceUnits.Microsiemens:
            return f"""{super()._truncate_fraction_digits(self.microsiemens, fractional_digits)} μS"""
        
        if unit == ElectricAdmittanceUnits.Millisiemens:
            return f"""{super()._truncate_fraction_digits(self.millisiemens, fractional_digits)} mS"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: ElectricAdmittanceUnits = ElectricAdmittanceUnits.Siemens) -> str:
        """
        Get ElectricAdmittance unit abbreviation.
        Note! the default abbreviation for ElectricAdmittance is Siemens.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == ElectricAdmittanceUnits.Siemens:
            return """S"""
        
        if unit_abbreviation == ElectricAdmittanceUnits.Nanosiemens:
            return """nS"""
        
        if unit_abbreviation == ElectricAdmittanceUnits.Microsiemens:
            return """μS"""
        
        if unit_abbreviation == ElectricAdmittanceUnits.Millisiemens:
            return """mS"""
        
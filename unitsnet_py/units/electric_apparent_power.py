from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class ElectricApparentPowerUnits(Enum):
        """
            ElectricApparentPowerUnits enumeration
        """
        
        Voltampere = 'Voltampere'
        """
            
        """
        
        Microvoltampere = 'Microvoltampere'
        """
            
        """
        
        Millivoltampere = 'Millivoltampere'
        """
            
        """
        
        Kilovoltampere = 'Kilovoltampere'
        """
            
        """
        
        Megavoltampere = 'Megavoltampere'
        """
            
        """
        
        Gigavoltampere = 'Gigavoltampere'
        """
            
        """
        

class ElectricApparentPowerDto:
    """
    A DTO representation of a ElectricApparentPower

    Attributes:
        value (float): The value of the ElectricApparentPower.
        unit (ElectricApparentPowerUnits): The specific unit that the ElectricApparentPower value is representing.
    """

    def __init__(self, value: float, unit: ElectricApparentPowerUnits):
        """
        Create a new DTO representation of a ElectricApparentPower

        Parameters:
            value (float): The value of the ElectricApparentPower.
            unit (ElectricApparentPowerUnits): The specific unit that the ElectricApparentPower value is representing.
        """
        self.value: float = value
        """
        The value of the ElectricApparentPower
        """
        self.unit: ElectricApparentPowerUnits = unit
        """
        The specific unit that the ElectricApparentPower value is representing
        """

    def to_json(self):
        """
        Get a ElectricApparentPower DTO JSON object representing the current unit.

        :return: JSON object represents ElectricApparentPower DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "Voltampere"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of ElectricApparentPower DTO from a json representation.

        :param data: The ElectricApparentPower DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "Voltampere"}
        :return: A new instance of ElectricApparentPowerDto.
        :rtype: ElectricApparentPowerDto
        """
        return ElectricApparentPowerDto(value=data["value"], unit=ElectricApparentPowerUnits(data["unit"]))


class ElectricApparentPower(AbstractMeasure):
    """
    Power engineers measure apparent power as the magnitude of the vector sum of active and reactive power. It is the product of the root mean square voltage (in volts) and the root mean square current (in amperes).

    Args:
        value (float): The value.
        from_unit (ElectricApparentPowerUnits): The ElectricApparentPower unit to create from, The default unit is Voltampere
    """
    def __init__(self, value: float, from_unit: ElectricApparentPowerUnits = ElectricApparentPowerUnits.Voltampere):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__voltamperes = None
        
        self.__microvoltamperes = None
        
        self.__millivoltamperes = None
        
        self.__kilovoltamperes = None
        
        self.__megavoltamperes = None
        
        self.__gigavoltamperes = None
        

    def convert(self, unit: ElectricApparentPowerUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: ElectricApparentPowerUnits = ElectricApparentPowerUnits.Voltampere) -> ElectricApparentPowerDto:
        """
        Get a new instance of ElectricApparentPower DTO representing the current unit.

        :param hold_in_unit: The specific ElectricApparentPower unit to store the ElectricApparentPower value in the DTO representation.
        :type hold_in_unit: ElectricApparentPowerUnits
        :return: A new instance of ElectricApparentPowerDto.
        :rtype: ElectricApparentPowerDto
        """
        return ElectricApparentPowerDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: ElectricApparentPowerUnits = ElectricApparentPowerUnits.Voltampere):
        """
        Get a ElectricApparentPower DTO JSON object representing the current unit.

        :param hold_in_unit: The specific ElectricApparentPower unit to store the ElectricApparentPower value in the DTO representation.
        :type hold_in_unit: ElectricApparentPowerUnits
        :return: JSON object represents ElectricApparentPower DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "Voltampere"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(electric_apparent_power_dto: ElectricApparentPowerDto):
        """
        Obtain a new instance of ElectricApparentPower from a DTO unit object.

        :param electric_apparent_power_dto: The ElectricApparentPower DTO representation.
        :type electric_apparent_power_dto: ElectricApparentPowerDto
        :return: A new instance of ElectricApparentPower.
        :rtype: ElectricApparentPower
        """
        return ElectricApparentPower(electric_apparent_power_dto.value, electric_apparent_power_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of ElectricApparentPower from a DTO unit json representation.

        :param data: The ElectricApparentPower DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "Voltampere"}
        :return: A new instance of ElectricApparentPower.
        :rtype: ElectricApparentPower
        """
        return ElectricApparentPower.from_dto(ElectricApparentPowerDto.from_json(data))

    def __convert_from_base(self, from_unit: ElectricApparentPowerUnits) -> float:
        value = self._value
        
        if from_unit == ElectricApparentPowerUnits.Voltampere:
            return (value)
        
        if from_unit == ElectricApparentPowerUnits.Microvoltampere:
            return ((value) / 1e-06)
        
        if from_unit == ElectricApparentPowerUnits.Millivoltampere:
            return ((value) / 0.001)
        
        if from_unit == ElectricApparentPowerUnits.Kilovoltampere:
            return ((value) / 1000.0)
        
        if from_unit == ElectricApparentPowerUnits.Megavoltampere:
            return ((value) / 1000000.0)
        
        if from_unit == ElectricApparentPowerUnits.Gigavoltampere:
            return ((value) / 1000000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: ElectricApparentPowerUnits) -> float:
        
        if to_unit == ElectricApparentPowerUnits.Voltampere:
            return (value)
        
        if to_unit == ElectricApparentPowerUnits.Microvoltampere:
            return ((value) * 1e-06)
        
        if to_unit == ElectricApparentPowerUnits.Millivoltampere:
            return ((value) * 0.001)
        
        if to_unit == ElectricApparentPowerUnits.Kilovoltampere:
            return ((value) * 1000.0)
        
        if to_unit == ElectricApparentPowerUnits.Megavoltampere:
            return ((value) * 1000000.0)
        
        if to_unit == ElectricApparentPowerUnits.Gigavoltampere:
            return ((value) * 1000000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_voltamperes(voltamperes: float):
        """
        Create a new instance of ElectricApparentPower from a value in voltamperes.

        

        :param meters: The ElectricApparentPower value in voltamperes.
        :type voltamperes: float
        :return: A new instance of ElectricApparentPower.
        :rtype: ElectricApparentPower
        """
        return ElectricApparentPower(voltamperes, ElectricApparentPowerUnits.Voltampere)

    
    @staticmethod
    def from_microvoltamperes(microvoltamperes: float):
        """
        Create a new instance of ElectricApparentPower from a value in microvoltamperes.

        

        :param meters: The ElectricApparentPower value in microvoltamperes.
        :type microvoltamperes: float
        :return: A new instance of ElectricApparentPower.
        :rtype: ElectricApparentPower
        """
        return ElectricApparentPower(microvoltamperes, ElectricApparentPowerUnits.Microvoltampere)

    
    @staticmethod
    def from_millivoltamperes(millivoltamperes: float):
        """
        Create a new instance of ElectricApparentPower from a value in millivoltamperes.

        

        :param meters: The ElectricApparentPower value in millivoltamperes.
        :type millivoltamperes: float
        :return: A new instance of ElectricApparentPower.
        :rtype: ElectricApparentPower
        """
        return ElectricApparentPower(millivoltamperes, ElectricApparentPowerUnits.Millivoltampere)

    
    @staticmethod
    def from_kilovoltamperes(kilovoltamperes: float):
        """
        Create a new instance of ElectricApparentPower from a value in kilovoltamperes.

        

        :param meters: The ElectricApparentPower value in kilovoltamperes.
        :type kilovoltamperes: float
        :return: A new instance of ElectricApparentPower.
        :rtype: ElectricApparentPower
        """
        return ElectricApparentPower(kilovoltamperes, ElectricApparentPowerUnits.Kilovoltampere)

    
    @staticmethod
    def from_megavoltamperes(megavoltamperes: float):
        """
        Create a new instance of ElectricApparentPower from a value in megavoltamperes.

        

        :param meters: The ElectricApparentPower value in megavoltamperes.
        :type megavoltamperes: float
        :return: A new instance of ElectricApparentPower.
        :rtype: ElectricApparentPower
        """
        return ElectricApparentPower(megavoltamperes, ElectricApparentPowerUnits.Megavoltampere)

    
    @staticmethod
    def from_gigavoltamperes(gigavoltamperes: float):
        """
        Create a new instance of ElectricApparentPower from a value in gigavoltamperes.

        

        :param meters: The ElectricApparentPower value in gigavoltamperes.
        :type gigavoltamperes: float
        :return: A new instance of ElectricApparentPower.
        :rtype: ElectricApparentPower
        """
        return ElectricApparentPower(gigavoltamperes, ElectricApparentPowerUnits.Gigavoltampere)

    
    @property
    def voltamperes(self) -> float:
        """
        
        """
        if self.__voltamperes != None:
            return self.__voltamperes
        self.__voltamperes = self.__convert_from_base(ElectricApparentPowerUnits.Voltampere)
        return self.__voltamperes

    
    @property
    def microvoltamperes(self) -> float:
        """
        
        """
        if self.__microvoltamperes != None:
            return self.__microvoltamperes
        self.__microvoltamperes = self.__convert_from_base(ElectricApparentPowerUnits.Microvoltampere)
        return self.__microvoltamperes

    
    @property
    def millivoltamperes(self) -> float:
        """
        
        """
        if self.__millivoltamperes != None:
            return self.__millivoltamperes
        self.__millivoltamperes = self.__convert_from_base(ElectricApparentPowerUnits.Millivoltampere)
        return self.__millivoltamperes

    
    @property
    def kilovoltamperes(self) -> float:
        """
        
        """
        if self.__kilovoltamperes != None:
            return self.__kilovoltamperes
        self.__kilovoltamperes = self.__convert_from_base(ElectricApparentPowerUnits.Kilovoltampere)
        return self.__kilovoltamperes

    
    @property
    def megavoltamperes(self) -> float:
        """
        
        """
        if self.__megavoltamperes != None:
            return self.__megavoltamperes
        self.__megavoltamperes = self.__convert_from_base(ElectricApparentPowerUnits.Megavoltampere)
        return self.__megavoltamperes

    
    @property
    def gigavoltamperes(self) -> float:
        """
        
        """
        if self.__gigavoltamperes != None:
            return self.__gigavoltamperes
        self.__gigavoltamperes = self.__convert_from_base(ElectricApparentPowerUnits.Gigavoltampere)
        return self.__gigavoltamperes

    
    def to_string(self, unit: ElectricApparentPowerUnits = ElectricApparentPowerUnits.Voltampere, fractional_digits: int = None) -> str:
        """
        Format the ElectricApparentPower to a string.
        
        Note: the default format for ElectricApparentPower is Voltampere.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the ElectricApparentPower. Default is 'Voltampere'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == ElectricApparentPowerUnits.Voltampere:
            return f"""{super()._truncate_fraction_digits(self.voltamperes, fractional_digits)} VA"""
        
        if unit == ElectricApparentPowerUnits.Microvoltampere:
            return f"""{super()._truncate_fraction_digits(self.microvoltamperes, fractional_digits)} μVA"""
        
        if unit == ElectricApparentPowerUnits.Millivoltampere:
            return f"""{super()._truncate_fraction_digits(self.millivoltamperes, fractional_digits)} mVA"""
        
        if unit == ElectricApparentPowerUnits.Kilovoltampere:
            return f"""{super()._truncate_fraction_digits(self.kilovoltamperes, fractional_digits)} kVA"""
        
        if unit == ElectricApparentPowerUnits.Megavoltampere:
            return f"""{super()._truncate_fraction_digits(self.megavoltamperes, fractional_digits)} MVA"""
        
        if unit == ElectricApparentPowerUnits.Gigavoltampere:
            return f"""{super()._truncate_fraction_digits(self.gigavoltamperes, fractional_digits)} GVA"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: ElectricApparentPowerUnits = ElectricApparentPowerUnits.Voltampere) -> str:
        """
        Get ElectricApparentPower unit abbreviation.
        Note! the default abbreviation for ElectricApparentPower is Voltampere.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == ElectricApparentPowerUnits.Voltampere:
            return """VA"""
        
        if unit_abbreviation == ElectricApparentPowerUnits.Microvoltampere:
            return """μVA"""
        
        if unit_abbreviation == ElectricApparentPowerUnits.Millivoltampere:
            return """mVA"""
        
        if unit_abbreviation == ElectricApparentPowerUnits.Kilovoltampere:
            return """kVA"""
        
        if unit_abbreviation == ElectricApparentPowerUnits.Megavoltampere:
            return """MVA"""
        
        if unit_abbreviation == ElectricApparentPowerUnits.Gigavoltampere:
            return """GVA"""
        
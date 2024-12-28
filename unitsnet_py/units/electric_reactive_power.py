from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class ElectricReactivePowerUnits(Enum):
        """
            ElectricReactivePowerUnits enumeration
        """
        
        VoltampereReactive = 'VoltampereReactive'
        """
            
        """
        
        KilovoltampereReactive = 'KilovoltampereReactive'
        """
            
        """
        
        MegavoltampereReactive = 'MegavoltampereReactive'
        """
            
        """
        
        GigavoltampereReactive = 'GigavoltampereReactive'
        """
            
        """
        

class ElectricReactivePowerDto:
    """
    A DTO representation of a ElectricReactivePower

    Attributes:
        value (float): The value of the ElectricReactivePower.
        unit (ElectricReactivePowerUnits): The specific unit that the ElectricReactivePower value is representing.
    """

    def __init__(self, value: float, unit: ElectricReactivePowerUnits):
        """
        Create a new DTO representation of a ElectricReactivePower

        Parameters:
            value (float): The value of the ElectricReactivePower.
            unit (ElectricReactivePowerUnits): The specific unit that the ElectricReactivePower value is representing.
        """
        self.value: float = value
        """
        The value of the ElectricReactivePower
        """
        self.unit: ElectricReactivePowerUnits = unit
        """
        The specific unit that the ElectricReactivePower value is representing
        """

    def to_json(self):
        """
        Get a ElectricReactivePower DTO JSON object representing the current unit.

        :return: JSON object represents ElectricReactivePower DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "VoltampereReactive"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of ElectricReactivePower DTO from a json representation.

        :param data: The ElectricReactivePower DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "VoltampereReactive"}
        :return: A new instance of ElectricReactivePowerDto.
        :rtype: ElectricReactivePowerDto
        """
        return ElectricReactivePowerDto(value=data["value"], unit=ElectricReactivePowerUnits(data["unit"]))


class ElectricReactivePower(AbstractMeasure):
    """
    In electric power transmission and distribution, volt-ampere reactive (var) is a unit of measurement of reactive power. Reactive power exists in an AC circuit when the current and voltage are not in phase.

    Args:
        value (float): The value.
        from_unit (ElectricReactivePowerUnits): The ElectricReactivePower unit to create from, The default unit is VoltampereReactive
    """
    def __init__(self, value: float, from_unit: ElectricReactivePowerUnits = ElectricReactivePowerUnits.VoltampereReactive):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__voltamperes_reactive = None
        
        self.__kilovoltamperes_reactive = None
        
        self.__megavoltamperes_reactive = None
        
        self.__gigavoltamperes_reactive = None
        

    def convert(self, unit: ElectricReactivePowerUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: ElectricReactivePowerUnits = ElectricReactivePowerUnits.VoltampereReactive) -> ElectricReactivePowerDto:
        """
        Get a new instance of ElectricReactivePower DTO representing the current unit.

        :param hold_in_unit: The specific ElectricReactivePower unit to store the ElectricReactivePower value in the DTO representation.
        :type hold_in_unit: ElectricReactivePowerUnits
        :return: A new instance of ElectricReactivePowerDto.
        :rtype: ElectricReactivePowerDto
        """
        return ElectricReactivePowerDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: ElectricReactivePowerUnits = ElectricReactivePowerUnits.VoltampereReactive):
        """
        Get a ElectricReactivePower DTO JSON object representing the current unit.

        :param hold_in_unit: The specific ElectricReactivePower unit to store the ElectricReactivePower value in the DTO representation.
        :type hold_in_unit: ElectricReactivePowerUnits
        :return: JSON object represents ElectricReactivePower DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "VoltampereReactive"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(electric_reactive_power_dto: ElectricReactivePowerDto):
        """
        Obtain a new instance of ElectricReactivePower from a DTO unit object.

        :param electric_reactive_power_dto: The ElectricReactivePower DTO representation.
        :type electric_reactive_power_dto: ElectricReactivePowerDto
        :return: A new instance of ElectricReactivePower.
        :rtype: ElectricReactivePower
        """
        return ElectricReactivePower(electric_reactive_power_dto.value, electric_reactive_power_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of ElectricReactivePower from a DTO unit json representation.

        :param data: The ElectricReactivePower DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "VoltampereReactive"}
        :return: A new instance of ElectricReactivePower.
        :rtype: ElectricReactivePower
        """
        return ElectricReactivePower.from_dto(ElectricReactivePowerDto.from_json(data))

    def __convert_from_base(self, from_unit: ElectricReactivePowerUnits) -> float:
        value = self._value
        
        if from_unit == ElectricReactivePowerUnits.VoltampereReactive:
            return (value)
        
        if from_unit == ElectricReactivePowerUnits.KilovoltampereReactive:
            return ((value) / 1000.0)
        
        if from_unit == ElectricReactivePowerUnits.MegavoltampereReactive:
            return ((value) / 1000000.0)
        
        if from_unit == ElectricReactivePowerUnits.GigavoltampereReactive:
            return ((value) / 1000000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: ElectricReactivePowerUnits) -> float:
        
        if to_unit == ElectricReactivePowerUnits.VoltampereReactive:
            return (value)
        
        if to_unit == ElectricReactivePowerUnits.KilovoltampereReactive:
            return ((value) * 1000.0)
        
        if to_unit == ElectricReactivePowerUnits.MegavoltampereReactive:
            return ((value) * 1000000.0)
        
        if to_unit == ElectricReactivePowerUnits.GigavoltampereReactive:
            return ((value) * 1000000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_voltamperes_reactive(voltamperes_reactive: float):
        """
        Create a new instance of ElectricReactivePower from a value in voltamperes_reactive.

        

        :param meters: The ElectricReactivePower value in voltamperes_reactive.
        :type voltamperes_reactive: float
        :return: A new instance of ElectricReactivePower.
        :rtype: ElectricReactivePower
        """
        return ElectricReactivePower(voltamperes_reactive, ElectricReactivePowerUnits.VoltampereReactive)

    
    @staticmethod
    def from_kilovoltamperes_reactive(kilovoltamperes_reactive: float):
        """
        Create a new instance of ElectricReactivePower from a value in kilovoltamperes_reactive.

        

        :param meters: The ElectricReactivePower value in kilovoltamperes_reactive.
        :type kilovoltamperes_reactive: float
        :return: A new instance of ElectricReactivePower.
        :rtype: ElectricReactivePower
        """
        return ElectricReactivePower(kilovoltamperes_reactive, ElectricReactivePowerUnits.KilovoltampereReactive)

    
    @staticmethod
    def from_megavoltamperes_reactive(megavoltamperes_reactive: float):
        """
        Create a new instance of ElectricReactivePower from a value in megavoltamperes_reactive.

        

        :param meters: The ElectricReactivePower value in megavoltamperes_reactive.
        :type megavoltamperes_reactive: float
        :return: A new instance of ElectricReactivePower.
        :rtype: ElectricReactivePower
        """
        return ElectricReactivePower(megavoltamperes_reactive, ElectricReactivePowerUnits.MegavoltampereReactive)

    
    @staticmethod
    def from_gigavoltamperes_reactive(gigavoltamperes_reactive: float):
        """
        Create a new instance of ElectricReactivePower from a value in gigavoltamperes_reactive.

        

        :param meters: The ElectricReactivePower value in gigavoltamperes_reactive.
        :type gigavoltamperes_reactive: float
        :return: A new instance of ElectricReactivePower.
        :rtype: ElectricReactivePower
        """
        return ElectricReactivePower(gigavoltamperes_reactive, ElectricReactivePowerUnits.GigavoltampereReactive)

    
    @property
    def voltamperes_reactive(self) -> float:
        """
        
        """
        if self.__voltamperes_reactive != None:
            return self.__voltamperes_reactive
        self.__voltamperes_reactive = self.__convert_from_base(ElectricReactivePowerUnits.VoltampereReactive)
        return self.__voltamperes_reactive

    
    @property
    def kilovoltamperes_reactive(self) -> float:
        """
        
        """
        if self.__kilovoltamperes_reactive != None:
            return self.__kilovoltamperes_reactive
        self.__kilovoltamperes_reactive = self.__convert_from_base(ElectricReactivePowerUnits.KilovoltampereReactive)
        return self.__kilovoltamperes_reactive

    
    @property
    def megavoltamperes_reactive(self) -> float:
        """
        
        """
        if self.__megavoltamperes_reactive != None:
            return self.__megavoltamperes_reactive
        self.__megavoltamperes_reactive = self.__convert_from_base(ElectricReactivePowerUnits.MegavoltampereReactive)
        return self.__megavoltamperes_reactive

    
    @property
    def gigavoltamperes_reactive(self) -> float:
        """
        
        """
        if self.__gigavoltamperes_reactive != None:
            return self.__gigavoltamperes_reactive
        self.__gigavoltamperes_reactive = self.__convert_from_base(ElectricReactivePowerUnits.GigavoltampereReactive)
        return self.__gigavoltamperes_reactive

    
    def to_string(self, unit: ElectricReactivePowerUnits = ElectricReactivePowerUnits.VoltampereReactive, fractional_digits: int = None) -> str:
        """
        Format the ElectricReactivePower to a string.
        
        Note: the default format for ElectricReactivePower is VoltampereReactive.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the ElectricReactivePower. Default is 'VoltampereReactive'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == ElectricReactivePowerUnits.VoltampereReactive:
            return f"""{super()._truncate_fraction_digits(self.voltamperes_reactive, fractional_digits)} var"""
        
        if unit == ElectricReactivePowerUnits.KilovoltampereReactive:
            return f"""{super()._truncate_fraction_digits(self.kilovoltamperes_reactive, fractional_digits)} kvar"""
        
        if unit == ElectricReactivePowerUnits.MegavoltampereReactive:
            return f"""{super()._truncate_fraction_digits(self.megavoltamperes_reactive, fractional_digits)} Mvar"""
        
        if unit == ElectricReactivePowerUnits.GigavoltampereReactive:
            return f"""{super()._truncate_fraction_digits(self.gigavoltamperes_reactive, fractional_digits)} Gvar"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: ElectricReactivePowerUnits = ElectricReactivePowerUnits.VoltampereReactive) -> str:
        """
        Get ElectricReactivePower unit abbreviation.
        Note! the default abbreviation for ElectricReactivePower is VoltampereReactive.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == ElectricReactivePowerUnits.VoltampereReactive:
            return """var"""
        
        if unit_abbreviation == ElectricReactivePowerUnits.KilovoltampereReactive:
            return """kvar"""
        
        if unit_abbreviation == ElectricReactivePowerUnits.MegavoltampereReactive:
            return """Mvar"""
        
        if unit_abbreviation == ElectricReactivePowerUnits.GigavoltampereReactive:
            return """Gvar"""
        
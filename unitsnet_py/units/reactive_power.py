from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class ReactivePowerUnits(Enum):
        """
            ReactivePowerUnits enumeration
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
        

class ReactivePowerDto:
    """
    A DTO representation of a ReactivePower

    Attributes:
        value (float): The value of the ReactivePower.
        unit (ReactivePowerUnits): The specific unit that the ReactivePower value is representing.
    """

    def __init__(self, value: float, unit: ReactivePowerUnits):
        """
        Create a new DTO representation of a ReactivePower

        Parameters:
            value (float): The value of the ReactivePower.
            unit (ReactivePowerUnits): The specific unit that the ReactivePower value is representing.
        """
        self.value: float = value
        """
        The value of the ReactivePower
        """
        self.unit: ReactivePowerUnits = unit
        """
        The specific unit that the ReactivePower value is representing
        """

    def to_json(self):
        """
        Get a ReactivePower DTO JSON object representing the current unit.

        :return: JSON object represents ReactivePower DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "VoltampereReactive"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of ReactivePower DTO from a json representation.

        :param data: The ReactivePower DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "VoltampereReactive"}
        :return: A new instance of ReactivePowerDto.
        :rtype: ReactivePowerDto
        """
        return ReactivePowerDto(value=data["value"], unit=ReactivePowerUnits(data["unit"]))


class ReactivePower(AbstractMeasure):
    """
    Volt-ampere reactive (var) is a unit by which reactive power is expressed in an AC electric power system. Reactive power exists in an AC circuit when the current and voltage are not in phase.

    Args:
        value (float): The value.
        from_unit (ReactivePowerUnits): The ReactivePower unit to create from, The default unit is VoltampereReactive
    """
    def __init__(self, value: float, from_unit: ReactivePowerUnits = ReactivePowerUnits.VoltampereReactive):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__voltamperes_reactive = None
        
        self.__kilovoltamperes_reactive = None
        
        self.__megavoltamperes_reactive = None
        
        self.__gigavoltamperes_reactive = None
        

    def convert(self, unit: ReactivePowerUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: ReactivePowerUnits = ReactivePowerUnits.VoltampereReactive) -> ReactivePowerDto:
        """
        Get a new instance of ReactivePower DTO representing the current unit.

        :param hold_in_unit: The specific ReactivePower unit to store the ReactivePower value in the DTO representation.
        :type hold_in_unit: ReactivePowerUnits
        :return: A new instance of ReactivePowerDto.
        :rtype: ReactivePowerDto
        """
        return ReactivePowerDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: ReactivePowerUnits = ReactivePowerUnits.VoltampereReactive):
        """
        Get a ReactivePower DTO JSON object representing the current unit.

        :param hold_in_unit: The specific ReactivePower unit to store the ReactivePower value in the DTO representation.
        :type hold_in_unit: ReactivePowerUnits
        :return: JSON object represents ReactivePower DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "VoltampereReactive"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(reactive_power_dto: ReactivePowerDto):
        """
        Obtain a new instance of ReactivePower from a DTO unit object.

        :param reactive_power_dto: The ReactivePower DTO representation.
        :type reactive_power_dto: ReactivePowerDto
        :return: A new instance of ReactivePower.
        :rtype: ReactivePower
        """
        return ReactivePower(reactive_power_dto.value, reactive_power_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of ReactivePower from a DTO unit json representation.

        :param data: The ReactivePower DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "VoltampereReactive"}
        :return: A new instance of ReactivePower.
        :rtype: ReactivePower
        """
        return ReactivePower.from_dto(ReactivePowerDto.from_json(data))

    def __convert_from_base(self, from_unit: ReactivePowerUnits) -> float:
        value = self._value
        
        if from_unit == ReactivePowerUnits.VoltampereReactive:
            return (value)
        
        if from_unit == ReactivePowerUnits.KilovoltampereReactive:
            return ((value) / 1000.0)
        
        if from_unit == ReactivePowerUnits.MegavoltampereReactive:
            return ((value) / 1000000.0)
        
        if from_unit == ReactivePowerUnits.GigavoltampereReactive:
            return ((value) / 1000000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: ReactivePowerUnits) -> float:
        
        if to_unit == ReactivePowerUnits.VoltampereReactive:
            return (value)
        
        if to_unit == ReactivePowerUnits.KilovoltampereReactive:
            return ((value) * 1000.0)
        
        if to_unit == ReactivePowerUnits.MegavoltampereReactive:
            return ((value) * 1000000.0)
        
        if to_unit == ReactivePowerUnits.GigavoltampereReactive:
            return ((value) * 1000000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_voltamperes_reactive(voltamperes_reactive: float):
        """
        Create a new instance of ReactivePower from a value in voltamperes_reactive.

        

        :param meters: The ReactivePower value in voltamperes_reactive.
        :type voltamperes_reactive: float
        :return: A new instance of ReactivePower.
        :rtype: ReactivePower
        """
        return ReactivePower(voltamperes_reactive, ReactivePowerUnits.VoltampereReactive)

    
    @staticmethod
    def from_kilovoltamperes_reactive(kilovoltamperes_reactive: float):
        """
        Create a new instance of ReactivePower from a value in kilovoltamperes_reactive.

        

        :param meters: The ReactivePower value in kilovoltamperes_reactive.
        :type kilovoltamperes_reactive: float
        :return: A new instance of ReactivePower.
        :rtype: ReactivePower
        """
        return ReactivePower(kilovoltamperes_reactive, ReactivePowerUnits.KilovoltampereReactive)

    
    @staticmethod
    def from_megavoltamperes_reactive(megavoltamperes_reactive: float):
        """
        Create a new instance of ReactivePower from a value in megavoltamperes_reactive.

        

        :param meters: The ReactivePower value in megavoltamperes_reactive.
        :type megavoltamperes_reactive: float
        :return: A new instance of ReactivePower.
        :rtype: ReactivePower
        """
        return ReactivePower(megavoltamperes_reactive, ReactivePowerUnits.MegavoltampereReactive)

    
    @staticmethod
    def from_gigavoltamperes_reactive(gigavoltamperes_reactive: float):
        """
        Create a new instance of ReactivePower from a value in gigavoltamperes_reactive.

        

        :param meters: The ReactivePower value in gigavoltamperes_reactive.
        :type gigavoltamperes_reactive: float
        :return: A new instance of ReactivePower.
        :rtype: ReactivePower
        """
        return ReactivePower(gigavoltamperes_reactive, ReactivePowerUnits.GigavoltampereReactive)

    
    @property
    def voltamperes_reactive(self) -> float:
        """
        
        """
        if self.__voltamperes_reactive != None:
            return self.__voltamperes_reactive
        self.__voltamperes_reactive = self.__convert_from_base(ReactivePowerUnits.VoltampereReactive)
        return self.__voltamperes_reactive

    
    @property
    def kilovoltamperes_reactive(self) -> float:
        """
        
        """
        if self.__kilovoltamperes_reactive != None:
            return self.__kilovoltamperes_reactive
        self.__kilovoltamperes_reactive = self.__convert_from_base(ReactivePowerUnits.KilovoltampereReactive)
        return self.__kilovoltamperes_reactive

    
    @property
    def megavoltamperes_reactive(self) -> float:
        """
        
        """
        if self.__megavoltamperes_reactive != None:
            return self.__megavoltamperes_reactive
        self.__megavoltamperes_reactive = self.__convert_from_base(ReactivePowerUnits.MegavoltampereReactive)
        return self.__megavoltamperes_reactive

    
    @property
    def gigavoltamperes_reactive(self) -> float:
        """
        
        """
        if self.__gigavoltamperes_reactive != None:
            return self.__gigavoltamperes_reactive
        self.__gigavoltamperes_reactive = self.__convert_from_base(ReactivePowerUnits.GigavoltampereReactive)
        return self.__gigavoltamperes_reactive

    
    def to_string(self, unit: ReactivePowerUnits = ReactivePowerUnits.VoltampereReactive, fractional_digits: int = None) -> str:
        """
        Format the ReactivePower to a string.
        
        Note: the default format for ReactivePower is VoltampereReactive.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the ReactivePower. Default is 'VoltampereReactive'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == ReactivePowerUnits.VoltampereReactive:
            return f"""{super()._truncate_fraction_digits(self.voltamperes_reactive, fractional_digits)} var"""
        
        if unit == ReactivePowerUnits.KilovoltampereReactive:
            return f"""{super()._truncate_fraction_digits(self.kilovoltamperes_reactive, fractional_digits)} kvar"""
        
        if unit == ReactivePowerUnits.MegavoltampereReactive:
            return f"""{super()._truncate_fraction_digits(self.megavoltamperes_reactive, fractional_digits)} Mvar"""
        
        if unit == ReactivePowerUnits.GigavoltampereReactive:
            return f"""{super()._truncate_fraction_digits(self.gigavoltamperes_reactive, fractional_digits)} Gvar"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: ReactivePowerUnits = ReactivePowerUnits.VoltampereReactive) -> str:
        """
        Get ReactivePower unit abbreviation.
        Note! the default abbreviation for ReactivePower is VoltampereReactive.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == ReactivePowerUnits.VoltampereReactive:
            return """var"""
        
        if unit_abbreviation == ReactivePowerUnits.KilovoltampereReactive:
            return """kvar"""
        
        if unit_abbreviation == ReactivePowerUnits.MegavoltampereReactive:
            return """Mvar"""
        
        if unit_abbreviation == ReactivePowerUnits.GigavoltampereReactive:
            return """Gvar"""
        
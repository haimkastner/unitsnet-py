from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class ReactiveEnergyUnits(Enum):
        """
            ReactiveEnergyUnits enumeration
        """
        
        VoltampereReactiveHour = 'VoltampereReactiveHour'
        """
            
        """
        
        KilovoltampereReactiveHour = 'KilovoltampereReactiveHour'
        """
            
        """
        
        MegavoltampereReactiveHour = 'MegavoltampereReactiveHour'
        """
            
        """
        

class ReactiveEnergyDto:
    """
    A DTO representation of a ReactiveEnergy

    Attributes:
        value (float): The value of the ReactiveEnergy.
        unit (ReactiveEnergyUnits): The specific unit that the ReactiveEnergy value is representing.
    """

    def __init__(self, value: float, unit: ReactiveEnergyUnits):
        """
        Create a new DTO representation of a ReactiveEnergy

        Parameters:
            value (float): The value of the ReactiveEnergy.
            unit (ReactiveEnergyUnits): The specific unit that the ReactiveEnergy value is representing.
        """
        self.value: float = value
        """
        The value of the ReactiveEnergy
        """
        self.unit: ReactiveEnergyUnits = unit
        """
        The specific unit that the ReactiveEnergy value is representing
        """

    def to_json(self):
        """
        Get a ReactiveEnergy DTO JSON object representing the current unit.

        :return: JSON object represents ReactiveEnergy DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "VoltampereReactiveHour"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of ReactiveEnergy DTO from a json representation.

        :param data: The ReactiveEnergy DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "VoltampereReactiveHour"}
        :return: A new instance of ReactiveEnergyDto.
        :rtype: ReactiveEnergyDto
        """
        return ReactiveEnergyDto(value=data["value"], unit=ReactiveEnergyUnits(data["unit"]))


class ReactiveEnergy(AbstractMeasure):
    """
    The Volt-ampere reactive hour (expressed as varh) is the reactive power of one Volt-ampere reactive produced in one hour.

    Args:
        value (float): The value.
        from_unit (ReactiveEnergyUnits): The ReactiveEnergy unit to create from, The default unit is VoltampereReactiveHour
    """
    def __init__(self, value: float, from_unit: ReactiveEnergyUnits = ReactiveEnergyUnits.VoltampereReactiveHour):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__voltampere_reactive_hours = None
        
        self.__kilovoltampere_reactive_hours = None
        
        self.__megavoltampere_reactive_hours = None
        

    def convert(self, unit: ReactiveEnergyUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: ReactiveEnergyUnits = ReactiveEnergyUnits.VoltampereReactiveHour) -> ReactiveEnergyDto:
        """
        Get a new instance of ReactiveEnergy DTO representing the current unit.

        :param hold_in_unit: The specific ReactiveEnergy unit to store the ReactiveEnergy value in the DTO representation.
        :type hold_in_unit: ReactiveEnergyUnits
        :return: A new instance of ReactiveEnergyDto.
        :rtype: ReactiveEnergyDto
        """
        return ReactiveEnergyDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: ReactiveEnergyUnits = ReactiveEnergyUnits.VoltampereReactiveHour):
        """
        Get a ReactiveEnergy DTO JSON object representing the current unit.

        :param hold_in_unit: The specific ReactiveEnergy unit to store the ReactiveEnergy value in the DTO representation.
        :type hold_in_unit: ReactiveEnergyUnits
        :return: JSON object represents ReactiveEnergy DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "VoltampereReactiveHour"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(reactive_energy_dto: ReactiveEnergyDto):
        """
        Obtain a new instance of ReactiveEnergy from a DTO unit object.

        :param reactive_energy_dto: The ReactiveEnergy DTO representation.
        :type reactive_energy_dto: ReactiveEnergyDto
        :return: A new instance of ReactiveEnergy.
        :rtype: ReactiveEnergy
        """
        return ReactiveEnergy(reactive_energy_dto.value, reactive_energy_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of ReactiveEnergy from a DTO unit json representation.

        :param data: The ReactiveEnergy DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "VoltampereReactiveHour"}
        :return: A new instance of ReactiveEnergy.
        :rtype: ReactiveEnergy
        """
        return ReactiveEnergy.from_dto(ReactiveEnergyDto.from_json(data))

    def __convert_from_base(self, from_unit: ReactiveEnergyUnits) -> float:
        value = self._value
        
        if from_unit == ReactiveEnergyUnits.VoltampereReactiveHour:
            return (value)
        
        if from_unit == ReactiveEnergyUnits.KilovoltampereReactiveHour:
            return ((value) / 1000.0)
        
        if from_unit == ReactiveEnergyUnits.MegavoltampereReactiveHour:
            return ((value) / 1000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: ReactiveEnergyUnits) -> float:
        
        if to_unit == ReactiveEnergyUnits.VoltampereReactiveHour:
            return (value)
        
        if to_unit == ReactiveEnergyUnits.KilovoltampereReactiveHour:
            return ((value) * 1000.0)
        
        if to_unit == ReactiveEnergyUnits.MegavoltampereReactiveHour:
            return ((value) * 1000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_voltampere_reactive_hours(voltampere_reactive_hours: float):
        """
        Create a new instance of ReactiveEnergy from a value in voltampere_reactive_hours.

        

        :param meters: The ReactiveEnergy value in voltampere_reactive_hours.
        :type voltampere_reactive_hours: float
        :return: A new instance of ReactiveEnergy.
        :rtype: ReactiveEnergy
        """
        return ReactiveEnergy(voltampere_reactive_hours, ReactiveEnergyUnits.VoltampereReactiveHour)

    
    @staticmethod
    def from_kilovoltampere_reactive_hours(kilovoltampere_reactive_hours: float):
        """
        Create a new instance of ReactiveEnergy from a value in kilovoltampere_reactive_hours.

        

        :param meters: The ReactiveEnergy value in kilovoltampere_reactive_hours.
        :type kilovoltampere_reactive_hours: float
        :return: A new instance of ReactiveEnergy.
        :rtype: ReactiveEnergy
        """
        return ReactiveEnergy(kilovoltampere_reactive_hours, ReactiveEnergyUnits.KilovoltampereReactiveHour)

    
    @staticmethod
    def from_megavoltampere_reactive_hours(megavoltampere_reactive_hours: float):
        """
        Create a new instance of ReactiveEnergy from a value in megavoltampere_reactive_hours.

        

        :param meters: The ReactiveEnergy value in megavoltampere_reactive_hours.
        :type megavoltampere_reactive_hours: float
        :return: A new instance of ReactiveEnergy.
        :rtype: ReactiveEnergy
        """
        return ReactiveEnergy(megavoltampere_reactive_hours, ReactiveEnergyUnits.MegavoltampereReactiveHour)

    
    @property
    def voltampere_reactive_hours(self) -> float:
        """
        
        """
        if self.__voltampere_reactive_hours != None:
            return self.__voltampere_reactive_hours
        self.__voltampere_reactive_hours = self.__convert_from_base(ReactiveEnergyUnits.VoltampereReactiveHour)
        return self.__voltampere_reactive_hours

    
    @property
    def kilovoltampere_reactive_hours(self) -> float:
        """
        
        """
        if self.__kilovoltampere_reactive_hours != None:
            return self.__kilovoltampere_reactive_hours
        self.__kilovoltampere_reactive_hours = self.__convert_from_base(ReactiveEnergyUnits.KilovoltampereReactiveHour)
        return self.__kilovoltampere_reactive_hours

    
    @property
    def megavoltampere_reactive_hours(self) -> float:
        """
        
        """
        if self.__megavoltampere_reactive_hours != None:
            return self.__megavoltampere_reactive_hours
        self.__megavoltampere_reactive_hours = self.__convert_from_base(ReactiveEnergyUnits.MegavoltampereReactiveHour)
        return self.__megavoltampere_reactive_hours

    
    def to_string(self, unit: ReactiveEnergyUnits = ReactiveEnergyUnits.VoltampereReactiveHour, fractional_digits: int = None) -> str:
        """
        Format the ReactiveEnergy to a string.
        
        Note: the default format for ReactiveEnergy is VoltampereReactiveHour.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the ReactiveEnergy. Default is 'VoltampereReactiveHour'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == ReactiveEnergyUnits.VoltampereReactiveHour:
            return f"""{super()._truncate_fraction_digits(self.voltampere_reactive_hours, fractional_digits)} varh"""
        
        if unit == ReactiveEnergyUnits.KilovoltampereReactiveHour:
            return f"""{super()._truncate_fraction_digits(self.kilovoltampere_reactive_hours, fractional_digits)} kvarh"""
        
        if unit == ReactiveEnergyUnits.MegavoltampereReactiveHour:
            return f"""{super()._truncate_fraction_digits(self.megavoltampere_reactive_hours, fractional_digits)} Mvarh"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: ReactiveEnergyUnits = ReactiveEnergyUnits.VoltampereReactiveHour) -> str:
        """
        Get ReactiveEnergy unit abbreviation.
        Note! the default abbreviation for ReactiveEnergy is VoltampereReactiveHour.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == ReactiveEnergyUnits.VoltampereReactiveHour:
            return """varh"""
        
        if unit_abbreviation == ReactiveEnergyUnits.KilovoltampereReactiveHour:
            return """kvarh"""
        
        if unit_abbreviation == ReactiveEnergyUnits.MegavoltampereReactiveHour:
            return """Mvarh"""
        
from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class ElectricCurrentDensityUnits(Enum):
        """
            ElectricCurrentDensityUnits enumeration
        """
        
        AmperePerSquareMeter = 'AmperePerSquareMeter'
        """
            
        """
        
        AmperePerSquareInch = 'AmperePerSquareInch'
        """
            
        """
        
        AmperePerSquareFoot = 'AmperePerSquareFoot'
        """
            
        """
        

class ElectricCurrentDensityDto:
    """
    A DTO representation of a ElectricCurrentDensity

    Attributes:
        value (float): The value of the ElectricCurrentDensity.
        unit (ElectricCurrentDensityUnits): The specific unit that the ElectricCurrentDensity value is representing.
    """

    def __init__(self, value: float, unit: ElectricCurrentDensityUnits):
        """
        Create a new DTO representation of a ElectricCurrentDensity

        Parameters:
            value (float): The value of the ElectricCurrentDensity.
            unit (ElectricCurrentDensityUnits): The specific unit that the ElectricCurrentDensity value is representing.
        """
        self.value: float = value
        """
        The value of the ElectricCurrentDensity
        """
        self.unit: ElectricCurrentDensityUnits = unit
        """
        The specific unit that the ElectricCurrentDensity value is representing
        """

    def to_json(self):
        """
        Get a ElectricCurrentDensity DTO JSON object representing the current unit.

        :return: JSON object represents ElectricCurrentDensity DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "AmperePerSquareMeter"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of ElectricCurrentDensity DTO from a json representation.

        :param data: The ElectricCurrentDensity DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "AmperePerSquareMeter"}
        :return: A new instance of ElectricCurrentDensityDto.
        :rtype: ElectricCurrentDensityDto
        """
        return ElectricCurrentDensityDto(value=data["value"], unit=ElectricCurrentDensityUnits(data["unit"]))


class ElectricCurrentDensity(AbstractMeasure):
    """
    In electromagnetism, current density is the electric current per unit area of cross section.

    Args:
        value (float): The value.
        from_unit (ElectricCurrentDensityUnits): The ElectricCurrentDensity unit to create from, The default unit is AmperePerSquareMeter
    """
    def __init__(self, value: float, from_unit: ElectricCurrentDensityUnits = ElectricCurrentDensityUnits.AmperePerSquareMeter):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__amperes_per_square_meter = None
        
        self.__amperes_per_square_inch = None
        
        self.__amperes_per_square_foot = None
        

    def convert(self, unit: ElectricCurrentDensityUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: ElectricCurrentDensityUnits = ElectricCurrentDensityUnits.AmperePerSquareMeter) -> ElectricCurrentDensityDto:
        """
        Get a new instance of ElectricCurrentDensity DTO representing the current unit.

        :param hold_in_unit: The specific ElectricCurrentDensity unit to store the ElectricCurrentDensity value in the DTO representation.
        :type hold_in_unit: ElectricCurrentDensityUnits
        :return: A new instance of ElectricCurrentDensityDto.
        :rtype: ElectricCurrentDensityDto
        """
        return ElectricCurrentDensityDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: ElectricCurrentDensityUnits = ElectricCurrentDensityUnits.AmperePerSquareMeter):
        """
        Get a ElectricCurrentDensity DTO JSON object representing the current unit.

        :param hold_in_unit: The specific ElectricCurrentDensity unit to store the ElectricCurrentDensity value in the DTO representation.
        :type hold_in_unit: ElectricCurrentDensityUnits
        :return: JSON object represents ElectricCurrentDensity DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "AmperePerSquareMeter"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(electric_current_density_dto: ElectricCurrentDensityDto):
        """
        Obtain a new instance of ElectricCurrentDensity from a DTO unit object.

        :param electric_current_density_dto: The ElectricCurrentDensity DTO representation.
        :type electric_current_density_dto: ElectricCurrentDensityDto
        :return: A new instance of ElectricCurrentDensity.
        :rtype: ElectricCurrentDensity
        """
        return ElectricCurrentDensity(electric_current_density_dto.value, electric_current_density_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of ElectricCurrentDensity from a DTO unit json representation.

        :param data: The ElectricCurrentDensity DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "AmperePerSquareMeter"}
        :return: A new instance of ElectricCurrentDensity.
        :rtype: ElectricCurrentDensity
        """
        return ElectricCurrentDensity.from_dto(ElectricCurrentDensityDto.from_json(data))

    def __convert_from_base(self, from_unit: ElectricCurrentDensityUnits) -> float:
        value = self._value
        
        if from_unit == ElectricCurrentDensityUnits.AmperePerSquareMeter:
            return (value)
        
        if from_unit == ElectricCurrentDensityUnits.AmperePerSquareInch:
            return (value / 1.5500031000062000e3)
        
        if from_unit == ElectricCurrentDensityUnits.AmperePerSquareFoot:
            return (value / 1.0763910416709722e1)
        
        return None


    def __convert_to_base(self, value: float, to_unit: ElectricCurrentDensityUnits) -> float:
        
        if to_unit == ElectricCurrentDensityUnits.AmperePerSquareMeter:
            return (value)
        
        if to_unit == ElectricCurrentDensityUnits.AmperePerSquareInch:
            return (value * 1.5500031000062000e3)
        
        if to_unit == ElectricCurrentDensityUnits.AmperePerSquareFoot:
            return (value * 1.0763910416709722e1)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_amperes_per_square_meter(amperes_per_square_meter: float):
        """
        Create a new instance of ElectricCurrentDensity from a value in amperes_per_square_meter.

        

        :param meters: The ElectricCurrentDensity value in amperes_per_square_meter.
        :type amperes_per_square_meter: float
        :return: A new instance of ElectricCurrentDensity.
        :rtype: ElectricCurrentDensity
        """
        return ElectricCurrentDensity(amperes_per_square_meter, ElectricCurrentDensityUnits.AmperePerSquareMeter)

    
    @staticmethod
    def from_amperes_per_square_inch(amperes_per_square_inch: float):
        """
        Create a new instance of ElectricCurrentDensity from a value in amperes_per_square_inch.

        

        :param meters: The ElectricCurrentDensity value in amperes_per_square_inch.
        :type amperes_per_square_inch: float
        :return: A new instance of ElectricCurrentDensity.
        :rtype: ElectricCurrentDensity
        """
        return ElectricCurrentDensity(amperes_per_square_inch, ElectricCurrentDensityUnits.AmperePerSquareInch)

    
    @staticmethod
    def from_amperes_per_square_foot(amperes_per_square_foot: float):
        """
        Create a new instance of ElectricCurrentDensity from a value in amperes_per_square_foot.

        

        :param meters: The ElectricCurrentDensity value in amperes_per_square_foot.
        :type amperes_per_square_foot: float
        :return: A new instance of ElectricCurrentDensity.
        :rtype: ElectricCurrentDensity
        """
        return ElectricCurrentDensity(amperes_per_square_foot, ElectricCurrentDensityUnits.AmperePerSquareFoot)

    
    @property
    def amperes_per_square_meter(self) -> float:
        """
        
        """
        if self.__amperes_per_square_meter != None:
            return self.__amperes_per_square_meter
        self.__amperes_per_square_meter = self.__convert_from_base(ElectricCurrentDensityUnits.AmperePerSquareMeter)
        return self.__amperes_per_square_meter

    
    @property
    def amperes_per_square_inch(self) -> float:
        """
        
        """
        if self.__amperes_per_square_inch != None:
            return self.__amperes_per_square_inch
        self.__amperes_per_square_inch = self.__convert_from_base(ElectricCurrentDensityUnits.AmperePerSquareInch)
        return self.__amperes_per_square_inch

    
    @property
    def amperes_per_square_foot(self) -> float:
        """
        
        """
        if self.__amperes_per_square_foot != None:
            return self.__amperes_per_square_foot
        self.__amperes_per_square_foot = self.__convert_from_base(ElectricCurrentDensityUnits.AmperePerSquareFoot)
        return self.__amperes_per_square_foot

    
    def to_string(self, unit: ElectricCurrentDensityUnits = ElectricCurrentDensityUnits.AmperePerSquareMeter, fractional_digits: int = None) -> str:
        """
        Format the ElectricCurrentDensity to a string.
        
        Note: the default format for ElectricCurrentDensity is AmperePerSquareMeter.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the ElectricCurrentDensity. Default is 'AmperePerSquareMeter'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == ElectricCurrentDensityUnits.AmperePerSquareMeter:
            return f"""{super()._truncate_fraction_digits(self.amperes_per_square_meter, fractional_digits)} A/m²"""
        
        if unit == ElectricCurrentDensityUnits.AmperePerSquareInch:
            return f"""{super()._truncate_fraction_digits(self.amperes_per_square_inch, fractional_digits)} A/in²"""
        
        if unit == ElectricCurrentDensityUnits.AmperePerSquareFoot:
            return f"""{super()._truncate_fraction_digits(self.amperes_per_square_foot, fractional_digits)} A/ft²"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: ElectricCurrentDensityUnits = ElectricCurrentDensityUnits.AmperePerSquareMeter) -> str:
        """
        Get ElectricCurrentDensity unit abbreviation.
        Note! the default abbreviation for ElectricCurrentDensity is AmperePerSquareMeter.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == ElectricCurrentDensityUnits.AmperePerSquareMeter:
            return """A/m²"""
        
        if unit_abbreviation == ElectricCurrentDensityUnits.AmperePerSquareInch:
            return """A/in²"""
        
        if unit_abbreviation == ElectricCurrentDensityUnits.AmperePerSquareFoot:
            return """A/ft²"""
        
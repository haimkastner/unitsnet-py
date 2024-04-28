from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class MagneticFluxUnits(Enum):
        """
            MagneticFluxUnits enumeration
        """
        
        Weber = 'Weber'
        """
            
        """
        

class MagneticFluxDto:
    """
    A DTO representation of a MagneticFlux

    Attributes:
        value (float): The value of the MagneticFlux.
        unit (MagneticFluxUnits): The specific unit that the MagneticFlux value is representing.
    """

    def __init__(self, value: float, unit: MagneticFluxUnits):
        """
        Create a new DTO representation of a MagneticFlux

        Parameters:
            value (float): The value of the MagneticFlux.
            unit (MagneticFluxUnits): The specific unit that the MagneticFlux value is representing.
        """
        self.value: float = value
        """
        The value of the MagneticFlux
        """
        self.unit: MagneticFluxUnits = unit
        """
        The specific unit that the MagneticFlux value is representing
        """

    def to_json(self):
        """
        Get a MagneticFlux DTO JSON object representing the current unit.

        :return: JSON object represents MagneticFlux DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "Weber"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of MagneticFlux DTO from a json representation.

        :param data: The MagneticFlux DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "Weber"}
        :return: A new instance of MagneticFluxDto.
        :rtype: MagneticFluxDto
        """
        return MagneticFluxDto(value=data["value"], unit=MagneticFluxUnits(data["unit"]))


class MagneticFlux(AbstractMeasure):
    """
    In physics, specifically electromagnetism, the magnetic flux through a surface is the surface integral of the normal component of the magnetic field B passing through that surface.

    Args:
        value (float): The value.
        from_unit (MagneticFluxUnits): The MagneticFlux unit to create from, The default unit is Weber
    """
    def __init__(self, value: float, from_unit: MagneticFluxUnits = MagneticFluxUnits.Weber):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__webers = None
        

    def convert(self, unit: MagneticFluxUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: MagneticFluxUnits = MagneticFluxUnits.Weber) -> MagneticFluxDto:
        """
        Get a new instance of MagneticFlux DTO representing the current unit.

        :param hold_in_unit: The specific MagneticFlux unit to store the MagneticFlux value in the DTO representation.
        :type hold_in_unit: MagneticFluxUnits
        :return: A new instance of MagneticFluxDto.
        :rtype: MagneticFluxDto
        """
        return MagneticFluxDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: MagneticFluxUnits = MagneticFluxUnits.Weber):
        """
        Get a MagneticFlux DTO JSON object representing the current unit.

        :param hold_in_unit: The specific MagneticFlux unit to store the MagneticFlux value in the DTO representation.
        :type hold_in_unit: MagneticFluxUnits
        :return: JSON object represents MagneticFlux DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "Weber"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(magnetic_flux_dto: MagneticFluxDto):
        """
        Obtain a new instance of MagneticFlux from a DTO unit object.

        :param magnetic_flux_dto: The MagneticFlux DTO representation.
        :type magnetic_flux_dto: MagneticFluxDto
        :return: A new instance of MagneticFlux.
        :rtype: MagneticFlux
        """
        return MagneticFlux(magnetic_flux_dto.value, magnetic_flux_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of MagneticFlux from a DTO unit json representation.

        :param data: The MagneticFlux DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "Weber"}
        :return: A new instance of MagneticFlux.
        :rtype: MagneticFlux
        """
        return MagneticFlux.from_dto(MagneticFluxDto.from_json(data))

    def __convert_from_base(self, from_unit: MagneticFluxUnits) -> float:
        value = self._value
        
        if from_unit == MagneticFluxUnits.Weber:
            return (value)
        
        return None


    def __convert_to_base(self, value: float, to_unit: MagneticFluxUnits) -> float:
        
        if to_unit == MagneticFluxUnits.Weber:
            return (value)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_webers(webers: float):
        """
        Create a new instance of MagneticFlux from a value in webers.

        

        :param meters: The MagneticFlux value in webers.
        :type webers: float
        :return: A new instance of MagneticFlux.
        :rtype: MagneticFlux
        """
        return MagneticFlux(webers, MagneticFluxUnits.Weber)

    
    @property
    def webers(self) -> float:
        """
        
        """
        if self.__webers != None:
            return self.__webers
        self.__webers = self.__convert_from_base(MagneticFluxUnits.Weber)
        return self.__webers

    
    def to_string(self, unit: MagneticFluxUnits = MagneticFluxUnits.Weber, fractional_digits: int = None) -> str:
        """
        Format the MagneticFlux to a string.
        
        Note: the default format for MagneticFlux is Weber.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the MagneticFlux. Default is 'Weber'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == MagneticFluxUnits.Weber:
            return f"""{super()._truncate_fraction_digits(self.webers, fractional_digits)} Wb"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: MagneticFluxUnits = MagneticFluxUnits.Weber) -> str:
        """
        Get MagneticFlux unit abbreviation.
        Note! the default abbreviation for MagneticFlux is Weber.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == MagneticFluxUnits.Weber:
            return """Wb"""
        
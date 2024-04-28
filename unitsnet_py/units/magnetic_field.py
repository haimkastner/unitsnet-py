from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class MagneticFieldUnits(Enum):
        """
            MagneticFieldUnits enumeration
        """
        
        Tesla = 'Tesla'
        """
            
        """
        
        Gauss = 'Gauss'
        """
            
        """
        
        Nanotesla = 'Nanotesla'
        """
            
        """
        
        Microtesla = 'Microtesla'
        """
            
        """
        
        Millitesla = 'Millitesla'
        """
            
        """
        
        Milligauss = 'Milligauss'
        """
            
        """
        

class MagneticFieldDto:
    """
    A DTO representation of a MagneticField

    Attributes:
        value (float): The value of the MagneticField.
        unit (MagneticFieldUnits): The specific unit that the MagneticField value is representing.
    """

    def __init__(self, value: float, unit: MagneticFieldUnits):
        """
        Create a new DTO representation of a MagneticField

        Parameters:
            value (float): The value of the MagneticField.
            unit (MagneticFieldUnits): The specific unit that the MagneticField value is representing.
        """
        self.value: float = value
        """
        The value of the MagneticField
        """
        self.unit: MagneticFieldUnits = unit
        """
        The specific unit that the MagneticField value is representing
        """

    def to_json(self):
        """
        Get a MagneticField DTO JSON object representing the current unit.

        :return: JSON object represents MagneticField DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "Tesla"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of MagneticField DTO from a json representation.

        :param data: The MagneticField DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "Tesla"}
        :return: A new instance of MagneticFieldDto.
        :rtype: MagneticFieldDto
        """
        return MagneticFieldDto(value=data["value"], unit=MagneticFieldUnits(data["unit"]))


class MagneticField(AbstractMeasure):
    """
    A magnetic field is a force field that is created by moving electric charges (electric currents) and magnetic dipoles, and exerts a force on other nearby moving charges and magnetic dipoles.

    Args:
        value (float): The value.
        from_unit (MagneticFieldUnits): The MagneticField unit to create from, The default unit is Tesla
    """
    def __init__(self, value: float, from_unit: MagneticFieldUnits = MagneticFieldUnits.Tesla):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__teslas = None
        
        self.__gausses = None
        
        self.__nanoteslas = None
        
        self.__microteslas = None
        
        self.__milliteslas = None
        
        self.__milligausses = None
        

    def convert(self, unit: MagneticFieldUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: MagneticFieldUnits = MagneticFieldUnits.Tesla) -> MagneticFieldDto:
        """
        Get a new instance of MagneticField DTO representing the current unit.

        :param hold_in_unit: The specific MagneticField unit to store the MagneticField value in the DTO representation.
        :type hold_in_unit: MagneticFieldUnits
        :return: A new instance of MagneticFieldDto.
        :rtype: MagneticFieldDto
        """
        return MagneticFieldDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: MagneticFieldUnits = MagneticFieldUnits.Tesla):
        """
        Get a MagneticField DTO JSON object representing the current unit.

        :param hold_in_unit: The specific MagneticField unit to store the MagneticField value in the DTO representation.
        :type hold_in_unit: MagneticFieldUnits
        :return: JSON object represents MagneticField DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "Tesla"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(magnetic_field_dto: MagneticFieldDto):
        """
        Obtain a new instance of MagneticField from a DTO unit object.

        :param magnetic_field_dto: The MagneticField DTO representation.
        :type magnetic_field_dto: MagneticFieldDto
        :return: A new instance of MagneticField.
        :rtype: MagneticField
        """
        return MagneticField(magnetic_field_dto.value, magnetic_field_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of MagneticField from a DTO unit json representation.

        :param data: The MagneticField DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "Tesla"}
        :return: A new instance of MagneticField.
        :rtype: MagneticField
        """
        return MagneticField.from_dto(MagneticFieldDto.from_json(data))

    def __convert_from_base(self, from_unit: MagneticFieldUnits) -> float:
        value = self._value
        
        if from_unit == MagneticFieldUnits.Tesla:
            return (value)
        
        if from_unit == MagneticFieldUnits.Gauss:
            return (value * 1e4)
        
        if from_unit == MagneticFieldUnits.Nanotesla:
            return ((value) / 1e-09)
        
        if from_unit == MagneticFieldUnits.Microtesla:
            return ((value) / 1e-06)
        
        if from_unit == MagneticFieldUnits.Millitesla:
            return ((value) / 0.001)
        
        if from_unit == MagneticFieldUnits.Milligauss:
            return ((value * 1e4) / 0.001)
        
        return None


    def __convert_to_base(self, value: float, to_unit: MagneticFieldUnits) -> float:
        
        if to_unit == MagneticFieldUnits.Tesla:
            return (value)
        
        if to_unit == MagneticFieldUnits.Gauss:
            return (value / 1e4)
        
        if to_unit == MagneticFieldUnits.Nanotesla:
            return ((value) * 1e-09)
        
        if to_unit == MagneticFieldUnits.Microtesla:
            return ((value) * 1e-06)
        
        if to_unit == MagneticFieldUnits.Millitesla:
            return ((value) * 0.001)
        
        if to_unit == MagneticFieldUnits.Milligauss:
            return ((value / 1e4) * 0.001)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_teslas(teslas: float):
        """
        Create a new instance of MagneticField from a value in teslas.

        

        :param meters: The MagneticField value in teslas.
        :type teslas: float
        :return: A new instance of MagneticField.
        :rtype: MagneticField
        """
        return MagneticField(teslas, MagneticFieldUnits.Tesla)

    
    @staticmethod
    def from_gausses(gausses: float):
        """
        Create a new instance of MagneticField from a value in gausses.

        

        :param meters: The MagneticField value in gausses.
        :type gausses: float
        :return: A new instance of MagneticField.
        :rtype: MagneticField
        """
        return MagneticField(gausses, MagneticFieldUnits.Gauss)

    
    @staticmethod
    def from_nanoteslas(nanoteslas: float):
        """
        Create a new instance of MagneticField from a value in nanoteslas.

        

        :param meters: The MagneticField value in nanoteslas.
        :type nanoteslas: float
        :return: A new instance of MagneticField.
        :rtype: MagneticField
        """
        return MagneticField(nanoteslas, MagneticFieldUnits.Nanotesla)

    
    @staticmethod
    def from_microteslas(microteslas: float):
        """
        Create a new instance of MagneticField from a value in microteslas.

        

        :param meters: The MagneticField value in microteslas.
        :type microteslas: float
        :return: A new instance of MagneticField.
        :rtype: MagneticField
        """
        return MagneticField(microteslas, MagneticFieldUnits.Microtesla)

    
    @staticmethod
    def from_milliteslas(milliteslas: float):
        """
        Create a new instance of MagneticField from a value in milliteslas.

        

        :param meters: The MagneticField value in milliteslas.
        :type milliteslas: float
        :return: A new instance of MagneticField.
        :rtype: MagneticField
        """
        return MagneticField(milliteslas, MagneticFieldUnits.Millitesla)

    
    @staticmethod
    def from_milligausses(milligausses: float):
        """
        Create a new instance of MagneticField from a value in milligausses.

        

        :param meters: The MagneticField value in milligausses.
        :type milligausses: float
        :return: A new instance of MagneticField.
        :rtype: MagneticField
        """
        return MagneticField(milligausses, MagneticFieldUnits.Milligauss)

    
    @property
    def teslas(self) -> float:
        """
        
        """
        if self.__teslas != None:
            return self.__teslas
        self.__teslas = self.__convert_from_base(MagneticFieldUnits.Tesla)
        return self.__teslas

    
    @property
    def gausses(self) -> float:
        """
        
        """
        if self.__gausses != None:
            return self.__gausses
        self.__gausses = self.__convert_from_base(MagneticFieldUnits.Gauss)
        return self.__gausses

    
    @property
    def nanoteslas(self) -> float:
        """
        
        """
        if self.__nanoteslas != None:
            return self.__nanoteslas
        self.__nanoteslas = self.__convert_from_base(MagneticFieldUnits.Nanotesla)
        return self.__nanoteslas

    
    @property
    def microteslas(self) -> float:
        """
        
        """
        if self.__microteslas != None:
            return self.__microteslas
        self.__microteslas = self.__convert_from_base(MagneticFieldUnits.Microtesla)
        return self.__microteslas

    
    @property
    def milliteslas(self) -> float:
        """
        
        """
        if self.__milliteslas != None:
            return self.__milliteslas
        self.__milliteslas = self.__convert_from_base(MagneticFieldUnits.Millitesla)
        return self.__milliteslas

    
    @property
    def milligausses(self) -> float:
        """
        
        """
        if self.__milligausses != None:
            return self.__milligausses
        self.__milligausses = self.__convert_from_base(MagneticFieldUnits.Milligauss)
        return self.__milligausses

    
    def to_string(self, unit: MagneticFieldUnits = MagneticFieldUnits.Tesla, fractional_digits: int = None) -> str:
        """
        Format the MagneticField to a string.
        
        Note: the default format for MagneticField is Tesla.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the MagneticField. Default is 'Tesla'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == MagneticFieldUnits.Tesla:
            return f"""{super()._truncate_fraction_digits(self.teslas, fractional_digits)} T"""
        
        if unit == MagneticFieldUnits.Gauss:
            return f"""{super()._truncate_fraction_digits(self.gausses, fractional_digits)} G"""
        
        if unit == MagneticFieldUnits.Nanotesla:
            return f"""{super()._truncate_fraction_digits(self.nanoteslas, fractional_digits)} nT"""
        
        if unit == MagneticFieldUnits.Microtesla:
            return f"""{super()._truncate_fraction_digits(self.microteslas, fractional_digits)} μT"""
        
        if unit == MagneticFieldUnits.Millitesla:
            return f"""{super()._truncate_fraction_digits(self.milliteslas, fractional_digits)} mT"""
        
        if unit == MagneticFieldUnits.Milligauss:
            return f"""{super()._truncate_fraction_digits(self.milligausses, fractional_digits)} mG"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: MagneticFieldUnits = MagneticFieldUnits.Tesla) -> str:
        """
        Get MagneticField unit abbreviation.
        Note! the default abbreviation for MagneticField is Tesla.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == MagneticFieldUnits.Tesla:
            return """T"""
        
        if unit_abbreviation == MagneticFieldUnits.Gauss:
            return """G"""
        
        if unit_abbreviation == MagneticFieldUnits.Nanotesla:
            return """nT"""
        
        if unit_abbreviation == MagneticFieldUnits.Microtesla:
            return """μT"""
        
        if unit_abbreviation == MagneticFieldUnits.Millitesla:
            return """mT"""
        
        if unit_abbreviation == MagneticFieldUnits.Milligauss:
            return """mG"""
        
from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class ElectricConductanceUnits(Enum):
        """
            ElectricConductanceUnits enumeration
        """
        
        Siemens = 'Siemens'
        """
            
        """
        
        Mho = 'Mho'
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
        
        Kilosiemens = 'Kilosiemens'
        """
            
        """
        
        Megasiemens = 'Megasiemens'
        """
            
        """
        
        Gigasiemens = 'Gigasiemens'
        """
            
        """
        
        Terasiemens = 'Terasiemens'
        """
            
        """
        
        Nanomho = 'Nanomho'
        """
            
        """
        
        Micromho = 'Micromho'
        """
            
        """
        
        Millimho = 'Millimho'
        """
            
        """
        
        Kilomho = 'Kilomho'
        """
            
        """
        
        Megamho = 'Megamho'
        """
            
        """
        
        Gigamho = 'Gigamho'
        """
            
        """
        
        Teramho = 'Teramho'
        """
            
        """
        

class ElectricConductanceDto:
    """
    A DTO representation of a ElectricConductance

    Attributes:
        value (float): The value of the ElectricConductance.
        unit (ElectricConductanceUnits): The specific unit that the ElectricConductance value is representing.
    """

    def __init__(self, value: float, unit: ElectricConductanceUnits):
        """
        Create a new DTO representation of a ElectricConductance

        Parameters:
            value (float): The value of the ElectricConductance.
            unit (ElectricConductanceUnits): The specific unit that the ElectricConductance value is representing.
        """
        self.value: float = value
        """
        The value of the ElectricConductance
        """
        self.unit: ElectricConductanceUnits = unit
        """
        The specific unit that the ElectricConductance value is representing
        """

    def to_json(self):
        """
        Get a ElectricConductance DTO JSON object representing the current unit.

        :return: JSON object represents ElectricConductance DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "Siemens"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of ElectricConductance DTO from a json representation.

        :param data: The ElectricConductance DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "Siemens"}
        :return: A new instance of ElectricConductanceDto.
        :rtype: ElectricConductanceDto
        """
        return ElectricConductanceDto(value=data["value"], unit=ElectricConductanceUnits(data["unit"]))


class ElectricConductance(AbstractMeasure):
    """
    The electrical conductance of an object is a measure of the ease with which an electric current passes. Along with susceptance, it is one of two elements of admittance. Its reciprocal quantity is electrical resistance.

    Args:
        value (float): The value.
        from_unit (ElectricConductanceUnits): The ElectricConductance unit to create from, The default unit is Siemens
    """
    def __init__(self, value: float, from_unit: ElectricConductanceUnits = ElectricConductanceUnits.Siemens):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__siemens = None
        
        self.__mhos = None
        
        self.__nanosiemens = None
        
        self.__microsiemens = None
        
        self.__millisiemens = None
        
        self.__kilosiemens = None
        
        self.__megasiemens = None
        
        self.__gigasiemens = None
        
        self.__terasiemens = None
        
        self.__nanomhos = None
        
        self.__micromhos = None
        
        self.__millimhos = None
        
        self.__kilomhos = None
        
        self.__megamhos = None
        
        self.__gigamhos = None
        
        self.__teramhos = None
        

    def convert(self, unit: ElectricConductanceUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: ElectricConductanceUnits = ElectricConductanceUnits.Siemens) -> ElectricConductanceDto:
        """
        Get a new instance of ElectricConductance DTO representing the current unit.

        :param hold_in_unit: The specific ElectricConductance unit to store the ElectricConductance value in the DTO representation.
        :type hold_in_unit: ElectricConductanceUnits
        :return: A new instance of ElectricConductanceDto.
        :rtype: ElectricConductanceDto
        """
        return ElectricConductanceDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: ElectricConductanceUnits = ElectricConductanceUnits.Siemens):
        """
        Get a ElectricConductance DTO JSON object representing the current unit.

        :param hold_in_unit: The specific ElectricConductance unit to store the ElectricConductance value in the DTO representation.
        :type hold_in_unit: ElectricConductanceUnits
        :return: JSON object represents ElectricConductance DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "Siemens"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(electric_conductance_dto: ElectricConductanceDto):
        """
        Obtain a new instance of ElectricConductance from a DTO unit object.

        :param electric_conductance_dto: The ElectricConductance DTO representation.
        :type electric_conductance_dto: ElectricConductanceDto
        :return: A new instance of ElectricConductance.
        :rtype: ElectricConductance
        """
        return ElectricConductance(electric_conductance_dto.value, electric_conductance_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of ElectricConductance from a DTO unit json representation.

        :param data: The ElectricConductance DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "Siemens"}
        :return: A new instance of ElectricConductance.
        :rtype: ElectricConductance
        """
        return ElectricConductance.from_dto(ElectricConductanceDto.from_json(data))

    def __convert_from_base(self, from_unit: ElectricConductanceUnits) -> float:
        value = self._value
        
        if from_unit == ElectricConductanceUnits.Siemens:
            return (value)
        
        if from_unit == ElectricConductanceUnits.Mho:
            return (value)
        
        if from_unit == ElectricConductanceUnits.Nanosiemens:
            return ((value) / 1e-09)
        
        if from_unit == ElectricConductanceUnits.Microsiemens:
            return ((value) / 1e-06)
        
        if from_unit == ElectricConductanceUnits.Millisiemens:
            return ((value) / 0.001)
        
        if from_unit == ElectricConductanceUnits.Kilosiemens:
            return ((value) / 1000.0)
        
        if from_unit == ElectricConductanceUnits.Megasiemens:
            return ((value) / 1000000.0)
        
        if from_unit == ElectricConductanceUnits.Gigasiemens:
            return ((value) / 1000000000.0)
        
        if from_unit == ElectricConductanceUnits.Terasiemens:
            return ((value) / 1000000000000.0)
        
        if from_unit == ElectricConductanceUnits.Nanomho:
            return ((value) / 1e-09)
        
        if from_unit == ElectricConductanceUnits.Micromho:
            return ((value) / 1e-06)
        
        if from_unit == ElectricConductanceUnits.Millimho:
            return ((value) / 0.001)
        
        if from_unit == ElectricConductanceUnits.Kilomho:
            return ((value) / 1000.0)
        
        if from_unit == ElectricConductanceUnits.Megamho:
            return ((value) / 1000000.0)
        
        if from_unit == ElectricConductanceUnits.Gigamho:
            return ((value) / 1000000000.0)
        
        if from_unit == ElectricConductanceUnits.Teramho:
            return ((value) / 1000000000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: ElectricConductanceUnits) -> float:
        
        if to_unit == ElectricConductanceUnits.Siemens:
            return (value)
        
        if to_unit == ElectricConductanceUnits.Mho:
            return (value)
        
        if to_unit == ElectricConductanceUnits.Nanosiemens:
            return ((value) * 1e-09)
        
        if to_unit == ElectricConductanceUnits.Microsiemens:
            return ((value) * 1e-06)
        
        if to_unit == ElectricConductanceUnits.Millisiemens:
            return ((value) * 0.001)
        
        if to_unit == ElectricConductanceUnits.Kilosiemens:
            return ((value) * 1000.0)
        
        if to_unit == ElectricConductanceUnits.Megasiemens:
            return ((value) * 1000000.0)
        
        if to_unit == ElectricConductanceUnits.Gigasiemens:
            return ((value) * 1000000000.0)
        
        if to_unit == ElectricConductanceUnits.Terasiemens:
            return ((value) * 1000000000000.0)
        
        if to_unit == ElectricConductanceUnits.Nanomho:
            return ((value) * 1e-09)
        
        if to_unit == ElectricConductanceUnits.Micromho:
            return ((value) * 1e-06)
        
        if to_unit == ElectricConductanceUnits.Millimho:
            return ((value) * 0.001)
        
        if to_unit == ElectricConductanceUnits.Kilomho:
            return ((value) * 1000.0)
        
        if to_unit == ElectricConductanceUnits.Megamho:
            return ((value) * 1000000.0)
        
        if to_unit == ElectricConductanceUnits.Gigamho:
            return ((value) * 1000000000.0)
        
        if to_unit == ElectricConductanceUnits.Teramho:
            return ((value) * 1000000000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_siemens(siemens: float):
        """
        Create a new instance of ElectricConductance from a value in siemens.

        

        :param meters: The ElectricConductance value in siemens.
        :type siemens: float
        :return: A new instance of ElectricConductance.
        :rtype: ElectricConductance
        """
        return ElectricConductance(siemens, ElectricConductanceUnits.Siemens)

    
    @staticmethod
    def from_mhos(mhos: float):
        """
        Create a new instance of ElectricConductance from a value in mhos.

        

        :param meters: The ElectricConductance value in mhos.
        :type mhos: float
        :return: A new instance of ElectricConductance.
        :rtype: ElectricConductance
        """
        return ElectricConductance(mhos, ElectricConductanceUnits.Mho)

    
    @staticmethod
    def from_nanosiemens(nanosiemens: float):
        """
        Create a new instance of ElectricConductance from a value in nanosiemens.

        

        :param meters: The ElectricConductance value in nanosiemens.
        :type nanosiemens: float
        :return: A new instance of ElectricConductance.
        :rtype: ElectricConductance
        """
        return ElectricConductance(nanosiemens, ElectricConductanceUnits.Nanosiemens)

    
    @staticmethod
    def from_microsiemens(microsiemens: float):
        """
        Create a new instance of ElectricConductance from a value in microsiemens.

        

        :param meters: The ElectricConductance value in microsiemens.
        :type microsiemens: float
        :return: A new instance of ElectricConductance.
        :rtype: ElectricConductance
        """
        return ElectricConductance(microsiemens, ElectricConductanceUnits.Microsiemens)

    
    @staticmethod
    def from_millisiemens(millisiemens: float):
        """
        Create a new instance of ElectricConductance from a value in millisiemens.

        

        :param meters: The ElectricConductance value in millisiemens.
        :type millisiemens: float
        :return: A new instance of ElectricConductance.
        :rtype: ElectricConductance
        """
        return ElectricConductance(millisiemens, ElectricConductanceUnits.Millisiemens)

    
    @staticmethod
    def from_kilosiemens(kilosiemens: float):
        """
        Create a new instance of ElectricConductance from a value in kilosiemens.

        

        :param meters: The ElectricConductance value in kilosiemens.
        :type kilosiemens: float
        :return: A new instance of ElectricConductance.
        :rtype: ElectricConductance
        """
        return ElectricConductance(kilosiemens, ElectricConductanceUnits.Kilosiemens)

    
    @staticmethod
    def from_megasiemens(megasiemens: float):
        """
        Create a new instance of ElectricConductance from a value in megasiemens.

        

        :param meters: The ElectricConductance value in megasiemens.
        :type megasiemens: float
        :return: A new instance of ElectricConductance.
        :rtype: ElectricConductance
        """
        return ElectricConductance(megasiemens, ElectricConductanceUnits.Megasiemens)

    
    @staticmethod
    def from_gigasiemens(gigasiemens: float):
        """
        Create a new instance of ElectricConductance from a value in gigasiemens.

        

        :param meters: The ElectricConductance value in gigasiemens.
        :type gigasiemens: float
        :return: A new instance of ElectricConductance.
        :rtype: ElectricConductance
        """
        return ElectricConductance(gigasiemens, ElectricConductanceUnits.Gigasiemens)

    
    @staticmethod
    def from_terasiemens(terasiemens: float):
        """
        Create a new instance of ElectricConductance from a value in terasiemens.

        

        :param meters: The ElectricConductance value in terasiemens.
        :type terasiemens: float
        :return: A new instance of ElectricConductance.
        :rtype: ElectricConductance
        """
        return ElectricConductance(terasiemens, ElectricConductanceUnits.Terasiemens)

    
    @staticmethod
    def from_nanomhos(nanomhos: float):
        """
        Create a new instance of ElectricConductance from a value in nanomhos.

        

        :param meters: The ElectricConductance value in nanomhos.
        :type nanomhos: float
        :return: A new instance of ElectricConductance.
        :rtype: ElectricConductance
        """
        return ElectricConductance(nanomhos, ElectricConductanceUnits.Nanomho)

    
    @staticmethod
    def from_micromhos(micromhos: float):
        """
        Create a new instance of ElectricConductance from a value in micromhos.

        

        :param meters: The ElectricConductance value in micromhos.
        :type micromhos: float
        :return: A new instance of ElectricConductance.
        :rtype: ElectricConductance
        """
        return ElectricConductance(micromhos, ElectricConductanceUnits.Micromho)

    
    @staticmethod
    def from_millimhos(millimhos: float):
        """
        Create a new instance of ElectricConductance from a value in millimhos.

        

        :param meters: The ElectricConductance value in millimhos.
        :type millimhos: float
        :return: A new instance of ElectricConductance.
        :rtype: ElectricConductance
        """
        return ElectricConductance(millimhos, ElectricConductanceUnits.Millimho)

    
    @staticmethod
    def from_kilomhos(kilomhos: float):
        """
        Create a new instance of ElectricConductance from a value in kilomhos.

        

        :param meters: The ElectricConductance value in kilomhos.
        :type kilomhos: float
        :return: A new instance of ElectricConductance.
        :rtype: ElectricConductance
        """
        return ElectricConductance(kilomhos, ElectricConductanceUnits.Kilomho)

    
    @staticmethod
    def from_megamhos(megamhos: float):
        """
        Create a new instance of ElectricConductance from a value in megamhos.

        

        :param meters: The ElectricConductance value in megamhos.
        :type megamhos: float
        :return: A new instance of ElectricConductance.
        :rtype: ElectricConductance
        """
        return ElectricConductance(megamhos, ElectricConductanceUnits.Megamho)

    
    @staticmethod
    def from_gigamhos(gigamhos: float):
        """
        Create a new instance of ElectricConductance from a value in gigamhos.

        

        :param meters: The ElectricConductance value in gigamhos.
        :type gigamhos: float
        :return: A new instance of ElectricConductance.
        :rtype: ElectricConductance
        """
        return ElectricConductance(gigamhos, ElectricConductanceUnits.Gigamho)

    
    @staticmethod
    def from_teramhos(teramhos: float):
        """
        Create a new instance of ElectricConductance from a value in teramhos.

        

        :param meters: The ElectricConductance value in teramhos.
        :type teramhos: float
        :return: A new instance of ElectricConductance.
        :rtype: ElectricConductance
        """
        return ElectricConductance(teramhos, ElectricConductanceUnits.Teramho)

    
    @property
    def siemens(self) -> float:
        """
        
        """
        if self.__siemens != None:
            return self.__siemens
        self.__siemens = self.__convert_from_base(ElectricConductanceUnits.Siemens)
        return self.__siemens

    
    @property
    def mhos(self) -> float:
        """
        
        """
        if self.__mhos != None:
            return self.__mhos
        self.__mhos = self.__convert_from_base(ElectricConductanceUnits.Mho)
        return self.__mhos

    
    @property
    def nanosiemens(self) -> float:
        """
        
        """
        if self.__nanosiemens != None:
            return self.__nanosiemens
        self.__nanosiemens = self.__convert_from_base(ElectricConductanceUnits.Nanosiemens)
        return self.__nanosiemens

    
    @property
    def microsiemens(self) -> float:
        """
        
        """
        if self.__microsiemens != None:
            return self.__microsiemens
        self.__microsiemens = self.__convert_from_base(ElectricConductanceUnits.Microsiemens)
        return self.__microsiemens

    
    @property
    def millisiemens(self) -> float:
        """
        
        """
        if self.__millisiemens != None:
            return self.__millisiemens
        self.__millisiemens = self.__convert_from_base(ElectricConductanceUnits.Millisiemens)
        return self.__millisiemens

    
    @property
    def kilosiemens(self) -> float:
        """
        
        """
        if self.__kilosiemens != None:
            return self.__kilosiemens
        self.__kilosiemens = self.__convert_from_base(ElectricConductanceUnits.Kilosiemens)
        return self.__kilosiemens

    
    @property
    def megasiemens(self) -> float:
        """
        
        """
        if self.__megasiemens != None:
            return self.__megasiemens
        self.__megasiemens = self.__convert_from_base(ElectricConductanceUnits.Megasiemens)
        return self.__megasiemens

    
    @property
    def gigasiemens(self) -> float:
        """
        
        """
        if self.__gigasiemens != None:
            return self.__gigasiemens
        self.__gigasiemens = self.__convert_from_base(ElectricConductanceUnits.Gigasiemens)
        return self.__gigasiemens

    
    @property
    def terasiemens(self) -> float:
        """
        
        """
        if self.__terasiemens != None:
            return self.__terasiemens
        self.__terasiemens = self.__convert_from_base(ElectricConductanceUnits.Terasiemens)
        return self.__terasiemens

    
    @property
    def nanomhos(self) -> float:
        """
        
        """
        if self.__nanomhos != None:
            return self.__nanomhos
        self.__nanomhos = self.__convert_from_base(ElectricConductanceUnits.Nanomho)
        return self.__nanomhos

    
    @property
    def micromhos(self) -> float:
        """
        
        """
        if self.__micromhos != None:
            return self.__micromhos
        self.__micromhos = self.__convert_from_base(ElectricConductanceUnits.Micromho)
        return self.__micromhos

    
    @property
    def millimhos(self) -> float:
        """
        
        """
        if self.__millimhos != None:
            return self.__millimhos
        self.__millimhos = self.__convert_from_base(ElectricConductanceUnits.Millimho)
        return self.__millimhos

    
    @property
    def kilomhos(self) -> float:
        """
        
        """
        if self.__kilomhos != None:
            return self.__kilomhos
        self.__kilomhos = self.__convert_from_base(ElectricConductanceUnits.Kilomho)
        return self.__kilomhos

    
    @property
    def megamhos(self) -> float:
        """
        
        """
        if self.__megamhos != None:
            return self.__megamhos
        self.__megamhos = self.__convert_from_base(ElectricConductanceUnits.Megamho)
        return self.__megamhos

    
    @property
    def gigamhos(self) -> float:
        """
        
        """
        if self.__gigamhos != None:
            return self.__gigamhos
        self.__gigamhos = self.__convert_from_base(ElectricConductanceUnits.Gigamho)
        return self.__gigamhos

    
    @property
    def teramhos(self) -> float:
        """
        
        """
        if self.__teramhos != None:
            return self.__teramhos
        self.__teramhos = self.__convert_from_base(ElectricConductanceUnits.Teramho)
        return self.__teramhos

    
    def to_string(self, unit: ElectricConductanceUnits = ElectricConductanceUnits.Siemens, fractional_digits: int = None) -> str:
        """
        Format the ElectricConductance to a string.
        
        Note: the default format for ElectricConductance is Siemens.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the ElectricConductance. Default is 'Siemens'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == ElectricConductanceUnits.Siemens:
            return f"""{super()._truncate_fraction_digits(self.siemens, fractional_digits)} S"""
        
        if unit == ElectricConductanceUnits.Mho:
            return f"""{super()._truncate_fraction_digits(self.mhos, fractional_digits)} ℧"""
        
        if unit == ElectricConductanceUnits.Nanosiemens:
            return f"""{super()._truncate_fraction_digits(self.nanosiemens, fractional_digits)} nS"""
        
        if unit == ElectricConductanceUnits.Microsiemens:
            return f"""{super()._truncate_fraction_digits(self.microsiemens, fractional_digits)} μS"""
        
        if unit == ElectricConductanceUnits.Millisiemens:
            return f"""{super()._truncate_fraction_digits(self.millisiemens, fractional_digits)} mS"""
        
        if unit == ElectricConductanceUnits.Kilosiemens:
            return f"""{super()._truncate_fraction_digits(self.kilosiemens, fractional_digits)} kS"""
        
        if unit == ElectricConductanceUnits.Megasiemens:
            return f"""{super()._truncate_fraction_digits(self.megasiemens, fractional_digits)} MS"""
        
        if unit == ElectricConductanceUnits.Gigasiemens:
            return f"""{super()._truncate_fraction_digits(self.gigasiemens, fractional_digits)} GS"""
        
        if unit == ElectricConductanceUnits.Terasiemens:
            return f"""{super()._truncate_fraction_digits(self.terasiemens, fractional_digits)} TS"""
        
        if unit == ElectricConductanceUnits.Nanomho:
            return f"""{super()._truncate_fraction_digits(self.nanomhos, fractional_digits)} n℧"""
        
        if unit == ElectricConductanceUnits.Micromho:
            return f"""{super()._truncate_fraction_digits(self.micromhos, fractional_digits)} μ℧"""
        
        if unit == ElectricConductanceUnits.Millimho:
            return f"""{super()._truncate_fraction_digits(self.millimhos, fractional_digits)} m℧"""
        
        if unit == ElectricConductanceUnits.Kilomho:
            return f"""{super()._truncate_fraction_digits(self.kilomhos, fractional_digits)} k℧"""
        
        if unit == ElectricConductanceUnits.Megamho:
            return f"""{super()._truncate_fraction_digits(self.megamhos, fractional_digits)} M℧"""
        
        if unit == ElectricConductanceUnits.Gigamho:
            return f"""{super()._truncate_fraction_digits(self.gigamhos, fractional_digits)} G℧"""
        
        if unit == ElectricConductanceUnits.Teramho:
            return f"""{super()._truncate_fraction_digits(self.teramhos, fractional_digits)} T℧"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: ElectricConductanceUnits = ElectricConductanceUnits.Siemens) -> str:
        """
        Get ElectricConductance unit abbreviation.
        Note! the default abbreviation for ElectricConductance is Siemens.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == ElectricConductanceUnits.Siemens:
            return """S"""
        
        if unit_abbreviation == ElectricConductanceUnits.Mho:
            return """℧"""
        
        if unit_abbreviation == ElectricConductanceUnits.Nanosiemens:
            return """nS"""
        
        if unit_abbreviation == ElectricConductanceUnits.Microsiemens:
            return """μS"""
        
        if unit_abbreviation == ElectricConductanceUnits.Millisiemens:
            return """mS"""
        
        if unit_abbreviation == ElectricConductanceUnits.Kilosiemens:
            return """kS"""
        
        if unit_abbreviation == ElectricConductanceUnits.Megasiemens:
            return """MS"""
        
        if unit_abbreviation == ElectricConductanceUnits.Gigasiemens:
            return """GS"""
        
        if unit_abbreviation == ElectricConductanceUnits.Terasiemens:
            return """TS"""
        
        if unit_abbreviation == ElectricConductanceUnits.Nanomho:
            return """n℧"""
        
        if unit_abbreviation == ElectricConductanceUnits.Micromho:
            return """μ℧"""
        
        if unit_abbreviation == ElectricConductanceUnits.Millimho:
            return """m℧"""
        
        if unit_abbreviation == ElectricConductanceUnits.Kilomho:
            return """k℧"""
        
        if unit_abbreviation == ElectricConductanceUnits.Megamho:
            return """M℧"""
        
        if unit_abbreviation == ElectricConductanceUnits.Gigamho:
            return """G℧"""
        
        if unit_abbreviation == ElectricConductanceUnits.Teramho:
            return """T℧"""
        
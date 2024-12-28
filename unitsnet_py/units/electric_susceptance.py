from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class ElectricSusceptanceUnits(Enum):
        """
            ElectricSusceptanceUnits enumeration
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
        

class ElectricSusceptanceDto:
    """
    A DTO representation of a ElectricSusceptance

    Attributes:
        value (float): The value of the ElectricSusceptance.
        unit (ElectricSusceptanceUnits): The specific unit that the ElectricSusceptance value is representing.
    """

    def __init__(self, value: float, unit: ElectricSusceptanceUnits):
        """
        Create a new DTO representation of a ElectricSusceptance

        Parameters:
            value (float): The value of the ElectricSusceptance.
            unit (ElectricSusceptanceUnits): The specific unit that the ElectricSusceptance value is representing.
        """
        self.value: float = value
        """
        The value of the ElectricSusceptance
        """
        self.unit: ElectricSusceptanceUnits = unit
        """
        The specific unit that the ElectricSusceptance value is representing
        """

    def to_json(self):
        """
        Get a ElectricSusceptance DTO JSON object representing the current unit.

        :return: JSON object represents ElectricSusceptance DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "Siemens"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of ElectricSusceptance DTO from a json representation.

        :param data: The ElectricSusceptance DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "Siemens"}
        :return: A new instance of ElectricSusceptanceDto.
        :rtype: ElectricSusceptanceDto
        """
        return ElectricSusceptanceDto(value=data["value"], unit=ElectricSusceptanceUnits(data["unit"]))


class ElectricSusceptance(AbstractMeasure):
    """
    Electrical susceptance is the imaginary part of admittance, where the real part is conductance.

    Args:
        value (float): The value.
        from_unit (ElectricSusceptanceUnits): The ElectricSusceptance unit to create from, The default unit is Siemens
    """
    def __init__(self, value: float, from_unit: ElectricSusceptanceUnits = ElectricSusceptanceUnits.Siemens):
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
        

    def convert(self, unit: ElectricSusceptanceUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: ElectricSusceptanceUnits = ElectricSusceptanceUnits.Siemens) -> ElectricSusceptanceDto:
        """
        Get a new instance of ElectricSusceptance DTO representing the current unit.

        :param hold_in_unit: The specific ElectricSusceptance unit to store the ElectricSusceptance value in the DTO representation.
        :type hold_in_unit: ElectricSusceptanceUnits
        :return: A new instance of ElectricSusceptanceDto.
        :rtype: ElectricSusceptanceDto
        """
        return ElectricSusceptanceDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: ElectricSusceptanceUnits = ElectricSusceptanceUnits.Siemens):
        """
        Get a ElectricSusceptance DTO JSON object representing the current unit.

        :param hold_in_unit: The specific ElectricSusceptance unit to store the ElectricSusceptance value in the DTO representation.
        :type hold_in_unit: ElectricSusceptanceUnits
        :return: JSON object represents ElectricSusceptance DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "Siemens"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(electric_susceptance_dto: ElectricSusceptanceDto):
        """
        Obtain a new instance of ElectricSusceptance from a DTO unit object.

        :param electric_susceptance_dto: The ElectricSusceptance DTO representation.
        :type electric_susceptance_dto: ElectricSusceptanceDto
        :return: A new instance of ElectricSusceptance.
        :rtype: ElectricSusceptance
        """
        return ElectricSusceptance(electric_susceptance_dto.value, electric_susceptance_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of ElectricSusceptance from a DTO unit json representation.

        :param data: The ElectricSusceptance DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "Siemens"}
        :return: A new instance of ElectricSusceptance.
        :rtype: ElectricSusceptance
        """
        return ElectricSusceptance.from_dto(ElectricSusceptanceDto.from_json(data))

    def __convert_from_base(self, from_unit: ElectricSusceptanceUnits) -> float:
        value = self._value
        
        if from_unit == ElectricSusceptanceUnits.Siemens:
            return (value)
        
        if from_unit == ElectricSusceptanceUnits.Mho:
            return (value)
        
        if from_unit == ElectricSusceptanceUnits.Nanosiemens:
            return ((value) / 1e-09)
        
        if from_unit == ElectricSusceptanceUnits.Microsiemens:
            return ((value) / 1e-06)
        
        if from_unit == ElectricSusceptanceUnits.Millisiemens:
            return ((value) / 0.001)
        
        if from_unit == ElectricSusceptanceUnits.Kilosiemens:
            return ((value) / 1000.0)
        
        if from_unit == ElectricSusceptanceUnits.Megasiemens:
            return ((value) / 1000000.0)
        
        if from_unit == ElectricSusceptanceUnits.Gigasiemens:
            return ((value) / 1000000000.0)
        
        if from_unit == ElectricSusceptanceUnits.Terasiemens:
            return ((value) / 1000000000000.0)
        
        if from_unit == ElectricSusceptanceUnits.Nanomho:
            return ((value) / 1e-09)
        
        if from_unit == ElectricSusceptanceUnits.Micromho:
            return ((value) / 1e-06)
        
        if from_unit == ElectricSusceptanceUnits.Millimho:
            return ((value) / 0.001)
        
        if from_unit == ElectricSusceptanceUnits.Kilomho:
            return ((value) / 1000.0)
        
        if from_unit == ElectricSusceptanceUnits.Megamho:
            return ((value) / 1000000.0)
        
        if from_unit == ElectricSusceptanceUnits.Gigamho:
            return ((value) / 1000000000.0)
        
        if from_unit == ElectricSusceptanceUnits.Teramho:
            return ((value) / 1000000000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: ElectricSusceptanceUnits) -> float:
        
        if to_unit == ElectricSusceptanceUnits.Siemens:
            return (value)
        
        if to_unit == ElectricSusceptanceUnits.Mho:
            return (value)
        
        if to_unit == ElectricSusceptanceUnits.Nanosiemens:
            return ((value) * 1e-09)
        
        if to_unit == ElectricSusceptanceUnits.Microsiemens:
            return ((value) * 1e-06)
        
        if to_unit == ElectricSusceptanceUnits.Millisiemens:
            return ((value) * 0.001)
        
        if to_unit == ElectricSusceptanceUnits.Kilosiemens:
            return ((value) * 1000.0)
        
        if to_unit == ElectricSusceptanceUnits.Megasiemens:
            return ((value) * 1000000.0)
        
        if to_unit == ElectricSusceptanceUnits.Gigasiemens:
            return ((value) * 1000000000.0)
        
        if to_unit == ElectricSusceptanceUnits.Terasiemens:
            return ((value) * 1000000000000.0)
        
        if to_unit == ElectricSusceptanceUnits.Nanomho:
            return ((value) * 1e-09)
        
        if to_unit == ElectricSusceptanceUnits.Micromho:
            return ((value) * 1e-06)
        
        if to_unit == ElectricSusceptanceUnits.Millimho:
            return ((value) * 0.001)
        
        if to_unit == ElectricSusceptanceUnits.Kilomho:
            return ((value) * 1000.0)
        
        if to_unit == ElectricSusceptanceUnits.Megamho:
            return ((value) * 1000000.0)
        
        if to_unit == ElectricSusceptanceUnits.Gigamho:
            return ((value) * 1000000000.0)
        
        if to_unit == ElectricSusceptanceUnits.Teramho:
            return ((value) * 1000000000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_siemens(siemens: float):
        """
        Create a new instance of ElectricSusceptance from a value in siemens.

        

        :param meters: The ElectricSusceptance value in siemens.
        :type siemens: float
        :return: A new instance of ElectricSusceptance.
        :rtype: ElectricSusceptance
        """
        return ElectricSusceptance(siemens, ElectricSusceptanceUnits.Siemens)

    
    @staticmethod
    def from_mhos(mhos: float):
        """
        Create a new instance of ElectricSusceptance from a value in mhos.

        

        :param meters: The ElectricSusceptance value in mhos.
        :type mhos: float
        :return: A new instance of ElectricSusceptance.
        :rtype: ElectricSusceptance
        """
        return ElectricSusceptance(mhos, ElectricSusceptanceUnits.Mho)

    
    @staticmethod
    def from_nanosiemens(nanosiemens: float):
        """
        Create a new instance of ElectricSusceptance from a value in nanosiemens.

        

        :param meters: The ElectricSusceptance value in nanosiemens.
        :type nanosiemens: float
        :return: A new instance of ElectricSusceptance.
        :rtype: ElectricSusceptance
        """
        return ElectricSusceptance(nanosiemens, ElectricSusceptanceUnits.Nanosiemens)

    
    @staticmethod
    def from_microsiemens(microsiemens: float):
        """
        Create a new instance of ElectricSusceptance from a value in microsiemens.

        

        :param meters: The ElectricSusceptance value in microsiemens.
        :type microsiemens: float
        :return: A new instance of ElectricSusceptance.
        :rtype: ElectricSusceptance
        """
        return ElectricSusceptance(microsiemens, ElectricSusceptanceUnits.Microsiemens)

    
    @staticmethod
    def from_millisiemens(millisiemens: float):
        """
        Create a new instance of ElectricSusceptance from a value in millisiemens.

        

        :param meters: The ElectricSusceptance value in millisiemens.
        :type millisiemens: float
        :return: A new instance of ElectricSusceptance.
        :rtype: ElectricSusceptance
        """
        return ElectricSusceptance(millisiemens, ElectricSusceptanceUnits.Millisiemens)

    
    @staticmethod
    def from_kilosiemens(kilosiemens: float):
        """
        Create a new instance of ElectricSusceptance from a value in kilosiemens.

        

        :param meters: The ElectricSusceptance value in kilosiemens.
        :type kilosiemens: float
        :return: A new instance of ElectricSusceptance.
        :rtype: ElectricSusceptance
        """
        return ElectricSusceptance(kilosiemens, ElectricSusceptanceUnits.Kilosiemens)

    
    @staticmethod
    def from_megasiemens(megasiemens: float):
        """
        Create a new instance of ElectricSusceptance from a value in megasiemens.

        

        :param meters: The ElectricSusceptance value in megasiemens.
        :type megasiemens: float
        :return: A new instance of ElectricSusceptance.
        :rtype: ElectricSusceptance
        """
        return ElectricSusceptance(megasiemens, ElectricSusceptanceUnits.Megasiemens)

    
    @staticmethod
    def from_gigasiemens(gigasiemens: float):
        """
        Create a new instance of ElectricSusceptance from a value in gigasiemens.

        

        :param meters: The ElectricSusceptance value in gigasiemens.
        :type gigasiemens: float
        :return: A new instance of ElectricSusceptance.
        :rtype: ElectricSusceptance
        """
        return ElectricSusceptance(gigasiemens, ElectricSusceptanceUnits.Gigasiemens)

    
    @staticmethod
    def from_terasiemens(terasiemens: float):
        """
        Create a new instance of ElectricSusceptance from a value in terasiemens.

        

        :param meters: The ElectricSusceptance value in terasiemens.
        :type terasiemens: float
        :return: A new instance of ElectricSusceptance.
        :rtype: ElectricSusceptance
        """
        return ElectricSusceptance(terasiemens, ElectricSusceptanceUnits.Terasiemens)

    
    @staticmethod
    def from_nanomhos(nanomhos: float):
        """
        Create a new instance of ElectricSusceptance from a value in nanomhos.

        

        :param meters: The ElectricSusceptance value in nanomhos.
        :type nanomhos: float
        :return: A new instance of ElectricSusceptance.
        :rtype: ElectricSusceptance
        """
        return ElectricSusceptance(nanomhos, ElectricSusceptanceUnits.Nanomho)

    
    @staticmethod
    def from_micromhos(micromhos: float):
        """
        Create a new instance of ElectricSusceptance from a value in micromhos.

        

        :param meters: The ElectricSusceptance value in micromhos.
        :type micromhos: float
        :return: A new instance of ElectricSusceptance.
        :rtype: ElectricSusceptance
        """
        return ElectricSusceptance(micromhos, ElectricSusceptanceUnits.Micromho)

    
    @staticmethod
    def from_millimhos(millimhos: float):
        """
        Create a new instance of ElectricSusceptance from a value in millimhos.

        

        :param meters: The ElectricSusceptance value in millimhos.
        :type millimhos: float
        :return: A new instance of ElectricSusceptance.
        :rtype: ElectricSusceptance
        """
        return ElectricSusceptance(millimhos, ElectricSusceptanceUnits.Millimho)

    
    @staticmethod
    def from_kilomhos(kilomhos: float):
        """
        Create a new instance of ElectricSusceptance from a value in kilomhos.

        

        :param meters: The ElectricSusceptance value in kilomhos.
        :type kilomhos: float
        :return: A new instance of ElectricSusceptance.
        :rtype: ElectricSusceptance
        """
        return ElectricSusceptance(kilomhos, ElectricSusceptanceUnits.Kilomho)

    
    @staticmethod
    def from_megamhos(megamhos: float):
        """
        Create a new instance of ElectricSusceptance from a value in megamhos.

        

        :param meters: The ElectricSusceptance value in megamhos.
        :type megamhos: float
        :return: A new instance of ElectricSusceptance.
        :rtype: ElectricSusceptance
        """
        return ElectricSusceptance(megamhos, ElectricSusceptanceUnits.Megamho)

    
    @staticmethod
    def from_gigamhos(gigamhos: float):
        """
        Create a new instance of ElectricSusceptance from a value in gigamhos.

        

        :param meters: The ElectricSusceptance value in gigamhos.
        :type gigamhos: float
        :return: A new instance of ElectricSusceptance.
        :rtype: ElectricSusceptance
        """
        return ElectricSusceptance(gigamhos, ElectricSusceptanceUnits.Gigamho)

    
    @staticmethod
    def from_teramhos(teramhos: float):
        """
        Create a new instance of ElectricSusceptance from a value in teramhos.

        

        :param meters: The ElectricSusceptance value in teramhos.
        :type teramhos: float
        :return: A new instance of ElectricSusceptance.
        :rtype: ElectricSusceptance
        """
        return ElectricSusceptance(teramhos, ElectricSusceptanceUnits.Teramho)

    
    @property
    def siemens(self) -> float:
        """
        
        """
        if self.__siemens != None:
            return self.__siemens
        self.__siemens = self.__convert_from_base(ElectricSusceptanceUnits.Siemens)
        return self.__siemens

    
    @property
    def mhos(self) -> float:
        """
        
        """
        if self.__mhos != None:
            return self.__mhos
        self.__mhos = self.__convert_from_base(ElectricSusceptanceUnits.Mho)
        return self.__mhos

    
    @property
    def nanosiemens(self) -> float:
        """
        
        """
        if self.__nanosiemens != None:
            return self.__nanosiemens
        self.__nanosiemens = self.__convert_from_base(ElectricSusceptanceUnits.Nanosiemens)
        return self.__nanosiemens

    
    @property
    def microsiemens(self) -> float:
        """
        
        """
        if self.__microsiemens != None:
            return self.__microsiemens
        self.__microsiemens = self.__convert_from_base(ElectricSusceptanceUnits.Microsiemens)
        return self.__microsiemens

    
    @property
    def millisiemens(self) -> float:
        """
        
        """
        if self.__millisiemens != None:
            return self.__millisiemens
        self.__millisiemens = self.__convert_from_base(ElectricSusceptanceUnits.Millisiemens)
        return self.__millisiemens

    
    @property
    def kilosiemens(self) -> float:
        """
        
        """
        if self.__kilosiemens != None:
            return self.__kilosiemens
        self.__kilosiemens = self.__convert_from_base(ElectricSusceptanceUnits.Kilosiemens)
        return self.__kilosiemens

    
    @property
    def megasiemens(self) -> float:
        """
        
        """
        if self.__megasiemens != None:
            return self.__megasiemens
        self.__megasiemens = self.__convert_from_base(ElectricSusceptanceUnits.Megasiemens)
        return self.__megasiemens

    
    @property
    def gigasiemens(self) -> float:
        """
        
        """
        if self.__gigasiemens != None:
            return self.__gigasiemens
        self.__gigasiemens = self.__convert_from_base(ElectricSusceptanceUnits.Gigasiemens)
        return self.__gigasiemens

    
    @property
    def terasiemens(self) -> float:
        """
        
        """
        if self.__terasiemens != None:
            return self.__terasiemens
        self.__terasiemens = self.__convert_from_base(ElectricSusceptanceUnits.Terasiemens)
        return self.__terasiemens

    
    @property
    def nanomhos(self) -> float:
        """
        
        """
        if self.__nanomhos != None:
            return self.__nanomhos
        self.__nanomhos = self.__convert_from_base(ElectricSusceptanceUnits.Nanomho)
        return self.__nanomhos

    
    @property
    def micromhos(self) -> float:
        """
        
        """
        if self.__micromhos != None:
            return self.__micromhos
        self.__micromhos = self.__convert_from_base(ElectricSusceptanceUnits.Micromho)
        return self.__micromhos

    
    @property
    def millimhos(self) -> float:
        """
        
        """
        if self.__millimhos != None:
            return self.__millimhos
        self.__millimhos = self.__convert_from_base(ElectricSusceptanceUnits.Millimho)
        return self.__millimhos

    
    @property
    def kilomhos(self) -> float:
        """
        
        """
        if self.__kilomhos != None:
            return self.__kilomhos
        self.__kilomhos = self.__convert_from_base(ElectricSusceptanceUnits.Kilomho)
        return self.__kilomhos

    
    @property
    def megamhos(self) -> float:
        """
        
        """
        if self.__megamhos != None:
            return self.__megamhos
        self.__megamhos = self.__convert_from_base(ElectricSusceptanceUnits.Megamho)
        return self.__megamhos

    
    @property
    def gigamhos(self) -> float:
        """
        
        """
        if self.__gigamhos != None:
            return self.__gigamhos
        self.__gigamhos = self.__convert_from_base(ElectricSusceptanceUnits.Gigamho)
        return self.__gigamhos

    
    @property
    def teramhos(self) -> float:
        """
        
        """
        if self.__teramhos != None:
            return self.__teramhos
        self.__teramhos = self.__convert_from_base(ElectricSusceptanceUnits.Teramho)
        return self.__teramhos

    
    def to_string(self, unit: ElectricSusceptanceUnits = ElectricSusceptanceUnits.Siemens, fractional_digits: int = None) -> str:
        """
        Format the ElectricSusceptance to a string.
        
        Note: the default format for ElectricSusceptance is Siemens.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the ElectricSusceptance. Default is 'Siemens'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == ElectricSusceptanceUnits.Siemens:
            return f"""{super()._truncate_fraction_digits(self.siemens, fractional_digits)} S"""
        
        if unit == ElectricSusceptanceUnits.Mho:
            return f"""{super()._truncate_fraction_digits(self.mhos, fractional_digits)} ℧"""
        
        if unit == ElectricSusceptanceUnits.Nanosiemens:
            return f"""{super()._truncate_fraction_digits(self.nanosiemens, fractional_digits)} nS"""
        
        if unit == ElectricSusceptanceUnits.Microsiemens:
            return f"""{super()._truncate_fraction_digits(self.microsiemens, fractional_digits)} μS"""
        
        if unit == ElectricSusceptanceUnits.Millisiemens:
            return f"""{super()._truncate_fraction_digits(self.millisiemens, fractional_digits)} mS"""
        
        if unit == ElectricSusceptanceUnits.Kilosiemens:
            return f"""{super()._truncate_fraction_digits(self.kilosiemens, fractional_digits)} kS"""
        
        if unit == ElectricSusceptanceUnits.Megasiemens:
            return f"""{super()._truncate_fraction_digits(self.megasiemens, fractional_digits)} MS"""
        
        if unit == ElectricSusceptanceUnits.Gigasiemens:
            return f"""{super()._truncate_fraction_digits(self.gigasiemens, fractional_digits)} GS"""
        
        if unit == ElectricSusceptanceUnits.Terasiemens:
            return f"""{super()._truncate_fraction_digits(self.terasiemens, fractional_digits)} TS"""
        
        if unit == ElectricSusceptanceUnits.Nanomho:
            return f"""{super()._truncate_fraction_digits(self.nanomhos, fractional_digits)} n℧"""
        
        if unit == ElectricSusceptanceUnits.Micromho:
            return f"""{super()._truncate_fraction_digits(self.micromhos, fractional_digits)} μ℧"""
        
        if unit == ElectricSusceptanceUnits.Millimho:
            return f"""{super()._truncate_fraction_digits(self.millimhos, fractional_digits)} m℧"""
        
        if unit == ElectricSusceptanceUnits.Kilomho:
            return f"""{super()._truncate_fraction_digits(self.kilomhos, fractional_digits)} k℧"""
        
        if unit == ElectricSusceptanceUnits.Megamho:
            return f"""{super()._truncate_fraction_digits(self.megamhos, fractional_digits)} M℧"""
        
        if unit == ElectricSusceptanceUnits.Gigamho:
            return f"""{super()._truncate_fraction_digits(self.gigamhos, fractional_digits)} G℧"""
        
        if unit == ElectricSusceptanceUnits.Teramho:
            return f"""{super()._truncate_fraction_digits(self.teramhos, fractional_digits)} T℧"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: ElectricSusceptanceUnits = ElectricSusceptanceUnits.Siemens) -> str:
        """
        Get ElectricSusceptance unit abbreviation.
        Note! the default abbreviation for ElectricSusceptance is Siemens.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == ElectricSusceptanceUnits.Siemens:
            return """S"""
        
        if unit_abbreviation == ElectricSusceptanceUnits.Mho:
            return """℧"""
        
        if unit_abbreviation == ElectricSusceptanceUnits.Nanosiemens:
            return """nS"""
        
        if unit_abbreviation == ElectricSusceptanceUnits.Microsiemens:
            return """μS"""
        
        if unit_abbreviation == ElectricSusceptanceUnits.Millisiemens:
            return """mS"""
        
        if unit_abbreviation == ElectricSusceptanceUnits.Kilosiemens:
            return """kS"""
        
        if unit_abbreviation == ElectricSusceptanceUnits.Megasiemens:
            return """MS"""
        
        if unit_abbreviation == ElectricSusceptanceUnits.Gigasiemens:
            return """GS"""
        
        if unit_abbreviation == ElectricSusceptanceUnits.Terasiemens:
            return """TS"""
        
        if unit_abbreviation == ElectricSusceptanceUnits.Nanomho:
            return """n℧"""
        
        if unit_abbreviation == ElectricSusceptanceUnits.Micromho:
            return """μ℧"""
        
        if unit_abbreviation == ElectricSusceptanceUnits.Millimho:
            return """m℧"""
        
        if unit_abbreviation == ElectricSusceptanceUnits.Kilomho:
            return """k℧"""
        
        if unit_abbreviation == ElectricSusceptanceUnits.Megamho:
            return """M℧"""
        
        if unit_abbreviation == ElectricSusceptanceUnits.Gigamho:
            return """G℧"""
        
        if unit_abbreviation == ElectricSusceptanceUnits.Teramho:
            return """T℧"""
        
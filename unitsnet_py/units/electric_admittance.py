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
    Electric admittance is a measure of how easily a circuit or device will allow a current to flow by the combined effect of conductance and susceptance in a circuit. It is defined as the inverse of impedance. The SI unit of admittance is the siemens (symbol S).

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
        
        if from_unit == ElectricAdmittanceUnits.Mho:
            return (value)
        
        if from_unit == ElectricAdmittanceUnits.Nanosiemens:
            return ((value) / 1e-09)
        
        if from_unit == ElectricAdmittanceUnits.Microsiemens:
            return ((value) / 1e-06)
        
        if from_unit == ElectricAdmittanceUnits.Millisiemens:
            return ((value) / 0.001)
        
        if from_unit == ElectricAdmittanceUnits.Kilosiemens:
            return ((value) / 1000.0)
        
        if from_unit == ElectricAdmittanceUnits.Megasiemens:
            return ((value) / 1000000.0)
        
        if from_unit == ElectricAdmittanceUnits.Gigasiemens:
            return ((value) / 1000000000.0)
        
        if from_unit == ElectricAdmittanceUnits.Terasiemens:
            return ((value) / 1000000000000.0)
        
        if from_unit == ElectricAdmittanceUnits.Nanomho:
            return ((value) / 1e-09)
        
        if from_unit == ElectricAdmittanceUnits.Micromho:
            return ((value) / 1e-06)
        
        if from_unit == ElectricAdmittanceUnits.Millimho:
            return ((value) / 0.001)
        
        if from_unit == ElectricAdmittanceUnits.Kilomho:
            return ((value) / 1000.0)
        
        if from_unit == ElectricAdmittanceUnits.Megamho:
            return ((value) / 1000000.0)
        
        if from_unit == ElectricAdmittanceUnits.Gigamho:
            return ((value) / 1000000000.0)
        
        if from_unit == ElectricAdmittanceUnits.Teramho:
            return ((value) / 1000000000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: ElectricAdmittanceUnits) -> float:
        
        if to_unit == ElectricAdmittanceUnits.Siemens:
            return (value)
        
        if to_unit == ElectricAdmittanceUnits.Mho:
            return (value)
        
        if to_unit == ElectricAdmittanceUnits.Nanosiemens:
            return ((value) * 1e-09)
        
        if to_unit == ElectricAdmittanceUnits.Microsiemens:
            return ((value) * 1e-06)
        
        if to_unit == ElectricAdmittanceUnits.Millisiemens:
            return ((value) * 0.001)
        
        if to_unit == ElectricAdmittanceUnits.Kilosiemens:
            return ((value) * 1000.0)
        
        if to_unit == ElectricAdmittanceUnits.Megasiemens:
            return ((value) * 1000000.0)
        
        if to_unit == ElectricAdmittanceUnits.Gigasiemens:
            return ((value) * 1000000000.0)
        
        if to_unit == ElectricAdmittanceUnits.Terasiemens:
            return ((value) * 1000000000000.0)
        
        if to_unit == ElectricAdmittanceUnits.Nanomho:
            return ((value) * 1e-09)
        
        if to_unit == ElectricAdmittanceUnits.Micromho:
            return ((value) * 1e-06)
        
        if to_unit == ElectricAdmittanceUnits.Millimho:
            return ((value) * 0.001)
        
        if to_unit == ElectricAdmittanceUnits.Kilomho:
            return ((value) * 1000.0)
        
        if to_unit == ElectricAdmittanceUnits.Megamho:
            return ((value) * 1000000.0)
        
        if to_unit == ElectricAdmittanceUnits.Gigamho:
            return ((value) * 1000000000.0)
        
        if to_unit == ElectricAdmittanceUnits.Teramho:
            return ((value) * 1000000000000.0)
        
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
    def from_mhos(mhos: float):
        """
        Create a new instance of ElectricAdmittance from a value in mhos.

        

        :param meters: The ElectricAdmittance value in mhos.
        :type mhos: float
        :return: A new instance of ElectricAdmittance.
        :rtype: ElectricAdmittance
        """
        return ElectricAdmittance(mhos, ElectricAdmittanceUnits.Mho)

    
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

    
    @staticmethod
    def from_kilosiemens(kilosiemens: float):
        """
        Create a new instance of ElectricAdmittance from a value in kilosiemens.

        

        :param meters: The ElectricAdmittance value in kilosiemens.
        :type kilosiemens: float
        :return: A new instance of ElectricAdmittance.
        :rtype: ElectricAdmittance
        """
        return ElectricAdmittance(kilosiemens, ElectricAdmittanceUnits.Kilosiemens)

    
    @staticmethod
    def from_megasiemens(megasiemens: float):
        """
        Create a new instance of ElectricAdmittance from a value in megasiemens.

        

        :param meters: The ElectricAdmittance value in megasiemens.
        :type megasiemens: float
        :return: A new instance of ElectricAdmittance.
        :rtype: ElectricAdmittance
        """
        return ElectricAdmittance(megasiemens, ElectricAdmittanceUnits.Megasiemens)

    
    @staticmethod
    def from_gigasiemens(gigasiemens: float):
        """
        Create a new instance of ElectricAdmittance from a value in gigasiemens.

        

        :param meters: The ElectricAdmittance value in gigasiemens.
        :type gigasiemens: float
        :return: A new instance of ElectricAdmittance.
        :rtype: ElectricAdmittance
        """
        return ElectricAdmittance(gigasiemens, ElectricAdmittanceUnits.Gigasiemens)

    
    @staticmethod
    def from_terasiemens(terasiemens: float):
        """
        Create a new instance of ElectricAdmittance from a value in terasiemens.

        

        :param meters: The ElectricAdmittance value in terasiemens.
        :type terasiemens: float
        :return: A new instance of ElectricAdmittance.
        :rtype: ElectricAdmittance
        """
        return ElectricAdmittance(terasiemens, ElectricAdmittanceUnits.Terasiemens)

    
    @staticmethod
    def from_nanomhos(nanomhos: float):
        """
        Create a new instance of ElectricAdmittance from a value in nanomhos.

        

        :param meters: The ElectricAdmittance value in nanomhos.
        :type nanomhos: float
        :return: A new instance of ElectricAdmittance.
        :rtype: ElectricAdmittance
        """
        return ElectricAdmittance(nanomhos, ElectricAdmittanceUnits.Nanomho)

    
    @staticmethod
    def from_micromhos(micromhos: float):
        """
        Create a new instance of ElectricAdmittance from a value in micromhos.

        

        :param meters: The ElectricAdmittance value in micromhos.
        :type micromhos: float
        :return: A new instance of ElectricAdmittance.
        :rtype: ElectricAdmittance
        """
        return ElectricAdmittance(micromhos, ElectricAdmittanceUnits.Micromho)

    
    @staticmethod
    def from_millimhos(millimhos: float):
        """
        Create a new instance of ElectricAdmittance from a value in millimhos.

        

        :param meters: The ElectricAdmittance value in millimhos.
        :type millimhos: float
        :return: A new instance of ElectricAdmittance.
        :rtype: ElectricAdmittance
        """
        return ElectricAdmittance(millimhos, ElectricAdmittanceUnits.Millimho)

    
    @staticmethod
    def from_kilomhos(kilomhos: float):
        """
        Create a new instance of ElectricAdmittance from a value in kilomhos.

        

        :param meters: The ElectricAdmittance value in kilomhos.
        :type kilomhos: float
        :return: A new instance of ElectricAdmittance.
        :rtype: ElectricAdmittance
        """
        return ElectricAdmittance(kilomhos, ElectricAdmittanceUnits.Kilomho)

    
    @staticmethod
    def from_megamhos(megamhos: float):
        """
        Create a new instance of ElectricAdmittance from a value in megamhos.

        

        :param meters: The ElectricAdmittance value in megamhos.
        :type megamhos: float
        :return: A new instance of ElectricAdmittance.
        :rtype: ElectricAdmittance
        """
        return ElectricAdmittance(megamhos, ElectricAdmittanceUnits.Megamho)

    
    @staticmethod
    def from_gigamhos(gigamhos: float):
        """
        Create a new instance of ElectricAdmittance from a value in gigamhos.

        

        :param meters: The ElectricAdmittance value in gigamhos.
        :type gigamhos: float
        :return: A new instance of ElectricAdmittance.
        :rtype: ElectricAdmittance
        """
        return ElectricAdmittance(gigamhos, ElectricAdmittanceUnits.Gigamho)

    
    @staticmethod
    def from_teramhos(teramhos: float):
        """
        Create a new instance of ElectricAdmittance from a value in teramhos.

        

        :param meters: The ElectricAdmittance value in teramhos.
        :type teramhos: float
        :return: A new instance of ElectricAdmittance.
        :rtype: ElectricAdmittance
        """
        return ElectricAdmittance(teramhos, ElectricAdmittanceUnits.Teramho)

    
    @property
    def siemens(self) -> float:
        """
        
        """
        if self.__siemens != None:
            return self.__siemens
        self.__siemens = self.__convert_from_base(ElectricAdmittanceUnits.Siemens)
        return self.__siemens

    
    @property
    def mhos(self) -> float:
        """
        
        """
        if self.__mhos != None:
            return self.__mhos
        self.__mhos = self.__convert_from_base(ElectricAdmittanceUnits.Mho)
        return self.__mhos

    
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

    
    @property
    def kilosiemens(self) -> float:
        """
        
        """
        if self.__kilosiemens != None:
            return self.__kilosiemens
        self.__kilosiemens = self.__convert_from_base(ElectricAdmittanceUnits.Kilosiemens)
        return self.__kilosiemens

    
    @property
    def megasiemens(self) -> float:
        """
        
        """
        if self.__megasiemens != None:
            return self.__megasiemens
        self.__megasiemens = self.__convert_from_base(ElectricAdmittanceUnits.Megasiemens)
        return self.__megasiemens

    
    @property
    def gigasiemens(self) -> float:
        """
        
        """
        if self.__gigasiemens != None:
            return self.__gigasiemens
        self.__gigasiemens = self.__convert_from_base(ElectricAdmittanceUnits.Gigasiemens)
        return self.__gigasiemens

    
    @property
    def terasiemens(self) -> float:
        """
        
        """
        if self.__terasiemens != None:
            return self.__terasiemens
        self.__terasiemens = self.__convert_from_base(ElectricAdmittanceUnits.Terasiemens)
        return self.__terasiemens

    
    @property
    def nanomhos(self) -> float:
        """
        
        """
        if self.__nanomhos != None:
            return self.__nanomhos
        self.__nanomhos = self.__convert_from_base(ElectricAdmittanceUnits.Nanomho)
        return self.__nanomhos

    
    @property
    def micromhos(self) -> float:
        """
        
        """
        if self.__micromhos != None:
            return self.__micromhos
        self.__micromhos = self.__convert_from_base(ElectricAdmittanceUnits.Micromho)
        return self.__micromhos

    
    @property
    def millimhos(self) -> float:
        """
        
        """
        if self.__millimhos != None:
            return self.__millimhos
        self.__millimhos = self.__convert_from_base(ElectricAdmittanceUnits.Millimho)
        return self.__millimhos

    
    @property
    def kilomhos(self) -> float:
        """
        
        """
        if self.__kilomhos != None:
            return self.__kilomhos
        self.__kilomhos = self.__convert_from_base(ElectricAdmittanceUnits.Kilomho)
        return self.__kilomhos

    
    @property
    def megamhos(self) -> float:
        """
        
        """
        if self.__megamhos != None:
            return self.__megamhos
        self.__megamhos = self.__convert_from_base(ElectricAdmittanceUnits.Megamho)
        return self.__megamhos

    
    @property
    def gigamhos(self) -> float:
        """
        
        """
        if self.__gigamhos != None:
            return self.__gigamhos
        self.__gigamhos = self.__convert_from_base(ElectricAdmittanceUnits.Gigamho)
        return self.__gigamhos

    
    @property
    def teramhos(self) -> float:
        """
        
        """
        if self.__teramhos != None:
            return self.__teramhos
        self.__teramhos = self.__convert_from_base(ElectricAdmittanceUnits.Teramho)
        return self.__teramhos

    
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
        
        if unit == ElectricAdmittanceUnits.Mho:
            return f"""{super()._truncate_fraction_digits(self.mhos, fractional_digits)} ℧"""
        
        if unit == ElectricAdmittanceUnits.Nanosiemens:
            return f"""{super()._truncate_fraction_digits(self.nanosiemens, fractional_digits)} nS"""
        
        if unit == ElectricAdmittanceUnits.Microsiemens:
            return f"""{super()._truncate_fraction_digits(self.microsiemens, fractional_digits)} μS"""
        
        if unit == ElectricAdmittanceUnits.Millisiemens:
            return f"""{super()._truncate_fraction_digits(self.millisiemens, fractional_digits)} mS"""
        
        if unit == ElectricAdmittanceUnits.Kilosiemens:
            return f"""{super()._truncate_fraction_digits(self.kilosiemens, fractional_digits)} kS"""
        
        if unit == ElectricAdmittanceUnits.Megasiemens:
            return f"""{super()._truncate_fraction_digits(self.megasiemens, fractional_digits)} MS"""
        
        if unit == ElectricAdmittanceUnits.Gigasiemens:
            return f"""{super()._truncate_fraction_digits(self.gigasiemens, fractional_digits)} GS"""
        
        if unit == ElectricAdmittanceUnits.Terasiemens:
            return f"""{super()._truncate_fraction_digits(self.terasiemens, fractional_digits)} TS"""
        
        if unit == ElectricAdmittanceUnits.Nanomho:
            return f"""{super()._truncate_fraction_digits(self.nanomhos, fractional_digits)} n℧"""
        
        if unit == ElectricAdmittanceUnits.Micromho:
            return f"""{super()._truncate_fraction_digits(self.micromhos, fractional_digits)} μ℧"""
        
        if unit == ElectricAdmittanceUnits.Millimho:
            return f"""{super()._truncate_fraction_digits(self.millimhos, fractional_digits)} m℧"""
        
        if unit == ElectricAdmittanceUnits.Kilomho:
            return f"""{super()._truncate_fraction_digits(self.kilomhos, fractional_digits)} k℧"""
        
        if unit == ElectricAdmittanceUnits.Megamho:
            return f"""{super()._truncate_fraction_digits(self.megamhos, fractional_digits)} M℧"""
        
        if unit == ElectricAdmittanceUnits.Gigamho:
            return f"""{super()._truncate_fraction_digits(self.gigamhos, fractional_digits)} G℧"""
        
        if unit == ElectricAdmittanceUnits.Teramho:
            return f"""{super()._truncate_fraction_digits(self.teramhos, fractional_digits)} T℧"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: ElectricAdmittanceUnits = ElectricAdmittanceUnits.Siemens) -> str:
        """
        Get ElectricAdmittance unit abbreviation.
        Note! the default abbreviation for ElectricAdmittance is Siemens.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == ElectricAdmittanceUnits.Siemens:
            return """S"""
        
        if unit_abbreviation == ElectricAdmittanceUnits.Mho:
            return """℧"""
        
        if unit_abbreviation == ElectricAdmittanceUnits.Nanosiemens:
            return """nS"""
        
        if unit_abbreviation == ElectricAdmittanceUnits.Microsiemens:
            return """μS"""
        
        if unit_abbreviation == ElectricAdmittanceUnits.Millisiemens:
            return """mS"""
        
        if unit_abbreviation == ElectricAdmittanceUnits.Kilosiemens:
            return """kS"""
        
        if unit_abbreviation == ElectricAdmittanceUnits.Megasiemens:
            return """MS"""
        
        if unit_abbreviation == ElectricAdmittanceUnits.Gigasiemens:
            return """GS"""
        
        if unit_abbreviation == ElectricAdmittanceUnits.Terasiemens:
            return """TS"""
        
        if unit_abbreviation == ElectricAdmittanceUnits.Nanomho:
            return """n℧"""
        
        if unit_abbreviation == ElectricAdmittanceUnits.Micromho:
            return """μ℧"""
        
        if unit_abbreviation == ElectricAdmittanceUnits.Millimho:
            return """m℧"""
        
        if unit_abbreviation == ElectricAdmittanceUnits.Kilomho:
            return """k℧"""
        
        if unit_abbreviation == ElectricAdmittanceUnits.Megamho:
            return """M℧"""
        
        if unit_abbreviation == ElectricAdmittanceUnits.Gigamho:
            return """G℧"""
        
        if unit_abbreviation == ElectricAdmittanceUnits.Teramho:
            return """T℧"""
        
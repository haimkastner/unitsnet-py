from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class VolumeConcentrationUnits(Enum):
        """
            VolumeConcentrationUnits enumeration
        """
        
        DecimalFraction = 'DecimalFraction'
        """
            
        """
        
        LiterPerLiter = 'LiterPerLiter'
        """
            
        """
        
        LiterPerMilliliter = 'LiterPerMilliliter'
        """
            
        """
        
        Percent = 'Percent'
        """
            
        """
        
        PartPerThousand = 'PartPerThousand'
        """
            
        """
        
        PartPerMillion = 'PartPerMillion'
        """
            
        """
        
        PartPerBillion = 'PartPerBillion'
        """
            
        """
        
        PartPerTrillion = 'PartPerTrillion'
        """
            
        """
        
        PicoliterPerLiter = 'PicoliterPerLiter'
        """
            
        """
        
        NanoliterPerLiter = 'NanoliterPerLiter'
        """
            
        """
        
        MicroliterPerLiter = 'MicroliterPerLiter'
        """
            
        """
        
        MilliliterPerLiter = 'MilliliterPerLiter'
        """
            
        """
        
        CentiliterPerLiter = 'CentiliterPerLiter'
        """
            
        """
        
        DeciliterPerLiter = 'DeciliterPerLiter'
        """
            
        """
        
        PicoliterPerMilliliter = 'PicoliterPerMilliliter'
        """
            
        """
        
        NanoliterPerMilliliter = 'NanoliterPerMilliliter'
        """
            
        """
        
        MicroliterPerMilliliter = 'MicroliterPerMilliliter'
        """
            
        """
        
        MilliliterPerMilliliter = 'MilliliterPerMilliliter'
        """
            
        """
        
        CentiliterPerMilliliter = 'CentiliterPerMilliliter'
        """
            
        """
        
        DeciliterPerMilliliter = 'DeciliterPerMilliliter'
        """
            
        """
        

class VolumeConcentrationDto:
    """
    A DTO representation of a VolumeConcentration

    Attributes:
        value (float): The value of the VolumeConcentration.
        unit (VolumeConcentrationUnits): The specific unit that the VolumeConcentration value is representing.
    """

    def __init__(self, value: float, unit: VolumeConcentrationUnits):
        """
        Create a new DTO representation of a VolumeConcentration

        Parameters:
            value (float): The value of the VolumeConcentration.
            unit (VolumeConcentrationUnits): The specific unit that the VolumeConcentration value is representing.
        """
        self.value: float = value
        """
        The value of the VolumeConcentration
        """
        self.unit: VolumeConcentrationUnits = unit
        """
        The specific unit that the VolumeConcentration value is representing
        """

    def to_json(self):
        """
        Get a VolumeConcentration DTO JSON object representing the current unit.

        :return: JSON object represents VolumeConcentration DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "DecimalFraction"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of VolumeConcentration DTO from a json representation.

        :param data: The VolumeConcentration DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "DecimalFraction"}
        :return: A new instance of VolumeConcentrationDto.
        :rtype: VolumeConcentrationDto
        """
        return VolumeConcentrationDto(value=data["value"], unit=VolumeConcentrationUnits(data["unit"]))


class VolumeConcentration(AbstractMeasure):
    """
    The volume concentration (not to be confused with volume fraction) is defined as the volume of a constituent divided by the total volume of the mixture.

    Args:
        value (float): The value.
        from_unit (VolumeConcentrationUnits): The VolumeConcentration unit to create from, The default unit is DecimalFraction
    """
    def __init__(self, value: float, from_unit: VolumeConcentrationUnits = VolumeConcentrationUnits.DecimalFraction):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__decimal_fractions = None
        
        self.__liters_per_liter = None
        
        self.__liters_per_milliliter = None
        
        self.__percent = None
        
        self.__parts_per_thousand = None
        
        self.__parts_per_million = None
        
        self.__parts_per_billion = None
        
        self.__parts_per_trillion = None
        
        self.__picoliters_per_liter = None
        
        self.__nanoliters_per_liter = None
        
        self.__microliters_per_liter = None
        
        self.__milliliters_per_liter = None
        
        self.__centiliters_per_liter = None
        
        self.__deciliters_per_liter = None
        
        self.__picoliters_per_milliliter = None
        
        self.__nanoliters_per_milliliter = None
        
        self.__microliters_per_milliliter = None
        
        self.__milliliters_per_milliliter = None
        
        self.__centiliters_per_milliliter = None
        
        self.__deciliters_per_milliliter = None
        

    def convert(self, unit: VolumeConcentrationUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: VolumeConcentrationUnits = VolumeConcentrationUnits.DecimalFraction) -> VolumeConcentrationDto:
        """
        Get a new instance of VolumeConcentration DTO representing the current unit.

        :param hold_in_unit: The specific VolumeConcentration unit to store the VolumeConcentration value in the DTO representation.
        :type hold_in_unit: VolumeConcentrationUnits
        :return: A new instance of VolumeConcentrationDto.
        :rtype: VolumeConcentrationDto
        """
        return VolumeConcentrationDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: VolumeConcentrationUnits = VolumeConcentrationUnits.DecimalFraction):
        """
        Get a VolumeConcentration DTO JSON object representing the current unit.

        :param hold_in_unit: The specific VolumeConcentration unit to store the VolumeConcentration value in the DTO representation.
        :type hold_in_unit: VolumeConcentrationUnits
        :return: JSON object represents VolumeConcentration DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "DecimalFraction"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(volume_concentration_dto: VolumeConcentrationDto):
        """
        Obtain a new instance of VolumeConcentration from a DTO unit object.

        :param volume_concentration_dto: The VolumeConcentration DTO representation.
        :type volume_concentration_dto: VolumeConcentrationDto
        :return: A new instance of VolumeConcentration.
        :rtype: VolumeConcentration
        """
        return VolumeConcentration(volume_concentration_dto.value, volume_concentration_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of VolumeConcentration from a DTO unit json representation.

        :param data: The VolumeConcentration DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "DecimalFraction"}
        :return: A new instance of VolumeConcentration.
        :rtype: VolumeConcentration
        """
        return VolumeConcentration.from_dto(VolumeConcentrationDto.from_json(data))

    def __convert_from_base(self, from_unit: VolumeConcentrationUnits) -> float:
        value = self._value
        
        if from_unit == VolumeConcentrationUnits.DecimalFraction:
            return (value)
        
        if from_unit == VolumeConcentrationUnits.LiterPerLiter:
            return (value)
        
        if from_unit == VolumeConcentrationUnits.LiterPerMilliliter:
            return (value * 1e-3)
        
        if from_unit == VolumeConcentrationUnits.Percent:
            return (value * 1e2)
        
        if from_unit == VolumeConcentrationUnits.PartPerThousand:
            return (value * 1e3)
        
        if from_unit == VolumeConcentrationUnits.PartPerMillion:
            return (value * 1e6)
        
        if from_unit == VolumeConcentrationUnits.PartPerBillion:
            return (value * 1e9)
        
        if from_unit == VolumeConcentrationUnits.PartPerTrillion:
            return (value * 1e12)
        
        if from_unit == VolumeConcentrationUnits.PicoliterPerLiter:
            return ((value) / 1e-12)
        
        if from_unit == VolumeConcentrationUnits.NanoliterPerLiter:
            return ((value) / 1e-09)
        
        if from_unit == VolumeConcentrationUnits.MicroliterPerLiter:
            return ((value) / 1e-06)
        
        if from_unit == VolumeConcentrationUnits.MilliliterPerLiter:
            return ((value) / 0.001)
        
        if from_unit == VolumeConcentrationUnits.CentiliterPerLiter:
            return ((value) / 0.01)
        
        if from_unit == VolumeConcentrationUnits.DeciliterPerLiter:
            return ((value) / 0.1)
        
        if from_unit == VolumeConcentrationUnits.PicoliterPerMilliliter:
            return ((value * 1e-3) / 1e-12)
        
        if from_unit == VolumeConcentrationUnits.NanoliterPerMilliliter:
            return ((value * 1e-3) / 1e-09)
        
        if from_unit == VolumeConcentrationUnits.MicroliterPerMilliliter:
            return ((value * 1e-3) / 1e-06)
        
        if from_unit == VolumeConcentrationUnits.MilliliterPerMilliliter:
            return ((value * 1e-3) / 0.001)
        
        if from_unit == VolumeConcentrationUnits.CentiliterPerMilliliter:
            return ((value * 1e-3) / 0.01)
        
        if from_unit == VolumeConcentrationUnits.DeciliterPerMilliliter:
            return ((value * 1e-3) / 0.1)
        
        return None


    def __convert_to_base(self, value: float, to_unit: VolumeConcentrationUnits) -> float:
        
        if to_unit == VolumeConcentrationUnits.DecimalFraction:
            return (value)
        
        if to_unit == VolumeConcentrationUnits.LiterPerLiter:
            return (value)
        
        if to_unit == VolumeConcentrationUnits.LiterPerMilliliter:
            return (value / 1e-3)
        
        if to_unit == VolumeConcentrationUnits.Percent:
            return (value / 1e2)
        
        if to_unit == VolumeConcentrationUnits.PartPerThousand:
            return (value / 1e3)
        
        if to_unit == VolumeConcentrationUnits.PartPerMillion:
            return (value / 1e6)
        
        if to_unit == VolumeConcentrationUnits.PartPerBillion:
            return (value / 1e9)
        
        if to_unit == VolumeConcentrationUnits.PartPerTrillion:
            return (value / 1e12)
        
        if to_unit == VolumeConcentrationUnits.PicoliterPerLiter:
            return ((value) * 1e-12)
        
        if to_unit == VolumeConcentrationUnits.NanoliterPerLiter:
            return ((value) * 1e-09)
        
        if to_unit == VolumeConcentrationUnits.MicroliterPerLiter:
            return ((value) * 1e-06)
        
        if to_unit == VolumeConcentrationUnits.MilliliterPerLiter:
            return ((value) * 0.001)
        
        if to_unit == VolumeConcentrationUnits.CentiliterPerLiter:
            return ((value) * 0.01)
        
        if to_unit == VolumeConcentrationUnits.DeciliterPerLiter:
            return ((value) * 0.1)
        
        if to_unit == VolumeConcentrationUnits.PicoliterPerMilliliter:
            return ((value / 1e-3) * 1e-12)
        
        if to_unit == VolumeConcentrationUnits.NanoliterPerMilliliter:
            return ((value / 1e-3) * 1e-09)
        
        if to_unit == VolumeConcentrationUnits.MicroliterPerMilliliter:
            return ((value / 1e-3) * 1e-06)
        
        if to_unit == VolumeConcentrationUnits.MilliliterPerMilliliter:
            return ((value / 1e-3) * 0.001)
        
        if to_unit == VolumeConcentrationUnits.CentiliterPerMilliliter:
            return ((value / 1e-3) * 0.01)
        
        if to_unit == VolumeConcentrationUnits.DeciliterPerMilliliter:
            return ((value / 1e-3) * 0.1)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_decimal_fractions(decimal_fractions: float):
        """
        Create a new instance of VolumeConcentration from a value in decimal_fractions.

        

        :param meters: The VolumeConcentration value in decimal_fractions.
        :type decimal_fractions: float
        :return: A new instance of VolumeConcentration.
        :rtype: VolumeConcentration
        """
        return VolumeConcentration(decimal_fractions, VolumeConcentrationUnits.DecimalFraction)

    
    @staticmethod
    def from_liters_per_liter(liters_per_liter: float):
        """
        Create a new instance of VolumeConcentration from a value in liters_per_liter.

        

        :param meters: The VolumeConcentration value in liters_per_liter.
        :type liters_per_liter: float
        :return: A new instance of VolumeConcentration.
        :rtype: VolumeConcentration
        """
        return VolumeConcentration(liters_per_liter, VolumeConcentrationUnits.LiterPerLiter)

    
    @staticmethod
    def from_liters_per_milliliter(liters_per_milliliter: float):
        """
        Create a new instance of VolumeConcentration from a value in liters_per_milliliter.

        

        :param meters: The VolumeConcentration value in liters_per_milliliter.
        :type liters_per_milliliter: float
        :return: A new instance of VolumeConcentration.
        :rtype: VolumeConcentration
        """
        return VolumeConcentration(liters_per_milliliter, VolumeConcentrationUnits.LiterPerMilliliter)

    
    @staticmethod
    def from_percent(percent: float):
        """
        Create a new instance of VolumeConcentration from a value in percent.

        

        :param meters: The VolumeConcentration value in percent.
        :type percent: float
        :return: A new instance of VolumeConcentration.
        :rtype: VolumeConcentration
        """
        return VolumeConcentration(percent, VolumeConcentrationUnits.Percent)

    
    @staticmethod
    def from_parts_per_thousand(parts_per_thousand: float):
        """
        Create a new instance of VolumeConcentration from a value in parts_per_thousand.

        

        :param meters: The VolumeConcentration value in parts_per_thousand.
        :type parts_per_thousand: float
        :return: A new instance of VolumeConcentration.
        :rtype: VolumeConcentration
        """
        return VolumeConcentration(parts_per_thousand, VolumeConcentrationUnits.PartPerThousand)

    
    @staticmethod
    def from_parts_per_million(parts_per_million: float):
        """
        Create a new instance of VolumeConcentration from a value in parts_per_million.

        

        :param meters: The VolumeConcentration value in parts_per_million.
        :type parts_per_million: float
        :return: A new instance of VolumeConcentration.
        :rtype: VolumeConcentration
        """
        return VolumeConcentration(parts_per_million, VolumeConcentrationUnits.PartPerMillion)

    
    @staticmethod
    def from_parts_per_billion(parts_per_billion: float):
        """
        Create a new instance of VolumeConcentration from a value in parts_per_billion.

        

        :param meters: The VolumeConcentration value in parts_per_billion.
        :type parts_per_billion: float
        :return: A new instance of VolumeConcentration.
        :rtype: VolumeConcentration
        """
        return VolumeConcentration(parts_per_billion, VolumeConcentrationUnits.PartPerBillion)

    
    @staticmethod
    def from_parts_per_trillion(parts_per_trillion: float):
        """
        Create a new instance of VolumeConcentration from a value in parts_per_trillion.

        

        :param meters: The VolumeConcentration value in parts_per_trillion.
        :type parts_per_trillion: float
        :return: A new instance of VolumeConcentration.
        :rtype: VolumeConcentration
        """
        return VolumeConcentration(parts_per_trillion, VolumeConcentrationUnits.PartPerTrillion)

    
    @staticmethod
    def from_picoliters_per_liter(picoliters_per_liter: float):
        """
        Create a new instance of VolumeConcentration from a value in picoliters_per_liter.

        

        :param meters: The VolumeConcentration value in picoliters_per_liter.
        :type picoliters_per_liter: float
        :return: A new instance of VolumeConcentration.
        :rtype: VolumeConcentration
        """
        return VolumeConcentration(picoliters_per_liter, VolumeConcentrationUnits.PicoliterPerLiter)

    
    @staticmethod
    def from_nanoliters_per_liter(nanoliters_per_liter: float):
        """
        Create a new instance of VolumeConcentration from a value in nanoliters_per_liter.

        

        :param meters: The VolumeConcentration value in nanoliters_per_liter.
        :type nanoliters_per_liter: float
        :return: A new instance of VolumeConcentration.
        :rtype: VolumeConcentration
        """
        return VolumeConcentration(nanoliters_per_liter, VolumeConcentrationUnits.NanoliterPerLiter)

    
    @staticmethod
    def from_microliters_per_liter(microliters_per_liter: float):
        """
        Create a new instance of VolumeConcentration from a value in microliters_per_liter.

        

        :param meters: The VolumeConcentration value in microliters_per_liter.
        :type microliters_per_liter: float
        :return: A new instance of VolumeConcentration.
        :rtype: VolumeConcentration
        """
        return VolumeConcentration(microliters_per_liter, VolumeConcentrationUnits.MicroliterPerLiter)

    
    @staticmethod
    def from_milliliters_per_liter(milliliters_per_liter: float):
        """
        Create a new instance of VolumeConcentration from a value in milliliters_per_liter.

        

        :param meters: The VolumeConcentration value in milliliters_per_liter.
        :type milliliters_per_liter: float
        :return: A new instance of VolumeConcentration.
        :rtype: VolumeConcentration
        """
        return VolumeConcentration(milliliters_per_liter, VolumeConcentrationUnits.MilliliterPerLiter)

    
    @staticmethod
    def from_centiliters_per_liter(centiliters_per_liter: float):
        """
        Create a new instance of VolumeConcentration from a value in centiliters_per_liter.

        

        :param meters: The VolumeConcentration value in centiliters_per_liter.
        :type centiliters_per_liter: float
        :return: A new instance of VolumeConcentration.
        :rtype: VolumeConcentration
        """
        return VolumeConcentration(centiliters_per_liter, VolumeConcentrationUnits.CentiliterPerLiter)

    
    @staticmethod
    def from_deciliters_per_liter(deciliters_per_liter: float):
        """
        Create a new instance of VolumeConcentration from a value in deciliters_per_liter.

        

        :param meters: The VolumeConcentration value in deciliters_per_liter.
        :type deciliters_per_liter: float
        :return: A new instance of VolumeConcentration.
        :rtype: VolumeConcentration
        """
        return VolumeConcentration(deciliters_per_liter, VolumeConcentrationUnits.DeciliterPerLiter)

    
    @staticmethod
    def from_picoliters_per_milliliter(picoliters_per_milliliter: float):
        """
        Create a new instance of VolumeConcentration from a value in picoliters_per_milliliter.

        

        :param meters: The VolumeConcentration value in picoliters_per_milliliter.
        :type picoliters_per_milliliter: float
        :return: A new instance of VolumeConcentration.
        :rtype: VolumeConcentration
        """
        return VolumeConcentration(picoliters_per_milliliter, VolumeConcentrationUnits.PicoliterPerMilliliter)

    
    @staticmethod
    def from_nanoliters_per_milliliter(nanoliters_per_milliliter: float):
        """
        Create a new instance of VolumeConcentration from a value in nanoliters_per_milliliter.

        

        :param meters: The VolumeConcentration value in nanoliters_per_milliliter.
        :type nanoliters_per_milliliter: float
        :return: A new instance of VolumeConcentration.
        :rtype: VolumeConcentration
        """
        return VolumeConcentration(nanoliters_per_milliliter, VolumeConcentrationUnits.NanoliterPerMilliliter)

    
    @staticmethod
    def from_microliters_per_milliliter(microliters_per_milliliter: float):
        """
        Create a new instance of VolumeConcentration from a value in microliters_per_milliliter.

        

        :param meters: The VolumeConcentration value in microliters_per_milliliter.
        :type microliters_per_milliliter: float
        :return: A new instance of VolumeConcentration.
        :rtype: VolumeConcentration
        """
        return VolumeConcentration(microliters_per_milliliter, VolumeConcentrationUnits.MicroliterPerMilliliter)

    
    @staticmethod
    def from_milliliters_per_milliliter(milliliters_per_milliliter: float):
        """
        Create a new instance of VolumeConcentration from a value in milliliters_per_milliliter.

        

        :param meters: The VolumeConcentration value in milliliters_per_milliliter.
        :type milliliters_per_milliliter: float
        :return: A new instance of VolumeConcentration.
        :rtype: VolumeConcentration
        """
        return VolumeConcentration(milliliters_per_milliliter, VolumeConcentrationUnits.MilliliterPerMilliliter)

    
    @staticmethod
    def from_centiliters_per_milliliter(centiliters_per_milliliter: float):
        """
        Create a new instance of VolumeConcentration from a value in centiliters_per_milliliter.

        

        :param meters: The VolumeConcentration value in centiliters_per_milliliter.
        :type centiliters_per_milliliter: float
        :return: A new instance of VolumeConcentration.
        :rtype: VolumeConcentration
        """
        return VolumeConcentration(centiliters_per_milliliter, VolumeConcentrationUnits.CentiliterPerMilliliter)

    
    @staticmethod
    def from_deciliters_per_milliliter(deciliters_per_milliliter: float):
        """
        Create a new instance of VolumeConcentration from a value in deciliters_per_milliliter.

        

        :param meters: The VolumeConcentration value in deciliters_per_milliliter.
        :type deciliters_per_milliliter: float
        :return: A new instance of VolumeConcentration.
        :rtype: VolumeConcentration
        """
        return VolumeConcentration(deciliters_per_milliliter, VolumeConcentrationUnits.DeciliterPerMilliliter)

    
    @property
    def decimal_fractions(self) -> float:
        """
        
        """
        if self.__decimal_fractions != None:
            return self.__decimal_fractions
        self.__decimal_fractions = self.__convert_from_base(VolumeConcentrationUnits.DecimalFraction)
        return self.__decimal_fractions

    
    @property
    def liters_per_liter(self) -> float:
        """
        
        """
        if self.__liters_per_liter != None:
            return self.__liters_per_liter
        self.__liters_per_liter = self.__convert_from_base(VolumeConcentrationUnits.LiterPerLiter)
        return self.__liters_per_liter

    
    @property
    def liters_per_milliliter(self) -> float:
        """
        
        """
        if self.__liters_per_milliliter != None:
            return self.__liters_per_milliliter
        self.__liters_per_milliliter = self.__convert_from_base(VolumeConcentrationUnits.LiterPerMilliliter)
        return self.__liters_per_milliliter

    
    @property
    def percent(self) -> float:
        """
        
        """
        if self.__percent != None:
            return self.__percent
        self.__percent = self.__convert_from_base(VolumeConcentrationUnits.Percent)
        return self.__percent

    
    @property
    def parts_per_thousand(self) -> float:
        """
        
        """
        if self.__parts_per_thousand != None:
            return self.__parts_per_thousand
        self.__parts_per_thousand = self.__convert_from_base(VolumeConcentrationUnits.PartPerThousand)
        return self.__parts_per_thousand

    
    @property
    def parts_per_million(self) -> float:
        """
        
        """
        if self.__parts_per_million != None:
            return self.__parts_per_million
        self.__parts_per_million = self.__convert_from_base(VolumeConcentrationUnits.PartPerMillion)
        return self.__parts_per_million

    
    @property
    def parts_per_billion(self) -> float:
        """
        
        """
        if self.__parts_per_billion != None:
            return self.__parts_per_billion
        self.__parts_per_billion = self.__convert_from_base(VolumeConcentrationUnits.PartPerBillion)
        return self.__parts_per_billion

    
    @property
    def parts_per_trillion(self) -> float:
        """
        
        """
        if self.__parts_per_trillion != None:
            return self.__parts_per_trillion
        self.__parts_per_trillion = self.__convert_from_base(VolumeConcentrationUnits.PartPerTrillion)
        return self.__parts_per_trillion

    
    @property
    def picoliters_per_liter(self) -> float:
        """
        
        """
        if self.__picoliters_per_liter != None:
            return self.__picoliters_per_liter
        self.__picoliters_per_liter = self.__convert_from_base(VolumeConcentrationUnits.PicoliterPerLiter)
        return self.__picoliters_per_liter

    
    @property
    def nanoliters_per_liter(self) -> float:
        """
        
        """
        if self.__nanoliters_per_liter != None:
            return self.__nanoliters_per_liter
        self.__nanoliters_per_liter = self.__convert_from_base(VolumeConcentrationUnits.NanoliterPerLiter)
        return self.__nanoliters_per_liter

    
    @property
    def microliters_per_liter(self) -> float:
        """
        
        """
        if self.__microliters_per_liter != None:
            return self.__microliters_per_liter
        self.__microliters_per_liter = self.__convert_from_base(VolumeConcentrationUnits.MicroliterPerLiter)
        return self.__microliters_per_liter

    
    @property
    def milliliters_per_liter(self) -> float:
        """
        
        """
        if self.__milliliters_per_liter != None:
            return self.__milliliters_per_liter
        self.__milliliters_per_liter = self.__convert_from_base(VolumeConcentrationUnits.MilliliterPerLiter)
        return self.__milliliters_per_liter

    
    @property
    def centiliters_per_liter(self) -> float:
        """
        
        """
        if self.__centiliters_per_liter != None:
            return self.__centiliters_per_liter
        self.__centiliters_per_liter = self.__convert_from_base(VolumeConcentrationUnits.CentiliterPerLiter)
        return self.__centiliters_per_liter

    
    @property
    def deciliters_per_liter(self) -> float:
        """
        
        """
        if self.__deciliters_per_liter != None:
            return self.__deciliters_per_liter
        self.__deciliters_per_liter = self.__convert_from_base(VolumeConcentrationUnits.DeciliterPerLiter)
        return self.__deciliters_per_liter

    
    @property
    def picoliters_per_milliliter(self) -> float:
        """
        
        """
        if self.__picoliters_per_milliliter != None:
            return self.__picoliters_per_milliliter
        self.__picoliters_per_milliliter = self.__convert_from_base(VolumeConcentrationUnits.PicoliterPerMilliliter)
        return self.__picoliters_per_milliliter

    
    @property
    def nanoliters_per_milliliter(self) -> float:
        """
        
        """
        if self.__nanoliters_per_milliliter != None:
            return self.__nanoliters_per_milliliter
        self.__nanoliters_per_milliliter = self.__convert_from_base(VolumeConcentrationUnits.NanoliterPerMilliliter)
        return self.__nanoliters_per_milliliter

    
    @property
    def microliters_per_milliliter(self) -> float:
        """
        
        """
        if self.__microliters_per_milliliter != None:
            return self.__microliters_per_milliliter
        self.__microliters_per_milliliter = self.__convert_from_base(VolumeConcentrationUnits.MicroliterPerMilliliter)
        return self.__microliters_per_milliliter

    
    @property
    def milliliters_per_milliliter(self) -> float:
        """
        
        """
        if self.__milliliters_per_milliliter != None:
            return self.__milliliters_per_milliliter
        self.__milliliters_per_milliliter = self.__convert_from_base(VolumeConcentrationUnits.MilliliterPerMilliliter)
        return self.__milliliters_per_milliliter

    
    @property
    def centiliters_per_milliliter(self) -> float:
        """
        
        """
        if self.__centiliters_per_milliliter != None:
            return self.__centiliters_per_milliliter
        self.__centiliters_per_milliliter = self.__convert_from_base(VolumeConcentrationUnits.CentiliterPerMilliliter)
        return self.__centiliters_per_milliliter

    
    @property
    def deciliters_per_milliliter(self) -> float:
        """
        
        """
        if self.__deciliters_per_milliliter != None:
            return self.__deciliters_per_milliliter
        self.__deciliters_per_milliliter = self.__convert_from_base(VolumeConcentrationUnits.DeciliterPerMilliliter)
        return self.__deciliters_per_milliliter

    
    def to_string(self, unit: VolumeConcentrationUnits = VolumeConcentrationUnits.DecimalFraction, fractional_digits: int = None) -> str:
        """
        Format the VolumeConcentration to a string.
        
        Note: the default format for VolumeConcentration is DecimalFraction.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the VolumeConcentration. Default is 'DecimalFraction'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == VolumeConcentrationUnits.DecimalFraction:
            return f"""{super()._truncate_fraction_digits(self.decimal_fractions, fractional_digits)} """
        
        if unit == VolumeConcentrationUnits.LiterPerLiter:
            return f"""{super()._truncate_fraction_digits(self.liters_per_liter, fractional_digits)} l/l"""
        
        if unit == VolumeConcentrationUnits.LiterPerMilliliter:
            return f"""{super()._truncate_fraction_digits(self.liters_per_milliliter, fractional_digits)} l/ml"""
        
        if unit == VolumeConcentrationUnits.Percent:
            return f"""{super()._truncate_fraction_digits(self.percent, fractional_digits)} %"""
        
        if unit == VolumeConcentrationUnits.PartPerThousand:
            return f"""{super()._truncate_fraction_digits(self.parts_per_thousand, fractional_digits)} ‰"""
        
        if unit == VolumeConcentrationUnits.PartPerMillion:
            return f"""{super()._truncate_fraction_digits(self.parts_per_million, fractional_digits)} ppm"""
        
        if unit == VolumeConcentrationUnits.PartPerBillion:
            return f"""{super()._truncate_fraction_digits(self.parts_per_billion, fractional_digits)} ppb"""
        
        if unit == VolumeConcentrationUnits.PartPerTrillion:
            return f"""{super()._truncate_fraction_digits(self.parts_per_trillion, fractional_digits)} ppt"""
        
        if unit == VolumeConcentrationUnits.PicoliterPerLiter:
            return f"""{super()._truncate_fraction_digits(self.picoliters_per_liter, fractional_digits)} pl/l"""
        
        if unit == VolumeConcentrationUnits.NanoliterPerLiter:
            return f"""{super()._truncate_fraction_digits(self.nanoliters_per_liter, fractional_digits)} nl/l"""
        
        if unit == VolumeConcentrationUnits.MicroliterPerLiter:
            return f"""{super()._truncate_fraction_digits(self.microliters_per_liter, fractional_digits)} μl/l"""
        
        if unit == VolumeConcentrationUnits.MilliliterPerLiter:
            return f"""{super()._truncate_fraction_digits(self.milliliters_per_liter, fractional_digits)} ml/l"""
        
        if unit == VolumeConcentrationUnits.CentiliterPerLiter:
            return f"""{super()._truncate_fraction_digits(self.centiliters_per_liter, fractional_digits)} cl/l"""
        
        if unit == VolumeConcentrationUnits.DeciliterPerLiter:
            return f"""{super()._truncate_fraction_digits(self.deciliters_per_liter, fractional_digits)} dl/l"""
        
        if unit == VolumeConcentrationUnits.PicoliterPerMilliliter:
            return f"""{super()._truncate_fraction_digits(self.picoliters_per_milliliter, fractional_digits)} pl/ml"""
        
        if unit == VolumeConcentrationUnits.NanoliterPerMilliliter:
            return f"""{super()._truncate_fraction_digits(self.nanoliters_per_milliliter, fractional_digits)} nl/ml"""
        
        if unit == VolumeConcentrationUnits.MicroliterPerMilliliter:
            return f"""{super()._truncate_fraction_digits(self.microliters_per_milliliter, fractional_digits)} μl/ml"""
        
        if unit == VolumeConcentrationUnits.MilliliterPerMilliliter:
            return f"""{super()._truncate_fraction_digits(self.milliliters_per_milliliter, fractional_digits)} ml/ml"""
        
        if unit == VolumeConcentrationUnits.CentiliterPerMilliliter:
            return f"""{super()._truncate_fraction_digits(self.centiliters_per_milliliter, fractional_digits)} cl/ml"""
        
        if unit == VolumeConcentrationUnits.DeciliterPerMilliliter:
            return f"""{super()._truncate_fraction_digits(self.deciliters_per_milliliter, fractional_digits)} dl/ml"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: VolumeConcentrationUnits = VolumeConcentrationUnits.DecimalFraction) -> str:
        """
        Get VolumeConcentration unit abbreviation.
        Note! the default abbreviation for VolumeConcentration is DecimalFraction.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == VolumeConcentrationUnits.DecimalFraction:
            return """"""
        
        if unit_abbreviation == VolumeConcentrationUnits.LiterPerLiter:
            return """l/l"""
        
        if unit_abbreviation == VolumeConcentrationUnits.LiterPerMilliliter:
            return """l/ml"""
        
        if unit_abbreviation == VolumeConcentrationUnits.Percent:
            return """%"""
        
        if unit_abbreviation == VolumeConcentrationUnits.PartPerThousand:
            return """‰"""
        
        if unit_abbreviation == VolumeConcentrationUnits.PartPerMillion:
            return """ppm"""
        
        if unit_abbreviation == VolumeConcentrationUnits.PartPerBillion:
            return """ppb"""
        
        if unit_abbreviation == VolumeConcentrationUnits.PartPerTrillion:
            return """ppt"""
        
        if unit_abbreviation == VolumeConcentrationUnits.PicoliterPerLiter:
            return """pl/l"""
        
        if unit_abbreviation == VolumeConcentrationUnits.NanoliterPerLiter:
            return """nl/l"""
        
        if unit_abbreviation == VolumeConcentrationUnits.MicroliterPerLiter:
            return """μl/l"""
        
        if unit_abbreviation == VolumeConcentrationUnits.MilliliterPerLiter:
            return """ml/l"""
        
        if unit_abbreviation == VolumeConcentrationUnits.CentiliterPerLiter:
            return """cl/l"""
        
        if unit_abbreviation == VolumeConcentrationUnits.DeciliterPerLiter:
            return """dl/l"""
        
        if unit_abbreviation == VolumeConcentrationUnits.PicoliterPerMilliliter:
            return """pl/ml"""
        
        if unit_abbreviation == VolumeConcentrationUnits.NanoliterPerMilliliter:
            return """nl/ml"""
        
        if unit_abbreviation == VolumeConcentrationUnits.MicroliterPerMilliliter:
            return """μl/ml"""
        
        if unit_abbreviation == VolumeConcentrationUnits.MilliliterPerMilliliter:
            return """ml/ml"""
        
        if unit_abbreviation == VolumeConcentrationUnits.CentiliterPerMilliliter:
            return """cl/ml"""
        
        if unit_abbreviation == VolumeConcentrationUnits.DeciliterPerMilliliter:
            return """dl/ml"""
        
from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class LuminanceUnits(Enum):
        """
            LuminanceUnits enumeration
        """
        
        CandelaPerSquareMeter = 'CandelaPerSquareMeter'
        """
            
        """
        
        CandelaPerSquareFoot = 'CandelaPerSquareFoot'
        """
            
        """
        
        CandelaPerSquareInch = 'CandelaPerSquareInch'
        """
            
        """
        
        Nit = 'Nit'
        """
            
        """
        
        NanocandelaPerSquareMeter = 'NanocandelaPerSquareMeter'
        """
            
        """
        
        MicrocandelaPerSquareMeter = 'MicrocandelaPerSquareMeter'
        """
            
        """
        
        MillicandelaPerSquareMeter = 'MillicandelaPerSquareMeter'
        """
            
        """
        
        CenticandelaPerSquareMeter = 'CenticandelaPerSquareMeter'
        """
            
        """
        
        DecicandelaPerSquareMeter = 'DecicandelaPerSquareMeter'
        """
            
        """
        
        KilocandelaPerSquareMeter = 'KilocandelaPerSquareMeter'
        """
            
        """
        

class LuminanceDto:
    """
    A DTO representation of a Luminance

    Attributes:
        value (float): The value of the Luminance.
        unit (LuminanceUnits): The specific unit that the Luminance value is representing.
    """

    def __init__(self, value: float, unit: LuminanceUnits):
        """
        Create a new DTO representation of a Luminance

        Parameters:
            value (float): The value of the Luminance.
            unit (LuminanceUnits): The specific unit that the Luminance value is representing.
        """
        self.value: float = value
        """
        The value of the Luminance
        """
        self.unit: LuminanceUnits = unit
        """
        The specific unit that the Luminance value is representing
        """

    def to_json(self):
        """
        Get a Luminance DTO JSON object representing the current unit.

        :return: JSON object represents Luminance DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "CandelaPerSquareMeter"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of Luminance DTO from a json representation.

        :param data: The Luminance DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "CandelaPerSquareMeter"}
        :return: A new instance of LuminanceDto.
        :rtype: LuminanceDto
        """
        return LuminanceDto(value=data["value"], unit=LuminanceUnits(data["unit"]))


class Luminance(AbstractMeasure):
    """
    None

    Args:
        value (float): The value.
        from_unit (LuminanceUnits): The Luminance unit to create from, The default unit is CandelaPerSquareMeter
    """
    def __init__(self, value: float, from_unit: LuminanceUnits = LuminanceUnits.CandelaPerSquareMeter):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__candelas_per_square_meter = None
        
        self.__candelas_per_square_foot = None
        
        self.__candelas_per_square_inch = None
        
        self.__nits = None
        
        self.__nanocandelas_per_square_meter = None
        
        self.__microcandelas_per_square_meter = None
        
        self.__millicandelas_per_square_meter = None
        
        self.__centicandelas_per_square_meter = None
        
        self.__decicandelas_per_square_meter = None
        
        self.__kilocandelas_per_square_meter = None
        

    def convert(self, unit: LuminanceUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: LuminanceUnits = LuminanceUnits.CandelaPerSquareMeter) -> LuminanceDto:
        """
        Get a new instance of Luminance DTO representing the current unit.

        :param hold_in_unit: The specific Luminance unit to store the Luminance value in the DTO representation.
        :type hold_in_unit: LuminanceUnits
        :return: A new instance of LuminanceDto.
        :rtype: LuminanceDto
        """
        return LuminanceDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: LuminanceUnits = LuminanceUnits.CandelaPerSquareMeter):
        """
        Get a Luminance DTO JSON object representing the current unit.

        :param hold_in_unit: The specific Luminance unit to store the Luminance value in the DTO representation.
        :type hold_in_unit: LuminanceUnits
        :return: JSON object represents Luminance DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "CandelaPerSquareMeter"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(luminance_dto: LuminanceDto):
        """
        Obtain a new instance of Luminance from a DTO unit object.

        :param luminance_dto: The Luminance DTO representation.
        :type luminance_dto: LuminanceDto
        :return: A new instance of Luminance.
        :rtype: Luminance
        """
        return Luminance(luminance_dto.value, luminance_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of Luminance from a DTO unit json representation.

        :param data: The Luminance DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "CandelaPerSquareMeter"}
        :return: A new instance of Luminance.
        :rtype: Luminance
        """
        return Luminance.from_dto(LuminanceDto.from_json(data))

    def __convert_from_base(self, from_unit: LuminanceUnits) -> float:
        value = self._value
        
        if from_unit == LuminanceUnits.CandelaPerSquareMeter:
            return (value)
        
        if from_unit == LuminanceUnits.CandelaPerSquareFoot:
            return (value/ 1.07639e1)
        
        if from_unit == LuminanceUnits.CandelaPerSquareInch:
            return (value/ 1.5500031e3)
        
        if from_unit == LuminanceUnits.Nit:
            return (value)
        
        if from_unit == LuminanceUnits.NanocandelaPerSquareMeter:
            return ((value) / 1e-09)
        
        if from_unit == LuminanceUnits.MicrocandelaPerSquareMeter:
            return ((value) / 1e-06)
        
        if from_unit == LuminanceUnits.MillicandelaPerSquareMeter:
            return ((value) / 0.001)
        
        if from_unit == LuminanceUnits.CenticandelaPerSquareMeter:
            return ((value) / 0.01)
        
        if from_unit == LuminanceUnits.DecicandelaPerSquareMeter:
            return ((value) / 0.1)
        
        if from_unit == LuminanceUnits.KilocandelaPerSquareMeter:
            return ((value) / 1000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: LuminanceUnits) -> float:
        
        if to_unit == LuminanceUnits.CandelaPerSquareMeter:
            return (value)
        
        if to_unit == LuminanceUnits.CandelaPerSquareFoot:
            return (value* 1.07639e1)
        
        if to_unit == LuminanceUnits.CandelaPerSquareInch:
            return (value* 1.5500031e3)
        
        if to_unit == LuminanceUnits.Nit:
            return (value)
        
        if to_unit == LuminanceUnits.NanocandelaPerSquareMeter:
            return ((value) * 1e-09)
        
        if to_unit == LuminanceUnits.MicrocandelaPerSquareMeter:
            return ((value) * 1e-06)
        
        if to_unit == LuminanceUnits.MillicandelaPerSquareMeter:
            return ((value) * 0.001)
        
        if to_unit == LuminanceUnits.CenticandelaPerSquareMeter:
            return ((value) * 0.01)
        
        if to_unit == LuminanceUnits.DecicandelaPerSquareMeter:
            return ((value) * 0.1)
        
        if to_unit == LuminanceUnits.KilocandelaPerSquareMeter:
            return ((value) * 1000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_candelas_per_square_meter(candelas_per_square_meter: float):
        """
        Create a new instance of Luminance from a value in candelas_per_square_meter.

        

        :param meters: The Luminance value in candelas_per_square_meter.
        :type candelas_per_square_meter: float
        :return: A new instance of Luminance.
        :rtype: Luminance
        """
        return Luminance(candelas_per_square_meter, LuminanceUnits.CandelaPerSquareMeter)

    
    @staticmethod
    def from_candelas_per_square_foot(candelas_per_square_foot: float):
        """
        Create a new instance of Luminance from a value in candelas_per_square_foot.

        

        :param meters: The Luminance value in candelas_per_square_foot.
        :type candelas_per_square_foot: float
        :return: A new instance of Luminance.
        :rtype: Luminance
        """
        return Luminance(candelas_per_square_foot, LuminanceUnits.CandelaPerSquareFoot)

    
    @staticmethod
    def from_candelas_per_square_inch(candelas_per_square_inch: float):
        """
        Create a new instance of Luminance from a value in candelas_per_square_inch.

        

        :param meters: The Luminance value in candelas_per_square_inch.
        :type candelas_per_square_inch: float
        :return: A new instance of Luminance.
        :rtype: Luminance
        """
        return Luminance(candelas_per_square_inch, LuminanceUnits.CandelaPerSquareInch)

    
    @staticmethod
    def from_nits(nits: float):
        """
        Create a new instance of Luminance from a value in nits.

        

        :param meters: The Luminance value in nits.
        :type nits: float
        :return: A new instance of Luminance.
        :rtype: Luminance
        """
        return Luminance(nits, LuminanceUnits.Nit)

    
    @staticmethod
    def from_nanocandelas_per_square_meter(nanocandelas_per_square_meter: float):
        """
        Create a new instance of Luminance from a value in nanocandelas_per_square_meter.

        

        :param meters: The Luminance value in nanocandelas_per_square_meter.
        :type nanocandelas_per_square_meter: float
        :return: A new instance of Luminance.
        :rtype: Luminance
        """
        return Luminance(nanocandelas_per_square_meter, LuminanceUnits.NanocandelaPerSquareMeter)

    
    @staticmethod
    def from_microcandelas_per_square_meter(microcandelas_per_square_meter: float):
        """
        Create a new instance of Luminance from a value in microcandelas_per_square_meter.

        

        :param meters: The Luminance value in microcandelas_per_square_meter.
        :type microcandelas_per_square_meter: float
        :return: A new instance of Luminance.
        :rtype: Luminance
        """
        return Luminance(microcandelas_per_square_meter, LuminanceUnits.MicrocandelaPerSquareMeter)

    
    @staticmethod
    def from_millicandelas_per_square_meter(millicandelas_per_square_meter: float):
        """
        Create a new instance of Luminance from a value in millicandelas_per_square_meter.

        

        :param meters: The Luminance value in millicandelas_per_square_meter.
        :type millicandelas_per_square_meter: float
        :return: A new instance of Luminance.
        :rtype: Luminance
        """
        return Luminance(millicandelas_per_square_meter, LuminanceUnits.MillicandelaPerSquareMeter)

    
    @staticmethod
    def from_centicandelas_per_square_meter(centicandelas_per_square_meter: float):
        """
        Create a new instance of Luminance from a value in centicandelas_per_square_meter.

        

        :param meters: The Luminance value in centicandelas_per_square_meter.
        :type centicandelas_per_square_meter: float
        :return: A new instance of Luminance.
        :rtype: Luminance
        """
        return Luminance(centicandelas_per_square_meter, LuminanceUnits.CenticandelaPerSquareMeter)

    
    @staticmethod
    def from_decicandelas_per_square_meter(decicandelas_per_square_meter: float):
        """
        Create a new instance of Luminance from a value in decicandelas_per_square_meter.

        

        :param meters: The Luminance value in decicandelas_per_square_meter.
        :type decicandelas_per_square_meter: float
        :return: A new instance of Luminance.
        :rtype: Luminance
        """
        return Luminance(decicandelas_per_square_meter, LuminanceUnits.DecicandelaPerSquareMeter)

    
    @staticmethod
    def from_kilocandelas_per_square_meter(kilocandelas_per_square_meter: float):
        """
        Create a new instance of Luminance from a value in kilocandelas_per_square_meter.

        

        :param meters: The Luminance value in kilocandelas_per_square_meter.
        :type kilocandelas_per_square_meter: float
        :return: A new instance of Luminance.
        :rtype: Luminance
        """
        return Luminance(kilocandelas_per_square_meter, LuminanceUnits.KilocandelaPerSquareMeter)

    
    @property
    def candelas_per_square_meter(self) -> float:
        """
        
        """
        if self.__candelas_per_square_meter != None:
            return self.__candelas_per_square_meter
        self.__candelas_per_square_meter = self.__convert_from_base(LuminanceUnits.CandelaPerSquareMeter)
        return self.__candelas_per_square_meter

    
    @property
    def candelas_per_square_foot(self) -> float:
        """
        
        """
        if self.__candelas_per_square_foot != None:
            return self.__candelas_per_square_foot
        self.__candelas_per_square_foot = self.__convert_from_base(LuminanceUnits.CandelaPerSquareFoot)
        return self.__candelas_per_square_foot

    
    @property
    def candelas_per_square_inch(self) -> float:
        """
        
        """
        if self.__candelas_per_square_inch != None:
            return self.__candelas_per_square_inch
        self.__candelas_per_square_inch = self.__convert_from_base(LuminanceUnits.CandelaPerSquareInch)
        return self.__candelas_per_square_inch

    
    @property
    def nits(self) -> float:
        """
        
        """
        if self.__nits != None:
            return self.__nits
        self.__nits = self.__convert_from_base(LuminanceUnits.Nit)
        return self.__nits

    
    @property
    def nanocandelas_per_square_meter(self) -> float:
        """
        
        """
        if self.__nanocandelas_per_square_meter != None:
            return self.__nanocandelas_per_square_meter
        self.__nanocandelas_per_square_meter = self.__convert_from_base(LuminanceUnits.NanocandelaPerSquareMeter)
        return self.__nanocandelas_per_square_meter

    
    @property
    def microcandelas_per_square_meter(self) -> float:
        """
        
        """
        if self.__microcandelas_per_square_meter != None:
            return self.__microcandelas_per_square_meter
        self.__microcandelas_per_square_meter = self.__convert_from_base(LuminanceUnits.MicrocandelaPerSquareMeter)
        return self.__microcandelas_per_square_meter

    
    @property
    def millicandelas_per_square_meter(self) -> float:
        """
        
        """
        if self.__millicandelas_per_square_meter != None:
            return self.__millicandelas_per_square_meter
        self.__millicandelas_per_square_meter = self.__convert_from_base(LuminanceUnits.MillicandelaPerSquareMeter)
        return self.__millicandelas_per_square_meter

    
    @property
    def centicandelas_per_square_meter(self) -> float:
        """
        
        """
        if self.__centicandelas_per_square_meter != None:
            return self.__centicandelas_per_square_meter
        self.__centicandelas_per_square_meter = self.__convert_from_base(LuminanceUnits.CenticandelaPerSquareMeter)
        return self.__centicandelas_per_square_meter

    
    @property
    def decicandelas_per_square_meter(self) -> float:
        """
        
        """
        if self.__decicandelas_per_square_meter != None:
            return self.__decicandelas_per_square_meter
        self.__decicandelas_per_square_meter = self.__convert_from_base(LuminanceUnits.DecicandelaPerSquareMeter)
        return self.__decicandelas_per_square_meter

    
    @property
    def kilocandelas_per_square_meter(self) -> float:
        """
        
        """
        if self.__kilocandelas_per_square_meter != None:
            return self.__kilocandelas_per_square_meter
        self.__kilocandelas_per_square_meter = self.__convert_from_base(LuminanceUnits.KilocandelaPerSquareMeter)
        return self.__kilocandelas_per_square_meter

    
    def to_string(self, unit: LuminanceUnits = LuminanceUnits.CandelaPerSquareMeter, fractional_digits: int = None) -> str:
        """
        Format the Luminance to a string.
        
        Note: the default format for Luminance is CandelaPerSquareMeter.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the Luminance. Default is 'CandelaPerSquareMeter'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == LuminanceUnits.CandelaPerSquareMeter:
            return f"""{super()._truncate_fraction_digits(self.candelas_per_square_meter, fractional_digits)} Cd/m²"""
        
        if unit == LuminanceUnits.CandelaPerSquareFoot:
            return f"""{super()._truncate_fraction_digits(self.candelas_per_square_foot, fractional_digits)} Cd/ft²"""
        
        if unit == LuminanceUnits.CandelaPerSquareInch:
            return f"""{super()._truncate_fraction_digits(self.candelas_per_square_inch, fractional_digits)} Cd/in²"""
        
        if unit == LuminanceUnits.Nit:
            return f"""{super()._truncate_fraction_digits(self.nits, fractional_digits)} nt"""
        
        if unit == LuminanceUnits.NanocandelaPerSquareMeter:
            return f"""{super()._truncate_fraction_digits(self.nanocandelas_per_square_meter, fractional_digits)} nCd/m²"""
        
        if unit == LuminanceUnits.MicrocandelaPerSquareMeter:
            return f"""{super()._truncate_fraction_digits(self.microcandelas_per_square_meter, fractional_digits)} μCd/m²"""
        
        if unit == LuminanceUnits.MillicandelaPerSquareMeter:
            return f"""{super()._truncate_fraction_digits(self.millicandelas_per_square_meter, fractional_digits)} mCd/m²"""
        
        if unit == LuminanceUnits.CenticandelaPerSquareMeter:
            return f"""{super()._truncate_fraction_digits(self.centicandelas_per_square_meter, fractional_digits)} cCd/m²"""
        
        if unit == LuminanceUnits.DecicandelaPerSquareMeter:
            return f"""{super()._truncate_fraction_digits(self.decicandelas_per_square_meter, fractional_digits)} dCd/m²"""
        
        if unit == LuminanceUnits.KilocandelaPerSquareMeter:
            return f"""{super()._truncate_fraction_digits(self.kilocandelas_per_square_meter, fractional_digits)} kCd/m²"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: LuminanceUnits = LuminanceUnits.CandelaPerSquareMeter) -> str:
        """
        Get Luminance unit abbreviation.
        Note! the default abbreviation for Luminance is CandelaPerSquareMeter.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == LuminanceUnits.CandelaPerSquareMeter:
            return """Cd/m²"""
        
        if unit_abbreviation == LuminanceUnits.CandelaPerSquareFoot:
            return """Cd/ft²"""
        
        if unit_abbreviation == LuminanceUnits.CandelaPerSquareInch:
            return """Cd/in²"""
        
        if unit_abbreviation == LuminanceUnits.Nit:
            return """nt"""
        
        if unit_abbreviation == LuminanceUnits.NanocandelaPerSquareMeter:
            return """nCd/m²"""
        
        if unit_abbreviation == LuminanceUnits.MicrocandelaPerSquareMeter:
            return """μCd/m²"""
        
        if unit_abbreviation == LuminanceUnits.MillicandelaPerSquareMeter:
            return """mCd/m²"""
        
        if unit_abbreviation == LuminanceUnits.CenticandelaPerSquareMeter:
            return """cCd/m²"""
        
        if unit_abbreviation == LuminanceUnits.DecicandelaPerSquareMeter:
            return """dCd/m²"""
        
        if unit_abbreviation == LuminanceUnits.KilocandelaPerSquareMeter:
            return """kCd/m²"""
        
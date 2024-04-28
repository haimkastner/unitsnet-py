from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class CompressibilityUnits(Enum):
        """
            CompressibilityUnits enumeration
        """
        
        InversePascal = 'InversePascal'
        """
            
        """
        
        InverseKilopascal = 'InverseKilopascal'
        """
            
        """
        
        InverseMegapascal = 'InverseMegapascal'
        """
            
        """
        
        InverseAtmosphere = 'InverseAtmosphere'
        """
            
        """
        
        InverseMillibar = 'InverseMillibar'
        """
            
        """
        
        InverseBar = 'InverseBar'
        """
            
        """
        
        InversePoundForcePerSquareInch = 'InversePoundForcePerSquareInch'
        """
            
        """
        

class CompressibilityDto:
    """
    A DTO representation of a Compressibility

    Attributes:
        value (float): The value of the Compressibility.
        unit (CompressibilityUnits): The specific unit that the Compressibility value is representing.
    """

    def __init__(self, value: float, unit: CompressibilityUnits):
        """
        Create a new DTO representation of a Compressibility

        Parameters:
            value (float): The value of the Compressibility.
            unit (CompressibilityUnits): The specific unit that the Compressibility value is representing.
        """
        self.value: float = value
        """
        The value of the Compressibility
        """
        self.unit: CompressibilityUnits = unit
        """
        The specific unit that the Compressibility value is representing
        """

    def to_json(self):
        """
        Get a Compressibility DTO JSON object representing the current unit.

        :return: JSON object represents Compressibility DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "InversePascal"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of Compressibility DTO from a json representation.

        :param data: The Compressibility DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "InversePascal"}
        :return: A new instance of CompressibilityDto.
        :rtype: CompressibilityDto
        """
        return CompressibilityDto(value=data["value"], unit=CompressibilityUnits(data["unit"]))


class Compressibility(AbstractMeasure):
    """
    None

    Args:
        value (float): The value.
        from_unit (CompressibilityUnits): The Compressibility unit to create from, The default unit is InversePascal
    """
    def __init__(self, value: float, from_unit: CompressibilityUnits = CompressibilityUnits.InversePascal):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__inverse_pascals = None
        
        self.__inverse_kilopascals = None
        
        self.__inverse_megapascals = None
        
        self.__inverse_atmospheres = None
        
        self.__inverse_millibars = None
        
        self.__inverse_bars = None
        
        self.__inverse_pounds_force_per_square_inch = None
        

    def convert(self, unit: CompressibilityUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: CompressibilityUnits = CompressibilityUnits.InversePascal) -> CompressibilityDto:
        """
        Get a new instance of Compressibility DTO representing the current unit.

        :param hold_in_unit: The specific Compressibility unit to store the Compressibility value in the DTO representation.
        :type hold_in_unit: CompressibilityUnits
        :return: A new instance of CompressibilityDto.
        :rtype: CompressibilityDto
        """
        return CompressibilityDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: CompressibilityUnits = CompressibilityUnits.InversePascal):
        """
        Get a Compressibility DTO JSON object representing the current unit.

        :param hold_in_unit: The specific Compressibility unit to store the Compressibility value in the DTO representation.
        :type hold_in_unit: CompressibilityUnits
        :return: JSON object represents Compressibility DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "InversePascal"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(compressibility_dto: CompressibilityDto):
        """
        Obtain a new instance of Compressibility from a DTO unit object.

        :param compressibility_dto: The Compressibility DTO representation.
        :type compressibility_dto: CompressibilityDto
        :return: A new instance of Compressibility.
        :rtype: Compressibility
        """
        return Compressibility(compressibility_dto.value, compressibility_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of Compressibility from a DTO unit json representation.

        :param data: The Compressibility DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "InversePascal"}
        :return: A new instance of Compressibility.
        :rtype: Compressibility
        """
        return Compressibility.from_dto(CompressibilityDto.from_json(data))

    def __convert_from_base(self, from_unit: CompressibilityUnits) -> float:
        value = self._value
        
        if from_unit == CompressibilityUnits.InversePascal:
            return (value)
        
        if from_unit == CompressibilityUnits.InverseKilopascal:
            return (value / 1e3)
        
        if from_unit == CompressibilityUnits.InverseMegapascal:
            return (value / 1e6)
        
        if from_unit == CompressibilityUnits.InverseAtmosphere:
            return (value / 101325)
        
        if from_unit == CompressibilityUnits.InverseMillibar:
            return (value / 100)
        
        if from_unit == CompressibilityUnits.InverseBar:
            return (value / 1e5)
        
        if from_unit == CompressibilityUnits.InversePoundForcePerSquareInch:
            return (value / 6.894757293168361e3)
        
        return None


    def __convert_to_base(self, value: float, to_unit: CompressibilityUnits) -> float:
        
        if to_unit == CompressibilityUnits.InversePascal:
            return (value)
        
        if to_unit == CompressibilityUnits.InverseKilopascal:
            return (value * 1e3)
        
        if to_unit == CompressibilityUnits.InverseMegapascal:
            return (value * 1e6)
        
        if to_unit == CompressibilityUnits.InverseAtmosphere:
            return (value * 101325)
        
        if to_unit == CompressibilityUnits.InverseMillibar:
            return (value * 100)
        
        if to_unit == CompressibilityUnits.InverseBar:
            return (value * 1e5)
        
        if to_unit == CompressibilityUnits.InversePoundForcePerSquareInch:
            return (value * 6.894757293168361e3)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_inverse_pascals(inverse_pascals: float):
        """
        Create a new instance of Compressibility from a value in inverse_pascals.

        

        :param meters: The Compressibility value in inverse_pascals.
        :type inverse_pascals: float
        :return: A new instance of Compressibility.
        :rtype: Compressibility
        """
        return Compressibility(inverse_pascals, CompressibilityUnits.InversePascal)

    
    @staticmethod
    def from_inverse_kilopascals(inverse_kilopascals: float):
        """
        Create a new instance of Compressibility from a value in inverse_kilopascals.

        

        :param meters: The Compressibility value in inverse_kilopascals.
        :type inverse_kilopascals: float
        :return: A new instance of Compressibility.
        :rtype: Compressibility
        """
        return Compressibility(inverse_kilopascals, CompressibilityUnits.InverseKilopascal)

    
    @staticmethod
    def from_inverse_megapascals(inverse_megapascals: float):
        """
        Create a new instance of Compressibility from a value in inverse_megapascals.

        

        :param meters: The Compressibility value in inverse_megapascals.
        :type inverse_megapascals: float
        :return: A new instance of Compressibility.
        :rtype: Compressibility
        """
        return Compressibility(inverse_megapascals, CompressibilityUnits.InverseMegapascal)

    
    @staticmethod
    def from_inverse_atmospheres(inverse_atmospheres: float):
        """
        Create a new instance of Compressibility from a value in inverse_atmospheres.

        

        :param meters: The Compressibility value in inverse_atmospheres.
        :type inverse_atmospheres: float
        :return: A new instance of Compressibility.
        :rtype: Compressibility
        """
        return Compressibility(inverse_atmospheres, CompressibilityUnits.InverseAtmosphere)

    
    @staticmethod
    def from_inverse_millibars(inverse_millibars: float):
        """
        Create a new instance of Compressibility from a value in inverse_millibars.

        

        :param meters: The Compressibility value in inverse_millibars.
        :type inverse_millibars: float
        :return: A new instance of Compressibility.
        :rtype: Compressibility
        """
        return Compressibility(inverse_millibars, CompressibilityUnits.InverseMillibar)

    
    @staticmethod
    def from_inverse_bars(inverse_bars: float):
        """
        Create a new instance of Compressibility from a value in inverse_bars.

        

        :param meters: The Compressibility value in inverse_bars.
        :type inverse_bars: float
        :return: A new instance of Compressibility.
        :rtype: Compressibility
        """
        return Compressibility(inverse_bars, CompressibilityUnits.InverseBar)

    
    @staticmethod
    def from_inverse_pounds_force_per_square_inch(inverse_pounds_force_per_square_inch: float):
        """
        Create a new instance of Compressibility from a value in inverse_pounds_force_per_square_inch.

        

        :param meters: The Compressibility value in inverse_pounds_force_per_square_inch.
        :type inverse_pounds_force_per_square_inch: float
        :return: A new instance of Compressibility.
        :rtype: Compressibility
        """
        return Compressibility(inverse_pounds_force_per_square_inch, CompressibilityUnits.InversePoundForcePerSquareInch)

    
    @property
    def inverse_pascals(self) -> float:
        """
        
        """
        if self.__inverse_pascals != None:
            return self.__inverse_pascals
        self.__inverse_pascals = self.__convert_from_base(CompressibilityUnits.InversePascal)
        return self.__inverse_pascals

    
    @property
    def inverse_kilopascals(self) -> float:
        """
        
        """
        if self.__inverse_kilopascals != None:
            return self.__inverse_kilopascals
        self.__inverse_kilopascals = self.__convert_from_base(CompressibilityUnits.InverseKilopascal)
        return self.__inverse_kilopascals

    
    @property
    def inverse_megapascals(self) -> float:
        """
        
        """
        if self.__inverse_megapascals != None:
            return self.__inverse_megapascals
        self.__inverse_megapascals = self.__convert_from_base(CompressibilityUnits.InverseMegapascal)
        return self.__inverse_megapascals

    
    @property
    def inverse_atmospheres(self) -> float:
        """
        
        """
        if self.__inverse_atmospheres != None:
            return self.__inverse_atmospheres
        self.__inverse_atmospheres = self.__convert_from_base(CompressibilityUnits.InverseAtmosphere)
        return self.__inverse_atmospheres

    
    @property
    def inverse_millibars(self) -> float:
        """
        
        """
        if self.__inverse_millibars != None:
            return self.__inverse_millibars
        self.__inverse_millibars = self.__convert_from_base(CompressibilityUnits.InverseMillibar)
        return self.__inverse_millibars

    
    @property
    def inverse_bars(self) -> float:
        """
        
        """
        if self.__inverse_bars != None:
            return self.__inverse_bars
        self.__inverse_bars = self.__convert_from_base(CompressibilityUnits.InverseBar)
        return self.__inverse_bars

    
    @property
    def inverse_pounds_force_per_square_inch(self) -> float:
        """
        
        """
        if self.__inverse_pounds_force_per_square_inch != None:
            return self.__inverse_pounds_force_per_square_inch
        self.__inverse_pounds_force_per_square_inch = self.__convert_from_base(CompressibilityUnits.InversePoundForcePerSquareInch)
        return self.__inverse_pounds_force_per_square_inch

    
    def to_string(self, unit: CompressibilityUnits = CompressibilityUnits.InversePascal, fractional_digits: int = None) -> str:
        """
        Format the Compressibility to a string.
        
        Note: the default format for Compressibility is InversePascal.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the Compressibility. Default is 'InversePascal'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == CompressibilityUnits.InversePascal:
            return f"""{super()._truncate_fraction_digits(self.inverse_pascals, fractional_digits)} Pa⁻¹"""
        
        if unit == CompressibilityUnits.InverseKilopascal:
            return f"""{super()._truncate_fraction_digits(self.inverse_kilopascals, fractional_digits)} kPa⁻¹"""
        
        if unit == CompressibilityUnits.InverseMegapascal:
            return f"""{super()._truncate_fraction_digits(self.inverse_megapascals, fractional_digits)} MPa⁻¹"""
        
        if unit == CompressibilityUnits.InverseAtmosphere:
            return f"""{super()._truncate_fraction_digits(self.inverse_atmospheres, fractional_digits)} atm⁻¹"""
        
        if unit == CompressibilityUnits.InverseMillibar:
            return f"""{super()._truncate_fraction_digits(self.inverse_millibars, fractional_digits)} mbar⁻¹"""
        
        if unit == CompressibilityUnits.InverseBar:
            return f"""{super()._truncate_fraction_digits(self.inverse_bars, fractional_digits)} bar⁻¹"""
        
        if unit == CompressibilityUnits.InversePoundForcePerSquareInch:
            return f"""{super()._truncate_fraction_digits(self.inverse_pounds_force_per_square_inch, fractional_digits)} psi⁻¹"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: CompressibilityUnits = CompressibilityUnits.InversePascal) -> str:
        """
        Get Compressibility unit abbreviation.
        Note! the default abbreviation for Compressibility is InversePascal.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == CompressibilityUnits.InversePascal:
            return """Pa⁻¹"""
        
        if unit_abbreviation == CompressibilityUnits.InverseKilopascal:
            return """kPa⁻¹"""
        
        if unit_abbreviation == CompressibilityUnits.InverseMegapascal:
            return """MPa⁻¹"""
        
        if unit_abbreviation == CompressibilityUnits.InverseAtmosphere:
            return """atm⁻¹"""
        
        if unit_abbreviation == CompressibilityUnits.InverseMillibar:
            return """mbar⁻¹"""
        
        if unit_abbreviation == CompressibilityUnits.InverseBar:
            return """bar⁻¹"""
        
        if unit_abbreviation == CompressibilityUnits.InversePoundForcePerSquareInch:
            return """psi⁻¹"""
        
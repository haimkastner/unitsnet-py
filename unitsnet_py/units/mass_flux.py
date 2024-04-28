from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class MassFluxUnits(Enum):
        """
            MassFluxUnits enumeration
        """
        
        GramPerSecondPerSquareMeter = 'GramPerSecondPerSquareMeter'
        """
            
        """
        
        GramPerSecondPerSquareCentimeter = 'GramPerSecondPerSquareCentimeter'
        """
            
        """
        
        GramPerSecondPerSquareMillimeter = 'GramPerSecondPerSquareMillimeter'
        """
            
        """
        
        GramPerHourPerSquareMeter = 'GramPerHourPerSquareMeter'
        """
            
        """
        
        GramPerHourPerSquareCentimeter = 'GramPerHourPerSquareCentimeter'
        """
            
        """
        
        GramPerHourPerSquareMillimeter = 'GramPerHourPerSquareMillimeter'
        """
            
        """
        
        KilogramPerSecondPerSquareMeter = 'KilogramPerSecondPerSquareMeter'
        """
            
        """
        
        KilogramPerSecondPerSquareCentimeter = 'KilogramPerSecondPerSquareCentimeter'
        """
            
        """
        
        KilogramPerSecondPerSquareMillimeter = 'KilogramPerSecondPerSquareMillimeter'
        """
            
        """
        
        KilogramPerHourPerSquareMeter = 'KilogramPerHourPerSquareMeter'
        """
            
        """
        
        KilogramPerHourPerSquareCentimeter = 'KilogramPerHourPerSquareCentimeter'
        """
            
        """
        
        KilogramPerHourPerSquareMillimeter = 'KilogramPerHourPerSquareMillimeter'
        """
            
        """
        

class MassFluxDto:
    """
    A DTO representation of a MassFlux

    Attributes:
        value (float): The value of the MassFlux.
        unit (MassFluxUnits): The specific unit that the MassFlux value is representing.
    """

    def __init__(self, value: float, unit: MassFluxUnits):
        """
        Create a new DTO representation of a MassFlux

        Parameters:
            value (float): The value of the MassFlux.
            unit (MassFluxUnits): The specific unit that the MassFlux value is representing.
        """
        self.value: float = value
        """
        The value of the MassFlux
        """
        self.unit: MassFluxUnits = unit
        """
        The specific unit that the MassFlux value is representing
        """

    def to_json(self):
        """
        Get a MassFlux DTO JSON object representing the current unit.

        :return: JSON object represents MassFlux DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "KilogramPerSecondPerSquareMeter"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of MassFlux DTO from a json representation.

        :param data: The MassFlux DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "KilogramPerSecondPerSquareMeter"}
        :return: A new instance of MassFluxDto.
        :rtype: MassFluxDto
        """
        return MassFluxDto(value=data["value"], unit=MassFluxUnits(data["unit"]))


class MassFlux(AbstractMeasure):
    """
    Mass flux is the mass flow rate per unit area.

    Args:
        value (float): The value.
        from_unit (MassFluxUnits): The MassFlux unit to create from, The default unit is KilogramPerSecondPerSquareMeter
    """
    def __init__(self, value: float, from_unit: MassFluxUnits = MassFluxUnits.KilogramPerSecondPerSquareMeter):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__grams_per_second_per_square_meter = None
        
        self.__grams_per_second_per_square_centimeter = None
        
        self.__grams_per_second_per_square_millimeter = None
        
        self.__grams_per_hour_per_square_meter = None
        
        self.__grams_per_hour_per_square_centimeter = None
        
        self.__grams_per_hour_per_square_millimeter = None
        
        self.__kilograms_per_second_per_square_meter = None
        
        self.__kilograms_per_second_per_square_centimeter = None
        
        self.__kilograms_per_second_per_square_millimeter = None
        
        self.__kilograms_per_hour_per_square_meter = None
        
        self.__kilograms_per_hour_per_square_centimeter = None
        
        self.__kilograms_per_hour_per_square_millimeter = None
        

    def convert(self, unit: MassFluxUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: MassFluxUnits = MassFluxUnits.KilogramPerSecondPerSquareMeter) -> MassFluxDto:
        """
        Get a new instance of MassFlux DTO representing the current unit.

        :param hold_in_unit: The specific MassFlux unit to store the MassFlux value in the DTO representation.
        :type hold_in_unit: MassFluxUnits
        :return: A new instance of MassFluxDto.
        :rtype: MassFluxDto
        """
        return MassFluxDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: MassFluxUnits = MassFluxUnits.KilogramPerSecondPerSquareMeter):
        """
        Get a MassFlux DTO JSON object representing the current unit.

        :param hold_in_unit: The specific MassFlux unit to store the MassFlux value in the DTO representation.
        :type hold_in_unit: MassFluxUnits
        :return: JSON object represents MassFlux DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "KilogramPerSecondPerSquareMeter"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(mass_flux_dto: MassFluxDto):
        """
        Obtain a new instance of MassFlux from a DTO unit object.

        :param mass_flux_dto: The MassFlux DTO representation.
        :type mass_flux_dto: MassFluxDto
        :return: A new instance of MassFlux.
        :rtype: MassFlux
        """
        return MassFlux(mass_flux_dto.value, mass_flux_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of MassFlux from a DTO unit json representation.

        :param data: The MassFlux DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "KilogramPerSecondPerSquareMeter"}
        :return: A new instance of MassFlux.
        :rtype: MassFlux
        """
        return MassFlux.from_dto(MassFluxDto.from_json(data))

    def __convert_from_base(self, from_unit: MassFluxUnits) -> float:
        value = self._value
        
        if from_unit == MassFluxUnits.GramPerSecondPerSquareMeter:
            return (value * 1e3)
        
        if from_unit == MassFluxUnits.GramPerSecondPerSquareCentimeter:
            return (value * 1e-1)
        
        if from_unit == MassFluxUnits.GramPerSecondPerSquareMillimeter:
            return (value * 1e-3)
        
        if from_unit == MassFluxUnits.GramPerHourPerSquareMeter:
            return (value * 3.6e6)
        
        if from_unit == MassFluxUnits.GramPerHourPerSquareCentimeter:
            return (value * 3.6e2)
        
        if from_unit == MassFluxUnits.GramPerHourPerSquareMillimeter:
            return (value * 3.6e0)
        
        if from_unit == MassFluxUnits.KilogramPerSecondPerSquareMeter:
            return ((value * 1e3) / 1000.0)
        
        if from_unit == MassFluxUnits.KilogramPerSecondPerSquareCentimeter:
            return ((value * 1e-1) / 1000.0)
        
        if from_unit == MassFluxUnits.KilogramPerSecondPerSquareMillimeter:
            return ((value * 1e-3) / 1000.0)
        
        if from_unit == MassFluxUnits.KilogramPerHourPerSquareMeter:
            return ((value * 3.6e6) / 1000.0)
        
        if from_unit == MassFluxUnits.KilogramPerHourPerSquareCentimeter:
            return ((value * 3.6e2) / 1000.0)
        
        if from_unit == MassFluxUnits.KilogramPerHourPerSquareMillimeter:
            return ((value * 3.6e0) / 1000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: MassFluxUnits) -> float:
        
        if to_unit == MassFluxUnits.GramPerSecondPerSquareMeter:
            return (value / 1e3)
        
        if to_unit == MassFluxUnits.GramPerSecondPerSquareCentimeter:
            return (value / 1e-1)
        
        if to_unit == MassFluxUnits.GramPerSecondPerSquareMillimeter:
            return (value / 1e-3)
        
        if to_unit == MassFluxUnits.GramPerHourPerSquareMeter:
            return (value / 3.6e6)
        
        if to_unit == MassFluxUnits.GramPerHourPerSquareCentimeter:
            return (value / 3.6e2)
        
        if to_unit == MassFluxUnits.GramPerHourPerSquareMillimeter:
            return (value / 3.6e0)
        
        if to_unit == MassFluxUnits.KilogramPerSecondPerSquareMeter:
            return ((value / 1e3) * 1000.0)
        
        if to_unit == MassFluxUnits.KilogramPerSecondPerSquareCentimeter:
            return ((value / 1e-1) * 1000.0)
        
        if to_unit == MassFluxUnits.KilogramPerSecondPerSquareMillimeter:
            return ((value / 1e-3) * 1000.0)
        
        if to_unit == MassFluxUnits.KilogramPerHourPerSquareMeter:
            return ((value / 3.6e6) * 1000.0)
        
        if to_unit == MassFluxUnits.KilogramPerHourPerSquareCentimeter:
            return ((value / 3.6e2) * 1000.0)
        
        if to_unit == MassFluxUnits.KilogramPerHourPerSquareMillimeter:
            return ((value / 3.6e0) * 1000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_grams_per_second_per_square_meter(grams_per_second_per_square_meter: float):
        """
        Create a new instance of MassFlux from a value in grams_per_second_per_square_meter.

        

        :param meters: The MassFlux value in grams_per_second_per_square_meter.
        :type grams_per_second_per_square_meter: float
        :return: A new instance of MassFlux.
        :rtype: MassFlux
        """
        return MassFlux(grams_per_second_per_square_meter, MassFluxUnits.GramPerSecondPerSquareMeter)

    
    @staticmethod
    def from_grams_per_second_per_square_centimeter(grams_per_second_per_square_centimeter: float):
        """
        Create a new instance of MassFlux from a value in grams_per_second_per_square_centimeter.

        

        :param meters: The MassFlux value in grams_per_second_per_square_centimeter.
        :type grams_per_second_per_square_centimeter: float
        :return: A new instance of MassFlux.
        :rtype: MassFlux
        """
        return MassFlux(grams_per_second_per_square_centimeter, MassFluxUnits.GramPerSecondPerSquareCentimeter)

    
    @staticmethod
    def from_grams_per_second_per_square_millimeter(grams_per_second_per_square_millimeter: float):
        """
        Create a new instance of MassFlux from a value in grams_per_second_per_square_millimeter.

        

        :param meters: The MassFlux value in grams_per_second_per_square_millimeter.
        :type grams_per_second_per_square_millimeter: float
        :return: A new instance of MassFlux.
        :rtype: MassFlux
        """
        return MassFlux(grams_per_second_per_square_millimeter, MassFluxUnits.GramPerSecondPerSquareMillimeter)

    
    @staticmethod
    def from_grams_per_hour_per_square_meter(grams_per_hour_per_square_meter: float):
        """
        Create a new instance of MassFlux from a value in grams_per_hour_per_square_meter.

        

        :param meters: The MassFlux value in grams_per_hour_per_square_meter.
        :type grams_per_hour_per_square_meter: float
        :return: A new instance of MassFlux.
        :rtype: MassFlux
        """
        return MassFlux(grams_per_hour_per_square_meter, MassFluxUnits.GramPerHourPerSquareMeter)

    
    @staticmethod
    def from_grams_per_hour_per_square_centimeter(grams_per_hour_per_square_centimeter: float):
        """
        Create a new instance of MassFlux from a value in grams_per_hour_per_square_centimeter.

        

        :param meters: The MassFlux value in grams_per_hour_per_square_centimeter.
        :type grams_per_hour_per_square_centimeter: float
        :return: A new instance of MassFlux.
        :rtype: MassFlux
        """
        return MassFlux(grams_per_hour_per_square_centimeter, MassFluxUnits.GramPerHourPerSquareCentimeter)

    
    @staticmethod
    def from_grams_per_hour_per_square_millimeter(grams_per_hour_per_square_millimeter: float):
        """
        Create a new instance of MassFlux from a value in grams_per_hour_per_square_millimeter.

        

        :param meters: The MassFlux value in grams_per_hour_per_square_millimeter.
        :type grams_per_hour_per_square_millimeter: float
        :return: A new instance of MassFlux.
        :rtype: MassFlux
        """
        return MassFlux(grams_per_hour_per_square_millimeter, MassFluxUnits.GramPerHourPerSquareMillimeter)

    
    @staticmethod
    def from_kilograms_per_second_per_square_meter(kilograms_per_second_per_square_meter: float):
        """
        Create a new instance of MassFlux from a value in kilograms_per_second_per_square_meter.

        

        :param meters: The MassFlux value in kilograms_per_second_per_square_meter.
        :type kilograms_per_second_per_square_meter: float
        :return: A new instance of MassFlux.
        :rtype: MassFlux
        """
        return MassFlux(kilograms_per_second_per_square_meter, MassFluxUnits.KilogramPerSecondPerSquareMeter)

    
    @staticmethod
    def from_kilograms_per_second_per_square_centimeter(kilograms_per_second_per_square_centimeter: float):
        """
        Create a new instance of MassFlux from a value in kilograms_per_second_per_square_centimeter.

        

        :param meters: The MassFlux value in kilograms_per_second_per_square_centimeter.
        :type kilograms_per_second_per_square_centimeter: float
        :return: A new instance of MassFlux.
        :rtype: MassFlux
        """
        return MassFlux(kilograms_per_second_per_square_centimeter, MassFluxUnits.KilogramPerSecondPerSquareCentimeter)

    
    @staticmethod
    def from_kilograms_per_second_per_square_millimeter(kilograms_per_second_per_square_millimeter: float):
        """
        Create a new instance of MassFlux from a value in kilograms_per_second_per_square_millimeter.

        

        :param meters: The MassFlux value in kilograms_per_second_per_square_millimeter.
        :type kilograms_per_second_per_square_millimeter: float
        :return: A new instance of MassFlux.
        :rtype: MassFlux
        """
        return MassFlux(kilograms_per_second_per_square_millimeter, MassFluxUnits.KilogramPerSecondPerSquareMillimeter)

    
    @staticmethod
    def from_kilograms_per_hour_per_square_meter(kilograms_per_hour_per_square_meter: float):
        """
        Create a new instance of MassFlux from a value in kilograms_per_hour_per_square_meter.

        

        :param meters: The MassFlux value in kilograms_per_hour_per_square_meter.
        :type kilograms_per_hour_per_square_meter: float
        :return: A new instance of MassFlux.
        :rtype: MassFlux
        """
        return MassFlux(kilograms_per_hour_per_square_meter, MassFluxUnits.KilogramPerHourPerSquareMeter)

    
    @staticmethod
    def from_kilograms_per_hour_per_square_centimeter(kilograms_per_hour_per_square_centimeter: float):
        """
        Create a new instance of MassFlux from a value in kilograms_per_hour_per_square_centimeter.

        

        :param meters: The MassFlux value in kilograms_per_hour_per_square_centimeter.
        :type kilograms_per_hour_per_square_centimeter: float
        :return: A new instance of MassFlux.
        :rtype: MassFlux
        """
        return MassFlux(kilograms_per_hour_per_square_centimeter, MassFluxUnits.KilogramPerHourPerSquareCentimeter)

    
    @staticmethod
    def from_kilograms_per_hour_per_square_millimeter(kilograms_per_hour_per_square_millimeter: float):
        """
        Create a new instance of MassFlux from a value in kilograms_per_hour_per_square_millimeter.

        

        :param meters: The MassFlux value in kilograms_per_hour_per_square_millimeter.
        :type kilograms_per_hour_per_square_millimeter: float
        :return: A new instance of MassFlux.
        :rtype: MassFlux
        """
        return MassFlux(kilograms_per_hour_per_square_millimeter, MassFluxUnits.KilogramPerHourPerSquareMillimeter)

    
    @property
    def grams_per_second_per_square_meter(self) -> float:
        """
        
        """
        if self.__grams_per_second_per_square_meter != None:
            return self.__grams_per_second_per_square_meter
        self.__grams_per_second_per_square_meter = self.__convert_from_base(MassFluxUnits.GramPerSecondPerSquareMeter)
        return self.__grams_per_second_per_square_meter

    
    @property
    def grams_per_second_per_square_centimeter(self) -> float:
        """
        
        """
        if self.__grams_per_second_per_square_centimeter != None:
            return self.__grams_per_second_per_square_centimeter
        self.__grams_per_second_per_square_centimeter = self.__convert_from_base(MassFluxUnits.GramPerSecondPerSquareCentimeter)
        return self.__grams_per_second_per_square_centimeter

    
    @property
    def grams_per_second_per_square_millimeter(self) -> float:
        """
        
        """
        if self.__grams_per_second_per_square_millimeter != None:
            return self.__grams_per_second_per_square_millimeter
        self.__grams_per_second_per_square_millimeter = self.__convert_from_base(MassFluxUnits.GramPerSecondPerSquareMillimeter)
        return self.__grams_per_second_per_square_millimeter

    
    @property
    def grams_per_hour_per_square_meter(self) -> float:
        """
        
        """
        if self.__grams_per_hour_per_square_meter != None:
            return self.__grams_per_hour_per_square_meter
        self.__grams_per_hour_per_square_meter = self.__convert_from_base(MassFluxUnits.GramPerHourPerSquareMeter)
        return self.__grams_per_hour_per_square_meter

    
    @property
    def grams_per_hour_per_square_centimeter(self) -> float:
        """
        
        """
        if self.__grams_per_hour_per_square_centimeter != None:
            return self.__grams_per_hour_per_square_centimeter
        self.__grams_per_hour_per_square_centimeter = self.__convert_from_base(MassFluxUnits.GramPerHourPerSquareCentimeter)
        return self.__grams_per_hour_per_square_centimeter

    
    @property
    def grams_per_hour_per_square_millimeter(self) -> float:
        """
        
        """
        if self.__grams_per_hour_per_square_millimeter != None:
            return self.__grams_per_hour_per_square_millimeter
        self.__grams_per_hour_per_square_millimeter = self.__convert_from_base(MassFluxUnits.GramPerHourPerSquareMillimeter)
        return self.__grams_per_hour_per_square_millimeter

    
    @property
    def kilograms_per_second_per_square_meter(self) -> float:
        """
        
        """
        if self.__kilograms_per_second_per_square_meter != None:
            return self.__kilograms_per_second_per_square_meter
        self.__kilograms_per_second_per_square_meter = self.__convert_from_base(MassFluxUnits.KilogramPerSecondPerSquareMeter)
        return self.__kilograms_per_second_per_square_meter

    
    @property
    def kilograms_per_second_per_square_centimeter(self) -> float:
        """
        
        """
        if self.__kilograms_per_second_per_square_centimeter != None:
            return self.__kilograms_per_second_per_square_centimeter
        self.__kilograms_per_second_per_square_centimeter = self.__convert_from_base(MassFluxUnits.KilogramPerSecondPerSquareCentimeter)
        return self.__kilograms_per_second_per_square_centimeter

    
    @property
    def kilograms_per_second_per_square_millimeter(self) -> float:
        """
        
        """
        if self.__kilograms_per_second_per_square_millimeter != None:
            return self.__kilograms_per_second_per_square_millimeter
        self.__kilograms_per_second_per_square_millimeter = self.__convert_from_base(MassFluxUnits.KilogramPerSecondPerSquareMillimeter)
        return self.__kilograms_per_second_per_square_millimeter

    
    @property
    def kilograms_per_hour_per_square_meter(self) -> float:
        """
        
        """
        if self.__kilograms_per_hour_per_square_meter != None:
            return self.__kilograms_per_hour_per_square_meter
        self.__kilograms_per_hour_per_square_meter = self.__convert_from_base(MassFluxUnits.KilogramPerHourPerSquareMeter)
        return self.__kilograms_per_hour_per_square_meter

    
    @property
    def kilograms_per_hour_per_square_centimeter(self) -> float:
        """
        
        """
        if self.__kilograms_per_hour_per_square_centimeter != None:
            return self.__kilograms_per_hour_per_square_centimeter
        self.__kilograms_per_hour_per_square_centimeter = self.__convert_from_base(MassFluxUnits.KilogramPerHourPerSquareCentimeter)
        return self.__kilograms_per_hour_per_square_centimeter

    
    @property
    def kilograms_per_hour_per_square_millimeter(self) -> float:
        """
        
        """
        if self.__kilograms_per_hour_per_square_millimeter != None:
            return self.__kilograms_per_hour_per_square_millimeter
        self.__kilograms_per_hour_per_square_millimeter = self.__convert_from_base(MassFluxUnits.KilogramPerHourPerSquareMillimeter)
        return self.__kilograms_per_hour_per_square_millimeter

    
    def to_string(self, unit: MassFluxUnits = MassFluxUnits.KilogramPerSecondPerSquareMeter, fractional_digits: int = None) -> str:
        """
        Format the MassFlux to a string.
        
        Note: the default format for MassFlux is KilogramPerSecondPerSquareMeter.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the MassFlux. Default is 'KilogramPerSecondPerSquareMeter'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == MassFluxUnits.GramPerSecondPerSquareMeter:
            return f"""{super()._truncate_fraction_digits(self.grams_per_second_per_square_meter, fractional_digits)} g·s⁻¹·m⁻²"""
        
        if unit == MassFluxUnits.GramPerSecondPerSquareCentimeter:
            return f"""{super()._truncate_fraction_digits(self.grams_per_second_per_square_centimeter, fractional_digits)} g·s⁻¹·cm⁻²"""
        
        if unit == MassFluxUnits.GramPerSecondPerSquareMillimeter:
            return f"""{super()._truncate_fraction_digits(self.grams_per_second_per_square_millimeter, fractional_digits)} g·s⁻¹·mm⁻²"""
        
        if unit == MassFluxUnits.GramPerHourPerSquareMeter:
            return f"""{super()._truncate_fraction_digits(self.grams_per_hour_per_square_meter, fractional_digits)} g·h⁻¹·m⁻²"""
        
        if unit == MassFluxUnits.GramPerHourPerSquareCentimeter:
            return f"""{super()._truncate_fraction_digits(self.grams_per_hour_per_square_centimeter, fractional_digits)} g·h⁻¹·cm⁻²"""
        
        if unit == MassFluxUnits.GramPerHourPerSquareMillimeter:
            return f"""{super()._truncate_fraction_digits(self.grams_per_hour_per_square_millimeter, fractional_digits)} g·h⁻¹·mm⁻²"""
        
        if unit == MassFluxUnits.KilogramPerSecondPerSquareMeter:
            return f"""{super()._truncate_fraction_digits(self.kilograms_per_second_per_square_meter, fractional_digits)} kg·s⁻¹·m⁻²"""
        
        if unit == MassFluxUnits.KilogramPerSecondPerSquareCentimeter:
            return f"""{super()._truncate_fraction_digits(self.kilograms_per_second_per_square_centimeter, fractional_digits)} kg·s⁻¹·cm⁻²"""
        
        if unit == MassFluxUnits.KilogramPerSecondPerSquareMillimeter:
            return f"""{super()._truncate_fraction_digits(self.kilograms_per_second_per_square_millimeter, fractional_digits)} kg·s⁻¹·mm⁻²"""
        
        if unit == MassFluxUnits.KilogramPerHourPerSquareMeter:
            return f"""{super()._truncate_fraction_digits(self.kilograms_per_hour_per_square_meter, fractional_digits)} kg·h⁻¹·m⁻²"""
        
        if unit == MassFluxUnits.KilogramPerHourPerSquareCentimeter:
            return f"""{super()._truncate_fraction_digits(self.kilograms_per_hour_per_square_centimeter, fractional_digits)} kg·h⁻¹·cm⁻²"""
        
        if unit == MassFluxUnits.KilogramPerHourPerSquareMillimeter:
            return f"""{super()._truncate_fraction_digits(self.kilograms_per_hour_per_square_millimeter, fractional_digits)} kg·h⁻¹·mm⁻²"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: MassFluxUnits = MassFluxUnits.KilogramPerSecondPerSquareMeter) -> str:
        """
        Get MassFlux unit abbreviation.
        Note! the default abbreviation for MassFlux is KilogramPerSecondPerSquareMeter.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == MassFluxUnits.GramPerSecondPerSquareMeter:
            return """g·s⁻¹·m⁻²"""
        
        if unit_abbreviation == MassFluxUnits.GramPerSecondPerSquareCentimeter:
            return """g·s⁻¹·cm⁻²"""
        
        if unit_abbreviation == MassFluxUnits.GramPerSecondPerSquareMillimeter:
            return """g·s⁻¹·mm⁻²"""
        
        if unit_abbreviation == MassFluxUnits.GramPerHourPerSquareMeter:
            return """g·h⁻¹·m⁻²"""
        
        if unit_abbreviation == MassFluxUnits.GramPerHourPerSquareCentimeter:
            return """g·h⁻¹·cm⁻²"""
        
        if unit_abbreviation == MassFluxUnits.GramPerHourPerSquareMillimeter:
            return """g·h⁻¹·mm⁻²"""
        
        if unit_abbreviation == MassFluxUnits.KilogramPerSecondPerSquareMeter:
            return """kg·s⁻¹·m⁻²"""
        
        if unit_abbreviation == MassFluxUnits.KilogramPerSecondPerSquareCentimeter:
            return """kg·s⁻¹·cm⁻²"""
        
        if unit_abbreviation == MassFluxUnits.KilogramPerSecondPerSquareMillimeter:
            return """kg·s⁻¹·mm⁻²"""
        
        if unit_abbreviation == MassFluxUnits.KilogramPerHourPerSquareMeter:
            return """kg·h⁻¹·m⁻²"""
        
        if unit_abbreviation == MassFluxUnits.KilogramPerHourPerSquareCentimeter:
            return """kg·h⁻¹·cm⁻²"""
        
        if unit_abbreviation == MassFluxUnits.KilogramPerHourPerSquareMillimeter:
            return """kg·h⁻¹·mm⁻²"""
        
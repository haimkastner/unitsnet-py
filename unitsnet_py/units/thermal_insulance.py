from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class ThermalInsulanceUnits(Enum):
        """
            ThermalInsulanceUnits enumeration
        """
        
        SquareMeterKelvinPerKilowatt = 'SquareMeterKelvinPerKilowatt'
        """
            
        """
        
        SquareMeterKelvinPerWatt = 'SquareMeterKelvinPerWatt'
        """
            
        """
        
        SquareMeterDegreeCelsiusPerWatt = 'SquareMeterDegreeCelsiusPerWatt'
        """
            
        """
        
        SquareCentimeterKelvinPerWatt = 'SquareCentimeterKelvinPerWatt'
        """
            
        """
        
        SquareMillimeterKelvinPerWatt = 'SquareMillimeterKelvinPerWatt'
        """
            
        """
        
        SquareCentimeterHourDegreeCelsiusPerKilocalorie = 'SquareCentimeterHourDegreeCelsiusPerKilocalorie'
        """
            
        """
        
        HourSquareFeetDegreeFahrenheitPerBtu = 'HourSquareFeetDegreeFahrenheitPerBtu'
        """
            
        """
        

class ThermalInsulanceDto:
    """
    A DTO representation of a ThermalInsulance

    Attributes:
        value (float): The value of the ThermalInsulance.
        unit (ThermalInsulanceUnits): The specific unit that the ThermalInsulance value is representing.
    """

    def __init__(self, value: float, unit: ThermalInsulanceUnits):
        """
        Create a new DTO representation of a ThermalInsulance

        Parameters:
            value (float): The value of the ThermalInsulance.
            unit (ThermalInsulanceUnits): The specific unit that the ThermalInsulance value is representing.
        """
        self.value: float = value
        """
        The value of the ThermalInsulance
        """
        self.unit: ThermalInsulanceUnits = unit
        """
        The specific unit that the ThermalInsulance value is representing
        """

    def to_json(self):
        """
        Get a ThermalInsulance DTO JSON object representing the current unit.

        :return: JSON object represents ThermalInsulance DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "SquareMeterKelvinPerKilowatt"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of ThermalInsulance DTO from a json representation.

        :param data: The ThermalInsulance DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "SquareMeterKelvinPerKilowatt"}
        :return: A new instance of ThermalInsulanceDto.
        :rtype: ThermalInsulanceDto
        """
        return ThermalInsulanceDto(value=data["value"], unit=ThermalInsulanceUnits(data["unit"]))


class ThermalInsulance(AbstractMeasure):
    """
    Thermal insulance (R-value) is a measure of a material's resistance to the heat current. It quantifies how effectively a material can resist the transfer of heat through conduction, convection, and radiation. It has the units square metre kelvins per watt (m2⋅K/W) in SI units or square foot degree Fahrenheit–hours per British thermal unit (ft2⋅°F⋅h/Btu) in imperial units. The higher the thermal insulance, the better a material insulates against heat transfer. It is commonly used in construction to assess the insulation properties of materials such as walls, roofs, and insulation products.

    Args:
        value (float): The value.
        from_unit (ThermalInsulanceUnits): The ThermalInsulance unit to create from, The default unit is SquareMeterKelvinPerKilowatt
    """
    def __init__(self, value: float, from_unit: ThermalInsulanceUnits = ThermalInsulanceUnits.SquareMeterKelvinPerKilowatt):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__square_meter_kelvins_per_kilowatt = None
        
        self.__square_meter_kelvins_per_watt = None
        
        self.__square_meter_degrees_celsius_per_watt = None
        
        self.__square_centimeter_kelvins_per_watt = None
        
        self.__square_millimeter_kelvins_per_watt = None
        
        self.__square_centimeter_hour_degrees_celsius_per_kilocalorie = None
        
        self.__hour_square_feet_degrees_fahrenheit_per_btu = None
        

    def convert(self, unit: ThermalInsulanceUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: ThermalInsulanceUnits = ThermalInsulanceUnits.SquareMeterKelvinPerKilowatt) -> ThermalInsulanceDto:
        """
        Get a new instance of ThermalInsulance DTO representing the current unit.

        :param hold_in_unit: The specific ThermalInsulance unit to store the ThermalInsulance value in the DTO representation.
        :type hold_in_unit: ThermalInsulanceUnits
        :return: A new instance of ThermalInsulanceDto.
        :rtype: ThermalInsulanceDto
        """
        return ThermalInsulanceDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: ThermalInsulanceUnits = ThermalInsulanceUnits.SquareMeterKelvinPerKilowatt):
        """
        Get a ThermalInsulance DTO JSON object representing the current unit.

        :param hold_in_unit: The specific ThermalInsulance unit to store the ThermalInsulance value in the DTO representation.
        :type hold_in_unit: ThermalInsulanceUnits
        :return: JSON object represents ThermalInsulance DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "SquareMeterKelvinPerKilowatt"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(thermal_insulance_dto: ThermalInsulanceDto):
        """
        Obtain a new instance of ThermalInsulance from a DTO unit object.

        :param thermal_insulance_dto: The ThermalInsulance DTO representation.
        :type thermal_insulance_dto: ThermalInsulanceDto
        :return: A new instance of ThermalInsulance.
        :rtype: ThermalInsulance
        """
        return ThermalInsulance(thermal_insulance_dto.value, thermal_insulance_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of ThermalInsulance from a DTO unit json representation.

        :param data: The ThermalInsulance DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "SquareMeterKelvinPerKilowatt"}
        :return: A new instance of ThermalInsulance.
        :rtype: ThermalInsulance
        """
        return ThermalInsulance.from_dto(ThermalInsulanceDto.from_json(data))

    def __convert_from_base(self, from_unit: ThermalInsulanceUnits) -> float:
        value = self._value
        
        if from_unit == ThermalInsulanceUnits.SquareMeterKelvinPerKilowatt:
            return (value)
        
        if from_unit == ThermalInsulanceUnits.SquareMeterKelvinPerWatt:
            return (value / 1000)
        
        if from_unit == ThermalInsulanceUnits.SquareMeterDegreeCelsiusPerWatt:
            return (value / 1000.0)
        
        if from_unit == ThermalInsulanceUnits.SquareCentimeterKelvinPerWatt:
            return (value / 0.1)
        
        if from_unit == ThermalInsulanceUnits.SquareMillimeterKelvinPerWatt:
            return (value / 0.001)
        
        if from_unit == ThermalInsulanceUnits.SquareCentimeterHourDegreeCelsiusPerKilocalorie:
            return (value * 4.184 / (0.0001 * 3600))
        
        if from_unit == ThermalInsulanceUnits.HourSquareFeetDegreeFahrenheitPerBtu:
            return (value * (1055.05585262 * 1.8) / (1000 * 0.3048 * 0.3048 * 3600))
        
        return None


    def __convert_to_base(self, value: float, to_unit: ThermalInsulanceUnits) -> float:
        
        if to_unit == ThermalInsulanceUnits.SquareMeterKelvinPerKilowatt:
            return (value)
        
        if to_unit == ThermalInsulanceUnits.SquareMeterKelvinPerWatt:
            return (value * 1000)
        
        if to_unit == ThermalInsulanceUnits.SquareMeterDegreeCelsiusPerWatt:
            return (value * 1000.0)
        
        if to_unit == ThermalInsulanceUnits.SquareCentimeterKelvinPerWatt:
            return (value * 0.1)
        
        if to_unit == ThermalInsulanceUnits.SquareMillimeterKelvinPerWatt:
            return (value * 0.001)
        
        if to_unit == ThermalInsulanceUnits.SquareCentimeterHourDegreeCelsiusPerKilocalorie:
            return (value * (0.0001 * 3600) / 4.184)
        
        if to_unit == ThermalInsulanceUnits.HourSquareFeetDegreeFahrenheitPerBtu:
            return (value * (1000 * 0.3048 * 0.3048 * 3600) / (1055.05585262 * 1.8))
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_square_meter_kelvins_per_kilowatt(square_meter_kelvins_per_kilowatt: float):
        """
        Create a new instance of ThermalInsulance from a value in square_meter_kelvins_per_kilowatt.

        

        :param meters: The ThermalInsulance value in square_meter_kelvins_per_kilowatt.
        :type square_meter_kelvins_per_kilowatt: float
        :return: A new instance of ThermalInsulance.
        :rtype: ThermalInsulance
        """
        return ThermalInsulance(square_meter_kelvins_per_kilowatt, ThermalInsulanceUnits.SquareMeterKelvinPerKilowatt)

    
    @staticmethod
    def from_square_meter_kelvins_per_watt(square_meter_kelvins_per_watt: float):
        """
        Create a new instance of ThermalInsulance from a value in square_meter_kelvins_per_watt.

        

        :param meters: The ThermalInsulance value in square_meter_kelvins_per_watt.
        :type square_meter_kelvins_per_watt: float
        :return: A new instance of ThermalInsulance.
        :rtype: ThermalInsulance
        """
        return ThermalInsulance(square_meter_kelvins_per_watt, ThermalInsulanceUnits.SquareMeterKelvinPerWatt)

    
    @staticmethod
    def from_square_meter_degrees_celsius_per_watt(square_meter_degrees_celsius_per_watt: float):
        """
        Create a new instance of ThermalInsulance from a value in square_meter_degrees_celsius_per_watt.

        

        :param meters: The ThermalInsulance value in square_meter_degrees_celsius_per_watt.
        :type square_meter_degrees_celsius_per_watt: float
        :return: A new instance of ThermalInsulance.
        :rtype: ThermalInsulance
        """
        return ThermalInsulance(square_meter_degrees_celsius_per_watt, ThermalInsulanceUnits.SquareMeterDegreeCelsiusPerWatt)

    
    @staticmethod
    def from_square_centimeter_kelvins_per_watt(square_centimeter_kelvins_per_watt: float):
        """
        Create a new instance of ThermalInsulance from a value in square_centimeter_kelvins_per_watt.

        

        :param meters: The ThermalInsulance value in square_centimeter_kelvins_per_watt.
        :type square_centimeter_kelvins_per_watt: float
        :return: A new instance of ThermalInsulance.
        :rtype: ThermalInsulance
        """
        return ThermalInsulance(square_centimeter_kelvins_per_watt, ThermalInsulanceUnits.SquareCentimeterKelvinPerWatt)

    
    @staticmethod
    def from_square_millimeter_kelvins_per_watt(square_millimeter_kelvins_per_watt: float):
        """
        Create a new instance of ThermalInsulance from a value in square_millimeter_kelvins_per_watt.

        

        :param meters: The ThermalInsulance value in square_millimeter_kelvins_per_watt.
        :type square_millimeter_kelvins_per_watt: float
        :return: A new instance of ThermalInsulance.
        :rtype: ThermalInsulance
        """
        return ThermalInsulance(square_millimeter_kelvins_per_watt, ThermalInsulanceUnits.SquareMillimeterKelvinPerWatt)

    
    @staticmethod
    def from_square_centimeter_hour_degrees_celsius_per_kilocalorie(square_centimeter_hour_degrees_celsius_per_kilocalorie: float):
        """
        Create a new instance of ThermalInsulance from a value in square_centimeter_hour_degrees_celsius_per_kilocalorie.

        

        :param meters: The ThermalInsulance value in square_centimeter_hour_degrees_celsius_per_kilocalorie.
        :type square_centimeter_hour_degrees_celsius_per_kilocalorie: float
        :return: A new instance of ThermalInsulance.
        :rtype: ThermalInsulance
        """
        return ThermalInsulance(square_centimeter_hour_degrees_celsius_per_kilocalorie, ThermalInsulanceUnits.SquareCentimeterHourDegreeCelsiusPerKilocalorie)

    
    @staticmethod
    def from_hour_square_feet_degrees_fahrenheit_per_btu(hour_square_feet_degrees_fahrenheit_per_btu: float):
        """
        Create a new instance of ThermalInsulance from a value in hour_square_feet_degrees_fahrenheit_per_btu.

        

        :param meters: The ThermalInsulance value in hour_square_feet_degrees_fahrenheit_per_btu.
        :type hour_square_feet_degrees_fahrenheit_per_btu: float
        :return: A new instance of ThermalInsulance.
        :rtype: ThermalInsulance
        """
        return ThermalInsulance(hour_square_feet_degrees_fahrenheit_per_btu, ThermalInsulanceUnits.HourSquareFeetDegreeFahrenheitPerBtu)

    
    @property
    def square_meter_kelvins_per_kilowatt(self) -> float:
        """
        
        """
        if self.__square_meter_kelvins_per_kilowatt != None:
            return self.__square_meter_kelvins_per_kilowatt
        self.__square_meter_kelvins_per_kilowatt = self.__convert_from_base(ThermalInsulanceUnits.SquareMeterKelvinPerKilowatt)
        return self.__square_meter_kelvins_per_kilowatt

    
    @property
    def square_meter_kelvins_per_watt(self) -> float:
        """
        
        """
        if self.__square_meter_kelvins_per_watt != None:
            return self.__square_meter_kelvins_per_watt
        self.__square_meter_kelvins_per_watt = self.__convert_from_base(ThermalInsulanceUnits.SquareMeterKelvinPerWatt)
        return self.__square_meter_kelvins_per_watt

    
    @property
    def square_meter_degrees_celsius_per_watt(self) -> float:
        """
        
        """
        if self.__square_meter_degrees_celsius_per_watt != None:
            return self.__square_meter_degrees_celsius_per_watt
        self.__square_meter_degrees_celsius_per_watt = self.__convert_from_base(ThermalInsulanceUnits.SquareMeterDegreeCelsiusPerWatt)
        return self.__square_meter_degrees_celsius_per_watt

    
    @property
    def square_centimeter_kelvins_per_watt(self) -> float:
        """
        
        """
        if self.__square_centimeter_kelvins_per_watt != None:
            return self.__square_centimeter_kelvins_per_watt
        self.__square_centimeter_kelvins_per_watt = self.__convert_from_base(ThermalInsulanceUnits.SquareCentimeterKelvinPerWatt)
        return self.__square_centimeter_kelvins_per_watt

    
    @property
    def square_millimeter_kelvins_per_watt(self) -> float:
        """
        
        """
        if self.__square_millimeter_kelvins_per_watt != None:
            return self.__square_millimeter_kelvins_per_watt
        self.__square_millimeter_kelvins_per_watt = self.__convert_from_base(ThermalInsulanceUnits.SquareMillimeterKelvinPerWatt)
        return self.__square_millimeter_kelvins_per_watt

    
    @property
    def square_centimeter_hour_degrees_celsius_per_kilocalorie(self) -> float:
        """
        
        """
        if self.__square_centimeter_hour_degrees_celsius_per_kilocalorie != None:
            return self.__square_centimeter_hour_degrees_celsius_per_kilocalorie
        self.__square_centimeter_hour_degrees_celsius_per_kilocalorie = self.__convert_from_base(ThermalInsulanceUnits.SquareCentimeterHourDegreeCelsiusPerKilocalorie)
        return self.__square_centimeter_hour_degrees_celsius_per_kilocalorie

    
    @property
    def hour_square_feet_degrees_fahrenheit_per_btu(self) -> float:
        """
        
        """
        if self.__hour_square_feet_degrees_fahrenheit_per_btu != None:
            return self.__hour_square_feet_degrees_fahrenheit_per_btu
        self.__hour_square_feet_degrees_fahrenheit_per_btu = self.__convert_from_base(ThermalInsulanceUnits.HourSquareFeetDegreeFahrenheitPerBtu)
        return self.__hour_square_feet_degrees_fahrenheit_per_btu

    
    def to_string(self, unit: ThermalInsulanceUnits = ThermalInsulanceUnits.SquareMeterKelvinPerKilowatt, fractional_digits: int = None) -> str:
        """
        Format the ThermalInsulance to a string.
        
        Note: the default format for ThermalInsulance is SquareMeterKelvinPerKilowatt.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the ThermalInsulance. Default is 'SquareMeterKelvinPerKilowatt'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == ThermalInsulanceUnits.SquareMeterKelvinPerKilowatt:
            return f"""{super()._truncate_fraction_digits(self.square_meter_kelvins_per_kilowatt, fractional_digits)} m²K/kW"""
        
        if unit == ThermalInsulanceUnits.SquareMeterKelvinPerWatt:
            return f"""{super()._truncate_fraction_digits(self.square_meter_kelvins_per_watt, fractional_digits)} m²K/W"""
        
        if unit == ThermalInsulanceUnits.SquareMeterDegreeCelsiusPerWatt:
            return f"""{super()._truncate_fraction_digits(self.square_meter_degrees_celsius_per_watt, fractional_digits)} m²°C/W"""
        
        if unit == ThermalInsulanceUnits.SquareCentimeterKelvinPerWatt:
            return f"""{super()._truncate_fraction_digits(self.square_centimeter_kelvins_per_watt, fractional_digits)} cm²K/W"""
        
        if unit == ThermalInsulanceUnits.SquareMillimeterKelvinPerWatt:
            return f"""{super()._truncate_fraction_digits(self.square_millimeter_kelvins_per_watt, fractional_digits)} mm²K/W"""
        
        if unit == ThermalInsulanceUnits.SquareCentimeterHourDegreeCelsiusPerKilocalorie:
            return f"""{super()._truncate_fraction_digits(self.square_centimeter_hour_degrees_celsius_per_kilocalorie, fractional_digits)} cm²Hr°C/kcal"""
        
        if unit == ThermalInsulanceUnits.HourSquareFeetDegreeFahrenheitPerBtu:
            return f"""{super()._truncate_fraction_digits(self.hour_square_feet_degrees_fahrenheit_per_btu, fractional_digits)} Hrft²°F/Btu"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: ThermalInsulanceUnits = ThermalInsulanceUnits.SquareMeterKelvinPerKilowatt) -> str:
        """
        Get ThermalInsulance unit abbreviation.
        Note! the default abbreviation for ThermalInsulance is SquareMeterKelvinPerKilowatt.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == ThermalInsulanceUnits.SquareMeterKelvinPerKilowatt:
            return """m²K/kW"""
        
        if unit_abbreviation == ThermalInsulanceUnits.SquareMeterKelvinPerWatt:
            return """m²K/W"""
        
        if unit_abbreviation == ThermalInsulanceUnits.SquareMeterDegreeCelsiusPerWatt:
            return """m²°C/W"""
        
        if unit_abbreviation == ThermalInsulanceUnits.SquareCentimeterKelvinPerWatt:
            return """cm²K/W"""
        
        if unit_abbreviation == ThermalInsulanceUnits.SquareMillimeterKelvinPerWatt:
            return """mm²K/W"""
        
        if unit_abbreviation == ThermalInsulanceUnits.SquareCentimeterHourDegreeCelsiusPerKilocalorie:
            return """cm²Hr°C/kcal"""
        
        if unit_abbreviation == ThermalInsulanceUnits.HourSquareFeetDegreeFahrenheitPerBtu:
            return """Hrft²°F/Btu"""
        
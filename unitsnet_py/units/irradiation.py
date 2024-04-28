from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class IrradiationUnits(Enum):
        """
            IrradiationUnits enumeration
        """
        
        JoulePerSquareMeter = 'JoulePerSquareMeter'
        """
            
        """
        
        JoulePerSquareCentimeter = 'JoulePerSquareCentimeter'
        """
            
        """
        
        JoulePerSquareMillimeter = 'JoulePerSquareMillimeter'
        """
            
        """
        
        WattHourPerSquareMeter = 'WattHourPerSquareMeter'
        """
            
        """
        
        BtuPerSquareFoot = 'BtuPerSquareFoot'
        """
            
        """
        
        KilojoulePerSquareMeter = 'KilojoulePerSquareMeter'
        """
            
        """
        
        MillijoulePerSquareCentimeter = 'MillijoulePerSquareCentimeter'
        """
            
        """
        
        KilowattHourPerSquareMeter = 'KilowattHourPerSquareMeter'
        """
            
        """
        
        KilobtuPerSquareFoot = 'KilobtuPerSquareFoot'
        """
            
        """
        

class IrradiationDto:
    """
    A DTO representation of a Irradiation

    Attributes:
        value (float): The value of the Irradiation.
        unit (IrradiationUnits): The specific unit that the Irradiation value is representing.
    """

    def __init__(self, value: float, unit: IrradiationUnits):
        """
        Create a new DTO representation of a Irradiation

        Parameters:
            value (float): The value of the Irradiation.
            unit (IrradiationUnits): The specific unit that the Irradiation value is representing.
        """
        self.value: float = value
        """
        The value of the Irradiation
        """
        self.unit: IrradiationUnits = unit
        """
        The specific unit that the Irradiation value is representing
        """

    def to_json(self):
        """
        Get a Irradiation DTO JSON object representing the current unit.

        :return: JSON object represents Irradiation DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "JoulePerSquareMeter"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of Irradiation DTO from a json representation.

        :param data: The Irradiation DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "JoulePerSquareMeter"}
        :return: A new instance of IrradiationDto.
        :rtype: IrradiationDto
        """
        return IrradiationDto(value=data["value"], unit=IrradiationUnits(data["unit"]))


class Irradiation(AbstractMeasure):
    """
    Irradiation is the process by which an object is exposed to radiation. The exposure can originate from various sources, including natural sources.

    Args:
        value (float): The value.
        from_unit (IrradiationUnits): The Irradiation unit to create from, The default unit is JoulePerSquareMeter
    """
    def __init__(self, value: float, from_unit: IrradiationUnits = IrradiationUnits.JoulePerSquareMeter):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__joules_per_square_meter = None
        
        self.__joules_per_square_centimeter = None
        
        self.__joules_per_square_millimeter = None
        
        self.__watt_hours_per_square_meter = None
        
        self.__btus_per_square_foot = None
        
        self.__kilojoules_per_square_meter = None
        
        self.__millijoules_per_square_centimeter = None
        
        self.__kilowatt_hours_per_square_meter = None
        
        self.__kilobtus_per_square_foot = None
        

    def convert(self, unit: IrradiationUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: IrradiationUnits = IrradiationUnits.JoulePerSquareMeter) -> IrradiationDto:
        """
        Get a new instance of Irradiation DTO representing the current unit.

        :param hold_in_unit: The specific Irradiation unit to store the Irradiation value in the DTO representation.
        :type hold_in_unit: IrradiationUnits
        :return: A new instance of IrradiationDto.
        :rtype: IrradiationDto
        """
        return IrradiationDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: IrradiationUnits = IrradiationUnits.JoulePerSquareMeter):
        """
        Get a Irradiation DTO JSON object representing the current unit.

        :param hold_in_unit: The specific Irradiation unit to store the Irradiation value in the DTO representation.
        :type hold_in_unit: IrradiationUnits
        :return: JSON object represents Irradiation DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "JoulePerSquareMeter"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(irradiation_dto: IrradiationDto):
        """
        Obtain a new instance of Irradiation from a DTO unit object.

        :param irradiation_dto: The Irradiation DTO representation.
        :type irradiation_dto: IrradiationDto
        :return: A new instance of Irradiation.
        :rtype: Irradiation
        """
        return Irradiation(irradiation_dto.value, irradiation_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of Irradiation from a DTO unit json representation.

        :param data: The Irradiation DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "JoulePerSquareMeter"}
        :return: A new instance of Irradiation.
        :rtype: Irradiation
        """
        return Irradiation.from_dto(IrradiationDto.from_json(data))

    def __convert_from_base(self, from_unit: IrradiationUnits) -> float:
        value = self._value
        
        if from_unit == IrradiationUnits.JoulePerSquareMeter:
            return (value)
        
        if from_unit == IrradiationUnits.JoulePerSquareCentimeter:
            return (value / 1e4)
        
        if from_unit == IrradiationUnits.JoulePerSquareMillimeter:
            return (value / 1e6)
        
        if from_unit == IrradiationUnits.WattHourPerSquareMeter:
            return (value / 3600)
        
        if from_unit == IrradiationUnits.BtuPerSquareFoot:
            return (value / (52752792631 / 4645152))
        
        if from_unit == IrradiationUnits.KilojoulePerSquareMeter:
            return ((value) / 1000.0)
        
        if from_unit == IrradiationUnits.MillijoulePerSquareCentimeter:
            return ((value / 1e4) / 0.001)
        
        if from_unit == IrradiationUnits.KilowattHourPerSquareMeter:
            return ((value / 3600) / 1000.0)
        
        if from_unit == IrradiationUnits.KilobtuPerSquareFoot:
            return ((value / (52752792631 / 4645152)) / 1000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: IrradiationUnits) -> float:
        
        if to_unit == IrradiationUnits.JoulePerSquareMeter:
            return (value)
        
        if to_unit == IrradiationUnits.JoulePerSquareCentimeter:
            return (value * 1e4)
        
        if to_unit == IrradiationUnits.JoulePerSquareMillimeter:
            return (value * 1e6)
        
        if to_unit == IrradiationUnits.WattHourPerSquareMeter:
            return (value * 3600)
        
        if to_unit == IrradiationUnits.BtuPerSquareFoot:
            return (value * (52752792631 / 4645152))
        
        if to_unit == IrradiationUnits.KilojoulePerSquareMeter:
            return ((value) * 1000.0)
        
        if to_unit == IrradiationUnits.MillijoulePerSquareCentimeter:
            return ((value * 1e4) * 0.001)
        
        if to_unit == IrradiationUnits.KilowattHourPerSquareMeter:
            return ((value * 3600) * 1000.0)
        
        if to_unit == IrradiationUnits.KilobtuPerSquareFoot:
            return ((value * (52752792631 / 4645152)) * 1000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_joules_per_square_meter(joules_per_square_meter: float):
        """
        Create a new instance of Irradiation from a value in joules_per_square_meter.

        

        :param meters: The Irradiation value in joules_per_square_meter.
        :type joules_per_square_meter: float
        :return: A new instance of Irradiation.
        :rtype: Irradiation
        """
        return Irradiation(joules_per_square_meter, IrradiationUnits.JoulePerSquareMeter)

    
    @staticmethod
    def from_joules_per_square_centimeter(joules_per_square_centimeter: float):
        """
        Create a new instance of Irradiation from a value in joules_per_square_centimeter.

        

        :param meters: The Irradiation value in joules_per_square_centimeter.
        :type joules_per_square_centimeter: float
        :return: A new instance of Irradiation.
        :rtype: Irradiation
        """
        return Irradiation(joules_per_square_centimeter, IrradiationUnits.JoulePerSquareCentimeter)

    
    @staticmethod
    def from_joules_per_square_millimeter(joules_per_square_millimeter: float):
        """
        Create a new instance of Irradiation from a value in joules_per_square_millimeter.

        

        :param meters: The Irradiation value in joules_per_square_millimeter.
        :type joules_per_square_millimeter: float
        :return: A new instance of Irradiation.
        :rtype: Irradiation
        """
        return Irradiation(joules_per_square_millimeter, IrradiationUnits.JoulePerSquareMillimeter)

    
    @staticmethod
    def from_watt_hours_per_square_meter(watt_hours_per_square_meter: float):
        """
        Create a new instance of Irradiation from a value in watt_hours_per_square_meter.

        

        :param meters: The Irradiation value in watt_hours_per_square_meter.
        :type watt_hours_per_square_meter: float
        :return: A new instance of Irradiation.
        :rtype: Irradiation
        """
        return Irradiation(watt_hours_per_square_meter, IrradiationUnits.WattHourPerSquareMeter)

    
    @staticmethod
    def from_btus_per_square_foot(btus_per_square_foot: float):
        """
        Create a new instance of Irradiation from a value in btus_per_square_foot.

        

        :param meters: The Irradiation value in btus_per_square_foot.
        :type btus_per_square_foot: float
        :return: A new instance of Irradiation.
        :rtype: Irradiation
        """
        return Irradiation(btus_per_square_foot, IrradiationUnits.BtuPerSquareFoot)

    
    @staticmethod
    def from_kilojoules_per_square_meter(kilojoules_per_square_meter: float):
        """
        Create a new instance of Irradiation from a value in kilojoules_per_square_meter.

        

        :param meters: The Irradiation value in kilojoules_per_square_meter.
        :type kilojoules_per_square_meter: float
        :return: A new instance of Irradiation.
        :rtype: Irradiation
        """
        return Irradiation(kilojoules_per_square_meter, IrradiationUnits.KilojoulePerSquareMeter)

    
    @staticmethod
    def from_millijoules_per_square_centimeter(millijoules_per_square_centimeter: float):
        """
        Create a new instance of Irradiation from a value in millijoules_per_square_centimeter.

        

        :param meters: The Irradiation value in millijoules_per_square_centimeter.
        :type millijoules_per_square_centimeter: float
        :return: A new instance of Irradiation.
        :rtype: Irradiation
        """
        return Irradiation(millijoules_per_square_centimeter, IrradiationUnits.MillijoulePerSquareCentimeter)

    
    @staticmethod
    def from_kilowatt_hours_per_square_meter(kilowatt_hours_per_square_meter: float):
        """
        Create a new instance of Irradiation from a value in kilowatt_hours_per_square_meter.

        

        :param meters: The Irradiation value in kilowatt_hours_per_square_meter.
        :type kilowatt_hours_per_square_meter: float
        :return: A new instance of Irradiation.
        :rtype: Irradiation
        """
        return Irradiation(kilowatt_hours_per_square_meter, IrradiationUnits.KilowattHourPerSquareMeter)

    
    @staticmethod
    def from_kilobtus_per_square_foot(kilobtus_per_square_foot: float):
        """
        Create a new instance of Irradiation from a value in kilobtus_per_square_foot.

        

        :param meters: The Irradiation value in kilobtus_per_square_foot.
        :type kilobtus_per_square_foot: float
        :return: A new instance of Irradiation.
        :rtype: Irradiation
        """
        return Irradiation(kilobtus_per_square_foot, IrradiationUnits.KilobtuPerSquareFoot)

    
    @property
    def joules_per_square_meter(self) -> float:
        """
        
        """
        if self.__joules_per_square_meter != None:
            return self.__joules_per_square_meter
        self.__joules_per_square_meter = self.__convert_from_base(IrradiationUnits.JoulePerSquareMeter)
        return self.__joules_per_square_meter

    
    @property
    def joules_per_square_centimeter(self) -> float:
        """
        
        """
        if self.__joules_per_square_centimeter != None:
            return self.__joules_per_square_centimeter
        self.__joules_per_square_centimeter = self.__convert_from_base(IrradiationUnits.JoulePerSquareCentimeter)
        return self.__joules_per_square_centimeter

    
    @property
    def joules_per_square_millimeter(self) -> float:
        """
        
        """
        if self.__joules_per_square_millimeter != None:
            return self.__joules_per_square_millimeter
        self.__joules_per_square_millimeter = self.__convert_from_base(IrradiationUnits.JoulePerSquareMillimeter)
        return self.__joules_per_square_millimeter

    
    @property
    def watt_hours_per_square_meter(self) -> float:
        """
        
        """
        if self.__watt_hours_per_square_meter != None:
            return self.__watt_hours_per_square_meter
        self.__watt_hours_per_square_meter = self.__convert_from_base(IrradiationUnits.WattHourPerSquareMeter)
        return self.__watt_hours_per_square_meter

    
    @property
    def btus_per_square_foot(self) -> float:
        """
        
        """
        if self.__btus_per_square_foot != None:
            return self.__btus_per_square_foot
        self.__btus_per_square_foot = self.__convert_from_base(IrradiationUnits.BtuPerSquareFoot)
        return self.__btus_per_square_foot

    
    @property
    def kilojoules_per_square_meter(self) -> float:
        """
        
        """
        if self.__kilojoules_per_square_meter != None:
            return self.__kilojoules_per_square_meter
        self.__kilojoules_per_square_meter = self.__convert_from_base(IrradiationUnits.KilojoulePerSquareMeter)
        return self.__kilojoules_per_square_meter

    
    @property
    def millijoules_per_square_centimeter(self) -> float:
        """
        
        """
        if self.__millijoules_per_square_centimeter != None:
            return self.__millijoules_per_square_centimeter
        self.__millijoules_per_square_centimeter = self.__convert_from_base(IrradiationUnits.MillijoulePerSquareCentimeter)
        return self.__millijoules_per_square_centimeter

    
    @property
    def kilowatt_hours_per_square_meter(self) -> float:
        """
        
        """
        if self.__kilowatt_hours_per_square_meter != None:
            return self.__kilowatt_hours_per_square_meter
        self.__kilowatt_hours_per_square_meter = self.__convert_from_base(IrradiationUnits.KilowattHourPerSquareMeter)
        return self.__kilowatt_hours_per_square_meter

    
    @property
    def kilobtus_per_square_foot(self) -> float:
        """
        
        """
        if self.__kilobtus_per_square_foot != None:
            return self.__kilobtus_per_square_foot
        self.__kilobtus_per_square_foot = self.__convert_from_base(IrradiationUnits.KilobtuPerSquareFoot)
        return self.__kilobtus_per_square_foot

    
    def to_string(self, unit: IrradiationUnits = IrradiationUnits.JoulePerSquareMeter, fractional_digits: int = None) -> str:
        """
        Format the Irradiation to a string.
        
        Note: the default format for Irradiation is JoulePerSquareMeter.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the Irradiation. Default is 'JoulePerSquareMeter'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == IrradiationUnits.JoulePerSquareMeter:
            return f"""{super()._truncate_fraction_digits(self.joules_per_square_meter, fractional_digits)} J/m²"""
        
        if unit == IrradiationUnits.JoulePerSquareCentimeter:
            return f"""{super()._truncate_fraction_digits(self.joules_per_square_centimeter, fractional_digits)} J/cm²"""
        
        if unit == IrradiationUnits.JoulePerSquareMillimeter:
            return f"""{super()._truncate_fraction_digits(self.joules_per_square_millimeter, fractional_digits)} J/mm²"""
        
        if unit == IrradiationUnits.WattHourPerSquareMeter:
            return f"""{super()._truncate_fraction_digits(self.watt_hours_per_square_meter, fractional_digits)} Wh/m²"""
        
        if unit == IrradiationUnits.BtuPerSquareFoot:
            return f"""{super()._truncate_fraction_digits(self.btus_per_square_foot, fractional_digits)} Btu/ft²"""
        
        if unit == IrradiationUnits.KilojoulePerSquareMeter:
            return f"""{super()._truncate_fraction_digits(self.kilojoules_per_square_meter, fractional_digits)} kJ/m²"""
        
        if unit == IrradiationUnits.MillijoulePerSquareCentimeter:
            return f"""{super()._truncate_fraction_digits(self.millijoules_per_square_centimeter, fractional_digits)} mJ/cm²"""
        
        if unit == IrradiationUnits.KilowattHourPerSquareMeter:
            return f"""{super()._truncate_fraction_digits(self.kilowatt_hours_per_square_meter, fractional_digits)} kWh/m²"""
        
        if unit == IrradiationUnits.KilobtuPerSquareFoot:
            return f"""{super()._truncate_fraction_digits(self.kilobtus_per_square_foot, fractional_digits)} kBtu/ft²"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: IrradiationUnits = IrradiationUnits.JoulePerSquareMeter) -> str:
        """
        Get Irradiation unit abbreviation.
        Note! the default abbreviation for Irradiation is JoulePerSquareMeter.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == IrradiationUnits.JoulePerSquareMeter:
            return """J/m²"""
        
        if unit_abbreviation == IrradiationUnits.JoulePerSquareCentimeter:
            return """J/cm²"""
        
        if unit_abbreviation == IrradiationUnits.JoulePerSquareMillimeter:
            return """J/mm²"""
        
        if unit_abbreviation == IrradiationUnits.WattHourPerSquareMeter:
            return """Wh/m²"""
        
        if unit_abbreviation == IrradiationUnits.BtuPerSquareFoot:
            return """Btu/ft²"""
        
        if unit_abbreviation == IrradiationUnits.KilojoulePerSquareMeter:
            return """kJ/m²"""
        
        if unit_abbreviation == IrradiationUnits.MillijoulePerSquareCentimeter:
            return """mJ/cm²"""
        
        if unit_abbreviation == IrradiationUnits.KilowattHourPerSquareMeter:
            return """kWh/m²"""
        
        if unit_abbreviation == IrradiationUnits.KilobtuPerSquareFoot:
            return """kBtu/ft²"""
        
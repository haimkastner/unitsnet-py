from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class IrradianceUnits(Enum):
        """
            IrradianceUnits enumeration
        """
        
        WattPerSquareMeter = 'WattPerSquareMeter'
        """
            
        """
        
        WattPerSquareCentimeter = 'WattPerSquareCentimeter'
        """
            
        """
        
        PicowattPerSquareMeter = 'PicowattPerSquareMeter'
        """
            
        """
        
        NanowattPerSquareMeter = 'NanowattPerSquareMeter'
        """
            
        """
        
        MicrowattPerSquareMeter = 'MicrowattPerSquareMeter'
        """
            
        """
        
        MilliwattPerSquareMeter = 'MilliwattPerSquareMeter'
        """
            
        """
        
        KilowattPerSquareMeter = 'KilowattPerSquareMeter'
        """
            
        """
        
        MegawattPerSquareMeter = 'MegawattPerSquareMeter'
        """
            
        """
        
        PicowattPerSquareCentimeter = 'PicowattPerSquareCentimeter'
        """
            
        """
        
        NanowattPerSquareCentimeter = 'NanowattPerSquareCentimeter'
        """
            
        """
        
        MicrowattPerSquareCentimeter = 'MicrowattPerSquareCentimeter'
        """
            
        """
        
        MilliwattPerSquareCentimeter = 'MilliwattPerSquareCentimeter'
        """
            
        """
        
        KilowattPerSquareCentimeter = 'KilowattPerSquareCentimeter'
        """
            
        """
        
        MegawattPerSquareCentimeter = 'MegawattPerSquareCentimeter'
        """
            
        """
        

class IrradianceDto:
    """
    A DTO representation of a Irradiance

    Attributes:
        value (float): The value of the Irradiance.
        unit (IrradianceUnits): The specific unit that the Irradiance value is representing.
    """

    def __init__(self, value: float, unit: IrradianceUnits):
        """
        Create a new DTO representation of a Irradiance

        Parameters:
            value (float): The value of the Irradiance.
            unit (IrradianceUnits): The specific unit that the Irradiance value is representing.
        """
        self.value: float = value
        """
        The value of the Irradiance
        """
        self.unit: IrradianceUnits = unit
        """
        The specific unit that the Irradiance value is representing
        """

    def to_json(self):
        """
        Get a Irradiance DTO JSON object representing the current unit.

        :return: JSON object represents Irradiance DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "WattPerSquareMeter"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of Irradiance DTO from a json representation.

        :param data: The Irradiance DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "WattPerSquareMeter"}
        :return: A new instance of IrradianceDto.
        :rtype: IrradianceDto
        """
        return IrradianceDto(value=data["value"], unit=IrradianceUnits(data["unit"]))


class Irradiance(AbstractMeasure):
    """
    Irradiance is the intensity of ultraviolet (UV) or visible light incident on a surface.

    Args:
        value (float): The value.
        from_unit (IrradianceUnits): The Irradiance unit to create from, The default unit is WattPerSquareMeter
    """
    def __init__(self, value: float, from_unit: IrradianceUnits = IrradianceUnits.WattPerSquareMeter):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__watts_per_square_meter = None
        
        self.__watts_per_square_centimeter = None
        
        self.__picowatts_per_square_meter = None
        
        self.__nanowatts_per_square_meter = None
        
        self.__microwatts_per_square_meter = None
        
        self.__milliwatts_per_square_meter = None
        
        self.__kilowatts_per_square_meter = None
        
        self.__megawatts_per_square_meter = None
        
        self.__picowatts_per_square_centimeter = None
        
        self.__nanowatts_per_square_centimeter = None
        
        self.__microwatts_per_square_centimeter = None
        
        self.__milliwatts_per_square_centimeter = None
        
        self.__kilowatts_per_square_centimeter = None
        
        self.__megawatts_per_square_centimeter = None
        

    def convert(self, unit: IrradianceUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: IrradianceUnits = IrradianceUnits.WattPerSquareMeter) -> IrradianceDto:
        """
        Get a new instance of Irradiance DTO representing the current unit.

        :param hold_in_unit: The specific Irradiance unit to store the Irradiance value in the DTO representation.
        :type hold_in_unit: IrradianceUnits
        :return: A new instance of IrradianceDto.
        :rtype: IrradianceDto
        """
        return IrradianceDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: IrradianceUnits = IrradianceUnits.WattPerSquareMeter):
        """
        Get a Irradiance DTO JSON object representing the current unit.

        :param hold_in_unit: The specific Irradiance unit to store the Irradiance value in the DTO representation.
        :type hold_in_unit: IrradianceUnits
        :return: JSON object represents Irradiance DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "WattPerSquareMeter"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(irradiance_dto: IrradianceDto):
        """
        Obtain a new instance of Irradiance from a DTO unit object.

        :param irradiance_dto: The Irradiance DTO representation.
        :type irradiance_dto: IrradianceDto
        :return: A new instance of Irradiance.
        :rtype: Irradiance
        """
        return Irradiance(irradiance_dto.value, irradiance_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of Irradiance from a DTO unit json representation.

        :param data: The Irradiance DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "WattPerSquareMeter"}
        :return: A new instance of Irradiance.
        :rtype: Irradiance
        """
        return Irradiance.from_dto(IrradianceDto.from_json(data))

    def __convert_from_base(self, from_unit: IrradianceUnits) -> float:
        value = self._value
        
        if from_unit == IrradianceUnits.WattPerSquareMeter:
            return (value)
        
        if from_unit == IrradianceUnits.WattPerSquareCentimeter:
            return (value * 0.0001)
        
        if from_unit == IrradianceUnits.PicowattPerSquareMeter:
            return ((value) / 1e-12)
        
        if from_unit == IrradianceUnits.NanowattPerSquareMeter:
            return ((value) / 1e-09)
        
        if from_unit == IrradianceUnits.MicrowattPerSquareMeter:
            return ((value) / 1e-06)
        
        if from_unit == IrradianceUnits.MilliwattPerSquareMeter:
            return ((value) / 0.001)
        
        if from_unit == IrradianceUnits.KilowattPerSquareMeter:
            return ((value) / 1000.0)
        
        if from_unit == IrradianceUnits.MegawattPerSquareMeter:
            return ((value) / 1000000.0)
        
        if from_unit == IrradianceUnits.PicowattPerSquareCentimeter:
            return ((value * 0.0001) / 1e-12)
        
        if from_unit == IrradianceUnits.NanowattPerSquareCentimeter:
            return ((value * 0.0001) / 1e-09)
        
        if from_unit == IrradianceUnits.MicrowattPerSquareCentimeter:
            return ((value * 0.0001) / 1e-06)
        
        if from_unit == IrradianceUnits.MilliwattPerSquareCentimeter:
            return ((value * 0.0001) / 0.001)
        
        if from_unit == IrradianceUnits.KilowattPerSquareCentimeter:
            return ((value * 0.0001) / 1000.0)
        
        if from_unit == IrradianceUnits.MegawattPerSquareCentimeter:
            return ((value * 0.0001) / 1000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: IrradianceUnits) -> float:
        
        if to_unit == IrradianceUnits.WattPerSquareMeter:
            return (value)
        
        if to_unit == IrradianceUnits.WattPerSquareCentimeter:
            return (value * 10000)
        
        if to_unit == IrradianceUnits.PicowattPerSquareMeter:
            return ((value) * 1e-12)
        
        if to_unit == IrradianceUnits.NanowattPerSquareMeter:
            return ((value) * 1e-09)
        
        if to_unit == IrradianceUnits.MicrowattPerSquareMeter:
            return ((value) * 1e-06)
        
        if to_unit == IrradianceUnits.MilliwattPerSquareMeter:
            return ((value) * 0.001)
        
        if to_unit == IrradianceUnits.KilowattPerSquareMeter:
            return ((value) * 1000.0)
        
        if to_unit == IrradianceUnits.MegawattPerSquareMeter:
            return ((value) * 1000000.0)
        
        if to_unit == IrradianceUnits.PicowattPerSquareCentimeter:
            return ((value * 10000) * 1e-12)
        
        if to_unit == IrradianceUnits.NanowattPerSquareCentimeter:
            return ((value * 10000) * 1e-09)
        
        if to_unit == IrradianceUnits.MicrowattPerSquareCentimeter:
            return ((value * 10000) * 1e-06)
        
        if to_unit == IrradianceUnits.MilliwattPerSquareCentimeter:
            return ((value * 10000) * 0.001)
        
        if to_unit == IrradianceUnits.KilowattPerSquareCentimeter:
            return ((value * 10000) * 1000.0)
        
        if to_unit == IrradianceUnits.MegawattPerSquareCentimeter:
            return ((value * 10000) * 1000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_watts_per_square_meter(watts_per_square_meter: float):
        """
        Create a new instance of Irradiance from a value in watts_per_square_meter.

        

        :param meters: The Irradiance value in watts_per_square_meter.
        :type watts_per_square_meter: float
        :return: A new instance of Irradiance.
        :rtype: Irradiance
        """
        return Irradiance(watts_per_square_meter, IrradianceUnits.WattPerSquareMeter)

    
    @staticmethod
    def from_watts_per_square_centimeter(watts_per_square_centimeter: float):
        """
        Create a new instance of Irradiance from a value in watts_per_square_centimeter.

        

        :param meters: The Irradiance value in watts_per_square_centimeter.
        :type watts_per_square_centimeter: float
        :return: A new instance of Irradiance.
        :rtype: Irradiance
        """
        return Irradiance(watts_per_square_centimeter, IrradianceUnits.WattPerSquareCentimeter)

    
    @staticmethod
    def from_picowatts_per_square_meter(picowatts_per_square_meter: float):
        """
        Create a new instance of Irradiance from a value in picowatts_per_square_meter.

        

        :param meters: The Irradiance value in picowatts_per_square_meter.
        :type picowatts_per_square_meter: float
        :return: A new instance of Irradiance.
        :rtype: Irradiance
        """
        return Irradiance(picowatts_per_square_meter, IrradianceUnits.PicowattPerSquareMeter)

    
    @staticmethod
    def from_nanowatts_per_square_meter(nanowatts_per_square_meter: float):
        """
        Create a new instance of Irradiance from a value in nanowatts_per_square_meter.

        

        :param meters: The Irradiance value in nanowatts_per_square_meter.
        :type nanowatts_per_square_meter: float
        :return: A new instance of Irradiance.
        :rtype: Irradiance
        """
        return Irradiance(nanowatts_per_square_meter, IrradianceUnits.NanowattPerSquareMeter)

    
    @staticmethod
    def from_microwatts_per_square_meter(microwatts_per_square_meter: float):
        """
        Create a new instance of Irradiance from a value in microwatts_per_square_meter.

        

        :param meters: The Irradiance value in microwatts_per_square_meter.
        :type microwatts_per_square_meter: float
        :return: A new instance of Irradiance.
        :rtype: Irradiance
        """
        return Irradiance(microwatts_per_square_meter, IrradianceUnits.MicrowattPerSquareMeter)

    
    @staticmethod
    def from_milliwatts_per_square_meter(milliwatts_per_square_meter: float):
        """
        Create a new instance of Irradiance from a value in milliwatts_per_square_meter.

        

        :param meters: The Irradiance value in milliwatts_per_square_meter.
        :type milliwatts_per_square_meter: float
        :return: A new instance of Irradiance.
        :rtype: Irradiance
        """
        return Irradiance(milliwatts_per_square_meter, IrradianceUnits.MilliwattPerSquareMeter)

    
    @staticmethod
    def from_kilowatts_per_square_meter(kilowatts_per_square_meter: float):
        """
        Create a new instance of Irradiance from a value in kilowatts_per_square_meter.

        

        :param meters: The Irradiance value in kilowatts_per_square_meter.
        :type kilowatts_per_square_meter: float
        :return: A new instance of Irradiance.
        :rtype: Irradiance
        """
        return Irradiance(kilowatts_per_square_meter, IrradianceUnits.KilowattPerSquareMeter)

    
    @staticmethod
    def from_megawatts_per_square_meter(megawatts_per_square_meter: float):
        """
        Create a new instance of Irradiance from a value in megawatts_per_square_meter.

        

        :param meters: The Irradiance value in megawatts_per_square_meter.
        :type megawatts_per_square_meter: float
        :return: A new instance of Irradiance.
        :rtype: Irradiance
        """
        return Irradiance(megawatts_per_square_meter, IrradianceUnits.MegawattPerSquareMeter)

    
    @staticmethod
    def from_picowatts_per_square_centimeter(picowatts_per_square_centimeter: float):
        """
        Create a new instance of Irradiance from a value in picowatts_per_square_centimeter.

        

        :param meters: The Irradiance value in picowatts_per_square_centimeter.
        :type picowatts_per_square_centimeter: float
        :return: A new instance of Irradiance.
        :rtype: Irradiance
        """
        return Irradiance(picowatts_per_square_centimeter, IrradianceUnits.PicowattPerSquareCentimeter)

    
    @staticmethod
    def from_nanowatts_per_square_centimeter(nanowatts_per_square_centimeter: float):
        """
        Create a new instance of Irradiance from a value in nanowatts_per_square_centimeter.

        

        :param meters: The Irradiance value in nanowatts_per_square_centimeter.
        :type nanowatts_per_square_centimeter: float
        :return: A new instance of Irradiance.
        :rtype: Irradiance
        """
        return Irradiance(nanowatts_per_square_centimeter, IrradianceUnits.NanowattPerSquareCentimeter)

    
    @staticmethod
    def from_microwatts_per_square_centimeter(microwatts_per_square_centimeter: float):
        """
        Create a new instance of Irradiance from a value in microwatts_per_square_centimeter.

        

        :param meters: The Irradiance value in microwatts_per_square_centimeter.
        :type microwatts_per_square_centimeter: float
        :return: A new instance of Irradiance.
        :rtype: Irradiance
        """
        return Irradiance(microwatts_per_square_centimeter, IrradianceUnits.MicrowattPerSquareCentimeter)

    
    @staticmethod
    def from_milliwatts_per_square_centimeter(milliwatts_per_square_centimeter: float):
        """
        Create a new instance of Irradiance from a value in milliwatts_per_square_centimeter.

        

        :param meters: The Irradiance value in milliwatts_per_square_centimeter.
        :type milliwatts_per_square_centimeter: float
        :return: A new instance of Irradiance.
        :rtype: Irradiance
        """
        return Irradiance(milliwatts_per_square_centimeter, IrradianceUnits.MilliwattPerSquareCentimeter)

    
    @staticmethod
    def from_kilowatts_per_square_centimeter(kilowatts_per_square_centimeter: float):
        """
        Create a new instance of Irradiance from a value in kilowatts_per_square_centimeter.

        

        :param meters: The Irradiance value in kilowatts_per_square_centimeter.
        :type kilowatts_per_square_centimeter: float
        :return: A new instance of Irradiance.
        :rtype: Irradiance
        """
        return Irradiance(kilowatts_per_square_centimeter, IrradianceUnits.KilowattPerSquareCentimeter)

    
    @staticmethod
    def from_megawatts_per_square_centimeter(megawatts_per_square_centimeter: float):
        """
        Create a new instance of Irradiance from a value in megawatts_per_square_centimeter.

        

        :param meters: The Irradiance value in megawatts_per_square_centimeter.
        :type megawatts_per_square_centimeter: float
        :return: A new instance of Irradiance.
        :rtype: Irradiance
        """
        return Irradiance(megawatts_per_square_centimeter, IrradianceUnits.MegawattPerSquareCentimeter)

    
    @property
    def watts_per_square_meter(self) -> float:
        """
        
        """
        if self.__watts_per_square_meter != None:
            return self.__watts_per_square_meter
        self.__watts_per_square_meter = self.__convert_from_base(IrradianceUnits.WattPerSquareMeter)
        return self.__watts_per_square_meter

    
    @property
    def watts_per_square_centimeter(self) -> float:
        """
        
        """
        if self.__watts_per_square_centimeter != None:
            return self.__watts_per_square_centimeter
        self.__watts_per_square_centimeter = self.__convert_from_base(IrradianceUnits.WattPerSquareCentimeter)
        return self.__watts_per_square_centimeter

    
    @property
    def picowatts_per_square_meter(self) -> float:
        """
        
        """
        if self.__picowatts_per_square_meter != None:
            return self.__picowatts_per_square_meter
        self.__picowatts_per_square_meter = self.__convert_from_base(IrradianceUnits.PicowattPerSquareMeter)
        return self.__picowatts_per_square_meter

    
    @property
    def nanowatts_per_square_meter(self) -> float:
        """
        
        """
        if self.__nanowatts_per_square_meter != None:
            return self.__nanowatts_per_square_meter
        self.__nanowatts_per_square_meter = self.__convert_from_base(IrradianceUnits.NanowattPerSquareMeter)
        return self.__nanowatts_per_square_meter

    
    @property
    def microwatts_per_square_meter(self) -> float:
        """
        
        """
        if self.__microwatts_per_square_meter != None:
            return self.__microwatts_per_square_meter
        self.__microwatts_per_square_meter = self.__convert_from_base(IrradianceUnits.MicrowattPerSquareMeter)
        return self.__microwatts_per_square_meter

    
    @property
    def milliwatts_per_square_meter(self) -> float:
        """
        
        """
        if self.__milliwatts_per_square_meter != None:
            return self.__milliwatts_per_square_meter
        self.__milliwatts_per_square_meter = self.__convert_from_base(IrradianceUnits.MilliwattPerSquareMeter)
        return self.__milliwatts_per_square_meter

    
    @property
    def kilowatts_per_square_meter(self) -> float:
        """
        
        """
        if self.__kilowatts_per_square_meter != None:
            return self.__kilowatts_per_square_meter
        self.__kilowatts_per_square_meter = self.__convert_from_base(IrradianceUnits.KilowattPerSquareMeter)
        return self.__kilowatts_per_square_meter

    
    @property
    def megawatts_per_square_meter(self) -> float:
        """
        
        """
        if self.__megawatts_per_square_meter != None:
            return self.__megawatts_per_square_meter
        self.__megawatts_per_square_meter = self.__convert_from_base(IrradianceUnits.MegawattPerSquareMeter)
        return self.__megawatts_per_square_meter

    
    @property
    def picowatts_per_square_centimeter(self) -> float:
        """
        
        """
        if self.__picowatts_per_square_centimeter != None:
            return self.__picowatts_per_square_centimeter
        self.__picowatts_per_square_centimeter = self.__convert_from_base(IrradianceUnits.PicowattPerSquareCentimeter)
        return self.__picowatts_per_square_centimeter

    
    @property
    def nanowatts_per_square_centimeter(self) -> float:
        """
        
        """
        if self.__nanowatts_per_square_centimeter != None:
            return self.__nanowatts_per_square_centimeter
        self.__nanowatts_per_square_centimeter = self.__convert_from_base(IrradianceUnits.NanowattPerSquareCentimeter)
        return self.__nanowatts_per_square_centimeter

    
    @property
    def microwatts_per_square_centimeter(self) -> float:
        """
        
        """
        if self.__microwatts_per_square_centimeter != None:
            return self.__microwatts_per_square_centimeter
        self.__microwatts_per_square_centimeter = self.__convert_from_base(IrradianceUnits.MicrowattPerSquareCentimeter)
        return self.__microwatts_per_square_centimeter

    
    @property
    def milliwatts_per_square_centimeter(self) -> float:
        """
        
        """
        if self.__milliwatts_per_square_centimeter != None:
            return self.__milliwatts_per_square_centimeter
        self.__milliwatts_per_square_centimeter = self.__convert_from_base(IrradianceUnits.MilliwattPerSquareCentimeter)
        return self.__milliwatts_per_square_centimeter

    
    @property
    def kilowatts_per_square_centimeter(self) -> float:
        """
        
        """
        if self.__kilowatts_per_square_centimeter != None:
            return self.__kilowatts_per_square_centimeter
        self.__kilowatts_per_square_centimeter = self.__convert_from_base(IrradianceUnits.KilowattPerSquareCentimeter)
        return self.__kilowatts_per_square_centimeter

    
    @property
    def megawatts_per_square_centimeter(self) -> float:
        """
        
        """
        if self.__megawatts_per_square_centimeter != None:
            return self.__megawatts_per_square_centimeter
        self.__megawatts_per_square_centimeter = self.__convert_from_base(IrradianceUnits.MegawattPerSquareCentimeter)
        return self.__megawatts_per_square_centimeter

    
    def to_string(self, unit: IrradianceUnits = IrradianceUnits.WattPerSquareMeter, fractional_digits: int = None) -> str:
        """
        Format the Irradiance to a string.
        
        Note: the default format for Irradiance is WattPerSquareMeter.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the Irradiance. Default is 'WattPerSquareMeter'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == IrradianceUnits.WattPerSquareMeter:
            return f"""{super()._truncate_fraction_digits(self.watts_per_square_meter, fractional_digits)} W/m²"""
        
        if unit == IrradianceUnits.WattPerSquareCentimeter:
            return f"""{super()._truncate_fraction_digits(self.watts_per_square_centimeter, fractional_digits)} W/cm²"""
        
        if unit == IrradianceUnits.PicowattPerSquareMeter:
            return f"""{super()._truncate_fraction_digits(self.picowatts_per_square_meter, fractional_digits)} pW/m²"""
        
        if unit == IrradianceUnits.NanowattPerSquareMeter:
            return f"""{super()._truncate_fraction_digits(self.nanowatts_per_square_meter, fractional_digits)} nW/m²"""
        
        if unit == IrradianceUnits.MicrowattPerSquareMeter:
            return f"""{super()._truncate_fraction_digits(self.microwatts_per_square_meter, fractional_digits)} μW/m²"""
        
        if unit == IrradianceUnits.MilliwattPerSquareMeter:
            return f"""{super()._truncate_fraction_digits(self.milliwatts_per_square_meter, fractional_digits)} mW/m²"""
        
        if unit == IrradianceUnits.KilowattPerSquareMeter:
            return f"""{super()._truncate_fraction_digits(self.kilowatts_per_square_meter, fractional_digits)} kW/m²"""
        
        if unit == IrradianceUnits.MegawattPerSquareMeter:
            return f"""{super()._truncate_fraction_digits(self.megawatts_per_square_meter, fractional_digits)} MW/m²"""
        
        if unit == IrradianceUnits.PicowattPerSquareCentimeter:
            return f"""{super()._truncate_fraction_digits(self.picowatts_per_square_centimeter, fractional_digits)} pW/cm²"""
        
        if unit == IrradianceUnits.NanowattPerSquareCentimeter:
            return f"""{super()._truncate_fraction_digits(self.nanowatts_per_square_centimeter, fractional_digits)} nW/cm²"""
        
        if unit == IrradianceUnits.MicrowattPerSquareCentimeter:
            return f"""{super()._truncate_fraction_digits(self.microwatts_per_square_centimeter, fractional_digits)} μW/cm²"""
        
        if unit == IrradianceUnits.MilliwattPerSquareCentimeter:
            return f"""{super()._truncate_fraction_digits(self.milliwatts_per_square_centimeter, fractional_digits)} mW/cm²"""
        
        if unit == IrradianceUnits.KilowattPerSquareCentimeter:
            return f"""{super()._truncate_fraction_digits(self.kilowatts_per_square_centimeter, fractional_digits)} kW/cm²"""
        
        if unit == IrradianceUnits.MegawattPerSquareCentimeter:
            return f"""{super()._truncate_fraction_digits(self.megawatts_per_square_centimeter, fractional_digits)} MW/cm²"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: IrradianceUnits = IrradianceUnits.WattPerSquareMeter) -> str:
        """
        Get Irradiance unit abbreviation.
        Note! the default abbreviation for Irradiance is WattPerSquareMeter.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == IrradianceUnits.WattPerSquareMeter:
            return """W/m²"""
        
        if unit_abbreviation == IrradianceUnits.WattPerSquareCentimeter:
            return """W/cm²"""
        
        if unit_abbreviation == IrradianceUnits.PicowattPerSquareMeter:
            return """pW/m²"""
        
        if unit_abbreviation == IrradianceUnits.NanowattPerSquareMeter:
            return """nW/m²"""
        
        if unit_abbreviation == IrradianceUnits.MicrowattPerSquareMeter:
            return """μW/m²"""
        
        if unit_abbreviation == IrradianceUnits.MilliwattPerSquareMeter:
            return """mW/m²"""
        
        if unit_abbreviation == IrradianceUnits.KilowattPerSquareMeter:
            return """kW/m²"""
        
        if unit_abbreviation == IrradianceUnits.MegawattPerSquareMeter:
            return """MW/m²"""
        
        if unit_abbreviation == IrradianceUnits.PicowattPerSquareCentimeter:
            return """pW/cm²"""
        
        if unit_abbreviation == IrradianceUnits.NanowattPerSquareCentimeter:
            return """nW/cm²"""
        
        if unit_abbreviation == IrradianceUnits.MicrowattPerSquareCentimeter:
            return """μW/cm²"""
        
        if unit_abbreviation == IrradianceUnits.MilliwattPerSquareCentimeter:
            return """mW/cm²"""
        
        if unit_abbreviation == IrradianceUnits.KilowattPerSquareCentimeter:
            return """kW/cm²"""
        
        if unit_abbreviation == IrradianceUnits.MegawattPerSquareCentimeter:
            return """MW/cm²"""
        
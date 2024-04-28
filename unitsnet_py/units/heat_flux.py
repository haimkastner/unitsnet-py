from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class HeatFluxUnits(Enum):
        """
            HeatFluxUnits enumeration
        """
        
        WattPerSquareMeter = 'WattPerSquareMeter'
        """
            
        """
        
        WattPerSquareInch = 'WattPerSquareInch'
        """
            
        """
        
        WattPerSquareFoot = 'WattPerSquareFoot'
        """
            
        """
        
        BtuPerSecondSquareInch = 'BtuPerSecondSquareInch'
        """
            
        """
        
        BtuPerSecondSquareFoot = 'BtuPerSecondSquareFoot'
        """
            
        """
        
        BtuPerMinuteSquareFoot = 'BtuPerMinuteSquareFoot'
        """
            
        """
        
        BtuPerHourSquareFoot = 'BtuPerHourSquareFoot'
        """
            
        """
        
        CaloriePerSecondSquareCentimeter = 'CaloriePerSecondSquareCentimeter'
        """
            
        """
        
        KilocaloriePerHourSquareMeter = 'KilocaloriePerHourSquareMeter'
        """
            
        """
        
        PoundForcePerFootSecond = 'PoundForcePerFootSecond'
        """
            
        """
        
        PoundPerSecondCubed = 'PoundPerSecondCubed'
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
        
        CentiwattPerSquareMeter = 'CentiwattPerSquareMeter'
        """
            
        """
        
        DeciwattPerSquareMeter = 'DeciwattPerSquareMeter'
        """
            
        """
        
        KilowattPerSquareMeter = 'KilowattPerSquareMeter'
        """
            
        """
        
        KilocaloriePerSecondSquareCentimeter = 'KilocaloriePerSecondSquareCentimeter'
        """
            
        """
        

class HeatFluxDto:
    """
    A DTO representation of a HeatFlux

    Attributes:
        value (float): The value of the HeatFlux.
        unit (HeatFluxUnits): The specific unit that the HeatFlux value is representing.
    """

    def __init__(self, value: float, unit: HeatFluxUnits):
        """
        Create a new DTO representation of a HeatFlux

        Parameters:
            value (float): The value of the HeatFlux.
            unit (HeatFluxUnits): The specific unit that the HeatFlux value is representing.
        """
        self.value: float = value
        """
        The value of the HeatFlux
        """
        self.unit: HeatFluxUnits = unit
        """
        The specific unit that the HeatFlux value is representing
        """

    def to_json(self):
        """
        Get a HeatFlux DTO JSON object representing the current unit.

        :return: JSON object represents HeatFlux DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "WattPerSquareMeter"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of HeatFlux DTO from a json representation.

        :param data: The HeatFlux DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "WattPerSquareMeter"}
        :return: A new instance of HeatFluxDto.
        :rtype: HeatFluxDto
        """
        return HeatFluxDto(value=data["value"], unit=HeatFluxUnits(data["unit"]))


class HeatFlux(AbstractMeasure):
    """
    Heat flux is the flow of energy per unit of area per unit of time

    Args:
        value (float): The value.
        from_unit (HeatFluxUnits): The HeatFlux unit to create from, The default unit is WattPerSquareMeter
    """
    def __init__(self, value: float, from_unit: HeatFluxUnits = HeatFluxUnits.WattPerSquareMeter):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__watts_per_square_meter = None
        
        self.__watts_per_square_inch = None
        
        self.__watts_per_square_foot = None
        
        self.__btus_per_second_square_inch = None
        
        self.__btus_per_second_square_foot = None
        
        self.__btus_per_minute_square_foot = None
        
        self.__btus_per_hour_square_foot = None
        
        self.__calories_per_second_square_centimeter = None
        
        self.__kilocalories_per_hour_square_meter = None
        
        self.__pounds_force_per_foot_second = None
        
        self.__pounds_per_second_cubed = None
        
        self.__nanowatts_per_square_meter = None
        
        self.__microwatts_per_square_meter = None
        
        self.__milliwatts_per_square_meter = None
        
        self.__centiwatts_per_square_meter = None
        
        self.__deciwatts_per_square_meter = None
        
        self.__kilowatts_per_square_meter = None
        
        self.__kilocalories_per_second_square_centimeter = None
        

    def convert(self, unit: HeatFluxUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: HeatFluxUnits = HeatFluxUnits.WattPerSquareMeter) -> HeatFluxDto:
        """
        Get a new instance of HeatFlux DTO representing the current unit.

        :param hold_in_unit: The specific HeatFlux unit to store the HeatFlux value in the DTO representation.
        :type hold_in_unit: HeatFluxUnits
        :return: A new instance of HeatFluxDto.
        :rtype: HeatFluxDto
        """
        return HeatFluxDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: HeatFluxUnits = HeatFluxUnits.WattPerSquareMeter):
        """
        Get a HeatFlux DTO JSON object representing the current unit.

        :param hold_in_unit: The specific HeatFlux unit to store the HeatFlux value in the DTO representation.
        :type hold_in_unit: HeatFluxUnits
        :return: JSON object represents HeatFlux DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "WattPerSquareMeter"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(heat_flux_dto: HeatFluxDto):
        """
        Obtain a new instance of HeatFlux from a DTO unit object.

        :param heat_flux_dto: The HeatFlux DTO representation.
        :type heat_flux_dto: HeatFluxDto
        :return: A new instance of HeatFlux.
        :rtype: HeatFlux
        """
        return HeatFlux(heat_flux_dto.value, heat_flux_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of HeatFlux from a DTO unit json representation.

        :param data: The HeatFlux DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "WattPerSquareMeter"}
        :return: A new instance of HeatFlux.
        :rtype: HeatFlux
        """
        return HeatFlux.from_dto(HeatFluxDto.from_json(data))

    def __convert_from_base(self, from_unit: HeatFluxUnits) -> float:
        value = self._value
        
        if from_unit == HeatFluxUnits.WattPerSquareMeter:
            return (value)
        
        if from_unit == HeatFluxUnits.WattPerSquareInch:
            return (value / 1.5500031e3)
        
        if from_unit == HeatFluxUnits.WattPerSquareFoot:
            return (value / 1.07639e1)
        
        if from_unit == HeatFluxUnits.BtuPerSecondSquareInch:
            return (value / 1.63533984e6)
        
        if from_unit == HeatFluxUnits.BtuPerSecondSquareFoot:
            return (value / 1.13565267e4)
        
        if from_unit == HeatFluxUnits.BtuPerMinuteSquareFoot:
            return (value / 1.89275445e2)
        
        if from_unit == HeatFluxUnits.BtuPerHourSquareFoot:
            return (value / 3.15459075)
        
        if from_unit == HeatFluxUnits.CaloriePerSecondSquareCentimeter:
            return (value / 4.1868e4)
        
        if from_unit == HeatFluxUnits.KilocaloriePerHourSquareMeter:
            return (value / 1.163)
        
        if from_unit == HeatFluxUnits.PoundForcePerFootSecond:
            return (value / 1.459390293720636e1)
        
        if from_unit == HeatFluxUnits.PoundPerSecondCubed:
            return (value / 4.5359237e-1)
        
        if from_unit == HeatFluxUnits.NanowattPerSquareMeter:
            return ((value) / 1e-09)
        
        if from_unit == HeatFluxUnits.MicrowattPerSquareMeter:
            return ((value) / 1e-06)
        
        if from_unit == HeatFluxUnits.MilliwattPerSquareMeter:
            return ((value) / 0.001)
        
        if from_unit == HeatFluxUnits.CentiwattPerSquareMeter:
            return ((value) / 0.01)
        
        if from_unit == HeatFluxUnits.DeciwattPerSquareMeter:
            return ((value) / 0.1)
        
        if from_unit == HeatFluxUnits.KilowattPerSquareMeter:
            return ((value) / 1000.0)
        
        if from_unit == HeatFluxUnits.KilocaloriePerSecondSquareCentimeter:
            return ((value / 4.1868e4) / 1000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: HeatFluxUnits) -> float:
        
        if to_unit == HeatFluxUnits.WattPerSquareMeter:
            return (value)
        
        if to_unit == HeatFluxUnits.WattPerSquareInch:
            return (value * 1.5500031e3)
        
        if to_unit == HeatFluxUnits.WattPerSquareFoot:
            return (value * 1.07639e1)
        
        if to_unit == HeatFluxUnits.BtuPerSecondSquareInch:
            return (value * 1.63533984e6)
        
        if to_unit == HeatFluxUnits.BtuPerSecondSquareFoot:
            return (value * 1.13565267e4)
        
        if to_unit == HeatFluxUnits.BtuPerMinuteSquareFoot:
            return (value * 1.89275445e2)
        
        if to_unit == HeatFluxUnits.BtuPerHourSquareFoot:
            return (value * 3.15459075)
        
        if to_unit == HeatFluxUnits.CaloriePerSecondSquareCentimeter:
            return (value * 4.1868e4)
        
        if to_unit == HeatFluxUnits.KilocaloriePerHourSquareMeter:
            return (value * 1.163)
        
        if to_unit == HeatFluxUnits.PoundForcePerFootSecond:
            return (value * 1.459390293720636e1)
        
        if to_unit == HeatFluxUnits.PoundPerSecondCubed:
            return (value * 4.5359237e-1)
        
        if to_unit == HeatFluxUnits.NanowattPerSquareMeter:
            return ((value) * 1e-09)
        
        if to_unit == HeatFluxUnits.MicrowattPerSquareMeter:
            return ((value) * 1e-06)
        
        if to_unit == HeatFluxUnits.MilliwattPerSquareMeter:
            return ((value) * 0.001)
        
        if to_unit == HeatFluxUnits.CentiwattPerSquareMeter:
            return ((value) * 0.01)
        
        if to_unit == HeatFluxUnits.DeciwattPerSquareMeter:
            return ((value) * 0.1)
        
        if to_unit == HeatFluxUnits.KilowattPerSquareMeter:
            return ((value) * 1000.0)
        
        if to_unit == HeatFluxUnits.KilocaloriePerSecondSquareCentimeter:
            return ((value * 4.1868e4) * 1000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_watts_per_square_meter(watts_per_square_meter: float):
        """
        Create a new instance of HeatFlux from a value in watts_per_square_meter.

        

        :param meters: The HeatFlux value in watts_per_square_meter.
        :type watts_per_square_meter: float
        :return: A new instance of HeatFlux.
        :rtype: HeatFlux
        """
        return HeatFlux(watts_per_square_meter, HeatFluxUnits.WattPerSquareMeter)

    
    @staticmethod
    def from_watts_per_square_inch(watts_per_square_inch: float):
        """
        Create a new instance of HeatFlux from a value in watts_per_square_inch.

        

        :param meters: The HeatFlux value in watts_per_square_inch.
        :type watts_per_square_inch: float
        :return: A new instance of HeatFlux.
        :rtype: HeatFlux
        """
        return HeatFlux(watts_per_square_inch, HeatFluxUnits.WattPerSquareInch)

    
    @staticmethod
    def from_watts_per_square_foot(watts_per_square_foot: float):
        """
        Create a new instance of HeatFlux from a value in watts_per_square_foot.

        

        :param meters: The HeatFlux value in watts_per_square_foot.
        :type watts_per_square_foot: float
        :return: A new instance of HeatFlux.
        :rtype: HeatFlux
        """
        return HeatFlux(watts_per_square_foot, HeatFluxUnits.WattPerSquareFoot)

    
    @staticmethod
    def from_btus_per_second_square_inch(btus_per_second_square_inch: float):
        """
        Create a new instance of HeatFlux from a value in btus_per_second_square_inch.

        

        :param meters: The HeatFlux value in btus_per_second_square_inch.
        :type btus_per_second_square_inch: float
        :return: A new instance of HeatFlux.
        :rtype: HeatFlux
        """
        return HeatFlux(btus_per_second_square_inch, HeatFluxUnits.BtuPerSecondSquareInch)

    
    @staticmethod
    def from_btus_per_second_square_foot(btus_per_second_square_foot: float):
        """
        Create a new instance of HeatFlux from a value in btus_per_second_square_foot.

        

        :param meters: The HeatFlux value in btus_per_second_square_foot.
        :type btus_per_second_square_foot: float
        :return: A new instance of HeatFlux.
        :rtype: HeatFlux
        """
        return HeatFlux(btus_per_second_square_foot, HeatFluxUnits.BtuPerSecondSquareFoot)

    
    @staticmethod
    def from_btus_per_minute_square_foot(btus_per_minute_square_foot: float):
        """
        Create a new instance of HeatFlux from a value in btus_per_minute_square_foot.

        

        :param meters: The HeatFlux value in btus_per_minute_square_foot.
        :type btus_per_minute_square_foot: float
        :return: A new instance of HeatFlux.
        :rtype: HeatFlux
        """
        return HeatFlux(btus_per_minute_square_foot, HeatFluxUnits.BtuPerMinuteSquareFoot)

    
    @staticmethod
    def from_btus_per_hour_square_foot(btus_per_hour_square_foot: float):
        """
        Create a new instance of HeatFlux from a value in btus_per_hour_square_foot.

        

        :param meters: The HeatFlux value in btus_per_hour_square_foot.
        :type btus_per_hour_square_foot: float
        :return: A new instance of HeatFlux.
        :rtype: HeatFlux
        """
        return HeatFlux(btus_per_hour_square_foot, HeatFluxUnits.BtuPerHourSquareFoot)

    
    @staticmethod
    def from_calories_per_second_square_centimeter(calories_per_second_square_centimeter: float):
        """
        Create a new instance of HeatFlux from a value in calories_per_second_square_centimeter.

        

        :param meters: The HeatFlux value in calories_per_second_square_centimeter.
        :type calories_per_second_square_centimeter: float
        :return: A new instance of HeatFlux.
        :rtype: HeatFlux
        """
        return HeatFlux(calories_per_second_square_centimeter, HeatFluxUnits.CaloriePerSecondSquareCentimeter)

    
    @staticmethod
    def from_kilocalories_per_hour_square_meter(kilocalories_per_hour_square_meter: float):
        """
        Create a new instance of HeatFlux from a value in kilocalories_per_hour_square_meter.

        

        :param meters: The HeatFlux value in kilocalories_per_hour_square_meter.
        :type kilocalories_per_hour_square_meter: float
        :return: A new instance of HeatFlux.
        :rtype: HeatFlux
        """
        return HeatFlux(kilocalories_per_hour_square_meter, HeatFluxUnits.KilocaloriePerHourSquareMeter)

    
    @staticmethod
    def from_pounds_force_per_foot_second(pounds_force_per_foot_second: float):
        """
        Create a new instance of HeatFlux from a value in pounds_force_per_foot_second.

        

        :param meters: The HeatFlux value in pounds_force_per_foot_second.
        :type pounds_force_per_foot_second: float
        :return: A new instance of HeatFlux.
        :rtype: HeatFlux
        """
        return HeatFlux(pounds_force_per_foot_second, HeatFluxUnits.PoundForcePerFootSecond)

    
    @staticmethod
    def from_pounds_per_second_cubed(pounds_per_second_cubed: float):
        """
        Create a new instance of HeatFlux from a value in pounds_per_second_cubed.

        

        :param meters: The HeatFlux value in pounds_per_second_cubed.
        :type pounds_per_second_cubed: float
        :return: A new instance of HeatFlux.
        :rtype: HeatFlux
        """
        return HeatFlux(pounds_per_second_cubed, HeatFluxUnits.PoundPerSecondCubed)

    
    @staticmethod
    def from_nanowatts_per_square_meter(nanowatts_per_square_meter: float):
        """
        Create a new instance of HeatFlux from a value in nanowatts_per_square_meter.

        

        :param meters: The HeatFlux value in nanowatts_per_square_meter.
        :type nanowatts_per_square_meter: float
        :return: A new instance of HeatFlux.
        :rtype: HeatFlux
        """
        return HeatFlux(nanowatts_per_square_meter, HeatFluxUnits.NanowattPerSquareMeter)

    
    @staticmethod
    def from_microwatts_per_square_meter(microwatts_per_square_meter: float):
        """
        Create a new instance of HeatFlux from a value in microwatts_per_square_meter.

        

        :param meters: The HeatFlux value in microwatts_per_square_meter.
        :type microwatts_per_square_meter: float
        :return: A new instance of HeatFlux.
        :rtype: HeatFlux
        """
        return HeatFlux(microwatts_per_square_meter, HeatFluxUnits.MicrowattPerSquareMeter)

    
    @staticmethod
    def from_milliwatts_per_square_meter(milliwatts_per_square_meter: float):
        """
        Create a new instance of HeatFlux from a value in milliwatts_per_square_meter.

        

        :param meters: The HeatFlux value in milliwatts_per_square_meter.
        :type milliwatts_per_square_meter: float
        :return: A new instance of HeatFlux.
        :rtype: HeatFlux
        """
        return HeatFlux(milliwatts_per_square_meter, HeatFluxUnits.MilliwattPerSquareMeter)

    
    @staticmethod
    def from_centiwatts_per_square_meter(centiwatts_per_square_meter: float):
        """
        Create a new instance of HeatFlux from a value in centiwatts_per_square_meter.

        

        :param meters: The HeatFlux value in centiwatts_per_square_meter.
        :type centiwatts_per_square_meter: float
        :return: A new instance of HeatFlux.
        :rtype: HeatFlux
        """
        return HeatFlux(centiwatts_per_square_meter, HeatFluxUnits.CentiwattPerSquareMeter)

    
    @staticmethod
    def from_deciwatts_per_square_meter(deciwatts_per_square_meter: float):
        """
        Create a new instance of HeatFlux from a value in deciwatts_per_square_meter.

        

        :param meters: The HeatFlux value in deciwatts_per_square_meter.
        :type deciwatts_per_square_meter: float
        :return: A new instance of HeatFlux.
        :rtype: HeatFlux
        """
        return HeatFlux(deciwatts_per_square_meter, HeatFluxUnits.DeciwattPerSquareMeter)

    
    @staticmethod
    def from_kilowatts_per_square_meter(kilowatts_per_square_meter: float):
        """
        Create a new instance of HeatFlux from a value in kilowatts_per_square_meter.

        

        :param meters: The HeatFlux value in kilowatts_per_square_meter.
        :type kilowatts_per_square_meter: float
        :return: A new instance of HeatFlux.
        :rtype: HeatFlux
        """
        return HeatFlux(kilowatts_per_square_meter, HeatFluxUnits.KilowattPerSquareMeter)

    
    @staticmethod
    def from_kilocalories_per_second_square_centimeter(kilocalories_per_second_square_centimeter: float):
        """
        Create a new instance of HeatFlux from a value in kilocalories_per_second_square_centimeter.

        

        :param meters: The HeatFlux value in kilocalories_per_second_square_centimeter.
        :type kilocalories_per_second_square_centimeter: float
        :return: A new instance of HeatFlux.
        :rtype: HeatFlux
        """
        return HeatFlux(kilocalories_per_second_square_centimeter, HeatFluxUnits.KilocaloriePerSecondSquareCentimeter)

    
    @property
    def watts_per_square_meter(self) -> float:
        """
        
        """
        if self.__watts_per_square_meter != None:
            return self.__watts_per_square_meter
        self.__watts_per_square_meter = self.__convert_from_base(HeatFluxUnits.WattPerSquareMeter)
        return self.__watts_per_square_meter

    
    @property
    def watts_per_square_inch(self) -> float:
        """
        
        """
        if self.__watts_per_square_inch != None:
            return self.__watts_per_square_inch
        self.__watts_per_square_inch = self.__convert_from_base(HeatFluxUnits.WattPerSquareInch)
        return self.__watts_per_square_inch

    
    @property
    def watts_per_square_foot(self) -> float:
        """
        
        """
        if self.__watts_per_square_foot != None:
            return self.__watts_per_square_foot
        self.__watts_per_square_foot = self.__convert_from_base(HeatFluxUnits.WattPerSquareFoot)
        return self.__watts_per_square_foot

    
    @property
    def btus_per_second_square_inch(self) -> float:
        """
        
        """
        if self.__btus_per_second_square_inch != None:
            return self.__btus_per_second_square_inch
        self.__btus_per_second_square_inch = self.__convert_from_base(HeatFluxUnits.BtuPerSecondSquareInch)
        return self.__btus_per_second_square_inch

    
    @property
    def btus_per_second_square_foot(self) -> float:
        """
        
        """
        if self.__btus_per_second_square_foot != None:
            return self.__btus_per_second_square_foot
        self.__btus_per_second_square_foot = self.__convert_from_base(HeatFluxUnits.BtuPerSecondSquareFoot)
        return self.__btus_per_second_square_foot

    
    @property
    def btus_per_minute_square_foot(self) -> float:
        """
        
        """
        if self.__btus_per_minute_square_foot != None:
            return self.__btus_per_minute_square_foot
        self.__btus_per_minute_square_foot = self.__convert_from_base(HeatFluxUnits.BtuPerMinuteSquareFoot)
        return self.__btus_per_minute_square_foot

    
    @property
    def btus_per_hour_square_foot(self) -> float:
        """
        
        """
        if self.__btus_per_hour_square_foot != None:
            return self.__btus_per_hour_square_foot
        self.__btus_per_hour_square_foot = self.__convert_from_base(HeatFluxUnits.BtuPerHourSquareFoot)
        return self.__btus_per_hour_square_foot

    
    @property
    def calories_per_second_square_centimeter(self) -> float:
        """
        
        """
        if self.__calories_per_second_square_centimeter != None:
            return self.__calories_per_second_square_centimeter
        self.__calories_per_second_square_centimeter = self.__convert_from_base(HeatFluxUnits.CaloriePerSecondSquareCentimeter)
        return self.__calories_per_second_square_centimeter

    
    @property
    def kilocalories_per_hour_square_meter(self) -> float:
        """
        
        """
        if self.__kilocalories_per_hour_square_meter != None:
            return self.__kilocalories_per_hour_square_meter
        self.__kilocalories_per_hour_square_meter = self.__convert_from_base(HeatFluxUnits.KilocaloriePerHourSquareMeter)
        return self.__kilocalories_per_hour_square_meter

    
    @property
    def pounds_force_per_foot_second(self) -> float:
        """
        
        """
        if self.__pounds_force_per_foot_second != None:
            return self.__pounds_force_per_foot_second
        self.__pounds_force_per_foot_second = self.__convert_from_base(HeatFluxUnits.PoundForcePerFootSecond)
        return self.__pounds_force_per_foot_second

    
    @property
    def pounds_per_second_cubed(self) -> float:
        """
        
        """
        if self.__pounds_per_second_cubed != None:
            return self.__pounds_per_second_cubed
        self.__pounds_per_second_cubed = self.__convert_from_base(HeatFluxUnits.PoundPerSecondCubed)
        return self.__pounds_per_second_cubed

    
    @property
    def nanowatts_per_square_meter(self) -> float:
        """
        
        """
        if self.__nanowatts_per_square_meter != None:
            return self.__nanowatts_per_square_meter
        self.__nanowatts_per_square_meter = self.__convert_from_base(HeatFluxUnits.NanowattPerSquareMeter)
        return self.__nanowatts_per_square_meter

    
    @property
    def microwatts_per_square_meter(self) -> float:
        """
        
        """
        if self.__microwatts_per_square_meter != None:
            return self.__microwatts_per_square_meter
        self.__microwatts_per_square_meter = self.__convert_from_base(HeatFluxUnits.MicrowattPerSquareMeter)
        return self.__microwatts_per_square_meter

    
    @property
    def milliwatts_per_square_meter(self) -> float:
        """
        
        """
        if self.__milliwatts_per_square_meter != None:
            return self.__milliwatts_per_square_meter
        self.__milliwatts_per_square_meter = self.__convert_from_base(HeatFluxUnits.MilliwattPerSquareMeter)
        return self.__milliwatts_per_square_meter

    
    @property
    def centiwatts_per_square_meter(self) -> float:
        """
        
        """
        if self.__centiwatts_per_square_meter != None:
            return self.__centiwatts_per_square_meter
        self.__centiwatts_per_square_meter = self.__convert_from_base(HeatFluxUnits.CentiwattPerSquareMeter)
        return self.__centiwatts_per_square_meter

    
    @property
    def deciwatts_per_square_meter(self) -> float:
        """
        
        """
        if self.__deciwatts_per_square_meter != None:
            return self.__deciwatts_per_square_meter
        self.__deciwatts_per_square_meter = self.__convert_from_base(HeatFluxUnits.DeciwattPerSquareMeter)
        return self.__deciwatts_per_square_meter

    
    @property
    def kilowatts_per_square_meter(self) -> float:
        """
        
        """
        if self.__kilowatts_per_square_meter != None:
            return self.__kilowatts_per_square_meter
        self.__kilowatts_per_square_meter = self.__convert_from_base(HeatFluxUnits.KilowattPerSquareMeter)
        return self.__kilowatts_per_square_meter

    
    @property
    def kilocalories_per_second_square_centimeter(self) -> float:
        """
        
        """
        if self.__kilocalories_per_second_square_centimeter != None:
            return self.__kilocalories_per_second_square_centimeter
        self.__kilocalories_per_second_square_centimeter = self.__convert_from_base(HeatFluxUnits.KilocaloriePerSecondSquareCentimeter)
        return self.__kilocalories_per_second_square_centimeter

    
    def to_string(self, unit: HeatFluxUnits = HeatFluxUnits.WattPerSquareMeter, fractional_digits: int = None) -> str:
        """
        Format the HeatFlux to a string.
        
        Note: the default format for HeatFlux is WattPerSquareMeter.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the HeatFlux. Default is 'WattPerSquareMeter'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == HeatFluxUnits.WattPerSquareMeter:
            return f"""{super()._truncate_fraction_digits(self.watts_per_square_meter, fractional_digits)} W/m²"""
        
        if unit == HeatFluxUnits.WattPerSquareInch:
            return f"""{super()._truncate_fraction_digits(self.watts_per_square_inch, fractional_digits)} W/in²"""
        
        if unit == HeatFluxUnits.WattPerSquareFoot:
            return f"""{super()._truncate_fraction_digits(self.watts_per_square_foot, fractional_digits)} W/ft²"""
        
        if unit == HeatFluxUnits.BtuPerSecondSquareInch:
            return f"""{super()._truncate_fraction_digits(self.btus_per_second_square_inch, fractional_digits)} BTU/s·in²"""
        
        if unit == HeatFluxUnits.BtuPerSecondSquareFoot:
            return f"""{super()._truncate_fraction_digits(self.btus_per_second_square_foot, fractional_digits)} BTU/s·ft²"""
        
        if unit == HeatFluxUnits.BtuPerMinuteSquareFoot:
            return f"""{super()._truncate_fraction_digits(self.btus_per_minute_square_foot, fractional_digits)} BTU/min·ft²"""
        
        if unit == HeatFluxUnits.BtuPerHourSquareFoot:
            return f"""{super()._truncate_fraction_digits(self.btus_per_hour_square_foot, fractional_digits)} BTU/h·ft²"""
        
        if unit == HeatFluxUnits.CaloriePerSecondSquareCentimeter:
            return f"""{super()._truncate_fraction_digits(self.calories_per_second_square_centimeter, fractional_digits)} cal/s·cm²"""
        
        if unit == HeatFluxUnits.KilocaloriePerHourSquareMeter:
            return f"""{super()._truncate_fraction_digits(self.kilocalories_per_hour_square_meter, fractional_digits)} kcal/h·m²"""
        
        if unit == HeatFluxUnits.PoundForcePerFootSecond:
            return f"""{super()._truncate_fraction_digits(self.pounds_force_per_foot_second, fractional_digits)} lbf/(ft·s)"""
        
        if unit == HeatFluxUnits.PoundPerSecondCubed:
            return f"""{super()._truncate_fraction_digits(self.pounds_per_second_cubed, fractional_digits)} lb/s³"""
        
        if unit == HeatFluxUnits.NanowattPerSquareMeter:
            return f"""{super()._truncate_fraction_digits(self.nanowatts_per_square_meter, fractional_digits)} nW/m²"""
        
        if unit == HeatFluxUnits.MicrowattPerSquareMeter:
            return f"""{super()._truncate_fraction_digits(self.microwatts_per_square_meter, fractional_digits)} μW/m²"""
        
        if unit == HeatFluxUnits.MilliwattPerSquareMeter:
            return f"""{super()._truncate_fraction_digits(self.milliwatts_per_square_meter, fractional_digits)} mW/m²"""
        
        if unit == HeatFluxUnits.CentiwattPerSquareMeter:
            return f"""{super()._truncate_fraction_digits(self.centiwatts_per_square_meter, fractional_digits)} cW/m²"""
        
        if unit == HeatFluxUnits.DeciwattPerSquareMeter:
            return f"""{super()._truncate_fraction_digits(self.deciwatts_per_square_meter, fractional_digits)} dW/m²"""
        
        if unit == HeatFluxUnits.KilowattPerSquareMeter:
            return f"""{super()._truncate_fraction_digits(self.kilowatts_per_square_meter, fractional_digits)} kW/m²"""
        
        if unit == HeatFluxUnits.KilocaloriePerSecondSquareCentimeter:
            return f"""{super()._truncate_fraction_digits(self.kilocalories_per_second_square_centimeter, fractional_digits)} kcal/s·cm²"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: HeatFluxUnits = HeatFluxUnits.WattPerSquareMeter) -> str:
        """
        Get HeatFlux unit abbreviation.
        Note! the default abbreviation for HeatFlux is WattPerSquareMeter.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == HeatFluxUnits.WattPerSquareMeter:
            return """W/m²"""
        
        if unit_abbreviation == HeatFluxUnits.WattPerSquareInch:
            return """W/in²"""
        
        if unit_abbreviation == HeatFluxUnits.WattPerSquareFoot:
            return """W/ft²"""
        
        if unit_abbreviation == HeatFluxUnits.BtuPerSecondSquareInch:
            return """BTU/s·in²"""
        
        if unit_abbreviation == HeatFluxUnits.BtuPerSecondSquareFoot:
            return """BTU/s·ft²"""
        
        if unit_abbreviation == HeatFluxUnits.BtuPerMinuteSquareFoot:
            return """BTU/min·ft²"""
        
        if unit_abbreviation == HeatFluxUnits.BtuPerHourSquareFoot:
            return """BTU/h·ft²"""
        
        if unit_abbreviation == HeatFluxUnits.CaloriePerSecondSquareCentimeter:
            return """cal/s·cm²"""
        
        if unit_abbreviation == HeatFluxUnits.KilocaloriePerHourSquareMeter:
            return """kcal/h·m²"""
        
        if unit_abbreviation == HeatFluxUnits.PoundForcePerFootSecond:
            return """lbf/(ft·s)"""
        
        if unit_abbreviation == HeatFluxUnits.PoundPerSecondCubed:
            return """lb/s³"""
        
        if unit_abbreviation == HeatFluxUnits.NanowattPerSquareMeter:
            return """nW/m²"""
        
        if unit_abbreviation == HeatFluxUnits.MicrowattPerSquareMeter:
            return """μW/m²"""
        
        if unit_abbreviation == HeatFluxUnits.MilliwattPerSquareMeter:
            return """mW/m²"""
        
        if unit_abbreviation == HeatFluxUnits.CentiwattPerSquareMeter:
            return """cW/m²"""
        
        if unit_abbreviation == HeatFluxUnits.DeciwattPerSquareMeter:
            return """dW/m²"""
        
        if unit_abbreviation == HeatFluxUnits.KilowattPerSquareMeter:
            return """kW/m²"""
        
        if unit_abbreviation == HeatFluxUnits.KilocaloriePerSecondSquareCentimeter:
            return """kcal/s·cm²"""
        
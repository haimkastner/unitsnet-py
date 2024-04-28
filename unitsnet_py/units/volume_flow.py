from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class VolumeFlowUnits(Enum):
        """
            VolumeFlowUnits enumeration
        """
        
        CubicMeterPerSecond = 'CubicMeterPerSecond'
        """
            
        """
        
        CubicMeterPerMinute = 'CubicMeterPerMinute'
        """
            
        """
        
        CubicMeterPerHour = 'CubicMeterPerHour'
        """
            
        """
        
        CubicMeterPerDay = 'CubicMeterPerDay'
        """
            
        """
        
        CubicFootPerSecond = 'CubicFootPerSecond'
        """
            
        """
        
        CubicFootPerMinute = 'CubicFootPerMinute'
        """
            
        """
        
        CubicFootPerHour = 'CubicFootPerHour'
        """
            
        """
        
        CubicYardPerSecond = 'CubicYardPerSecond'
        """
            
        """
        
        CubicYardPerMinute = 'CubicYardPerMinute'
        """
            
        """
        
        CubicYardPerHour = 'CubicYardPerHour'
        """
            
        """
        
        CubicYardPerDay = 'CubicYardPerDay'
        """
            
        """
        
        MillionUsGallonPerDay = 'MillionUsGallonPerDay'
        """
            
        """
        
        UsGallonPerDay = 'UsGallonPerDay'
        """
            
        """
        
        LiterPerSecond = 'LiterPerSecond'
        """
            
        """
        
        LiterPerMinute = 'LiterPerMinute'
        """
            
        """
        
        LiterPerHour = 'LiterPerHour'
        """
            
        """
        
        LiterPerDay = 'LiterPerDay'
        """
            
        """
        
        UsGallonPerSecond = 'UsGallonPerSecond'
        """
            
        """
        
        UsGallonPerMinute = 'UsGallonPerMinute'
        """
            
        """
        
        UkGallonPerDay = 'UkGallonPerDay'
        """
            
        """
        
        UkGallonPerHour = 'UkGallonPerHour'
        """
            
        """
        
        UkGallonPerMinute = 'UkGallonPerMinute'
        """
            
        """
        
        UkGallonPerSecond = 'UkGallonPerSecond'
        """
            
        """
        
        KilousGallonPerMinute = 'KilousGallonPerMinute'
        """
            
        """
        
        UsGallonPerHour = 'UsGallonPerHour'
        """
            
        """
        
        CubicDecimeterPerMinute = 'CubicDecimeterPerMinute'
        """
            
        """
        
        OilBarrelPerDay = 'OilBarrelPerDay'
        """
            
        """
        
        OilBarrelPerMinute = 'OilBarrelPerMinute'
        """
            
        """
        
        OilBarrelPerHour = 'OilBarrelPerHour'
        """
            
        """
        
        OilBarrelPerSecond = 'OilBarrelPerSecond'
        """
            
        """
        
        CubicMillimeterPerSecond = 'CubicMillimeterPerSecond'
        """
            
        """
        
        AcreFootPerSecond = 'AcreFootPerSecond'
        """
            
        """
        
        AcreFootPerMinute = 'AcreFootPerMinute'
        """
            
        """
        
        AcreFootPerHour = 'AcreFootPerHour'
        """
            
        """
        
        AcreFootPerDay = 'AcreFootPerDay'
        """
            
        """
        
        CubicCentimeterPerMinute = 'CubicCentimeterPerMinute'
        """
            
        """
        
        MegausGallonPerDay = 'MegausGallonPerDay'
        """
            
        """
        
        NanoliterPerSecond = 'NanoliterPerSecond'
        """
            
        """
        
        MicroliterPerSecond = 'MicroliterPerSecond'
        """
            
        """
        
        MilliliterPerSecond = 'MilliliterPerSecond'
        """
            
        """
        
        CentiliterPerSecond = 'CentiliterPerSecond'
        """
            
        """
        
        DeciliterPerSecond = 'DeciliterPerSecond'
        """
            
        """
        
        DecaliterPerSecond = 'DecaliterPerSecond'
        """
            
        """
        
        HectoliterPerSecond = 'HectoliterPerSecond'
        """
            
        """
        
        KiloliterPerSecond = 'KiloliterPerSecond'
        """
            
        """
        
        MegaliterPerSecond = 'MegaliterPerSecond'
        """
            
        """
        
        NanoliterPerMinute = 'NanoliterPerMinute'
        """
            
        """
        
        MicroliterPerMinute = 'MicroliterPerMinute'
        """
            
        """
        
        MilliliterPerMinute = 'MilliliterPerMinute'
        """
            
        """
        
        CentiliterPerMinute = 'CentiliterPerMinute'
        """
            
        """
        
        DeciliterPerMinute = 'DeciliterPerMinute'
        """
            
        """
        
        DecaliterPerMinute = 'DecaliterPerMinute'
        """
            
        """
        
        HectoliterPerMinute = 'HectoliterPerMinute'
        """
            
        """
        
        KiloliterPerMinute = 'KiloliterPerMinute'
        """
            
        """
        
        MegaliterPerMinute = 'MegaliterPerMinute'
        """
            
        """
        
        NanoliterPerHour = 'NanoliterPerHour'
        """
            
        """
        
        MicroliterPerHour = 'MicroliterPerHour'
        """
            
        """
        
        MilliliterPerHour = 'MilliliterPerHour'
        """
            
        """
        
        CentiliterPerHour = 'CentiliterPerHour'
        """
            
        """
        
        DeciliterPerHour = 'DeciliterPerHour'
        """
            
        """
        
        DecaliterPerHour = 'DecaliterPerHour'
        """
            
        """
        
        HectoliterPerHour = 'HectoliterPerHour'
        """
            
        """
        
        KiloliterPerHour = 'KiloliterPerHour'
        """
            
        """
        
        MegaliterPerHour = 'MegaliterPerHour'
        """
            
        """
        
        NanoliterPerDay = 'NanoliterPerDay'
        """
            
        """
        
        MicroliterPerDay = 'MicroliterPerDay'
        """
            
        """
        
        MilliliterPerDay = 'MilliliterPerDay'
        """
            
        """
        
        CentiliterPerDay = 'CentiliterPerDay'
        """
            
        """
        
        DeciliterPerDay = 'DeciliterPerDay'
        """
            
        """
        
        DecaliterPerDay = 'DecaliterPerDay'
        """
            
        """
        
        HectoliterPerDay = 'HectoliterPerDay'
        """
            
        """
        
        KiloliterPerDay = 'KiloliterPerDay'
        """
            
        """
        
        MegaliterPerDay = 'MegaliterPerDay'
        """
            
        """
        
        MegaukGallonPerDay = 'MegaukGallonPerDay'
        """
            
        """
        
        MegaukGallonPerSecond = 'MegaukGallonPerSecond'
        """
            
        """
        

class VolumeFlowDto:
    """
    A DTO representation of a VolumeFlow

    Attributes:
        value (float): The value of the VolumeFlow.
        unit (VolumeFlowUnits): The specific unit that the VolumeFlow value is representing.
    """

    def __init__(self, value: float, unit: VolumeFlowUnits):
        """
        Create a new DTO representation of a VolumeFlow

        Parameters:
            value (float): The value of the VolumeFlow.
            unit (VolumeFlowUnits): The specific unit that the VolumeFlow value is representing.
        """
        self.value: float = value
        """
        The value of the VolumeFlow
        """
        self.unit: VolumeFlowUnits = unit
        """
        The specific unit that the VolumeFlow value is representing
        """

    def to_json(self):
        """
        Get a VolumeFlow DTO JSON object representing the current unit.

        :return: JSON object represents VolumeFlow DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "CubicMeterPerSecond"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of VolumeFlow DTO from a json representation.

        :param data: The VolumeFlow DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "CubicMeterPerSecond"}
        :return: A new instance of VolumeFlowDto.
        :rtype: VolumeFlowDto
        """
        return VolumeFlowDto(value=data["value"], unit=VolumeFlowUnits(data["unit"]))


class VolumeFlow(AbstractMeasure):
    """
    In physics and engineering, in particular fluid dynamics and hydrometry, the volumetric flow rate, (also known as volume flow rate, rate of fluid flow or volume velocity) is the volume of fluid which passes through a given surface per unit time. The SI unit is m³/s (cubic meters per second). In US Customary Units and British Imperial Units, volumetric flow rate is often expressed as ft³/s (cubic feet per second). It is usually represented by the symbol Q.

    Args:
        value (float): The value.
        from_unit (VolumeFlowUnits): The VolumeFlow unit to create from, The default unit is CubicMeterPerSecond
    """
    def __init__(self, value: float, from_unit: VolumeFlowUnits = VolumeFlowUnits.CubicMeterPerSecond):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__cubic_meters_per_second = None
        
        self.__cubic_meters_per_minute = None
        
        self.__cubic_meters_per_hour = None
        
        self.__cubic_meters_per_day = None
        
        self.__cubic_feet_per_second = None
        
        self.__cubic_feet_per_minute = None
        
        self.__cubic_feet_per_hour = None
        
        self.__cubic_yards_per_second = None
        
        self.__cubic_yards_per_minute = None
        
        self.__cubic_yards_per_hour = None
        
        self.__cubic_yards_per_day = None
        
        self.__million_us_gallons_per_day = None
        
        self.__us_gallons_per_day = None
        
        self.__liters_per_second = None
        
        self.__liters_per_minute = None
        
        self.__liters_per_hour = None
        
        self.__liters_per_day = None
        
        self.__us_gallons_per_second = None
        
        self.__us_gallons_per_minute = None
        
        self.__uk_gallons_per_day = None
        
        self.__uk_gallons_per_hour = None
        
        self.__uk_gallons_per_minute = None
        
        self.__uk_gallons_per_second = None
        
        self.__kilous_gallons_per_minute = None
        
        self.__us_gallons_per_hour = None
        
        self.__cubic_decimeters_per_minute = None
        
        self.__oil_barrels_per_day = None
        
        self.__oil_barrels_per_minute = None
        
        self.__oil_barrels_per_hour = None
        
        self.__oil_barrels_per_second = None
        
        self.__cubic_millimeters_per_second = None
        
        self.__acre_feet_per_second = None
        
        self.__acre_feet_per_minute = None
        
        self.__acre_feet_per_hour = None
        
        self.__acre_feet_per_day = None
        
        self.__cubic_centimeters_per_minute = None
        
        self.__megaus_gallons_per_day = None
        
        self.__nanoliters_per_second = None
        
        self.__microliters_per_second = None
        
        self.__milliliters_per_second = None
        
        self.__centiliters_per_second = None
        
        self.__deciliters_per_second = None
        
        self.__decaliters_per_second = None
        
        self.__hectoliters_per_second = None
        
        self.__kiloliters_per_second = None
        
        self.__megaliters_per_second = None
        
        self.__nanoliters_per_minute = None
        
        self.__microliters_per_minute = None
        
        self.__milliliters_per_minute = None
        
        self.__centiliters_per_minute = None
        
        self.__deciliters_per_minute = None
        
        self.__decaliters_per_minute = None
        
        self.__hectoliters_per_minute = None
        
        self.__kiloliters_per_minute = None
        
        self.__megaliters_per_minute = None
        
        self.__nanoliters_per_hour = None
        
        self.__microliters_per_hour = None
        
        self.__milliliters_per_hour = None
        
        self.__centiliters_per_hour = None
        
        self.__deciliters_per_hour = None
        
        self.__decaliters_per_hour = None
        
        self.__hectoliters_per_hour = None
        
        self.__kiloliters_per_hour = None
        
        self.__megaliters_per_hour = None
        
        self.__nanoliters_per_day = None
        
        self.__microliters_per_day = None
        
        self.__milliliters_per_day = None
        
        self.__centiliters_per_day = None
        
        self.__deciliters_per_day = None
        
        self.__decaliters_per_day = None
        
        self.__hectoliters_per_day = None
        
        self.__kiloliters_per_day = None
        
        self.__megaliters_per_day = None
        
        self.__megauk_gallons_per_day = None
        
        self.__megauk_gallons_per_second = None
        

    def convert(self, unit: VolumeFlowUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: VolumeFlowUnits = VolumeFlowUnits.CubicMeterPerSecond) -> VolumeFlowDto:
        """
        Get a new instance of VolumeFlow DTO representing the current unit.

        :param hold_in_unit: The specific VolumeFlow unit to store the VolumeFlow value in the DTO representation.
        :type hold_in_unit: VolumeFlowUnits
        :return: A new instance of VolumeFlowDto.
        :rtype: VolumeFlowDto
        """
        return VolumeFlowDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: VolumeFlowUnits = VolumeFlowUnits.CubicMeterPerSecond):
        """
        Get a VolumeFlow DTO JSON object representing the current unit.

        :param hold_in_unit: The specific VolumeFlow unit to store the VolumeFlow value in the DTO representation.
        :type hold_in_unit: VolumeFlowUnits
        :return: JSON object represents VolumeFlow DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "CubicMeterPerSecond"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(volume_flow_dto: VolumeFlowDto):
        """
        Obtain a new instance of VolumeFlow from a DTO unit object.

        :param volume_flow_dto: The VolumeFlow DTO representation.
        :type volume_flow_dto: VolumeFlowDto
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(volume_flow_dto.value, volume_flow_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of VolumeFlow from a DTO unit json representation.

        :param data: The VolumeFlow DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "CubicMeterPerSecond"}
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow.from_dto(VolumeFlowDto.from_json(data))

    def __convert_from_base(self, from_unit: VolumeFlowUnits) -> float:
        value = self._value
        
        if from_unit == VolumeFlowUnits.CubicMeterPerSecond:
            return (value)
        
        if from_unit == VolumeFlowUnits.CubicMeterPerMinute:
            return (value * 60)
        
        if from_unit == VolumeFlowUnits.CubicMeterPerHour:
            return (value * 3600)
        
        if from_unit == VolumeFlowUnits.CubicMeterPerDay:
            return (value * 86400)
        
        if from_unit == VolumeFlowUnits.CubicFootPerSecond:
            return (value * 35.314666721)
        
        if from_unit == VolumeFlowUnits.CubicFootPerMinute:
            return (value * 2118.88000326)
        
        if from_unit == VolumeFlowUnits.CubicFootPerHour:
            return (value / 7.8657907199999087346816086183876e-6)
        
        if from_unit == VolumeFlowUnits.CubicYardPerSecond:
            return (value / 0.764554857984)
        
        if from_unit == VolumeFlowUnits.CubicYardPerMinute:
            return (value / 0.0127425809664)
        
        if from_unit == VolumeFlowUnits.CubicYardPerHour:
            return (value / 2.1237634944e-4)
        
        if from_unit == VolumeFlowUnits.CubicYardPerDay:
            return (value * 113007)
        
        if from_unit == VolumeFlowUnits.MillionUsGallonPerDay:
            return (value * 22.824465227)
        
        if from_unit == VolumeFlowUnits.UsGallonPerDay:
            return (value * 22824465.227)
        
        if from_unit == VolumeFlowUnits.LiterPerSecond:
            return (value * 1000)
        
        if from_unit == VolumeFlowUnits.LiterPerMinute:
            return (value * 60000.00000)
        
        if from_unit == VolumeFlowUnits.LiterPerHour:
            return (value * 3600000.000)
        
        if from_unit == VolumeFlowUnits.LiterPerDay:
            return (value * 86400000)
        
        if from_unit == VolumeFlowUnits.UsGallonPerSecond:
            return (value * 264.1720523581484)
        
        if from_unit == VolumeFlowUnits.UsGallonPerMinute:
            return (value * 15850.323141489)
        
        if from_unit == VolumeFlowUnits.UkGallonPerDay:
            return (value * 19005304)
        
        if from_unit == VolumeFlowUnits.UkGallonPerHour:
            return (value * 791887.667)
        
        if from_unit == VolumeFlowUnits.UkGallonPerMinute:
            return (value * 13198.2)
        
        if from_unit == VolumeFlowUnits.UkGallonPerSecond:
            return (value * 219.969)
        
        if from_unit == VolumeFlowUnits.KilousGallonPerMinute:
            return (value * 15.850323141489)
        
        if from_unit == VolumeFlowUnits.UsGallonPerHour:
            return (value * 951019.38848933424)
        
        if from_unit == VolumeFlowUnits.CubicDecimeterPerMinute:
            return (value * 60000.00000)
        
        if from_unit == VolumeFlowUnits.OilBarrelPerDay:
            return (value / 1.8401307283333333333333333333333e-6)
        
        if from_unit == VolumeFlowUnits.OilBarrelPerMinute:
            return (value / 2.64978825e-3)
        
        if from_unit == VolumeFlowUnits.OilBarrelPerHour:
            return (value / 4.41631375e-5)
        
        if from_unit == VolumeFlowUnits.OilBarrelPerSecond:
            return (value * 6.28981)
        
        if from_unit == VolumeFlowUnits.CubicMillimeterPerSecond:
            return (value / 1e-9)
        
        if from_unit == VolumeFlowUnits.AcreFootPerSecond:
            return (value * 0.000810713194)
        
        if from_unit == VolumeFlowUnits.AcreFootPerMinute:
            return (value * 0.0486427916)
        
        if from_unit == VolumeFlowUnits.AcreFootPerHour:
            return (value * 2.91857)
        
        if from_unit == VolumeFlowUnits.AcreFootPerDay:
            return (value * 70.0457)
        
        if from_unit == VolumeFlowUnits.CubicCentimeterPerMinute:
            return (value / 1.6666666666667e-8)
        
        if from_unit == VolumeFlowUnits.MegausGallonPerDay:
            return ((value * 22824465.227) / 1000000.0)
        
        if from_unit == VolumeFlowUnits.NanoliterPerSecond:
            return ((value * 1000) / 1e-09)
        
        if from_unit == VolumeFlowUnits.MicroliterPerSecond:
            return ((value * 1000) / 1e-06)
        
        if from_unit == VolumeFlowUnits.MilliliterPerSecond:
            return ((value * 1000) / 0.001)
        
        if from_unit == VolumeFlowUnits.CentiliterPerSecond:
            return ((value * 1000) / 0.01)
        
        if from_unit == VolumeFlowUnits.DeciliterPerSecond:
            return ((value * 1000) / 0.1)
        
        if from_unit == VolumeFlowUnits.DecaliterPerSecond:
            return ((value * 1000) / 10.0)
        
        if from_unit == VolumeFlowUnits.HectoliterPerSecond:
            return ((value * 1000) / 100.0)
        
        if from_unit == VolumeFlowUnits.KiloliterPerSecond:
            return ((value * 1000) / 1000.0)
        
        if from_unit == VolumeFlowUnits.MegaliterPerSecond:
            return ((value * 1000) / 1000000.0)
        
        if from_unit == VolumeFlowUnits.NanoliterPerMinute:
            return ((value * 60000.00000) / 1e-09)
        
        if from_unit == VolumeFlowUnits.MicroliterPerMinute:
            return ((value * 60000.00000) / 1e-06)
        
        if from_unit == VolumeFlowUnits.MilliliterPerMinute:
            return ((value * 60000.00000) / 0.001)
        
        if from_unit == VolumeFlowUnits.CentiliterPerMinute:
            return ((value * 60000.00000) / 0.01)
        
        if from_unit == VolumeFlowUnits.DeciliterPerMinute:
            return ((value * 60000.00000) / 0.1)
        
        if from_unit == VolumeFlowUnits.DecaliterPerMinute:
            return ((value * 60000.00000) / 10.0)
        
        if from_unit == VolumeFlowUnits.HectoliterPerMinute:
            return ((value * 60000.00000) / 100.0)
        
        if from_unit == VolumeFlowUnits.KiloliterPerMinute:
            return ((value * 60000.00000) / 1000.0)
        
        if from_unit == VolumeFlowUnits.MegaliterPerMinute:
            return ((value * 60000.00000) / 1000000.0)
        
        if from_unit == VolumeFlowUnits.NanoliterPerHour:
            return ((value * 3600000.000) / 1e-09)
        
        if from_unit == VolumeFlowUnits.MicroliterPerHour:
            return ((value * 3600000.000) / 1e-06)
        
        if from_unit == VolumeFlowUnits.MilliliterPerHour:
            return ((value * 3600000.000) / 0.001)
        
        if from_unit == VolumeFlowUnits.CentiliterPerHour:
            return ((value * 3600000.000) / 0.01)
        
        if from_unit == VolumeFlowUnits.DeciliterPerHour:
            return ((value * 3600000.000) / 0.1)
        
        if from_unit == VolumeFlowUnits.DecaliterPerHour:
            return ((value * 3600000.000) / 10.0)
        
        if from_unit == VolumeFlowUnits.HectoliterPerHour:
            return ((value * 3600000.000) / 100.0)
        
        if from_unit == VolumeFlowUnits.KiloliterPerHour:
            return ((value * 3600000.000) / 1000.0)
        
        if from_unit == VolumeFlowUnits.MegaliterPerHour:
            return ((value * 3600000.000) / 1000000.0)
        
        if from_unit == VolumeFlowUnits.NanoliterPerDay:
            return ((value * 86400000) / 1e-09)
        
        if from_unit == VolumeFlowUnits.MicroliterPerDay:
            return ((value * 86400000) / 1e-06)
        
        if from_unit == VolumeFlowUnits.MilliliterPerDay:
            return ((value * 86400000) / 0.001)
        
        if from_unit == VolumeFlowUnits.CentiliterPerDay:
            return ((value * 86400000) / 0.01)
        
        if from_unit == VolumeFlowUnits.DeciliterPerDay:
            return ((value * 86400000) / 0.1)
        
        if from_unit == VolumeFlowUnits.DecaliterPerDay:
            return ((value * 86400000) / 10.0)
        
        if from_unit == VolumeFlowUnits.HectoliterPerDay:
            return ((value * 86400000) / 100.0)
        
        if from_unit == VolumeFlowUnits.KiloliterPerDay:
            return ((value * 86400000) / 1000.0)
        
        if from_unit == VolumeFlowUnits.MegaliterPerDay:
            return ((value * 86400000) / 1000000.0)
        
        if from_unit == VolumeFlowUnits.MegaukGallonPerDay:
            return ((value * 19005304) / 1000000.0)
        
        if from_unit == VolumeFlowUnits.MegaukGallonPerSecond:
            return ((value * 219.969) / 1000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: VolumeFlowUnits) -> float:
        
        if to_unit == VolumeFlowUnits.CubicMeterPerSecond:
            return (value)
        
        if to_unit == VolumeFlowUnits.CubicMeterPerMinute:
            return (value / 60)
        
        if to_unit == VolumeFlowUnits.CubicMeterPerHour:
            return (value / 3600)
        
        if to_unit == VolumeFlowUnits.CubicMeterPerDay:
            return (value / 86400)
        
        if to_unit == VolumeFlowUnits.CubicFootPerSecond:
            return (value / 35.314666721)
        
        if to_unit == VolumeFlowUnits.CubicFootPerMinute:
            return (value / 2118.88000326)
        
        if to_unit == VolumeFlowUnits.CubicFootPerHour:
            return (value * 7.8657907199999087346816086183876e-6)
        
        if to_unit == VolumeFlowUnits.CubicYardPerSecond:
            return (value * 0.764554857984)
        
        if to_unit == VolumeFlowUnits.CubicYardPerMinute:
            return (value * 0.0127425809664)
        
        if to_unit == VolumeFlowUnits.CubicYardPerHour:
            return (value * 2.1237634944e-4)
        
        if to_unit == VolumeFlowUnits.CubicYardPerDay:
            return (value / 113007)
        
        if to_unit == VolumeFlowUnits.MillionUsGallonPerDay:
            return (value / 22.824465227)
        
        if to_unit == VolumeFlowUnits.UsGallonPerDay:
            return (value / 22824465.227)
        
        if to_unit == VolumeFlowUnits.LiterPerSecond:
            return (value / 1000)
        
        if to_unit == VolumeFlowUnits.LiterPerMinute:
            return (value / 60000.00000)
        
        if to_unit == VolumeFlowUnits.LiterPerHour:
            return (value / 3600000.000)
        
        if to_unit == VolumeFlowUnits.LiterPerDay:
            return (value / 86400000)
        
        if to_unit == VolumeFlowUnits.UsGallonPerSecond:
            return (value / 264.1720523581484)
        
        if to_unit == VolumeFlowUnits.UsGallonPerMinute:
            return (value / 15850.323141489)
        
        if to_unit == VolumeFlowUnits.UkGallonPerDay:
            return (value / 19005304)
        
        if to_unit == VolumeFlowUnits.UkGallonPerHour:
            return (value / 791887.667)
        
        if to_unit == VolumeFlowUnits.UkGallonPerMinute:
            return (value / 13198.2)
        
        if to_unit == VolumeFlowUnits.UkGallonPerSecond:
            return (value / 219.969)
        
        if to_unit == VolumeFlowUnits.KilousGallonPerMinute:
            return (value / 15.850323141489)
        
        if to_unit == VolumeFlowUnits.UsGallonPerHour:
            return (value / 951019.38848933424)
        
        if to_unit == VolumeFlowUnits.CubicDecimeterPerMinute:
            return (value / 60000.00000)
        
        if to_unit == VolumeFlowUnits.OilBarrelPerDay:
            return (value * 1.8401307283333333333333333333333e-6)
        
        if to_unit == VolumeFlowUnits.OilBarrelPerMinute:
            return (value * 2.64978825e-3)
        
        if to_unit == VolumeFlowUnits.OilBarrelPerHour:
            return (value * 4.41631375e-5)
        
        if to_unit == VolumeFlowUnits.OilBarrelPerSecond:
            return (value / 6.28981)
        
        if to_unit == VolumeFlowUnits.CubicMillimeterPerSecond:
            return (value * 1e-9)
        
        if to_unit == VolumeFlowUnits.AcreFootPerSecond:
            return (value / 0.000810713194)
        
        if to_unit == VolumeFlowUnits.AcreFootPerMinute:
            return (value / 0.0486427916)
        
        if to_unit == VolumeFlowUnits.AcreFootPerHour:
            return (value / 2.91857)
        
        if to_unit == VolumeFlowUnits.AcreFootPerDay:
            return (value / 70.0457)
        
        if to_unit == VolumeFlowUnits.CubicCentimeterPerMinute:
            return (value * 1.6666666666667e-8)
        
        if to_unit == VolumeFlowUnits.MegausGallonPerDay:
            return ((value / 22824465.227) * 1000000.0)
        
        if to_unit == VolumeFlowUnits.NanoliterPerSecond:
            return ((value / 1000) * 1e-09)
        
        if to_unit == VolumeFlowUnits.MicroliterPerSecond:
            return ((value / 1000) * 1e-06)
        
        if to_unit == VolumeFlowUnits.MilliliterPerSecond:
            return ((value / 1000) * 0.001)
        
        if to_unit == VolumeFlowUnits.CentiliterPerSecond:
            return ((value / 1000) * 0.01)
        
        if to_unit == VolumeFlowUnits.DeciliterPerSecond:
            return ((value / 1000) * 0.1)
        
        if to_unit == VolumeFlowUnits.DecaliterPerSecond:
            return ((value / 1000) * 10.0)
        
        if to_unit == VolumeFlowUnits.HectoliterPerSecond:
            return ((value / 1000) * 100.0)
        
        if to_unit == VolumeFlowUnits.KiloliterPerSecond:
            return ((value / 1000) * 1000.0)
        
        if to_unit == VolumeFlowUnits.MegaliterPerSecond:
            return ((value / 1000) * 1000000.0)
        
        if to_unit == VolumeFlowUnits.NanoliterPerMinute:
            return ((value / 60000.00000) * 1e-09)
        
        if to_unit == VolumeFlowUnits.MicroliterPerMinute:
            return ((value / 60000.00000) * 1e-06)
        
        if to_unit == VolumeFlowUnits.MilliliterPerMinute:
            return ((value / 60000.00000) * 0.001)
        
        if to_unit == VolumeFlowUnits.CentiliterPerMinute:
            return ((value / 60000.00000) * 0.01)
        
        if to_unit == VolumeFlowUnits.DeciliterPerMinute:
            return ((value / 60000.00000) * 0.1)
        
        if to_unit == VolumeFlowUnits.DecaliterPerMinute:
            return ((value / 60000.00000) * 10.0)
        
        if to_unit == VolumeFlowUnits.HectoliterPerMinute:
            return ((value / 60000.00000) * 100.0)
        
        if to_unit == VolumeFlowUnits.KiloliterPerMinute:
            return ((value / 60000.00000) * 1000.0)
        
        if to_unit == VolumeFlowUnits.MegaliterPerMinute:
            return ((value / 60000.00000) * 1000000.0)
        
        if to_unit == VolumeFlowUnits.NanoliterPerHour:
            return ((value / 3600000.000) * 1e-09)
        
        if to_unit == VolumeFlowUnits.MicroliterPerHour:
            return ((value / 3600000.000) * 1e-06)
        
        if to_unit == VolumeFlowUnits.MilliliterPerHour:
            return ((value / 3600000.000) * 0.001)
        
        if to_unit == VolumeFlowUnits.CentiliterPerHour:
            return ((value / 3600000.000) * 0.01)
        
        if to_unit == VolumeFlowUnits.DeciliterPerHour:
            return ((value / 3600000.000) * 0.1)
        
        if to_unit == VolumeFlowUnits.DecaliterPerHour:
            return ((value / 3600000.000) * 10.0)
        
        if to_unit == VolumeFlowUnits.HectoliterPerHour:
            return ((value / 3600000.000) * 100.0)
        
        if to_unit == VolumeFlowUnits.KiloliterPerHour:
            return ((value / 3600000.000) * 1000.0)
        
        if to_unit == VolumeFlowUnits.MegaliterPerHour:
            return ((value / 3600000.000) * 1000000.0)
        
        if to_unit == VolumeFlowUnits.NanoliterPerDay:
            return ((value / 86400000) * 1e-09)
        
        if to_unit == VolumeFlowUnits.MicroliterPerDay:
            return ((value / 86400000) * 1e-06)
        
        if to_unit == VolumeFlowUnits.MilliliterPerDay:
            return ((value / 86400000) * 0.001)
        
        if to_unit == VolumeFlowUnits.CentiliterPerDay:
            return ((value / 86400000) * 0.01)
        
        if to_unit == VolumeFlowUnits.DeciliterPerDay:
            return ((value / 86400000) * 0.1)
        
        if to_unit == VolumeFlowUnits.DecaliterPerDay:
            return ((value / 86400000) * 10.0)
        
        if to_unit == VolumeFlowUnits.HectoliterPerDay:
            return ((value / 86400000) * 100.0)
        
        if to_unit == VolumeFlowUnits.KiloliterPerDay:
            return ((value / 86400000) * 1000.0)
        
        if to_unit == VolumeFlowUnits.MegaliterPerDay:
            return ((value / 86400000) * 1000000.0)
        
        if to_unit == VolumeFlowUnits.MegaukGallonPerDay:
            return ((value / 19005304) * 1000000.0)
        
        if to_unit == VolumeFlowUnits.MegaukGallonPerSecond:
            return ((value / 219.969) * 1000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_cubic_meters_per_second(cubic_meters_per_second: float):
        """
        Create a new instance of VolumeFlow from a value in cubic_meters_per_second.

        

        :param meters: The VolumeFlow value in cubic_meters_per_second.
        :type cubic_meters_per_second: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(cubic_meters_per_second, VolumeFlowUnits.CubicMeterPerSecond)

    
    @staticmethod
    def from_cubic_meters_per_minute(cubic_meters_per_minute: float):
        """
        Create a new instance of VolumeFlow from a value in cubic_meters_per_minute.

        

        :param meters: The VolumeFlow value in cubic_meters_per_minute.
        :type cubic_meters_per_minute: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(cubic_meters_per_minute, VolumeFlowUnits.CubicMeterPerMinute)

    
    @staticmethod
    def from_cubic_meters_per_hour(cubic_meters_per_hour: float):
        """
        Create a new instance of VolumeFlow from a value in cubic_meters_per_hour.

        

        :param meters: The VolumeFlow value in cubic_meters_per_hour.
        :type cubic_meters_per_hour: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(cubic_meters_per_hour, VolumeFlowUnits.CubicMeterPerHour)

    
    @staticmethod
    def from_cubic_meters_per_day(cubic_meters_per_day: float):
        """
        Create a new instance of VolumeFlow from a value in cubic_meters_per_day.

        

        :param meters: The VolumeFlow value in cubic_meters_per_day.
        :type cubic_meters_per_day: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(cubic_meters_per_day, VolumeFlowUnits.CubicMeterPerDay)

    
    @staticmethod
    def from_cubic_feet_per_second(cubic_feet_per_second: float):
        """
        Create a new instance of VolumeFlow from a value in cubic_feet_per_second.

        

        :param meters: The VolumeFlow value in cubic_feet_per_second.
        :type cubic_feet_per_second: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(cubic_feet_per_second, VolumeFlowUnits.CubicFootPerSecond)

    
    @staticmethod
    def from_cubic_feet_per_minute(cubic_feet_per_minute: float):
        """
        Create a new instance of VolumeFlow from a value in cubic_feet_per_minute.

        

        :param meters: The VolumeFlow value in cubic_feet_per_minute.
        :type cubic_feet_per_minute: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(cubic_feet_per_minute, VolumeFlowUnits.CubicFootPerMinute)

    
    @staticmethod
    def from_cubic_feet_per_hour(cubic_feet_per_hour: float):
        """
        Create a new instance of VolumeFlow from a value in cubic_feet_per_hour.

        

        :param meters: The VolumeFlow value in cubic_feet_per_hour.
        :type cubic_feet_per_hour: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(cubic_feet_per_hour, VolumeFlowUnits.CubicFootPerHour)

    
    @staticmethod
    def from_cubic_yards_per_second(cubic_yards_per_second: float):
        """
        Create a new instance of VolumeFlow from a value in cubic_yards_per_second.

        

        :param meters: The VolumeFlow value in cubic_yards_per_second.
        :type cubic_yards_per_second: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(cubic_yards_per_second, VolumeFlowUnits.CubicYardPerSecond)

    
    @staticmethod
    def from_cubic_yards_per_minute(cubic_yards_per_minute: float):
        """
        Create a new instance of VolumeFlow from a value in cubic_yards_per_minute.

        

        :param meters: The VolumeFlow value in cubic_yards_per_minute.
        :type cubic_yards_per_minute: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(cubic_yards_per_minute, VolumeFlowUnits.CubicYardPerMinute)

    
    @staticmethod
    def from_cubic_yards_per_hour(cubic_yards_per_hour: float):
        """
        Create a new instance of VolumeFlow from a value in cubic_yards_per_hour.

        

        :param meters: The VolumeFlow value in cubic_yards_per_hour.
        :type cubic_yards_per_hour: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(cubic_yards_per_hour, VolumeFlowUnits.CubicYardPerHour)

    
    @staticmethod
    def from_cubic_yards_per_day(cubic_yards_per_day: float):
        """
        Create a new instance of VolumeFlow from a value in cubic_yards_per_day.

        

        :param meters: The VolumeFlow value in cubic_yards_per_day.
        :type cubic_yards_per_day: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(cubic_yards_per_day, VolumeFlowUnits.CubicYardPerDay)

    
    @staticmethod
    def from_million_us_gallons_per_day(million_us_gallons_per_day: float):
        """
        Create a new instance of VolumeFlow from a value in million_us_gallons_per_day.

        

        :param meters: The VolumeFlow value in million_us_gallons_per_day.
        :type million_us_gallons_per_day: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(million_us_gallons_per_day, VolumeFlowUnits.MillionUsGallonPerDay)

    
    @staticmethod
    def from_us_gallons_per_day(us_gallons_per_day: float):
        """
        Create a new instance of VolumeFlow from a value in us_gallons_per_day.

        

        :param meters: The VolumeFlow value in us_gallons_per_day.
        :type us_gallons_per_day: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(us_gallons_per_day, VolumeFlowUnits.UsGallonPerDay)

    
    @staticmethod
    def from_liters_per_second(liters_per_second: float):
        """
        Create a new instance of VolumeFlow from a value in liters_per_second.

        

        :param meters: The VolumeFlow value in liters_per_second.
        :type liters_per_second: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(liters_per_second, VolumeFlowUnits.LiterPerSecond)

    
    @staticmethod
    def from_liters_per_minute(liters_per_minute: float):
        """
        Create a new instance of VolumeFlow from a value in liters_per_minute.

        

        :param meters: The VolumeFlow value in liters_per_minute.
        :type liters_per_minute: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(liters_per_minute, VolumeFlowUnits.LiterPerMinute)

    
    @staticmethod
    def from_liters_per_hour(liters_per_hour: float):
        """
        Create a new instance of VolumeFlow from a value in liters_per_hour.

        

        :param meters: The VolumeFlow value in liters_per_hour.
        :type liters_per_hour: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(liters_per_hour, VolumeFlowUnits.LiterPerHour)

    
    @staticmethod
    def from_liters_per_day(liters_per_day: float):
        """
        Create a new instance of VolumeFlow from a value in liters_per_day.

        

        :param meters: The VolumeFlow value in liters_per_day.
        :type liters_per_day: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(liters_per_day, VolumeFlowUnits.LiterPerDay)

    
    @staticmethod
    def from_us_gallons_per_second(us_gallons_per_second: float):
        """
        Create a new instance of VolumeFlow from a value in us_gallons_per_second.

        

        :param meters: The VolumeFlow value in us_gallons_per_second.
        :type us_gallons_per_second: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(us_gallons_per_second, VolumeFlowUnits.UsGallonPerSecond)

    
    @staticmethod
    def from_us_gallons_per_minute(us_gallons_per_minute: float):
        """
        Create a new instance of VolumeFlow from a value in us_gallons_per_minute.

        

        :param meters: The VolumeFlow value in us_gallons_per_minute.
        :type us_gallons_per_minute: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(us_gallons_per_minute, VolumeFlowUnits.UsGallonPerMinute)

    
    @staticmethod
    def from_uk_gallons_per_day(uk_gallons_per_day: float):
        """
        Create a new instance of VolumeFlow from a value in uk_gallons_per_day.

        

        :param meters: The VolumeFlow value in uk_gallons_per_day.
        :type uk_gallons_per_day: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(uk_gallons_per_day, VolumeFlowUnits.UkGallonPerDay)

    
    @staticmethod
    def from_uk_gallons_per_hour(uk_gallons_per_hour: float):
        """
        Create a new instance of VolumeFlow from a value in uk_gallons_per_hour.

        

        :param meters: The VolumeFlow value in uk_gallons_per_hour.
        :type uk_gallons_per_hour: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(uk_gallons_per_hour, VolumeFlowUnits.UkGallonPerHour)

    
    @staticmethod
    def from_uk_gallons_per_minute(uk_gallons_per_minute: float):
        """
        Create a new instance of VolumeFlow from a value in uk_gallons_per_minute.

        

        :param meters: The VolumeFlow value in uk_gallons_per_minute.
        :type uk_gallons_per_minute: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(uk_gallons_per_minute, VolumeFlowUnits.UkGallonPerMinute)

    
    @staticmethod
    def from_uk_gallons_per_second(uk_gallons_per_second: float):
        """
        Create a new instance of VolumeFlow from a value in uk_gallons_per_second.

        

        :param meters: The VolumeFlow value in uk_gallons_per_second.
        :type uk_gallons_per_second: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(uk_gallons_per_second, VolumeFlowUnits.UkGallonPerSecond)

    
    @staticmethod
    def from_kilous_gallons_per_minute(kilous_gallons_per_minute: float):
        """
        Create a new instance of VolumeFlow from a value in kilous_gallons_per_minute.

        

        :param meters: The VolumeFlow value in kilous_gallons_per_minute.
        :type kilous_gallons_per_minute: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(kilous_gallons_per_minute, VolumeFlowUnits.KilousGallonPerMinute)

    
    @staticmethod
    def from_us_gallons_per_hour(us_gallons_per_hour: float):
        """
        Create a new instance of VolumeFlow from a value in us_gallons_per_hour.

        

        :param meters: The VolumeFlow value in us_gallons_per_hour.
        :type us_gallons_per_hour: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(us_gallons_per_hour, VolumeFlowUnits.UsGallonPerHour)

    
    @staticmethod
    def from_cubic_decimeters_per_minute(cubic_decimeters_per_minute: float):
        """
        Create a new instance of VolumeFlow from a value in cubic_decimeters_per_minute.

        

        :param meters: The VolumeFlow value in cubic_decimeters_per_minute.
        :type cubic_decimeters_per_minute: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(cubic_decimeters_per_minute, VolumeFlowUnits.CubicDecimeterPerMinute)

    
    @staticmethod
    def from_oil_barrels_per_day(oil_barrels_per_day: float):
        """
        Create a new instance of VolumeFlow from a value in oil_barrels_per_day.

        

        :param meters: The VolumeFlow value in oil_barrels_per_day.
        :type oil_barrels_per_day: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(oil_barrels_per_day, VolumeFlowUnits.OilBarrelPerDay)

    
    @staticmethod
    def from_oil_barrels_per_minute(oil_barrels_per_minute: float):
        """
        Create a new instance of VolumeFlow from a value in oil_barrels_per_minute.

        

        :param meters: The VolumeFlow value in oil_barrels_per_minute.
        :type oil_barrels_per_minute: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(oil_barrels_per_minute, VolumeFlowUnits.OilBarrelPerMinute)

    
    @staticmethod
    def from_oil_barrels_per_hour(oil_barrels_per_hour: float):
        """
        Create a new instance of VolumeFlow from a value in oil_barrels_per_hour.

        

        :param meters: The VolumeFlow value in oil_barrels_per_hour.
        :type oil_barrels_per_hour: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(oil_barrels_per_hour, VolumeFlowUnits.OilBarrelPerHour)

    
    @staticmethod
    def from_oil_barrels_per_second(oil_barrels_per_second: float):
        """
        Create a new instance of VolumeFlow from a value in oil_barrels_per_second.

        

        :param meters: The VolumeFlow value in oil_barrels_per_second.
        :type oil_barrels_per_second: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(oil_barrels_per_second, VolumeFlowUnits.OilBarrelPerSecond)

    
    @staticmethod
    def from_cubic_millimeters_per_second(cubic_millimeters_per_second: float):
        """
        Create a new instance of VolumeFlow from a value in cubic_millimeters_per_second.

        

        :param meters: The VolumeFlow value in cubic_millimeters_per_second.
        :type cubic_millimeters_per_second: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(cubic_millimeters_per_second, VolumeFlowUnits.CubicMillimeterPerSecond)

    
    @staticmethod
    def from_acre_feet_per_second(acre_feet_per_second: float):
        """
        Create a new instance of VolumeFlow from a value in acre_feet_per_second.

        

        :param meters: The VolumeFlow value in acre_feet_per_second.
        :type acre_feet_per_second: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(acre_feet_per_second, VolumeFlowUnits.AcreFootPerSecond)

    
    @staticmethod
    def from_acre_feet_per_minute(acre_feet_per_minute: float):
        """
        Create a new instance of VolumeFlow from a value in acre_feet_per_minute.

        

        :param meters: The VolumeFlow value in acre_feet_per_minute.
        :type acre_feet_per_minute: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(acre_feet_per_minute, VolumeFlowUnits.AcreFootPerMinute)

    
    @staticmethod
    def from_acre_feet_per_hour(acre_feet_per_hour: float):
        """
        Create a new instance of VolumeFlow from a value in acre_feet_per_hour.

        

        :param meters: The VolumeFlow value in acre_feet_per_hour.
        :type acre_feet_per_hour: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(acre_feet_per_hour, VolumeFlowUnits.AcreFootPerHour)

    
    @staticmethod
    def from_acre_feet_per_day(acre_feet_per_day: float):
        """
        Create a new instance of VolumeFlow from a value in acre_feet_per_day.

        

        :param meters: The VolumeFlow value in acre_feet_per_day.
        :type acre_feet_per_day: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(acre_feet_per_day, VolumeFlowUnits.AcreFootPerDay)

    
    @staticmethod
    def from_cubic_centimeters_per_minute(cubic_centimeters_per_minute: float):
        """
        Create a new instance of VolumeFlow from a value in cubic_centimeters_per_minute.

        

        :param meters: The VolumeFlow value in cubic_centimeters_per_minute.
        :type cubic_centimeters_per_minute: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(cubic_centimeters_per_minute, VolumeFlowUnits.CubicCentimeterPerMinute)

    
    @staticmethod
    def from_megaus_gallons_per_day(megaus_gallons_per_day: float):
        """
        Create a new instance of VolumeFlow from a value in megaus_gallons_per_day.

        

        :param meters: The VolumeFlow value in megaus_gallons_per_day.
        :type megaus_gallons_per_day: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(megaus_gallons_per_day, VolumeFlowUnits.MegausGallonPerDay)

    
    @staticmethod
    def from_nanoliters_per_second(nanoliters_per_second: float):
        """
        Create a new instance of VolumeFlow from a value in nanoliters_per_second.

        

        :param meters: The VolumeFlow value in nanoliters_per_second.
        :type nanoliters_per_second: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(nanoliters_per_second, VolumeFlowUnits.NanoliterPerSecond)

    
    @staticmethod
    def from_microliters_per_second(microliters_per_second: float):
        """
        Create a new instance of VolumeFlow from a value in microliters_per_second.

        

        :param meters: The VolumeFlow value in microliters_per_second.
        :type microliters_per_second: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(microliters_per_second, VolumeFlowUnits.MicroliterPerSecond)

    
    @staticmethod
    def from_milliliters_per_second(milliliters_per_second: float):
        """
        Create a new instance of VolumeFlow from a value in milliliters_per_second.

        

        :param meters: The VolumeFlow value in milliliters_per_second.
        :type milliliters_per_second: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(milliliters_per_second, VolumeFlowUnits.MilliliterPerSecond)

    
    @staticmethod
    def from_centiliters_per_second(centiliters_per_second: float):
        """
        Create a new instance of VolumeFlow from a value in centiliters_per_second.

        

        :param meters: The VolumeFlow value in centiliters_per_second.
        :type centiliters_per_second: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(centiliters_per_second, VolumeFlowUnits.CentiliterPerSecond)

    
    @staticmethod
    def from_deciliters_per_second(deciliters_per_second: float):
        """
        Create a new instance of VolumeFlow from a value in deciliters_per_second.

        

        :param meters: The VolumeFlow value in deciliters_per_second.
        :type deciliters_per_second: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(deciliters_per_second, VolumeFlowUnits.DeciliterPerSecond)

    
    @staticmethod
    def from_decaliters_per_second(decaliters_per_second: float):
        """
        Create a new instance of VolumeFlow from a value in decaliters_per_second.

        

        :param meters: The VolumeFlow value in decaliters_per_second.
        :type decaliters_per_second: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(decaliters_per_second, VolumeFlowUnits.DecaliterPerSecond)

    
    @staticmethod
    def from_hectoliters_per_second(hectoliters_per_second: float):
        """
        Create a new instance of VolumeFlow from a value in hectoliters_per_second.

        

        :param meters: The VolumeFlow value in hectoliters_per_second.
        :type hectoliters_per_second: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(hectoliters_per_second, VolumeFlowUnits.HectoliterPerSecond)

    
    @staticmethod
    def from_kiloliters_per_second(kiloliters_per_second: float):
        """
        Create a new instance of VolumeFlow from a value in kiloliters_per_second.

        

        :param meters: The VolumeFlow value in kiloliters_per_second.
        :type kiloliters_per_second: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(kiloliters_per_second, VolumeFlowUnits.KiloliterPerSecond)

    
    @staticmethod
    def from_megaliters_per_second(megaliters_per_second: float):
        """
        Create a new instance of VolumeFlow from a value in megaliters_per_second.

        

        :param meters: The VolumeFlow value in megaliters_per_second.
        :type megaliters_per_second: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(megaliters_per_second, VolumeFlowUnits.MegaliterPerSecond)

    
    @staticmethod
    def from_nanoliters_per_minute(nanoliters_per_minute: float):
        """
        Create a new instance of VolumeFlow from a value in nanoliters_per_minute.

        

        :param meters: The VolumeFlow value in nanoliters_per_minute.
        :type nanoliters_per_minute: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(nanoliters_per_minute, VolumeFlowUnits.NanoliterPerMinute)

    
    @staticmethod
    def from_microliters_per_minute(microliters_per_minute: float):
        """
        Create a new instance of VolumeFlow from a value in microliters_per_minute.

        

        :param meters: The VolumeFlow value in microliters_per_minute.
        :type microliters_per_minute: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(microliters_per_minute, VolumeFlowUnits.MicroliterPerMinute)

    
    @staticmethod
    def from_milliliters_per_minute(milliliters_per_minute: float):
        """
        Create a new instance of VolumeFlow from a value in milliliters_per_minute.

        

        :param meters: The VolumeFlow value in milliliters_per_minute.
        :type milliliters_per_minute: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(milliliters_per_minute, VolumeFlowUnits.MilliliterPerMinute)

    
    @staticmethod
    def from_centiliters_per_minute(centiliters_per_minute: float):
        """
        Create a new instance of VolumeFlow from a value in centiliters_per_minute.

        

        :param meters: The VolumeFlow value in centiliters_per_minute.
        :type centiliters_per_minute: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(centiliters_per_minute, VolumeFlowUnits.CentiliterPerMinute)

    
    @staticmethod
    def from_deciliters_per_minute(deciliters_per_minute: float):
        """
        Create a new instance of VolumeFlow from a value in deciliters_per_minute.

        

        :param meters: The VolumeFlow value in deciliters_per_minute.
        :type deciliters_per_minute: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(deciliters_per_minute, VolumeFlowUnits.DeciliterPerMinute)

    
    @staticmethod
    def from_decaliters_per_minute(decaliters_per_minute: float):
        """
        Create a new instance of VolumeFlow from a value in decaliters_per_minute.

        

        :param meters: The VolumeFlow value in decaliters_per_minute.
        :type decaliters_per_minute: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(decaliters_per_minute, VolumeFlowUnits.DecaliterPerMinute)

    
    @staticmethod
    def from_hectoliters_per_minute(hectoliters_per_minute: float):
        """
        Create a new instance of VolumeFlow from a value in hectoliters_per_minute.

        

        :param meters: The VolumeFlow value in hectoliters_per_minute.
        :type hectoliters_per_minute: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(hectoliters_per_minute, VolumeFlowUnits.HectoliterPerMinute)

    
    @staticmethod
    def from_kiloliters_per_minute(kiloliters_per_minute: float):
        """
        Create a new instance of VolumeFlow from a value in kiloliters_per_minute.

        

        :param meters: The VolumeFlow value in kiloliters_per_minute.
        :type kiloliters_per_minute: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(kiloliters_per_minute, VolumeFlowUnits.KiloliterPerMinute)

    
    @staticmethod
    def from_megaliters_per_minute(megaliters_per_minute: float):
        """
        Create a new instance of VolumeFlow from a value in megaliters_per_minute.

        

        :param meters: The VolumeFlow value in megaliters_per_minute.
        :type megaliters_per_minute: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(megaliters_per_minute, VolumeFlowUnits.MegaliterPerMinute)

    
    @staticmethod
    def from_nanoliters_per_hour(nanoliters_per_hour: float):
        """
        Create a new instance of VolumeFlow from a value in nanoliters_per_hour.

        

        :param meters: The VolumeFlow value in nanoliters_per_hour.
        :type nanoliters_per_hour: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(nanoliters_per_hour, VolumeFlowUnits.NanoliterPerHour)

    
    @staticmethod
    def from_microliters_per_hour(microliters_per_hour: float):
        """
        Create a new instance of VolumeFlow from a value in microliters_per_hour.

        

        :param meters: The VolumeFlow value in microliters_per_hour.
        :type microliters_per_hour: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(microliters_per_hour, VolumeFlowUnits.MicroliterPerHour)

    
    @staticmethod
    def from_milliliters_per_hour(milliliters_per_hour: float):
        """
        Create a new instance of VolumeFlow from a value in milliliters_per_hour.

        

        :param meters: The VolumeFlow value in milliliters_per_hour.
        :type milliliters_per_hour: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(milliliters_per_hour, VolumeFlowUnits.MilliliterPerHour)

    
    @staticmethod
    def from_centiliters_per_hour(centiliters_per_hour: float):
        """
        Create a new instance of VolumeFlow from a value in centiliters_per_hour.

        

        :param meters: The VolumeFlow value in centiliters_per_hour.
        :type centiliters_per_hour: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(centiliters_per_hour, VolumeFlowUnits.CentiliterPerHour)

    
    @staticmethod
    def from_deciliters_per_hour(deciliters_per_hour: float):
        """
        Create a new instance of VolumeFlow from a value in deciliters_per_hour.

        

        :param meters: The VolumeFlow value in deciliters_per_hour.
        :type deciliters_per_hour: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(deciliters_per_hour, VolumeFlowUnits.DeciliterPerHour)

    
    @staticmethod
    def from_decaliters_per_hour(decaliters_per_hour: float):
        """
        Create a new instance of VolumeFlow from a value in decaliters_per_hour.

        

        :param meters: The VolumeFlow value in decaliters_per_hour.
        :type decaliters_per_hour: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(decaliters_per_hour, VolumeFlowUnits.DecaliterPerHour)

    
    @staticmethod
    def from_hectoliters_per_hour(hectoliters_per_hour: float):
        """
        Create a new instance of VolumeFlow from a value in hectoliters_per_hour.

        

        :param meters: The VolumeFlow value in hectoliters_per_hour.
        :type hectoliters_per_hour: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(hectoliters_per_hour, VolumeFlowUnits.HectoliterPerHour)

    
    @staticmethod
    def from_kiloliters_per_hour(kiloliters_per_hour: float):
        """
        Create a new instance of VolumeFlow from a value in kiloliters_per_hour.

        

        :param meters: The VolumeFlow value in kiloliters_per_hour.
        :type kiloliters_per_hour: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(kiloliters_per_hour, VolumeFlowUnits.KiloliterPerHour)

    
    @staticmethod
    def from_megaliters_per_hour(megaliters_per_hour: float):
        """
        Create a new instance of VolumeFlow from a value in megaliters_per_hour.

        

        :param meters: The VolumeFlow value in megaliters_per_hour.
        :type megaliters_per_hour: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(megaliters_per_hour, VolumeFlowUnits.MegaliterPerHour)

    
    @staticmethod
    def from_nanoliters_per_day(nanoliters_per_day: float):
        """
        Create a new instance of VolumeFlow from a value in nanoliters_per_day.

        

        :param meters: The VolumeFlow value in nanoliters_per_day.
        :type nanoliters_per_day: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(nanoliters_per_day, VolumeFlowUnits.NanoliterPerDay)

    
    @staticmethod
    def from_microliters_per_day(microliters_per_day: float):
        """
        Create a new instance of VolumeFlow from a value in microliters_per_day.

        

        :param meters: The VolumeFlow value in microliters_per_day.
        :type microliters_per_day: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(microliters_per_day, VolumeFlowUnits.MicroliterPerDay)

    
    @staticmethod
    def from_milliliters_per_day(milliliters_per_day: float):
        """
        Create a new instance of VolumeFlow from a value in milliliters_per_day.

        

        :param meters: The VolumeFlow value in milliliters_per_day.
        :type milliliters_per_day: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(milliliters_per_day, VolumeFlowUnits.MilliliterPerDay)

    
    @staticmethod
    def from_centiliters_per_day(centiliters_per_day: float):
        """
        Create a new instance of VolumeFlow from a value in centiliters_per_day.

        

        :param meters: The VolumeFlow value in centiliters_per_day.
        :type centiliters_per_day: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(centiliters_per_day, VolumeFlowUnits.CentiliterPerDay)

    
    @staticmethod
    def from_deciliters_per_day(deciliters_per_day: float):
        """
        Create a new instance of VolumeFlow from a value in deciliters_per_day.

        

        :param meters: The VolumeFlow value in deciliters_per_day.
        :type deciliters_per_day: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(deciliters_per_day, VolumeFlowUnits.DeciliterPerDay)

    
    @staticmethod
    def from_decaliters_per_day(decaliters_per_day: float):
        """
        Create a new instance of VolumeFlow from a value in decaliters_per_day.

        

        :param meters: The VolumeFlow value in decaliters_per_day.
        :type decaliters_per_day: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(decaliters_per_day, VolumeFlowUnits.DecaliterPerDay)

    
    @staticmethod
    def from_hectoliters_per_day(hectoliters_per_day: float):
        """
        Create a new instance of VolumeFlow from a value in hectoliters_per_day.

        

        :param meters: The VolumeFlow value in hectoliters_per_day.
        :type hectoliters_per_day: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(hectoliters_per_day, VolumeFlowUnits.HectoliterPerDay)

    
    @staticmethod
    def from_kiloliters_per_day(kiloliters_per_day: float):
        """
        Create a new instance of VolumeFlow from a value in kiloliters_per_day.

        

        :param meters: The VolumeFlow value in kiloliters_per_day.
        :type kiloliters_per_day: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(kiloliters_per_day, VolumeFlowUnits.KiloliterPerDay)

    
    @staticmethod
    def from_megaliters_per_day(megaliters_per_day: float):
        """
        Create a new instance of VolumeFlow from a value in megaliters_per_day.

        

        :param meters: The VolumeFlow value in megaliters_per_day.
        :type megaliters_per_day: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(megaliters_per_day, VolumeFlowUnits.MegaliterPerDay)

    
    @staticmethod
    def from_megauk_gallons_per_day(megauk_gallons_per_day: float):
        """
        Create a new instance of VolumeFlow from a value in megauk_gallons_per_day.

        

        :param meters: The VolumeFlow value in megauk_gallons_per_day.
        :type megauk_gallons_per_day: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(megauk_gallons_per_day, VolumeFlowUnits.MegaukGallonPerDay)

    
    @staticmethod
    def from_megauk_gallons_per_second(megauk_gallons_per_second: float):
        """
        Create a new instance of VolumeFlow from a value in megauk_gallons_per_second.

        

        :param meters: The VolumeFlow value in megauk_gallons_per_second.
        :type megauk_gallons_per_second: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(megauk_gallons_per_second, VolumeFlowUnits.MegaukGallonPerSecond)

    
    @property
    def cubic_meters_per_second(self) -> float:
        """
        
        """
        if self.__cubic_meters_per_second != None:
            return self.__cubic_meters_per_second
        self.__cubic_meters_per_second = self.__convert_from_base(VolumeFlowUnits.CubicMeterPerSecond)
        return self.__cubic_meters_per_second

    
    @property
    def cubic_meters_per_minute(self) -> float:
        """
        
        """
        if self.__cubic_meters_per_minute != None:
            return self.__cubic_meters_per_minute
        self.__cubic_meters_per_minute = self.__convert_from_base(VolumeFlowUnits.CubicMeterPerMinute)
        return self.__cubic_meters_per_minute

    
    @property
    def cubic_meters_per_hour(self) -> float:
        """
        
        """
        if self.__cubic_meters_per_hour != None:
            return self.__cubic_meters_per_hour
        self.__cubic_meters_per_hour = self.__convert_from_base(VolumeFlowUnits.CubicMeterPerHour)
        return self.__cubic_meters_per_hour

    
    @property
    def cubic_meters_per_day(self) -> float:
        """
        
        """
        if self.__cubic_meters_per_day != None:
            return self.__cubic_meters_per_day
        self.__cubic_meters_per_day = self.__convert_from_base(VolumeFlowUnits.CubicMeterPerDay)
        return self.__cubic_meters_per_day

    
    @property
    def cubic_feet_per_second(self) -> float:
        """
        
        """
        if self.__cubic_feet_per_second != None:
            return self.__cubic_feet_per_second
        self.__cubic_feet_per_second = self.__convert_from_base(VolumeFlowUnits.CubicFootPerSecond)
        return self.__cubic_feet_per_second

    
    @property
    def cubic_feet_per_minute(self) -> float:
        """
        
        """
        if self.__cubic_feet_per_minute != None:
            return self.__cubic_feet_per_minute
        self.__cubic_feet_per_minute = self.__convert_from_base(VolumeFlowUnits.CubicFootPerMinute)
        return self.__cubic_feet_per_minute

    
    @property
    def cubic_feet_per_hour(self) -> float:
        """
        
        """
        if self.__cubic_feet_per_hour != None:
            return self.__cubic_feet_per_hour
        self.__cubic_feet_per_hour = self.__convert_from_base(VolumeFlowUnits.CubicFootPerHour)
        return self.__cubic_feet_per_hour

    
    @property
    def cubic_yards_per_second(self) -> float:
        """
        
        """
        if self.__cubic_yards_per_second != None:
            return self.__cubic_yards_per_second
        self.__cubic_yards_per_second = self.__convert_from_base(VolumeFlowUnits.CubicYardPerSecond)
        return self.__cubic_yards_per_second

    
    @property
    def cubic_yards_per_minute(self) -> float:
        """
        
        """
        if self.__cubic_yards_per_minute != None:
            return self.__cubic_yards_per_minute
        self.__cubic_yards_per_minute = self.__convert_from_base(VolumeFlowUnits.CubicYardPerMinute)
        return self.__cubic_yards_per_minute

    
    @property
    def cubic_yards_per_hour(self) -> float:
        """
        
        """
        if self.__cubic_yards_per_hour != None:
            return self.__cubic_yards_per_hour
        self.__cubic_yards_per_hour = self.__convert_from_base(VolumeFlowUnits.CubicYardPerHour)
        return self.__cubic_yards_per_hour

    
    @property
    def cubic_yards_per_day(self) -> float:
        """
        
        """
        if self.__cubic_yards_per_day != None:
            return self.__cubic_yards_per_day
        self.__cubic_yards_per_day = self.__convert_from_base(VolumeFlowUnits.CubicYardPerDay)
        return self.__cubic_yards_per_day

    
    @property
    def million_us_gallons_per_day(self) -> float:
        """
        
        """
        if self.__million_us_gallons_per_day != None:
            return self.__million_us_gallons_per_day
        self.__million_us_gallons_per_day = self.__convert_from_base(VolumeFlowUnits.MillionUsGallonPerDay)
        return self.__million_us_gallons_per_day

    
    @property
    def us_gallons_per_day(self) -> float:
        """
        
        """
        if self.__us_gallons_per_day != None:
            return self.__us_gallons_per_day
        self.__us_gallons_per_day = self.__convert_from_base(VolumeFlowUnits.UsGallonPerDay)
        return self.__us_gallons_per_day

    
    @property
    def liters_per_second(self) -> float:
        """
        
        """
        if self.__liters_per_second != None:
            return self.__liters_per_second
        self.__liters_per_second = self.__convert_from_base(VolumeFlowUnits.LiterPerSecond)
        return self.__liters_per_second

    
    @property
    def liters_per_minute(self) -> float:
        """
        
        """
        if self.__liters_per_minute != None:
            return self.__liters_per_minute
        self.__liters_per_minute = self.__convert_from_base(VolumeFlowUnits.LiterPerMinute)
        return self.__liters_per_minute

    
    @property
    def liters_per_hour(self) -> float:
        """
        
        """
        if self.__liters_per_hour != None:
            return self.__liters_per_hour
        self.__liters_per_hour = self.__convert_from_base(VolumeFlowUnits.LiterPerHour)
        return self.__liters_per_hour

    
    @property
    def liters_per_day(self) -> float:
        """
        
        """
        if self.__liters_per_day != None:
            return self.__liters_per_day
        self.__liters_per_day = self.__convert_from_base(VolumeFlowUnits.LiterPerDay)
        return self.__liters_per_day

    
    @property
    def us_gallons_per_second(self) -> float:
        """
        
        """
        if self.__us_gallons_per_second != None:
            return self.__us_gallons_per_second
        self.__us_gallons_per_second = self.__convert_from_base(VolumeFlowUnits.UsGallonPerSecond)
        return self.__us_gallons_per_second

    
    @property
    def us_gallons_per_minute(self) -> float:
        """
        
        """
        if self.__us_gallons_per_minute != None:
            return self.__us_gallons_per_minute
        self.__us_gallons_per_minute = self.__convert_from_base(VolumeFlowUnits.UsGallonPerMinute)
        return self.__us_gallons_per_minute

    
    @property
    def uk_gallons_per_day(self) -> float:
        """
        
        """
        if self.__uk_gallons_per_day != None:
            return self.__uk_gallons_per_day
        self.__uk_gallons_per_day = self.__convert_from_base(VolumeFlowUnits.UkGallonPerDay)
        return self.__uk_gallons_per_day

    
    @property
    def uk_gallons_per_hour(self) -> float:
        """
        
        """
        if self.__uk_gallons_per_hour != None:
            return self.__uk_gallons_per_hour
        self.__uk_gallons_per_hour = self.__convert_from_base(VolumeFlowUnits.UkGallonPerHour)
        return self.__uk_gallons_per_hour

    
    @property
    def uk_gallons_per_minute(self) -> float:
        """
        
        """
        if self.__uk_gallons_per_minute != None:
            return self.__uk_gallons_per_minute
        self.__uk_gallons_per_minute = self.__convert_from_base(VolumeFlowUnits.UkGallonPerMinute)
        return self.__uk_gallons_per_minute

    
    @property
    def uk_gallons_per_second(self) -> float:
        """
        
        """
        if self.__uk_gallons_per_second != None:
            return self.__uk_gallons_per_second
        self.__uk_gallons_per_second = self.__convert_from_base(VolumeFlowUnits.UkGallonPerSecond)
        return self.__uk_gallons_per_second

    
    @property
    def kilous_gallons_per_minute(self) -> float:
        """
        
        """
        if self.__kilous_gallons_per_minute != None:
            return self.__kilous_gallons_per_minute
        self.__kilous_gallons_per_minute = self.__convert_from_base(VolumeFlowUnits.KilousGallonPerMinute)
        return self.__kilous_gallons_per_minute

    
    @property
    def us_gallons_per_hour(self) -> float:
        """
        
        """
        if self.__us_gallons_per_hour != None:
            return self.__us_gallons_per_hour
        self.__us_gallons_per_hour = self.__convert_from_base(VolumeFlowUnits.UsGallonPerHour)
        return self.__us_gallons_per_hour

    
    @property
    def cubic_decimeters_per_minute(self) -> float:
        """
        
        """
        if self.__cubic_decimeters_per_minute != None:
            return self.__cubic_decimeters_per_minute
        self.__cubic_decimeters_per_minute = self.__convert_from_base(VolumeFlowUnits.CubicDecimeterPerMinute)
        return self.__cubic_decimeters_per_minute

    
    @property
    def oil_barrels_per_day(self) -> float:
        """
        
        """
        if self.__oil_barrels_per_day != None:
            return self.__oil_barrels_per_day
        self.__oil_barrels_per_day = self.__convert_from_base(VolumeFlowUnits.OilBarrelPerDay)
        return self.__oil_barrels_per_day

    
    @property
    def oil_barrels_per_minute(self) -> float:
        """
        
        """
        if self.__oil_barrels_per_minute != None:
            return self.__oil_barrels_per_minute
        self.__oil_barrels_per_minute = self.__convert_from_base(VolumeFlowUnits.OilBarrelPerMinute)
        return self.__oil_barrels_per_minute

    
    @property
    def oil_barrels_per_hour(self) -> float:
        """
        
        """
        if self.__oil_barrels_per_hour != None:
            return self.__oil_barrels_per_hour
        self.__oil_barrels_per_hour = self.__convert_from_base(VolumeFlowUnits.OilBarrelPerHour)
        return self.__oil_barrels_per_hour

    
    @property
    def oil_barrels_per_second(self) -> float:
        """
        
        """
        if self.__oil_barrels_per_second != None:
            return self.__oil_barrels_per_second
        self.__oil_barrels_per_second = self.__convert_from_base(VolumeFlowUnits.OilBarrelPerSecond)
        return self.__oil_barrels_per_second

    
    @property
    def cubic_millimeters_per_second(self) -> float:
        """
        
        """
        if self.__cubic_millimeters_per_second != None:
            return self.__cubic_millimeters_per_second
        self.__cubic_millimeters_per_second = self.__convert_from_base(VolumeFlowUnits.CubicMillimeterPerSecond)
        return self.__cubic_millimeters_per_second

    
    @property
    def acre_feet_per_second(self) -> float:
        """
        
        """
        if self.__acre_feet_per_second != None:
            return self.__acre_feet_per_second
        self.__acre_feet_per_second = self.__convert_from_base(VolumeFlowUnits.AcreFootPerSecond)
        return self.__acre_feet_per_second

    
    @property
    def acre_feet_per_minute(self) -> float:
        """
        
        """
        if self.__acre_feet_per_minute != None:
            return self.__acre_feet_per_minute
        self.__acre_feet_per_minute = self.__convert_from_base(VolumeFlowUnits.AcreFootPerMinute)
        return self.__acre_feet_per_minute

    
    @property
    def acre_feet_per_hour(self) -> float:
        """
        
        """
        if self.__acre_feet_per_hour != None:
            return self.__acre_feet_per_hour
        self.__acre_feet_per_hour = self.__convert_from_base(VolumeFlowUnits.AcreFootPerHour)
        return self.__acre_feet_per_hour

    
    @property
    def acre_feet_per_day(self) -> float:
        """
        
        """
        if self.__acre_feet_per_day != None:
            return self.__acre_feet_per_day
        self.__acre_feet_per_day = self.__convert_from_base(VolumeFlowUnits.AcreFootPerDay)
        return self.__acre_feet_per_day

    
    @property
    def cubic_centimeters_per_minute(self) -> float:
        """
        
        """
        if self.__cubic_centimeters_per_minute != None:
            return self.__cubic_centimeters_per_minute
        self.__cubic_centimeters_per_minute = self.__convert_from_base(VolumeFlowUnits.CubicCentimeterPerMinute)
        return self.__cubic_centimeters_per_minute

    
    @property
    def megaus_gallons_per_day(self) -> float:
        """
        
        """
        if self.__megaus_gallons_per_day != None:
            return self.__megaus_gallons_per_day
        self.__megaus_gallons_per_day = self.__convert_from_base(VolumeFlowUnits.MegausGallonPerDay)
        return self.__megaus_gallons_per_day

    
    @property
    def nanoliters_per_second(self) -> float:
        """
        
        """
        if self.__nanoliters_per_second != None:
            return self.__nanoliters_per_second
        self.__nanoliters_per_second = self.__convert_from_base(VolumeFlowUnits.NanoliterPerSecond)
        return self.__nanoliters_per_second

    
    @property
    def microliters_per_second(self) -> float:
        """
        
        """
        if self.__microliters_per_second != None:
            return self.__microliters_per_second
        self.__microliters_per_second = self.__convert_from_base(VolumeFlowUnits.MicroliterPerSecond)
        return self.__microliters_per_second

    
    @property
    def milliliters_per_second(self) -> float:
        """
        
        """
        if self.__milliliters_per_second != None:
            return self.__milliliters_per_second
        self.__milliliters_per_second = self.__convert_from_base(VolumeFlowUnits.MilliliterPerSecond)
        return self.__milliliters_per_second

    
    @property
    def centiliters_per_second(self) -> float:
        """
        
        """
        if self.__centiliters_per_second != None:
            return self.__centiliters_per_second
        self.__centiliters_per_second = self.__convert_from_base(VolumeFlowUnits.CentiliterPerSecond)
        return self.__centiliters_per_second

    
    @property
    def deciliters_per_second(self) -> float:
        """
        
        """
        if self.__deciliters_per_second != None:
            return self.__deciliters_per_second
        self.__deciliters_per_second = self.__convert_from_base(VolumeFlowUnits.DeciliterPerSecond)
        return self.__deciliters_per_second

    
    @property
    def decaliters_per_second(self) -> float:
        """
        
        """
        if self.__decaliters_per_second != None:
            return self.__decaliters_per_second
        self.__decaliters_per_second = self.__convert_from_base(VolumeFlowUnits.DecaliterPerSecond)
        return self.__decaliters_per_second

    
    @property
    def hectoliters_per_second(self) -> float:
        """
        
        """
        if self.__hectoliters_per_second != None:
            return self.__hectoliters_per_second
        self.__hectoliters_per_second = self.__convert_from_base(VolumeFlowUnits.HectoliterPerSecond)
        return self.__hectoliters_per_second

    
    @property
    def kiloliters_per_second(self) -> float:
        """
        
        """
        if self.__kiloliters_per_second != None:
            return self.__kiloliters_per_second
        self.__kiloliters_per_second = self.__convert_from_base(VolumeFlowUnits.KiloliterPerSecond)
        return self.__kiloliters_per_second

    
    @property
    def megaliters_per_second(self) -> float:
        """
        
        """
        if self.__megaliters_per_second != None:
            return self.__megaliters_per_second
        self.__megaliters_per_second = self.__convert_from_base(VolumeFlowUnits.MegaliterPerSecond)
        return self.__megaliters_per_second

    
    @property
    def nanoliters_per_minute(self) -> float:
        """
        
        """
        if self.__nanoliters_per_minute != None:
            return self.__nanoliters_per_minute
        self.__nanoliters_per_minute = self.__convert_from_base(VolumeFlowUnits.NanoliterPerMinute)
        return self.__nanoliters_per_minute

    
    @property
    def microliters_per_minute(self) -> float:
        """
        
        """
        if self.__microliters_per_minute != None:
            return self.__microliters_per_minute
        self.__microliters_per_minute = self.__convert_from_base(VolumeFlowUnits.MicroliterPerMinute)
        return self.__microliters_per_minute

    
    @property
    def milliliters_per_minute(self) -> float:
        """
        
        """
        if self.__milliliters_per_minute != None:
            return self.__milliliters_per_minute
        self.__milliliters_per_minute = self.__convert_from_base(VolumeFlowUnits.MilliliterPerMinute)
        return self.__milliliters_per_minute

    
    @property
    def centiliters_per_minute(self) -> float:
        """
        
        """
        if self.__centiliters_per_minute != None:
            return self.__centiliters_per_minute
        self.__centiliters_per_minute = self.__convert_from_base(VolumeFlowUnits.CentiliterPerMinute)
        return self.__centiliters_per_minute

    
    @property
    def deciliters_per_minute(self) -> float:
        """
        
        """
        if self.__deciliters_per_minute != None:
            return self.__deciliters_per_minute
        self.__deciliters_per_minute = self.__convert_from_base(VolumeFlowUnits.DeciliterPerMinute)
        return self.__deciliters_per_minute

    
    @property
    def decaliters_per_minute(self) -> float:
        """
        
        """
        if self.__decaliters_per_minute != None:
            return self.__decaliters_per_minute
        self.__decaliters_per_minute = self.__convert_from_base(VolumeFlowUnits.DecaliterPerMinute)
        return self.__decaliters_per_minute

    
    @property
    def hectoliters_per_minute(self) -> float:
        """
        
        """
        if self.__hectoliters_per_minute != None:
            return self.__hectoliters_per_minute
        self.__hectoliters_per_minute = self.__convert_from_base(VolumeFlowUnits.HectoliterPerMinute)
        return self.__hectoliters_per_minute

    
    @property
    def kiloliters_per_minute(self) -> float:
        """
        
        """
        if self.__kiloliters_per_minute != None:
            return self.__kiloliters_per_minute
        self.__kiloliters_per_minute = self.__convert_from_base(VolumeFlowUnits.KiloliterPerMinute)
        return self.__kiloliters_per_minute

    
    @property
    def megaliters_per_minute(self) -> float:
        """
        
        """
        if self.__megaliters_per_minute != None:
            return self.__megaliters_per_minute
        self.__megaliters_per_minute = self.__convert_from_base(VolumeFlowUnits.MegaliterPerMinute)
        return self.__megaliters_per_minute

    
    @property
    def nanoliters_per_hour(self) -> float:
        """
        
        """
        if self.__nanoliters_per_hour != None:
            return self.__nanoliters_per_hour
        self.__nanoliters_per_hour = self.__convert_from_base(VolumeFlowUnits.NanoliterPerHour)
        return self.__nanoliters_per_hour

    
    @property
    def microliters_per_hour(self) -> float:
        """
        
        """
        if self.__microliters_per_hour != None:
            return self.__microliters_per_hour
        self.__microliters_per_hour = self.__convert_from_base(VolumeFlowUnits.MicroliterPerHour)
        return self.__microliters_per_hour

    
    @property
    def milliliters_per_hour(self) -> float:
        """
        
        """
        if self.__milliliters_per_hour != None:
            return self.__milliliters_per_hour
        self.__milliliters_per_hour = self.__convert_from_base(VolumeFlowUnits.MilliliterPerHour)
        return self.__milliliters_per_hour

    
    @property
    def centiliters_per_hour(self) -> float:
        """
        
        """
        if self.__centiliters_per_hour != None:
            return self.__centiliters_per_hour
        self.__centiliters_per_hour = self.__convert_from_base(VolumeFlowUnits.CentiliterPerHour)
        return self.__centiliters_per_hour

    
    @property
    def deciliters_per_hour(self) -> float:
        """
        
        """
        if self.__deciliters_per_hour != None:
            return self.__deciliters_per_hour
        self.__deciliters_per_hour = self.__convert_from_base(VolumeFlowUnits.DeciliterPerHour)
        return self.__deciliters_per_hour

    
    @property
    def decaliters_per_hour(self) -> float:
        """
        
        """
        if self.__decaliters_per_hour != None:
            return self.__decaliters_per_hour
        self.__decaliters_per_hour = self.__convert_from_base(VolumeFlowUnits.DecaliterPerHour)
        return self.__decaliters_per_hour

    
    @property
    def hectoliters_per_hour(self) -> float:
        """
        
        """
        if self.__hectoliters_per_hour != None:
            return self.__hectoliters_per_hour
        self.__hectoliters_per_hour = self.__convert_from_base(VolumeFlowUnits.HectoliterPerHour)
        return self.__hectoliters_per_hour

    
    @property
    def kiloliters_per_hour(self) -> float:
        """
        
        """
        if self.__kiloliters_per_hour != None:
            return self.__kiloliters_per_hour
        self.__kiloliters_per_hour = self.__convert_from_base(VolumeFlowUnits.KiloliterPerHour)
        return self.__kiloliters_per_hour

    
    @property
    def megaliters_per_hour(self) -> float:
        """
        
        """
        if self.__megaliters_per_hour != None:
            return self.__megaliters_per_hour
        self.__megaliters_per_hour = self.__convert_from_base(VolumeFlowUnits.MegaliterPerHour)
        return self.__megaliters_per_hour

    
    @property
    def nanoliters_per_day(self) -> float:
        """
        
        """
        if self.__nanoliters_per_day != None:
            return self.__nanoliters_per_day
        self.__nanoliters_per_day = self.__convert_from_base(VolumeFlowUnits.NanoliterPerDay)
        return self.__nanoliters_per_day

    
    @property
    def microliters_per_day(self) -> float:
        """
        
        """
        if self.__microliters_per_day != None:
            return self.__microliters_per_day
        self.__microliters_per_day = self.__convert_from_base(VolumeFlowUnits.MicroliterPerDay)
        return self.__microliters_per_day

    
    @property
    def milliliters_per_day(self) -> float:
        """
        
        """
        if self.__milliliters_per_day != None:
            return self.__milliliters_per_day
        self.__milliliters_per_day = self.__convert_from_base(VolumeFlowUnits.MilliliterPerDay)
        return self.__milliliters_per_day

    
    @property
    def centiliters_per_day(self) -> float:
        """
        
        """
        if self.__centiliters_per_day != None:
            return self.__centiliters_per_day
        self.__centiliters_per_day = self.__convert_from_base(VolumeFlowUnits.CentiliterPerDay)
        return self.__centiliters_per_day

    
    @property
    def deciliters_per_day(self) -> float:
        """
        
        """
        if self.__deciliters_per_day != None:
            return self.__deciliters_per_day
        self.__deciliters_per_day = self.__convert_from_base(VolumeFlowUnits.DeciliterPerDay)
        return self.__deciliters_per_day

    
    @property
    def decaliters_per_day(self) -> float:
        """
        
        """
        if self.__decaliters_per_day != None:
            return self.__decaliters_per_day
        self.__decaliters_per_day = self.__convert_from_base(VolumeFlowUnits.DecaliterPerDay)
        return self.__decaliters_per_day

    
    @property
    def hectoliters_per_day(self) -> float:
        """
        
        """
        if self.__hectoliters_per_day != None:
            return self.__hectoliters_per_day
        self.__hectoliters_per_day = self.__convert_from_base(VolumeFlowUnits.HectoliterPerDay)
        return self.__hectoliters_per_day

    
    @property
    def kiloliters_per_day(self) -> float:
        """
        
        """
        if self.__kiloliters_per_day != None:
            return self.__kiloliters_per_day
        self.__kiloliters_per_day = self.__convert_from_base(VolumeFlowUnits.KiloliterPerDay)
        return self.__kiloliters_per_day

    
    @property
    def megaliters_per_day(self) -> float:
        """
        
        """
        if self.__megaliters_per_day != None:
            return self.__megaliters_per_day
        self.__megaliters_per_day = self.__convert_from_base(VolumeFlowUnits.MegaliterPerDay)
        return self.__megaliters_per_day

    
    @property
    def megauk_gallons_per_day(self) -> float:
        """
        
        """
        if self.__megauk_gallons_per_day != None:
            return self.__megauk_gallons_per_day
        self.__megauk_gallons_per_day = self.__convert_from_base(VolumeFlowUnits.MegaukGallonPerDay)
        return self.__megauk_gallons_per_day

    
    @property
    def megauk_gallons_per_second(self) -> float:
        """
        
        """
        if self.__megauk_gallons_per_second != None:
            return self.__megauk_gallons_per_second
        self.__megauk_gallons_per_second = self.__convert_from_base(VolumeFlowUnits.MegaukGallonPerSecond)
        return self.__megauk_gallons_per_second

    
    def to_string(self, unit: VolumeFlowUnits = VolumeFlowUnits.CubicMeterPerSecond, fractional_digits: int = None) -> str:
        """
        Format the VolumeFlow to a string.
        
        Note: the default format for VolumeFlow is CubicMeterPerSecond.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the VolumeFlow. Default is 'CubicMeterPerSecond'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == VolumeFlowUnits.CubicMeterPerSecond:
            return f"""{super()._truncate_fraction_digits(self.cubic_meters_per_second, fractional_digits)} m³/s"""
        
        if unit == VolumeFlowUnits.CubicMeterPerMinute:
            return f"""{super()._truncate_fraction_digits(self.cubic_meters_per_minute, fractional_digits)} m³/min"""
        
        if unit == VolumeFlowUnits.CubicMeterPerHour:
            return f"""{super()._truncate_fraction_digits(self.cubic_meters_per_hour, fractional_digits)} m³/h"""
        
        if unit == VolumeFlowUnits.CubicMeterPerDay:
            return f"""{super()._truncate_fraction_digits(self.cubic_meters_per_day, fractional_digits)} m³/d"""
        
        if unit == VolumeFlowUnits.CubicFootPerSecond:
            return f"""{super()._truncate_fraction_digits(self.cubic_feet_per_second, fractional_digits)} ft³/s"""
        
        if unit == VolumeFlowUnits.CubicFootPerMinute:
            return f"""{super()._truncate_fraction_digits(self.cubic_feet_per_minute, fractional_digits)} ft³/min"""
        
        if unit == VolumeFlowUnits.CubicFootPerHour:
            return f"""{super()._truncate_fraction_digits(self.cubic_feet_per_hour, fractional_digits)} ft³/h"""
        
        if unit == VolumeFlowUnits.CubicYardPerSecond:
            return f"""{super()._truncate_fraction_digits(self.cubic_yards_per_second, fractional_digits)} yd³/s"""
        
        if unit == VolumeFlowUnits.CubicYardPerMinute:
            return f"""{super()._truncate_fraction_digits(self.cubic_yards_per_minute, fractional_digits)} yd³/min"""
        
        if unit == VolumeFlowUnits.CubicYardPerHour:
            return f"""{super()._truncate_fraction_digits(self.cubic_yards_per_hour, fractional_digits)} yd³/h"""
        
        if unit == VolumeFlowUnits.CubicYardPerDay:
            return f"""{super()._truncate_fraction_digits(self.cubic_yards_per_day, fractional_digits)} cy/day"""
        
        if unit == VolumeFlowUnits.MillionUsGallonPerDay:
            return f"""{super()._truncate_fraction_digits(self.million_us_gallons_per_day, fractional_digits)} MGD"""
        
        if unit == VolumeFlowUnits.UsGallonPerDay:
            return f"""{super()._truncate_fraction_digits(self.us_gallons_per_day, fractional_digits)} gpd"""
        
        if unit == VolumeFlowUnits.LiterPerSecond:
            return f"""{super()._truncate_fraction_digits(self.liters_per_second, fractional_digits)} L/s"""
        
        if unit == VolumeFlowUnits.LiterPerMinute:
            return f"""{super()._truncate_fraction_digits(self.liters_per_minute, fractional_digits)} L/min"""
        
        if unit == VolumeFlowUnits.LiterPerHour:
            return f"""{super()._truncate_fraction_digits(self.liters_per_hour, fractional_digits)} L/h"""
        
        if unit == VolumeFlowUnits.LiterPerDay:
            return f"""{super()._truncate_fraction_digits(self.liters_per_day, fractional_digits)} l/day"""
        
        if unit == VolumeFlowUnits.UsGallonPerSecond:
            return f"""{super()._truncate_fraction_digits(self.us_gallons_per_second, fractional_digits)} gal (U.S.)/s"""
        
        if unit == VolumeFlowUnits.UsGallonPerMinute:
            return f"""{super()._truncate_fraction_digits(self.us_gallons_per_minute, fractional_digits)} gal (U.S.)/min"""
        
        if unit == VolumeFlowUnits.UkGallonPerDay:
            return f"""{super()._truncate_fraction_digits(self.uk_gallons_per_day, fractional_digits)} gal (U. K.)/d"""
        
        if unit == VolumeFlowUnits.UkGallonPerHour:
            return f"""{super()._truncate_fraction_digits(self.uk_gallons_per_hour, fractional_digits)} gal (imp.)/h"""
        
        if unit == VolumeFlowUnits.UkGallonPerMinute:
            return f"""{super()._truncate_fraction_digits(self.uk_gallons_per_minute, fractional_digits)} gal (imp.)/min"""
        
        if unit == VolumeFlowUnits.UkGallonPerSecond:
            return f"""{super()._truncate_fraction_digits(self.uk_gallons_per_second, fractional_digits)} gal (imp.)/s"""
        
        if unit == VolumeFlowUnits.KilousGallonPerMinute:
            return f"""{super()._truncate_fraction_digits(self.kilous_gallons_per_minute, fractional_digits)} kgal (U.S.)/min"""
        
        if unit == VolumeFlowUnits.UsGallonPerHour:
            return f"""{super()._truncate_fraction_digits(self.us_gallons_per_hour, fractional_digits)} gal (U.S.)/h"""
        
        if unit == VolumeFlowUnits.CubicDecimeterPerMinute:
            return f"""{super()._truncate_fraction_digits(self.cubic_decimeters_per_minute, fractional_digits)} dm³/min"""
        
        if unit == VolumeFlowUnits.OilBarrelPerDay:
            return f"""{super()._truncate_fraction_digits(self.oil_barrels_per_day, fractional_digits)} bbl/d"""
        
        if unit == VolumeFlowUnits.OilBarrelPerMinute:
            return f"""{super()._truncate_fraction_digits(self.oil_barrels_per_minute, fractional_digits)} bbl/min"""
        
        if unit == VolumeFlowUnits.OilBarrelPerHour:
            return f"""{super()._truncate_fraction_digits(self.oil_barrels_per_hour, fractional_digits)} bbl/hr"""
        
        if unit == VolumeFlowUnits.OilBarrelPerSecond:
            return f"""{super()._truncate_fraction_digits(self.oil_barrels_per_second, fractional_digits)} bbl/s"""
        
        if unit == VolumeFlowUnits.CubicMillimeterPerSecond:
            return f"""{super()._truncate_fraction_digits(self.cubic_millimeters_per_second, fractional_digits)} mm³/s"""
        
        if unit == VolumeFlowUnits.AcreFootPerSecond:
            return f"""{super()._truncate_fraction_digits(self.acre_feet_per_second, fractional_digits)} af/s"""
        
        if unit == VolumeFlowUnits.AcreFootPerMinute:
            return f"""{super()._truncate_fraction_digits(self.acre_feet_per_minute, fractional_digits)} af/m"""
        
        if unit == VolumeFlowUnits.AcreFootPerHour:
            return f"""{super()._truncate_fraction_digits(self.acre_feet_per_hour, fractional_digits)} af/h"""
        
        if unit == VolumeFlowUnits.AcreFootPerDay:
            return f"""{super()._truncate_fraction_digits(self.acre_feet_per_day, fractional_digits)} af/d"""
        
        if unit == VolumeFlowUnits.CubicCentimeterPerMinute:
            return f"""{super()._truncate_fraction_digits(self.cubic_centimeters_per_minute, fractional_digits)} cm³/min"""
        
        if unit == VolumeFlowUnits.MegausGallonPerDay:
            return f"""{super()._truncate_fraction_digits(self.megaus_gallons_per_day, fractional_digits)} Mgpd"""
        
        if unit == VolumeFlowUnits.NanoliterPerSecond:
            return f"""{super()._truncate_fraction_digits(self.nanoliters_per_second, fractional_digits)} nL/s"""
        
        if unit == VolumeFlowUnits.MicroliterPerSecond:
            return f"""{super()._truncate_fraction_digits(self.microliters_per_second, fractional_digits)} μL/s"""
        
        if unit == VolumeFlowUnits.MilliliterPerSecond:
            return f"""{super()._truncate_fraction_digits(self.milliliters_per_second, fractional_digits)} mL/s"""
        
        if unit == VolumeFlowUnits.CentiliterPerSecond:
            return f"""{super()._truncate_fraction_digits(self.centiliters_per_second, fractional_digits)} cL/s"""
        
        if unit == VolumeFlowUnits.DeciliterPerSecond:
            return f"""{super()._truncate_fraction_digits(self.deciliters_per_second, fractional_digits)} dL/s"""
        
        if unit == VolumeFlowUnits.DecaliterPerSecond:
            return f"""{super()._truncate_fraction_digits(self.decaliters_per_second, fractional_digits)} daL/s"""
        
        if unit == VolumeFlowUnits.HectoliterPerSecond:
            return f"""{super()._truncate_fraction_digits(self.hectoliters_per_second, fractional_digits)} hL/s"""
        
        if unit == VolumeFlowUnits.KiloliterPerSecond:
            return f"""{super()._truncate_fraction_digits(self.kiloliters_per_second, fractional_digits)} kL/s"""
        
        if unit == VolumeFlowUnits.MegaliterPerSecond:
            return f"""{super()._truncate_fraction_digits(self.megaliters_per_second, fractional_digits)} ML/s"""
        
        if unit == VolumeFlowUnits.NanoliterPerMinute:
            return f"""{super()._truncate_fraction_digits(self.nanoliters_per_minute, fractional_digits)} nL/min"""
        
        if unit == VolumeFlowUnits.MicroliterPerMinute:
            return f"""{super()._truncate_fraction_digits(self.microliters_per_minute, fractional_digits)} μL/min"""
        
        if unit == VolumeFlowUnits.MilliliterPerMinute:
            return f"""{super()._truncate_fraction_digits(self.milliliters_per_minute, fractional_digits)} mL/min"""
        
        if unit == VolumeFlowUnits.CentiliterPerMinute:
            return f"""{super()._truncate_fraction_digits(self.centiliters_per_minute, fractional_digits)} cL/min"""
        
        if unit == VolumeFlowUnits.DeciliterPerMinute:
            return f"""{super()._truncate_fraction_digits(self.deciliters_per_minute, fractional_digits)} dL/min"""
        
        if unit == VolumeFlowUnits.DecaliterPerMinute:
            return f"""{super()._truncate_fraction_digits(self.decaliters_per_minute, fractional_digits)} daL/min"""
        
        if unit == VolumeFlowUnits.HectoliterPerMinute:
            return f"""{super()._truncate_fraction_digits(self.hectoliters_per_minute, fractional_digits)} hL/min"""
        
        if unit == VolumeFlowUnits.KiloliterPerMinute:
            return f"""{super()._truncate_fraction_digits(self.kiloliters_per_minute, fractional_digits)} kL/min"""
        
        if unit == VolumeFlowUnits.MegaliterPerMinute:
            return f"""{super()._truncate_fraction_digits(self.megaliters_per_minute, fractional_digits)} ML/min"""
        
        if unit == VolumeFlowUnits.NanoliterPerHour:
            return f"""{super()._truncate_fraction_digits(self.nanoliters_per_hour, fractional_digits)} nL/h"""
        
        if unit == VolumeFlowUnits.MicroliterPerHour:
            return f"""{super()._truncate_fraction_digits(self.microliters_per_hour, fractional_digits)} μL/h"""
        
        if unit == VolumeFlowUnits.MilliliterPerHour:
            return f"""{super()._truncate_fraction_digits(self.milliliters_per_hour, fractional_digits)} mL/h"""
        
        if unit == VolumeFlowUnits.CentiliterPerHour:
            return f"""{super()._truncate_fraction_digits(self.centiliters_per_hour, fractional_digits)} cL/h"""
        
        if unit == VolumeFlowUnits.DeciliterPerHour:
            return f"""{super()._truncate_fraction_digits(self.deciliters_per_hour, fractional_digits)} dL/h"""
        
        if unit == VolumeFlowUnits.DecaliterPerHour:
            return f"""{super()._truncate_fraction_digits(self.decaliters_per_hour, fractional_digits)} daL/h"""
        
        if unit == VolumeFlowUnits.HectoliterPerHour:
            return f"""{super()._truncate_fraction_digits(self.hectoliters_per_hour, fractional_digits)} hL/h"""
        
        if unit == VolumeFlowUnits.KiloliterPerHour:
            return f"""{super()._truncate_fraction_digits(self.kiloliters_per_hour, fractional_digits)} kL/h"""
        
        if unit == VolumeFlowUnits.MegaliterPerHour:
            return f"""{super()._truncate_fraction_digits(self.megaliters_per_hour, fractional_digits)} ML/h"""
        
        if unit == VolumeFlowUnits.NanoliterPerDay:
            return f"""{super()._truncate_fraction_digits(self.nanoliters_per_day, fractional_digits)} nl/day"""
        
        if unit == VolumeFlowUnits.MicroliterPerDay:
            return f"""{super()._truncate_fraction_digits(self.microliters_per_day, fractional_digits)} μl/day"""
        
        if unit == VolumeFlowUnits.MilliliterPerDay:
            return f"""{super()._truncate_fraction_digits(self.milliliters_per_day, fractional_digits)} ml/day"""
        
        if unit == VolumeFlowUnits.CentiliterPerDay:
            return f"""{super()._truncate_fraction_digits(self.centiliters_per_day, fractional_digits)} cl/day"""
        
        if unit == VolumeFlowUnits.DeciliterPerDay:
            return f"""{super()._truncate_fraction_digits(self.deciliters_per_day, fractional_digits)} dl/day"""
        
        if unit == VolumeFlowUnits.DecaliterPerDay:
            return f"""{super()._truncate_fraction_digits(self.decaliters_per_day, fractional_digits)} dal/day"""
        
        if unit == VolumeFlowUnits.HectoliterPerDay:
            return f"""{super()._truncate_fraction_digits(self.hectoliters_per_day, fractional_digits)} hl/day"""
        
        if unit == VolumeFlowUnits.KiloliterPerDay:
            return f"""{super()._truncate_fraction_digits(self.kiloliters_per_day, fractional_digits)} kl/day"""
        
        if unit == VolumeFlowUnits.MegaliterPerDay:
            return f"""{super()._truncate_fraction_digits(self.megaliters_per_day, fractional_digits)} Ml/day"""
        
        if unit == VolumeFlowUnits.MegaukGallonPerDay:
            return f"""{super()._truncate_fraction_digits(self.megauk_gallons_per_day, fractional_digits)} Mgal (U. K.)/d"""
        
        if unit == VolumeFlowUnits.MegaukGallonPerSecond:
            return f"""{super()._truncate_fraction_digits(self.megauk_gallons_per_second, fractional_digits)} Mgal (imp.)/s"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: VolumeFlowUnits = VolumeFlowUnits.CubicMeterPerSecond) -> str:
        """
        Get VolumeFlow unit abbreviation.
        Note! the default abbreviation for VolumeFlow is CubicMeterPerSecond.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == VolumeFlowUnits.CubicMeterPerSecond:
            return """m³/s"""
        
        if unit_abbreviation == VolumeFlowUnits.CubicMeterPerMinute:
            return """m³/min"""
        
        if unit_abbreviation == VolumeFlowUnits.CubicMeterPerHour:
            return """m³/h"""
        
        if unit_abbreviation == VolumeFlowUnits.CubicMeterPerDay:
            return """m³/d"""
        
        if unit_abbreviation == VolumeFlowUnits.CubicFootPerSecond:
            return """ft³/s"""
        
        if unit_abbreviation == VolumeFlowUnits.CubicFootPerMinute:
            return """ft³/min"""
        
        if unit_abbreviation == VolumeFlowUnits.CubicFootPerHour:
            return """ft³/h"""
        
        if unit_abbreviation == VolumeFlowUnits.CubicYardPerSecond:
            return """yd³/s"""
        
        if unit_abbreviation == VolumeFlowUnits.CubicYardPerMinute:
            return """yd³/min"""
        
        if unit_abbreviation == VolumeFlowUnits.CubicYardPerHour:
            return """yd³/h"""
        
        if unit_abbreviation == VolumeFlowUnits.CubicYardPerDay:
            return """cy/day"""
        
        if unit_abbreviation == VolumeFlowUnits.MillionUsGallonPerDay:
            return """MGD"""
        
        if unit_abbreviation == VolumeFlowUnits.UsGallonPerDay:
            return """gpd"""
        
        if unit_abbreviation == VolumeFlowUnits.LiterPerSecond:
            return """L/s"""
        
        if unit_abbreviation == VolumeFlowUnits.LiterPerMinute:
            return """L/min"""
        
        if unit_abbreviation == VolumeFlowUnits.LiterPerHour:
            return """L/h"""
        
        if unit_abbreviation == VolumeFlowUnits.LiterPerDay:
            return """l/day"""
        
        if unit_abbreviation == VolumeFlowUnits.UsGallonPerSecond:
            return """gal (U.S.)/s"""
        
        if unit_abbreviation == VolumeFlowUnits.UsGallonPerMinute:
            return """gal (U.S.)/min"""
        
        if unit_abbreviation == VolumeFlowUnits.UkGallonPerDay:
            return """gal (U. K.)/d"""
        
        if unit_abbreviation == VolumeFlowUnits.UkGallonPerHour:
            return """gal (imp.)/h"""
        
        if unit_abbreviation == VolumeFlowUnits.UkGallonPerMinute:
            return """gal (imp.)/min"""
        
        if unit_abbreviation == VolumeFlowUnits.UkGallonPerSecond:
            return """gal (imp.)/s"""
        
        if unit_abbreviation == VolumeFlowUnits.KilousGallonPerMinute:
            return """kgal (U.S.)/min"""
        
        if unit_abbreviation == VolumeFlowUnits.UsGallonPerHour:
            return """gal (U.S.)/h"""
        
        if unit_abbreviation == VolumeFlowUnits.CubicDecimeterPerMinute:
            return """dm³/min"""
        
        if unit_abbreviation == VolumeFlowUnits.OilBarrelPerDay:
            return """bbl/d"""
        
        if unit_abbreviation == VolumeFlowUnits.OilBarrelPerMinute:
            return """bbl/min"""
        
        if unit_abbreviation == VolumeFlowUnits.OilBarrelPerHour:
            return """bbl/hr"""
        
        if unit_abbreviation == VolumeFlowUnits.OilBarrelPerSecond:
            return """bbl/s"""
        
        if unit_abbreviation == VolumeFlowUnits.CubicMillimeterPerSecond:
            return """mm³/s"""
        
        if unit_abbreviation == VolumeFlowUnits.AcreFootPerSecond:
            return """af/s"""
        
        if unit_abbreviation == VolumeFlowUnits.AcreFootPerMinute:
            return """af/m"""
        
        if unit_abbreviation == VolumeFlowUnits.AcreFootPerHour:
            return """af/h"""
        
        if unit_abbreviation == VolumeFlowUnits.AcreFootPerDay:
            return """af/d"""
        
        if unit_abbreviation == VolumeFlowUnits.CubicCentimeterPerMinute:
            return """cm³/min"""
        
        if unit_abbreviation == VolumeFlowUnits.MegausGallonPerDay:
            return """Mgpd"""
        
        if unit_abbreviation == VolumeFlowUnits.NanoliterPerSecond:
            return """nL/s"""
        
        if unit_abbreviation == VolumeFlowUnits.MicroliterPerSecond:
            return """μL/s"""
        
        if unit_abbreviation == VolumeFlowUnits.MilliliterPerSecond:
            return """mL/s"""
        
        if unit_abbreviation == VolumeFlowUnits.CentiliterPerSecond:
            return """cL/s"""
        
        if unit_abbreviation == VolumeFlowUnits.DeciliterPerSecond:
            return """dL/s"""
        
        if unit_abbreviation == VolumeFlowUnits.DecaliterPerSecond:
            return """daL/s"""
        
        if unit_abbreviation == VolumeFlowUnits.HectoliterPerSecond:
            return """hL/s"""
        
        if unit_abbreviation == VolumeFlowUnits.KiloliterPerSecond:
            return """kL/s"""
        
        if unit_abbreviation == VolumeFlowUnits.MegaliterPerSecond:
            return """ML/s"""
        
        if unit_abbreviation == VolumeFlowUnits.NanoliterPerMinute:
            return """nL/min"""
        
        if unit_abbreviation == VolumeFlowUnits.MicroliterPerMinute:
            return """μL/min"""
        
        if unit_abbreviation == VolumeFlowUnits.MilliliterPerMinute:
            return """mL/min"""
        
        if unit_abbreviation == VolumeFlowUnits.CentiliterPerMinute:
            return """cL/min"""
        
        if unit_abbreviation == VolumeFlowUnits.DeciliterPerMinute:
            return """dL/min"""
        
        if unit_abbreviation == VolumeFlowUnits.DecaliterPerMinute:
            return """daL/min"""
        
        if unit_abbreviation == VolumeFlowUnits.HectoliterPerMinute:
            return """hL/min"""
        
        if unit_abbreviation == VolumeFlowUnits.KiloliterPerMinute:
            return """kL/min"""
        
        if unit_abbreviation == VolumeFlowUnits.MegaliterPerMinute:
            return """ML/min"""
        
        if unit_abbreviation == VolumeFlowUnits.NanoliterPerHour:
            return """nL/h"""
        
        if unit_abbreviation == VolumeFlowUnits.MicroliterPerHour:
            return """μL/h"""
        
        if unit_abbreviation == VolumeFlowUnits.MilliliterPerHour:
            return """mL/h"""
        
        if unit_abbreviation == VolumeFlowUnits.CentiliterPerHour:
            return """cL/h"""
        
        if unit_abbreviation == VolumeFlowUnits.DeciliterPerHour:
            return """dL/h"""
        
        if unit_abbreviation == VolumeFlowUnits.DecaliterPerHour:
            return """daL/h"""
        
        if unit_abbreviation == VolumeFlowUnits.HectoliterPerHour:
            return """hL/h"""
        
        if unit_abbreviation == VolumeFlowUnits.KiloliterPerHour:
            return """kL/h"""
        
        if unit_abbreviation == VolumeFlowUnits.MegaliterPerHour:
            return """ML/h"""
        
        if unit_abbreviation == VolumeFlowUnits.NanoliterPerDay:
            return """nl/day"""
        
        if unit_abbreviation == VolumeFlowUnits.MicroliterPerDay:
            return """μl/day"""
        
        if unit_abbreviation == VolumeFlowUnits.MilliliterPerDay:
            return """ml/day"""
        
        if unit_abbreviation == VolumeFlowUnits.CentiliterPerDay:
            return """cl/day"""
        
        if unit_abbreviation == VolumeFlowUnits.DeciliterPerDay:
            return """dl/day"""
        
        if unit_abbreviation == VolumeFlowUnits.DecaliterPerDay:
            return """dal/day"""
        
        if unit_abbreviation == VolumeFlowUnits.HectoliterPerDay:
            return """hl/day"""
        
        if unit_abbreviation == VolumeFlowUnits.KiloliterPerDay:
            return """kl/day"""
        
        if unit_abbreviation == VolumeFlowUnits.MegaliterPerDay:
            return """Ml/day"""
        
        if unit_abbreviation == VolumeFlowUnits.MegaukGallonPerDay:
            return """Mgal (U. K.)/d"""
        
        if unit_abbreviation == VolumeFlowUnits.MegaukGallonPerSecond:
            return """Mgal (imp.)/s"""
        
from enum import Enum
import math
import string


class VolumeFlowUnits(Enum):
        """
            VolumeFlowUnits enumeration
        """
        
        CubicMeterPerSecond = 'cubic_meter_per_second'
        """
            
        """
        
        CubicMeterPerMinute = 'cubic_meter_per_minute'
        """
            
        """
        
        CubicMeterPerHour = 'cubic_meter_per_hour'
        """
            
        """
        
        CubicMeterPerDay = 'cubic_meter_per_day'
        """
            
        """
        
        CubicFootPerSecond = 'cubic_foot_per_second'
        """
            
        """
        
        CubicFootPerMinute = 'cubic_foot_per_minute'
        """
            
        """
        
        CubicFootPerHour = 'cubic_foot_per_hour'
        """
            
        """
        
        CubicYardPerSecond = 'cubic_yard_per_second'
        """
            
        """
        
        CubicYardPerMinute = 'cubic_yard_per_minute'
        """
            
        """
        
        CubicYardPerHour = 'cubic_yard_per_hour'
        """
            
        """
        
        CubicYardPerDay = 'cubic_yard_per_day'
        """
            
        """
        
        MillionUsGallonPerDay = 'million_us_gallon_per_day'
        """
            
        """
        
        UsGallonPerDay = 'us_gallon_per_day'
        """
            
        """
        
        LiterPerSecond = 'liter_per_second'
        """
            
        """
        
        LiterPerMinute = 'liter_per_minute'
        """
            
        """
        
        LiterPerHour = 'liter_per_hour'
        """
            
        """
        
        LiterPerDay = 'liter_per_day'
        """
            
        """
        
        UsGallonPerSecond = 'us_gallon_per_second'
        """
            
        """
        
        UsGallonPerMinute = 'us_gallon_per_minute'
        """
            
        """
        
        UkGallonPerDay = 'uk_gallon_per_day'
        """
            
        """
        
        UkGallonPerHour = 'uk_gallon_per_hour'
        """
            
        """
        
        UkGallonPerMinute = 'uk_gallon_per_minute'
        """
            
        """
        
        UkGallonPerSecond = 'uk_gallon_per_second'
        """
            
        """
        
        KilousGallonPerMinute = 'kilous_gallon_per_minute'
        """
            
        """
        
        UsGallonPerHour = 'us_gallon_per_hour'
        """
            
        """
        
        CubicDecimeterPerMinute = 'cubic_decimeter_per_minute'
        """
            
        """
        
        OilBarrelPerDay = 'oil_barrel_per_day'
        """
            
        """
        
        OilBarrelPerMinute = 'oil_barrel_per_minute'
        """
            
        """
        
        OilBarrelPerHour = 'oil_barrel_per_hour'
        """
            
        """
        
        OilBarrelPerSecond = 'oil_barrel_per_second'
        """
            
        """
        
        CubicMillimeterPerSecond = 'cubic_millimeter_per_second'
        """
            
        """
        
        AcreFootPerSecond = 'acre_foot_per_second'
        """
            
        """
        
        AcreFootPerMinute = 'acre_foot_per_minute'
        """
            
        """
        
        AcreFootPerHour = 'acre_foot_per_hour'
        """
            
        """
        
        AcreFootPerDay = 'acre_foot_per_day'
        """
            
        """
        
        CubicCentimeterPerMinute = 'cubic_centimeter_per_minute'
        """
            
        """
        
        MegaUsGallonPerDay = 'mega_us_gallon_per_day'
        """
            
        """
        
        NanoLiterPerSecond = 'nano_liter_per_second'
        """
            
        """
        
        MicroLiterPerSecond = 'micro_liter_per_second'
        """
            
        """
        
        MilliLiterPerSecond = 'milli_liter_per_second'
        """
            
        """
        
        CentiLiterPerSecond = 'centi_liter_per_second'
        """
            
        """
        
        DeciLiterPerSecond = 'deci_liter_per_second'
        """
            
        """
        
        KiloLiterPerSecond = 'kilo_liter_per_second'
        """
            
        """
        
        MegaLiterPerSecond = 'mega_liter_per_second'
        """
            
        """
        
        NanoLiterPerMinute = 'nano_liter_per_minute'
        """
            
        """
        
        MicroLiterPerMinute = 'micro_liter_per_minute'
        """
            
        """
        
        MilliLiterPerMinute = 'milli_liter_per_minute'
        """
            
        """
        
        CentiLiterPerMinute = 'centi_liter_per_minute'
        """
            
        """
        
        DeciLiterPerMinute = 'deci_liter_per_minute'
        """
            
        """
        
        KiloLiterPerMinute = 'kilo_liter_per_minute'
        """
            
        """
        
        MegaLiterPerMinute = 'mega_liter_per_minute'
        """
            
        """
        
        NanoLiterPerHour = 'nano_liter_per_hour'
        """
            
        """
        
        MicroLiterPerHour = 'micro_liter_per_hour'
        """
            
        """
        
        MilliLiterPerHour = 'milli_liter_per_hour'
        """
            
        """
        
        CentiLiterPerHour = 'centi_liter_per_hour'
        """
            
        """
        
        DeciLiterPerHour = 'deci_liter_per_hour'
        """
            
        """
        
        KiloLiterPerHour = 'kilo_liter_per_hour'
        """
            
        """
        
        MegaLiterPerHour = 'mega_liter_per_hour'
        """
            
        """
        
        NanoLiterPerDay = 'nano_liter_per_day'
        """
            
        """
        
        MicroLiterPerDay = 'micro_liter_per_day'
        """
            
        """
        
        MilliLiterPerDay = 'milli_liter_per_day'
        """
            
        """
        
        CentiLiterPerDay = 'centi_liter_per_day'
        """
            
        """
        
        DeciLiterPerDay = 'deci_liter_per_day'
        """
            
        """
        
        KiloLiterPerDay = 'kilo_liter_per_day'
        """
            
        """
        
        MegaLiterPerDay = 'mega_liter_per_day'
        """
            
        """
        
        MegaUkGallonPerDay = 'mega_uk_gallon_per_day'
        """
            
        """
        
        MegaUkGallonPerSecond = 'mega_uk_gallon_per_second'
        """
            
        """
        

class VolumeFlow:
    """
    In physics and engineering, in particular fluid dynamics and hydrometry, the volumetric flow rate, (also known as volume flow rate, rate of fluid flow or volume velocity) is the volume of fluid which passes through a given surface per unit time. The SI unit is m³/s (cubic meters per second). In US Customary Units and British Imperial Units, volumetric flow rate is often expressed as ft³/s (cubic feet per second). It is usually represented by the symbol Q.

    Args:
        value (float): The value.
        from_unit (VolumeFlowUnits): The VolumeFlow unit to create from, The default unit is CubicMeterPerSecond
    """
    def __init__(self, value: float, from_unit: VolumeFlowUnits = VolumeFlowUnits.CubicMeterPerSecond):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
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
        
        self.__mega_us_gallons_per_day = None
        
        self.__nano_liters_per_second = None
        
        self.__micro_liters_per_second = None
        
        self.__milli_liters_per_second = None
        
        self.__centi_liters_per_second = None
        
        self.__deci_liters_per_second = None
        
        self.__kilo_liters_per_second = None
        
        self.__mega_liters_per_second = None
        
        self.__nano_liters_per_minute = None
        
        self.__micro_liters_per_minute = None
        
        self.__milli_liters_per_minute = None
        
        self.__centi_liters_per_minute = None
        
        self.__deci_liters_per_minute = None
        
        self.__kilo_liters_per_minute = None
        
        self.__mega_liters_per_minute = None
        
        self.__nano_liters_per_hour = None
        
        self.__micro_liters_per_hour = None
        
        self.__milli_liters_per_hour = None
        
        self.__centi_liters_per_hour = None
        
        self.__deci_liters_per_hour = None
        
        self.__kilo_liters_per_hour = None
        
        self.__mega_liters_per_hour = None
        
        self.__nano_liters_per_day = None
        
        self.__micro_liters_per_day = None
        
        self.__milli_liters_per_day = None
        
        self.__centi_liters_per_day = None
        
        self.__deci_liters_per_day = None
        
        self.__kilo_liters_per_day = None
        
        self.__mega_liters_per_day = None
        
        self.__mega_uk_gallons_per_day = None
        
        self.__mega_uk_gallons_per_second = None
        

    def __convert_from_base(self, from_unit: VolumeFlowUnits) -> float:
        value = self.__value
        
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
        
        if from_unit == VolumeFlowUnits.MegaUsGallonPerDay:
            return ((value * 22824465.227) / 1000000.0)
        
        if from_unit == VolumeFlowUnits.NanoLiterPerSecond:
            return ((value * 1000) / 1e-09)
        
        if from_unit == VolumeFlowUnits.MicroLiterPerSecond:
            return ((value * 1000) / 1e-06)
        
        if from_unit == VolumeFlowUnits.MilliLiterPerSecond:
            return ((value * 1000) / 0.001)
        
        if from_unit == VolumeFlowUnits.CentiLiterPerSecond:
            return ((value * 1000) / 0.01)
        
        if from_unit == VolumeFlowUnits.DeciLiterPerSecond:
            return ((value * 1000) / 0.1)
        
        if from_unit == VolumeFlowUnits.KiloLiterPerSecond:
            return ((value * 1000) / 1000.0)
        
        if from_unit == VolumeFlowUnits.MegaLiterPerSecond:
            return ((value * 1000) / 1000000.0)
        
        if from_unit == VolumeFlowUnits.NanoLiterPerMinute:
            return ((value * 60000.00000) / 1e-09)
        
        if from_unit == VolumeFlowUnits.MicroLiterPerMinute:
            return ((value * 60000.00000) / 1e-06)
        
        if from_unit == VolumeFlowUnits.MilliLiterPerMinute:
            return ((value * 60000.00000) / 0.001)
        
        if from_unit == VolumeFlowUnits.CentiLiterPerMinute:
            return ((value * 60000.00000) / 0.01)
        
        if from_unit == VolumeFlowUnits.DeciLiterPerMinute:
            return ((value * 60000.00000) / 0.1)
        
        if from_unit == VolumeFlowUnits.KiloLiterPerMinute:
            return ((value * 60000.00000) / 1000.0)
        
        if from_unit == VolumeFlowUnits.MegaLiterPerMinute:
            return ((value * 60000.00000) / 1000000.0)
        
        if from_unit == VolumeFlowUnits.NanoLiterPerHour:
            return ((value * 3600000.000) / 1e-09)
        
        if from_unit == VolumeFlowUnits.MicroLiterPerHour:
            return ((value * 3600000.000) / 1e-06)
        
        if from_unit == VolumeFlowUnits.MilliLiterPerHour:
            return ((value * 3600000.000) / 0.001)
        
        if from_unit == VolumeFlowUnits.CentiLiterPerHour:
            return ((value * 3600000.000) / 0.01)
        
        if from_unit == VolumeFlowUnits.DeciLiterPerHour:
            return ((value * 3600000.000) / 0.1)
        
        if from_unit == VolumeFlowUnits.KiloLiterPerHour:
            return ((value * 3600000.000) / 1000.0)
        
        if from_unit == VolumeFlowUnits.MegaLiterPerHour:
            return ((value * 3600000.000) / 1000000.0)
        
        if from_unit == VolumeFlowUnits.NanoLiterPerDay:
            return ((value * 86400000) / 1e-09)
        
        if from_unit == VolumeFlowUnits.MicroLiterPerDay:
            return ((value * 86400000) / 1e-06)
        
        if from_unit == VolumeFlowUnits.MilliLiterPerDay:
            return ((value * 86400000) / 0.001)
        
        if from_unit == VolumeFlowUnits.CentiLiterPerDay:
            return ((value * 86400000) / 0.01)
        
        if from_unit == VolumeFlowUnits.DeciLiterPerDay:
            return ((value * 86400000) / 0.1)
        
        if from_unit == VolumeFlowUnits.KiloLiterPerDay:
            return ((value * 86400000) / 1000.0)
        
        if from_unit == VolumeFlowUnits.MegaLiterPerDay:
            return ((value * 86400000) / 1000000.0)
        
        if from_unit == VolumeFlowUnits.MegaUkGallonPerDay:
            return ((value * 19005304) / 1000000.0)
        
        if from_unit == VolumeFlowUnits.MegaUkGallonPerSecond:
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
        
        if to_unit == VolumeFlowUnits.MegaUsGallonPerDay:
            return ((value / 22824465.227) * 1000000.0)
        
        if to_unit == VolumeFlowUnits.NanoLiterPerSecond:
            return ((value / 1000) * 1e-09)
        
        if to_unit == VolumeFlowUnits.MicroLiterPerSecond:
            return ((value / 1000) * 1e-06)
        
        if to_unit == VolumeFlowUnits.MilliLiterPerSecond:
            return ((value / 1000) * 0.001)
        
        if to_unit == VolumeFlowUnits.CentiLiterPerSecond:
            return ((value / 1000) * 0.01)
        
        if to_unit == VolumeFlowUnits.DeciLiterPerSecond:
            return ((value / 1000) * 0.1)
        
        if to_unit == VolumeFlowUnits.KiloLiterPerSecond:
            return ((value / 1000) * 1000.0)
        
        if to_unit == VolumeFlowUnits.MegaLiterPerSecond:
            return ((value / 1000) * 1000000.0)
        
        if to_unit == VolumeFlowUnits.NanoLiterPerMinute:
            return ((value / 60000.00000) * 1e-09)
        
        if to_unit == VolumeFlowUnits.MicroLiterPerMinute:
            return ((value / 60000.00000) * 1e-06)
        
        if to_unit == VolumeFlowUnits.MilliLiterPerMinute:
            return ((value / 60000.00000) * 0.001)
        
        if to_unit == VolumeFlowUnits.CentiLiterPerMinute:
            return ((value / 60000.00000) * 0.01)
        
        if to_unit == VolumeFlowUnits.DeciLiterPerMinute:
            return ((value / 60000.00000) * 0.1)
        
        if to_unit == VolumeFlowUnits.KiloLiterPerMinute:
            return ((value / 60000.00000) * 1000.0)
        
        if to_unit == VolumeFlowUnits.MegaLiterPerMinute:
            return ((value / 60000.00000) * 1000000.0)
        
        if to_unit == VolumeFlowUnits.NanoLiterPerHour:
            return ((value / 3600000.000) * 1e-09)
        
        if to_unit == VolumeFlowUnits.MicroLiterPerHour:
            return ((value / 3600000.000) * 1e-06)
        
        if to_unit == VolumeFlowUnits.MilliLiterPerHour:
            return ((value / 3600000.000) * 0.001)
        
        if to_unit == VolumeFlowUnits.CentiLiterPerHour:
            return ((value / 3600000.000) * 0.01)
        
        if to_unit == VolumeFlowUnits.DeciLiterPerHour:
            return ((value / 3600000.000) * 0.1)
        
        if to_unit == VolumeFlowUnits.KiloLiterPerHour:
            return ((value / 3600000.000) * 1000.0)
        
        if to_unit == VolumeFlowUnits.MegaLiterPerHour:
            return ((value / 3600000.000) * 1000000.0)
        
        if to_unit == VolumeFlowUnits.NanoLiterPerDay:
            return ((value / 86400000) * 1e-09)
        
        if to_unit == VolumeFlowUnits.MicroLiterPerDay:
            return ((value / 86400000) * 1e-06)
        
        if to_unit == VolumeFlowUnits.MilliLiterPerDay:
            return ((value / 86400000) * 0.001)
        
        if to_unit == VolumeFlowUnits.CentiLiterPerDay:
            return ((value / 86400000) * 0.01)
        
        if to_unit == VolumeFlowUnits.DeciLiterPerDay:
            return ((value / 86400000) * 0.1)
        
        if to_unit == VolumeFlowUnits.KiloLiterPerDay:
            return ((value / 86400000) * 1000.0)
        
        if to_unit == VolumeFlowUnits.MegaLiterPerDay:
            return ((value / 86400000) * 1000000.0)
        
        if to_unit == VolumeFlowUnits.MegaUkGallonPerDay:
            return ((value / 19005304) * 1000000.0)
        
        if to_unit == VolumeFlowUnits.MegaUkGallonPerSecond:
            return ((value / 219.969) * 1000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
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
    def from_mega_us_gallons_per_day(mega_us_gallons_per_day: float):
        """
        Create a new instance of VolumeFlow from a value in mega_us_gallons_per_day.

        

        :param meters: The VolumeFlow value in mega_us_gallons_per_day.
        :type mega_us_gallons_per_day: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(mega_us_gallons_per_day, VolumeFlowUnits.MegaUsGallonPerDay)

    
    @staticmethod
    def from_nano_liters_per_second(nano_liters_per_second: float):
        """
        Create a new instance of VolumeFlow from a value in nano_liters_per_second.

        

        :param meters: The VolumeFlow value in nano_liters_per_second.
        :type nano_liters_per_second: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(nano_liters_per_second, VolumeFlowUnits.NanoLiterPerSecond)

    
    @staticmethod
    def from_micro_liters_per_second(micro_liters_per_second: float):
        """
        Create a new instance of VolumeFlow from a value in micro_liters_per_second.

        

        :param meters: The VolumeFlow value in micro_liters_per_second.
        :type micro_liters_per_second: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(micro_liters_per_second, VolumeFlowUnits.MicroLiterPerSecond)

    
    @staticmethod
    def from_milli_liters_per_second(milli_liters_per_second: float):
        """
        Create a new instance of VolumeFlow from a value in milli_liters_per_second.

        

        :param meters: The VolumeFlow value in milli_liters_per_second.
        :type milli_liters_per_second: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(milli_liters_per_second, VolumeFlowUnits.MilliLiterPerSecond)

    
    @staticmethod
    def from_centi_liters_per_second(centi_liters_per_second: float):
        """
        Create a new instance of VolumeFlow from a value in centi_liters_per_second.

        

        :param meters: The VolumeFlow value in centi_liters_per_second.
        :type centi_liters_per_second: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(centi_liters_per_second, VolumeFlowUnits.CentiLiterPerSecond)

    
    @staticmethod
    def from_deci_liters_per_second(deci_liters_per_second: float):
        """
        Create a new instance of VolumeFlow from a value in deci_liters_per_second.

        

        :param meters: The VolumeFlow value in deci_liters_per_second.
        :type deci_liters_per_second: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(deci_liters_per_second, VolumeFlowUnits.DeciLiterPerSecond)

    
    @staticmethod
    def from_kilo_liters_per_second(kilo_liters_per_second: float):
        """
        Create a new instance of VolumeFlow from a value in kilo_liters_per_second.

        

        :param meters: The VolumeFlow value in kilo_liters_per_second.
        :type kilo_liters_per_second: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(kilo_liters_per_second, VolumeFlowUnits.KiloLiterPerSecond)

    
    @staticmethod
    def from_mega_liters_per_second(mega_liters_per_second: float):
        """
        Create a new instance of VolumeFlow from a value in mega_liters_per_second.

        

        :param meters: The VolumeFlow value in mega_liters_per_second.
        :type mega_liters_per_second: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(mega_liters_per_second, VolumeFlowUnits.MegaLiterPerSecond)

    
    @staticmethod
    def from_nano_liters_per_minute(nano_liters_per_minute: float):
        """
        Create a new instance of VolumeFlow from a value in nano_liters_per_minute.

        

        :param meters: The VolumeFlow value in nano_liters_per_minute.
        :type nano_liters_per_minute: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(nano_liters_per_minute, VolumeFlowUnits.NanoLiterPerMinute)

    
    @staticmethod
    def from_micro_liters_per_minute(micro_liters_per_minute: float):
        """
        Create a new instance of VolumeFlow from a value in micro_liters_per_minute.

        

        :param meters: The VolumeFlow value in micro_liters_per_minute.
        :type micro_liters_per_minute: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(micro_liters_per_minute, VolumeFlowUnits.MicroLiterPerMinute)

    
    @staticmethod
    def from_milli_liters_per_minute(milli_liters_per_minute: float):
        """
        Create a new instance of VolumeFlow from a value in milli_liters_per_minute.

        

        :param meters: The VolumeFlow value in milli_liters_per_minute.
        :type milli_liters_per_minute: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(milli_liters_per_minute, VolumeFlowUnits.MilliLiterPerMinute)

    
    @staticmethod
    def from_centi_liters_per_minute(centi_liters_per_minute: float):
        """
        Create a new instance of VolumeFlow from a value in centi_liters_per_minute.

        

        :param meters: The VolumeFlow value in centi_liters_per_minute.
        :type centi_liters_per_minute: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(centi_liters_per_minute, VolumeFlowUnits.CentiLiterPerMinute)

    
    @staticmethod
    def from_deci_liters_per_minute(deci_liters_per_minute: float):
        """
        Create a new instance of VolumeFlow from a value in deci_liters_per_minute.

        

        :param meters: The VolumeFlow value in deci_liters_per_minute.
        :type deci_liters_per_minute: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(deci_liters_per_minute, VolumeFlowUnits.DeciLiterPerMinute)

    
    @staticmethod
    def from_kilo_liters_per_minute(kilo_liters_per_minute: float):
        """
        Create a new instance of VolumeFlow from a value in kilo_liters_per_minute.

        

        :param meters: The VolumeFlow value in kilo_liters_per_minute.
        :type kilo_liters_per_minute: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(kilo_liters_per_minute, VolumeFlowUnits.KiloLiterPerMinute)

    
    @staticmethod
    def from_mega_liters_per_minute(mega_liters_per_minute: float):
        """
        Create a new instance of VolumeFlow from a value in mega_liters_per_minute.

        

        :param meters: The VolumeFlow value in mega_liters_per_minute.
        :type mega_liters_per_minute: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(mega_liters_per_minute, VolumeFlowUnits.MegaLiterPerMinute)

    
    @staticmethod
    def from_nano_liters_per_hour(nano_liters_per_hour: float):
        """
        Create a new instance of VolumeFlow from a value in nano_liters_per_hour.

        

        :param meters: The VolumeFlow value in nano_liters_per_hour.
        :type nano_liters_per_hour: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(nano_liters_per_hour, VolumeFlowUnits.NanoLiterPerHour)

    
    @staticmethod
    def from_micro_liters_per_hour(micro_liters_per_hour: float):
        """
        Create a new instance of VolumeFlow from a value in micro_liters_per_hour.

        

        :param meters: The VolumeFlow value in micro_liters_per_hour.
        :type micro_liters_per_hour: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(micro_liters_per_hour, VolumeFlowUnits.MicroLiterPerHour)

    
    @staticmethod
    def from_milli_liters_per_hour(milli_liters_per_hour: float):
        """
        Create a new instance of VolumeFlow from a value in milli_liters_per_hour.

        

        :param meters: The VolumeFlow value in milli_liters_per_hour.
        :type milli_liters_per_hour: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(milli_liters_per_hour, VolumeFlowUnits.MilliLiterPerHour)

    
    @staticmethod
    def from_centi_liters_per_hour(centi_liters_per_hour: float):
        """
        Create a new instance of VolumeFlow from a value in centi_liters_per_hour.

        

        :param meters: The VolumeFlow value in centi_liters_per_hour.
        :type centi_liters_per_hour: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(centi_liters_per_hour, VolumeFlowUnits.CentiLiterPerHour)

    
    @staticmethod
    def from_deci_liters_per_hour(deci_liters_per_hour: float):
        """
        Create a new instance of VolumeFlow from a value in deci_liters_per_hour.

        

        :param meters: The VolumeFlow value in deci_liters_per_hour.
        :type deci_liters_per_hour: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(deci_liters_per_hour, VolumeFlowUnits.DeciLiterPerHour)

    
    @staticmethod
    def from_kilo_liters_per_hour(kilo_liters_per_hour: float):
        """
        Create a new instance of VolumeFlow from a value in kilo_liters_per_hour.

        

        :param meters: The VolumeFlow value in kilo_liters_per_hour.
        :type kilo_liters_per_hour: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(kilo_liters_per_hour, VolumeFlowUnits.KiloLiterPerHour)

    
    @staticmethod
    def from_mega_liters_per_hour(mega_liters_per_hour: float):
        """
        Create a new instance of VolumeFlow from a value in mega_liters_per_hour.

        

        :param meters: The VolumeFlow value in mega_liters_per_hour.
        :type mega_liters_per_hour: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(mega_liters_per_hour, VolumeFlowUnits.MegaLiterPerHour)

    
    @staticmethod
    def from_nano_liters_per_day(nano_liters_per_day: float):
        """
        Create a new instance of VolumeFlow from a value in nano_liters_per_day.

        

        :param meters: The VolumeFlow value in nano_liters_per_day.
        :type nano_liters_per_day: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(nano_liters_per_day, VolumeFlowUnits.NanoLiterPerDay)

    
    @staticmethod
    def from_micro_liters_per_day(micro_liters_per_day: float):
        """
        Create a new instance of VolumeFlow from a value in micro_liters_per_day.

        

        :param meters: The VolumeFlow value in micro_liters_per_day.
        :type micro_liters_per_day: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(micro_liters_per_day, VolumeFlowUnits.MicroLiterPerDay)

    
    @staticmethod
    def from_milli_liters_per_day(milli_liters_per_day: float):
        """
        Create a new instance of VolumeFlow from a value in milli_liters_per_day.

        

        :param meters: The VolumeFlow value in milli_liters_per_day.
        :type milli_liters_per_day: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(milli_liters_per_day, VolumeFlowUnits.MilliLiterPerDay)

    
    @staticmethod
    def from_centi_liters_per_day(centi_liters_per_day: float):
        """
        Create a new instance of VolumeFlow from a value in centi_liters_per_day.

        

        :param meters: The VolumeFlow value in centi_liters_per_day.
        :type centi_liters_per_day: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(centi_liters_per_day, VolumeFlowUnits.CentiLiterPerDay)

    
    @staticmethod
    def from_deci_liters_per_day(deci_liters_per_day: float):
        """
        Create a new instance of VolumeFlow from a value in deci_liters_per_day.

        

        :param meters: The VolumeFlow value in deci_liters_per_day.
        :type deci_liters_per_day: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(deci_liters_per_day, VolumeFlowUnits.DeciLiterPerDay)

    
    @staticmethod
    def from_kilo_liters_per_day(kilo_liters_per_day: float):
        """
        Create a new instance of VolumeFlow from a value in kilo_liters_per_day.

        

        :param meters: The VolumeFlow value in kilo_liters_per_day.
        :type kilo_liters_per_day: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(kilo_liters_per_day, VolumeFlowUnits.KiloLiterPerDay)

    
    @staticmethod
    def from_mega_liters_per_day(mega_liters_per_day: float):
        """
        Create a new instance of VolumeFlow from a value in mega_liters_per_day.

        

        :param meters: The VolumeFlow value in mega_liters_per_day.
        :type mega_liters_per_day: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(mega_liters_per_day, VolumeFlowUnits.MegaLiterPerDay)

    
    @staticmethod
    def from_mega_uk_gallons_per_day(mega_uk_gallons_per_day: float):
        """
        Create a new instance of VolumeFlow from a value in mega_uk_gallons_per_day.

        

        :param meters: The VolumeFlow value in mega_uk_gallons_per_day.
        :type mega_uk_gallons_per_day: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(mega_uk_gallons_per_day, VolumeFlowUnits.MegaUkGallonPerDay)

    
    @staticmethod
    def from_mega_uk_gallons_per_second(mega_uk_gallons_per_second: float):
        """
        Create a new instance of VolumeFlow from a value in mega_uk_gallons_per_second.

        

        :param meters: The VolumeFlow value in mega_uk_gallons_per_second.
        :type mega_uk_gallons_per_second: float
        :return: A new instance of VolumeFlow.
        :rtype: VolumeFlow
        """
        return VolumeFlow(mega_uk_gallons_per_second, VolumeFlowUnits.MegaUkGallonPerSecond)

    
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
    def mega_us_gallons_per_day(self) -> float:
        """
        
        """
        if self.__mega_us_gallons_per_day != None:
            return self.__mega_us_gallons_per_day
        self.__mega_us_gallons_per_day = self.__convert_from_base(VolumeFlowUnits.MegaUsGallonPerDay)
        return self.__mega_us_gallons_per_day

    
    @property
    def nano_liters_per_second(self) -> float:
        """
        
        """
        if self.__nano_liters_per_second != None:
            return self.__nano_liters_per_second
        self.__nano_liters_per_second = self.__convert_from_base(VolumeFlowUnits.NanoLiterPerSecond)
        return self.__nano_liters_per_second

    
    @property
    def micro_liters_per_second(self) -> float:
        """
        
        """
        if self.__micro_liters_per_second != None:
            return self.__micro_liters_per_second
        self.__micro_liters_per_second = self.__convert_from_base(VolumeFlowUnits.MicroLiterPerSecond)
        return self.__micro_liters_per_second

    
    @property
    def milli_liters_per_second(self) -> float:
        """
        
        """
        if self.__milli_liters_per_second != None:
            return self.__milli_liters_per_second
        self.__milli_liters_per_second = self.__convert_from_base(VolumeFlowUnits.MilliLiterPerSecond)
        return self.__milli_liters_per_second

    
    @property
    def centi_liters_per_second(self) -> float:
        """
        
        """
        if self.__centi_liters_per_second != None:
            return self.__centi_liters_per_second
        self.__centi_liters_per_second = self.__convert_from_base(VolumeFlowUnits.CentiLiterPerSecond)
        return self.__centi_liters_per_second

    
    @property
    def deci_liters_per_second(self) -> float:
        """
        
        """
        if self.__deci_liters_per_second != None:
            return self.__deci_liters_per_second
        self.__deci_liters_per_second = self.__convert_from_base(VolumeFlowUnits.DeciLiterPerSecond)
        return self.__deci_liters_per_second

    
    @property
    def kilo_liters_per_second(self) -> float:
        """
        
        """
        if self.__kilo_liters_per_second != None:
            return self.__kilo_liters_per_second
        self.__kilo_liters_per_second = self.__convert_from_base(VolumeFlowUnits.KiloLiterPerSecond)
        return self.__kilo_liters_per_second

    
    @property
    def mega_liters_per_second(self) -> float:
        """
        
        """
        if self.__mega_liters_per_second != None:
            return self.__mega_liters_per_second
        self.__mega_liters_per_second = self.__convert_from_base(VolumeFlowUnits.MegaLiterPerSecond)
        return self.__mega_liters_per_second

    
    @property
    def nano_liters_per_minute(self) -> float:
        """
        
        """
        if self.__nano_liters_per_minute != None:
            return self.__nano_liters_per_minute
        self.__nano_liters_per_minute = self.__convert_from_base(VolumeFlowUnits.NanoLiterPerMinute)
        return self.__nano_liters_per_minute

    
    @property
    def micro_liters_per_minute(self) -> float:
        """
        
        """
        if self.__micro_liters_per_minute != None:
            return self.__micro_liters_per_minute
        self.__micro_liters_per_minute = self.__convert_from_base(VolumeFlowUnits.MicroLiterPerMinute)
        return self.__micro_liters_per_minute

    
    @property
    def milli_liters_per_minute(self) -> float:
        """
        
        """
        if self.__milli_liters_per_minute != None:
            return self.__milli_liters_per_minute
        self.__milli_liters_per_minute = self.__convert_from_base(VolumeFlowUnits.MilliLiterPerMinute)
        return self.__milli_liters_per_minute

    
    @property
    def centi_liters_per_minute(self) -> float:
        """
        
        """
        if self.__centi_liters_per_minute != None:
            return self.__centi_liters_per_minute
        self.__centi_liters_per_minute = self.__convert_from_base(VolumeFlowUnits.CentiLiterPerMinute)
        return self.__centi_liters_per_minute

    
    @property
    def deci_liters_per_minute(self) -> float:
        """
        
        """
        if self.__deci_liters_per_minute != None:
            return self.__deci_liters_per_minute
        self.__deci_liters_per_minute = self.__convert_from_base(VolumeFlowUnits.DeciLiterPerMinute)
        return self.__deci_liters_per_minute

    
    @property
    def kilo_liters_per_minute(self) -> float:
        """
        
        """
        if self.__kilo_liters_per_minute != None:
            return self.__kilo_liters_per_minute
        self.__kilo_liters_per_minute = self.__convert_from_base(VolumeFlowUnits.KiloLiterPerMinute)
        return self.__kilo_liters_per_minute

    
    @property
    def mega_liters_per_minute(self) -> float:
        """
        
        """
        if self.__mega_liters_per_minute != None:
            return self.__mega_liters_per_minute
        self.__mega_liters_per_minute = self.__convert_from_base(VolumeFlowUnits.MegaLiterPerMinute)
        return self.__mega_liters_per_minute

    
    @property
    def nano_liters_per_hour(self) -> float:
        """
        
        """
        if self.__nano_liters_per_hour != None:
            return self.__nano_liters_per_hour
        self.__nano_liters_per_hour = self.__convert_from_base(VolumeFlowUnits.NanoLiterPerHour)
        return self.__nano_liters_per_hour

    
    @property
    def micro_liters_per_hour(self) -> float:
        """
        
        """
        if self.__micro_liters_per_hour != None:
            return self.__micro_liters_per_hour
        self.__micro_liters_per_hour = self.__convert_from_base(VolumeFlowUnits.MicroLiterPerHour)
        return self.__micro_liters_per_hour

    
    @property
    def milli_liters_per_hour(self) -> float:
        """
        
        """
        if self.__milli_liters_per_hour != None:
            return self.__milli_liters_per_hour
        self.__milli_liters_per_hour = self.__convert_from_base(VolumeFlowUnits.MilliLiterPerHour)
        return self.__milli_liters_per_hour

    
    @property
    def centi_liters_per_hour(self) -> float:
        """
        
        """
        if self.__centi_liters_per_hour != None:
            return self.__centi_liters_per_hour
        self.__centi_liters_per_hour = self.__convert_from_base(VolumeFlowUnits.CentiLiterPerHour)
        return self.__centi_liters_per_hour

    
    @property
    def deci_liters_per_hour(self) -> float:
        """
        
        """
        if self.__deci_liters_per_hour != None:
            return self.__deci_liters_per_hour
        self.__deci_liters_per_hour = self.__convert_from_base(VolumeFlowUnits.DeciLiterPerHour)
        return self.__deci_liters_per_hour

    
    @property
    def kilo_liters_per_hour(self) -> float:
        """
        
        """
        if self.__kilo_liters_per_hour != None:
            return self.__kilo_liters_per_hour
        self.__kilo_liters_per_hour = self.__convert_from_base(VolumeFlowUnits.KiloLiterPerHour)
        return self.__kilo_liters_per_hour

    
    @property
    def mega_liters_per_hour(self) -> float:
        """
        
        """
        if self.__mega_liters_per_hour != None:
            return self.__mega_liters_per_hour
        self.__mega_liters_per_hour = self.__convert_from_base(VolumeFlowUnits.MegaLiterPerHour)
        return self.__mega_liters_per_hour

    
    @property
    def nano_liters_per_day(self) -> float:
        """
        
        """
        if self.__nano_liters_per_day != None:
            return self.__nano_liters_per_day
        self.__nano_liters_per_day = self.__convert_from_base(VolumeFlowUnits.NanoLiterPerDay)
        return self.__nano_liters_per_day

    
    @property
    def micro_liters_per_day(self) -> float:
        """
        
        """
        if self.__micro_liters_per_day != None:
            return self.__micro_liters_per_day
        self.__micro_liters_per_day = self.__convert_from_base(VolumeFlowUnits.MicroLiterPerDay)
        return self.__micro_liters_per_day

    
    @property
    def milli_liters_per_day(self) -> float:
        """
        
        """
        if self.__milli_liters_per_day != None:
            return self.__milli_liters_per_day
        self.__milli_liters_per_day = self.__convert_from_base(VolumeFlowUnits.MilliLiterPerDay)
        return self.__milli_liters_per_day

    
    @property
    def centi_liters_per_day(self) -> float:
        """
        
        """
        if self.__centi_liters_per_day != None:
            return self.__centi_liters_per_day
        self.__centi_liters_per_day = self.__convert_from_base(VolumeFlowUnits.CentiLiterPerDay)
        return self.__centi_liters_per_day

    
    @property
    def deci_liters_per_day(self) -> float:
        """
        
        """
        if self.__deci_liters_per_day != None:
            return self.__deci_liters_per_day
        self.__deci_liters_per_day = self.__convert_from_base(VolumeFlowUnits.DeciLiterPerDay)
        return self.__deci_liters_per_day

    
    @property
    def kilo_liters_per_day(self) -> float:
        """
        
        """
        if self.__kilo_liters_per_day != None:
            return self.__kilo_liters_per_day
        self.__kilo_liters_per_day = self.__convert_from_base(VolumeFlowUnits.KiloLiterPerDay)
        return self.__kilo_liters_per_day

    
    @property
    def mega_liters_per_day(self) -> float:
        """
        
        """
        if self.__mega_liters_per_day != None:
            return self.__mega_liters_per_day
        self.__mega_liters_per_day = self.__convert_from_base(VolumeFlowUnits.MegaLiterPerDay)
        return self.__mega_liters_per_day

    
    @property
    def mega_uk_gallons_per_day(self) -> float:
        """
        
        """
        if self.__mega_uk_gallons_per_day != None:
            return self.__mega_uk_gallons_per_day
        self.__mega_uk_gallons_per_day = self.__convert_from_base(VolumeFlowUnits.MegaUkGallonPerDay)
        return self.__mega_uk_gallons_per_day

    
    @property
    def mega_uk_gallons_per_second(self) -> float:
        """
        
        """
        if self.__mega_uk_gallons_per_second != None:
            return self.__mega_uk_gallons_per_second
        self.__mega_uk_gallons_per_second = self.__convert_from_base(VolumeFlowUnits.MegaUkGallonPerSecond)
        return self.__mega_uk_gallons_per_second

    
    def to_string(self, unit: VolumeFlowUnits = VolumeFlowUnits.CubicMeterPerSecond) -> string:
        """
        Format the VolumeFlow to string.
        Note! the default format for VolumeFlow is CubicMeterPerSecond.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == VolumeFlowUnits.CubicMeterPerSecond:
            return f"""{self.cubic_meters_per_second} m³/s"""
        
        if unit == VolumeFlowUnits.CubicMeterPerMinute:
            return f"""{self.cubic_meters_per_minute} m³/min"""
        
        if unit == VolumeFlowUnits.CubicMeterPerHour:
            return f"""{self.cubic_meters_per_hour} m³/h"""
        
        if unit == VolumeFlowUnits.CubicMeterPerDay:
            return f"""{self.cubic_meters_per_day} m³/d"""
        
        if unit == VolumeFlowUnits.CubicFootPerSecond:
            return f"""{self.cubic_feet_per_second} ft³/s"""
        
        if unit == VolumeFlowUnits.CubicFootPerMinute:
            return f"""{self.cubic_feet_per_minute} ft³/min"""
        
        if unit == VolumeFlowUnits.CubicFootPerHour:
            return f"""{self.cubic_feet_per_hour} ft³/h"""
        
        if unit == VolumeFlowUnits.CubicYardPerSecond:
            return f"""{self.cubic_yards_per_second} yd³/s"""
        
        if unit == VolumeFlowUnits.CubicYardPerMinute:
            return f"""{self.cubic_yards_per_minute} yd³/min"""
        
        if unit == VolumeFlowUnits.CubicYardPerHour:
            return f"""{self.cubic_yards_per_hour} yd³/h"""
        
        if unit == VolumeFlowUnits.CubicYardPerDay:
            return f"""{self.cubic_yards_per_day} cy/day"""
        
        if unit == VolumeFlowUnits.MillionUsGallonPerDay:
            return f"""{self.million_us_gallons_per_day} MGD"""
        
        if unit == VolumeFlowUnits.UsGallonPerDay:
            return f"""{self.us_gallons_per_day} gpd"""
        
        if unit == VolumeFlowUnits.LiterPerSecond:
            return f"""{self.liters_per_second} L/s"""
        
        if unit == VolumeFlowUnits.LiterPerMinute:
            return f"""{self.liters_per_minute} L/min"""
        
        if unit == VolumeFlowUnits.LiterPerHour:
            return f"""{self.liters_per_hour} L/h"""
        
        if unit == VolumeFlowUnits.LiterPerDay:
            return f"""{self.liters_per_day} l/day"""
        
        if unit == VolumeFlowUnits.UsGallonPerSecond:
            return f"""{self.us_gallons_per_second} gal (U.S.)/s"""
        
        if unit == VolumeFlowUnits.UsGallonPerMinute:
            return f"""{self.us_gallons_per_minute} gal (U.S.)/min"""
        
        if unit == VolumeFlowUnits.UkGallonPerDay:
            return f"""{self.uk_gallons_per_day} gal (U. K.)/d"""
        
        if unit == VolumeFlowUnits.UkGallonPerHour:
            return f"""{self.uk_gallons_per_hour} gal (imp.)/h"""
        
        if unit == VolumeFlowUnits.UkGallonPerMinute:
            return f"""{self.uk_gallons_per_minute} gal (imp.)/min"""
        
        if unit == VolumeFlowUnits.UkGallonPerSecond:
            return f"""{self.uk_gallons_per_second} gal (imp.)/s"""
        
        if unit == VolumeFlowUnits.KilousGallonPerMinute:
            return f"""{self.kilous_gallons_per_minute} kgal (U.S.)/min"""
        
        if unit == VolumeFlowUnits.UsGallonPerHour:
            return f"""{self.us_gallons_per_hour} gal (U.S.)/h"""
        
        if unit == VolumeFlowUnits.CubicDecimeterPerMinute:
            return f"""{self.cubic_decimeters_per_minute} dm³/min"""
        
        if unit == VolumeFlowUnits.OilBarrelPerDay:
            return f"""{self.oil_barrels_per_day} bbl/d"""
        
        if unit == VolumeFlowUnits.OilBarrelPerMinute:
            return f"""{self.oil_barrels_per_minute} bbl/min"""
        
        if unit == VolumeFlowUnits.OilBarrelPerHour:
            return f"""{self.oil_barrels_per_hour} bbl/hr"""
        
        if unit == VolumeFlowUnits.OilBarrelPerSecond:
            return f"""{self.oil_barrels_per_second} bbl/s"""
        
        if unit == VolumeFlowUnits.CubicMillimeterPerSecond:
            return f"""{self.cubic_millimeters_per_second} mm³/s"""
        
        if unit == VolumeFlowUnits.AcreFootPerSecond:
            return f"""{self.acre_feet_per_second} af/s"""
        
        if unit == VolumeFlowUnits.AcreFootPerMinute:
            return f"""{self.acre_feet_per_minute} af/m"""
        
        if unit == VolumeFlowUnits.AcreFootPerHour:
            return f"""{self.acre_feet_per_hour} af/h"""
        
        if unit == VolumeFlowUnits.AcreFootPerDay:
            return f"""{self.acre_feet_per_day} af/d"""
        
        if unit == VolumeFlowUnits.CubicCentimeterPerMinute:
            return f"""{self.cubic_centimeters_per_minute} cm³/min"""
        
        if unit == VolumeFlowUnits.MegaUsGallonPerDay:
            return f"""{self.mega_us_gallons_per_day} """
        
        if unit == VolumeFlowUnits.NanoLiterPerSecond:
            return f"""{self.nano_liters_per_second} """
        
        if unit == VolumeFlowUnits.MicroLiterPerSecond:
            return f"""{self.micro_liters_per_second} """
        
        if unit == VolumeFlowUnits.MilliLiterPerSecond:
            return f"""{self.milli_liters_per_second} """
        
        if unit == VolumeFlowUnits.CentiLiterPerSecond:
            return f"""{self.centi_liters_per_second} """
        
        if unit == VolumeFlowUnits.DeciLiterPerSecond:
            return f"""{self.deci_liters_per_second} """
        
        if unit == VolumeFlowUnits.KiloLiterPerSecond:
            return f"""{self.kilo_liters_per_second} """
        
        if unit == VolumeFlowUnits.MegaLiterPerSecond:
            return f"""{self.mega_liters_per_second} """
        
        if unit == VolumeFlowUnits.NanoLiterPerMinute:
            return f"""{self.nano_liters_per_minute} """
        
        if unit == VolumeFlowUnits.MicroLiterPerMinute:
            return f"""{self.micro_liters_per_minute} """
        
        if unit == VolumeFlowUnits.MilliLiterPerMinute:
            return f"""{self.milli_liters_per_minute} """
        
        if unit == VolumeFlowUnits.CentiLiterPerMinute:
            return f"""{self.centi_liters_per_minute} """
        
        if unit == VolumeFlowUnits.DeciLiterPerMinute:
            return f"""{self.deci_liters_per_minute} """
        
        if unit == VolumeFlowUnits.KiloLiterPerMinute:
            return f"""{self.kilo_liters_per_minute} """
        
        if unit == VolumeFlowUnits.MegaLiterPerMinute:
            return f"""{self.mega_liters_per_minute} """
        
        if unit == VolumeFlowUnits.NanoLiterPerHour:
            return f"""{self.nano_liters_per_hour} """
        
        if unit == VolumeFlowUnits.MicroLiterPerHour:
            return f"""{self.micro_liters_per_hour} """
        
        if unit == VolumeFlowUnits.MilliLiterPerHour:
            return f"""{self.milli_liters_per_hour} """
        
        if unit == VolumeFlowUnits.CentiLiterPerHour:
            return f"""{self.centi_liters_per_hour} """
        
        if unit == VolumeFlowUnits.DeciLiterPerHour:
            return f"""{self.deci_liters_per_hour} """
        
        if unit == VolumeFlowUnits.KiloLiterPerHour:
            return f"""{self.kilo_liters_per_hour} """
        
        if unit == VolumeFlowUnits.MegaLiterPerHour:
            return f"""{self.mega_liters_per_hour} """
        
        if unit == VolumeFlowUnits.NanoLiterPerDay:
            return f"""{self.nano_liters_per_day} """
        
        if unit == VolumeFlowUnits.MicroLiterPerDay:
            return f"""{self.micro_liters_per_day} """
        
        if unit == VolumeFlowUnits.MilliLiterPerDay:
            return f"""{self.milli_liters_per_day} """
        
        if unit == VolumeFlowUnits.CentiLiterPerDay:
            return f"""{self.centi_liters_per_day} """
        
        if unit == VolumeFlowUnits.DeciLiterPerDay:
            return f"""{self.deci_liters_per_day} """
        
        if unit == VolumeFlowUnits.KiloLiterPerDay:
            return f"""{self.kilo_liters_per_day} """
        
        if unit == VolumeFlowUnits.MegaLiterPerDay:
            return f"""{self.mega_liters_per_day} """
        
        if unit == VolumeFlowUnits.MegaUkGallonPerDay:
            return f"""{self.mega_uk_gallons_per_day} """
        
        if unit == VolumeFlowUnits.MegaUkGallonPerSecond:
            return f"""{self.mega_uk_gallons_per_second} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: VolumeFlowUnits = VolumeFlowUnits.CubicMeterPerSecond) -> string:
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
        
        if unit_abbreviation == VolumeFlowUnits.MegaUsGallonPerDay:
            return """"""
        
        if unit_abbreviation == VolumeFlowUnits.NanoLiterPerSecond:
            return """"""
        
        if unit_abbreviation == VolumeFlowUnits.MicroLiterPerSecond:
            return """"""
        
        if unit_abbreviation == VolumeFlowUnits.MilliLiterPerSecond:
            return """"""
        
        if unit_abbreviation == VolumeFlowUnits.CentiLiterPerSecond:
            return """"""
        
        if unit_abbreviation == VolumeFlowUnits.DeciLiterPerSecond:
            return """"""
        
        if unit_abbreviation == VolumeFlowUnits.KiloLiterPerSecond:
            return """"""
        
        if unit_abbreviation == VolumeFlowUnits.MegaLiterPerSecond:
            return """"""
        
        if unit_abbreviation == VolumeFlowUnits.NanoLiterPerMinute:
            return """"""
        
        if unit_abbreviation == VolumeFlowUnits.MicroLiterPerMinute:
            return """"""
        
        if unit_abbreviation == VolumeFlowUnits.MilliLiterPerMinute:
            return """"""
        
        if unit_abbreviation == VolumeFlowUnits.CentiLiterPerMinute:
            return """"""
        
        if unit_abbreviation == VolumeFlowUnits.DeciLiterPerMinute:
            return """"""
        
        if unit_abbreviation == VolumeFlowUnits.KiloLiterPerMinute:
            return """"""
        
        if unit_abbreviation == VolumeFlowUnits.MegaLiterPerMinute:
            return """"""
        
        if unit_abbreviation == VolumeFlowUnits.NanoLiterPerHour:
            return """"""
        
        if unit_abbreviation == VolumeFlowUnits.MicroLiterPerHour:
            return """"""
        
        if unit_abbreviation == VolumeFlowUnits.MilliLiterPerHour:
            return """"""
        
        if unit_abbreviation == VolumeFlowUnits.CentiLiterPerHour:
            return """"""
        
        if unit_abbreviation == VolumeFlowUnits.DeciLiterPerHour:
            return """"""
        
        if unit_abbreviation == VolumeFlowUnits.KiloLiterPerHour:
            return """"""
        
        if unit_abbreviation == VolumeFlowUnits.MegaLiterPerHour:
            return """"""
        
        if unit_abbreviation == VolumeFlowUnits.NanoLiterPerDay:
            return """"""
        
        if unit_abbreviation == VolumeFlowUnits.MicroLiterPerDay:
            return """"""
        
        if unit_abbreviation == VolumeFlowUnits.MilliLiterPerDay:
            return """"""
        
        if unit_abbreviation == VolumeFlowUnits.CentiLiterPerDay:
            return """"""
        
        if unit_abbreviation == VolumeFlowUnits.DeciLiterPerDay:
            return """"""
        
        if unit_abbreviation == VolumeFlowUnits.KiloLiterPerDay:
            return """"""
        
        if unit_abbreviation == VolumeFlowUnits.MegaLiterPerDay:
            return """"""
        
        if unit_abbreviation == VolumeFlowUnits.MegaUkGallonPerDay:
            return """"""
        
        if unit_abbreviation == VolumeFlowUnits.MegaUkGallonPerSecond:
            return """"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, VolumeFlow):
            raise TypeError("unsupported operand type(s) for +: 'VolumeFlow' and '{}'".format(type(other).__name__))
        return VolumeFlow(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, VolumeFlow):
            raise TypeError("unsupported operand type(s) for *: 'VolumeFlow' and '{}'".format(type(other).__name__))
        return VolumeFlow(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, VolumeFlow):
            raise TypeError("unsupported operand type(s) for -: 'VolumeFlow' and '{}'".format(type(other).__name__))
        return VolumeFlow(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, VolumeFlow):
            raise TypeError("unsupported operand type(s) for /: 'VolumeFlow' and '{}'".format(type(other).__name__))
        return VolumeFlow(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, VolumeFlow):
            raise TypeError("unsupported operand type(s) for %: 'VolumeFlow' and '{}'".format(type(other).__name__))
        return VolumeFlow(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, VolumeFlow):
            raise TypeError("unsupported operand type(s) for **: 'VolumeFlow' and '{}'".format(type(other).__name__))
        return VolumeFlow(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, VolumeFlow):
            raise TypeError("unsupported operand type(s) for ==: 'VolumeFlow' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, VolumeFlow):
            raise TypeError("unsupported operand type(s) for <: 'VolumeFlow' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, VolumeFlow):
            raise TypeError("unsupported operand type(s) for >: 'VolumeFlow' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, VolumeFlow):
            raise TypeError("unsupported operand type(s) for <=: 'VolumeFlow' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, VolumeFlow):
            raise TypeError("unsupported operand type(s) for >=: 'VolumeFlow' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value
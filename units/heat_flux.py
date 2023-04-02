from enum import Enum
import math
import string


class HeatFluxUnits(Enum):
        """
            HeatFluxUnits enumeration
        """
        
        WattPerSquareMeter = 'watt_per_square_meter'
        """
            
        """
        
        WattPerSquareInch = 'watt_per_square_inch'
        """
            
        """
        
        WattPerSquareFoot = 'watt_per_square_foot'
        """
            
        """
        
        BtuPerSecondSquareInch = 'btu_per_second_square_inch'
        """
            
        """
        
        BtuPerSecondSquareFoot = 'btu_per_second_square_foot'
        """
            
        """
        
        BtuPerMinuteSquareFoot = 'btu_per_minute_square_foot'
        """
            
        """
        
        BtuPerHourSquareFoot = 'btu_per_hour_square_foot'
        """
            
        """
        
        CaloriePerSecondSquareCentimeter = 'calorie_per_second_square_centimeter'
        """
            
        """
        
        KilocaloriePerHourSquareMeter = 'kilocalorie_per_hour_square_meter'
        """
            
        """
        
        PoundForcePerFootSecond = 'pound_force_per_foot_second'
        """
            
        """
        
        PoundPerSecondCubed = 'pound_per_second_cubed'
        """
            
        """
        
        NanoWattPerSquareMeter = 'nano_watt_per_square_meter'
        """
            
        """
        
        MicroWattPerSquareMeter = 'micro_watt_per_square_meter'
        """
            
        """
        
        MilliWattPerSquareMeter = 'milli_watt_per_square_meter'
        """
            
        """
        
        CentiWattPerSquareMeter = 'centi_watt_per_square_meter'
        """
            
        """
        
        DeciWattPerSquareMeter = 'deci_watt_per_square_meter'
        """
            
        """
        
        KiloWattPerSquareMeter = 'kilo_watt_per_square_meter'
        """
            
        """
        
        KiloCaloriePerSecondSquareCentimeter = 'kilo_calorie_per_second_square_centimeter'
        """
            
        """
        

class HeatFlux:
    """
    Heat flux is the flow of energy per unit of area per unit of time

    Args:
        value (float): The value.
        from_unit (HeatFluxUnits): The HeatFlux unit to create from, The default unit is WattPerSquareMeter
    """
    def __init__(self, value: float, from_unit: HeatFluxUnits = HeatFluxUnits.WattPerSquareMeter):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
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
        
        self.__nano_watts_per_square_meter = None
        
        self.__micro_watts_per_square_meter = None
        
        self.__milli_watts_per_square_meter = None
        
        self.__centi_watts_per_square_meter = None
        
        self.__deci_watts_per_square_meter = None
        
        self.__kilo_watts_per_square_meter = None
        
        self.__kilo_calories_per_second_square_centimeter = None
        

    def __convert_from_base(self, from_unit: HeatFluxUnits) -> float:
        value = self.__value
        
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
        
        if from_unit == HeatFluxUnits.NanoWattPerSquareMeter:
            return ((value) / 1e-09)
        
        if from_unit == HeatFluxUnits.MicroWattPerSquareMeter:
            return ((value) / 1e-06)
        
        if from_unit == HeatFluxUnits.MilliWattPerSquareMeter:
            return ((value) / 0.001)
        
        if from_unit == HeatFluxUnits.CentiWattPerSquareMeter:
            return ((value) / 0.01)
        
        if from_unit == HeatFluxUnits.DeciWattPerSquareMeter:
            return ((value) / 0.1)
        
        if from_unit == HeatFluxUnits.KiloWattPerSquareMeter:
            return ((value) / 1000.0)
        
        if from_unit == HeatFluxUnits.KiloCaloriePerSecondSquareCentimeter:
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
        
        if to_unit == HeatFluxUnits.NanoWattPerSquareMeter:
            return ((value) * 1e-09)
        
        if to_unit == HeatFluxUnits.MicroWattPerSquareMeter:
            return ((value) * 1e-06)
        
        if to_unit == HeatFluxUnits.MilliWattPerSquareMeter:
            return ((value) * 0.001)
        
        if to_unit == HeatFluxUnits.CentiWattPerSquareMeter:
            return ((value) * 0.01)
        
        if to_unit == HeatFluxUnits.DeciWattPerSquareMeter:
            return ((value) * 0.1)
        
        if to_unit == HeatFluxUnits.KiloWattPerSquareMeter:
            return ((value) * 1000.0)
        
        if to_unit == HeatFluxUnits.KiloCaloriePerSecondSquareCentimeter:
            return ((value * 4.1868e4) * 1000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
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
    def from_nano_watts_per_square_meter(nano_watts_per_square_meter: float):
        """
        Create a new instance of HeatFlux from a value in nano_watts_per_square_meter.

        

        :param meters: The HeatFlux value in nano_watts_per_square_meter.
        :type nano_watts_per_square_meter: float
        :return: A new instance of HeatFlux.
        :rtype: HeatFlux
        """
        return HeatFlux(nano_watts_per_square_meter, HeatFluxUnits.NanoWattPerSquareMeter)

    
    @staticmethod
    def from_micro_watts_per_square_meter(micro_watts_per_square_meter: float):
        """
        Create a new instance of HeatFlux from a value in micro_watts_per_square_meter.

        

        :param meters: The HeatFlux value in micro_watts_per_square_meter.
        :type micro_watts_per_square_meter: float
        :return: A new instance of HeatFlux.
        :rtype: HeatFlux
        """
        return HeatFlux(micro_watts_per_square_meter, HeatFluxUnits.MicroWattPerSquareMeter)

    
    @staticmethod
    def from_milli_watts_per_square_meter(milli_watts_per_square_meter: float):
        """
        Create a new instance of HeatFlux from a value in milli_watts_per_square_meter.

        

        :param meters: The HeatFlux value in milli_watts_per_square_meter.
        :type milli_watts_per_square_meter: float
        :return: A new instance of HeatFlux.
        :rtype: HeatFlux
        """
        return HeatFlux(milli_watts_per_square_meter, HeatFluxUnits.MilliWattPerSquareMeter)

    
    @staticmethod
    def from_centi_watts_per_square_meter(centi_watts_per_square_meter: float):
        """
        Create a new instance of HeatFlux from a value in centi_watts_per_square_meter.

        

        :param meters: The HeatFlux value in centi_watts_per_square_meter.
        :type centi_watts_per_square_meter: float
        :return: A new instance of HeatFlux.
        :rtype: HeatFlux
        """
        return HeatFlux(centi_watts_per_square_meter, HeatFluxUnits.CentiWattPerSquareMeter)

    
    @staticmethod
    def from_deci_watts_per_square_meter(deci_watts_per_square_meter: float):
        """
        Create a new instance of HeatFlux from a value in deci_watts_per_square_meter.

        

        :param meters: The HeatFlux value in deci_watts_per_square_meter.
        :type deci_watts_per_square_meter: float
        :return: A new instance of HeatFlux.
        :rtype: HeatFlux
        """
        return HeatFlux(deci_watts_per_square_meter, HeatFluxUnits.DeciWattPerSquareMeter)

    
    @staticmethod
    def from_kilo_watts_per_square_meter(kilo_watts_per_square_meter: float):
        """
        Create a new instance of HeatFlux from a value in kilo_watts_per_square_meter.

        

        :param meters: The HeatFlux value in kilo_watts_per_square_meter.
        :type kilo_watts_per_square_meter: float
        :return: A new instance of HeatFlux.
        :rtype: HeatFlux
        """
        return HeatFlux(kilo_watts_per_square_meter, HeatFluxUnits.KiloWattPerSquareMeter)

    
    @staticmethod
    def from_kilo_calories_per_second_square_centimeter(kilo_calories_per_second_square_centimeter: float):
        """
        Create a new instance of HeatFlux from a value in kilo_calories_per_second_square_centimeter.

        

        :param meters: The HeatFlux value in kilo_calories_per_second_square_centimeter.
        :type kilo_calories_per_second_square_centimeter: float
        :return: A new instance of HeatFlux.
        :rtype: HeatFlux
        """
        return HeatFlux(kilo_calories_per_second_square_centimeter, HeatFluxUnits.KiloCaloriePerSecondSquareCentimeter)

    
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
    def nano_watts_per_square_meter(self) -> float:
        """
        
        """
        if self.__nano_watts_per_square_meter != None:
            return self.__nano_watts_per_square_meter
        self.__nano_watts_per_square_meter = self.__convert_from_base(HeatFluxUnits.NanoWattPerSquareMeter)
        return self.__nano_watts_per_square_meter

    
    @property
    def micro_watts_per_square_meter(self) -> float:
        """
        
        """
        if self.__micro_watts_per_square_meter != None:
            return self.__micro_watts_per_square_meter
        self.__micro_watts_per_square_meter = self.__convert_from_base(HeatFluxUnits.MicroWattPerSquareMeter)
        return self.__micro_watts_per_square_meter

    
    @property
    def milli_watts_per_square_meter(self) -> float:
        """
        
        """
        if self.__milli_watts_per_square_meter != None:
            return self.__milli_watts_per_square_meter
        self.__milli_watts_per_square_meter = self.__convert_from_base(HeatFluxUnits.MilliWattPerSquareMeter)
        return self.__milli_watts_per_square_meter

    
    @property
    def centi_watts_per_square_meter(self) -> float:
        """
        
        """
        if self.__centi_watts_per_square_meter != None:
            return self.__centi_watts_per_square_meter
        self.__centi_watts_per_square_meter = self.__convert_from_base(HeatFluxUnits.CentiWattPerSquareMeter)
        return self.__centi_watts_per_square_meter

    
    @property
    def deci_watts_per_square_meter(self) -> float:
        """
        
        """
        if self.__deci_watts_per_square_meter != None:
            return self.__deci_watts_per_square_meter
        self.__deci_watts_per_square_meter = self.__convert_from_base(HeatFluxUnits.DeciWattPerSquareMeter)
        return self.__deci_watts_per_square_meter

    
    @property
    def kilo_watts_per_square_meter(self) -> float:
        """
        
        """
        if self.__kilo_watts_per_square_meter != None:
            return self.__kilo_watts_per_square_meter
        self.__kilo_watts_per_square_meter = self.__convert_from_base(HeatFluxUnits.KiloWattPerSquareMeter)
        return self.__kilo_watts_per_square_meter

    
    @property
    def kilo_calories_per_second_square_centimeter(self) -> float:
        """
        
        """
        if self.__kilo_calories_per_second_square_centimeter != None:
            return self.__kilo_calories_per_second_square_centimeter
        self.__kilo_calories_per_second_square_centimeter = self.__convert_from_base(HeatFluxUnits.KiloCaloriePerSecondSquareCentimeter)
        return self.__kilo_calories_per_second_square_centimeter

    
    def to_string(self, unit: HeatFluxUnits = HeatFluxUnits.WattPerSquareMeter) -> string:
        """
        Format the HeatFlux to string.
        Note! the default format for HeatFlux is WattPerSquareMeter.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == HeatFluxUnits.WattPerSquareMeter:
            return f"""{self.watts_per_square_meter} W/m²"""
        
        if unit == HeatFluxUnits.WattPerSquareInch:
            return f"""{self.watts_per_square_inch} W/in²"""
        
        if unit == HeatFluxUnits.WattPerSquareFoot:
            return f"""{self.watts_per_square_foot} W/ft²"""
        
        if unit == HeatFluxUnits.BtuPerSecondSquareInch:
            return f"""{self.btus_per_second_square_inch} BTU/s·in²"""
        
        if unit == HeatFluxUnits.BtuPerSecondSquareFoot:
            return f"""{self.btus_per_second_square_foot} BTU/s·ft²"""
        
        if unit == HeatFluxUnits.BtuPerMinuteSquareFoot:
            return f"""{self.btus_per_minute_square_foot} BTU/min·ft²"""
        
        if unit == HeatFluxUnits.BtuPerHourSquareFoot:
            return f"""{self.btus_per_hour_square_foot} BTU/h·ft²"""
        
        if unit == HeatFluxUnits.CaloriePerSecondSquareCentimeter:
            return f"""{self.calories_per_second_square_centimeter} cal/s·cm²"""
        
        if unit == HeatFluxUnits.KilocaloriePerHourSquareMeter:
            return f"""{self.kilocalories_per_hour_square_meter} kcal/h·m²"""
        
        if unit == HeatFluxUnits.PoundForcePerFootSecond:
            return f"""{self.pounds_force_per_foot_second} lbf/(ft·s)"""
        
        if unit == HeatFluxUnits.PoundPerSecondCubed:
            return f"""{self.pounds_per_second_cubed} lb/s³"""
        
        if unit == HeatFluxUnits.NanoWattPerSquareMeter:
            return f"""{self.nano_watts_per_square_meter} """
        
        if unit == HeatFluxUnits.MicroWattPerSquareMeter:
            return f"""{self.micro_watts_per_square_meter} """
        
        if unit == HeatFluxUnits.MilliWattPerSquareMeter:
            return f"""{self.milli_watts_per_square_meter} """
        
        if unit == HeatFluxUnits.CentiWattPerSquareMeter:
            return f"""{self.centi_watts_per_square_meter} """
        
        if unit == HeatFluxUnits.DeciWattPerSquareMeter:
            return f"""{self.deci_watts_per_square_meter} """
        
        if unit == HeatFluxUnits.KiloWattPerSquareMeter:
            return f"""{self.kilo_watts_per_square_meter} """
        
        if unit == HeatFluxUnits.KiloCaloriePerSecondSquareCentimeter:
            return f"""{self.kilo_calories_per_second_square_centimeter} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: HeatFluxUnits = HeatFluxUnits.WattPerSquareMeter) -> string:
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
        
        if unit_abbreviation == HeatFluxUnits.NanoWattPerSquareMeter:
            return """"""
        
        if unit_abbreviation == HeatFluxUnits.MicroWattPerSquareMeter:
            return """"""
        
        if unit_abbreviation == HeatFluxUnits.MilliWattPerSquareMeter:
            return """"""
        
        if unit_abbreviation == HeatFluxUnits.CentiWattPerSquareMeter:
            return """"""
        
        if unit_abbreviation == HeatFluxUnits.DeciWattPerSquareMeter:
            return """"""
        
        if unit_abbreviation == HeatFluxUnits.KiloWattPerSquareMeter:
            return """"""
        
        if unit_abbreviation == HeatFluxUnits.KiloCaloriePerSecondSquareCentimeter:
            return """"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, HeatFlux):
            raise TypeError("unsupported operand type(s) for +: 'HeatFlux' and '{}'".format(type(other).__name__))
        return HeatFlux(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, HeatFlux):
            raise TypeError("unsupported operand type(s) for *: 'HeatFlux' and '{}'".format(type(other).__name__))
        return HeatFlux(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, HeatFlux):
            raise TypeError("unsupported operand type(s) for -: 'HeatFlux' and '{}'".format(type(other).__name__))
        return HeatFlux(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, HeatFlux):
            raise TypeError("unsupported operand type(s) for /: 'HeatFlux' and '{}'".format(type(other).__name__))
        return HeatFlux(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, HeatFlux):
            raise TypeError("unsupported operand type(s) for %: 'HeatFlux' and '{}'".format(type(other).__name__))
        return HeatFlux(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, HeatFlux):
            raise TypeError("unsupported operand type(s) for **: 'HeatFlux' and '{}'".format(type(other).__name__))
        return HeatFlux(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, HeatFlux):
            raise TypeError("unsupported operand type(s) for ==: 'HeatFlux' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, HeatFlux):
            raise TypeError("unsupported operand type(s) for <: 'HeatFlux' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, HeatFlux):
            raise TypeError("unsupported operand type(s) for >: 'HeatFlux' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, HeatFlux):
            raise TypeError("unsupported operand type(s) for <=: 'HeatFlux' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, HeatFlux):
            raise TypeError("unsupported operand type(s) for >=: 'HeatFlux' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value
from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



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
        
        NanowattPerSquareMeter = 'nanowatt_per_square_meter'
        """
            
        """
        
        MicrowattPerSquareMeter = 'microwatt_per_square_meter'
        """
            
        """
        
        MilliwattPerSquareMeter = 'milliwatt_per_square_meter'
        """
            
        """
        
        CentiwattPerSquareMeter = 'centiwatt_per_square_meter'
        """
            
        """
        
        DeciwattPerSquareMeter = 'deciwatt_per_square_meter'
        """
            
        """
        
        KilowattPerSquareMeter = 'kilowatt_per_square_meter'
        """
            
        """
        
        KilocaloriePerSecondSquareCentimeter = 'kilocalorie_per_second_square_centimeter'
        """
            
        """
        

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

    
    def to_string(self, unit: HeatFluxUnits = HeatFluxUnits.WattPerSquareMeter) -> str:
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
        
        if unit == HeatFluxUnits.NanowattPerSquareMeter:
            return f"""{self.nanowatts_per_square_meter} nW/m²"""
        
        if unit == HeatFluxUnits.MicrowattPerSquareMeter:
            return f"""{self.microwatts_per_square_meter} μW/m²"""
        
        if unit == HeatFluxUnits.MilliwattPerSquareMeter:
            return f"""{self.milliwatts_per_square_meter} mW/m²"""
        
        if unit == HeatFluxUnits.CentiwattPerSquareMeter:
            return f"""{self.centiwatts_per_square_meter} cW/m²"""
        
        if unit == HeatFluxUnits.DeciwattPerSquareMeter:
            return f"""{self.deciwatts_per_square_meter} dW/m²"""
        
        if unit == HeatFluxUnits.KilowattPerSquareMeter:
            return f"""{self.kilowatts_per_square_meter} kW/m²"""
        
        if unit == HeatFluxUnits.KilocaloriePerSecondSquareCentimeter:
            return f"""{self.kilocalories_per_second_square_centimeter} kcal/s·cm²"""
        
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
        
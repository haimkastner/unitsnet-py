from enum import Enum
import math
import string


class LinearPowerDensityUnits(Enum):
        """
            LinearPowerDensityUnits enumeration
        """
        
        WattPerMeter = 'watt_per_meter'
        """
            
        """
        
        WattPerCentimeter = 'watt_per_centimeter'
        """
            
        """
        
        WattPerMillimeter = 'watt_per_millimeter'
        """
            
        """
        
        WattPerInch = 'watt_per_inch'
        """
            
        """
        
        WattPerFoot = 'watt_per_foot'
        """
            
        """
        
        MilliWattPerMeter = 'milli_watt_per_meter'
        """
            
        """
        
        KiloWattPerMeter = 'kilo_watt_per_meter'
        """
            
        """
        
        MegaWattPerMeter = 'mega_watt_per_meter'
        """
            
        """
        
        GigaWattPerMeter = 'giga_watt_per_meter'
        """
            
        """
        
        MilliWattPerCentimeter = 'milli_watt_per_centimeter'
        """
            
        """
        
        KiloWattPerCentimeter = 'kilo_watt_per_centimeter'
        """
            
        """
        
        MegaWattPerCentimeter = 'mega_watt_per_centimeter'
        """
            
        """
        
        GigaWattPerCentimeter = 'giga_watt_per_centimeter'
        """
            
        """
        
        MilliWattPerMillimeter = 'milli_watt_per_millimeter'
        """
            
        """
        
        KiloWattPerMillimeter = 'kilo_watt_per_millimeter'
        """
            
        """
        
        MegaWattPerMillimeter = 'mega_watt_per_millimeter'
        """
            
        """
        
        GigaWattPerMillimeter = 'giga_watt_per_millimeter'
        """
            
        """
        
        MilliWattPerInch = 'milli_watt_per_inch'
        """
            
        """
        
        KiloWattPerInch = 'kilo_watt_per_inch'
        """
            
        """
        
        MegaWattPerInch = 'mega_watt_per_inch'
        """
            
        """
        
        GigaWattPerInch = 'giga_watt_per_inch'
        """
            
        """
        
        MilliWattPerFoot = 'milli_watt_per_foot'
        """
            
        """
        
        KiloWattPerFoot = 'kilo_watt_per_foot'
        """
            
        """
        
        MegaWattPerFoot = 'mega_watt_per_foot'
        """
            
        """
        
        GigaWattPerFoot = 'giga_watt_per_foot'
        """
            
        """
        

class LinearPowerDensity:
    """
    The Linear Power Density of a substance is its power per unit length.  The term linear density is most often used when describing the characteristics of one-dimensional objects, although linear density can also be used to describe the density of a three-dimensional quantity along one particular dimension.

    Args:
        value (float): The value.
        from_unit (LinearPowerDensityUnits): The LinearPowerDensity unit to create from, The default unit is WattPerMeter
    """
    def __init__(self, value: float, from_unit: LinearPowerDensityUnits = LinearPowerDensityUnits.WattPerMeter):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__watts_per_meter = None
        
        self.__watts_per_centimeter = None
        
        self.__watts_per_millimeter = None
        
        self.__watts_per_inch = None
        
        self.__watts_per_foot = None
        
        self.__milli_watts_per_meter = None
        
        self.__kilo_watts_per_meter = None
        
        self.__mega_watts_per_meter = None
        
        self.__giga_watts_per_meter = None
        
        self.__milli_watts_per_centimeter = None
        
        self.__kilo_watts_per_centimeter = None
        
        self.__mega_watts_per_centimeter = None
        
        self.__giga_watts_per_centimeter = None
        
        self.__milli_watts_per_millimeter = None
        
        self.__kilo_watts_per_millimeter = None
        
        self.__mega_watts_per_millimeter = None
        
        self.__giga_watts_per_millimeter = None
        
        self.__milli_watts_per_inch = None
        
        self.__kilo_watts_per_inch = None
        
        self.__mega_watts_per_inch = None
        
        self.__giga_watts_per_inch = None
        
        self.__milli_watts_per_foot = None
        
        self.__kilo_watts_per_foot = None
        
        self.__mega_watts_per_foot = None
        
        self.__giga_watts_per_foot = None
        

    def __convert_from_base(self, from_unit: LinearPowerDensityUnits) -> float:
        value = self.__value
        
        if from_unit == LinearPowerDensityUnits.WattPerMeter:
            return (value)
        
        if from_unit == LinearPowerDensityUnits.WattPerCentimeter:
            return (value / 1e2)
        
        if from_unit == LinearPowerDensityUnits.WattPerMillimeter:
            return (value / 1e3)
        
        if from_unit == LinearPowerDensityUnits.WattPerInch:
            return (value / 39.37007874)
        
        if from_unit == LinearPowerDensityUnits.WattPerFoot:
            return (value / 3.280839895)
        
        if from_unit == LinearPowerDensityUnits.MilliWattPerMeter:
            return ((value) / 0.001)
        
        if from_unit == LinearPowerDensityUnits.KiloWattPerMeter:
            return ((value) / 1000.0)
        
        if from_unit == LinearPowerDensityUnits.MegaWattPerMeter:
            return ((value) / 1000000.0)
        
        if from_unit == LinearPowerDensityUnits.GigaWattPerMeter:
            return ((value) / 1000000000.0)
        
        if from_unit == LinearPowerDensityUnits.MilliWattPerCentimeter:
            return ((value / 1e2) / 0.001)
        
        if from_unit == LinearPowerDensityUnits.KiloWattPerCentimeter:
            return ((value / 1e2) / 1000.0)
        
        if from_unit == LinearPowerDensityUnits.MegaWattPerCentimeter:
            return ((value / 1e2) / 1000000.0)
        
        if from_unit == LinearPowerDensityUnits.GigaWattPerCentimeter:
            return ((value / 1e2) / 1000000000.0)
        
        if from_unit == LinearPowerDensityUnits.MilliWattPerMillimeter:
            return ((value / 1e3) / 0.001)
        
        if from_unit == LinearPowerDensityUnits.KiloWattPerMillimeter:
            return ((value / 1e3) / 1000.0)
        
        if from_unit == LinearPowerDensityUnits.MegaWattPerMillimeter:
            return ((value / 1e3) / 1000000.0)
        
        if from_unit == LinearPowerDensityUnits.GigaWattPerMillimeter:
            return ((value / 1e3) / 1000000000.0)
        
        if from_unit == LinearPowerDensityUnits.MilliWattPerInch:
            return ((value / 39.37007874) / 0.001)
        
        if from_unit == LinearPowerDensityUnits.KiloWattPerInch:
            return ((value / 39.37007874) / 1000.0)
        
        if from_unit == LinearPowerDensityUnits.MegaWattPerInch:
            return ((value / 39.37007874) / 1000000.0)
        
        if from_unit == LinearPowerDensityUnits.GigaWattPerInch:
            return ((value / 39.37007874) / 1000000000.0)
        
        if from_unit == LinearPowerDensityUnits.MilliWattPerFoot:
            return ((value / 3.280839895) / 0.001)
        
        if from_unit == LinearPowerDensityUnits.KiloWattPerFoot:
            return ((value / 3.280839895) / 1000.0)
        
        if from_unit == LinearPowerDensityUnits.MegaWattPerFoot:
            return ((value / 3.280839895) / 1000000.0)
        
        if from_unit == LinearPowerDensityUnits.GigaWattPerFoot:
            return ((value / 3.280839895) / 1000000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: LinearPowerDensityUnits) -> float:
        
        if to_unit == LinearPowerDensityUnits.WattPerMeter:
            return (value)
        
        if to_unit == LinearPowerDensityUnits.WattPerCentimeter:
            return (value * 1e2)
        
        if to_unit == LinearPowerDensityUnits.WattPerMillimeter:
            return (value * 1e3)
        
        if to_unit == LinearPowerDensityUnits.WattPerInch:
            return (value * 39.37007874)
        
        if to_unit == LinearPowerDensityUnits.WattPerFoot:
            return (value * 3.280839895)
        
        if to_unit == LinearPowerDensityUnits.MilliWattPerMeter:
            return ((value) * 0.001)
        
        if to_unit == LinearPowerDensityUnits.KiloWattPerMeter:
            return ((value) * 1000.0)
        
        if to_unit == LinearPowerDensityUnits.MegaWattPerMeter:
            return ((value) * 1000000.0)
        
        if to_unit == LinearPowerDensityUnits.GigaWattPerMeter:
            return ((value) * 1000000000.0)
        
        if to_unit == LinearPowerDensityUnits.MilliWattPerCentimeter:
            return ((value * 1e2) * 0.001)
        
        if to_unit == LinearPowerDensityUnits.KiloWattPerCentimeter:
            return ((value * 1e2) * 1000.0)
        
        if to_unit == LinearPowerDensityUnits.MegaWattPerCentimeter:
            return ((value * 1e2) * 1000000.0)
        
        if to_unit == LinearPowerDensityUnits.GigaWattPerCentimeter:
            return ((value * 1e2) * 1000000000.0)
        
        if to_unit == LinearPowerDensityUnits.MilliWattPerMillimeter:
            return ((value * 1e3) * 0.001)
        
        if to_unit == LinearPowerDensityUnits.KiloWattPerMillimeter:
            return ((value * 1e3) * 1000.0)
        
        if to_unit == LinearPowerDensityUnits.MegaWattPerMillimeter:
            return ((value * 1e3) * 1000000.0)
        
        if to_unit == LinearPowerDensityUnits.GigaWattPerMillimeter:
            return ((value * 1e3) * 1000000000.0)
        
        if to_unit == LinearPowerDensityUnits.MilliWattPerInch:
            return ((value * 39.37007874) * 0.001)
        
        if to_unit == LinearPowerDensityUnits.KiloWattPerInch:
            return ((value * 39.37007874) * 1000.0)
        
        if to_unit == LinearPowerDensityUnits.MegaWattPerInch:
            return ((value * 39.37007874) * 1000000.0)
        
        if to_unit == LinearPowerDensityUnits.GigaWattPerInch:
            return ((value * 39.37007874) * 1000000000.0)
        
        if to_unit == LinearPowerDensityUnits.MilliWattPerFoot:
            return ((value * 3.280839895) * 0.001)
        
        if to_unit == LinearPowerDensityUnits.KiloWattPerFoot:
            return ((value * 3.280839895) * 1000.0)
        
        if to_unit == LinearPowerDensityUnits.MegaWattPerFoot:
            return ((value * 3.280839895) * 1000000.0)
        
        if to_unit == LinearPowerDensityUnits.GigaWattPerFoot:
            return ((value * 3.280839895) * 1000000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
    @staticmethod
    def from_watts_per_meter(watts_per_meter: float):
        """
        Create a new instance of LinearPowerDensity from a value in watts_per_meter.

        

        :param meters: The LinearPowerDensity value in watts_per_meter.
        :type watts_per_meter: float
        :return: A new instance of LinearPowerDensity.
        :rtype: LinearPowerDensity
        """
        return LinearPowerDensity(watts_per_meter, LinearPowerDensityUnits.WattPerMeter)

    
    @staticmethod
    def from_watts_per_centimeter(watts_per_centimeter: float):
        """
        Create a new instance of LinearPowerDensity from a value in watts_per_centimeter.

        

        :param meters: The LinearPowerDensity value in watts_per_centimeter.
        :type watts_per_centimeter: float
        :return: A new instance of LinearPowerDensity.
        :rtype: LinearPowerDensity
        """
        return LinearPowerDensity(watts_per_centimeter, LinearPowerDensityUnits.WattPerCentimeter)

    
    @staticmethod
    def from_watts_per_millimeter(watts_per_millimeter: float):
        """
        Create a new instance of LinearPowerDensity from a value in watts_per_millimeter.

        

        :param meters: The LinearPowerDensity value in watts_per_millimeter.
        :type watts_per_millimeter: float
        :return: A new instance of LinearPowerDensity.
        :rtype: LinearPowerDensity
        """
        return LinearPowerDensity(watts_per_millimeter, LinearPowerDensityUnits.WattPerMillimeter)

    
    @staticmethod
    def from_watts_per_inch(watts_per_inch: float):
        """
        Create a new instance of LinearPowerDensity from a value in watts_per_inch.

        

        :param meters: The LinearPowerDensity value in watts_per_inch.
        :type watts_per_inch: float
        :return: A new instance of LinearPowerDensity.
        :rtype: LinearPowerDensity
        """
        return LinearPowerDensity(watts_per_inch, LinearPowerDensityUnits.WattPerInch)

    
    @staticmethod
    def from_watts_per_foot(watts_per_foot: float):
        """
        Create a new instance of LinearPowerDensity from a value in watts_per_foot.

        

        :param meters: The LinearPowerDensity value in watts_per_foot.
        :type watts_per_foot: float
        :return: A new instance of LinearPowerDensity.
        :rtype: LinearPowerDensity
        """
        return LinearPowerDensity(watts_per_foot, LinearPowerDensityUnits.WattPerFoot)

    
    @staticmethod
    def from_milli_watts_per_meter(milli_watts_per_meter: float):
        """
        Create a new instance of LinearPowerDensity from a value in milli_watts_per_meter.

        

        :param meters: The LinearPowerDensity value in milli_watts_per_meter.
        :type milli_watts_per_meter: float
        :return: A new instance of LinearPowerDensity.
        :rtype: LinearPowerDensity
        """
        return LinearPowerDensity(milli_watts_per_meter, LinearPowerDensityUnits.MilliWattPerMeter)

    
    @staticmethod
    def from_kilo_watts_per_meter(kilo_watts_per_meter: float):
        """
        Create a new instance of LinearPowerDensity from a value in kilo_watts_per_meter.

        

        :param meters: The LinearPowerDensity value in kilo_watts_per_meter.
        :type kilo_watts_per_meter: float
        :return: A new instance of LinearPowerDensity.
        :rtype: LinearPowerDensity
        """
        return LinearPowerDensity(kilo_watts_per_meter, LinearPowerDensityUnits.KiloWattPerMeter)

    
    @staticmethod
    def from_mega_watts_per_meter(mega_watts_per_meter: float):
        """
        Create a new instance of LinearPowerDensity from a value in mega_watts_per_meter.

        

        :param meters: The LinearPowerDensity value in mega_watts_per_meter.
        :type mega_watts_per_meter: float
        :return: A new instance of LinearPowerDensity.
        :rtype: LinearPowerDensity
        """
        return LinearPowerDensity(mega_watts_per_meter, LinearPowerDensityUnits.MegaWattPerMeter)

    
    @staticmethod
    def from_giga_watts_per_meter(giga_watts_per_meter: float):
        """
        Create a new instance of LinearPowerDensity from a value in giga_watts_per_meter.

        

        :param meters: The LinearPowerDensity value in giga_watts_per_meter.
        :type giga_watts_per_meter: float
        :return: A new instance of LinearPowerDensity.
        :rtype: LinearPowerDensity
        """
        return LinearPowerDensity(giga_watts_per_meter, LinearPowerDensityUnits.GigaWattPerMeter)

    
    @staticmethod
    def from_milli_watts_per_centimeter(milli_watts_per_centimeter: float):
        """
        Create a new instance of LinearPowerDensity from a value in milli_watts_per_centimeter.

        

        :param meters: The LinearPowerDensity value in milli_watts_per_centimeter.
        :type milli_watts_per_centimeter: float
        :return: A new instance of LinearPowerDensity.
        :rtype: LinearPowerDensity
        """
        return LinearPowerDensity(milli_watts_per_centimeter, LinearPowerDensityUnits.MilliWattPerCentimeter)

    
    @staticmethod
    def from_kilo_watts_per_centimeter(kilo_watts_per_centimeter: float):
        """
        Create a new instance of LinearPowerDensity from a value in kilo_watts_per_centimeter.

        

        :param meters: The LinearPowerDensity value in kilo_watts_per_centimeter.
        :type kilo_watts_per_centimeter: float
        :return: A new instance of LinearPowerDensity.
        :rtype: LinearPowerDensity
        """
        return LinearPowerDensity(kilo_watts_per_centimeter, LinearPowerDensityUnits.KiloWattPerCentimeter)

    
    @staticmethod
    def from_mega_watts_per_centimeter(mega_watts_per_centimeter: float):
        """
        Create a new instance of LinearPowerDensity from a value in mega_watts_per_centimeter.

        

        :param meters: The LinearPowerDensity value in mega_watts_per_centimeter.
        :type mega_watts_per_centimeter: float
        :return: A new instance of LinearPowerDensity.
        :rtype: LinearPowerDensity
        """
        return LinearPowerDensity(mega_watts_per_centimeter, LinearPowerDensityUnits.MegaWattPerCentimeter)

    
    @staticmethod
    def from_giga_watts_per_centimeter(giga_watts_per_centimeter: float):
        """
        Create a new instance of LinearPowerDensity from a value in giga_watts_per_centimeter.

        

        :param meters: The LinearPowerDensity value in giga_watts_per_centimeter.
        :type giga_watts_per_centimeter: float
        :return: A new instance of LinearPowerDensity.
        :rtype: LinearPowerDensity
        """
        return LinearPowerDensity(giga_watts_per_centimeter, LinearPowerDensityUnits.GigaWattPerCentimeter)

    
    @staticmethod
    def from_milli_watts_per_millimeter(milli_watts_per_millimeter: float):
        """
        Create a new instance of LinearPowerDensity from a value in milli_watts_per_millimeter.

        

        :param meters: The LinearPowerDensity value in milli_watts_per_millimeter.
        :type milli_watts_per_millimeter: float
        :return: A new instance of LinearPowerDensity.
        :rtype: LinearPowerDensity
        """
        return LinearPowerDensity(milli_watts_per_millimeter, LinearPowerDensityUnits.MilliWattPerMillimeter)

    
    @staticmethod
    def from_kilo_watts_per_millimeter(kilo_watts_per_millimeter: float):
        """
        Create a new instance of LinearPowerDensity from a value in kilo_watts_per_millimeter.

        

        :param meters: The LinearPowerDensity value in kilo_watts_per_millimeter.
        :type kilo_watts_per_millimeter: float
        :return: A new instance of LinearPowerDensity.
        :rtype: LinearPowerDensity
        """
        return LinearPowerDensity(kilo_watts_per_millimeter, LinearPowerDensityUnits.KiloWattPerMillimeter)

    
    @staticmethod
    def from_mega_watts_per_millimeter(mega_watts_per_millimeter: float):
        """
        Create a new instance of LinearPowerDensity from a value in mega_watts_per_millimeter.

        

        :param meters: The LinearPowerDensity value in mega_watts_per_millimeter.
        :type mega_watts_per_millimeter: float
        :return: A new instance of LinearPowerDensity.
        :rtype: LinearPowerDensity
        """
        return LinearPowerDensity(mega_watts_per_millimeter, LinearPowerDensityUnits.MegaWattPerMillimeter)

    
    @staticmethod
    def from_giga_watts_per_millimeter(giga_watts_per_millimeter: float):
        """
        Create a new instance of LinearPowerDensity from a value in giga_watts_per_millimeter.

        

        :param meters: The LinearPowerDensity value in giga_watts_per_millimeter.
        :type giga_watts_per_millimeter: float
        :return: A new instance of LinearPowerDensity.
        :rtype: LinearPowerDensity
        """
        return LinearPowerDensity(giga_watts_per_millimeter, LinearPowerDensityUnits.GigaWattPerMillimeter)

    
    @staticmethod
    def from_milli_watts_per_inch(milli_watts_per_inch: float):
        """
        Create a new instance of LinearPowerDensity from a value in milli_watts_per_inch.

        

        :param meters: The LinearPowerDensity value in milli_watts_per_inch.
        :type milli_watts_per_inch: float
        :return: A new instance of LinearPowerDensity.
        :rtype: LinearPowerDensity
        """
        return LinearPowerDensity(milli_watts_per_inch, LinearPowerDensityUnits.MilliWattPerInch)

    
    @staticmethod
    def from_kilo_watts_per_inch(kilo_watts_per_inch: float):
        """
        Create a new instance of LinearPowerDensity from a value in kilo_watts_per_inch.

        

        :param meters: The LinearPowerDensity value in kilo_watts_per_inch.
        :type kilo_watts_per_inch: float
        :return: A new instance of LinearPowerDensity.
        :rtype: LinearPowerDensity
        """
        return LinearPowerDensity(kilo_watts_per_inch, LinearPowerDensityUnits.KiloWattPerInch)

    
    @staticmethod
    def from_mega_watts_per_inch(mega_watts_per_inch: float):
        """
        Create a new instance of LinearPowerDensity from a value in mega_watts_per_inch.

        

        :param meters: The LinearPowerDensity value in mega_watts_per_inch.
        :type mega_watts_per_inch: float
        :return: A new instance of LinearPowerDensity.
        :rtype: LinearPowerDensity
        """
        return LinearPowerDensity(mega_watts_per_inch, LinearPowerDensityUnits.MegaWattPerInch)

    
    @staticmethod
    def from_giga_watts_per_inch(giga_watts_per_inch: float):
        """
        Create a new instance of LinearPowerDensity from a value in giga_watts_per_inch.

        

        :param meters: The LinearPowerDensity value in giga_watts_per_inch.
        :type giga_watts_per_inch: float
        :return: A new instance of LinearPowerDensity.
        :rtype: LinearPowerDensity
        """
        return LinearPowerDensity(giga_watts_per_inch, LinearPowerDensityUnits.GigaWattPerInch)

    
    @staticmethod
    def from_milli_watts_per_foot(milli_watts_per_foot: float):
        """
        Create a new instance of LinearPowerDensity from a value in milli_watts_per_foot.

        

        :param meters: The LinearPowerDensity value in milli_watts_per_foot.
        :type milli_watts_per_foot: float
        :return: A new instance of LinearPowerDensity.
        :rtype: LinearPowerDensity
        """
        return LinearPowerDensity(milli_watts_per_foot, LinearPowerDensityUnits.MilliWattPerFoot)

    
    @staticmethod
    def from_kilo_watts_per_foot(kilo_watts_per_foot: float):
        """
        Create a new instance of LinearPowerDensity from a value in kilo_watts_per_foot.

        

        :param meters: The LinearPowerDensity value in kilo_watts_per_foot.
        :type kilo_watts_per_foot: float
        :return: A new instance of LinearPowerDensity.
        :rtype: LinearPowerDensity
        """
        return LinearPowerDensity(kilo_watts_per_foot, LinearPowerDensityUnits.KiloWattPerFoot)

    
    @staticmethod
    def from_mega_watts_per_foot(mega_watts_per_foot: float):
        """
        Create a new instance of LinearPowerDensity from a value in mega_watts_per_foot.

        

        :param meters: The LinearPowerDensity value in mega_watts_per_foot.
        :type mega_watts_per_foot: float
        :return: A new instance of LinearPowerDensity.
        :rtype: LinearPowerDensity
        """
        return LinearPowerDensity(mega_watts_per_foot, LinearPowerDensityUnits.MegaWattPerFoot)

    
    @staticmethod
    def from_giga_watts_per_foot(giga_watts_per_foot: float):
        """
        Create a new instance of LinearPowerDensity from a value in giga_watts_per_foot.

        

        :param meters: The LinearPowerDensity value in giga_watts_per_foot.
        :type giga_watts_per_foot: float
        :return: A new instance of LinearPowerDensity.
        :rtype: LinearPowerDensity
        """
        return LinearPowerDensity(giga_watts_per_foot, LinearPowerDensityUnits.GigaWattPerFoot)

    
    @property
    def watts_per_meter(self) -> float:
        """
        
        """
        if self.__watts_per_meter != None:
            return self.__watts_per_meter
        self.__watts_per_meter = self.__convert_from_base(LinearPowerDensityUnits.WattPerMeter)
        return self.__watts_per_meter

    
    @property
    def watts_per_centimeter(self) -> float:
        """
        
        """
        if self.__watts_per_centimeter != None:
            return self.__watts_per_centimeter
        self.__watts_per_centimeter = self.__convert_from_base(LinearPowerDensityUnits.WattPerCentimeter)
        return self.__watts_per_centimeter

    
    @property
    def watts_per_millimeter(self) -> float:
        """
        
        """
        if self.__watts_per_millimeter != None:
            return self.__watts_per_millimeter
        self.__watts_per_millimeter = self.__convert_from_base(LinearPowerDensityUnits.WattPerMillimeter)
        return self.__watts_per_millimeter

    
    @property
    def watts_per_inch(self) -> float:
        """
        
        """
        if self.__watts_per_inch != None:
            return self.__watts_per_inch
        self.__watts_per_inch = self.__convert_from_base(LinearPowerDensityUnits.WattPerInch)
        return self.__watts_per_inch

    
    @property
    def watts_per_foot(self) -> float:
        """
        
        """
        if self.__watts_per_foot != None:
            return self.__watts_per_foot
        self.__watts_per_foot = self.__convert_from_base(LinearPowerDensityUnits.WattPerFoot)
        return self.__watts_per_foot

    
    @property
    def milli_watts_per_meter(self) -> float:
        """
        
        """
        if self.__milli_watts_per_meter != None:
            return self.__milli_watts_per_meter
        self.__milli_watts_per_meter = self.__convert_from_base(LinearPowerDensityUnits.MilliWattPerMeter)
        return self.__milli_watts_per_meter

    
    @property
    def kilo_watts_per_meter(self) -> float:
        """
        
        """
        if self.__kilo_watts_per_meter != None:
            return self.__kilo_watts_per_meter
        self.__kilo_watts_per_meter = self.__convert_from_base(LinearPowerDensityUnits.KiloWattPerMeter)
        return self.__kilo_watts_per_meter

    
    @property
    def mega_watts_per_meter(self) -> float:
        """
        
        """
        if self.__mega_watts_per_meter != None:
            return self.__mega_watts_per_meter
        self.__mega_watts_per_meter = self.__convert_from_base(LinearPowerDensityUnits.MegaWattPerMeter)
        return self.__mega_watts_per_meter

    
    @property
    def giga_watts_per_meter(self) -> float:
        """
        
        """
        if self.__giga_watts_per_meter != None:
            return self.__giga_watts_per_meter
        self.__giga_watts_per_meter = self.__convert_from_base(LinearPowerDensityUnits.GigaWattPerMeter)
        return self.__giga_watts_per_meter

    
    @property
    def milli_watts_per_centimeter(self) -> float:
        """
        
        """
        if self.__milli_watts_per_centimeter != None:
            return self.__milli_watts_per_centimeter
        self.__milli_watts_per_centimeter = self.__convert_from_base(LinearPowerDensityUnits.MilliWattPerCentimeter)
        return self.__milli_watts_per_centimeter

    
    @property
    def kilo_watts_per_centimeter(self) -> float:
        """
        
        """
        if self.__kilo_watts_per_centimeter != None:
            return self.__kilo_watts_per_centimeter
        self.__kilo_watts_per_centimeter = self.__convert_from_base(LinearPowerDensityUnits.KiloWattPerCentimeter)
        return self.__kilo_watts_per_centimeter

    
    @property
    def mega_watts_per_centimeter(self) -> float:
        """
        
        """
        if self.__mega_watts_per_centimeter != None:
            return self.__mega_watts_per_centimeter
        self.__mega_watts_per_centimeter = self.__convert_from_base(LinearPowerDensityUnits.MegaWattPerCentimeter)
        return self.__mega_watts_per_centimeter

    
    @property
    def giga_watts_per_centimeter(self) -> float:
        """
        
        """
        if self.__giga_watts_per_centimeter != None:
            return self.__giga_watts_per_centimeter
        self.__giga_watts_per_centimeter = self.__convert_from_base(LinearPowerDensityUnits.GigaWattPerCentimeter)
        return self.__giga_watts_per_centimeter

    
    @property
    def milli_watts_per_millimeter(self) -> float:
        """
        
        """
        if self.__milli_watts_per_millimeter != None:
            return self.__milli_watts_per_millimeter
        self.__milli_watts_per_millimeter = self.__convert_from_base(LinearPowerDensityUnits.MilliWattPerMillimeter)
        return self.__milli_watts_per_millimeter

    
    @property
    def kilo_watts_per_millimeter(self) -> float:
        """
        
        """
        if self.__kilo_watts_per_millimeter != None:
            return self.__kilo_watts_per_millimeter
        self.__kilo_watts_per_millimeter = self.__convert_from_base(LinearPowerDensityUnits.KiloWattPerMillimeter)
        return self.__kilo_watts_per_millimeter

    
    @property
    def mega_watts_per_millimeter(self) -> float:
        """
        
        """
        if self.__mega_watts_per_millimeter != None:
            return self.__mega_watts_per_millimeter
        self.__mega_watts_per_millimeter = self.__convert_from_base(LinearPowerDensityUnits.MegaWattPerMillimeter)
        return self.__mega_watts_per_millimeter

    
    @property
    def giga_watts_per_millimeter(self) -> float:
        """
        
        """
        if self.__giga_watts_per_millimeter != None:
            return self.__giga_watts_per_millimeter
        self.__giga_watts_per_millimeter = self.__convert_from_base(LinearPowerDensityUnits.GigaWattPerMillimeter)
        return self.__giga_watts_per_millimeter

    
    @property
    def milli_watts_per_inch(self) -> float:
        """
        
        """
        if self.__milli_watts_per_inch != None:
            return self.__milli_watts_per_inch
        self.__milli_watts_per_inch = self.__convert_from_base(LinearPowerDensityUnits.MilliWattPerInch)
        return self.__milli_watts_per_inch

    
    @property
    def kilo_watts_per_inch(self) -> float:
        """
        
        """
        if self.__kilo_watts_per_inch != None:
            return self.__kilo_watts_per_inch
        self.__kilo_watts_per_inch = self.__convert_from_base(LinearPowerDensityUnits.KiloWattPerInch)
        return self.__kilo_watts_per_inch

    
    @property
    def mega_watts_per_inch(self) -> float:
        """
        
        """
        if self.__mega_watts_per_inch != None:
            return self.__mega_watts_per_inch
        self.__mega_watts_per_inch = self.__convert_from_base(LinearPowerDensityUnits.MegaWattPerInch)
        return self.__mega_watts_per_inch

    
    @property
    def giga_watts_per_inch(self) -> float:
        """
        
        """
        if self.__giga_watts_per_inch != None:
            return self.__giga_watts_per_inch
        self.__giga_watts_per_inch = self.__convert_from_base(LinearPowerDensityUnits.GigaWattPerInch)
        return self.__giga_watts_per_inch

    
    @property
    def milli_watts_per_foot(self) -> float:
        """
        
        """
        if self.__milli_watts_per_foot != None:
            return self.__milli_watts_per_foot
        self.__milli_watts_per_foot = self.__convert_from_base(LinearPowerDensityUnits.MilliWattPerFoot)
        return self.__milli_watts_per_foot

    
    @property
    def kilo_watts_per_foot(self) -> float:
        """
        
        """
        if self.__kilo_watts_per_foot != None:
            return self.__kilo_watts_per_foot
        self.__kilo_watts_per_foot = self.__convert_from_base(LinearPowerDensityUnits.KiloWattPerFoot)
        return self.__kilo_watts_per_foot

    
    @property
    def mega_watts_per_foot(self) -> float:
        """
        
        """
        if self.__mega_watts_per_foot != None:
            return self.__mega_watts_per_foot
        self.__mega_watts_per_foot = self.__convert_from_base(LinearPowerDensityUnits.MegaWattPerFoot)
        return self.__mega_watts_per_foot

    
    @property
    def giga_watts_per_foot(self) -> float:
        """
        
        """
        if self.__giga_watts_per_foot != None:
            return self.__giga_watts_per_foot
        self.__giga_watts_per_foot = self.__convert_from_base(LinearPowerDensityUnits.GigaWattPerFoot)
        return self.__giga_watts_per_foot

    
    def to_string(self, unit: LinearPowerDensityUnits = LinearPowerDensityUnits.WattPerMeter) -> string:
        """
        Format the LinearPowerDensity to string.
        Note! the default format for LinearPowerDensity is WattPerMeter.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == LinearPowerDensityUnits.WattPerMeter:
            return f"""{self.watts_per_meter} W/m"""
        
        if unit == LinearPowerDensityUnits.WattPerCentimeter:
            return f"""{self.watts_per_centimeter} W/cm"""
        
        if unit == LinearPowerDensityUnits.WattPerMillimeter:
            return f"""{self.watts_per_millimeter} W/mm"""
        
        if unit == LinearPowerDensityUnits.WattPerInch:
            return f"""{self.watts_per_inch} W/in"""
        
        if unit == LinearPowerDensityUnits.WattPerFoot:
            return f"""{self.watts_per_foot} W/ft"""
        
        if unit == LinearPowerDensityUnits.MilliWattPerMeter:
            return f"""{self.milli_watts_per_meter} """
        
        if unit == LinearPowerDensityUnits.KiloWattPerMeter:
            return f"""{self.kilo_watts_per_meter} """
        
        if unit == LinearPowerDensityUnits.MegaWattPerMeter:
            return f"""{self.mega_watts_per_meter} """
        
        if unit == LinearPowerDensityUnits.GigaWattPerMeter:
            return f"""{self.giga_watts_per_meter} """
        
        if unit == LinearPowerDensityUnits.MilliWattPerCentimeter:
            return f"""{self.milli_watts_per_centimeter} """
        
        if unit == LinearPowerDensityUnits.KiloWattPerCentimeter:
            return f"""{self.kilo_watts_per_centimeter} """
        
        if unit == LinearPowerDensityUnits.MegaWattPerCentimeter:
            return f"""{self.mega_watts_per_centimeter} """
        
        if unit == LinearPowerDensityUnits.GigaWattPerCentimeter:
            return f"""{self.giga_watts_per_centimeter} """
        
        if unit == LinearPowerDensityUnits.MilliWattPerMillimeter:
            return f"""{self.milli_watts_per_millimeter} """
        
        if unit == LinearPowerDensityUnits.KiloWattPerMillimeter:
            return f"""{self.kilo_watts_per_millimeter} """
        
        if unit == LinearPowerDensityUnits.MegaWattPerMillimeter:
            return f"""{self.mega_watts_per_millimeter} """
        
        if unit == LinearPowerDensityUnits.GigaWattPerMillimeter:
            return f"""{self.giga_watts_per_millimeter} """
        
        if unit == LinearPowerDensityUnits.MilliWattPerInch:
            return f"""{self.milli_watts_per_inch} """
        
        if unit == LinearPowerDensityUnits.KiloWattPerInch:
            return f"""{self.kilo_watts_per_inch} """
        
        if unit == LinearPowerDensityUnits.MegaWattPerInch:
            return f"""{self.mega_watts_per_inch} """
        
        if unit == LinearPowerDensityUnits.GigaWattPerInch:
            return f"""{self.giga_watts_per_inch} """
        
        if unit == LinearPowerDensityUnits.MilliWattPerFoot:
            return f"""{self.milli_watts_per_foot} """
        
        if unit == LinearPowerDensityUnits.KiloWattPerFoot:
            return f"""{self.kilo_watts_per_foot} """
        
        if unit == LinearPowerDensityUnits.MegaWattPerFoot:
            return f"""{self.mega_watts_per_foot} """
        
        if unit == LinearPowerDensityUnits.GigaWattPerFoot:
            return f"""{self.giga_watts_per_foot} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: LinearPowerDensityUnits = LinearPowerDensityUnits.WattPerMeter) -> string:
        """
        Get LinearPowerDensity unit abbreviation.
        Note! the default abbreviation for LinearPowerDensity is WattPerMeter.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == LinearPowerDensityUnits.WattPerMeter:
            return """W/m"""
        
        if unit_abbreviation == LinearPowerDensityUnits.WattPerCentimeter:
            return """W/cm"""
        
        if unit_abbreviation == LinearPowerDensityUnits.WattPerMillimeter:
            return """W/mm"""
        
        if unit_abbreviation == LinearPowerDensityUnits.WattPerInch:
            return """W/in"""
        
        if unit_abbreviation == LinearPowerDensityUnits.WattPerFoot:
            return """W/ft"""
        
        if unit_abbreviation == LinearPowerDensityUnits.MilliWattPerMeter:
            return """"""
        
        if unit_abbreviation == LinearPowerDensityUnits.KiloWattPerMeter:
            return """"""
        
        if unit_abbreviation == LinearPowerDensityUnits.MegaWattPerMeter:
            return """"""
        
        if unit_abbreviation == LinearPowerDensityUnits.GigaWattPerMeter:
            return """"""
        
        if unit_abbreviation == LinearPowerDensityUnits.MilliWattPerCentimeter:
            return """"""
        
        if unit_abbreviation == LinearPowerDensityUnits.KiloWattPerCentimeter:
            return """"""
        
        if unit_abbreviation == LinearPowerDensityUnits.MegaWattPerCentimeter:
            return """"""
        
        if unit_abbreviation == LinearPowerDensityUnits.GigaWattPerCentimeter:
            return """"""
        
        if unit_abbreviation == LinearPowerDensityUnits.MilliWattPerMillimeter:
            return """"""
        
        if unit_abbreviation == LinearPowerDensityUnits.KiloWattPerMillimeter:
            return """"""
        
        if unit_abbreviation == LinearPowerDensityUnits.MegaWattPerMillimeter:
            return """"""
        
        if unit_abbreviation == LinearPowerDensityUnits.GigaWattPerMillimeter:
            return """"""
        
        if unit_abbreviation == LinearPowerDensityUnits.MilliWattPerInch:
            return """"""
        
        if unit_abbreviation == LinearPowerDensityUnits.KiloWattPerInch:
            return """"""
        
        if unit_abbreviation == LinearPowerDensityUnits.MegaWattPerInch:
            return """"""
        
        if unit_abbreviation == LinearPowerDensityUnits.GigaWattPerInch:
            return """"""
        
        if unit_abbreviation == LinearPowerDensityUnits.MilliWattPerFoot:
            return """"""
        
        if unit_abbreviation == LinearPowerDensityUnits.KiloWattPerFoot:
            return """"""
        
        if unit_abbreviation == LinearPowerDensityUnits.MegaWattPerFoot:
            return """"""
        
        if unit_abbreviation == LinearPowerDensityUnits.GigaWattPerFoot:
            return """"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, LinearPowerDensity):
            raise TypeError("unsupported operand type(s) for +: 'LinearPowerDensity' and '{}'".format(type(other).__name__))
        return LinearPowerDensity(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, LinearPowerDensity):
            raise TypeError("unsupported operand type(s) for *: 'LinearPowerDensity' and '{}'".format(type(other).__name__))
        return LinearPowerDensity(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, LinearPowerDensity):
            raise TypeError("unsupported operand type(s) for -: 'LinearPowerDensity' and '{}'".format(type(other).__name__))
        return LinearPowerDensity(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, LinearPowerDensity):
            raise TypeError("unsupported operand type(s) for /: 'LinearPowerDensity' and '{}'".format(type(other).__name__))
        return LinearPowerDensity(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, LinearPowerDensity):
            raise TypeError("unsupported operand type(s) for %: 'LinearPowerDensity' and '{}'".format(type(other).__name__))
        return LinearPowerDensity(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, LinearPowerDensity):
            raise TypeError("unsupported operand type(s) for **: 'LinearPowerDensity' and '{}'".format(type(other).__name__))
        return LinearPowerDensity(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, LinearPowerDensity):
            raise TypeError("unsupported operand type(s) for ==: 'LinearPowerDensity' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, LinearPowerDensity):
            raise TypeError("unsupported operand type(s) for <: 'LinearPowerDensity' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, LinearPowerDensity):
            raise TypeError("unsupported operand type(s) for >: 'LinearPowerDensity' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, LinearPowerDensity):
            raise TypeError("unsupported operand type(s) for <=: 'LinearPowerDensity' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, LinearPowerDensity):
            raise TypeError("unsupported operand type(s) for >=: 'LinearPowerDensity' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value
from enum import Enum
import math
import string


class PowerDensityUnits(Enum):
        """
            PowerDensityUnits enumeration
        """
        
        WattPerCubicMeter = 'watt_per_cubic_meter'
        """
            
        """
        
        WattPerCubicInch = 'watt_per_cubic_inch'
        """
            
        """
        
        WattPerCubicFoot = 'watt_per_cubic_foot'
        """
            
        """
        
        WattPerLiter = 'watt_per_liter'
        """
            
        """
        
        PicoWattPerCubicMeter = 'pico_watt_per_cubic_meter'
        """
            
        """
        
        NanoWattPerCubicMeter = 'nano_watt_per_cubic_meter'
        """
            
        """
        
        MicroWattPerCubicMeter = 'micro_watt_per_cubic_meter'
        """
            
        """
        
        MilliWattPerCubicMeter = 'milli_watt_per_cubic_meter'
        """
            
        """
        
        DeciWattPerCubicMeter = 'deci_watt_per_cubic_meter'
        """
            
        """
        
        DecaWattPerCubicMeter = 'deca_watt_per_cubic_meter'
        """
            
        """
        
        KiloWattPerCubicMeter = 'kilo_watt_per_cubic_meter'
        """
            
        """
        
        MegaWattPerCubicMeter = 'mega_watt_per_cubic_meter'
        """
            
        """
        
        GigaWattPerCubicMeter = 'giga_watt_per_cubic_meter'
        """
            
        """
        
        TeraWattPerCubicMeter = 'tera_watt_per_cubic_meter'
        """
            
        """
        
        PicoWattPerCubicInch = 'pico_watt_per_cubic_inch'
        """
            
        """
        
        NanoWattPerCubicInch = 'nano_watt_per_cubic_inch'
        """
            
        """
        
        MicroWattPerCubicInch = 'micro_watt_per_cubic_inch'
        """
            
        """
        
        MilliWattPerCubicInch = 'milli_watt_per_cubic_inch'
        """
            
        """
        
        DeciWattPerCubicInch = 'deci_watt_per_cubic_inch'
        """
            
        """
        
        DecaWattPerCubicInch = 'deca_watt_per_cubic_inch'
        """
            
        """
        
        KiloWattPerCubicInch = 'kilo_watt_per_cubic_inch'
        """
            
        """
        
        MegaWattPerCubicInch = 'mega_watt_per_cubic_inch'
        """
            
        """
        
        GigaWattPerCubicInch = 'giga_watt_per_cubic_inch'
        """
            
        """
        
        TeraWattPerCubicInch = 'tera_watt_per_cubic_inch'
        """
            
        """
        
        PicoWattPerCubicFoot = 'pico_watt_per_cubic_foot'
        """
            
        """
        
        NanoWattPerCubicFoot = 'nano_watt_per_cubic_foot'
        """
            
        """
        
        MicroWattPerCubicFoot = 'micro_watt_per_cubic_foot'
        """
            
        """
        
        MilliWattPerCubicFoot = 'milli_watt_per_cubic_foot'
        """
            
        """
        
        DeciWattPerCubicFoot = 'deci_watt_per_cubic_foot'
        """
            
        """
        
        DecaWattPerCubicFoot = 'deca_watt_per_cubic_foot'
        """
            
        """
        
        KiloWattPerCubicFoot = 'kilo_watt_per_cubic_foot'
        """
            
        """
        
        MegaWattPerCubicFoot = 'mega_watt_per_cubic_foot'
        """
            
        """
        
        GigaWattPerCubicFoot = 'giga_watt_per_cubic_foot'
        """
            
        """
        
        TeraWattPerCubicFoot = 'tera_watt_per_cubic_foot'
        """
            
        """
        
        PicoWattPerLiter = 'pico_watt_per_liter'
        """
            
        """
        
        NanoWattPerLiter = 'nano_watt_per_liter'
        """
            
        """
        
        MicroWattPerLiter = 'micro_watt_per_liter'
        """
            
        """
        
        MilliWattPerLiter = 'milli_watt_per_liter'
        """
            
        """
        
        DeciWattPerLiter = 'deci_watt_per_liter'
        """
            
        """
        
        DecaWattPerLiter = 'deca_watt_per_liter'
        """
            
        """
        
        KiloWattPerLiter = 'kilo_watt_per_liter'
        """
            
        """
        
        MegaWattPerLiter = 'mega_watt_per_liter'
        """
            
        """
        
        GigaWattPerLiter = 'giga_watt_per_liter'
        """
            
        """
        
        TeraWattPerLiter = 'tera_watt_per_liter'
        """
            
        """
        
    
class PowerDensity:
    """
    The amount of power in a volume.

    Args:
        value (float): The value.
        from_unit (PowerDensityUnits): The PowerDensity unit to create from, The default unit is WattPerCubicMeter
    """
    def __init__(self, value: float, from_unit: PowerDensityUnits = PowerDensityUnits.WattPerCubicMeter):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__watts_per_cubic_meter = None
        
        self.__watts_per_cubic_inch = None
        
        self.__watts_per_cubic_foot = None
        
        self.__watts_per_liter = None
        
        self.__pico_watts_per_cubic_meter = None
        
        self.__nano_watts_per_cubic_meter = None
        
        self.__micro_watts_per_cubic_meter = None
        
        self.__milli_watts_per_cubic_meter = None
        
        self.__deci_watts_per_cubic_meter = None
        
        self.__deca_watts_per_cubic_meter = None
        
        self.__kilo_watts_per_cubic_meter = None
        
        self.__mega_watts_per_cubic_meter = None
        
        self.__giga_watts_per_cubic_meter = None
        
        self.__tera_watts_per_cubic_meter = None
        
        self.__pico_watts_per_cubic_inch = None
        
        self.__nano_watts_per_cubic_inch = None
        
        self.__micro_watts_per_cubic_inch = None
        
        self.__milli_watts_per_cubic_inch = None
        
        self.__deci_watts_per_cubic_inch = None
        
        self.__deca_watts_per_cubic_inch = None
        
        self.__kilo_watts_per_cubic_inch = None
        
        self.__mega_watts_per_cubic_inch = None
        
        self.__giga_watts_per_cubic_inch = None
        
        self.__tera_watts_per_cubic_inch = None
        
        self.__pico_watts_per_cubic_foot = None
        
        self.__nano_watts_per_cubic_foot = None
        
        self.__micro_watts_per_cubic_foot = None
        
        self.__milli_watts_per_cubic_foot = None
        
        self.__deci_watts_per_cubic_foot = None
        
        self.__deca_watts_per_cubic_foot = None
        
        self.__kilo_watts_per_cubic_foot = None
        
        self.__mega_watts_per_cubic_foot = None
        
        self.__giga_watts_per_cubic_foot = None
        
        self.__tera_watts_per_cubic_foot = None
        
        self.__pico_watts_per_liter = None
        
        self.__nano_watts_per_liter = None
        
        self.__micro_watts_per_liter = None
        
        self.__milli_watts_per_liter = None
        
        self.__deci_watts_per_liter = None
        
        self.__deca_watts_per_liter = None
        
        self.__kilo_watts_per_liter = None
        
        self.__mega_watts_per_liter = None
        
        self.__giga_watts_per_liter = None
        
        self.__tera_watts_per_liter = None
        

    def __convert_from_base(self, from_unit: PowerDensityUnits) -> float:
        value = self.__value
        
        if from_unit == PowerDensityUnits.WattPerCubicMeter:
            return (value)
        
        if from_unit == PowerDensityUnits.WattPerCubicInch:
            return (value / 6.102374409473228e4)
        
        if from_unit == PowerDensityUnits.WattPerCubicFoot:
            return (value / 3.531466672148859e1)
        
        if from_unit == PowerDensityUnits.WattPerLiter:
            return (value / 1.0e3)
        
        if from_unit == PowerDensityUnits.PicoWattPerCubicMeter:
            return ((value) / 1e-12)
        
        if from_unit == PowerDensityUnits.NanoWattPerCubicMeter:
            return ((value) / 1e-09)
        
        if from_unit == PowerDensityUnits.MicroWattPerCubicMeter:
            return ((value) / 1e-06)
        
        if from_unit == PowerDensityUnits.MilliWattPerCubicMeter:
            return ((value) / 0.001)
        
        if from_unit == PowerDensityUnits.DeciWattPerCubicMeter:
            return ((value) / 0.1)
        
        if from_unit == PowerDensityUnits.DecaWattPerCubicMeter:
            return ((value) / 10.0)
        
        if from_unit == PowerDensityUnits.KiloWattPerCubicMeter:
            return ((value) / 1000.0)
        
        if from_unit == PowerDensityUnits.MegaWattPerCubicMeter:
            return ((value) / 1000000.0)
        
        if from_unit == PowerDensityUnits.GigaWattPerCubicMeter:
            return ((value) / 1000000000.0)
        
        if from_unit == PowerDensityUnits.TeraWattPerCubicMeter:
            return ((value) / 1000000000000.0)
        
        if from_unit == PowerDensityUnits.PicoWattPerCubicInch:
            return ((value / 6.102374409473228e4) / 1e-12)
        
        if from_unit == PowerDensityUnits.NanoWattPerCubicInch:
            return ((value / 6.102374409473228e4) / 1e-09)
        
        if from_unit == PowerDensityUnits.MicroWattPerCubicInch:
            return ((value / 6.102374409473228e4) / 1e-06)
        
        if from_unit == PowerDensityUnits.MilliWattPerCubicInch:
            return ((value / 6.102374409473228e4) / 0.001)
        
        if from_unit == PowerDensityUnits.DeciWattPerCubicInch:
            return ((value / 6.102374409473228e4) / 0.1)
        
        if from_unit == PowerDensityUnits.DecaWattPerCubicInch:
            return ((value / 6.102374409473228e4) / 10.0)
        
        if from_unit == PowerDensityUnits.KiloWattPerCubicInch:
            return ((value / 6.102374409473228e4) / 1000.0)
        
        if from_unit == PowerDensityUnits.MegaWattPerCubicInch:
            return ((value / 6.102374409473228e4) / 1000000.0)
        
        if from_unit == PowerDensityUnits.GigaWattPerCubicInch:
            return ((value / 6.102374409473228e4) / 1000000000.0)
        
        if from_unit == PowerDensityUnits.TeraWattPerCubicInch:
            return ((value / 6.102374409473228e4) / 1000000000000.0)
        
        if from_unit == PowerDensityUnits.PicoWattPerCubicFoot:
            return ((value / 3.531466672148859e1) / 1e-12)
        
        if from_unit == PowerDensityUnits.NanoWattPerCubicFoot:
            return ((value / 3.531466672148859e1) / 1e-09)
        
        if from_unit == PowerDensityUnits.MicroWattPerCubicFoot:
            return ((value / 3.531466672148859e1) / 1e-06)
        
        if from_unit == PowerDensityUnits.MilliWattPerCubicFoot:
            return ((value / 3.531466672148859e1) / 0.001)
        
        if from_unit == PowerDensityUnits.DeciWattPerCubicFoot:
            return ((value / 3.531466672148859e1) / 0.1)
        
        if from_unit == PowerDensityUnits.DecaWattPerCubicFoot:
            return ((value / 3.531466672148859e1) / 10.0)
        
        if from_unit == PowerDensityUnits.KiloWattPerCubicFoot:
            return ((value / 3.531466672148859e1) / 1000.0)
        
        if from_unit == PowerDensityUnits.MegaWattPerCubicFoot:
            return ((value / 3.531466672148859e1) / 1000000.0)
        
        if from_unit == PowerDensityUnits.GigaWattPerCubicFoot:
            return ((value / 3.531466672148859e1) / 1000000000.0)
        
        if from_unit == PowerDensityUnits.TeraWattPerCubicFoot:
            return ((value / 3.531466672148859e1) / 1000000000000.0)
        
        if from_unit == PowerDensityUnits.PicoWattPerLiter:
            return ((value / 1.0e3) / 1e-12)
        
        if from_unit == PowerDensityUnits.NanoWattPerLiter:
            return ((value / 1.0e3) / 1e-09)
        
        if from_unit == PowerDensityUnits.MicroWattPerLiter:
            return ((value / 1.0e3) / 1e-06)
        
        if from_unit == PowerDensityUnits.MilliWattPerLiter:
            return ((value / 1.0e3) / 0.001)
        
        if from_unit == PowerDensityUnits.DeciWattPerLiter:
            return ((value / 1.0e3) / 0.1)
        
        if from_unit == PowerDensityUnits.DecaWattPerLiter:
            return ((value / 1.0e3) / 10.0)
        
        if from_unit == PowerDensityUnits.KiloWattPerLiter:
            return ((value / 1.0e3) / 1000.0)
        
        if from_unit == PowerDensityUnits.MegaWattPerLiter:
            return ((value / 1.0e3) / 1000000.0)
        
        if from_unit == PowerDensityUnits.GigaWattPerLiter:
            return ((value / 1.0e3) / 1000000000.0)
        
        if from_unit == PowerDensityUnits.TeraWattPerLiter:
            return ((value / 1.0e3) / 1000000000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: PowerDensityUnits) -> float:
        
        if to_unit == PowerDensityUnits.WattPerCubicMeter:
            return (value)
        
        if to_unit == PowerDensityUnits.WattPerCubicInch:
            return (value * 6.102374409473228e4)
        
        if to_unit == PowerDensityUnits.WattPerCubicFoot:
            return (value * 3.531466672148859e1)
        
        if to_unit == PowerDensityUnits.WattPerLiter:
            return (value * 1.0e3)
        
        if to_unit == PowerDensityUnits.PicoWattPerCubicMeter:
            return ((value) * 1e-12)
        
        if to_unit == PowerDensityUnits.NanoWattPerCubicMeter:
            return ((value) * 1e-09)
        
        if to_unit == PowerDensityUnits.MicroWattPerCubicMeter:
            return ((value) * 1e-06)
        
        if to_unit == PowerDensityUnits.MilliWattPerCubicMeter:
            return ((value) * 0.001)
        
        if to_unit == PowerDensityUnits.DeciWattPerCubicMeter:
            return ((value) * 0.1)
        
        if to_unit == PowerDensityUnits.DecaWattPerCubicMeter:
            return ((value) * 10.0)
        
        if to_unit == PowerDensityUnits.KiloWattPerCubicMeter:
            return ((value) * 1000.0)
        
        if to_unit == PowerDensityUnits.MegaWattPerCubicMeter:
            return ((value) * 1000000.0)
        
        if to_unit == PowerDensityUnits.GigaWattPerCubicMeter:
            return ((value) * 1000000000.0)
        
        if to_unit == PowerDensityUnits.TeraWattPerCubicMeter:
            return ((value) * 1000000000000.0)
        
        if to_unit == PowerDensityUnits.PicoWattPerCubicInch:
            return ((value * 6.102374409473228e4) * 1e-12)
        
        if to_unit == PowerDensityUnits.NanoWattPerCubicInch:
            return ((value * 6.102374409473228e4) * 1e-09)
        
        if to_unit == PowerDensityUnits.MicroWattPerCubicInch:
            return ((value * 6.102374409473228e4) * 1e-06)
        
        if to_unit == PowerDensityUnits.MilliWattPerCubicInch:
            return ((value * 6.102374409473228e4) * 0.001)
        
        if to_unit == PowerDensityUnits.DeciWattPerCubicInch:
            return ((value * 6.102374409473228e4) * 0.1)
        
        if to_unit == PowerDensityUnits.DecaWattPerCubicInch:
            return ((value * 6.102374409473228e4) * 10.0)
        
        if to_unit == PowerDensityUnits.KiloWattPerCubicInch:
            return ((value * 6.102374409473228e4) * 1000.0)
        
        if to_unit == PowerDensityUnits.MegaWattPerCubicInch:
            return ((value * 6.102374409473228e4) * 1000000.0)
        
        if to_unit == PowerDensityUnits.GigaWattPerCubicInch:
            return ((value * 6.102374409473228e4) * 1000000000.0)
        
        if to_unit == PowerDensityUnits.TeraWattPerCubicInch:
            return ((value * 6.102374409473228e4) * 1000000000000.0)
        
        if to_unit == PowerDensityUnits.PicoWattPerCubicFoot:
            return ((value * 3.531466672148859e1) * 1e-12)
        
        if to_unit == PowerDensityUnits.NanoWattPerCubicFoot:
            return ((value * 3.531466672148859e1) * 1e-09)
        
        if to_unit == PowerDensityUnits.MicroWattPerCubicFoot:
            return ((value * 3.531466672148859e1) * 1e-06)
        
        if to_unit == PowerDensityUnits.MilliWattPerCubicFoot:
            return ((value * 3.531466672148859e1) * 0.001)
        
        if to_unit == PowerDensityUnits.DeciWattPerCubicFoot:
            return ((value * 3.531466672148859e1) * 0.1)
        
        if to_unit == PowerDensityUnits.DecaWattPerCubicFoot:
            return ((value * 3.531466672148859e1) * 10.0)
        
        if to_unit == PowerDensityUnits.KiloWattPerCubicFoot:
            return ((value * 3.531466672148859e1) * 1000.0)
        
        if to_unit == PowerDensityUnits.MegaWattPerCubicFoot:
            return ((value * 3.531466672148859e1) * 1000000.0)
        
        if to_unit == PowerDensityUnits.GigaWattPerCubicFoot:
            return ((value * 3.531466672148859e1) * 1000000000.0)
        
        if to_unit == PowerDensityUnits.TeraWattPerCubicFoot:
            return ((value * 3.531466672148859e1) * 1000000000000.0)
        
        if to_unit == PowerDensityUnits.PicoWattPerLiter:
            return ((value * 1.0e3) * 1e-12)
        
        if to_unit == PowerDensityUnits.NanoWattPerLiter:
            return ((value * 1.0e3) * 1e-09)
        
        if to_unit == PowerDensityUnits.MicroWattPerLiter:
            return ((value * 1.0e3) * 1e-06)
        
        if to_unit == PowerDensityUnits.MilliWattPerLiter:
            return ((value * 1.0e3) * 0.001)
        
        if to_unit == PowerDensityUnits.DeciWattPerLiter:
            return ((value * 1.0e3) * 0.1)
        
        if to_unit == PowerDensityUnits.DecaWattPerLiter:
            return ((value * 1.0e3) * 10.0)
        
        if to_unit == PowerDensityUnits.KiloWattPerLiter:
            return ((value * 1.0e3) * 1000.0)
        
        if to_unit == PowerDensityUnits.MegaWattPerLiter:
            return ((value * 1.0e3) * 1000000.0)
        
        if to_unit == PowerDensityUnits.GigaWattPerLiter:
            return ((value * 1.0e3) * 1000000000.0)
        
        if to_unit == PowerDensityUnits.TeraWattPerLiter:
            return ((value * 1.0e3) * 1000000000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
    @staticmethod
    def from_watts_per_cubic_meter(watts_per_cubic_meter: float):
        """
        Create a new instance of PowerDensity from a value in watts_per_cubic_meter.

        

        :param meters: The PowerDensity value in watts_per_cubic_meter.
        :type watts_per_cubic_meter: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(watts_per_cubic_meter, PowerDensityUnits.WattPerCubicMeter)

    
    @staticmethod
    def from_watts_per_cubic_inch(watts_per_cubic_inch: float):
        """
        Create a new instance of PowerDensity from a value in watts_per_cubic_inch.

        

        :param meters: The PowerDensity value in watts_per_cubic_inch.
        :type watts_per_cubic_inch: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(watts_per_cubic_inch, PowerDensityUnits.WattPerCubicInch)

    
    @staticmethod
    def from_watts_per_cubic_foot(watts_per_cubic_foot: float):
        """
        Create a new instance of PowerDensity from a value in watts_per_cubic_foot.

        

        :param meters: The PowerDensity value in watts_per_cubic_foot.
        :type watts_per_cubic_foot: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(watts_per_cubic_foot, PowerDensityUnits.WattPerCubicFoot)

    
    @staticmethod
    def from_watts_per_liter(watts_per_liter: float):
        """
        Create a new instance of PowerDensity from a value in watts_per_liter.

        

        :param meters: The PowerDensity value in watts_per_liter.
        :type watts_per_liter: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(watts_per_liter, PowerDensityUnits.WattPerLiter)

    
    @staticmethod
    def from_pico_watts_per_cubic_meter(pico_watts_per_cubic_meter: float):
        """
        Create a new instance of PowerDensity from a value in pico_watts_per_cubic_meter.

        

        :param meters: The PowerDensity value in pico_watts_per_cubic_meter.
        :type pico_watts_per_cubic_meter: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(pico_watts_per_cubic_meter, PowerDensityUnits.PicoWattPerCubicMeter)

    
    @staticmethod
    def from_nano_watts_per_cubic_meter(nano_watts_per_cubic_meter: float):
        """
        Create a new instance of PowerDensity from a value in nano_watts_per_cubic_meter.

        

        :param meters: The PowerDensity value in nano_watts_per_cubic_meter.
        :type nano_watts_per_cubic_meter: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(nano_watts_per_cubic_meter, PowerDensityUnits.NanoWattPerCubicMeter)

    
    @staticmethod
    def from_micro_watts_per_cubic_meter(micro_watts_per_cubic_meter: float):
        """
        Create a new instance of PowerDensity from a value in micro_watts_per_cubic_meter.

        

        :param meters: The PowerDensity value in micro_watts_per_cubic_meter.
        :type micro_watts_per_cubic_meter: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(micro_watts_per_cubic_meter, PowerDensityUnits.MicroWattPerCubicMeter)

    
    @staticmethod
    def from_milli_watts_per_cubic_meter(milli_watts_per_cubic_meter: float):
        """
        Create a new instance of PowerDensity from a value in milli_watts_per_cubic_meter.

        

        :param meters: The PowerDensity value in milli_watts_per_cubic_meter.
        :type milli_watts_per_cubic_meter: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(milli_watts_per_cubic_meter, PowerDensityUnits.MilliWattPerCubicMeter)

    
    @staticmethod
    def from_deci_watts_per_cubic_meter(deci_watts_per_cubic_meter: float):
        """
        Create a new instance of PowerDensity from a value in deci_watts_per_cubic_meter.

        

        :param meters: The PowerDensity value in deci_watts_per_cubic_meter.
        :type deci_watts_per_cubic_meter: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(deci_watts_per_cubic_meter, PowerDensityUnits.DeciWattPerCubicMeter)

    
    @staticmethod
    def from_deca_watts_per_cubic_meter(deca_watts_per_cubic_meter: float):
        """
        Create a new instance of PowerDensity from a value in deca_watts_per_cubic_meter.

        

        :param meters: The PowerDensity value in deca_watts_per_cubic_meter.
        :type deca_watts_per_cubic_meter: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(deca_watts_per_cubic_meter, PowerDensityUnits.DecaWattPerCubicMeter)

    
    @staticmethod
    def from_kilo_watts_per_cubic_meter(kilo_watts_per_cubic_meter: float):
        """
        Create a new instance of PowerDensity from a value in kilo_watts_per_cubic_meter.

        

        :param meters: The PowerDensity value in kilo_watts_per_cubic_meter.
        :type kilo_watts_per_cubic_meter: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(kilo_watts_per_cubic_meter, PowerDensityUnits.KiloWattPerCubicMeter)

    
    @staticmethod
    def from_mega_watts_per_cubic_meter(mega_watts_per_cubic_meter: float):
        """
        Create a new instance of PowerDensity from a value in mega_watts_per_cubic_meter.

        

        :param meters: The PowerDensity value in mega_watts_per_cubic_meter.
        :type mega_watts_per_cubic_meter: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(mega_watts_per_cubic_meter, PowerDensityUnits.MegaWattPerCubicMeter)

    
    @staticmethod
    def from_giga_watts_per_cubic_meter(giga_watts_per_cubic_meter: float):
        """
        Create a new instance of PowerDensity from a value in giga_watts_per_cubic_meter.

        

        :param meters: The PowerDensity value in giga_watts_per_cubic_meter.
        :type giga_watts_per_cubic_meter: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(giga_watts_per_cubic_meter, PowerDensityUnits.GigaWattPerCubicMeter)

    
    @staticmethod
    def from_tera_watts_per_cubic_meter(tera_watts_per_cubic_meter: float):
        """
        Create a new instance of PowerDensity from a value in tera_watts_per_cubic_meter.

        

        :param meters: The PowerDensity value in tera_watts_per_cubic_meter.
        :type tera_watts_per_cubic_meter: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(tera_watts_per_cubic_meter, PowerDensityUnits.TeraWattPerCubicMeter)

    
    @staticmethod
    def from_pico_watts_per_cubic_inch(pico_watts_per_cubic_inch: float):
        """
        Create a new instance of PowerDensity from a value in pico_watts_per_cubic_inch.

        

        :param meters: The PowerDensity value in pico_watts_per_cubic_inch.
        :type pico_watts_per_cubic_inch: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(pico_watts_per_cubic_inch, PowerDensityUnits.PicoWattPerCubicInch)

    
    @staticmethod
    def from_nano_watts_per_cubic_inch(nano_watts_per_cubic_inch: float):
        """
        Create a new instance of PowerDensity from a value in nano_watts_per_cubic_inch.

        

        :param meters: The PowerDensity value in nano_watts_per_cubic_inch.
        :type nano_watts_per_cubic_inch: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(nano_watts_per_cubic_inch, PowerDensityUnits.NanoWattPerCubicInch)

    
    @staticmethod
    def from_micro_watts_per_cubic_inch(micro_watts_per_cubic_inch: float):
        """
        Create a new instance of PowerDensity from a value in micro_watts_per_cubic_inch.

        

        :param meters: The PowerDensity value in micro_watts_per_cubic_inch.
        :type micro_watts_per_cubic_inch: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(micro_watts_per_cubic_inch, PowerDensityUnits.MicroWattPerCubicInch)

    
    @staticmethod
    def from_milli_watts_per_cubic_inch(milli_watts_per_cubic_inch: float):
        """
        Create a new instance of PowerDensity from a value in milli_watts_per_cubic_inch.

        

        :param meters: The PowerDensity value in milli_watts_per_cubic_inch.
        :type milli_watts_per_cubic_inch: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(milli_watts_per_cubic_inch, PowerDensityUnits.MilliWattPerCubicInch)

    
    @staticmethod
    def from_deci_watts_per_cubic_inch(deci_watts_per_cubic_inch: float):
        """
        Create a new instance of PowerDensity from a value in deci_watts_per_cubic_inch.

        

        :param meters: The PowerDensity value in deci_watts_per_cubic_inch.
        :type deci_watts_per_cubic_inch: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(deci_watts_per_cubic_inch, PowerDensityUnits.DeciWattPerCubicInch)

    
    @staticmethod
    def from_deca_watts_per_cubic_inch(deca_watts_per_cubic_inch: float):
        """
        Create a new instance of PowerDensity from a value in deca_watts_per_cubic_inch.

        

        :param meters: The PowerDensity value in deca_watts_per_cubic_inch.
        :type deca_watts_per_cubic_inch: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(deca_watts_per_cubic_inch, PowerDensityUnits.DecaWattPerCubicInch)

    
    @staticmethod
    def from_kilo_watts_per_cubic_inch(kilo_watts_per_cubic_inch: float):
        """
        Create a new instance of PowerDensity from a value in kilo_watts_per_cubic_inch.

        

        :param meters: The PowerDensity value in kilo_watts_per_cubic_inch.
        :type kilo_watts_per_cubic_inch: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(kilo_watts_per_cubic_inch, PowerDensityUnits.KiloWattPerCubicInch)

    
    @staticmethod
    def from_mega_watts_per_cubic_inch(mega_watts_per_cubic_inch: float):
        """
        Create a new instance of PowerDensity from a value in mega_watts_per_cubic_inch.

        

        :param meters: The PowerDensity value in mega_watts_per_cubic_inch.
        :type mega_watts_per_cubic_inch: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(mega_watts_per_cubic_inch, PowerDensityUnits.MegaWattPerCubicInch)

    
    @staticmethod
    def from_giga_watts_per_cubic_inch(giga_watts_per_cubic_inch: float):
        """
        Create a new instance of PowerDensity from a value in giga_watts_per_cubic_inch.

        

        :param meters: The PowerDensity value in giga_watts_per_cubic_inch.
        :type giga_watts_per_cubic_inch: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(giga_watts_per_cubic_inch, PowerDensityUnits.GigaWattPerCubicInch)

    
    @staticmethod
    def from_tera_watts_per_cubic_inch(tera_watts_per_cubic_inch: float):
        """
        Create a new instance of PowerDensity from a value in tera_watts_per_cubic_inch.

        

        :param meters: The PowerDensity value in tera_watts_per_cubic_inch.
        :type tera_watts_per_cubic_inch: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(tera_watts_per_cubic_inch, PowerDensityUnits.TeraWattPerCubicInch)

    
    @staticmethod
    def from_pico_watts_per_cubic_foot(pico_watts_per_cubic_foot: float):
        """
        Create a new instance of PowerDensity from a value in pico_watts_per_cubic_foot.

        

        :param meters: The PowerDensity value in pico_watts_per_cubic_foot.
        :type pico_watts_per_cubic_foot: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(pico_watts_per_cubic_foot, PowerDensityUnits.PicoWattPerCubicFoot)

    
    @staticmethod
    def from_nano_watts_per_cubic_foot(nano_watts_per_cubic_foot: float):
        """
        Create a new instance of PowerDensity from a value in nano_watts_per_cubic_foot.

        

        :param meters: The PowerDensity value in nano_watts_per_cubic_foot.
        :type nano_watts_per_cubic_foot: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(nano_watts_per_cubic_foot, PowerDensityUnits.NanoWattPerCubicFoot)

    
    @staticmethod
    def from_micro_watts_per_cubic_foot(micro_watts_per_cubic_foot: float):
        """
        Create a new instance of PowerDensity from a value in micro_watts_per_cubic_foot.

        

        :param meters: The PowerDensity value in micro_watts_per_cubic_foot.
        :type micro_watts_per_cubic_foot: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(micro_watts_per_cubic_foot, PowerDensityUnits.MicroWattPerCubicFoot)

    
    @staticmethod
    def from_milli_watts_per_cubic_foot(milli_watts_per_cubic_foot: float):
        """
        Create a new instance of PowerDensity from a value in milli_watts_per_cubic_foot.

        

        :param meters: The PowerDensity value in milli_watts_per_cubic_foot.
        :type milli_watts_per_cubic_foot: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(milli_watts_per_cubic_foot, PowerDensityUnits.MilliWattPerCubicFoot)

    
    @staticmethod
    def from_deci_watts_per_cubic_foot(deci_watts_per_cubic_foot: float):
        """
        Create a new instance of PowerDensity from a value in deci_watts_per_cubic_foot.

        

        :param meters: The PowerDensity value in deci_watts_per_cubic_foot.
        :type deci_watts_per_cubic_foot: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(deci_watts_per_cubic_foot, PowerDensityUnits.DeciWattPerCubicFoot)

    
    @staticmethod
    def from_deca_watts_per_cubic_foot(deca_watts_per_cubic_foot: float):
        """
        Create a new instance of PowerDensity from a value in deca_watts_per_cubic_foot.

        

        :param meters: The PowerDensity value in deca_watts_per_cubic_foot.
        :type deca_watts_per_cubic_foot: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(deca_watts_per_cubic_foot, PowerDensityUnits.DecaWattPerCubicFoot)

    
    @staticmethod
    def from_kilo_watts_per_cubic_foot(kilo_watts_per_cubic_foot: float):
        """
        Create a new instance of PowerDensity from a value in kilo_watts_per_cubic_foot.

        

        :param meters: The PowerDensity value in kilo_watts_per_cubic_foot.
        :type kilo_watts_per_cubic_foot: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(kilo_watts_per_cubic_foot, PowerDensityUnits.KiloWattPerCubicFoot)

    
    @staticmethod
    def from_mega_watts_per_cubic_foot(mega_watts_per_cubic_foot: float):
        """
        Create a new instance of PowerDensity from a value in mega_watts_per_cubic_foot.

        

        :param meters: The PowerDensity value in mega_watts_per_cubic_foot.
        :type mega_watts_per_cubic_foot: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(mega_watts_per_cubic_foot, PowerDensityUnits.MegaWattPerCubicFoot)

    
    @staticmethod
    def from_giga_watts_per_cubic_foot(giga_watts_per_cubic_foot: float):
        """
        Create a new instance of PowerDensity from a value in giga_watts_per_cubic_foot.

        

        :param meters: The PowerDensity value in giga_watts_per_cubic_foot.
        :type giga_watts_per_cubic_foot: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(giga_watts_per_cubic_foot, PowerDensityUnits.GigaWattPerCubicFoot)

    
    @staticmethod
    def from_tera_watts_per_cubic_foot(tera_watts_per_cubic_foot: float):
        """
        Create a new instance of PowerDensity from a value in tera_watts_per_cubic_foot.

        

        :param meters: The PowerDensity value in tera_watts_per_cubic_foot.
        :type tera_watts_per_cubic_foot: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(tera_watts_per_cubic_foot, PowerDensityUnits.TeraWattPerCubicFoot)

    
    @staticmethod
    def from_pico_watts_per_liter(pico_watts_per_liter: float):
        """
        Create a new instance of PowerDensity from a value in pico_watts_per_liter.

        

        :param meters: The PowerDensity value in pico_watts_per_liter.
        :type pico_watts_per_liter: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(pico_watts_per_liter, PowerDensityUnits.PicoWattPerLiter)

    
    @staticmethod
    def from_nano_watts_per_liter(nano_watts_per_liter: float):
        """
        Create a new instance of PowerDensity from a value in nano_watts_per_liter.

        

        :param meters: The PowerDensity value in nano_watts_per_liter.
        :type nano_watts_per_liter: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(nano_watts_per_liter, PowerDensityUnits.NanoWattPerLiter)

    
    @staticmethod
    def from_micro_watts_per_liter(micro_watts_per_liter: float):
        """
        Create a new instance of PowerDensity from a value in micro_watts_per_liter.

        

        :param meters: The PowerDensity value in micro_watts_per_liter.
        :type micro_watts_per_liter: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(micro_watts_per_liter, PowerDensityUnits.MicroWattPerLiter)

    
    @staticmethod
    def from_milli_watts_per_liter(milli_watts_per_liter: float):
        """
        Create a new instance of PowerDensity from a value in milli_watts_per_liter.

        

        :param meters: The PowerDensity value in milli_watts_per_liter.
        :type milli_watts_per_liter: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(milli_watts_per_liter, PowerDensityUnits.MilliWattPerLiter)

    
    @staticmethod
    def from_deci_watts_per_liter(deci_watts_per_liter: float):
        """
        Create a new instance of PowerDensity from a value in deci_watts_per_liter.

        

        :param meters: The PowerDensity value in deci_watts_per_liter.
        :type deci_watts_per_liter: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(deci_watts_per_liter, PowerDensityUnits.DeciWattPerLiter)

    
    @staticmethod
    def from_deca_watts_per_liter(deca_watts_per_liter: float):
        """
        Create a new instance of PowerDensity from a value in deca_watts_per_liter.

        

        :param meters: The PowerDensity value in deca_watts_per_liter.
        :type deca_watts_per_liter: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(deca_watts_per_liter, PowerDensityUnits.DecaWattPerLiter)

    
    @staticmethod
    def from_kilo_watts_per_liter(kilo_watts_per_liter: float):
        """
        Create a new instance of PowerDensity from a value in kilo_watts_per_liter.

        

        :param meters: The PowerDensity value in kilo_watts_per_liter.
        :type kilo_watts_per_liter: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(kilo_watts_per_liter, PowerDensityUnits.KiloWattPerLiter)

    
    @staticmethod
    def from_mega_watts_per_liter(mega_watts_per_liter: float):
        """
        Create a new instance of PowerDensity from a value in mega_watts_per_liter.

        

        :param meters: The PowerDensity value in mega_watts_per_liter.
        :type mega_watts_per_liter: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(mega_watts_per_liter, PowerDensityUnits.MegaWattPerLiter)

    
    @staticmethod
    def from_giga_watts_per_liter(giga_watts_per_liter: float):
        """
        Create a new instance of PowerDensity from a value in giga_watts_per_liter.

        

        :param meters: The PowerDensity value in giga_watts_per_liter.
        :type giga_watts_per_liter: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(giga_watts_per_liter, PowerDensityUnits.GigaWattPerLiter)

    
    @staticmethod
    def from_tera_watts_per_liter(tera_watts_per_liter: float):
        """
        Create a new instance of PowerDensity from a value in tera_watts_per_liter.

        

        :param meters: The PowerDensity value in tera_watts_per_liter.
        :type tera_watts_per_liter: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(tera_watts_per_liter, PowerDensityUnits.TeraWattPerLiter)

    
    @property
    def watts_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__watts_per_cubic_meter != None:
            return self.__watts_per_cubic_meter
        self.__watts_per_cubic_meter = self.__convert_from_base(PowerDensityUnits.WattPerCubicMeter)
        return self.__watts_per_cubic_meter

    
    @property
    def watts_per_cubic_inch(self) -> float:
        """
        
        """
        if self.__watts_per_cubic_inch != None:
            return self.__watts_per_cubic_inch
        self.__watts_per_cubic_inch = self.__convert_from_base(PowerDensityUnits.WattPerCubicInch)
        return self.__watts_per_cubic_inch

    
    @property
    def watts_per_cubic_foot(self) -> float:
        """
        
        """
        if self.__watts_per_cubic_foot != None:
            return self.__watts_per_cubic_foot
        self.__watts_per_cubic_foot = self.__convert_from_base(PowerDensityUnits.WattPerCubicFoot)
        return self.__watts_per_cubic_foot

    
    @property
    def watts_per_liter(self) -> float:
        """
        
        """
        if self.__watts_per_liter != None:
            return self.__watts_per_liter
        self.__watts_per_liter = self.__convert_from_base(PowerDensityUnits.WattPerLiter)
        return self.__watts_per_liter

    
    @property
    def pico_watts_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__pico_watts_per_cubic_meter != None:
            return self.__pico_watts_per_cubic_meter
        self.__pico_watts_per_cubic_meter = self.__convert_from_base(PowerDensityUnits.PicoWattPerCubicMeter)
        return self.__pico_watts_per_cubic_meter

    
    @property
    def nano_watts_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__nano_watts_per_cubic_meter != None:
            return self.__nano_watts_per_cubic_meter
        self.__nano_watts_per_cubic_meter = self.__convert_from_base(PowerDensityUnits.NanoWattPerCubicMeter)
        return self.__nano_watts_per_cubic_meter

    
    @property
    def micro_watts_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__micro_watts_per_cubic_meter != None:
            return self.__micro_watts_per_cubic_meter
        self.__micro_watts_per_cubic_meter = self.__convert_from_base(PowerDensityUnits.MicroWattPerCubicMeter)
        return self.__micro_watts_per_cubic_meter

    
    @property
    def milli_watts_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__milli_watts_per_cubic_meter != None:
            return self.__milli_watts_per_cubic_meter
        self.__milli_watts_per_cubic_meter = self.__convert_from_base(PowerDensityUnits.MilliWattPerCubicMeter)
        return self.__milli_watts_per_cubic_meter

    
    @property
    def deci_watts_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__deci_watts_per_cubic_meter != None:
            return self.__deci_watts_per_cubic_meter
        self.__deci_watts_per_cubic_meter = self.__convert_from_base(PowerDensityUnits.DeciWattPerCubicMeter)
        return self.__deci_watts_per_cubic_meter

    
    @property
    def deca_watts_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__deca_watts_per_cubic_meter != None:
            return self.__deca_watts_per_cubic_meter
        self.__deca_watts_per_cubic_meter = self.__convert_from_base(PowerDensityUnits.DecaWattPerCubicMeter)
        return self.__deca_watts_per_cubic_meter

    
    @property
    def kilo_watts_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__kilo_watts_per_cubic_meter != None:
            return self.__kilo_watts_per_cubic_meter
        self.__kilo_watts_per_cubic_meter = self.__convert_from_base(PowerDensityUnits.KiloWattPerCubicMeter)
        return self.__kilo_watts_per_cubic_meter

    
    @property
    def mega_watts_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__mega_watts_per_cubic_meter != None:
            return self.__mega_watts_per_cubic_meter
        self.__mega_watts_per_cubic_meter = self.__convert_from_base(PowerDensityUnits.MegaWattPerCubicMeter)
        return self.__mega_watts_per_cubic_meter

    
    @property
    def giga_watts_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__giga_watts_per_cubic_meter != None:
            return self.__giga_watts_per_cubic_meter
        self.__giga_watts_per_cubic_meter = self.__convert_from_base(PowerDensityUnits.GigaWattPerCubicMeter)
        return self.__giga_watts_per_cubic_meter

    
    @property
    def tera_watts_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__tera_watts_per_cubic_meter != None:
            return self.__tera_watts_per_cubic_meter
        self.__tera_watts_per_cubic_meter = self.__convert_from_base(PowerDensityUnits.TeraWattPerCubicMeter)
        return self.__tera_watts_per_cubic_meter

    
    @property
    def pico_watts_per_cubic_inch(self) -> float:
        """
        
        """
        if self.__pico_watts_per_cubic_inch != None:
            return self.__pico_watts_per_cubic_inch
        self.__pico_watts_per_cubic_inch = self.__convert_from_base(PowerDensityUnits.PicoWattPerCubicInch)
        return self.__pico_watts_per_cubic_inch

    
    @property
    def nano_watts_per_cubic_inch(self) -> float:
        """
        
        """
        if self.__nano_watts_per_cubic_inch != None:
            return self.__nano_watts_per_cubic_inch
        self.__nano_watts_per_cubic_inch = self.__convert_from_base(PowerDensityUnits.NanoWattPerCubicInch)
        return self.__nano_watts_per_cubic_inch

    
    @property
    def micro_watts_per_cubic_inch(self) -> float:
        """
        
        """
        if self.__micro_watts_per_cubic_inch != None:
            return self.__micro_watts_per_cubic_inch
        self.__micro_watts_per_cubic_inch = self.__convert_from_base(PowerDensityUnits.MicroWattPerCubicInch)
        return self.__micro_watts_per_cubic_inch

    
    @property
    def milli_watts_per_cubic_inch(self) -> float:
        """
        
        """
        if self.__milli_watts_per_cubic_inch != None:
            return self.__milli_watts_per_cubic_inch
        self.__milli_watts_per_cubic_inch = self.__convert_from_base(PowerDensityUnits.MilliWattPerCubicInch)
        return self.__milli_watts_per_cubic_inch

    
    @property
    def deci_watts_per_cubic_inch(self) -> float:
        """
        
        """
        if self.__deci_watts_per_cubic_inch != None:
            return self.__deci_watts_per_cubic_inch
        self.__deci_watts_per_cubic_inch = self.__convert_from_base(PowerDensityUnits.DeciWattPerCubicInch)
        return self.__deci_watts_per_cubic_inch

    
    @property
    def deca_watts_per_cubic_inch(self) -> float:
        """
        
        """
        if self.__deca_watts_per_cubic_inch != None:
            return self.__deca_watts_per_cubic_inch
        self.__deca_watts_per_cubic_inch = self.__convert_from_base(PowerDensityUnits.DecaWattPerCubicInch)
        return self.__deca_watts_per_cubic_inch

    
    @property
    def kilo_watts_per_cubic_inch(self) -> float:
        """
        
        """
        if self.__kilo_watts_per_cubic_inch != None:
            return self.__kilo_watts_per_cubic_inch
        self.__kilo_watts_per_cubic_inch = self.__convert_from_base(PowerDensityUnits.KiloWattPerCubicInch)
        return self.__kilo_watts_per_cubic_inch

    
    @property
    def mega_watts_per_cubic_inch(self) -> float:
        """
        
        """
        if self.__mega_watts_per_cubic_inch != None:
            return self.__mega_watts_per_cubic_inch
        self.__mega_watts_per_cubic_inch = self.__convert_from_base(PowerDensityUnits.MegaWattPerCubicInch)
        return self.__mega_watts_per_cubic_inch

    
    @property
    def giga_watts_per_cubic_inch(self) -> float:
        """
        
        """
        if self.__giga_watts_per_cubic_inch != None:
            return self.__giga_watts_per_cubic_inch
        self.__giga_watts_per_cubic_inch = self.__convert_from_base(PowerDensityUnits.GigaWattPerCubicInch)
        return self.__giga_watts_per_cubic_inch

    
    @property
    def tera_watts_per_cubic_inch(self) -> float:
        """
        
        """
        if self.__tera_watts_per_cubic_inch != None:
            return self.__tera_watts_per_cubic_inch
        self.__tera_watts_per_cubic_inch = self.__convert_from_base(PowerDensityUnits.TeraWattPerCubicInch)
        return self.__tera_watts_per_cubic_inch

    
    @property
    def pico_watts_per_cubic_foot(self) -> float:
        """
        
        """
        if self.__pico_watts_per_cubic_foot != None:
            return self.__pico_watts_per_cubic_foot
        self.__pico_watts_per_cubic_foot = self.__convert_from_base(PowerDensityUnits.PicoWattPerCubicFoot)
        return self.__pico_watts_per_cubic_foot

    
    @property
    def nano_watts_per_cubic_foot(self) -> float:
        """
        
        """
        if self.__nano_watts_per_cubic_foot != None:
            return self.__nano_watts_per_cubic_foot
        self.__nano_watts_per_cubic_foot = self.__convert_from_base(PowerDensityUnits.NanoWattPerCubicFoot)
        return self.__nano_watts_per_cubic_foot

    
    @property
    def micro_watts_per_cubic_foot(self) -> float:
        """
        
        """
        if self.__micro_watts_per_cubic_foot != None:
            return self.__micro_watts_per_cubic_foot
        self.__micro_watts_per_cubic_foot = self.__convert_from_base(PowerDensityUnits.MicroWattPerCubicFoot)
        return self.__micro_watts_per_cubic_foot

    
    @property
    def milli_watts_per_cubic_foot(self) -> float:
        """
        
        """
        if self.__milli_watts_per_cubic_foot != None:
            return self.__milli_watts_per_cubic_foot
        self.__milli_watts_per_cubic_foot = self.__convert_from_base(PowerDensityUnits.MilliWattPerCubicFoot)
        return self.__milli_watts_per_cubic_foot

    
    @property
    def deci_watts_per_cubic_foot(self) -> float:
        """
        
        """
        if self.__deci_watts_per_cubic_foot != None:
            return self.__deci_watts_per_cubic_foot
        self.__deci_watts_per_cubic_foot = self.__convert_from_base(PowerDensityUnits.DeciWattPerCubicFoot)
        return self.__deci_watts_per_cubic_foot

    
    @property
    def deca_watts_per_cubic_foot(self) -> float:
        """
        
        """
        if self.__deca_watts_per_cubic_foot != None:
            return self.__deca_watts_per_cubic_foot
        self.__deca_watts_per_cubic_foot = self.__convert_from_base(PowerDensityUnits.DecaWattPerCubicFoot)
        return self.__deca_watts_per_cubic_foot

    
    @property
    def kilo_watts_per_cubic_foot(self) -> float:
        """
        
        """
        if self.__kilo_watts_per_cubic_foot != None:
            return self.__kilo_watts_per_cubic_foot
        self.__kilo_watts_per_cubic_foot = self.__convert_from_base(PowerDensityUnits.KiloWattPerCubicFoot)
        return self.__kilo_watts_per_cubic_foot

    
    @property
    def mega_watts_per_cubic_foot(self) -> float:
        """
        
        """
        if self.__mega_watts_per_cubic_foot != None:
            return self.__mega_watts_per_cubic_foot
        self.__mega_watts_per_cubic_foot = self.__convert_from_base(PowerDensityUnits.MegaWattPerCubicFoot)
        return self.__mega_watts_per_cubic_foot

    
    @property
    def giga_watts_per_cubic_foot(self) -> float:
        """
        
        """
        if self.__giga_watts_per_cubic_foot != None:
            return self.__giga_watts_per_cubic_foot
        self.__giga_watts_per_cubic_foot = self.__convert_from_base(PowerDensityUnits.GigaWattPerCubicFoot)
        return self.__giga_watts_per_cubic_foot

    
    @property
    def tera_watts_per_cubic_foot(self) -> float:
        """
        
        """
        if self.__tera_watts_per_cubic_foot != None:
            return self.__tera_watts_per_cubic_foot
        self.__tera_watts_per_cubic_foot = self.__convert_from_base(PowerDensityUnits.TeraWattPerCubicFoot)
        return self.__tera_watts_per_cubic_foot

    
    @property
    def pico_watts_per_liter(self) -> float:
        """
        
        """
        if self.__pico_watts_per_liter != None:
            return self.__pico_watts_per_liter
        self.__pico_watts_per_liter = self.__convert_from_base(PowerDensityUnits.PicoWattPerLiter)
        return self.__pico_watts_per_liter

    
    @property
    def nano_watts_per_liter(self) -> float:
        """
        
        """
        if self.__nano_watts_per_liter != None:
            return self.__nano_watts_per_liter
        self.__nano_watts_per_liter = self.__convert_from_base(PowerDensityUnits.NanoWattPerLiter)
        return self.__nano_watts_per_liter

    
    @property
    def micro_watts_per_liter(self) -> float:
        """
        
        """
        if self.__micro_watts_per_liter != None:
            return self.__micro_watts_per_liter
        self.__micro_watts_per_liter = self.__convert_from_base(PowerDensityUnits.MicroWattPerLiter)
        return self.__micro_watts_per_liter

    
    @property
    def milli_watts_per_liter(self) -> float:
        """
        
        """
        if self.__milli_watts_per_liter != None:
            return self.__milli_watts_per_liter
        self.__milli_watts_per_liter = self.__convert_from_base(PowerDensityUnits.MilliWattPerLiter)
        return self.__milli_watts_per_liter

    
    @property
    def deci_watts_per_liter(self) -> float:
        """
        
        """
        if self.__deci_watts_per_liter != None:
            return self.__deci_watts_per_liter
        self.__deci_watts_per_liter = self.__convert_from_base(PowerDensityUnits.DeciWattPerLiter)
        return self.__deci_watts_per_liter

    
    @property
    def deca_watts_per_liter(self) -> float:
        """
        
        """
        if self.__deca_watts_per_liter != None:
            return self.__deca_watts_per_liter
        self.__deca_watts_per_liter = self.__convert_from_base(PowerDensityUnits.DecaWattPerLiter)
        return self.__deca_watts_per_liter

    
    @property
    def kilo_watts_per_liter(self) -> float:
        """
        
        """
        if self.__kilo_watts_per_liter != None:
            return self.__kilo_watts_per_liter
        self.__kilo_watts_per_liter = self.__convert_from_base(PowerDensityUnits.KiloWattPerLiter)
        return self.__kilo_watts_per_liter

    
    @property
    def mega_watts_per_liter(self) -> float:
        """
        
        """
        if self.__mega_watts_per_liter != None:
            return self.__mega_watts_per_liter
        self.__mega_watts_per_liter = self.__convert_from_base(PowerDensityUnits.MegaWattPerLiter)
        return self.__mega_watts_per_liter

    
    @property
    def giga_watts_per_liter(self) -> float:
        """
        
        """
        if self.__giga_watts_per_liter != None:
            return self.__giga_watts_per_liter
        self.__giga_watts_per_liter = self.__convert_from_base(PowerDensityUnits.GigaWattPerLiter)
        return self.__giga_watts_per_liter

    
    @property
    def tera_watts_per_liter(self) -> float:
        """
        
        """
        if self.__tera_watts_per_liter != None:
            return self.__tera_watts_per_liter
        self.__tera_watts_per_liter = self.__convert_from_base(PowerDensityUnits.TeraWattPerLiter)
        return self.__tera_watts_per_liter

    
    def to_string(self, unit: PowerDensityUnits = PowerDensityUnits.WattPerCubicMeter) -> string:
        """
        Format the PowerDensity to string.
        Note! the default format for PowerDensity is WattPerCubicMeter.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == PowerDensityUnits.WattPerCubicMeter:
            return f"""{self.watts_per_cubic_meter} W/m³"""
        
        if unit == PowerDensityUnits.WattPerCubicInch:
            return f"""{self.watts_per_cubic_inch} W/in³"""
        
        if unit == PowerDensityUnits.WattPerCubicFoot:
            return f"""{self.watts_per_cubic_foot} W/ft³"""
        
        if unit == PowerDensityUnits.WattPerLiter:
            return f"""{self.watts_per_liter} W/l"""
        
        if unit == PowerDensityUnits.PicoWattPerCubicMeter:
            return f"""{self.pico_watts_per_cubic_meter} """
        
        if unit == PowerDensityUnits.NanoWattPerCubicMeter:
            return f"""{self.nano_watts_per_cubic_meter} """
        
        if unit == PowerDensityUnits.MicroWattPerCubicMeter:
            return f"""{self.micro_watts_per_cubic_meter} """
        
        if unit == PowerDensityUnits.MilliWattPerCubicMeter:
            return f"""{self.milli_watts_per_cubic_meter} """
        
        if unit == PowerDensityUnits.DeciWattPerCubicMeter:
            return f"""{self.deci_watts_per_cubic_meter} """
        
        if unit == PowerDensityUnits.DecaWattPerCubicMeter:
            return f"""{self.deca_watts_per_cubic_meter} """
        
        if unit == PowerDensityUnits.KiloWattPerCubicMeter:
            return f"""{self.kilo_watts_per_cubic_meter} """
        
        if unit == PowerDensityUnits.MegaWattPerCubicMeter:
            return f"""{self.mega_watts_per_cubic_meter} """
        
        if unit == PowerDensityUnits.GigaWattPerCubicMeter:
            return f"""{self.giga_watts_per_cubic_meter} """
        
        if unit == PowerDensityUnits.TeraWattPerCubicMeter:
            return f"""{self.tera_watts_per_cubic_meter} """
        
        if unit == PowerDensityUnits.PicoWattPerCubicInch:
            return f"""{self.pico_watts_per_cubic_inch} """
        
        if unit == PowerDensityUnits.NanoWattPerCubicInch:
            return f"""{self.nano_watts_per_cubic_inch} """
        
        if unit == PowerDensityUnits.MicroWattPerCubicInch:
            return f"""{self.micro_watts_per_cubic_inch} """
        
        if unit == PowerDensityUnits.MilliWattPerCubicInch:
            return f"""{self.milli_watts_per_cubic_inch} """
        
        if unit == PowerDensityUnits.DeciWattPerCubicInch:
            return f"""{self.deci_watts_per_cubic_inch} """
        
        if unit == PowerDensityUnits.DecaWattPerCubicInch:
            return f"""{self.deca_watts_per_cubic_inch} """
        
        if unit == PowerDensityUnits.KiloWattPerCubicInch:
            return f"""{self.kilo_watts_per_cubic_inch} """
        
        if unit == PowerDensityUnits.MegaWattPerCubicInch:
            return f"""{self.mega_watts_per_cubic_inch} """
        
        if unit == PowerDensityUnits.GigaWattPerCubicInch:
            return f"""{self.giga_watts_per_cubic_inch} """
        
        if unit == PowerDensityUnits.TeraWattPerCubicInch:
            return f"""{self.tera_watts_per_cubic_inch} """
        
        if unit == PowerDensityUnits.PicoWattPerCubicFoot:
            return f"""{self.pico_watts_per_cubic_foot} """
        
        if unit == PowerDensityUnits.NanoWattPerCubicFoot:
            return f"""{self.nano_watts_per_cubic_foot} """
        
        if unit == PowerDensityUnits.MicroWattPerCubicFoot:
            return f"""{self.micro_watts_per_cubic_foot} """
        
        if unit == PowerDensityUnits.MilliWattPerCubicFoot:
            return f"""{self.milli_watts_per_cubic_foot} """
        
        if unit == PowerDensityUnits.DeciWattPerCubicFoot:
            return f"""{self.deci_watts_per_cubic_foot} """
        
        if unit == PowerDensityUnits.DecaWattPerCubicFoot:
            return f"""{self.deca_watts_per_cubic_foot} """
        
        if unit == PowerDensityUnits.KiloWattPerCubicFoot:
            return f"""{self.kilo_watts_per_cubic_foot} """
        
        if unit == PowerDensityUnits.MegaWattPerCubicFoot:
            return f"""{self.mega_watts_per_cubic_foot} """
        
        if unit == PowerDensityUnits.GigaWattPerCubicFoot:
            return f"""{self.giga_watts_per_cubic_foot} """
        
        if unit == PowerDensityUnits.TeraWattPerCubicFoot:
            return f"""{self.tera_watts_per_cubic_foot} """
        
        if unit == PowerDensityUnits.PicoWattPerLiter:
            return f"""{self.pico_watts_per_liter} """
        
        if unit == PowerDensityUnits.NanoWattPerLiter:
            return f"""{self.nano_watts_per_liter} """
        
        if unit == PowerDensityUnits.MicroWattPerLiter:
            return f"""{self.micro_watts_per_liter} """
        
        if unit == PowerDensityUnits.MilliWattPerLiter:
            return f"""{self.milli_watts_per_liter} """
        
        if unit == PowerDensityUnits.DeciWattPerLiter:
            return f"""{self.deci_watts_per_liter} """
        
        if unit == PowerDensityUnits.DecaWattPerLiter:
            return f"""{self.deca_watts_per_liter} """
        
        if unit == PowerDensityUnits.KiloWattPerLiter:
            return f"""{self.kilo_watts_per_liter} """
        
        if unit == PowerDensityUnits.MegaWattPerLiter:
            return f"""{self.mega_watts_per_liter} """
        
        if unit == PowerDensityUnits.GigaWattPerLiter:
            return f"""{self.giga_watts_per_liter} """
        
        if unit == PowerDensityUnits.TeraWattPerLiter:
            return f"""{self.tera_watts_per_liter} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: PowerDensityUnits = PowerDensityUnits.WattPerCubicMeter) -> string:
        """
        Get PowerDensity unit abbreviation.
        Note! the default abbreviation for PowerDensity is WattPerCubicMeter.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == PowerDensityUnits.WattPerCubicMeter:
            return """W/m³"""
        
        if unit_abbreviation == PowerDensityUnits.WattPerCubicInch:
            return """W/in³"""
        
        if unit_abbreviation == PowerDensityUnits.WattPerCubicFoot:
            return """W/ft³"""
        
        if unit_abbreviation == PowerDensityUnits.WattPerLiter:
            return """W/l"""
        
        if unit_abbreviation == PowerDensityUnits.PicoWattPerCubicMeter:
            return """"""
        
        if unit_abbreviation == PowerDensityUnits.NanoWattPerCubicMeter:
            return """"""
        
        if unit_abbreviation == PowerDensityUnits.MicroWattPerCubicMeter:
            return """"""
        
        if unit_abbreviation == PowerDensityUnits.MilliWattPerCubicMeter:
            return """"""
        
        if unit_abbreviation == PowerDensityUnits.DeciWattPerCubicMeter:
            return """"""
        
        if unit_abbreviation == PowerDensityUnits.DecaWattPerCubicMeter:
            return """"""
        
        if unit_abbreviation == PowerDensityUnits.KiloWattPerCubicMeter:
            return """"""
        
        if unit_abbreviation == PowerDensityUnits.MegaWattPerCubicMeter:
            return """"""
        
        if unit_abbreviation == PowerDensityUnits.GigaWattPerCubicMeter:
            return """"""
        
        if unit_abbreviation == PowerDensityUnits.TeraWattPerCubicMeter:
            return """"""
        
        if unit_abbreviation == PowerDensityUnits.PicoWattPerCubicInch:
            return """"""
        
        if unit_abbreviation == PowerDensityUnits.NanoWattPerCubicInch:
            return """"""
        
        if unit_abbreviation == PowerDensityUnits.MicroWattPerCubicInch:
            return """"""
        
        if unit_abbreviation == PowerDensityUnits.MilliWattPerCubicInch:
            return """"""
        
        if unit_abbreviation == PowerDensityUnits.DeciWattPerCubicInch:
            return """"""
        
        if unit_abbreviation == PowerDensityUnits.DecaWattPerCubicInch:
            return """"""
        
        if unit_abbreviation == PowerDensityUnits.KiloWattPerCubicInch:
            return """"""
        
        if unit_abbreviation == PowerDensityUnits.MegaWattPerCubicInch:
            return """"""
        
        if unit_abbreviation == PowerDensityUnits.GigaWattPerCubicInch:
            return """"""
        
        if unit_abbreviation == PowerDensityUnits.TeraWattPerCubicInch:
            return """"""
        
        if unit_abbreviation == PowerDensityUnits.PicoWattPerCubicFoot:
            return """"""
        
        if unit_abbreviation == PowerDensityUnits.NanoWattPerCubicFoot:
            return """"""
        
        if unit_abbreviation == PowerDensityUnits.MicroWattPerCubicFoot:
            return """"""
        
        if unit_abbreviation == PowerDensityUnits.MilliWattPerCubicFoot:
            return """"""
        
        if unit_abbreviation == PowerDensityUnits.DeciWattPerCubicFoot:
            return """"""
        
        if unit_abbreviation == PowerDensityUnits.DecaWattPerCubicFoot:
            return """"""
        
        if unit_abbreviation == PowerDensityUnits.KiloWattPerCubicFoot:
            return """"""
        
        if unit_abbreviation == PowerDensityUnits.MegaWattPerCubicFoot:
            return """"""
        
        if unit_abbreviation == PowerDensityUnits.GigaWattPerCubicFoot:
            return """"""
        
        if unit_abbreviation == PowerDensityUnits.TeraWattPerCubicFoot:
            return """"""
        
        if unit_abbreviation == PowerDensityUnits.PicoWattPerLiter:
            return """"""
        
        if unit_abbreviation == PowerDensityUnits.NanoWattPerLiter:
            return """"""
        
        if unit_abbreviation == PowerDensityUnits.MicroWattPerLiter:
            return """"""
        
        if unit_abbreviation == PowerDensityUnits.MilliWattPerLiter:
            return """"""
        
        if unit_abbreviation == PowerDensityUnits.DeciWattPerLiter:
            return """"""
        
        if unit_abbreviation == PowerDensityUnits.DecaWattPerLiter:
            return """"""
        
        if unit_abbreviation == PowerDensityUnits.KiloWattPerLiter:
            return """"""
        
        if unit_abbreviation == PowerDensityUnits.MegaWattPerLiter:
            return """"""
        
        if unit_abbreviation == PowerDensityUnits.GigaWattPerLiter:
            return """"""
        
        if unit_abbreviation == PowerDensityUnits.TeraWattPerLiter:
            return """"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, PowerDensity):
            raise TypeError("unsupported operand type(s) for +: 'PowerDensity' and '{}'".format(type(other).__name__))
        return PowerDensity(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, PowerDensity):
            raise TypeError("unsupported operand type(s) for *: 'PowerDensity' and '{}'".format(type(other).__name__))
        return PowerDensity(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, PowerDensity):
            raise TypeError("unsupported operand type(s) for -: 'PowerDensity' and '{}'".format(type(other).__name__))
        return PowerDensity(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, PowerDensity):
            raise TypeError("unsupported operand type(s) for /: 'PowerDensity' and '{}'".format(type(other).__name__))
        return PowerDensity(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, PowerDensity):
            raise TypeError("unsupported operand type(s) for %: 'PowerDensity' and '{}'".format(type(other).__name__))
        return PowerDensity(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, PowerDensity):
            raise TypeError("unsupported operand type(s) for **: 'PowerDensity' and '{}'".format(type(other).__name__))
        return PowerDensity(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, PowerDensity):
            raise TypeError("unsupported operand type(s) for ==: 'PowerDensity' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, PowerDensity):
            raise TypeError("unsupported operand type(s) for <: 'PowerDensity' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, PowerDensity):
            raise TypeError("unsupported operand type(s) for >: 'PowerDensity' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, PowerDensity):
            raise TypeError("unsupported operand type(s) for <=: 'PowerDensity' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, PowerDensity):
            raise TypeError("unsupported operand type(s) for >=: 'PowerDensity' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value
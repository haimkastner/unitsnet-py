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
        
        PicowattPerCubicMeter = 'picowatt_per_cubic_meter'
        """
            
        """
        
        NanowattPerCubicMeter = 'nanowatt_per_cubic_meter'
        """
            
        """
        
        MicrowattPerCubicMeter = 'microwatt_per_cubic_meter'
        """
            
        """
        
        MilliwattPerCubicMeter = 'milliwatt_per_cubic_meter'
        """
            
        """
        
        DeciwattPerCubicMeter = 'deciwatt_per_cubic_meter'
        """
            
        """
        
        DecawattPerCubicMeter = 'decawatt_per_cubic_meter'
        """
            
        """
        
        KilowattPerCubicMeter = 'kilowatt_per_cubic_meter'
        """
            
        """
        
        MegawattPerCubicMeter = 'megawatt_per_cubic_meter'
        """
            
        """
        
        GigawattPerCubicMeter = 'gigawatt_per_cubic_meter'
        """
            
        """
        
        TerawattPerCubicMeter = 'terawatt_per_cubic_meter'
        """
            
        """
        
        PicowattPerCubicInch = 'picowatt_per_cubic_inch'
        """
            
        """
        
        NanowattPerCubicInch = 'nanowatt_per_cubic_inch'
        """
            
        """
        
        MicrowattPerCubicInch = 'microwatt_per_cubic_inch'
        """
            
        """
        
        MilliwattPerCubicInch = 'milliwatt_per_cubic_inch'
        """
            
        """
        
        DeciwattPerCubicInch = 'deciwatt_per_cubic_inch'
        """
            
        """
        
        DecawattPerCubicInch = 'decawatt_per_cubic_inch'
        """
            
        """
        
        KilowattPerCubicInch = 'kilowatt_per_cubic_inch'
        """
            
        """
        
        MegawattPerCubicInch = 'megawatt_per_cubic_inch'
        """
            
        """
        
        GigawattPerCubicInch = 'gigawatt_per_cubic_inch'
        """
            
        """
        
        TerawattPerCubicInch = 'terawatt_per_cubic_inch'
        """
            
        """
        
        PicowattPerCubicFoot = 'picowatt_per_cubic_foot'
        """
            
        """
        
        NanowattPerCubicFoot = 'nanowatt_per_cubic_foot'
        """
            
        """
        
        MicrowattPerCubicFoot = 'microwatt_per_cubic_foot'
        """
            
        """
        
        MilliwattPerCubicFoot = 'milliwatt_per_cubic_foot'
        """
            
        """
        
        DeciwattPerCubicFoot = 'deciwatt_per_cubic_foot'
        """
            
        """
        
        DecawattPerCubicFoot = 'decawatt_per_cubic_foot'
        """
            
        """
        
        KilowattPerCubicFoot = 'kilowatt_per_cubic_foot'
        """
            
        """
        
        MegawattPerCubicFoot = 'megawatt_per_cubic_foot'
        """
            
        """
        
        GigawattPerCubicFoot = 'gigawatt_per_cubic_foot'
        """
            
        """
        
        TerawattPerCubicFoot = 'terawatt_per_cubic_foot'
        """
            
        """
        
        PicowattPerLiter = 'picowatt_per_liter'
        """
            
        """
        
        NanowattPerLiter = 'nanowatt_per_liter'
        """
            
        """
        
        MicrowattPerLiter = 'microwatt_per_liter'
        """
            
        """
        
        MilliwattPerLiter = 'milliwatt_per_liter'
        """
            
        """
        
        DeciwattPerLiter = 'deciwatt_per_liter'
        """
            
        """
        
        DecawattPerLiter = 'decawatt_per_liter'
        """
            
        """
        
        KilowattPerLiter = 'kilowatt_per_liter'
        """
            
        """
        
        MegawattPerLiter = 'megawatt_per_liter'
        """
            
        """
        
        GigawattPerLiter = 'gigawatt_per_liter'
        """
            
        """
        
        TerawattPerLiter = 'terawatt_per_liter'
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
        
        self.__picowatts_per_cubic_meter = None
        
        self.__nanowatts_per_cubic_meter = None
        
        self.__microwatts_per_cubic_meter = None
        
        self.__milliwatts_per_cubic_meter = None
        
        self.__deciwatts_per_cubic_meter = None
        
        self.__decawatts_per_cubic_meter = None
        
        self.__kilowatts_per_cubic_meter = None
        
        self.__megawatts_per_cubic_meter = None
        
        self.__gigawatts_per_cubic_meter = None
        
        self.__terawatts_per_cubic_meter = None
        
        self.__picowatts_per_cubic_inch = None
        
        self.__nanowatts_per_cubic_inch = None
        
        self.__microwatts_per_cubic_inch = None
        
        self.__milliwatts_per_cubic_inch = None
        
        self.__deciwatts_per_cubic_inch = None
        
        self.__decawatts_per_cubic_inch = None
        
        self.__kilowatts_per_cubic_inch = None
        
        self.__megawatts_per_cubic_inch = None
        
        self.__gigawatts_per_cubic_inch = None
        
        self.__terawatts_per_cubic_inch = None
        
        self.__picowatts_per_cubic_foot = None
        
        self.__nanowatts_per_cubic_foot = None
        
        self.__microwatts_per_cubic_foot = None
        
        self.__milliwatts_per_cubic_foot = None
        
        self.__deciwatts_per_cubic_foot = None
        
        self.__decawatts_per_cubic_foot = None
        
        self.__kilowatts_per_cubic_foot = None
        
        self.__megawatts_per_cubic_foot = None
        
        self.__gigawatts_per_cubic_foot = None
        
        self.__terawatts_per_cubic_foot = None
        
        self.__picowatts_per_liter = None
        
        self.__nanowatts_per_liter = None
        
        self.__microwatts_per_liter = None
        
        self.__milliwatts_per_liter = None
        
        self.__deciwatts_per_liter = None
        
        self.__decawatts_per_liter = None
        
        self.__kilowatts_per_liter = None
        
        self.__megawatts_per_liter = None
        
        self.__gigawatts_per_liter = None
        
        self.__terawatts_per_liter = None
        

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
        
        if from_unit == PowerDensityUnits.PicowattPerCubicMeter:
            return ((value) / 1e-12)
        
        if from_unit == PowerDensityUnits.NanowattPerCubicMeter:
            return ((value) / 1e-09)
        
        if from_unit == PowerDensityUnits.MicrowattPerCubicMeter:
            return ((value) / 1e-06)
        
        if from_unit == PowerDensityUnits.MilliwattPerCubicMeter:
            return ((value) / 0.001)
        
        if from_unit == PowerDensityUnits.DeciwattPerCubicMeter:
            return ((value) / 0.1)
        
        if from_unit == PowerDensityUnits.DecawattPerCubicMeter:
            return ((value) / 10.0)
        
        if from_unit == PowerDensityUnits.KilowattPerCubicMeter:
            return ((value) / 1000.0)
        
        if from_unit == PowerDensityUnits.MegawattPerCubicMeter:
            return ((value) / 1000000.0)
        
        if from_unit == PowerDensityUnits.GigawattPerCubicMeter:
            return ((value) / 1000000000.0)
        
        if from_unit == PowerDensityUnits.TerawattPerCubicMeter:
            return ((value) / 1000000000000.0)
        
        if from_unit == PowerDensityUnits.PicowattPerCubicInch:
            return ((value / 6.102374409473228e4) / 1e-12)
        
        if from_unit == PowerDensityUnits.NanowattPerCubicInch:
            return ((value / 6.102374409473228e4) / 1e-09)
        
        if from_unit == PowerDensityUnits.MicrowattPerCubicInch:
            return ((value / 6.102374409473228e4) / 1e-06)
        
        if from_unit == PowerDensityUnits.MilliwattPerCubicInch:
            return ((value / 6.102374409473228e4) / 0.001)
        
        if from_unit == PowerDensityUnits.DeciwattPerCubicInch:
            return ((value / 6.102374409473228e4) / 0.1)
        
        if from_unit == PowerDensityUnits.DecawattPerCubicInch:
            return ((value / 6.102374409473228e4) / 10.0)
        
        if from_unit == PowerDensityUnits.KilowattPerCubicInch:
            return ((value / 6.102374409473228e4) / 1000.0)
        
        if from_unit == PowerDensityUnits.MegawattPerCubicInch:
            return ((value / 6.102374409473228e4) / 1000000.0)
        
        if from_unit == PowerDensityUnits.GigawattPerCubicInch:
            return ((value / 6.102374409473228e4) / 1000000000.0)
        
        if from_unit == PowerDensityUnits.TerawattPerCubicInch:
            return ((value / 6.102374409473228e4) / 1000000000000.0)
        
        if from_unit == PowerDensityUnits.PicowattPerCubicFoot:
            return ((value / 3.531466672148859e1) / 1e-12)
        
        if from_unit == PowerDensityUnits.NanowattPerCubicFoot:
            return ((value / 3.531466672148859e1) / 1e-09)
        
        if from_unit == PowerDensityUnits.MicrowattPerCubicFoot:
            return ((value / 3.531466672148859e1) / 1e-06)
        
        if from_unit == PowerDensityUnits.MilliwattPerCubicFoot:
            return ((value / 3.531466672148859e1) / 0.001)
        
        if from_unit == PowerDensityUnits.DeciwattPerCubicFoot:
            return ((value / 3.531466672148859e1) / 0.1)
        
        if from_unit == PowerDensityUnits.DecawattPerCubicFoot:
            return ((value / 3.531466672148859e1) / 10.0)
        
        if from_unit == PowerDensityUnits.KilowattPerCubicFoot:
            return ((value / 3.531466672148859e1) / 1000.0)
        
        if from_unit == PowerDensityUnits.MegawattPerCubicFoot:
            return ((value / 3.531466672148859e1) / 1000000.0)
        
        if from_unit == PowerDensityUnits.GigawattPerCubicFoot:
            return ((value / 3.531466672148859e1) / 1000000000.0)
        
        if from_unit == PowerDensityUnits.TerawattPerCubicFoot:
            return ((value / 3.531466672148859e1) / 1000000000000.0)
        
        if from_unit == PowerDensityUnits.PicowattPerLiter:
            return ((value / 1.0e3) / 1e-12)
        
        if from_unit == PowerDensityUnits.NanowattPerLiter:
            return ((value / 1.0e3) / 1e-09)
        
        if from_unit == PowerDensityUnits.MicrowattPerLiter:
            return ((value / 1.0e3) / 1e-06)
        
        if from_unit == PowerDensityUnits.MilliwattPerLiter:
            return ((value / 1.0e3) / 0.001)
        
        if from_unit == PowerDensityUnits.DeciwattPerLiter:
            return ((value / 1.0e3) / 0.1)
        
        if from_unit == PowerDensityUnits.DecawattPerLiter:
            return ((value / 1.0e3) / 10.0)
        
        if from_unit == PowerDensityUnits.KilowattPerLiter:
            return ((value / 1.0e3) / 1000.0)
        
        if from_unit == PowerDensityUnits.MegawattPerLiter:
            return ((value / 1.0e3) / 1000000.0)
        
        if from_unit == PowerDensityUnits.GigawattPerLiter:
            return ((value / 1.0e3) / 1000000000.0)
        
        if from_unit == PowerDensityUnits.TerawattPerLiter:
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
        
        if to_unit == PowerDensityUnits.PicowattPerCubicMeter:
            return ((value) * 1e-12)
        
        if to_unit == PowerDensityUnits.NanowattPerCubicMeter:
            return ((value) * 1e-09)
        
        if to_unit == PowerDensityUnits.MicrowattPerCubicMeter:
            return ((value) * 1e-06)
        
        if to_unit == PowerDensityUnits.MilliwattPerCubicMeter:
            return ((value) * 0.001)
        
        if to_unit == PowerDensityUnits.DeciwattPerCubicMeter:
            return ((value) * 0.1)
        
        if to_unit == PowerDensityUnits.DecawattPerCubicMeter:
            return ((value) * 10.0)
        
        if to_unit == PowerDensityUnits.KilowattPerCubicMeter:
            return ((value) * 1000.0)
        
        if to_unit == PowerDensityUnits.MegawattPerCubicMeter:
            return ((value) * 1000000.0)
        
        if to_unit == PowerDensityUnits.GigawattPerCubicMeter:
            return ((value) * 1000000000.0)
        
        if to_unit == PowerDensityUnits.TerawattPerCubicMeter:
            return ((value) * 1000000000000.0)
        
        if to_unit == PowerDensityUnits.PicowattPerCubicInch:
            return ((value * 6.102374409473228e4) * 1e-12)
        
        if to_unit == PowerDensityUnits.NanowattPerCubicInch:
            return ((value * 6.102374409473228e4) * 1e-09)
        
        if to_unit == PowerDensityUnits.MicrowattPerCubicInch:
            return ((value * 6.102374409473228e4) * 1e-06)
        
        if to_unit == PowerDensityUnits.MilliwattPerCubicInch:
            return ((value * 6.102374409473228e4) * 0.001)
        
        if to_unit == PowerDensityUnits.DeciwattPerCubicInch:
            return ((value * 6.102374409473228e4) * 0.1)
        
        if to_unit == PowerDensityUnits.DecawattPerCubicInch:
            return ((value * 6.102374409473228e4) * 10.0)
        
        if to_unit == PowerDensityUnits.KilowattPerCubicInch:
            return ((value * 6.102374409473228e4) * 1000.0)
        
        if to_unit == PowerDensityUnits.MegawattPerCubicInch:
            return ((value * 6.102374409473228e4) * 1000000.0)
        
        if to_unit == PowerDensityUnits.GigawattPerCubicInch:
            return ((value * 6.102374409473228e4) * 1000000000.0)
        
        if to_unit == PowerDensityUnits.TerawattPerCubicInch:
            return ((value * 6.102374409473228e4) * 1000000000000.0)
        
        if to_unit == PowerDensityUnits.PicowattPerCubicFoot:
            return ((value * 3.531466672148859e1) * 1e-12)
        
        if to_unit == PowerDensityUnits.NanowattPerCubicFoot:
            return ((value * 3.531466672148859e1) * 1e-09)
        
        if to_unit == PowerDensityUnits.MicrowattPerCubicFoot:
            return ((value * 3.531466672148859e1) * 1e-06)
        
        if to_unit == PowerDensityUnits.MilliwattPerCubicFoot:
            return ((value * 3.531466672148859e1) * 0.001)
        
        if to_unit == PowerDensityUnits.DeciwattPerCubicFoot:
            return ((value * 3.531466672148859e1) * 0.1)
        
        if to_unit == PowerDensityUnits.DecawattPerCubicFoot:
            return ((value * 3.531466672148859e1) * 10.0)
        
        if to_unit == PowerDensityUnits.KilowattPerCubicFoot:
            return ((value * 3.531466672148859e1) * 1000.0)
        
        if to_unit == PowerDensityUnits.MegawattPerCubicFoot:
            return ((value * 3.531466672148859e1) * 1000000.0)
        
        if to_unit == PowerDensityUnits.GigawattPerCubicFoot:
            return ((value * 3.531466672148859e1) * 1000000000.0)
        
        if to_unit == PowerDensityUnits.TerawattPerCubicFoot:
            return ((value * 3.531466672148859e1) * 1000000000000.0)
        
        if to_unit == PowerDensityUnits.PicowattPerLiter:
            return ((value * 1.0e3) * 1e-12)
        
        if to_unit == PowerDensityUnits.NanowattPerLiter:
            return ((value * 1.0e3) * 1e-09)
        
        if to_unit == PowerDensityUnits.MicrowattPerLiter:
            return ((value * 1.0e3) * 1e-06)
        
        if to_unit == PowerDensityUnits.MilliwattPerLiter:
            return ((value * 1.0e3) * 0.001)
        
        if to_unit == PowerDensityUnits.DeciwattPerLiter:
            return ((value * 1.0e3) * 0.1)
        
        if to_unit == PowerDensityUnits.DecawattPerLiter:
            return ((value * 1.0e3) * 10.0)
        
        if to_unit == PowerDensityUnits.KilowattPerLiter:
            return ((value * 1.0e3) * 1000.0)
        
        if to_unit == PowerDensityUnits.MegawattPerLiter:
            return ((value * 1.0e3) * 1000000.0)
        
        if to_unit == PowerDensityUnits.GigawattPerLiter:
            return ((value * 1.0e3) * 1000000000.0)
        
        if to_unit == PowerDensityUnits.TerawattPerLiter:
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
    def from_picowatts_per_cubic_meter(picowatts_per_cubic_meter: float):
        """
        Create a new instance of PowerDensity from a value in picowatts_per_cubic_meter.

        

        :param meters: The PowerDensity value in picowatts_per_cubic_meter.
        :type picowatts_per_cubic_meter: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(picowatts_per_cubic_meter, PowerDensityUnits.PicowattPerCubicMeter)

    
    @staticmethod
    def from_nanowatts_per_cubic_meter(nanowatts_per_cubic_meter: float):
        """
        Create a new instance of PowerDensity from a value in nanowatts_per_cubic_meter.

        

        :param meters: The PowerDensity value in nanowatts_per_cubic_meter.
        :type nanowatts_per_cubic_meter: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(nanowatts_per_cubic_meter, PowerDensityUnits.NanowattPerCubicMeter)

    
    @staticmethod
    def from_microwatts_per_cubic_meter(microwatts_per_cubic_meter: float):
        """
        Create a new instance of PowerDensity from a value in microwatts_per_cubic_meter.

        

        :param meters: The PowerDensity value in microwatts_per_cubic_meter.
        :type microwatts_per_cubic_meter: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(microwatts_per_cubic_meter, PowerDensityUnits.MicrowattPerCubicMeter)

    
    @staticmethod
    def from_milliwatts_per_cubic_meter(milliwatts_per_cubic_meter: float):
        """
        Create a new instance of PowerDensity from a value in milliwatts_per_cubic_meter.

        

        :param meters: The PowerDensity value in milliwatts_per_cubic_meter.
        :type milliwatts_per_cubic_meter: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(milliwatts_per_cubic_meter, PowerDensityUnits.MilliwattPerCubicMeter)

    
    @staticmethod
    def from_deciwatts_per_cubic_meter(deciwatts_per_cubic_meter: float):
        """
        Create a new instance of PowerDensity from a value in deciwatts_per_cubic_meter.

        

        :param meters: The PowerDensity value in deciwatts_per_cubic_meter.
        :type deciwatts_per_cubic_meter: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(deciwatts_per_cubic_meter, PowerDensityUnits.DeciwattPerCubicMeter)

    
    @staticmethod
    def from_decawatts_per_cubic_meter(decawatts_per_cubic_meter: float):
        """
        Create a new instance of PowerDensity from a value in decawatts_per_cubic_meter.

        

        :param meters: The PowerDensity value in decawatts_per_cubic_meter.
        :type decawatts_per_cubic_meter: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(decawatts_per_cubic_meter, PowerDensityUnits.DecawattPerCubicMeter)

    
    @staticmethod
    def from_kilowatts_per_cubic_meter(kilowatts_per_cubic_meter: float):
        """
        Create a new instance of PowerDensity from a value in kilowatts_per_cubic_meter.

        

        :param meters: The PowerDensity value in kilowatts_per_cubic_meter.
        :type kilowatts_per_cubic_meter: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(kilowatts_per_cubic_meter, PowerDensityUnits.KilowattPerCubicMeter)

    
    @staticmethod
    def from_megawatts_per_cubic_meter(megawatts_per_cubic_meter: float):
        """
        Create a new instance of PowerDensity from a value in megawatts_per_cubic_meter.

        

        :param meters: The PowerDensity value in megawatts_per_cubic_meter.
        :type megawatts_per_cubic_meter: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(megawatts_per_cubic_meter, PowerDensityUnits.MegawattPerCubicMeter)

    
    @staticmethod
    def from_gigawatts_per_cubic_meter(gigawatts_per_cubic_meter: float):
        """
        Create a new instance of PowerDensity from a value in gigawatts_per_cubic_meter.

        

        :param meters: The PowerDensity value in gigawatts_per_cubic_meter.
        :type gigawatts_per_cubic_meter: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(gigawatts_per_cubic_meter, PowerDensityUnits.GigawattPerCubicMeter)

    
    @staticmethod
    def from_terawatts_per_cubic_meter(terawatts_per_cubic_meter: float):
        """
        Create a new instance of PowerDensity from a value in terawatts_per_cubic_meter.

        

        :param meters: The PowerDensity value in terawatts_per_cubic_meter.
        :type terawatts_per_cubic_meter: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(terawatts_per_cubic_meter, PowerDensityUnits.TerawattPerCubicMeter)

    
    @staticmethod
    def from_picowatts_per_cubic_inch(picowatts_per_cubic_inch: float):
        """
        Create a new instance of PowerDensity from a value in picowatts_per_cubic_inch.

        

        :param meters: The PowerDensity value in picowatts_per_cubic_inch.
        :type picowatts_per_cubic_inch: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(picowatts_per_cubic_inch, PowerDensityUnits.PicowattPerCubicInch)

    
    @staticmethod
    def from_nanowatts_per_cubic_inch(nanowatts_per_cubic_inch: float):
        """
        Create a new instance of PowerDensity from a value in nanowatts_per_cubic_inch.

        

        :param meters: The PowerDensity value in nanowatts_per_cubic_inch.
        :type nanowatts_per_cubic_inch: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(nanowatts_per_cubic_inch, PowerDensityUnits.NanowattPerCubicInch)

    
    @staticmethod
    def from_microwatts_per_cubic_inch(microwatts_per_cubic_inch: float):
        """
        Create a new instance of PowerDensity from a value in microwatts_per_cubic_inch.

        

        :param meters: The PowerDensity value in microwatts_per_cubic_inch.
        :type microwatts_per_cubic_inch: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(microwatts_per_cubic_inch, PowerDensityUnits.MicrowattPerCubicInch)

    
    @staticmethod
    def from_milliwatts_per_cubic_inch(milliwatts_per_cubic_inch: float):
        """
        Create a new instance of PowerDensity from a value in milliwatts_per_cubic_inch.

        

        :param meters: The PowerDensity value in milliwatts_per_cubic_inch.
        :type milliwatts_per_cubic_inch: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(milliwatts_per_cubic_inch, PowerDensityUnits.MilliwattPerCubicInch)

    
    @staticmethod
    def from_deciwatts_per_cubic_inch(deciwatts_per_cubic_inch: float):
        """
        Create a new instance of PowerDensity from a value in deciwatts_per_cubic_inch.

        

        :param meters: The PowerDensity value in deciwatts_per_cubic_inch.
        :type deciwatts_per_cubic_inch: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(deciwatts_per_cubic_inch, PowerDensityUnits.DeciwattPerCubicInch)

    
    @staticmethod
    def from_decawatts_per_cubic_inch(decawatts_per_cubic_inch: float):
        """
        Create a new instance of PowerDensity from a value in decawatts_per_cubic_inch.

        

        :param meters: The PowerDensity value in decawatts_per_cubic_inch.
        :type decawatts_per_cubic_inch: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(decawatts_per_cubic_inch, PowerDensityUnits.DecawattPerCubicInch)

    
    @staticmethod
    def from_kilowatts_per_cubic_inch(kilowatts_per_cubic_inch: float):
        """
        Create a new instance of PowerDensity from a value in kilowatts_per_cubic_inch.

        

        :param meters: The PowerDensity value in kilowatts_per_cubic_inch.
        :type kilowatts_per_cubic_inch: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(kilowatts_per_cubic_inch, PowerDensityUnits.KilowattPerCubicInch)

    
    @staticmethod
    def from_megawatts_per_cubic_inch(megawatts_per_cubic_inch: float):
        """
        Create a new instance of PowerDensity from a value in megawatts_per_cubic_inch.

        

        :param meters: The PowerDensity value in megawatts_per_cubic_inch.
        :type megawatts_per_cubic_inch: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(megawatts_per_cubic_inch, PowerDensityUnits.MegawattPerCubicInch)

    
    @staticmethod
    def from_gigawatts_per_cubic_inch(gigawatts_per_cubic_inch: float):
        """
        Create a new instance of PowerDensity from a value in gigawatts_per_cubic_inch.

        

        :param meters: The PowerDensity value in gigawatts_per_cubic_inch.
        :type gigawatts_per_cubic_inch: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(gigawatts_per_cubic_inch, PowerDensityUnits.GigawattPerCubicInch)

    
    @staticmethod
    def from_terawatts_per_cubic_inch(terawatts_per_cubic_inch: float):
        """
        Create a new instance of PowerDensity from a value in terawatts_per_cubic_inch.

        

        :param meters: The PowerDensity value in terawatts_per_cubic_inch.
        :type terawatts_per_cubic_inch: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(terawatts_per_cubic_inch, PowerDensityUnits.TerawattPerCubicInch)

    
    @staticmethod
    def from_picowatts_per_cubic_foot(picowatts_per_cubic_foot: float):
        """
        Create a new instance of PowerDensity from a value in picowatts_per_cubic_foot.

        

        :param meters: The PowerDensity value in picowatts_per_cubic_foot.
        :type picowatts_per_cubic_foot: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(picowatts_per_cubic_foot, PowerDensityUnits.PicowattPerCubicFoot)

    
    @staticmethod
    def from_nanowatts_per_cubic_foot(nanowatts_per_cubic_foot: float):
        """
        Create a new instance of PowerDensity from a value in nanowatts_per_cubic_foot.

        

        :param meters: The PowerDensity value in nanowatts_per_cubic_foot.
        :type nanowatts_per_cubic_foot: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(nanowatts_per_cubic_foot, PowerDensityUnits.NanowattPerCubicFoot)

    
    @staticmethod
    def from_microwatts_per_cubic_foot(microwatts_per_cubic_foot: float):
        """
        Create a new instance of PowerDensity from a value in microwatts_per_cubic_foot.

        

        :param meters: The PowerDensity value in microwatts_per_cubic_foot.
        :type microwatts_per_cubic_foot: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(microwatts_per_cubic_foot, PowerDensityUnits.MicrowattPerCubicFoot)

    
    @staticmethod
    def from_milliwatts_per_cubic_foot(milliwatts_per_cubic_foot: float):
        """
        Create a new instance of PowerDensity from a value in milliwatts_per_cubic_foot.

        

        :param meters: The PowerDensity value in milliwatts_per_cubic_foot.
        :type milliwatts_per_cubic_foot: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(milliwatts_per_cubic_foot, PowerDensityUnits.MilliwattPerCubicFoot)

    
    @staticmethod
    def from_deciwatts_per_cubic_foot(deciwatts_per_cubic_foot: float):
        """
        Create a new instance of PowerDensity from a value in deciwatts_per_cubic_foot.

        

        :param meters: The PowerDensity value in deciwatts_per_cubic_foot.
        :type deciwatts_per_cubic_foot: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(deciwatts_per_cubic_foot, PowerDensityUnits.DeciwattPerCubicFoot)

    
    @staticmethod
    def from_decawatts_per_cubic_foot(decawatts_per_cubic_foot: float):
        """
        Create a new instance of PowerDensity from a value in decawatts_per_cubic_foot.

        

        :param meters: The PowerDensity value in decawatts_per_cubic_foot.
        :type decawatts_per_cubic_foot: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(decawatts_per_cubic_foot, PowerDensityUnits.DecawattPerCubicFoot)

    
    @staticmethod
    def from_kilowatts_per_cubic_foot(kilowatts_per_cubic_foot: float):
        """
        Create a new instance of PowerDensity from a value in kilowatts_per_cubic_foot.

        

        :param meters: The PowerDensity value in kilowatts_per_cubic_foot.
        :type kilowatts_per_cubic_foot: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(kilowatts_per_cubic_foot, PowerDensityUnits.KilowattPerCubicFoot)

    
    @staticmethod
    def from_megawatts_per_cubic_foot(megawatts_per_cubic_foot: float):
        """
        Create a new instance of PowerDensity from a value in megawatts_per_cubic_foot.

        

        :param meters: The PowerDensity value in megawatts_per_cubic_foot.
        :type megawatts_per_cubic_foot: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(megawatts_per_cubic_foot, PowerDensityUnits.MegawattPerCubicFoot)

    
    @staticmethod
    def from_gigawatts_per_cubic_foot(gigawatts_per_cubic_foot: float):
        """
        Create a new instance of PowerDensity from a value in gigawatts_per_cubic_foot.

        

        :param meters: The PowerDensity value in gigawatts_per_cubic_foot.
        :type gigawatts_per_cubic_foot: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(gigawatts_per_cubic_foot, PowerDensityUnits.GigawattPerCubicFoot)

    
    @staticmethod
    def from_terawatts_per_cubic_foot(terawatts_per_cubic_foot: float):
        """
        Create a new instance of PowerDensity from a value in terawatts_per_cubic_foot.

        

        :param meters: The PowerDensity value in terawatts_per_cubic_foot.
        :type terawatts_per_cubic_foot: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(terawatts_per_cubic_foot, PowerDensityUnits.TerawattPerCubicFoot)

    
    @staticmethod
    def from_picowatts_per_liter(picowatts_per_liter: float):
        """
        Create a new instance of PowerDensity from a value in picowatts_per_liter.

        

        :param meters: The PowerDensity value in picowatts_per_liter.
        :type picowatts_per_liter: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(picowatts_per_liter, PowerDensityUnits.PicowattPerLiter)

    
    @staticmethod
    def from_nanowatts_per_liter(nanowatts_per_liter: float):
        """
        Create a new instance of PowerDensity from a value in nanowatts_per_liter.

        

        :param meters: The PowerDensity value in nanowatts_per_liter.
        :type nanowatts_per_liter: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(nanowatts_per_liter, PowerDensityUnits.NanowattPerLiter)

    
    @staticmethod
    def from_microwatts_per_liter(microwatts_per_liter: float):
        """
        Create a new instance of PowerDensity from a value in microwatts_per_liter.

        

        :param meters: The PowerDensity value in microwatts_per_liter.
        :type microwatts_per_liter: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(microwatts_per_liter, PowerDensityUnits.MicrowattPerLiter)

    
    @staticmethod
    def from_milliwatts_per_liter(milliwatts_per_liter: float):
        """
        Create a new instance of PowerDensity from a value in milliwatts_per_liter.

        

        :param meters: The PowerDensity value in milliwatts_per_liter.
        :type milliwatts_per_liter: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(milliwatts_per_liter, PowerDensityUnits.MilliwattPerLiter)

    
    @staticmethod
    def from_deciwatts_per_liter(deciwatts_per_liter: float):
        """
        Create a new instance of PowerDensity from a value in deciwatts_per_liter.

        

        :param meters: The PowerDensity value in deciwatts_per_liter.
        :type deciwatts_per_liter: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(deciwatts_per_liter, PowerDensityUnits.DeciwattPerLiter)

    
    @staticmethod
    def from_decawatts_per_liter(decawatts_per_liter: float):
        """
        Create a new instance of PowerDensity from a value in decawatts_per_liter.

        

        :param meters: The PowerDensity value in decawatts_per_liter.
        :type decawatts_per_liter: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(decawatts_per_liter, PowerDensityUnits.DecawattPerLiter)

    
    @staticmethod
    def from_kilowatts_per_liter(kilowatts_per_liter: float):
        """
        Create a new instance of PowerDensity from a value in kilowatts_per_liter.

        

        :param meters: The PowerDensity value in kilowatts_per_liter.
        :type kilowatts_per_liter: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(kilowatts_per_liter, PowerDensityUnits.KilowattPerLiter)

    
    @staticmethod
    def from_megawatts_per_liter(megawatts_per_liter: float):
        """
        Create a new instance of PowerDensity from a value in megawatts_per_liter.

        

        :param meters: The PowerDensity value in megawatts_per_liter.
        :type megawatts_per_liter: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(megawatts_per_liter, PowerDensityUnits.MegawattPerLiter)

    
    @staticmethod
    def from_gigawatts_per_liter(gigawatts_per_liter: float):
        """
        Create a new instance of PowerDensity from a value in gigawatts_per_liter.

        

        :param meters: The PowerDensity value in gigawatts_per_liter.
        :type gigawatts_per_liter: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(gigawatts_per_liter, PowerDensityUnits.GigawattPerLiter)

    
    @staticmethod
    def from_terawatts_per_liter(terawatts_per_liter: float):
        """
        Create a new instance of PowerDensity from a value in terawatts_per_liter.

        

        :param meters: The PowerDensity value in terawatts_per_liter.
        :type terawatts_per_liter: float
        :return: A new instance of PowerDensity.
        :rtype: PowerDensity
        """
        return PowerDensity(terawatts_per_liter, PowerDensityUnits.TerawattPerLiter)

    
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
    def picowatts_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__picowatts_per_cubic_meter != None:
            return self.__picowatts_per_cubic_meter
        self.__picowatts_per_cubic_meter = self.__convert_from_base(PowerDensityUnits.PicowattPerCubicMeter)
        return self.__picowatts_per_cubic_meter

    
    @property
    def nanowatts_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__nanowatts_per_cubic_meter != None:
            return self.__nanowatts_per_cubic_meter
        self.__nanowatts_per_cubic_meter = self.__convert_from_base(PowerDensityUnits.NanowattPerCubicMeter)
        return self.__nanowatts_per_cubic_meter

    
    @property
    def microwatts_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__microwatts_per_cubic_meter != None:
            return self.__microwatts_per_cubic_meter
        self.__microwatts_per_cubic_meter = self.__convert_from_base(PowerDensityUnits.MicrowattPerCubicMeter)
        return self.__microwatts_per_cubic_meter

    
    @property
    def milliwatts_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__milliwatts_per_cubic_meter != None:
            return self.__milliwatts_per_cubic_meter
        self.__milliwatts_per_cubic_meter = self.__convert_from_base(PowerDensityUnits.MilliwattPerCubicMeter)
        return self.__milliwatts_per_cubic_meter

    
    @property
    def deciwatts_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__deciwatts_per_cubic_meter != None:
            return self.__deciwatts_per_cubic_meter
        self.__deciwatts_per_cubic_meter = self.__convert_from_base(PowerDensityUnits.DeciwattPerCubicMeter)
        return self.__deciwatts_per_cubic_meter

    
    @property
    def decawatts_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__decawatts_per_cubic_meter != None:
            return self.__decawatts_per_cubic_meter
        self.__decawatts_per_cubic_meter = self.__convert_from_base(PowerDensityUnits.DecawattPerCubicMeter)
        return self.__decawatts_per_cubic_meter

    
    @property
    def kilowatts_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__kilowatts_per_cubic_meter != None:
            return self.__kilowatts_per_cubic_meter
        self.__kilowatts_per_cubic_meter = self.__convert_from_base(PowerDensityUnits.KilowattPerCubicMeter)
        return self.__kilowatts_per_cubic_meter

    
    @property
    def megawatts_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__megawatts_per_cubic_meter != None:
            return self.__megawatts_per_cubic_meter
        self.__megawatts_per_cubic_meter = self.__convert_from_base(PowerDensityUnits.MegawattPerCubicMeter)
        return self.__megawatts_per_cubic_meter

    
    @property
    def gigawatts_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__gigawatts_per_cubic_meter != None:
            return self.__gigawatts_per_cubic_meter
        self.__gigawatts_per_cubic_meter = self.__convert_from_base(PowerDensityUnits.GigawattPerCubicMeter)
        return self.__gigawatts_per_cubic_meter

    
    @property
    def terawatts_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__terawatts_per_cubic_meter != None:
            return self.__terawatts_per_cubic_meter
        self.__terawatts_per_cubic_meter = self.__convert_from_base(PowerDensityUnits.TerawattPerCubicMeter)
        return self.__terawatts_per_cubic_meter

    
    @property
    def picowatts_per_cubic_inch(self) -> float:
        """
        
        """
        if self.__picowatts_per_cubic_inch != None:
            return self.__picowatts_per_cubic_inch
        self.__picowatts_per_cubic_inch = self.__convert_from_base(PowerDensityUnits.PicowattPerCubicInch)
        return self.__picowatts_per_cubic_inch

    
    @property
    def nanowatts_per_cubic_inch(self) -> float:
        """
        
        """
        if self.__nanowatts_per_cubic_inch != None:
            return self.__nanowatts_per_cubic_inch
        self.__nanowatts_per_cubic_inch = self.__convert_from_base(PowerDensityUnits.NanowattPerCubicInch)
        return self.__nanowatts_per_cubic_inch

    
    @property
    def microwatts_per_cubic_inch(self) -> float:
        """
        
        """
        if self.__microwatts_per_cubic_inch != None:
            return self.__microwatts_per_cubic_inch
        self.__microwatts_per_cubic_inch = self.__convert_from_base(PowerDensityUnits.MicrowattPerCubicInch)
        return self.__microwatts_per_cubic_inch

    
    @property
    def milliwatts_per_cubic_inch(self) -> float:
        """
        
        """
        if self.__milliwatts_per_cubic_inch != None:
            return self.__milliwatts_per_cubic_inch
        self.__milliwatts_per_cubic_inch = self.__convert_from_base(PowerDensityUnits.MilliwattPerCubicInch)
        return self.__milliwatts_per_cubic_inch

    
    @property
    def deciwatts_per_cubic_inch(self) -> float:
        """
        
        """
        if self.__deciwatts_per_cubic_inch != None:
            return self.__deciwatts_per_cubic_inch
        self.__deciwatts_per_cubic_inch = self.__convert_from_base(PowerDensityUnits.DeciwattPerCubicInch)
        return self.__deciwatts_per_cubic_inch

    
    @property
    def decawatts_per_cubic_inch(self) -> float:
        """
        
        """
        if self.__decawatts_per_cubic_inch != None:
            return self.__decawatts_per_cubic_inch
        self.__decawatts_per_cubic_inch = self.__convert_from_base(PowerDensityUnits.DecawattPerCubicInch)
        return self.__decawatts_per_cubic_inch

    
    @property
    def kilowatts_per_cubic_inch(self) -> float:
        """
        
        """
        if self.__kilowatts_per_cubic_inch != None:
            return self.__kilowatts_per_cubic_inch
        self.__kilowatts_per_cubic_inch = self.__convert_from_base(PowerDensityUnits.KilowattPerCubicInch)
        return self.__kilowatts_per_cubic_inch

    
    @property
    def megawatts_per_cubic_inch(self) -> float:
        """
        
        """
        if self.__megawatts_per_cubic_inch != None:
            return self.__megawatts_per_cubic_inch
        self.__megawatts_per_cubic_inch = self.__convert_from_base(PowerDensityUnits.MegawattPerCubicInch)
        return self.__megawatts_per_cubic_inch

    
    @property
    def gigawatts_per_cubic_inch(self) -> float:
        """
        
        """
        if self.__gigawatts_per_cubic_inch != None:
            return self.__gigawatts_per_cubic_inch
        self.__gigawatts_per_cubic_inch = self.__convert_from_base(PowerDensityUnits.GigawattPerCubicInch)
        return self.__gigawatts_per_cubic_inch

    
    @property
    def terawatts_per_cubic_inch(self) -> float:
        """
        
        """
        if self.__terawatts_per_cubic_inch != None:
            return self.__terawatts_per_cubic_inch
        self.__terawatts_per_cubic_inch = self.__convert_from_base(PowerDensityUnits.TerawattPerCubicInch)
        return self.__terawatts_per_cubic_inch

    
    @property
    def picowatts_per_cubic_foot(self) -> float:
        """
        
        """
        if self.__picowatts_per_cubic_foot != None:
            return self.__picowatts_per_cubic_foot
        self.__picowatts_per_cubic_foot = self.__convert_from_base(PowerDensityUnits.PicowattPerCubicFoot)
        return self.__picowatts_per_cubic_foot

    
    @property
    def nanowatts_per_cubic_foot(self) -> float:
        """
        
        """
        if self.__nanowatts_per_cubic_foot != None:
            return self.__nanowatts_per_cubic_foot
        self.__nanowatts_per_cubic_foot = self.__convert_from_base(PowerDensityUnits.NanowattPerCubicFoot)
        return self.__nanowatts_per_cubic_foot

    
    @property
    def microwatts_per_cubic_foot(self) -> float:
        """
        
        """
        if self.__microwatts_per_cubic_foot != None:
            return self.__microwatts_per_cubic_foot
        self.__microwatts_per_cubic_foot = self.__convert_from_base(PowerDensityUnits.MicrowattPerCubicFoot)
        return self.__microwatts_per_cubic_foot

    
    @property
    def milliwatts_per_cubic_foot(self) -> float:
        """
        
        """
        if self.__milliwatts_per_cubic_foot != None:
            return self.__milliwatts_per_cubic_foot
        self.__milliwatts_per_cubic_foot = self.__convert_from_base(PowerDensityUnits.MilliwattPerCubicFoot)
        return self.__milliwatts_per_cubic_foot

    
    @property
    def deciwatts_per_cubic_foot(self) -> float:
        """
        
        """
        if self.__deciwatts_per_cubic_foot != None:
            return self.__deciwatts_per_cubic_foot
        self.__deciwatts_per_cubic_foot = self.__convert_from_base(PowerDensityUnits.DeciwattPerCubicFoot)
        return self.__deciwatts_per_cubic_foot

    
    @property
    def decawatts_per_cubic_foot(self) -> float:
        """
        
        """
        if self.__decawatts_per_cubic_foot != None:
            return self.__decawatts_per_cubic_foot
        self.__decawatts_per_cubic_foot = self.__convert_from_base(PowerDensityUnits.DecawattPerCubicFoot)
        return self.__decawatts_per_cubic_foot

    
    @property
    def kilowatts_per_cubic_foot(self) -> float:
        """
        
        """
        if self.__kilowatts_per_cubic_foot != None:
            return self.__kilowatts_per_cubic_foot
        self.__kilowatts_per_cubic_foot = self.__convert_from_base(PowerDensityUnits.KilowattPerCubicFoot)
        return self.__kilowatts_per_cubic_foot

    
    @property
    def megawatts_per_cubic_foot(self) -> float:
        """
        
        """
        if self.__megawatts_per_cubic_foot != None:
            return self.__megawatts_per_cubic_foot
        self.__megawatts_per_cubic_foot = self.__convert_from_base(PowerDensityUnits.MegawattPerCubicFoot)
        return self.__megawatts_per_cubic_foot

    
    @property
    def gigawatts_per_cubic_foot(self) -> float:
        """
        
        """
        if self.__gigawatts_per_cubic_foot != None:
            return self.__gigawatts_per_cubic_foot
        self.__gigawatts_per_cubic_foot = self.__convert_from_base(PowerDensityUnits.GigawattPerCubicFoot)
        return self.__gigawatts_per_cubic_foot

    
    @property
    def terawatts_per_cubic_foot(self) -> float:
        """
        
        """
        if self.__terawatts_per_cubic_foot != None:
            return self.__terawatts_per_cubic_foot
        self.__terawatts_per_cubic_foot = self.__convert_from_base(PowerDensityUnits.TerawattPerCubicFoot)
        return self.__terawatts_per_cubic_foot

    
    @property
    def picowatts_per_liter(self) -> float:
        """
        
        """
        if self.__picowatts_per_liter != None:
            return self.__picowatts_per_liter
        self.__picowatts_per_liter = self.__convert_from_base(PowerDensityUnits.PicowattPerLiter)
        return self.__picowatts_per_liter

    
    @property
    def nanowatts_per_liter(self) -> float:
        """
        
        """
        if self.__nanowatts_per_liter != None:
            return self.__nanowatts_per_liter
        self.__nanowatts_per_liter = self.__convert_from_base(PowerDensityUnits.NanowattPerLiter)
        return self.__nanowatts_per_liter

    
    @property
    def microwatts_per_liter(self) -> float:
        """
        
        """
        if self.__microwatts_per_liter != None:
            return self.__microwatts_per_liter
        self.__microwatts_per_liter = self.__convert_from_base(PowerDensityUnits.MicrowattPerLiter)
        return self.__microwatts_per_liter

    
    @property
    def milliwatts_per_liter(self) -> float:
        """
        
        """
        if self.__milliwatts_per_liter != None:
            return self.__milliwatts_per_liter
        self.__milliwatts_per_liter = self.__convert_from_base(PowerDensityUnits.MilliwattPerLiter)
        return self.__milliwatts_per_liter

    
    @property
    def deciwatts_per_liter(self) -> float:
        """
        
        """
        if self.__deciwatts_per_liter != None:
            return self.__deciwatts_per_liter
        self.__deciwatts_per_liter = self.__convert_from_base(PowerDensityUnits.DeciwattPerLiter)
        return self.__deciwatts_per_liter

    
    @property
    def decawatts_per_liter(self) -> float:
        """
        
        """
        if self.__decawatts_per_liter != None:
            return self.__decawatts_per_liter
        self.__decawatts_per_liter = self.__convert_from_base(PowerDensityUnits.DecawattPerLiter)
        return self.__decawatts_per_liter

    
    @property
    def kilowatts_per_liter(self) -> float:
        """
        
        """
        if self.__kilowatts_per_liter != None:
            return self.__kilowatts_per_liter
        self.__kilowatts_per_liter = self.__convert_from_base(PowerDensityUnits.KilowattPerLiter)
        return self.__kilowatts_per_liter

    
    @property
    def megawatts_per_liter(self) -> float:
        """
        
        """
        if self.__megawatts_per_liter != None:
            return self.__megawatts_per_liter
        self.__megawatts_per_liter = self.__convert_from_base(PowerDensityUnits.MegawattPerLiter)
        return self.__megawatts_per_liter

    
    @property
    def gigawatts_per_liter(self) -> float:
        """
        
        """
        if self.__gigawatts_per_liter != None:
            return self.__gigawatts_per_liter
        self.__gigawatts_per_liter = self.__convert_from_base(PowerDensityUnits.GigawattPerLiter)
        return self.__gigawatts_per_liter

    
    @property
    def terawatts_per_liter(self) -> float:
        """
        
        """
        if self.__terawatts_per_liter != None:
            return self.__terawatts_per_liter
        self.__terawatts_per_liter = self.__convert_from_base(PowerDensityUnits.TerawattPerLiter)
        return self.__terawatts_per_liter

    
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
        
        if unit == PowerDensityUnits.PicowattPerCubicMeter:
            return f"""{self.picowatts_per_cubic_meter} """
        
        if unit == PowerDensityUnits.NanowattPerCubicMeter:
            return f"""{self.nanowatts_per_cubic_meter} """
        
        if unit == PowerDensityUnits.MicrowattPerCubicMeter:
            return f"""{self.microwatts_per_cubic_meter} """
        
        if unit == PowerDensityUnits.MilliwattPerCubicMeter:
            return f"""{self.milliwatts_per_cubic_meter} """
        
        if unit == PowerDensityUnits.DeciwattPerCubicMeter:
            return f"""{self.deciwatts_per_cubic_meter} """
        
        if unit == PowerDensityUnits.DecawattPerCubicMeter:
            return f"""{self.decawatts_per_cubic_meter} """
        
        if unit == PowerDensityUnits.KilowattPerCubicMeter:
            return f"""{self.kilowatts_per_cubic_meter} """
        
        if unit == PowerDensityUnits.MegawattPerCubicMeter:
            return f"""{self.megawatts_per_cubic_meter} """
        
        if unit == PowerDensityUnits.GigawattPerCubicMeter:
            return f"""{self.gigawatts_per_cubic_meter} """
        
        if unit == PowerDensityUnits.TerawattPerCubicMeter:
            return f"""{self.terawatts_per_cubic_meter} """
        
        if unit == PowerDensityUnits.PicowattPerCubicInch:
            return f"""{self.picowatts_per_cubic_inch} """
        
        if unit == PowerDensityUnits.NanowattPerCubicInch:
            return f"""{self.nanowatts_per_cubic_inch} """
        
        if unit == PowerDensityUnits.MicrowattPerCubicInch:
            return f"""{self.microwatts_per_cubic_inch} """
        
        if unit == PowerDensityUnits.MilliwattPerCubicInch:
            return f"""{self.milliwatts_per_cubic_inch} """
        
        if unit == PowerDensityUnits.DeciwattPerCubicInch:
            return f"""{self.deciwatts_per_cubic_inch} """
        
        if unit == PowerDensityUnits.DecawattPerCubicInch:
            return f"""{self.decawatts_per_cubic_inch} """
        
        if unit == PowerDensityUnits.KilowattPerCubicInch:
            return f"""{self.kilowatts_per_cubic_inch} """
        
        if unit == PowerDensityUnits.MegawattPerCubicInch:
            return f"""{self.megawatts_per_cubic_inch} """
        
        if unit == PowerDensityUnits.GigawattPerCubicInch:
            return f"""{self.gigawatts_per_cubic_inch} """
        
        if unit == PowerDensityUnits.TerawattPerCubicInch:
            return f"""{self.terawatts_per_cubic_inch} """
        
        if unit == PowerDensityUnits.PicowattPerCubicFoot:
            return f"""{self.picowatts_per_cubic_foot} """
        
        if unit == PowerDensityUnits.NanowattPerCubicFoot:
            return f"""{self.nanowatts_per_cubic_foot} """
        
        if unit == PowerDensityUnits.MicrowattPerCubicFoot:
            return f"""{self.microwatts_per_cubic_foot} """
        
        if unit == PowerDensityUnits.MilliwattPerCubicFoot:
            return f"""{self.milliwatts_per_cubic_foot} """
        
        if unit == PowerDensityUnits.DeciwattPerCubicFoot:
            return f"""{self.deciwatts_per_cubic_foot} """
        
        if unit == PowerDensityUnits.DecawattPerCubicFoot:
            return f"""{self.decawatts_per_cubic_foot} """
        
        if unit == PowerDensityUnits.KilowattPerCubicFoot:
            return f"""{self.kilowatts_per_cubic_foot} """
        
        if unit == PowerDensityUnits.MegawattPerCubicFoot:
            return f"""{self.megawatts_per_cubic_foot} """
        
        if unit == PowerDensityUnits.GigawattPerCubicFoot:
            return f"""{self.gigawatts_per_cubic_foot} """
        
        if unit == PowerDensityUnits.TerawattPerCubicFoot:
            return f"""{self.terawatts_per_cubic_foot} """
        
        if unit == PowerDensityUnits.PicowattPerLiter:
            return f"""{self.picowatts_per_liter} """
        
        if unit == PowerDensityUnits.NanowattPerLiter:
            return f"""{self.nanowatts_per_liter} """
        
        if unit == PowerDensityUnits.MicrowattPerLiter:
            return f"""{self.microwatts_per_liter} """
        
        if unit == PowerDensityUnits.MilliwattPerLiter:
            return f"""{self.milliwatts_per_liter} """
        
        if unit == PowerDensityUnits.DeciwattPerLiter:
            return f"""{self.deciwatts_per_liter} """
        
        if unit == PowerDensityUnits.DecawattPerLiter:
            return f"""{self.decawatts_per_liter} """
        
        if unit == PowerDensityUnits.KilowattPerLiter:
            return f"""{self.kilowatts_per_liter} """
        
        if unit == PowerDensityUnits.MegawattPerLiter:
            return f"""{self.megawatts_per_liter} """
        
        if unit == PowerDensityUnits.GigawattPerLiter:
            return f"""{self.gigawatts_per_liter} """
        
        if unit == PowerDensityUnits.TerawattPerLiter:
            return f"""{self.terawatts_per_liter} """
        
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
        
        if unit_abbreviation == PowerDensityUnits.PicowattPerCubicMeter:
            return """"""
        
        if unit_abbreviation == PowerDensityUnits.NanowattPerCubicMeter:
            return """"""
        
        if unit_abbreviation == PowerDensityUnits.MicrowattPerCubicMeter:
            return """"""
        
        if unit_abbreviation == PowerDensityUnits.MilliwattPerCubicMeter:
            return """"""
        
        if unit_abbreviation == PowerDensityUnits.DeciwattPerCubicMeter:
            return """"""
        
        if unit_abbreviation == PowerDensityUnits.DecawattPerCubicMeter:
            return """"""
        
        if unit_abbreviation == PowerDensityUnits.KilowattPerCubicMeter:
            return """"""
        
        if unit_abbreviation == PowerDensityUnits.MegawattPerCubicMeter:
            return """"""
        
        if unit_abbreviation == PowerDensityUnits.GigawattPerCubicMeter:
            return """"""
        
        if unit_abbreviation == PowerDensityUnits.TerawattPerCubicMeter:
            return """"""
        
        if unit_abbreviation == PowerDensityUnits.PicowattPerCubicInch:
            return """"""
        
        if unit_abbreviation == PowerDensityUnits.NanowattPerCubicInch:
            return """"""
        
        if unit_abbreviation == PowerDensityUnits.MicrowattPerCubicInch:
            return """"""
        
        if unit_abbreviation == PowerDensityUnits.MilliwattPerCubicInch:
            return """"""
        
        if unit_abbreviation == PowerDensityUnits.DeciwattPerCubicInch:
            return """"""
        
        if unit_abbreviation == PowerDensityUnits.DecawattPerCubicInch:
            return """"""
        
        if unit_abbreviation == PowerDensityUnits.KilowattPerCubicInch:
            return """"""
        
        if unit_abbreviation == PowerDensityUnits.MegawattPerCubicInch:
            return """"""
        
        if unit_abbreviation == PowerDensityUnits.GigawattPerCubicInch:
            return """"""
        
        if unit_abbreviation == PowerDensityUnits.TerawattPerCubicInch:
            return """"""
        
        if unit_abbreviation == PowerDensityUnits.PicowattPerCubicFoot:
            return """"""
        
        if unit_abbreviation == PowerDensityUnits.NanowattPerCubicFoot:
            return """"""
        
        if unit_abbreviation == PowerDensityUnits.MicrowattPerCubicFoot:
            return """"""
        
        if unit_abbreviation == PowerDensityUnits.MilliwattPerCubicFoot:
            return """"""
        
        if unit_abbreviation == PowerDensityUnits.DeciwattPerCubicFoot:
            return """"""
        
        if unit_abbreviation == PowerDensityUnits.DecawattPerCubicFoot:
            return """"""
        
        if unit_abbreviation == PowerDensityUnits.KilowattPerCubicFoot:
            return """"""
        
        if unit_abbreviation == PowerDensityUnits.MegawattPerCubicFoot:
            return """"""
        
        if unit_abbreviation == PowerDensityUnits.GigawattPerCubicFoot:
            return """"""
        
        if unit_abbreviation == PowerDensityUnits.TerawattPerCubicFoot:
            return """"""
        
        if unit_abbreviation == PowerDensityUnits.PicowattPerLiter:
            return """"""
        
        if unit_abbreviation == PowerDensityUnits.NanowattPerLiter:
            return """"""
        
        if unit_abbreviation == PowerDensityUnits.MicrowattPerLiter:
            return """"""
        
        if unit_abbreviation == PowerDensityUnits.MilliwattPerLiter:
            return """"""
        
        if unit_abbreviation == PowerDensityUnits.DeciwattPerLiter:
            return """"""
        
        if unit_abbreviation == PowerDensityUnits.DecawattPerLiter:
            return """"""
        
        if unit_abbreviation == PowerDensityUnits.KilowattPerLiter:
            return """"""
        
        if unit_abbreviation == PowerDensityUnits.MegawattPerLiter:
            return """"""
        
        if unit_abbreviation == PowerDensityUnits.GigawattPerLiter:
            return """"""
        
        if unit_abbreviation == PowerDensityUnits.TerawattPerLiter:
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
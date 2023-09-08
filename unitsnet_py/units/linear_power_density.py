from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



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
        
        MilliwattPerMeter = 'milliwatt_per_meter'
        """
            
        """
        
        KilowattPerMeter = 'kilowatt_per_meter'
        """
            
        """
        
        MegawattPerMeter = 'megawatt_per_meter'
        """
            
        """
        
        GigawattPerMeter = 'gigawatt_per_meter'
        """
            
        """
        
        MilliwattPerCentimeter = 'milliwatt_per_centimeter'
        """
            
        """
        
        KilowattPerCentimeter = 'kilowatt_per_centimeter'
        """
            
        """
        
        MegawattPerCentimeter = 'megawatt_per_centimeter'
        """
            
        """
        
        GigawattPerCentimeter = 'gigawatt_per_centimeter'
        """
            
        """
        
        MilliwattPerMillimeter = 'milliwatt_per_millimeter'
        """
            
        """
        
        KilowattPerMillimeter = 'kilowatt_per_millimeter'
        """
            
        """
        
        MegawattPerMillimeter = 'megawatt_per_millimeter'
        """
            
        """
        
        GigawattPerMillimeter = 'gigawatt_per_millimeter'
        """
            
        """
        
        MilliwattPerInch = 'milliwatt_per_inch'
        """
            
        """
        
        KilowattPerInch = 'kilowatt_per_inch'
        """
            
        """
        
        MegawattPerInch = 'megawatt_per_inch'
        """
            
        """
        
        GigawattPerInch = 'gigawatt_per_inch'
        """
            
        """
        
        MilliwattPerFoot = 'milliwatt_per_foot'
        """
            
        """
        
        KilowattPerFoot = 'kilowatt_per_foot'
        """
            
        """
        
        MegawattPerFoot = 'megawatt_per_foot'
        """
            
        """
        
        GigawattPerFoot = 'gigawatt_per_foot'
        """
            
        """
        

class LinearPowerDensity(AbstractMeasure):
    """
    The Linear Power Density of a substance is its power per unit length.  The term linear density is most often used when describing the characteristics of one-dimensional objects, although linear density can also be used to describe the density of a three-dimensional quantity along one particular dimension.

    Args:
        value (float): The value.
        from_unit (LinearPowerDensityUnits): The LinearPowerDensity unit to create from, The default unit is WattPerMeter
    """
    def __init__(self, value: float, from_unit: LinearPowerDensityUnits = LinearPowerDensityUnits.WattPerMeter):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__watts_per_meter = None
        
        self.__watts_per_centimeter = None
        
        self.__watts_per_millimeter = None
        
        self.__watts_per_inch = None
        
        self.__watts_per_foot = None
        
        self.__milliwatts_per_meter = None
        
        self.__kilowatts_per_meter = None
        
        self.__megawatts_per_meter = None
        
        self.__gigawatts_per_meter = None
        
        self.__milliwatts_per_centimeter = None
        
        self.__kilowatts_per_centimeter = None
        
        self.__megawatts_per_centimeter = None
        
        self.__gigawatts_per_centimeter = None
        
        self.__milliwatts_per_millimeter = None
        
        self.__kilowatts_per_millimeter = None
        
        self.__megawatts_per_millimeter = None
        
        self.__gigawatts_per_millimeter = None
        
        self.__milliwatts_per_inch = None
        
        self.__kilowatts_per_inch = None
        
        self.__megawatts_per_inch = None
        
        self.__gigawatts_per_inch = None
        
        self.__milliwatts_per_foot = None
        
        self.__kilowatts_per_foot = None
        
        self.__megawatts_per_foot = None
        
        self.__gigawatts_per_foot = None
        

    def convert(self, unit: LinearPowerDensityUnits) -> float:
        return self.__convert_from_base(unit)

    def __convert_from_base(self, from_unit: LinearPowerDensityUnits) -> float:
        value = self._value
        
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
        
        if from_unit == LinearPowerDensityUnits.MilliwattPerMeter:
            return ((value) / 0.001)
        
        if from_unit == LinearPowerDensityUnits.KilowattPerMeter:
            return ((value) / 1000.0)
        
        if from_unit == LinearPowerDensityUnits.MegawattPerMeter:
            return ((value) / 1000000.0)
        
        if from_unit == LinearPowerDensityUnits.GigawattPerMeter:
            return ((value) / 1000000000.0)
        
        if from_unit == LinearPowerDensityUnits.MilliwattPerCentimeter:
            return ((value / 1e2) / 0.001)
        
        if from_unit == LinearPowerDensityUnits.KilowattPerCentimeter:
            return ((value / 1e2) / 1000.0)
        
        if from_unit == LinearPowerDensityUnits.MegawattPerCentimeter:
            return ((value / 1e2) / 1000000.0)
        
        if from_unit == LinearPowerDensityUnits.GigawattPerCentimeter:
            return ((value / 1e2) / 1000000000.0)
        
        if from_unit == LinearPowerDensityUnits.MilliwattPerMillimeter:
            return ((value / 1e3) / 0.001)
        
        if from_unit == LinearPowerDensityUnits.KilowattPerMillimeter:
            return ((value / 1e3) / 1000.0)
        
        if from_unit == LinearPowerDensityUnits.MegawattPerMillimeter:
            return ((value / 1e3) / 1000000.0)
        
        if from_unit == LinearPowerDensityUnits.GigawattPerMillimeter:
            return ((value / 1e3) / 1000000000.0)
        
        if from_unit == LinearPowerDensityUnits.MilliwattPerInch:
            return ((value / 39.37007874) / 0.001)
        
        if from_unit == LinearPowerDensityUnits.KilowattPerInch:
            return ((value / 39.37007874) / 1000.0)
        
        if from_unit == LinearPowerDensityUnits.MegawattPerInch:
            return ((value / 39.37007874) / 1000000.0)
        
        if from_unit == LinearPowerDensityUnits.GigawattPerInch:
            return ((value / 39.37007874) / 1000000000.0)
        
        if from_unit == LinearPowerDensityUnits.MilliwattPerFoot:
            return ((value / 3.280839895) / 0.001)
        
        if from_unit == LinearPowerDensityUnits.KilowattPerFoot:
            return ((value / 3.280839895) / 1000.0)
        
        if from_unit == LinearPowerDensityUnits.MegawattPerFoot:
            return ((value / 3.280839895) / 1000000.0)
        
        if from_unit == LinearPowerDensityUnits.GigawattPerFoot:
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
        
        if to_unit == LinearPowerDensityUnits.MilliwattPerMeter:
            return ((value) * 0.001)
        
        if to_unit == LinearPowerDensityUnits.KilowattPerMeter:
            return ((value) * 1000.0)
        
        if to_unit == LinearPowerDensityUnits.MegawattPerMeter:
            return ((value) * 1000000.0)
        
        if to_unit == LinearPowerDensityUnits.GigawattPerMeter:
            return ((value) * 1000000000.0)
        
        if to_unit == LinearPowerDensityUnits.MilliwattPerCentimeter:
            return ((value * 1e2) * 0.001)
        
        if to_unit == LinearPowerDensityUnits.KilowattPerCentimeter:
            return ((value * 1e2) * 1000.0)
        
        if to_unit == LinearPowerDensityUnits.MegawattPerCentimeter:
            return ((value * 1e2) * 1000000.0)
        
        if to_unit == LinearPowerDensityUnits.GigawattPerCentimeter:
            return ((value * 1e2) * 1000000000.0)
        
        if to_unit == LinearPowerDensityUnits.MilliwattPerMillimeter:
            return ((value * 1e3) * 0.001)
        
        if to_unit == LinearPowerDensityUnits.KilowattPerMillimeter:
            return ((value * 1e3) * 1000.0)
        
        if to_unit == LinearPowerDensityUnits.MegawattPerMillimeter:
            return ((value * 1e3) * 1000000.0)
        
        if to_unit == LinearPowerDensityUnits.GigawattPerMillimeter:
            return ((value * 1e3) * 1000000000.0)
        
        if to_unit == LinearPowerDensityUnits.MilliwattPerInch:
            return ((value * 39.37007874) * 0.001)
        
        if to_unit == LinearPowerDensityUnits.KilowattPerInch:
            return ((value * 39.37007874) * 1000.0)
        
        if to_unit == LinearPowerDensityUnits.MegawattPerInch:
            return ((value * 39.37007874) * 1000000.0)
        
        if to_unit == LinearPowerDensityUnits.GigawattPerInch:
            return ((value * 39.37007874) * 1000000000.0)
        
        if to_unit == LinearPowerDensityUnits.MilliwattPerFoot:
            return ((value * 3.280839895) * 0.001)
        
        if to_unit == LinearPowerDensityUnits.KilowattPerFoot:
            return ((value * 3.280839895) * 1000.0)
        
        if to_unit == LinearPowerDensityUnits.MegawattPerFoot:
            return ((value * 3.280839895) * 1000000.0)
        
        if to_unit == LinearPowerDensityUnits.GigawattPerFoot:
            return ((value * 3.280839895) * 1000000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
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
    def from_milliwatts_per_meter(milliwatts_per_meter: float):
        """
        Create a new instance of LinearPowerDensity from a value in milliwatts_per_meter.

        

        :param meters: The LinearPowerDensity value in milliwatts_per_meter.
        :type milliwatts_per_meter: float
        :return: A new instance of LinearPowerDensity.
        :rtype: LinearPowerDensity
        """
        return LinearPowerDensity(milliwatts_per_meter, LinearPowerDensityUnits.MilliwattPerMeter)

    
    @staticmethod
    def from_kilowatts_per_meter(kilowatts_per_meter: float):
        """
        Create a new instance of LinearPowerDensity from a value in kilowatts_per_meter.

        

        :param meters: The LinearPowerDensity value in kilowatts_per_meter.
        :type kilowatts_per_meter: float
        :return: A new instance of LinearPowerDensity.
        :rtype: LinearPowerDensity
        """
        return LinearPowerDensity(kilowatts_per_meter, LinearPowerDensityUnits.KilowattPerMeter)

    
    @staticmethod
    def from_megawatts_per_meter(megawatts_per_meter: float):
        """
        Create a new instance of LinearPowerDensity from a value in megawatts_per_meter.

        

        :param meters: The LinearPowerDensity value in megawatts_per_meter.
        :type megawatts_per_meter: float
        :return: A new instance of LinearPowerDensity.
        :rtype: LinearPowerDensity
        """
        return LinearPowerDensity(megawatts_per_meter, LinearPowerDensityUnits.MegawattPerMeter)

    
    @staticmethod
    def from_gigawatts_per_meter(gigawatts_per_meter: float):
        """
        Create a new instance of LinearPowerDensity from a value in gigawatts_per_meter.

        

        :param meters: The LinearPowerDensity value in gigawatts_per_meter.
        :type gigawatts_per_meter: float
        :return: A new instance of LinearPowerDensity.
        :rtype: LinearPowerDensity
        """
        return LinearPowerDensity(gigawatts_per_meter, LinearPowerDensityUnits.GigawattPerMeter)

    
    @staticmethod
    def from_milliwatts_per_centimeter(milliwatts_per_centimeter: float):
        """
        Create a new instance of LinearPowerDensity from a value in milliwatts_per_centimeter.

        

        :param meters: The LinearPowerDensity value in milliwatts_per_centimeter.
        :type milliwatts_per_centimeter: float
        :return: A new instance of LinearPowerDensity.
        :rtype: LinearPowerDensity
        """
        return LinearPowerDensity(milliwatts_per_centimeter, LinearPowerDensityUnits.MilliwattPerCentimeter)

    
    @staticmethod
    def from_kilowatts_per_centimeter(kilowatts_per_centimeter: float):
        """
        Create a new instance of LinearPowerDensity from a value in kilowatts_per_centimeter.

        

        :param meters: The LinearPowerDensity value in kilowatts_per_centimeter.
        :type kilowatts_per_centimeter: float
        :return: A new instance of LinearPowerDensity.
        :rtype: LinearPowerDensity
        """
        return LinearPowerDensity(kilowatts_per_centimeter, LinearPowerDensityUnits.KilowattPerCentimeter)

    
    @staticmethod
    def from_megawatts_per_centimeter(megawatts_per_centimeter: float):
        """
        Create a new instance of LinearPowerDensity from a value in megawatts_per_centimeter.

        

        :param meters: The LinearPowerDensity value in megawatts_per_centimeter.
        :type megawatts_per_centimeter: float
        :return: A new instance of LinearPowerDensity.
        :rtype: LinearPowerDensity
        """
        return LinearPowerDensity(megawatts_per_centimeter, LinearPowerDensityUnits.MegawattPerCentimeter)

    
    @staticmethod
    def from_gigawatts_per_centimeter(gigawatts_per_centimeter: float):
        """
        Create a new instance of LinearPowerDensity from a value in gigawatts_per_centimeter.

        

        :param meters: The LinearPowerDensity value in gigawatts_per_centimeter.
        :type gigawatts_per_centimeter: float
        :return: A new instance of LinearPowerDensity.
        :rtype: LinearPowerDensity
        """
        return LinearPowerDensity(gigawatts_per_centimeter, LinearPowerDensityUnits.GigawattPerCentimeter)

    
    @staticmethod
    def from_milliwatts_per_millimeter(milliwatts_per_millimeter: float):
        """
        Create a new instance of LinearPowerDensity from a value in milliwatts_per_millimeter.

        

        :param meters: The LinearPowerDensity value in milliwatts_per_millimeter.
        :type milliwatts_per_millimeter: float
        :return: A new instance of LinearPowerDensity.
        :rtype: LinearPowerDensity
        """
        return LinearPowerDensity(milliwatts_per_millimeter, LinearPowerDensityUnits.MilliwattPerMillimeter)

    
    @staticmethod
    def from_kilowatts_per_millimeter(kilowatts_per_millimeter: float):
        """
        Create a new instance of LinearPowerDensity from a value in kilowatts_per_millimeter.

        

        :param meters: The LinearPowerDensity value in kilowatts_per_millimeter.
        :type kilowatts_per_millimeter: float
        :return: A new instance of LinearPowerDensity.
        :rtype: LinearPowerDensity
        """
        return LinearPowerDensity(kilowatts_per_millimeter, LinearPowerDensityUnits.KilowattPerMillimeter)

    
    @staticmethod
    def from_megawatts_per_millimeter(megawatts_per_millimeter: float):
        """
        Create a new instance of LinearPowerDensity from a value in megawatts_per_millimeter.

        

        :param meters: The LinearPowerDensity value in megawatts_per_millimeter.
        :type megawatts_per_millimeter: float
        :return: A new instance of LinearPowerDensity.
        :rtype: LinearPowerDensity
        """
        return LinearPowerDensity(megawatts_per_millimeter, LinearPowerDensityUnits.MegawattPerMillimeter)

    
    @staticmethod
    def from_gigawatts_per_millimeter(gigawatts_per_millimeter: float):
        """
        Create a new instance of LinearPowerDensity from a value in gigawatts_per_millimeter.

        

        :param meters: The LinearPowerDensity value in gigawatts_per_millimeter.
        :type gigawatts_per_millimeter: float
        :return: A new instance of LinearPowerDensity.
        :rtype: LinearPowerDensity
        """
        return LinearPowerDensity(gigawatts_per_millimeter, LinearPowerDensityUnits.GigawattPerMillimeter)

    
    @staticmethod
    def from_milliwatts_per_inch(milliwatts_per_inch: float):
        """
        Create a new instance of LinearPowerDensity from a value in milliwatts_per_inch.

        

        :param meters: The LinearPowerDensity value in milliwatts_per_inch.
        :type milliwatts_per_inch: float
        :return: A new instance of LinearPowerDensity.
        :rtype: LinearPowerDensity
        """
        return LinearPowerDensity(milliwatts_per_inch, LinearPowerDensityUnits.MilliwattPerInch)

    
    @staticmethod
    def from_kilowatts_per_inch(kilowatts_per_inch: float):
        """
        Create a new instance of LinearPowerDensity from a value in kilowatts_per_inch.

        

        :param meters: The LinearPowerDensity value in kilowatts_per_inch.
        :type kilowatts_per_inch: float
        :return: A new instance of LinearPowerDensity.
        :rtype: LinearPowerDensity
        """
        return LinearPowerDensity(kilowatts_per_inch, LinearPowerDensityUnits.KilowattPerInch)

    
    @staticmethod
    def from_megawatts_per_inch(megawatts_per_inch: float):
        """
        Create a new instance of LinearPowerDensity from a value in megawatts_per_inch.

        

        :param meters: The LinearPowerDensity value in megawatts_per_inch.
        :type megawatts_per_inch: float
        :return: A new instance of LinearPowerDensity.
        :rtype: LinearPowerDensity
        """
        return LinearPowerDensity(megawatts_per_inch, LinearPowerDensityUnits.MegawattPerInch)

    
    @staticmethod
    def from_gigawatts_per_inch(gigawatts_per_inch: float):
        """
        Create a new instance of LinearPowerDensity from a value in gigawatts_per_inch.

        

        :param meters: The LinearPowerDensity value in gigawatts_per_inch.
        :type gigawatts_per_inch: float
        :return: A new instance of LinearPowerDensity.
        :rtype: LinearPowerDensity
        """
        return LinearPowerDensity(gigawatts_per_inch, LinearPowerDensityUnits.GigawattPerInch)

    
    @staticmethod
    def from_milliwatts_per_foot(milliwatts_per_foot: float):
        """
        Create a new instance of LinearPowerDensity from a value in milliwatts_per_foot.

        

        :param meters: The LinearPowerDensity value in milliwatts_per_foot.
        :type milliwatts_per_foot: float
        :return: A new instance of LinearPowerDensity.
        :rtype: LinearPowerDensity
        """
        return LinearPowerDensity(milliwatts_per_foot, LinearPowerDensityUnits.MilliwattPerFoot)

    
    @staticmethod
    def from_kilowatts_per_foot(kilowatts_per_foot: float):
        """
        Create a new instance of LinearPowerDensity from a value in kilowatts_per_foot.

        

        :param meters: The LinearPowerDensity value in kilowatts_per_foot.
        :type kilowatts_per_foot: float
        :return: A new instance of LinearPowerDensity.
        :rtype: LinearPowerDensity
        """
        return LinearPowerDensity(kilowatts_per_foot, LinearPowerDensityUnits.KilowattPerFoot)

    
    @staticmethod
    def from_megawatts_per_foot(megawatts_per_foot: float):
        """
        Create a new instance of LinearPowerDensity from a value in megawatts_per_foot.

        

        :param meters: The LinearPowerDensity value in megawatts_per_foot.
        :type megawatts_per_foot: float
        :return: A new instance of LinearPowerDensity.
        :rtype: LinearPowerDensity
        """
        return LinearPowerDensity(megawatts_per_foot, LinearPowerDensityUnits.MegawattPerFoot)

    
    @staticmethod
    def from_gigawatts_per_foot(gigawatts_per_foot: float):
        """
        Create a new instance of LinearPowerDensity from a value in gigawatts_per_foot.

        

        :param meters: The LinearPowerDensity value in gigawatts_per_foot.
        :type gigawatts_per_foot: float
        :return: A new instance of LinearPowerDensity.
        :rtype: LinearPowerDensity
        """
        return LinearPowerDensity(gigawatts_per_foot, LinearPowerDensityUnits.GigawattPerFoot)

    
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
    def milliwatts_per_meter(self) -> float:
        """
        
        """
        if self.__milliwatts_per_meter != None:
            return self.__milliwatts_per_meter
        self.__milliwatts_per_meter = self.__convert_from_base(LinearPowerDensityUnits.MilliwattPerMeter)
        return self.__milliwatts_per_meter

    
    @property
    def kilowatts_per_meter(self) -> float:
        """
        
        """
        if self.__kilowatts_per_meter != None:
            return self.__kilowatts_per_meter
        self.__kilowatts_per_meter = self.__convert_from_base(LinearPowerDensityUnits.KilowattPerMeter)
        return self.__kilowatts_per_meter

    
    @property
    def megawatts_per_meter(self) -> float:
        """
        
        """
        if self.__megawatts_per_meter != None:
            return self.__megawatts_per_meter
        self.__megawatts_per_meter = self.__convert_from_base(LinearPowerDensityUnits.MegawattPerMeter)
        return self.__megawatts_per_meter

    
    @property
    def gigawatts_per_meter(self) -> float:
        """
        
        """
        if self.__gigawatts_per_meter != None:
            return self.__gigawatts_per_meter
        self.__gigawatts_per_meter = self.__convert_from_base(LinearPowerDensityUnits.GigawattPerMeter)
        return self.__gigawatts_per_meter

    
    @property
    def milliwatts_per_centimeter(self) -> float:
        """
        
        """
        if self.__milliwatts_per_centimeter != None:
            return self.__milliwatts_per_centimeter
        self.__milliwatts_per_centimeter = self.__convert_from_base(LinearPowerDensityUnits.MilliwattPerCentimeter)
        return self.__milliwatts_per_centimeter

    
    @property
    def kilowatts_per_centimeter(self) -> float:
        """
        
        """
        if self.__kilowatts_per_centimeter != None:
            return self.__kilowatts_per_centimeter
        self.__kilowatts_per_centimeter = self.__convert_from_base(LinearPowerDensityUnits.KilowattPerCentimeter)
        return self.__kilowatts_per_centimeter

    
    @property
    def megawatts_per_centimeter(self) -> float:
        """
        
        """
        if self.__megawatts_per_centimeter != None:
            return self.__megawatts_per_centimeter
        self.__megawatts_per_centimeter = self.__convert_from_base(LinearPowerDensityUnits.MegawattPerCentimeter)
        return self.__megawatts_per_centimeter

    
    @property
    def gigawatts_per_centimeter(self) -> float:
        """
        
        """
        if self.__gigawatts_per_centimeter != None:
            return self.__gigawatts_per_centimeter
        self.__gigawatts_per_centimeter = self.__convert_from_base(LinearPowerDensityUnits.GigawattPerCentimeter)
        return self.__gigawatts_per_centimeter

    
    @property
    def milliwatts_per_millimeter(self) -> float:
        """
        
        """
        if self.__milliwatts_per_millimeter != None:
            return self.__milliwatts_per_millimeter
        self.__milliwatts_per_millimeter = self.__convert_from_base(LinearPowerDensityUnits.MilliwattPerMillimeter)
        return self.__milliwatts_per_millimeter

    
    @property
    def kilowatts_per_millimeter(self) -> float:
        """
        
        """
        if self.__kilowatts_per_millimeter != None:
            return self.__kilowatts_per_millimeter
        self.__kilowatts_per_millimeter = self.__convert_from_base(LinearPowerDensityUnits.KilowattPerMillimeter)
        return self.__kilowatts_per_millimeter

    
    @property
    def megawatts_per_millimeter(self) -> float:
        """
        
        """
        if self.__megawatts_per_millimeter != None:
            return self.__megawatts_per_millimeter
        self.__megawatts_per_millimeter = self.__convert_from_base(LinearPowerDensityUnits.MegawattPerMillimeter)
        return self.__megawatts_per_millimeter

    
    @property
    def gigawatts_per_millimeter(self) -> float:
        """
        
        """
        if self.__gigawatts_per_millimeter != None:
            return self.__gigawatts_per_millimeter
        self.__gigawatts_per_millimeter = self.__convert_from_base(LinearPowerDensityUnits.GigawattPerMillimeter)
        return self.__gigawatts_per_millimeter

    
    @property
    def milliwatts_per_inch(self) -> float:
        """
        
        """
        if self.__milliwatts_per_inch != None:
            return self.__milliwatts_per_inch
        self.__milliwatts_per_inch = self.__convert_from_base(LinearPowerDensityUnits.MilliwattPerInch)
        return self.__milliwatts_per_inch

    
    @property
    def kilowatts_per_inch(self) -> float:
        """
        
        """
        if self.__kilowatts_per_inch != None:
            return self.__kilowatts_per_inch
        self.__kilowatts_per_inch = self.__convert_from_base(LinearPowerDensityUnits.KilowattPerInch)
        return self.__kilowatts_per_inch

    
    @property
    def megawatts_per_inch(self) -> float:
        """
        
        """
        if self.__megawatts_per_inch != None:
            return self.__megawatts_per_inch
        self.__megawatts_per_inch = self.__convert_from_base(LinearPowerDensityUnits.MegawattPerInch)
        return self.__megawatts_per_inch

    
    @property
    def gigawatts_per_inch(self) -> float:
        """
        
        """
        if self.__gigawatts_per_inch != None:
            return self.__gigawatts_per_inch
        self.__gigawatts_per_inch = self.__convert_from_base(LinearPowerDensityUnits.GigawattPerInch)
        return self.__gigawatts_per_inch

    
    @property
    def milliwatts_per_foot(self) -> float:
        """
        
        """
        if self.__milliwatts_per_foot != None:
            return self.__milliwatts_per_foot
        self.__milliwatts_per_foot = self.__convert_from_base(LinearPowerDensityUnits.MilliwattPerFoot)
        return self.__milliwatts_per_foot

    
    @property
    def kilowatts_per_foot(self) -> float:
        """
        
        """
        if self.__kilowatts_per_foot != None:
            return self.__kilowatts_per_foot
        self.__kilowatts_per_foot = self.__convert_from_base(LinearPowerDensityUnits.KilowattPerFoot)
        return self.__kilowatts_per_foot

    
    @property
    def megawatts_per_foot(self) -> float:
        """
        
        """
        if self.__megawatts_per_foot != None:
            return self.__megawatts_per_foot
        self.__megawatts_per_foot = self.__convert_from_base(LinearPowerDensityUnits.MegawattPerFoot)
        return self.__megawatts_per_foot

    
    @property
    def gigawatts_per_foot(self) -> float:
        """
        
        """
        if self.__gigawatts_per_foot != None:
            return self.__gigawatts_per_foot
        self.__gigawatts_per_foot = self.__convert_from_base(LinearPowerDensityUnits.GigawattPerFoot)
        return self.__gigawatts_per_foot

    
    def to_string(self, unit: LinearPowerDensityUnits = LinearPowerDensityUnits.WattPerMeter) -> str:
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
        
        if unit == LinearPowerDensityUnits.MilliwattPerMeter:
            return f"""{self.milliwatts_per_meter} mW/m"""
        
        if unit == LinearPowerDensityUnits.KilowattPerMeter:
            return f"""{self.kilowatts_per_meter} kW/m"""
        
        if unit == LinearPowerDensityUnits.MegawattPerMeter:
            return f"""{self.megawatts_per_meter} MW/m"""
        
        if unit == LinearPowerDensityUnits.GigawattPerMeter:
            return f"""{self.gigawatts_per_meter} GW/m"""
        
        if unit == LinearPowerDensityUnits.MilliwattPerCentimeter:
            return f"""{self.milliwatts_per_centimeter} mW/cm"""
        
        if unit == LinearPowerDensityUnits.KilowattPerCentimeter:
            return f"""{self.kilowatts_per_centimeter} kW/cm"""
        
        if unit == LinearPowerDensityUnits.MegawattPerCentimeter:
            return f"""{self.megawatts_per_centimeter} MW/cm"""
        
        if unit == LinearPowerDensityUnits.GigawattPerCentimeter:
            return f"""{self.gigawatts_per_centimeter} GW/cm"""
        
        if unit == LinearPowerDensityUnits.MilliwattPerMillimeter:
            return f"""{self.milliwatts_per_millimeter} mW/mm"""
        
        if unit == LinearPowerDensityUnits.KilowattPerMillimeter:
            return f"""{self.kilowatts_per_millimeter} kW/mm"""
        
        if unit == LinearPowerDensityUnits.MegawattPerMillimeter:
            return f"""{self.megawatts_per_millimeter} MW/mm"""
        
        if unit == LinearPowerDensityUnits.GigawattPerMillimeter:
            return f"""{self.gigawatts_per_millimeter} GW/mm"""
        
        if unit == LinearPowerDensityUnits.MilliwattPerInch:
            return f"""{self.milliwatts_per_inch} mW/in"""
        
        if unit == LinearPowerDensityUnits.KilowattPerInch:
            return f"""{self.kilowatts_per_inch} kW/in"""
        
        if unit == LinearPowerDensityUnits.MegawattPerInch:
            return f"""{self.megawatts_per_inch} MW/in"""
        
        if unit == LinearPowerDensityUnits.GigawattPerInch:
            return f"""{self.gigawatts_per_inch} GW/in"""
        
        if unit == LinearPowerDensityUnits.MilliwattPerFoot:
            return f"""{self.milliwatts_per_foot} mW/ft"""
        
        if unit == LinearPowerDensityUnits.KilowattPerFoot:
            return f"""{self.kilowatts_per_foot} kW/ft"""
        
        if unit == LinearPowerDensityUnits.MegawattPerFoot:
            return f"""{self.megawatts_per_foot} MW/ft"""
        
        if unit == LinearPowerDensityUnits.GigawattPerFoot:
            return f"""{self.gigawatts_per_foot} GW/ft"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: LinearPowerDensityUnits = LinearPowerDensityUnits.WattPerMeter) -> str:
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
        
        if unit_abbreviation == LinearPowerDensityUnits.MilliwattPerMeter:
            return """mW/m"""
        
        if unit_abbreviation == LinearPowerDensityUnits.KilowattPerMeter:
            return """kW/m"""
        
        if unit_abbreviation == LinearPowerDensityUnits.MegawattPerMeter:
            return """MW/m"""
        
        if unit_abbreviation == LinearPowerDensityUnits.GigawattPerMeter:
            return """GW/m"""
        
        if unit_abbreviation == LinearPowerDensityUnits.MilliwattPerCentimeter:
            return """mW/cm"""
        
        if unit_abbreviation == LinearPowerDensityUnits.KilowattPerCentimeter:
            return """kW/cm"""
        
        if unit_abbreviation == LinearPowerDensityUnits.MegawattPerCentimeter:
            return """MW/cm"""
        
        if unit_abbreviation == LinearPowerDensityUnits.GigawattPerCentimeter:
            return """GW/cm"""
        
        if unit_abbreviation == LinearPowerDensityUnits.MilliwattPerMillimeter:
            return """mW/mm"""
        
        if unit_abbreviation == LinearPowerDensityUnits.KilowattPerMillimeter:
            return """kW/mm"""
        
        if unit_abbreviation == LinearPowerDensityUnits.MegawattPerMillimeter:
            return """MW/mm"""
        
        if unit_abbreviation == LinearPowerDensityUnits.GigawattPerMillimeter:
            return """GW/mm"""
        
        if unit_abbreviation == LinearPowerDensityUnits.MilliwattPerInch:
            return """mW/in"""
        
        if unit_abbreviation == LinearPowerDensityUnits.KilowattPerInch:
            return """kW/in"""
        
        if unit_abbreviation == LinearPowerDensityUnits.MegawattPerInch:
            return """MW/in"""
        
        if unit_abbreviation == LinearPowerDensityUnits.GigawattPerInch:
            return """GW/in"""
        
        if unit_abbreviation == LinearPowerDensityUnits.MilliwattPerFoot:
            return """mW/ft"""
        
        if unit_abbreviation == LinearPowerDensityUnits.KilowattPerFoot:
            return """kW/ft"""
        
        if unit_abbreviation == LinearPowerDensityUnits.MegawattPerFoot:
            return """MW/ft"""
        
        if unit_abbreviation == LinearPowerDensityUnits.GigawattPerFoot:
            return """GW/ft"""
        
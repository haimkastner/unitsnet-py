from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class ForcePerLengthUnits(Enum):
        """
            ForcePerLengthUnits enumeration
        """
        
        NewtonPerMeter = 'newton_per_meter'
        """
            
        """
        
        NewtonPerCentimeter = 'newton_per_centimeter'
        """
            
        """
        
        NewtonPerMillimeter = 'newton_per_millimeter'
        """
            
        """
        
        KilogramForcePerMeter = 'kilogram_force_per_meter'
        """
            
        """
        
        KilogramForcePerCentimeter = 'kilogram_force_per_centimeter'
        """
            
        """
        
        KilogramForcePerMillimeter = 'kilogram_force_per_millimeter'
        """
            
        """
        
        TonneForcePerMeter = 'tonne_force_per_meter'
        """
            
        """
        
        TonneForcePerCentimeter = 'tonne_force_per_centimeter'
        """
            
        """
        
        TonneForcePerMillimeter = 'tonne_force_per_millimeter'
        """
            
        """
        
        PoundForcePerFoot = 'pound_force_per_foot'
        """
            
        """
        
        PoundForcePerInch = 'pound_force_per_inch'
        """
            
        """
        
        PoundForcePerYard = 'pound_force_per_yard'
        """
            
        """
        
        KilopoundForcePerFoot = 'kilopound_force_per_foot'
        """
            
        """
        
        KilopoundForcePerInch = 'kilopound_force_per_inch'
        """
            
        """
        
        NanonewtonPerMeter = 'nanonewton_per_meter'
        """
            
        """
        
        MicronewtonPerMeter = 'micronewton_per_meter'
        """
            
        """
        
        MillinewtonPerMeter = 'millinewton_per_meter'
        """
            
        """
        
        CentinewtonPerMeter = 'centinewton_per_meter'
        """
            
        """
        
        DecinewtonPerMeter = 'decinewton_per_meter'
        """
            
        """
        
        DecanewtonPerMeter = 'decanewton_per_meter'
        """
            
        """
        
        KilonewtonPerMeter = 'kilonewton_per_meter'
        """
            
        """
        
        MeganewtonPerMeter = 'meganewton_per_meter'
        """
            
        """
        
        NanonewtonPerCentimeter = 'nanonewton_per_centimeter'
        """
            
        """
        
        MicronewtonPerCentimeter = 'micronewton_per_centimeter'
        """
            
        """
        
        MillinewtonPerCentimeter = 'millinewton_per_centimeter'
        """
            
        """
        
        CentinewtonPerCentimeter = 'centinewton_per_centimeter'
        """
            
        """
        
        DecinewtonPerCentimeter = 'decinewton_per_centimeter'
        """
            
        """
        
        DecanewtonPerCentimeter = 'decanewton_per_centimeter'
        """
            
        """
        
        KilonewtonPerCentimeter = 'kilonewton_per_centimeter'
        """
            
        """
        
        MeganewtonPerCentimeter = 'meganewton_per_centimeter'
        """
            
        """
        
        NanonewtonPerMillimeter = 'nanonewton_per_millimeter'
        """
            
        """
        
        MicronewtonPerMillimeter = 'micronewton_per_millimeter'
        """
            
        """
        
        MillinewtonPerMillimeter = 'millinewton_per_millimeter'
        """
            
        """
        
        CentinewtonPerMillimeter = 'centinewton_per_millimeter'
        """
            
        """
        
        DecinewtonPerMillimeter = 'decinewton_per_millimeter'
        """
            
        """
        
        DecanewtonPerMillimeter = 'decanewton_per_millimeter'
        """
            
        """
        
        KilonewtonPerMillimeter = 'kilonewton_per_millimeter'
        """
            
        """
        
        MeganewtonPerMillimeter = 'meganewton_per_millimeter'
        """
            
        """
        

class ForcePerLength(AbstractMeasure):
    """
    The magnitude of force per unit length.

    Args:
        value (float): The value.
        from_unit (ForcePerLengthUnits): The ForcePerLength unit to create from, The default unit is NewtonPerMeter
    """
    def __init__(self, value: float, from_unit: ForcePerLengthUnits = ForcePerLengthUnits.NewtonPerMeter):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__newtons_per_meter = None
        
        self.__newtons_per_centimeter = None
        
        self.__newtons_per_millimeter = None
        
        self.__kilograms_force_per_meter = None
        
        self.__kilograms_force_per_centimeter = None
        
        self.__kilograms_force_per_millimeter = None
        
        self.__tonnes_force_per_meter = None
        
        self.__tonnes_force_per_centimeter = None
        
        self.__tonnes_force_per_millimeter = None
        
        self.__pounds_force_per_foot = None
        
        self.__pounds_force_per_inch = None
        
        self.__pounds_force_per_yard = None
        
        self.__kilopounds_force_per_foot = None
        
        self.__kilopounds_force_per_inch = None
        
        self.__nanonewtons_per_meter = None
        
        self.__micronewtons_per_meter = None
        
        self.__millinewtons_per_meter = None
        
        self.__centinewtons_per_meter = None
        
        self.__decinewtons_per_meter = None
        
        self.__decanewtons_per_meter = None
        
        self.__kilonewtons_per_meter = None
        
        self.__meganewtons_per_meter = None
        
        self.__nanonewtons_per_centimeter = None
        
        self.__micronewtons_per_centimeter = None
        
        self.__millinewtons_per_centimeter = None
        
        self.__centinewtons_per_centimeter = None
        
        self.__decinewtons_per_centimeter = None
        
        self.__decanewtons_per_centimeter = None
        
        self.__kilonewtons_per_centimeter = None
        
        self.__meganewtons_per_centimeter = None
        
        self.__nanonewtons_per_millimeter = None
        
        self.__micronewtons_per_millimeter = None
        
        self.__millinewtons_per_millimeter = None
        
        self.__centinewtons_per_millimeter = None
        
        self.__decinewtons_per_millimeter = None
        
        self.__decanewtons_per_millimeter = None
        
        self.__kilonewtons_per_millimeter = None
        
        self.__meganewtons_per_millimeter = None
        

    def convert(self, unit: ForcePerLengthUnits) -> float:
        return self.__convert_from_base(unit)

    def __convert_from_base(self, from_unit: ForcePerLengthUnits) -> float:
        value = self._value
        
        if from_unit == ForcePerLengthUnits.NewtonPerMeter:
            return (value)
        
        if from_unit == ForcePerLengthUnits.NewtonPerCentimeter:
            return (value / 1e2)
        
        if from_unit == ForcePerLengthUnits.NewtonPerMillimeter:
            return (value / 1e3)
        
        if from_unit == ForcePerLengthUnits.KilogramForcePerMeter:
            return (value / 9.80665002864)
        
        if from_unit == ForcePerLengthUnits.KilogramForcePerCentimeter:
            return (value / 980.665002864)
        
        if from_unit == ForcePerLengthUnits.KilogramForcePerMillimeter:
            return (value / 9.80665002864e3)
        
        if from_unit == ForcePerLengthUnits.TonneForcePerMeter:
            return (value / 9.80665002864e3)
        
        if from_unit == ForcePerLengthUnits.TonneForcePerCentimeter:
            return (value / 9.80665002864e5)
        
        if from_unit == ForcePerLengthUnits.TonneForcePerMillimeter:
            return (value / 9.80665002864e6)
        
        if from_unit == ForcePerLengthUnits.PoundForcePerFoot:
            return (value / 14.59390292)
        
        if from_unit == ForcePerLengthUnits.PoundForcePerInch:
            return (value / 1.75126835e2)
        
        if from_unit == ForcePerLengthUnits.PoundForcePerYard:
            return (value / 4.864634307)
        
        if from_unit == ForcePerLengthUnits.KilopoundForcePerFoot:
            return (value / 14593.90292)
        
        if from_unit == ForcePerLengthUnits.KilopoundForcePerInch:
            return (value / 1.75126835e5)
        
        if from_unit == ForcePerLengthUnits.NanonewtonPerMeter:
            return ((value) / 1e-09)
        
        if from_unit == ForcePerLengthUnits.MicronewtonPerMeter:
            return ((value) / 1e-06)
        
        if from_unit == ForcePerLengthUnits.MillinewtonPerMeter:
            return ((value) / 0.001)
        
        if from_unit == ForcePerLengthUnits.CentinewtonPerMeter:
            return ((value) / 0.01)
        
        if from_unit == ForcePerLengthUnits.DecinewtonPerMeter:
            return ((value) / 0.1)
        
        if from_unit == ForcePerLengthUnits.DecanewtonPerMeter:
            return ((value) / 10.0)
        
        if from_unit == ForcePerLengthUnits.KilonewtonPerMeter:
            return ((value) / 1000.0)
        
        if from_unit == ForcePerLengthUnits.MeganewtonPerMeter:
            return ((value) / 1000000.0)
        
        if from_unit == ForcePerLengthUnits.NanonewtonPerCentimeter:
            return ((value / 1e2) / 1e-09)
        
        if from_unit == ForcePerLengthUnits.MicronewtonPerCentimeter:
            return ((value / 1e2) / 1e-06)
        
        if from_unit == ForcePerLengthUnits.MillinewtonPerCentimeter:
            return ((value / 1e2) / 0.001)
        
        if from_unit == ForcePerLengthUnits.CentinewtonPerCentimeter:
            return ((value / 1e2) / 0.01)
        
        if from_unit == ForcePerLengthUnits.DecinewtonPerCentimeter:
            return ((value / 1e2) / 0.1)
        
        if from_unit == ForcePerLengthUnits.DecanewtonPerCentimeter:
            return ((value / 1e2) / 10.0)
        
        if from_unit == ForcePerLengthUnits.KilonewtonPerCentimeter:
            return ((value / 1e2) / 1000.0)
        
        if from_unit == ForcePerLengthUnits.MeganewtonPerCentimeter:
            return ((value / 1e2) / 1000000.0)
        
        if from_unit == ForcePerLengthUnits.NanonewtonPerMillimeter:
            return ((value / 1e3) / 1e-09)
        
        if from_unit == ForcePerLengthUnits.MicronewtonPerMillimeter:
            return ((value / 1e3) / 1e-06)
        
        if from_unit == ForcePerLengthUnits.MillinewtonPerMillimeter:
            return ((value / 1e3) / 0.001)
        
        if from_unit == ForcePerLengthUnits.CentinewtonPerMillimeter:
            return ((value / 1e3) / 0.01)
        
        if from_unit == ForcePerLengthUnits.DecinewtonPerMillimeter:
            return ((value / 1e3) / 0.1)
        
        if from_unit == ForcePerLengthUnits.DecanewtonPerMillimeter:
            return ((value / 1e3) / 10.0)
        
        if from_unit == ForcePerLengthUnits.KilonewtonPerMillimeter:
            return ((value / 1e3) / 1000.0)
        
        if from_unit == ForcePerLengthUnits.MeganewtonPerMillimeter:
            return ((value / 1e3) / 1000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: ForcePerLengthUnits) -> float:
        
        if to_unit == ForcePerLengthUnits.NewtonPerMeter:
            return (value)
        
        if to_unit == ForcePerLengthUnits.NewtonPerCentimeter:
            return (value * 1e2)
        
        if to_unit == ForcePerLengthUnits.NewtonPerMillimeter:
            return (value * 1e3)
        
        if to_unit == ForcePerLengthUnits.KilogramForcePerMeter:
            return (value * 9.80665002864)
        
        if to_unit == ForcePerLengthUnits.KilogramForcePerCentimeter:
            return (value * 980.665002864)
        
        if to_unit == ForcePerLengthUnits.KilogramForcePerMillimeter:
            return (value * 9.80665002864e3)
        
        if to_unit == ForcePerLengthUnits.TonneForcePerMeter:
            return (value * 9.80665002864e3)
        
        if to_unit == ForcePerLengthUnits.TonneForcePerCentimeter:
            return (value * 9.80665002864e5)
        
        if to_unit == ForcePerLengthUnits.TonneForcePerMillimeter:
            return (value * 9.80665002864e6)
        
        if to_unit == ForcePerLengthUnits.PoundForcePerFoot:
            return (value * 14.59390292)
        
        if to_unit == ForcePerLengthUnits.PoundForcePerInch:
            return (value * 1.75126835e2)
        
        if to_unit == ForcePerLengthUnits.PoundForcePerYard:
            return (value * 4.864634307)
        
        if to_unit == ForcePerLengthUnits.KilopoundForcePerFoot:
            return (value * 14593.90292)
        
        if to_unit == ForcePerLengthUnits.KilopoundForcePerInch:
            return (value * 1.75126835e5)
        
        if to_unit == ForcePerLengthUnits.NanonewtonPerMeter:
            return ((value) * 1e-09)
        
        if to_unit == ForcePerLengthUnits.MicronewtonPerMeter:
            return ((value) * 1e-06)
        
        if to_unit == ForcePerLengthUnits.MillinewtonPerMeter:
            return ((value) * 0.001)
        
        if to_unit == ForcePerLengthUnits.CentinewtonPerMeter:
            return ((value) * 0.01)
        
        if to_unit == ForcePerLengthUnits.DecinewtonPerMeter:
            return ((value) * 0.1)
        
        if to_unit == ForcePerLengthUnits.DecanewtonPerMeter:
            return ((value) * 10.0)
        
        if to_unit == ForcePerLengthUnits.KilonewtonPerMeter:
            return ((value) * 1000.0)
        
        if to_unit == ForcePerLengthUnits.MeganewtonPerMeter:
            return ((value) * 1000000.0)
        
        if to_unit == ForcePerLengthUnits.NanonewtonPerCentimeter:
            return ((value * 1e2) * 1e-09)
        
        if to_unit == ForcePerLengthUnits.MicronewtonPerCentimeter:
            return ((value * 1e2) * 1e-06)
        
        if to_unit == ForcePerLengthUnits.MillinewtonPerCentimeter:
            return ((value * 1e2) * 0.001)
        
        if to_unit == ForcePerLengthUnits.CentinewtonPerCentimeter:
            return ((value * 1e2) * 0.01)
        
        if to_unit == ForcePerLengthUnits.DecinewtonPerCentimeter:
            return ((value * 1e2) * 0.1)
        
        if to_unit == ForcePerLengthUnits.DecanewtonPerCentimeter:
            return ((value * 1e2) * 10.0)
        
        if to_unit == ForcePerLengthUnits.KilonewtonPerCentimeter:
            return ((value * 1e2) * 1000.0)
        
        if to_unit == ForcePerLengthUnits.MeganewtonPerCentimeter:
            return ((value * 1e2) * 1000000.0)
        
        if to_unit == ForcePerLengthUnits.NanonewtonPerMillimeter:
            return ((value * 1e3) * 1e-09)
        
        if to_unit == ForcePerLengthUnits.MicronewtonPerMillimeter:
            return ((value * 1e3) * 1e-06)
        
        if to_unit == ForcePerLengthUnits.MillinewtonPerMillimeter:
            return ((value * 1e3) * 0.001)
        
        if to_unit == ForcePerLengthUnits.CentinewtonPerMillimeter:
            return ((value * 1e3) * 0.01)
        
        if to_unit == ForcePerLengthUnits.DecinewtonPerMillimeter:
            return ((value * 1e3) * 0.1)
        
        if to_unit == ForcePerLengthUnits.DecanewtonPerMillimeter:
            return ((value * 1e3) * 10.0)
        
        if to_unit == ForcePerLengthUnits.KilonewtonPerMillimeter:
            return ((value * 1e3) * 1000.0)
        
        if to_unit == ForcePerLengthUnits.MeganewtonPerMillimeter:
            return ((value * 1e3) * 1000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_newtons_per_meter(newtons_per_meter: float):
        """
        Create a new instance of ForcePerLength from a value in newtons_per_meter.

        

        :param meters: The ForcePerLength value in newtons_per_meter.
        :type newtons_per_meter: float
        :return: A new instance of ForcePerLength.
        :rtype: ForcePerLength
        """
        return ForcePerLength(newtons_per_meter, ForcePerLengthUnits.NewtonPerMeter)

    
    @staticmethod
    def from_newtons_per_centimeter(newtons_per_centimeter: float):
        """
        Create a new instance of ForcePerLength from a value in newtons_per_centimeter.

        

        :param meters: The ForcePerLength value in newtons_per_centimeter.
        :type newtons_per_centimeter: float
        :return: A new instance of ForcePerLength.
        :rtype: ForcePerLength
        """
        return ForcePerLength(newtons_per_centimeter, ForcePerLengthUnits.NewtonPerCentimeter)

    
    @staticmethod
    def from_newtons_per_millimeter(newtons_per_millimeter: float):
        """
        Create a new instance of ForcePerLength from a value in newtons_per_millimeter.

        

        :param meters: The ForcePerLength value in newtons_per_millimeter.
        :type newtons_per_millimeter: float
        :return: A new instance of ForcePerLength.
        :rtype: ForcePerLength
        """
        return ForcePerLength(newtons_per_millimeter, ForcePerLengthUnits.NewtonPerMillimeter)

    
    @staticmethod
    def from_kilograms_force_per_meter(kilograms_force_per_meter: float):
        """
        Create a new instance of ForcePerLength from a value in kilograms_force_per_meter.

        

        :param meters: The ForcePerLength value in kilograms_force_per_meter.
        :type kilograms_force_per_meter: float
        :return: A new instance of ForcePerLength.
        :rtype: ForcePerLength
        """
        return ForcePerLength(kilograms_force_per_meter, ForcePerLengthUnits.KilogramForcePerMeter)

    
    @staticmethod
    def from_kilograms_force_per_centimeter(kilograms_force_per_centimeter: float):
        """
        Create a new instance of ForcePerLength from a value in kilograms_force_per_centimeter.

        

        :param meters: The ForcePerLength value in kilograms_force_per_centimeter.
        :type kilograms_force_per_centimeter: float
        :return: A new instance of ForcePerLength.
        :rtype: ForcePerLength
        """
        return ForcePerLength(kilograms_force_per_centimeter, ForcePerLengthUnits.KilogramForcePerCentimeter)

    
    @staticmethod
    def from_kilograms_force_per_millimeter(kilograms_force_per_millimeter: float):
        """
        Create a new instance of ForcePerLength from a value in kilograms_force_per_millimeter.

        

        :param meters: The ForcePerLength value in kilograms_force_per_millimeter.
        :type kilograms_force_per_millimeter: float
        :return: A new instance of ForcePerLength.
        :rtype: ForcePerLength
        """
        return ForcePerLength(kilograms_force_per_millimeter, ForcePerLengthUnits.KilogramForcePerMillimeter)

    
    @staticmethod
    def from_tonnes_force_per_meter(tonnes_force_per_meter: float):
        """
        Create a new instance of ForcePerLength from a value in tonnes_force_per_meter.

        

        :param meters: The ForcePerLength value in tonnes_force_per_meter.
        :type tonnes_force_per_meter: float
        :return: A new instance of ForcePerLength.
        :rtype: ForcePerLength
        """
        return ForcePerLength(tonnes_force_per_meter, ForcePerLengthUnits.TonneForcePerMeter)

    
    @staticmethod
    def from_tonnes_force_per_centimeter(tonnes_force_per_centimeter: float):
        """
        Create a new instance of ForcePerLength from a value in tonnes_force_per_centimeter.

        

        :param meters: The ForcePerLength value in tonnes_force_per_centimeter.
        :type tonnes_force_per_centimeter: float
        :return: A new instance of ForcePerLength.
        :rtype: ForcePerLength
        """
        return ForcePerLength(tonnes_force_per_centimeter, ForcePerLengthUnits.TonneForcePerCentimeter)

    
    @staticmethod
    def from_tonnes_force_per_millimeter(tonnes_force_per_millimeter: float):
        """
        Create a new instance of ForcePerLength from a value in tonnes_force_per_millimeter.

        

        :param meters: The ForcePerLength value in tonnes_force_per_millimeter.
        :type tonnes_force_per_millimeter: float
        :return: A new instance of ForcePerLength.
        :rtype: ForcePerLength
        """
        return ForcePerLength(tonnes_force_per_millimeter, ForcePerLengthUnits.TonneForcePerMillimeter)

    
    @staticmethod
    def from_pounds_force_per_foot(pounds_force_per_foot: float):
        """
        Create a new instance of ForcePerLength from a value in pounds_force_per_foot.

        

        :param meters: The ForcePerLength value in pounds_force_per_foot.
        :type pounds_force_per_foot: float
        :return: A new instance of ForcePerLength.
        :rtype: ForcePerLength
        """
        return ForcePerLength(pounds_force_per_foot, ForcePerLengthUnits.PoundForcePerFoot)

    
    @staticmethod
    def from_pounds_force_per_inch(pounds_force_per_inch: float):
        """
        Create a new instance of ForcePerLength from a value in pounds_force_per_inch.

        

        :param meters: The ForcePerLength value in pounds_force_per_inch.
        :type pounds_force_per_inch: float
        :return: A new instance of ForcePerLength.
        :rtype: ForcePerLength
        """
        return ForcePerLength(pounds_force_per_inch, ForcePerLengthUnits.PoundForcePerInch)

    
    @staticmethod
    def from_pounds_force_per_yard(pounds_force_per_yard: float):
        """
        Create a new instance of ForcePerLength from a value in pounds_force_per_yard.

        

        :param meters: The ForcePerLength value in pounds_force_per_yard.
        :type pounds_force_per_yard: float
        :return: A new instance of ForcePerLength.
        :rtype: ForcePerLength
        """
        return ForcePerLength(pounds_force_per_yard, ForcePerLengthUnits.PoundForcePerYard)

    
    @staticmethod
    def from_kilopounds_force_per_foot(kilopounds_force_per_foot: float):
        """
        Create a new instance of ForcePerLength from a value in kilopounds_force_per_foot.

        

        :param meters: The ForcePerLength value in kilopounds_force_per_foot.
        :type kilopounds_force_per_foot: float
        :return: A new instance of ForcePerLength.
        :rtype: ForcePerLength
        """
        return ForcePerLength(kilopounds_force_per_foot, ForcePerLengthUnits.KilopoundForcePerFoot)

    
    @staticmethod
    def from_kilopounds_force_per_inch(kilopounds_force_per_inch: float):
        """
        Create a new instance of ForcePerLength from a value in kilopounds_force_per_inch.

        

        :param meters: The ForcePerLength value in kilopounds_force_per_inch.
        :type kilopounds_force_per_inch: float
        :return: A new instance of ForcePerLength.
        :rtype: ForcePerLength
        """
        return ForcePerLength(kilopounds_force_per_inch, ForcePerLengthUnits.KilopoundForcePerInch)

    
    @staticmethod
    def from_nanonewtons_per_meter(nanonewtons_per_meter: float):
        """
        Create a new instance of ForcePerLength from a value in nanonewtons_per_meter.

        

        :param meters: The ForcePerLength value in nanonewtons_per_meter.
        :type nanonewtons_per_meter: float
        :return: A new instance of ForcePerLength.
        :rtype: ForcePerLength
        """
        return ForcePerLength(nanonewtons_per_meter, ForcePerLengthUnits.NanonewtonPerMeter)

    
    @staticmethod
    def from_micronewtons_per_meter(micronewtons_per_meter: float):
        """
        Create a new instance of ForcePerLength from a value in micronewtons_per_meter.

        

        :param meters: The ForcePerLength value in micronewtons_per_meter.
        :type micronewtons_per_meter: float
        :return: A new instance of ForcePerLength.
        :rtype: ForcePerLength
        """
        return ForcePerLength(micronewtons_per_meter, ForcePerLengthUnits.MicronewtonPerMeter)

    
    @staticmethod
    def from_millinewtons_per_meter(millinewtons_per_meter: float):
        """
        Create a new instance of ForcePerLength from a value in millinewtons_per_meter.

        

        :param meters: The ForcePerLength value in millinewtons_per_meter.
        :type millinewtons_per_meter: float
        :return: A new instance of ForcePerLength.
        :rtype: ForcePerLength
        """
        return ForcePerLength(millinewtons_per_meter, ForcePerLengthUnits.MillinewtonPerMeter)

    
    @staticmethod
    def from_centinewtons_per_meter(centinewtons_per_meter: float):
        """
        Create a new instance of ForcePerLength from a value in centinewtons_per_meter.

        

        :param meters: The ForcePerLength value in centinewtons_per_meter.
        :type centinewtons_per_meter: float
        :return: A new instance of ForcePerLength.
        :rtype: ForcePerLength
        """
        return ForcePerLength(centinewtons_per_meter, ForcePerLengthUnits.CentinewtonPerMeter)

    
    @staticmethod
    def from_decinewtons_per_meter(decinewtons_per_meter: float):
        """
        Create a new instance of ForcePerLength from a value in decinewtons_per_meter.

        

        :param meters: The ForcePerLength value in decinewtons_per_meter.
        :type decinewtons_per_meter: float
        :return: A new instance of ForcePerLength.
        :rtype: ForcePerLength
        """
        return ForcePerLength(decinewtons_per_meter, ForcePerLengthUnits.DecinewtonPerMeter)

    
    @staticmethod
    def from_decanewtons_per_meter(decanewtons_per_meter: float):
        """
        Create a new instance of ForcePerLength from a value in decanewtons_per_meter.

        

        :param meters: The ForcePerLength value in decanewtons_per_meter.
        :type decanewtons_per_meter: float
        :return: A new instance of ForcePerLength.
        :rtype: ForcePerLength
        """
        return ForcePerLength(decanewtons_per_meter, ForcePerLengthUnits.DecanewtonPerMeter)

    
    @staticmethod
    def from_kilonewtons_per_meter(kilonewtons_per_meter: float):
        """
        Create a new instance of ForcePerLength from a value in kilonewtons_per_meter.

        

        :param meters: The ForcePerLength value in kilonewtons_per_meter.
        :type kilonewtons_per_meter: float
        :return: A new instance of ForcePerLength.
        :rtype: ForcePerLength
        """
        return ForcePerLength(kilonewtons_per_meter, ForcePerLengthUnits.KilonewtonPerMeter)

    
    @staticmethod
    def from_meganewtons_per_meter(meganewtons_per_meter: float):
        """
        Create a new instance of ForcePerLength from a value in meganewtons_per_meter.

        

        :param meters: The ForcePerLength value in meganewtons_per_meter.
        :type meganewtons_per_meter: float
        :return: A new instance of ForcePerLength.
        :rtype: ForcePerLength
        """
        return ForcePerLength(meganewtons_per_meter, ForcePerLengthUnits.MeganewtonPerMeter)

    
    @staticmethod
    def from_nanonewtons_per_centimeter(nanonewtons_per_centimeter: float):
        """
        Create a new instance of ForcePerLength from a value in nanonewtons_per_centimeter.

        

        :param meters: The ForcePerLength value in nanonewtons_per_centimeter.
        :type nanonewtons_per_centimeter: float
        :return: A new instance of ForcePerLength.
        :rtype: ForcePerLength
        """
        return ForcePerLength(nanonewtons_per_centimeter, ForcePerLengthUnits.NanonewtonPerCentimeter)

    
    @staticmethod
    def from_micronewtons_per_centimeter(micronewtons_per_centimeter: float):
        """
        Create a new instance of ForcePerLength from a value in micronewtons_per_centimeter.

        

        :param meters: The ForcePerLength value in micronewtons_per_centimeter.
        :type micronewtons_per_centimeter: float
        :return: A new instance of ForcePerLength.
        :rtype: ForcePerLength
        """
        return ForcePerLength(micronewtons_per_centimeter, ForcePerLengthUnits.MicronewtonPerCentimeter)

    
    @staticmethod
    def from_millinewtons_per_centimeter(millinewtons_per_centimeter: float):
        """
        Create a new instance of ForcePerLength from a value in millinewtons_per_centimeter.

        

        :param meters: The ForcePerLength value in millinewtons_per_centimeter.
        :type millinewtons_per_centimeter: float
        :return: A new instance of ForcePerLength.
        :rtype: ForcePerLength
        """
        return ForcePerLength(millinewtons_per_centimeter, ForcePerLengthUnits.MillinewtonPerCentimeter)

    
    @staticmethod
    def from_centinewtons_per_centimeter(centinewtons_per_centimeter: float):
        """
        Create a new instance of ForcePerLength from a value in centinewtons_per_centimeter.

        

        :param meters: The ForcePerLength value in centinewtons_per_centimeter.
        :type centinewtons_per_centimeter: float
        :return: A new instance of ForcePerLength.
        :rtype: ForcePerLength
        """
        return ForcePerLength(centinewtons_per_centimeter, ForcePerLengthUnits.CentinewtonPerCentimeter)

    
    @staticmethod
    def from_decinewtons_per_centimeter(decinewtons_per_centimeter: float):
        """
        Create a new instance of ForcePerLength from a value in decinewtons_per_centimeter.

        

        :param meters: The ForcePerLength value in decinewtons_per_centimeter.
        :type decinewtons_per_centimeter: float
        :return: A new instance of ForcePerLength.
        :rtype: ForcePerLength
        """
        return ForcePerLength(decinewtons_per_centimeter, ForcePerLengthUnits.DecinewtonPerCentimeter)

    
    @staticmethod
    def from_decanewtons_per_centimeter(decanewtons_per_centimeter: float):
        """
        Create a new instance of ForcePerLength from a value in decanewtons_per_centimeter.

        

        :param meters: The ForcePerLength value in decanewtons_per_centimeter.
        :type decanewtons_per_centimeter: float
        :return: A new instance of ForcePerLength.
        :rtype: ForcePerLength
        """
        return ForcePerLength(decanewtons_per_centimeter, ForcePerLengthUnits.DecanewtonPerCentimeter)

    
    @staticmethod
    def from_kilonewtons_per_centimeter(kilonewtons_per_centimeter: float):
        """
        Create a new instance of ForcePerLength from a value in kilonewtons_per_centimeter.

        

        :param meters: The ForcePerLength value in kilonewtons_per_centimeter.
        :type kilonewtons_per_centimeter: float
        :return: A new instance of ForcePerLength.
        :rtype: ForcePerLength
        """
        return ForcePerLength(kilonewtons_per_centimeter, ForcePerLengthUnits.KilonewtonPerCentimeter)

    
    @staticmethod
    def from_meganewtons_per_centimeter(meganewtons_per_centimeter: float):
        """
        Create a new instance of ForcePerLength from a value in meganewtons_per_centimeter.

        

        :param meters: The ForcePerLength value in meganewtons_per_centimeter.
        :type meganewtons_per_centimeter: float
        :return: A new instance of ForcePerLength.
        :rtype: ForcePerLength
        """
        return ForcePerLength(meganewtons_per_centimeter, ForcePerLengthUnits.MeganewtonPerCentimeter)

    
    @staticmethod
    def from_nanonewtons_per_millimeter(nanonewtons_per_millimeter: float):
        """
        Create a new instance of ForcePerLength from a value in nanonewtons_per_millimeter.

        

        :param meters: The ForcePerLength value in nanonewtons_per_millimeter.
        :type nanonewtons_per_millimeter: float
        :return: A new instance of ForcePerLength.
        :rtype: ForcePerLength
        """
        return ForcePerLength(nanonewtons_per_millimeter, ForcePerLengthUnits.NanonewtonPerMillimeter)

    
    @staticmethod
    def from_micronewtons_per_millimeter(micronewtons_per_millimeter: float):
        """
        Create a new instance of ForcePerLength from a value in micronewtons_per_millimeter.

        

        :param meters: The ForcePerLength value in micronewtons_per_millimeter.
        :type micronewtons_per_millimeter: float
        :return: A new instance of ForcePerLength.
        :rtype: ForcePerLength
        """
        return ForcePerLength(micronewtons_per_millimeter, ForcePerLengthUnits.MicronewtonPerMillimeter)

    
    @staticmethod
    def from_millinewtons_per_millimeter(millinewtons_per_millimeter: float):
        """
        Create a new instance of ForcePerLength from a value in millinewtons_per_millimeter.

        

        :param meters: The ForcePerLength value in millinewtons_per_millimeter.
        :type millinewtons_per_millimeter: float
        :return: A new instance of ForcePerLength.
        :rtype: ForcePerLength
        """
        return ForcePerLength(millinewtons_per_millimeter, ForcePerLengthUnits.MillinewtonPerMillimeter)

    
    @staticmethod
    def from_centinewtons_per_millimeter(centinewtons_per_millimeter: float):
        """
        Create a new instance of ForcePerLength from a value in centinewtons_per_millimeter.

        

        :param meters: The ForcePerLength value in centinewtons_per_millimeter.
        :type centinewtons_per_millimeter: float
        :return: A new instance of ForcePerLength.
        :rtype: ForcePerLength
        """
        return ForcePerLength(centinewtons_per_millimeter, ForcePerLengthUnits.CentinewtonPerMillimeter)

    
    @staticmethod
    def from_decinewtons_per_millimeter(decinewtons_per_millimeter: float):
        """
        Create a new instance of ForcePerLength from a value in decinewtons_per_millimeter.

        

        :param meters: The ForcePerLength value in decinewtons_per_millimeter.
        :type decinewtons_per_millimeter: float
        :return: A new instance of ForcePerLength.
        :rtype: ForcePerLength
        """
        return ForcePerLength(decinewtons_per_millimeter, ForcePerLengthUnits.DecinewtonPerMillimeter)

    
    @staticmethod
    def from_decanewtons_per_millimeter(decanewtons_per_millimeter: float):
        """
        Create a new instance of ForcePerLength from a value in decanewtons_per_millimeter.

        

        :param meters: The ForcePerLength value in decanewtons_per_millimeter.
        :type decanewtons_per_millimeter: float
        :return: A new instance of ForcePerLength.
        :rtype: ForcePerLength
        """
        return ForcePerLength(decanewtons_per_millimeter, ForcePerLengthUnits.DecanewtonPerMillimeter)

    
    @staticmethod
    def from_kilonewtons_per_millimeter(kilonewtons_per_millimeter: float):
        """
        Create a new instance of ForcePerLength from a value in kilonewtons_per_millimeter.

        

        :param meters: The ForcePerLength value in kilonewtons_per_millimeter.
        :type kilonewtons_per_millimeter: float
        :return: A new instance of ForcePerLength.
        :rtype: ForcePerLength
        """
        return ForcePerLength(kilonewtons_per_millimeter, ForcePerLengthUnits.KilonewtonPerMillimeter)

    
    @staticmethod
    def from_meganewtons_per_millimeter(meganewtons_per_millimeter: float):
        """
        Create a new instance of ForcePerLength from a value in meganewtons_per_millimeter.

        

        :param meters: The ForcePerLength value in meganewtons_per_millimeter.
        :type meganewtons_per_millimeter: float
        :return: A new instance of ForcePerLength.
        :rtype: ForcePerLength
        """
        return ForcePerLength(meganewtons_per_millimeter, ForcePerLengthUnits.MeganewtonPerMillimeter)

    
    @property
    def newtons_per_meter(self) -> float:
        """
        
        """
        if self.__newtons_per_meter != None:
            return self.__newtons_per_meter
        self.__newtons_per_meter = self.__convert_from_base(ForcePerLengthUnits.NewtonPerMeter)
        return self.__newtons_per_meter

    
    @property
    def newtons_per_centimeter(self) -> float:
        """
        
        """
        if self.__newtons_per_centimeter != None:
            return self.__newtons_per_centimeter
        self.__newtons_per_centimeter = self.__convert_from_base(ForcePerLengthUnits.NewtonPerCentimeter)
        return self.__newtons_per_centimeter

    
    @property
    def newtons_per_millimeter(self) -> float:
        """
        
        """
        if self.__newtons_per_millimeter != None:
            return self.__newtons_per_millimeter
        self.__newtons_per_millimeter = self.__convert_from_base(ForcePerLengthUnits.NewtonPerMillimeter)
        return self.__newtons_per_millimeter

    
    @property
    def kilograms_force_per_meter(self) -> float:
        """
        
        """
        if self.__kilograms_force_per_meter != None:
            return self.__kilograms_force_per_meter
        self.__kilograms_force_per_meter = self.__convert_from_base(ForcePerLengthUnits.KilogramForcePerMeter)
        return self.__kilograms_force_per_meter

    
    @property
    def kilograms_force_per_centimeter(self) -> float:
        """
        
        """
        if self.__kilograms_force_per_centimeter != None:
            return self.__kilograms_force_per_centimeter
        self.__kilograms_force_per_centimeter = self.__convert_from_base(ForcePerLengthUnits.KilogramForcePerCentimeter)
        return self.__kilograms_force_per_centimeter

    
    @property
    def kilograms_force_per_millimeter(self) -> float:
        """
        
        """
        if self.__kilograms_force_per_millimeter != None:
            return self.__kilograms_force_per_millimeter
        self.__kilograms_force_per_millimeter = self.__convert_from_base(ForcePerLengthUnits.KilogramForcePerMillimeter)
        return self.__kilograms_force_per_millimeter

    
    @property
    def tonnes_force_per_meter(self) -> float:
        """
        
        """
        if self.__tonnes_force_per_meter != None:
            return self.__tonnes_force_per_meter
        self.__tonnes_force_per_meter = self.__convert_from_base(ForcePerLengthUnits.TonneForcePerMeter)
        return self.__tonnes_force_per_meter

    
    @property
    def tonnes_force_per_centimeter(self) -> float:
        """
        
        """
        if self.__tonnes_force_per_centimeter != None:
            return self.__tonnes_force_per_centimeter
        self.__tonnes_force_per_centimeter = self.__convert_from_base(ForcePerLengthUnits.TonneForcePerCentimeter)
        return self.__tonnes_force_per_centimeter

    
    @property
    def tonnes_force_per_millimeter(self) -> float:
        """
        
        """
        if self.__tonnes_force_per_millimeter != None:
            return self.__tonnes_force_per_millimeter
        self.__tonnes_force_per_millimeter = self.__convert_from_base(ForcePerLengthUnits.TonneForcePerMillimeter)
        return self.__tonnes_force_per_millimeter

    
    @property
    def pounds_force_per_foot(self) -> float:
        """
        
        """
        if self.__pounds_force_per_foot != None:
            return self.__pounds_force_per_foot
        self.__pounds_force_per_foot = self.__convert_from_base(ForcePerLengthUnits.PoundForcePerFoot)
        return self.__pounds_force_per_foot

    
    @property
    def pounds_force_per_inch(self) -> float:
        """
        
        """
        if self.__pounds_force_per_inch != None:
            return self.__pounds_force_per_inch
        self.__pounds_force_per_inch = self.__convert_from_base(ForcePerLengthUnits.PoundForcePerInch)
        return self.__pounds_force_per_inch

    
    @property
    def pounds_force_per_yard(self) -> float:
        """
        
        """
        if self.__pounds_force_per_yard != None:
            return self.__pounds_force_per_yard
        self.__pounds_force_per_yard = self.__convert_from_base(ForcePerLengthUnits.PoundForcePerYard)
        return self.__pounds_force_per_yard

    
    @property
    def kilopounds_force_per_foot(self) -> float:
        """
        
        """
        if self.__kilopounds_force_per_foot != None:
            return self.__kilopounds_force_per_foot
        self.__kilopounds_force_per_foot = self.__convert_from_base(ForcePerLengthUnits.KilopoundForcePerFoot)
        return self.__kilopounds_force_per_foot

    
    @property
    def kilopounds_force_per_inch(self) -> float:
        """
        
        """
        if self.__kilopounds_force_per_inch != None:
            return self.__kilopounds_force_per_inch
        self.__kilopounds_force_per_inch = self.__convert_from_base(ForcePerLengthUnits.KilopoundForcePerInch)
        return self.__kilopounds_force_per_inch

    
    @property
    def nanonewtons_per_meter(self) -> float:
        """
        
        """
        if self.__nanonewtons_per_meter != None:
            return self.__nanonewtons_per_meter
        self.__nanonewtons_per_meter = self.__convert_from_base(ForcePerLengthUnits.NanonewtonPerMeter)
        return self.__nanonewtons_per_meter

    
    @property
    def micronewtons_per_meter(self) -> float:
        """
        
        """
        if self.__micronewtons_per_meter != None:
            return self.__micronewtons_per_meter
        self.__micronewtons_per_meter = self.__convert_from_base(ForcePerLengthUnits.MicronewtonPerMeter)
        return self.__micronewtons_per_meter

    
    @property
    def millinewtons_per_meter(self) -> float:
        """
        
        """
        if self.__millinewtons_per_meter != None:
            return self.__millinewtons_per_meter
        self.__millinewtons_per_meter = self.__convert_from_base(ForcePerLengthUnits.MillinewtonPerMeter)
        return self.__millinewtons_per_meter

    
    @property
    def centinewtons_per_meter(self) -> float:
        """
        
        """
        if self.__centinewtons_per_meter != None:
            return self.__centinewtons_per_meter
        self.__centinewtons_per_meter = self.__convert_from_base(ForcePerLengthUnits.CentinewtonPerMeter)
        return self.__centinewtons_per_meter

    
    @property
    def decinewtons_per_meter(self) -> float:
        """
        
        """
        if self.__decinewtons_per_meter != None:
            return self.__decinewtons_per_meter
        self.__decinewtons_per_meter = self.__convert_from_base(ForcePerLengthUnits.DecinewtonPerMeter)
        return self.__decinewtons_per_meter

    
    @property
    def decanewtons_per_meter(self) -> float:
        """
        
        """
        if self.__decanewtons_per_meter != None:
            return self.__decanewtons_per_meter
        self.__decanewtons_per_meter = self.__convert_from_base(ForcePerLengthUnits.DecanewtonPerMeter)
        return self.__decanewtons_per_meter

    
    @property
    def kilonewtons_per_meter(self) -> float:
        """
        
        """
        if self.__kilonewtons_per_meter != None:
            return self.__kilonewtons_per_meter
        self.__kilonewtons_per_meter = self.__convert_from_base(ForcePerLengthUnits.KilonewtonPerMeter)
        return self.__kilonewtons_per_meter

    
    @property
    def meganewtons_per_meter(self) -> float:
        """
        
        """
        if self.__meganewtons_per_meter != None:
            return self.__meganewtons_per_meter
        self.__meganewtons_per_meter = self.__convert_from_base(ForcePerLengthUnits.MeganewtonPerMeter)
        return self.__meganewtons_per_meter

    
    @property
    def nanonewtons_per_centimeter(self) -> float:
        """
        
        """
        if self.__nanonewtons_per_centimeter != None:
            return self.__nanonewtons_per_centimeter
        self.__nanonewtons_per_centimeter = self.__convert_from_base(ForcePerLengthUnits.NanonewtonPerCentimeter)
        return self.__nanonewtons_per_centimeter

    
    @property
    def micronewtons_per_centimeter(self) -> float:
        """
        
        """
        if self.__micronewtons_per_centimeter != None:
            return self.__micronewtons_per_centimeter
        self.__micronewtons_per_centimeter = self.__convert_from_base(ForcePerLengthUnits.MicronewtonPerCentimeter)
        return self.__micronewtons_per_centimeter

    
    @property
    def millinewtons_per_centimeter(self) -> float:
        """
        
        """
        if self.__millinewtons_per_centimeter != None:
            return self.__millinewtons_per_centimeter
        self.__millinewtons_per_centimeter = self.__convert_from_base(ForcePerLengthUnits.MillinewtonPerCentimeter)
        return self.__millinewtons_per_centimeter

    
    @property
    def centinewtons_per_centimeter(self) -> float:
        """
        
        """
        if self.__centinewtons_per_centimeter != None:
            return self.__centinewtons_per_centimeter
        self.__centinewtons_per_centimeter = self.__convert_from_base(ForcePerLengthUnits.CentinewtonPerCentimeter)
        return self.__centinewtons_per_centimeter

    
    @property
    def decinewtons_per_centimeter(self) -> float:
        """
        
        """
        if self.__decinewtons_per_centimeter != None:
            return self.__decinewtons_per_centimeter
        self.__decinewtons_per_centimeter = self.__convert_from_base(ForcePerLengthUnits.DecinewtonPerCentimeter)
        return self.__decinewtons_per_centimeter

    
    @property
    def decanewtons_per_centimeter(self) -> float:
        """
        
        """
        if self.__decanewtons_per_centimeter != None:
            return self.__decanewtons_per_centimeter
        self.__decanewtons_per_centimeter = self.__convert_from_base(ForcePerLengthUnits.DecanewtonPerCentimeter)
        return self.__decanewtons_per_centimeter

    
    @property
    def kilonewtons_per_centimeter(self) -> float:
        """
        
        """
        if self.__kilonewtons_per_centimeter != None:
            return self.__kilonewtons_per_centimeter
        self.__kilonewtons_per_centimeter = self.__convert_from_base(ForcePerLengthUnits.KilonewtonPerCentimeter)
        return self.__kilonewtons_per_centimeter

    
    @property
    def meganewtons_per_centimeter(self) -> float:
        """
        
        """
        if self.__meganewtons_per_centimeter != None:
            return self.__meganewtons_per_centimeter
        self.__meganewtons_per_centimeter = self.__convert_from_base(ForcePerLengthUnits.MeganewtonPerCentimeter)
        return self.__meganewtons_per_centimeter

    
    @property
    def nanonewtons_per_millimeter(self) -> float:
        """
        
        """
        if self.__nanonewtons_per_millimeter != None:
            return self.__nanonewtons_per_millimeter
        self.__nanonewtons_per_millimeter = self.__convert_from_base(ForcePerLengthUnits.NanonewtonPerMillimeter)
        return self.__nanonewtons_per_millimeter

    
    @property
    def micronewtons_per_millimeter(self) -> float:
        """
        
        """
        if self.__micronewtons_per_millimeter != None:
            return self.__micronewtons_per_millimeter
        self.__micronewtons_per_millimeter = self.__convert_from_base(ForcePerLengthUnits.MicronewtonPerMillimeter)
        return self.__micronewtons_per_millimeter

    
    @property
    def millinewtons_per_millimeter(self) -> float:
        """
        
        """
        if self.__millinewtons_per_millimeter != None:
            return self.__millinewtons_per_millimeter
        self.__millinewtons_per_millimeter = self.__convert_from_base(ForcePerLengthUnits.MillinewtonPerMillimeter)
        return self.__millinewtons_per_millimeter

    
    @property
    def centinewtons_per_millimeter(self) -> float:
        """
        
        """
        if self.__centinewtons_per_millimeter != None:
            return self.__centinewtons_per_millimeter
        self.__centinewtons_per_millimeter = self.__convert_from_base(ForcePerLengthUnits.CentinewtonPerMillimeter)
        return self.__centinewtons_per_millimeter

    
    @property
    def decinewtons_per_millimeter(self) -> float:
        """
        
        """
        if self.__decinewtons_per_millimeter != None:
            return self.__decinewtons_per_millimeter
        self.__decinewtons_per_millimeter = self.__convert_from_base(ForcePerLengthUnits.DecinewtonPerMillimeter)
        return self.__decinewtons_per_millimeter

    
    @property
    def decanewtons_per_millimeter(self) -> float:
        """
        
        """
        if self.__decanewtons_per_millimeter != None:
            return self.__decanewtons_per_millimeter
        self.__decanewtons_per_millimeter = self.__convert_from_base(ForcePerLengthUnits.DecanewtonPerMillimeter)
        return self.__decanewtons_per_millimeter

    
    @property
    def kilonewtons_per_millimeter(self) -> float:
        """
        
        """
        if self.__kilonewtons_per_millimeter != None:
            return self.__kilonewtons_per_millimeter
        self.__kilonewtons_per_millimeter = self.__convert_from_base(ForcePerLengthUnits.KilonewtonPerMillimeter)
        return self.__kilonewtons_per_millimeter

    
    @property
    def meganewtons_per_millimeter(self) -> float:
        """
        
        """
        if self.__meganewtons_per_millimeter != None:
            return self.__meganewtons_per_millimeter
        self.__meganewtons_per_millimeter = self.__convert_from_base(ForcePerLengthUnits.MeganewtonPerMillimeter)
        return self.__meganewtons_per_millimeter

    
    def to_string(self, unit: ForcePerLengthUnits = ForcePerLengthUnits.NewtonPerMeter) -> str:
        """
        Format the ForcePerLength to string.
        Note! the default format for ForcePerLength is NewtonPerMeter.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == ForcePerLengthUnits.NewtonPerMeter:
            return f"""{self.newtons_per_meter} N/m"""
        
        if unit == ForcePerLengthUnits.NewtonPerCentimeter:
            return f"""{self.newtons_per_centimeter} N/cm"""
        
        if unit == ForcePerLengthUnits.NewtonPerMillimeter:
            return f"""{self.newtons_per_millimeter} N/mm"""
        
        if unit == ForcePerLengthUnits.KilogramForcePerMeter:
            return f"""{self.kilograms_force_per_meter} kgf/m"""
        
        if unit == ForcePerLengthUnits.KilogramForcePerCentimeter:
            return f"""{self.kilograms_force_per_centimeter} kgf/cm"""
        
        if unit == ForcePerLengthUnits.KilogramForcePerMillimeter:
            return f"""{self.kilograms_force_per_millimeter} kgf/mm"""
        
        if unit == ForcePerLengthUnits.TonneForcePerMeter:
            return f"""{self.tonnes_force_per_meter} tf/m"""
        
        if unit == ForcePerLengthUnits.TonneForcePerCentimeter:
            return f"""{self.tonnes_force_per_centimeter} tf/cm"""
        
        if unit == ForcePerLengthUnits.TonneForcePerMillimeter:
            return f"""{self.tonnes_force_per_millimeter} tf/mm"""
        
        if unit == ForcePerLengthUnits.PoundForcePerFoot:
            return f"""{self.pounds_force_per_foot} lbf/ft"""
        
        if unit == ForcePerLengthUnits.PoundForcePerInch:
            return f"""{self.pounds_force_per_inch} lbf/in"""
        
        if unit == ForcePerLengthUnits.PoundForcePerYard:
            return f"""{self.pounds_force_per_yard} lbf/yd"""
        
        if unit == ForcePerLengthUnits.KilopoundForcePerFoot:
            return f"""{self.kilopounds_force_per_foot} kipf/ft"""
        
        if unit == ForcePerLengthUnits.KilopoundForcePerInch:
            return f"""{self.kilopounds_force_per_inch} kipf/in"""
        
        if unit == ForcePerLengthUnits.NanonewtonPerMeter:
            return f"""{self.nanonewtons_per_meter} nN/m"""
        
        if unit == ForcePerLengthUnits.MicronewtonPerMeter:
            return f"""{self.micronewtons_per_meter} μN/m"""
        
        if unit == ForcePerLengthUnits.MillinewtonPerMeter:
            return f"""{self.millinewtons_per_meter} mN/m"""
        
        if unit == ForcePerLengthUnits.CentinewtonPerMeter:
            return f"""{self.centinewtons_per_meter} cN/m"""
        
        if unit == ForcePerLengthUnits.DecinewtonPerMeter:
            return f"""{self.decinewtons_per_meter} dN/m"""
        
        if unit == ForcePerLengthUnits.DecanewtonPerMeter:
            return f"""{self.decanewtons_per_meter} daN/m"""
        
        if unit == ForcePerLengthUnits.KilonewtonPerMeter:
            return f"""{self.kilonewtons_per_meter} kN/m"""
        
        if unit == ForcePerLengthUnits.MeganewtonPerMeter:
            return f"""{self.meganewtons_per_meter} MN/m"""
        
        if unit == ForcePerLengthUnits.NanonewtonPerCentimeter:
            return f"""{self.nanonewtons_per_centimeter} nN/cm"""
        
        if unit == ForcePerLengthUnits.MicronewtonPerCentimeter:
            return f"""{self.micronewtons_per_centimeter} μN/cm"""
        
        if unit == ForcePerLengthUnits.MillinewtonPerCentimeter:
            return f"""{self.millinewtons_per_centimeter} mN/cm"""
        
        if unit == ForcePerLengthUnits.CentinewtonPerCentimeter:
            return f"""{self.centinewtons_per_centimeter} cN/cm"""
        
        if unit == ForcePerLengthUnits.DecinewtonPerCentimeter:
            return f"""{self.decinewtons_per_centimeter} dN/cm"""
        
        if unit == ForcePerLengthUnits.DecanewtonPerCentimeter:
            return f"""{self.decanewtons_per_centimeter} daN/cm"""
        
        if unit == ForcePerLengthUnits.KilonewtonPerCentimeter:
            return f"""{self.kilonewtons_per_centimeter} kN/cm"""
        
        if unit == ForcePerLengthUnits.MeganewtonPerCentimeter:
            return f"""{self.meganewtons_per_centimeter} MN/cm"""
        
        if unit == ForcePerLengthUnits.NanonewtonPerMillimeter:
            return f"""{self.nanonewtons_per_millimeter} nN/mm"""
        
        if unit == ForcePerLengthUnits.MicronewtonPerMillimeter:
            return f"""{self.micronewtons_per_millimeter} μN/mm"""
        
        if unit == ForcePerLengthUnits.MillinewtonPerMillimeter:
            return f"""{self.millinewtons_per_millimeter} mN/mm"""
        
        if unit == ForcePerLengthUnits.CentinewtonPerMillimeter:
            return f"""{self.centinewtons_per_millimeter} cN/mm"""
        
        if unit == ForcePerLengthUnits.DecinewtonPerMillimeter:
            return f"""{self.decinewtons_per_millimeter} dN/mm"""
        
        if unit == ForcePerLengthUnits.DecanewtonPerMillimeter:
            return f"""{self.decanewtons_per_millimeter} daN/mm"""
        
        if unit == ForcePerLengthUnits.KilonewtonPerMillimeter:
            return f"""{self.kilonewtons_per_millimeter} kN/mm"""
        
        if unit == ForcePerLengthUnits.MeganewtonPerMillimeter:
            return f"""{self.meganewtons_per_millimeter} MN/mm"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: ForcePerLengthUnits = ForcePerLengthUnits.NewtonPerMeter) -> str:
        """
        Get ForcePerLength unit abbreviation.
        Note! the default abbreviation for ForcePerLength is NewtonPerMeter.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == ForcePerLengthUnits.NewtonPerMeter:
            return """N/m"""
        
        if unit_abbreviation == ForcePerLengthUnits.NewtonPerCentimeter:
            return """N/cm"""
        
        if unit_abbreviation == ForcePerLengthUnits.NewtonPerMillimeter:
            return """N/mm"""
        
        if unit_abbreviation == ForcePerLengthUnits.KilogramForcePerMeter:
            return """kgf/m"""
        
        if unit_abbreviation == ForcePerLengthUnits.KilogramForcePerCentimeter:
            return """kgf/cm"""
        
        if unit_abbreviation == ForcePerLengthUnits.KilogramForcePerMillimeter:
            return """kgf/mm"""
        
        if unit_abbreviation == ForcePerLengthUnits.TonneForcePerMeter:
            return """tf/m"""
        
        if unit_abbreviation == ForcePerLengthUnits.TonneForcePerCentimeter:
            return """tf/cm"""
        
        if unit_abbreviation == ForcePerLengthUnits.TonneForcePerMillimeter:
            return """tf/mm"""
        
        if unit_abbreviation == ForcePerLengthUnits.PoundForcePerFoot:
            return """lbf/ft"""
        
        if unit_abbreviation == ForcePerLengthUnits.PoundForcePerInch:
            return """lbf/in"""
        
        if unit_abbreviation == ForcePerLengthUnits.PoundForcePerYard:
            return """lbf/yd"""
        
        if unit_abbreviation == ForcePerLengthUnits.KilopoundForcePerFoot:
            return """kipf/ft"""
        
        if unit_abbreviation == ForcePerLengthUnits.KilopoundForcePerInch:
            return """kipf/in"""
        
        if unit_abbreviation == ForcePerLengthUnits.NanonewtonPerMeter:
            return """nN/m"""
        
        if unit_abbreviation == ForcePerLengthUnits.MicronewtonPerMeter:
            return """μN/m"""
        
        if unit_abbreviation == ForcePerLengthUnits.MillinewtonPerMeter:
            return """mN/m"""
        
        if unit_abbreviation == ForcePerLengthUnits.CentinewtonPerMeter:
            return """cN/m"""
        
        if unit_abbreviation == ForcePerLengthUnits.DecinewtonPerMeter:
            return """dN/m"""
        
        if unit_abbreviation == ForcePerLengthUnits.DecanewtonPerMeter:
            return """daN/m"""
        
        if unit_abbreviation == ForcePerLengthUnits.KilonewtonPerMeter:
            return """kN/m"""
        
        if unit_abbreviation == ForcePerLengthUnits.MeganewtonPerMeter:
            return """MN/m"""
        
        if unit_abbreviation == ForcePerLengthUnits.NanonewtonPerCentimeter:
            return """nN/cm"""
        
        if unit_abbreviation == ForcePerLengthUnits.MicronewtonPerCentimeter:
            return """μN/cm"""
        
        if unit_abbreviation == ForcePerLengthUnits.MillinewtonPerCentimeter:
            return """mN/cm"""
        
        if unit_abbreviation == ForcePerLengthUnits.CentinewtonPerCentimeter:
            return """cN/cm"""
        
        if unit_abbreviation == ForcePerLengthUnits.DecinewtonPerCentimeter:
            return """dN/cm"""
        
        if unit_abbreviation == ForcePerLengthUnits.DecanewtonPerCentimeter:
            return """daN/cm"""
        
        if unit_abbreviation == ForcePerLengthUnits.KilonewtonPerCentimeter:
            return """kN/cm"""
        
        if unit_abbreviation == ForcePerLengthUnits.MeganewtonPerCentimeter:
            return """MN/cm"""
        
        if unit_abbreviation == ForcePerLengthUnits.NanonewtonPerMillimeter:
            return """nN/mm"""
        
        if unit_abbreviation == ForcePerLengthUnits.MicronewtonPerMillimeter:
            return """μN/mm"""
        
        if unit_abbreviation == ForcePerLengthUnits.MillinewtonPerMillimeter:
            return """mN/mm"""
        
        if unit_abbreviation == ForcePerLengthUnits.CentinewtonPerMillimeter:
            return """cN/mm"""
        
        if unit_abbreviation == ForcePerLengthUnits.DecinewtonPerMillimeter:
            return """dN/mm"""
        
        if unit_abbreviation == ForcePerLengthUnits.DecanewtonPerMillimeter:
            return """daN/mm"""
        
        if unit_abbreviation == ForcePerLengthUnits.KilonewtonPerMillimeter:
            return """kN/mm"""
        
        if unit_abbreviation == ForcePerLengthUnits.MeganewtonPerMillimeter:
            return """MN/mm"""
        
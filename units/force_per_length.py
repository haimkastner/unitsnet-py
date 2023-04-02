from enum import Enum
import math
import string


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
        
        NanoNewtonPerMeter = 'nano_newton_per_meter'
        """
            
        """
        
        MicroNewtonPerMeter = 'micro_newton_per_meter'
        """
            
        """
        
        MilliNewtonPerMeter = 'milli_newton_per_meter'
        """
            
        """
        
        CentiNewtonPerMeter = 'centi_newton_per_meter'
        """
            
        """
        
        DeciNewtonPerMeter = 'deci_newton_per_meter'
        """
            
        """
        
        DecaNewtonPerMeter = 'deca_newton_per_meter'
        """
            
        """
        
        KiloNewtonPerMeter = 'kilo_newton_per_meter'
        """
            
        """
        
        MegaNewtonPerMeter = 'mega_newton_per_meter'
        """
            
        """
        
        NanoNewtonPerCentimeter = 'nano_newton_per_centimeter'
        """
            
        """
        
        MicroNewtonPerCentimeter = 'micro_newton_per_centimeter'
        """
            
        """
        
        MilliNewtonPerCentimeter = 'milli_newton_per_centimeter'
        """
            
        """
        
        CentiNewtonPerCentimeter = 'centi_newton_per_centimeter'
        """
            
        """
        
        DeciNewtonPerCentimeter = 'deci_newton_per_centimeter'
        """
            
        """
        
        DecaNewtonPerCentimeter = 'deca_newton_per_centimeter'
        """
            
        """
        
        KiloNewtonPerCentimeter = 'kilo_newton_per_centimeter'
        """
            
        """
        
        MegaNewtonPerCentimeter = 'mega_newton_per_centimeter'
        """
            
        """
        
        NanoNewtonPerMillimeter = 'nano_newton_per_millimeter'
        """
            
        """
        
        MicroNewtonPerMillimeter = 'micro_newton_per_millimeter'
        """
            
        """
        
        MilliNewtonPerMillimeter = 'milli_newton_per_millimeter'
        """
            
        """
        
        CentiNewtonPerMillimeter = 'centi_newton_per_millimeter'
        """
            
        """
        
        DeciNewtonPerMillimeter = 'deci_newton_per_millimeter'
        """
            
        """
        
        DecaNewtonPerMillimeter = 'deca_newton_per_millimeter'
        """
            
        """
        
        KiloNewtonPerMillimeter = 'kilo_newton_per_millimeter'
        """
            
        """
        
        MegaNewtonPerMillimeter = 'mega_newton_per_millimeter'
        """
            
        """
        

class ForcePerLength:
    """
    The magnitude of force per unit length.

    Args:
        value (float): The value.
        from_unit (ForcePerLengthUnits): The ForcePerLength unit to create from, The default unit is NewtonPerMeter
    """
    def __init__(self, value: float, from_unit: ForcePerLengthUnits = ForcePerLengthUnits.NewtonPerMeter):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
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
        
        self.__nano_newtons_per_meter = None
        
        self.__micro_newtons_per_meter = None
        
        self.__milli_newtons_per_meter = None
        
        self.__centi_newtons_per_meter = None
        
        self.__deci_newtons_per_meter = None
        
        self.__deca_newtons_per_meter = None
        
        self.__kilo_newtons_per_meter = None
        
        self.__mega_newtons_per_meter = None
        
        self.__nano_newtons_per_centimeter = None
        
        self.__micro_newtons_per_centimeter = None
        
        self.__milli_newtons_per_centimeter = None
        
        self.__centi_newtons_per_centimeter = None
        
        self.__deci_newtons_per_centimeter = None
        
        self.__deca_newtons_per_centimeter = None
        
        self.__kilo_newtons_per_centimeter = None
        
        self.__mega_newtons_per_centimeter = None
        
        self.__nano_newtons_per_millimeter = None
        
        self.__micro_newtons_per_millimeter = None
        
        self.__milli_newtons_per_millimeter = None
        
        self.__centi_newtons_per_millimeter = None
        
        self.__deci_newtons_per_millimeter = None
        
        self.__deca_newtons_per_millimeter = None
        
        self.__kilo_newtons_per_millimeter = None
        
        self.__mega_newtons_per_millimeter = None
        

    def __convert_from_base(self, from_unit: ForcePerLengthUnits) -> float:
        value = self.__value
        
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
        
        if from_unit == ForcePerLengthUnits.NanoNewtonPerMeter:
            return ((value) / 1e-09)
        
        if from_unit == ForcePerLengthUnits.MicroNewtonPerMeter:
            return ((value) / 1e-06)
        
        if from_unit == ForcePerLengthUnits.MilliNewtonPerMeter:
            return ((value) / 0.001)
        
        if from_unit == ForcePerLengthUnits.CentiNewtonPerMeter:
            return ((value) / 0.01)
        
        if from_unit == ForcePerLengthUnits.DeciNewtonPerMeter:
            return ((value) / 0.1)
        
        if from_unit == ForcePerLengthUnits.DecaNewtonPerMeter:
            return ((value) / 10.0)
        
        if from_unit == ForcePerLengthUnits.KiloNewtonPerMeter:
            return ((value) / 1000.0)
        
        if from_unit == ForcePerLengthUnits.MegaNewtonPerMeter:
            return ((value) / 1000000.0)
        
        if from_unit == ForcePerLengthUnits.NanoNewtonPerCentimeter:
            return ((value / 1e2) / 1e-09)
        
        if from_unit == ForcePerLengthUnits.MicroNewtonPerCentimeter:
            return ((value / 1e2) / 1e-06)
        
        if from_unit == ForcePerLengthUnits.MilliNewtonPerCentimeter:
            return ((value / 1e2) / 0.001)
        
        if from_unit == ForcePerLengthUnits.CentiNewtonPerCentimeter:
            return ((value / 1e2) / 0.01)
        
        if from_unit == ForcePerLengthUnits.DeciNewtonPerCentimeter:
            return ((value / 1e2) / 0.1)
        
        if from_unit == ForcePerLengthUnits.DecaNewtonPerCentimeter:
            return ((value / 1e2) / 10.0)
        
        if from_unit == ForcePerLengthUnits.KiloNewtonPerCentimeter:
            return ((value / 1e2) / 1000.0)
        
        if from_unit == ForcePerLengthUnits.MegaNewtonPerCentimeter:
            return ((value / 1e2) / 1000000.0)
        
        if from_unit == ForcePerLengthUnits.NanoNewtonPerMillimeter:
            return ((value / 1e3) / 1e-09)
        
        if from_unit == ForcePerLengthUnits.MicroNewtonPerMillimeter:
            return ((value / 1e3) / 1e-06)
        
        if from_unit == ForcePerLengthUnits.MilliNewtonPerMillimeter:
            return ((value / 1e3) / 0.001)
        
        if from_unit == ForcePerLengthUnits.CentiNewtonPerMillimeter:
            return ((value / 1e3) / 0.01)
        
        if from_unit == ForcePerLengthUnits.DeciNewtonPerMillimeter:
            return ((value / 1e3) / 0.1)
        
        if from_unit == ForcePerLengthUnits.DecaNewtonPerMillimeter:
            return ((value / 1e3) / 10.0)
        
        if from_unit == ForcePerLengthUnits.KiloNewtonPerMillimeter:
            return ((value / 1e3) / 1000.0)
        
        if from_unit == ForcePerLengthUnits.MegaNewtonPerMillimeter:
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
        
        if to_unit == ForcePerLengthUnits.NanoNewtonPerMeter:
            return ((value) * 1e-09)
        
        if to_unit == ForcePerLengthUnits.MicroNewtonPerMeter:
            return ((value) * 1e-06)
        
        if to_unit == ForcePerLengthUnits.MilliNewtonPerMeter:
            return ((value) * 0.001)
        
        if to_unit == ForcePerLengthUnits.CentiNewtonPerMeter:
            return ((value) * 0.01)
        
        if to_unit == ForcePerLengthUnits.DeciNewtonPerMeter:
            return ((value) * 0.1)
        
        if to_unit == ForcePerLengthUnits.DecaNewtonPerMeter:
            return ((value) * 10.0)
        
        if to_unit == ForcePerLengthUnits.KiloNewtonPerMeter:
            return ((value) * 1000.0)
        
        if to_unit == ForcePerLengthUnits.MegaNewtonPerMeter:
            return ((value) * 1000000.0)
        
        if to_unit == ForcePerLengthUnits.NanoNewtonPerCentimeter:
            return ((value * 1e2) * 1e-09)
        
        if to_unit == ForcePerLengthUnits.MicroNewtonPerCentimeter:
            return ((value * 1e2) * 1e-06)
        
        if to_unit == ForcePerLengthUnits.MilliNewtonPerCentimeter:
            return ((value * 1e2) * 0.001)
        
        if to_unit == ForcePerLengthUnits.CentiNewtonPerCentimeter:
            return ((value * 1e2) * 0.01)
        
        if to_unit == ForcePerLengthUnits.DeciNewtonPerCentimeter:
            return ((value * 1e2) * 0.1)
        
        if to_unit == ForcePerLengthUnits.DecaNewtonPerCentimeter:
            return ((value * 1e2) * 10.0)
        
        if to_unit == ForcePerLengthUnits.KiloNewtonPerCentimeter:
            return ((value * 1e2) * 1000.0)
        
        if to_unit == ForcePerLengthUnits.MegaNewtonPerCentimeter:
            return ((value * 1e2) * 1000000.0)
        
        if to_unit == ForcePerLengthUnits.NanoNewtonPerMillimeter:
            return ((value * 1e3) * 1e-09)
        
        if to_unit == ForcePerLengthUnits.MicroNewtonPerMillimeter:
            return ((value * 1e3) * 1e-06)
        
        if to_unit == ForcePerLengthUnits.MilliNewtonPerMillimeter:
            return ((value * 1e3) * 0.001)
        
        if to_unit == ForcePerLengthUnits.CentiNewtonPerMillimeter:
            return ((value * 1e3) * 0.01)
        
        if to_unit == ForcePerLengthUnits.DeciNewtonPerMillimeter:
            return ((value * 1e3) * 0.1)
        
        if to_unit == ForcePerLengthUnits.DecaNewtonPerMillimeter:
            return ((value * 1e3) * 10.0)
        
        if to_unit == ForcePerLengthUnits.KiloNewtonPerMillimeter:
            return ((value * 1e3) * 1000.0)
        
        if to_unit == ForcePerLengthUnits.MegaNewtonPerMillimeter:
            return ((value * 1e3) * 1000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
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
    def from_nano_newtons_per_meter(nano_newtons_per_meter: float):
        """
        Create a new instance of ForcePerLength from a value in nano_newtons_per_meter.

        

        :param meters: The ForcePerLength value in nano_newtons_per_meter.
        :type nano_newtons_per_meter: float
        :return: A new instance of ForcePerLength.
        :rtype: ForcePerLength
        """
        return ForcePerLength(nano_newtons_per_meter, ForcePerLengthUnits.NanoNewtonPerMeter)

    
    @staticmethod
    def from_micro_newtons_per_meter(micro_newtons_per_meter: float):
        """
        Create a new instance of ForcePerLength from a value in micro_newtons_per_meter.

        

        :param meters: The ForcePerLength value in micro_newtons_per_meter.
        :type micro_newtons_per_meter: float
        :return: A new instance of ForcePerLength.
        :rtype: ForcePerLength
        """
        return ForcePerLength(micro_newtons_per_meter, ForcePerLengthUnits.MicroNewtonPerMeter)

    
    @staticmethod
    def from_milli_newtons_per_meter(milli_newtons_per_meter: float):
        """
        Create a new instance of ForcePerLength from a value in milli_newtons_per_meter.

        

        :param meters: The ForcePerLength value in milli_newtons_per_meter.
        :type milli_newtons_per_meter: float
        :return: A new instance of ForcePerLength.
        :rtype: ForcePerLength
        """
        return ForcePerLength(milli_newtons_per_meter, ForcePerLengthUnits.MilliNewtonPerMeter)

    
    @staticmethod
    def from_centi_newtons_per_meter(centi_newtons_per_meter: float):
        """
        Create a new instance of ForcePerLength from a value in centi_newtons_per_meter.

        

        :param meters: The ForcePerLength value in centi_newtons_per_meter.
        :type centi_newtons_per_meter: float
        :return: A new instance of ForcePerLength.
        :rtype: ForcePerLength
        """
        return ForcePerLength(centi_newtons_per_meter, ForcePerLengthUnits.CentiNewtonPerMeter)

    
    @staticmethod
    def from_deci_newtons_per_meter(deci_newtons_per_meter: float):
        """
        Create a new instance of ForcePerLength from a value in deci_newtons_per_meter.

        

        :param meters: The ForcePerLength value in deci_newtons_per_meter.
        :type deci_newtons_per_meter: float
        :return: A new instance of ForcePerLength.
        :rtype: ForcePerLength
        """
        return ForcePerLength(deci_newtons_per_meter, ForcePerLengthUnits.DeciNewtonPerMeter)

    
    @staticmethod
    def from_deca_newtons_per_meter(deca_newtons_per_meter: float):
        """
        Create a new instance of ForcePerLength from a value in deca_newtons_per_meter.

        

        :param meters: The ForcePerLength value in deca_newtons_per_meter.
        :type deca_newtons_per_meter: float
        :return: A new instance of ForcePerLength.
        :rtype: ForcePerLength
        """
        return ForcePerLength(deca_newtons_per_meter, ForcePerLengthUnits.DecaNewtonPerMeter)

    
    @staticmethod
    def from_kilo_newtons_per_meter(kilo_newtons_per_meter: float):
        """
        Create a new instance of ForcePerLength from a value in kilo_newtons_per_meter.

        

        :param meters: The ForcePerLength value in kilo_newtons_per_meter.
        :type kilo_newtons_per_meter: float
        :return: A new instance of ForcePerLength.
        :rtype: ForcePerLength
        """
        return ForcePerLength(kilo_newtons_per_meter, ForcePerLengthUnits.KiloNewtonPerMeter)

    
    @staticmethod
    def from_mega_newtons_per_meter(mega_newtons_per_meter: float):
        """
        Create a new instance of ForcePerLength from a value in mega_newtons_per_meter.

        

        :param meters: The ForcePerLength value in mega_newtons_per_meter.
        :type mega_newtons_per_meter: float
        :return: A new instance of ForcePerLength.
        :rtype: ForcePerLength
        """
        return ForcePerLength(mega_newtons_per_meter, ForcePerLengthUnits.MegaNewtonPerMeter)

    
    @staticmethod
    def from_nano_newtons_per_centimeter(nano_newtons_per_centimeter: float):
        """
        Create a new instance of ForcePerLength from a value in nano_newtons_per_centimeter.

        

        :param meters: The ForcePerLength value in nano_newtons_per_centimeter.
        :type nano_newtons_per_centimeter: float
        :return: A new instance of ForcePerLength.
        :rtype: ForcePerLength
        """
        return ForcePerLength(nano_newtons_per_centimeter, ForcePerLengthUnits.NanoNewtonPerCentimeter)

    
    @staticmethod
    def from_micro_newtons_per_centimeter(micro_newtons_per_centimeter: float):
        """
        Create a new instance of ForcePerLength from a value in micro_newtons_per_centimeter.

        

        :param meters: The ForcePerLength value in micro_newtons_per_centimeter.
        :type micro_newtons_per_centimeter: float
        :return: A new instance of ForcePerLength.
        :rtype: ForcePerLength
        """
        return ForcePerLength(micro_newtons_per_centimeter, ForcePerLengthUnits.MicroNewtonPerCentimeter)

    
    @staticmethod
    def from_milli_newtons_per_centimeter(milli_newtons_per_centimeter: float):
        """
        Create a new instance of ForcePerLength from a value in milli_newtons_per_centimeter.

        

        :param meters: The ForcePerLength value in milli_newtons_per_centimeter.
        :type milli_newtons_per_centimeter: float
        :return: A new instance of ForcePerLength.
        :rtype: ForcePerLength
        """
        return ForcePerLength(milli_newtons_per_centimeter, ForcePerLengthUnits.MilliNewtonPerCentimeter)

    
    @staticmethod
    def from_centi_newtons_per_centimeter(centi_newtons_per_centimeter: float):
        """
        Create a new instance of ForcePerLength from a value in centi_newtons_per_centimeter.

        

        :param meters: The ForcePerLength value in centi_newtons_per_centimeter.
        :type centi_newtons_per_centimeter: float
        :return: A new instance of ForcePerLength.
        :rtype: ForcePerLength
        """
        return ForcePerLength(centi_newtons_per_centimeter, ForcePerLengthUnits.CentiNewtonPerCentimeter)

    
    @staticmethod
    def from_deci_newtons_per_centimeter(deci_newtons_per_centimeter: float):
        """
        Create a new instance of ForcePerLength from a value in deci_newtons_per_centimeter.

        

        :param meters: The ForcePerLength value in deci_newtons_per_centimeter.
        :type deci_newtons_per_centimeter: float
        :return: A new instance of ForcePerLength.
        :rtype: ForcePerLength
        """
        return ForcePerLength(deci_newtons_per_centimeter, ForcePerLengthUnits.DeciNewtonPerCentimeter)

    
    @staticmethod
    def from_deca_newtons_per_centimeter(deca_newtons_per_centimeter: float):
        """
        Create a new instance of ForcePerLength from a value in deca_newtons_per_centimeter.

        

        :param meters: The ForcePerLength value in deca_newtons_per_centimeter.
        :type deca_newtons_per_centimeter: float
        :return: A new instance of ForcePerLength.
        :rtype: ForcePerLength
        """
        return ForcePerLength(deca_newtons_per_centimeter, ForcePerLengthUnits.DecaNewtonPerCentimeter)

    
    @staticmethod
    def from_kilo_newtons_per_centimeter(kilo_newtons_per_centimeter: float):
        """
        Create a new instance of ForcePerLength from a value in kilo_newtons_per_centimeter.

        

        :param meters: The ForcePerLength value in kilo_newtons_per_centimeter.
        :type kilo_newtons_per_centimeter: float
        :return: A new instance of ForcePerLength.
        :rtype: ForcePerLength
        """
        return ForcePerLength(kilo_newtons_per_centimeter, ForcePerLengthUnits.KiloNewtonPerCentimeter)

    
    @staticmethod
    def from_mega_newtons_per_centimeter(mega_newtons_per_centimeter: float):
        """
        Create a new instance of ForcePerLength from a value in mega_newtons_per_centimeter.

        

        :param meters: The ForcePerLength value in mega_newtons_per_centimeter.
        :type mega_newtons_per_centimeter: float
        :return: A new instance of ForcePerLength.
        :rtype: ForcePerLength
        """
        return ForcePerLength(mega_newtons_per_centimeter, ForcePerLengthUnits.MegaNewtonPerCentimeter)

    
    @staticmethod
    def from_nano_newtons_per_millimeter(nano_newtons_per_millimeter: float):
        """
        Create a new instance of ForcePerLength from a value in nano_newtons_per_millimeter.

        

        :param meters: The ForcePerLength value in nano_newtons_per_millimeter.
        :type nano_newtons_per_millimeter: float
        :return: A new instance of ForcePerLength.
        :rtype: ForcePerLength
        """
        return ForcePerLength(nano_newtons_per_millimeter, ForcePerLengthUnits.NanoNewtonPerMillimeter)

    
    @staticmethod
    def from_micro_newtons_per_millimeter(micro_newtons_per_millimeter: float):
        """
        Create a new instance of ForcePerLength from a value in micro_newtons_per_millimeter.

        

        :param meters: The ForcePerLength value in micro_newtons_per_millimeter.
        :type micro_newtons_per_millimeter: float
        :return: A new instance of ForcePerLength.
        :rtype: ForcePerLength
        """
        return ForcePerLength(micro_newtons_per_millimeter, ForcePerLengthUnits.MicroNewtonPerMillimeter)

    
    @staticmethod
    def from_milli_newtons_per_millimeter(milli_newtons_per_millimeter: float):
        """
        Create a new instance of ForcePerLength from a value in milli_newtons_per_millimeter.

        

        :param meters: The ForcePerLength value in milli_newtons_per_millimeter.
        :type milli_newtons_per_millimeter: float
        :return: A new instance of ForcePerLength.
        :rtype: ForcePerLength
        """
        return ForcePerLength(milli_newtons_per_millimeter, ForcePerLengthUnits.MilliNewtonPerMillimeter)

    
    @staticmethod
    def from_centi_newtons_per_millimeter(centi_newtons_per_millimeter: float):
        """
        Create a new instance of ForcePerLength from a value in centi_newtons_per_millimeter.

        

        :param meters: The ForcePerLength value in centi_newtons_per_millimeter.
        :type centi_newtons_per_millimeter: float
        :return: A new instance of ForcePerLength.
        :rtype: ForcePerLength
        """
        return ForcePerLength(centi_newtons_per_millimeter, ForcePerLengthUnits.CentiNewtonPerMillimeter)

    
    @staticmethod
    def from_deci_newtons_per_millimeter(deci_newtons_per_millimeter: float):
        """
        Create a new instance of ForcePerLength from a value in deci_newtons_per_millimeter.

        

        :param meters: The ForcePerLength value in deci_newtons_per_millimeter.
        :type deci_newtons_per_millimeter: float
        :return: A new instance of ForcePerLength.
        :rtype: ForcePerLength
        """
        return ForcePerLength(deci_newtons_per_millimeter, ForcePerLengthUnits.DeciNewtonPerMillimeter)

    
    @staticmethod
    def from_deca_newtons_per_millimeter(deca_newtons_per_millimeter: float):
        """
        Create a new instance of ForcePerLength from a value in deca_newtons_per_millimeter.

        

        :param meters: The ForcePerLength value in deca_newtons_per_millimeter.
        :type deca_newtons_per_millimeter: float
        :return: A new instance of ForcePerLength.
        :rtype: ForcePerLength
        """
        return ForcePerLength(deca_newtons_per_millimeter, ForcePerLengthUnits.DecaNewtonPerMillimeter)

    
    @staticmethod
    def from_kilo_newtons_per_millimeter(kilo_newtons_per_millimeter: float):
        """
        Create a new instance of ForcePerLength from a value in kilo_newtons_per_millimeter.

        

        :param meters: The ForcePerLength value in kilo_newtons_per_millimeter.
        :type kilo_newtons_per_millimeter: float
        :return: A new instance of ForcePerLength.
        :rtype: ForcePerLength
        """
        return ForcePerLength(kilo_newtons_per_millimeter, ForcePerLengthUnits.KiloNewtonPerMillimeter)

    
    @staticmethod
    def from_mega_newtons_per_millimeter(mega_newtons_per_millimeter: float):
        """
        Create a new instance of ForcePerLength from a value in mega_newtons_per_millimeter.

        

        :param meters: The ForcePerLength value in mega_newtons_per_millimeter.
        :type mega_newtons_per_millimeter: float
        :return: A new instance of ForcePerLength.
        :rtype: ForcePerLength
        """
        return ForcePerLength(mega_newtons_per_millimeter, ForcePerLengthUnits.MegaNewtonPerMillimeter)

    
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
    def nano_newtons_per_meter(self) -> float:
        """
        
        """
        if self.__nano_newtons_per_meter != None:
            return self.__nano_newtons_per_meter
        self.__nano_newtons_per_meter = self.__convert_from_base(ForcePerLengthUnits.NanoNewtonPerMeter)
        return self.__nano_newtons_per_meter

    
    @property
    def micro_newtons_per_meter(self) -> float:
        """
        
        """
        if self.__micro_newtons_per_meter != None:
            return self.__micro_newtons_per_meter
        self.__micro_newtons_per_meter = self.__convert_from_base(ForcePerLengthUnits.MicroNewtonPerMeter)
        return self.__micro_newtons_per_meter

    
    @property
    def milli_newtons_per_meter(self) -> float:
        """
        
        """
        if self.__milli_newtons_per_meter != None:
            return self.__milli_newtons_per_meter
        self.__milli_newtons_per_meter = self.__convert_from_base(ForcePerLengthUnits.MilliNewtonPerMeter)
        return self.__milli_newtons_per_meter

    
    @property
    def centi_newtons_per_meter(self) -> float:
        """
        
        """
        if self.__centi_newtons_per_meter != None:
            return self.__centi_newtons_per_meter
        self.__centi_newtons_per_meter = self.__convert_from_base(ForcePerLengthUnits.CentiNewtonPerMeter)
        return self.__centi_newtons_per_meter

    
    @property
    def deci_newtons_per_meter(self) -> float:
        """
        
        """
        if self.__deci_newtons_per_meter != None:
            return self.__deci_newtons_per_meter
        self.__deci_newtons_per_meter = self.__convert_from_base(ForcePerLengthUnits.DeciNewtonPerMeter)
        return self.__deci_newtons_per_meter

    
    @property
    def deca_newtons_per_meter(self) -> float:
        """
        
        """
        if self.__deca_newtons_per_meter != None:
            return self.__deca_newtons_per_meter
        self.__deca_newtons_per_meter = self.__convert_from_base(ForcePerLengthUnits.DecaNewtonPerMeter)
        return self.__deca_newtons_per_meter

    
    @property
    def kilo_newtons_per_meter(self) -> float:
        """
        
        """
        if self.__kilo_newtons_per_meter != None:
            return self.__kilo_newtons_per_meter
        self.__kilo_newtons_per_meter = self.__convert_from_base(ForcePerLengthUnits.KiloNewtonPerMeter)
        return self.__kilo_newtons_per_meter

    
    @property
    def mega_newtons_per_meter(self) -> float:
        """
        
        """
        if self.__mega_newtons_per_meter != None:
            return self.__mega_newtons_per_meter
        self.__mega_newtons_per_meter = self.__convert_from_base(ForcePerLengthUnits.MegaNewtonPerMeter)
        return self.__mega_newtons_per_meter

    
    @property
    def nano_newtons_per_centimeter(self) -> float:
        """
        
        """
        if self.__nano_newtons_per_centimeter != None:
            return self.__nano_newtons_per_centimeter
        self.__nano_newtons_per_centimeter = self.__convert_from_base(ForcePerLengthUnits.NanoNewtonPerCentimeter)
        return self.__nano_newtons_per_centimeter

    
    @property
    def micro_newtons_per_centimeter(self) -> float:
        """
        
        """
        if self.__micro_newtons_per_centimeter != None:
            return self.__micro_newtons_per_centimeter
        self.__micro_newtons_per_centimeter = self.__convert_from_base(ForcePerLengthUnits.MicroNewtonPerCentimeter)
        return self.__micro_newtons_per_centimeter

    
    @property
    def milli_newtons_per_centimeter(self) -> float:
        """
        
        """
        if self.__milli_newtons_per_centimeter != None:
            return self.__milli_newtons_per_centimeter
        self.__milli_newtons_per_centimeter = self.__convert_from_base(ForcePerLengthUnits.MilliNewtonPerCentimeter)
        return self.__milli_newtons_per_centimeter

    
    @property
    def centi_newtons_per_centimeter(self) -> float:
        """
        
        """
        if self.__centi_newtons_per_centimeter != None:
            return self.__centi_newtons_per_centimeter
        self.__centi_newtons_per_centimeter = self.__convert_from_base(ForcePerLengthUnits.CentiNewtonPerCentimeter)
        return self.__centi_newtons_per_centimeter

    
    @property
    def deci_newtons_per_centimeter(self) -> float:
        """
        
        """
        if self.__deci_newtons_per_centimeter != None:
            return self.__deci_newtons_per_centimeter
        self.__deci_newtons_per_centimeter = self.__convert_from_base(ForcePerLengthUnits.DeciNewtonPerCentimeter)
        return self.__deci_newtons_per_centimeter

    
    @property
    def deca_newtons_per_centimeter(self) -> float:
        """
        
        """
        if self.__deca_newtons_per_centimeter != None:
            return self.__deca_newtons_per_centimeter
        self.__deca_newtons_per_centimeter = self.__convert_from_base(ForcePerLengthUnits.DecaNewtonPerCentimeter)
        return self.__deca_newtons_per_centimeter

    
    @property
    def kilo_newtons_per_centimeter(self) -> float:
        """
        
        """
        if self.__kilo_newtons_per_centimeter != None:
            return self.__kilo_newtons_per_centimeter
        self.__kilo_newtons_per_centimeter = self.__convert_from_base(ForcePerLengthUnits.KiloNewtonPerCentimeter)
        return self.__kilo_newtons_per_centimeter

    
    @property
    def mega_newtons_per_centimeter(self) -> float:
        """
        
        """
        if self.__mega_newtons_per_centimeter != None:
            return self.__mega_newtons_per_centimeter
        self.__mega_newtons_per_centimeter = self.__convert_from_base(ForcePerLengthUnits.MegaNewtonPerCentimeter)
        return self.__mega_newtons_per_centimeter

    
    @property
    def nano_newtons_per_millimeter(self) -> float:
        """
        
        """
        if self.__nano_newtons_per_millimeter != None:
            return self.__nano_newtons_per_millimeter
        self.__nano_newtons_per_millimeter = self.__convert_from_base(ForcePerLengthUnits.NanoNewtonPerMillimeter)
        return self.__nano_newtons_per_millimeter

    
    @property
    def micro_newtons_per_millimeter(self) -> float:
        """
        
        """
        if self.__micro_newtons_per_millimeter != None:
            return self.__micro_newtons_per_millimeter
        self.__micro_newtons_per_millimeter = self.__convert_from_base(ForcePerLengthUnits.MicroNewtonPerMillimeter)
        return self.__micro_newtons_per_millimeter

    
    @property
    def milli_newtons_per_millimeter(self) -> float:
        """
        
        """
        if self.__milli_newtons_per_millimeter != None:
            return self.__milli_newtons_per_millimeter
        self.__milli_newtons_per_millimeter = self.__convert_from_base(ForcePerLengthUnits.MilliNewtonPerMillimeter)
        return self.__milli_newtons_per_millimeter

    
    @property
    def centi_newtons_per_millimeter(self) -> float:
        """
        
        """
        if self.__centi_newtons_per_millimeter != None:
            return self.__centi_newtons_per_millimeter
        self.__centi_newtons_per_millimeter = self.__convert_from_base(ForcePerLengthUnits.CentiNewtonPerMillimeter)
        return self.__centi_newtons_per_millimeter

    
    @property
    def deci_newtons_per_millimeter(self) -> float:
        """
        
        """
        if self.__deci_newtons_per_millimeter != None:
            return self.__deci_newtons_per_millimeter
        self.__deci_newtons_per_millimeter = self.__convert_from_base(ForcePerLengthUnits.DeciNewtonPerMillimeter)
        return self.__deci_newtons_per_millimeter

    
    @property
    def deca_newtons_per_millimeter(self) -> float:
        """
        
        """
        if self.__deca_newtons_per_millimeter != None:
            return self.__deca_newtons_per_millimeter
        self.__deca_newtons_per_millimeter = self.__convert_from_base(ForcePerLengthUnits.DecaNewtonPerMillimeter)
        return self.__deca_newtons_per_millimeter

    
    @property
    def kilo_newtons_per_millimeter(self) -> float:
        """
        
        """
        if self.__kilo_newtons_per_millimeter != None:
            return self.__kilo_newtons_per_millimeter
        self.__kilo_newtons_per_millimeter = self.__convert_from_base(ForcePerLengthUnits.KiloNewtonPerMillimeter)
        return self.__kilo_newtons_per_millimeter

    
    @property
    def mega_newtons_per_millimeter(self) -> float:
        """
        
        """
        if self.__mega_newtons_per_millimeter != None:
            return self.__mega_newtons_per_millimeter
        self.__mega_newtons_per_millimeter = self.__convert_from_base(ForcePerLengthUnits.MegaNewtonPerMillimeter)
        return self.__mega_newtons_per_millimeter

    
    def to_string(self, unit: ForcePerLengthUnits = ForcePerLengthUnits.NewtonPerMeter) -> string:
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
        
        if unit == ForcePerLengthUnits.NanoNewtonPerMeter:
            return f"""{self.nano_newtons_per_meter} """
        
        if unit == ForcePerLengthUnits.MicroNewtonPerMeter:
            return f"""{self.micro_newtons_per_meter} """
        
        if unit == ForcePerLengthUnits.MilliNewtonPerMeter:
            return f"""{self.milli_newtons_per_meter} """
        
        if unit == ForcePerLengthUnits.CentiNewtonPerMeter:
            return f"""{self.centi_newtons_per_meter} """
        
        if unit == ForcePerLengthUnits.DeciNewtonPerMeter:
            return f"""{self.deci_newtons_per_meter} """
        
        if unit == ForcePerLengthUnits.DecaNewtonPerMeter:
            return f"""{self.deca_newtons_per_meter} """
        
        if unit == ForcePerLengthUnits.KiloNewtonPerMeter:
            return f"""{self.kilo_newtons_per_meter} """
        
        if unit == ForcePerLengthUnits.MegaNewtonPerMeter:
            return f"""{self.mega_newtons_per_meter} """
        
        if unit == ForcePerLengthUnits.NanoNewtonPerCentimeter:
            return f"""{self.nano_newtons_per_centimeter} """
        
        if unit == ForcePerLengthUnits.MicroNewtonPerCentimeter:
            return f"""{self.micro_newtons_per_centimeter} """
        
        if unit == ForcePerLengthUnits.MilliNewtonPerCentimeter:
            return f"""{self.milli_newtons_per_centimeter} """
        
        if unit == ForcePerLengthUnits.CentiNewtonPerCentimeter:
            return f"""{self.centi_newtons_per_centimeter} """
        
        if unit == ForcePerLengthUnits.DeciNewtonPerCentimeter:
            return f"""{self.deci_newtons_per_centimeter} """
        
        if unit == ForcePerLengthUnits.DecaNewtonPerCentimeter:
            return f"""{self.deca_newtons_per_centimeter} """
        
        if unit == ForcePerLengthUnits.KiloNewtonPerCentimeter:
            return f"""{self.kilo_newtons_per_centimeter} """
        
        if unit == ForcePerLengthUnits.MegaNewtonPerCentimeter:
            return f"""{self.mega_newtons_per_centimeter} """
        
        if unit == ForcePerLengthUnits.NanoNewtonPerMillimeter:
            return f"""{self.nano_newtons_per_millimeter} """
        
        if unit == ForcePerLengthUnits.MicroNewtonPerMillimeter:
            return f"""{self.micro_newtons_per_millimeter} """
        
        if unit == ForcePerLengthUnits.MilliNewtonPerMillimeter:
            return f"""{self.milli_newtons_per_millimeter} """
        
        if unit == ForcePerLengthUnits.CentiNewtonPerMillimeter:
            return f"""{self.centi_newtons_per_millimeter} """
        
        if unit == ForcePerLengthUnits.DeciNewtonPerMillimeter:
            return f"""{self.deci_newtons_per_millimeter} """
        
        if unit == ForcePerLengthUnits.DecaNewtonPerMillimeter:
            return f"""{self.deca_newtons_per_millimeter} """
        
        if unit == ForcePerLengthUnits.KiloNewtonPerMillimeter:
            return f"""{self.kilo_newtons_per_millimeter} """
        
        if unit == ForcePerLengthUnits.MegaNewtonPerMillimeter:
            return f"""{self.mega_newtons_per_millimeter} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: ForcePerLengthUnits = ForcePerLengthUnits.NewtonPerMeter) -> string:
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
        
        if unit_abbreviation == ForcePerLengthUnits.NanoNewtonPerMeter:
            return """"""
        
        if unit_abbreviation == ForcePerLengthUnits.MicroNewtonPerMeter:
            return """"""
        
        if unit_abbreviation == ForcePerLengthUnits.MilliNewtonPerMeter:
            return """"""
        
        if unit_abbreviation == ForcePerLengthUnits.CentiNewtonPerMeter:
            return """"""
        
        if unit_abbreviation == ForcePerLengthUnits.DeciNewtonPerMeter:
            return """"""
        
        if unit_abbreviation == ForcePerLengthUnits.DecaNewtonPerMeter:
            return """"""
        
        if unit_abbreviation == ForcePerLengthUnits.KiloNewtonPerMeter:
            return """"""
        
        if unit_abbreviation == ForcePerLengthUnits.MegaNewtonPerMeter:
            return """"""
        
        if unit_abbreviation == ForcePerLengthUnits.NanoNewtonPerCentimeter:
            return """"""
        
        if unit_abbreviation == ForcePerLengthUnits.MicroNewtonPerCentimeter:
            return """"""
        
        if unit_abbreviation == ForcePerLengthUnits.MilliNewtonPerCentimeter:
            return """"""
        
        if unit_abbreviation == ForcePerLengthUnits.CentiNewtonPerCentimeter:
            return """"""
        
        if unit_abbreviation == ForcePerLengthUnits.DeciNewtonPerCentimeter:
            return """"""
        
        if unit_abbreviation == ForcePerLengthUnits.DecaNewtonPerCentimeter:
            return """"""
        
        if unit_abbreviation == ForcePerLengthUnits.KiloNewtonPerCentimeter:
            return """"""
        
        if unit_abbreviation == ForcePerLengthUnits.MegaNewtonPerCentimeter:
            return """"""
        
        if unit_abbreviation == ForcePerLengthUnits.NanoNewtonPerMillimeter:
            return """"""
        
        if unit_abbreviation == ForcePerLengthUnits.MicroNewtonPerMillimeter:
            return """"""
        
        if unit_abbreviation == ForcePerLengthUnits.MilliNewtonPerMillimeter:
            return """"""
        
        if unit_abbreviation == ForcePerLengthUnits.CentiNewtonPerMillimeter:
            return """"""
        
        if unit_abbreviation == ForcePerLengthUnits.DeciNewtonPerMillimeter:
            return """"""
        
        if unit_abbreviation == ForcePerLengthUnits.DecaNewtonPerMillimeter:
            return """"""
        
        if unit_abbreviation == ForcePerLengthUnits.KiloNewtonPerMillimeter:
            return """"""
        
        if unit_abbreviation == ForcePerLengthUnits.MegaNewtonPerMillimeter:
            return """"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, ForcePerLength):
            raise TypeError("unsupported operand type(s) for +: 'ForcePerLength' and '{}'".format(type(other).__name__))
        return ForcePerLength(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, ForcePerLength):
            raise TypeError("unsupported operand type(s) for *: 'ForcePerLength' and '{}'".format(type(other).__name__))
        return ForcePerLength(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, ForcePerLength):
            raise TypeError("unsupported operand type(s) for -: 'ForcePerLength' and '{}'".format(type(other).__name__))
        return ForcePerLength(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, ForcePerLength):
            raise TypeError("unsupported operand type(s) for /: 'ForcePerLength' and '{}'".format(type(other).__name__))
        return ForcePerLength(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, ForcePerLength):
            raise TypeError("unsupported operand type(s) for %: 'ForcePerLength' and '{}'".format(type(other).__name__))
        return ForcePerLength(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, ForcePerLength):
            raise TypeError("unsupported operand type(s) for **: 'ForcePerLength' and '{}'".format(type(other).__name__))
        return ForcePerLength(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, ForcePerLength):
            raise TypeError("unsupported operand type(s) for ==: 'ForcePerLength' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, ForcePerLength):
            raise TypeError("unsupported operand type(s) for <: 'ForcePerLength' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, ForcePerLength):
            raise TypeError("unsupported operand type(s) for >: 'ForcePerLength' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, ForcePerLength):
            raise TypeError("unsupported operand type(s) for <=: 'ForcePerLength' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, ForcePerLength):
            raise TypeError("unsupported operand type(s) for >=: 'ForcePerLength' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value
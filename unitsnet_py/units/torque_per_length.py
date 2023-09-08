from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class TorquePerLengthUnits(Enum):
        """
            TorquePerLengthUnits enumeration
        """
        
        NewtonMillimeterPerMeter = 'newton_millimeter_per_meter'
        """
            
        """
        
        NewtonCentimeterPerMeter = 'newton_centimeter_per_meter'
        """
            
        """
        
        NewtonMeterPerMeter = 'newton_meter_per_meter'
        """
            
        """
        
        PoundForceInchPerFoot = 'pound_force_inch_per_foot'
        """
            
        """
        
        PoundForceFootPerFoot = 'pound_force_foot_per_foot'
        """
            
        """
        
        KilogramForceMillimeterPerMeter = 'kilogram_force_millimeter_per_meter'
        """
            
        """
        
        KilogramForceCentimeterPerMeter = 'kilogram_force_centimeter_per_meter'
        """
            
        """
        
        KilogramForceMeterPerMeter = 'kilogram_force_meter_per_meter'
        """
            
        """
        
        TonneForceMillimeterPerMeter = 'tonne_force_millimeter_per_meter'
        """
            
        """
        
        TonneForceCentimeterPerMeter = 'tonne_force_centimeter_per_meter'
        """
            
        """
        
        TonneForceMeterPerMeter = 'tonne_force_meter_per_meter'
        """
            
        """
        
        KilonewtonMillimeterPerMeter = 'kilonewton_millimeter_per_meter'
        """
            
        """
        
        MeganewtonMillimeterPerMeter = 'meganewton_millimeter_per_meter'
        """
            
        """
        
        KilonewtonCentimeterPerMeter = 'kilonewton_centimeter_per_meter'
        """
            
        """
        
        MeganewtonCentimeterPerMeter = 'meganewton_centimeter_per_meter'
        """
            
        """
        
        KilonewtonMeterPerMeter = 'kilonewton_meter_per_meter'
        """
            
        """
        
        MeganewtonMeterPerMeter = 'meganewton_meter_per_meter'
        """
            
        """
        
        KilopoundForceInchPerFoot = 'kilopound_force_inch_per_foot'
        """
            
        """
        
        MegapoundForceInchPerFoot = 'megapound_force_inch_per_foot'
        """
            
        """
        
        KilopoundForceFootPerFoot = 'kilopound_force_foot_per_foot'
        """
            
        """
        
        MegapoundForceFootPerFoot = 'megapound_force_foot_per_foot'
        """
            
        """
        

class TorquePerLength(AbstractMeasure):
    """
    The magnitude of torque per unit length.

    Args:
        value (float): The value.
        from_unit (TorquePerLengthUnits): The TorquePerLength unit to create from, The default unit is NewtonMeterPerMeter
    """
    def __init__(self, value: float, from_unit: TorquePerLengthUnits = TorquePerLengthUnits.NewtonMeterPerMeter):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__newton_millimeters_per_meter = None
        
        self.__newton_centimeters_per_meter = None
        
        self.__newton_meters_per_meter = None
        
        self.__pound_force_inches_per_foot = None
        
        self.__pound_force_feet_per_foot = None
        
        self.__kilogram_force_millimeters_per_meter = None
        
        self.__kilogram_force_centimeters_per_meter = None
        
        self.__kilogram_force_meters_per_meter = None
        
        self.__tonne_force_millimeters_per_meter = None
        
        self.__tonne_force_centimeters_per_meter = None
        
        self.__tonne_force_meters_per_meter = None
        
        self.__kilonewton_millimeters_per_meter = None
        
        self.__meganewton_millimeters_per_meter = None
        
        self.__kilonewton_centimeters_per_meter = None
        
        self.__meganewton_centimeters_per_meter = None
        
        self.__kilonewton_meters_per_meter = None
        
        self.__meganewton_meters_per_meter = None
        
        self.__kilopound_force_inches_per_foot = None
        
        self.__megapound_force_inches_per_foot = None
        
        self.__kilopound_force_feet_per_foot = None
        
        self.__megapound_force_feet_per_foot = None
        

    def convert(self, unit: TorquePerLengthUnits) -> float:
        return self.__convert_from_base(unit)

    def __convert_from_base(self, from_unit: TorquePerLengthUnits) -> float:
        value = self._value
        
        if from_unit == TorquePerLengthUnits.NewtonMillimeterPerMeter:
            return (value * 1000)
        
        if from_unit == TorquePerLengthUnits.NewtonCentimeterPerMeter:
            return (value * 100)
        
        if from_unit == TorquePerLengthUnits.NewtonMeterPerMeter:
            return (value)
        
        if from_unit == TorquePerLengthUnits.PoundForceInchPerFoot:
            return (value / 0.370685147638)
        
        if from_unit == TorquePerLengthUnits.PoundForceFootPerFoot:
            return (value / 4.44822161526)
        
        if from_unit == TorquePerLengthUnits.KilogramForceMillimeterPerMeter:
            return (value * 101.971619222242)
        
        if from_unit == TorquePerLengthUnits.KilogramForceCentimeterPerMeter:
            return (value * 10.1971619222242)
        
        if from_unit == TorquePerLengthUnits.KilogramForceMeterPerMeter:
            return (value * 0.101971619222242)
        
        if from_unit == TorquePerLengthUnits.TonneForceMillimeterPerMeter:
            return (value * 0.101971619222242)
        
        if from_unit == TorquePerLengthUnits.TonneForceCentimeterPerMeter:
            return (value * 0.0101971619222242)
        
        if from_unit == TorquePerLengthUnits.TonneForceMeterPerMeter:
            return (value * 0.000101971619222242)
        
        if from_unit == TorquePerLengthUnits.KilonewtonMillimeterPerMeter:
            return ((value * 1000) / 1000.0)
        
        if from_unit == TorquePerLengthUnits.MeganewtonMillimeterPerMeter:
            return ((value * 1000) / 1000000.0)
        
        if from_unit == TorquePerLengthUnits.KilonewtonCentimeterPerMeter:
            return ((value * 100) / 1000.0)
        
        if from_unit == TorquePerLengthUnits.MeganewtonCentimeterPerMeter:
            return ((value * 100) / 1000000.0)
        
        if from_unit == TorquePerLengthUnits.KilonewtonMeterPerMeter:
            return ((value) / 1000.0)
        
        if from_unit == TorquePerLengthUnits.MeganewtonMeterPerMeter:
            return ((value) / 1000000.0)
        
        if from_unit == TorquePerLengthUnits.KilopoundForceInchPerFoot:
            return ((value / 0.370685147638) / 1000.0)
        
        if from_unit == TorquePerLengthUnits.MegapoundForceInchPerFoot:
            return ((value / 0.370685147638) / 1000000.0)
        
        if from_unit == TorquePerLengthUnits.KilopoundForceFootPerFoot:
            return ((value / 4.44822161526) / 1000.0)
        
        if from_unit == TorquePerLengthUnits.MegapoundForceFootPerFoot:
            return ((value / 4.44822161526) / 1000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: TorquePerLengthUnits) -> float:
        
        if to_unit == TorquePerLengthUnits.NewtonMillimeterPerMeter:
            return (value * 0.001)
        
        if to_unit == TorquePerLengthUnits.NewtonCentimeterPerMeter:
            return (value * 0.01)
        
        if to_unit == TorquePerLengthUnits.NewtonMeterPerMeter:
            return (value)
        
        if to_unit == TorquePerLengthUnits.PoundForceInchPerFoot:
            return (value * 0.370685147638)
        
        if to_unit == TorquePerLengthUnits.PoundForceFootPerFoot:
            return (value * 4.44822161526)
        
        if to_unit == TorquePerLengthUnits.KilogramForceMillimeterPerMeter:
            return (value * 0.00980665019960652)
        
        if to_unit == TorquePerLengthUnits.KilogramForceCentimeterPerMeter:
            return (value * 0.0980665019960652)
        
        if to_unit == TorquePerLengthUnits.KilogramForceMeterPerMeter:
            return (value * 9.80665019960652)
        
        if to_unit == TorquePerLengthUnits.TonneForceMillimeterPerMeter:
            return (value * 9.80665019960652)
        
        if to_unit == TorquePerLengthUnits.TonneForceCentimeterPerMeter:
            return (value * 98.0665019960652)
        
        if to_unit == TorquePerLengthUnits.TonneForceMeterPerMeter:
            return (value * 9806.65019960653)
        
        if to_unit == TorquePerLengthUnits.KilonewtonMillimeterPerMeter:
            return ((value * 0.001) * 1000.0)
        
        if to_unit == TorquePerLengthUnits.MeganewtonMillimeterPerMeter:
            return ((value * 0.001) * 1000000.0)
        
        if to_unit == TorquePerLengthUnits.KilonewtonCentimeterPerMeter:
            return ((value * 0.01) * 1000.0)
        
        if to_unit == TorquePerLengthUnits.MeganewtonCentimeterPerMeter:
            return ((value * 0.01) * 1000000.0)
        
        if to_unit == TorquePerLengthUnits.KilonewtonMeterPerMeter:
            return ((value) * 1000.0)
        
        if to_unit == TorquePerLengthUnits.MeganewtonMeterPerMeter:
            return ((value) * 1000000.0)
        
        if to_unit == TorquePerLengthUnits.KilopoundForceInchPerFoot:
            return ((value * 0.370685147638) * 1000.0)
        
        if to_unit == TorquePerLengthUnits.MegapoundForceInchPerFoot:
            return ((value * 0.370685147638) * 1000000.0)
        
        if to_unit == TorquePerLengthUnits.KilopoundForceFootPerFoot:
            return ((value * 4.44822161526) * 1000.0)
        
        if to_unit == TorquePerLengthUnits.MegapoundForceFootPerFoot:
            return ((value * 4.44822161526) * 1000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_newton_millimeters_per_meter(newton_millimeters_per_meter: float):
        """
        Create a new instance of TorquePerLength from a value in newton_millimeters_per_meter.

        

        :param meters: The TorquePerLength value in newton_millimeters_per_meter.
        :type newton_millimeters_per_meter: float
        :return: A new instance of TorquePerLength.
        :rtype: TorquePerLength
        """
        return TorquePerLength(newton_millimeters_per_meter, TorquePerLengthUnits.NewtonMillimeterPerMeter)

    
    @staticmethod
    def from_newton_centimeters_per_meter(newton_centimeters_per_meter: float):
        """
        Create a new instance of TorquePerLength from a value in newton_centimeters_per_meter.

        

        :param meters: The TorquePerLength value in newton_centimeters_per_meter.
        :type newton_centimeters_per_meter: float
        :return: A new instance of TorquePerLength.
        :rtype: TorquePerLength
        """
        return TorquePerLength(newton_centimeters_per_meter, TorquePerLengthUnits.NewtonCentimeterPerMeter)

    
    @staticmethod
    def from_newton_meters_per_meter(newton_meters_per_meter: float):
        """
        Create a new instance of TorquePerLength from a value in newton_meters_per_meter.

        

        :param meters: The TorquePerLength value in newton_meters_per_meter.
        :type newton_meters_per_meter: float
        :return: A new instance of TorquePerLength.
        :rtype: TorquePerLength
        """
        return TorquePerLength(newton_meters_per_meter, TorquePerLengthUnits.NewtonMeterPerMeter)

    
    @staticmethod
    def from_pound_force_inches_per_foot(pound_force_inches_per_foot: float):
        """
        Create a new instance of TorquePerLength from a value in pound_force_inches_per_foot.

        

        :param meters: The TorquePerLength value in pound_force_inches_per_foot.
        :type pound_force_inches_per_foot: float
        :return: A new instance of TorquePerLength.
        :rtype: TorquePerLength
        """
        return TorquePerLength(pound_force_inches_per_foot, TorquePerLengthUnits.PoundForceInchPerFoot)

    
    @staticmethod
    def from_pound_force_feet_per_foot(pound_force_feet_per_foot: float):
        """
        Create a new instance of TorquePerLength from a value in pound_force_feet_per_foot.

        

        :param meters: The TorquePerLength value in pound_force_feet_per_foot.
        :type pound_force_feet_per_foot: float
        :return: A new instance of TorquePerLength.
        :rtype: TorquePerLength
        """
        return TorquePerLength(pound_force_feet_per_foot, TorquePerLengthUnits.PoundForceFootPerFoot)

    
    @staticmethod
    def from_kilogram_force_millimeters_per_meter(kilogram_force_millimeters_per_meter: float):
        """
        Create a new instance of TorquePerLength from a value in kilogram_force_millimeters_per_meter.

        

        :param meters: The TorquePerLength value in kilogram_force_millimeters_per_meter.
        :type kilogram_force_millimeters_per_meter: float
        :return: A new instance of TorquePerLength.
        :rtype: TorquePerLength
        """
        return TorquePerLength(kilogram_force_millimeters_per_meter, TorquePerLengthUnits.KilogramForceMillimeterPerMeter)

    
    @staticmethod
    def from_kilogram_force_centimeters_per_meter(kilogram_force_centimeters_per_meter: float):
        """
        Create a new instance of TorquePerLength from a value in kilogram_force_centimeters_per_meter.

        

        :param meters: The TorquePerLength value in kilogram_force_centimeters_per_meter.
        :type kilogram_force_centimeters_per_meter: float
        :return: A new instance of TorquePerLength.
        :rtype: TorquePerLength
        """
        return TorquePerLength(kilogram_force_centimeters_per_meter, TorquePerLengthUnits.KilogramForceCentimeterPerMeter)

    
    @staticmethod
    def from_kilogram_force_meters_per_meter(kilogram_force_meters_per_meter: float):
        """
        Create a new instance of TorquePerLength from a value in kilogram_force_meters_per_meter.

        

        :param meters: The TorquePerLength value in kilogram_force_meters_per_meter.
        :type kilogram_force_meters_per_meter: float
        :return: A new instance of TorquePerLength.
        :rtype: TorquePerLength
        """
        return TorquePerLength(kilogram_force_meters_per_meter, TorquePerLengthUnits.KilogramForceMeterPerMeter)

    
    @staticmethod
    def from_tonne_force_millimeters_per_meter(tonne_force_millimeters_per_meter: float):
        """
        Create a new instance of TorquePerLength from a value in tonne_force_millimeters_per_meter.

        

        :param meters: The TorquePerLength value in tonne_force_millimeters_per_meter.
        :type tonne_force_millimeters_per_meter: float
        :return: A new instance of TorquePerLength.
        :rtype: TorquePerLength
        """
        return TorquePerLength(tonne_force_millimeters_per_meter, TorquePerLengthUnits.TonneForceMillimeterPerMeter)

    
    @staticmethod
    def from_tonne_force_centimeters_per_meter(tonne_force_centimeters_per_meter: float):
        """
        Create a new instance of TorquePerLength from a value in tonne_force_centimeters_per_meter.

        

        :param meters: The TorquePerLength value in tonne_force_centimeters_per_meter.
        :type tonne_force_centimeters_per_meter: float
        :return: A new instance of TorquePerLength.
        :rtype: TorquePerLength
        """
        return TorquePerLength(tonne_force_centimeters_per_meter, TorquePerLengthUnits.TonneForceCentimeterPerMeter)

    
    @staticmethod
    def from_tonne_force_meters_per_meter(tonne_force_meters_per_meter: float):
        """
        Create a new instance of TorquePerLength from a value in tonne_force_meters_per_meter.

        

        :param meters: The TorquePerLength value in tonne_force_meters_per_meter.
        :type tonne_force_meters_per_meter: float
        :return: A new instance of TorquePerLength.
        :rtype: TorquePerLength
        """
        return TorquePerLength(tonne_force_meters_per_meter, TorquePerLengthUnits.TonneForceMeterPerMeter)

    
    @staticmethod
    def from_kilonewton_millimeters_per_meter(kilonewton_millimeters_per_meter: float):
        """
        Create a new instance of TorquePerLength from a value in kilonewton_millimeters_per_meter.

        

        :param meters: The TorquePerLength value in kilonewton_millimeters_per_meter.
        :type kilonewton_millimeters_per_meter: float
        :return: A new instance of TorquePerLength.
        :rtype: TorquePerLength
        """
        return TorquePerLength(kilonewton_millimeters_per_meter, TorquePerLengthUnits.KilonewtonMillimeterPerMeter)

    
    @staticmethod
    def from_meganewton_millimeters_per_meter(meganewton_millimeters_per_meter: float):
        """
        Create a new instance of TorquePerLength from a value in meganewton_millimeters_per_meter.

        

        :param meters: The TorquePerLength value in meganewton_millimeters_per_meter.
        :type meganewton_millimeters_per_meter: float
        :return: A new instance of TorquePerLength.
        :rtype: TorquePerLength
        """
        return TorquePerLength(meganewton_millimeters_per_meter, TorquePerLengthUnits.MeganewtonMillimeterPerMeter)

    
    @staticmethod
    def from_kilonewton_centimeters_per_meter(kilonewton_centimeters_per_meter: float):
        """
        Create a new instance of TorquePerLength from a value in kilonewton_centimeters_per_meter.

        

        :param meters: The TorquePerLength value in kilonewton_centimeters_per_meter.
        :type kilonewton_centimeters_per_meter: float
        :return: A new instance of TorquePerLength.
        :rtype: TorquePerLength
        """
        return TorquePerLength(kilonewton_centimeters_per_meter, TorquePerLengthUnits.KilonewtonCentimeterPerMeter)

    
    @staticmethod
    def from_meganewton_centimeters_per_meter(meganewton_centimeters_per_meter: float):
        """
        Create a new instance of TorquePerLength from a value in meganewton_centimeters_per_meter.

        

        :param meters: The TorquePerLength value in meganewton_centimeters_per_meter.
        :type meganewton_centimeters_per_meter: float
        :return: A new instance of TorquePerLength.
        :rtype: TorquePerLength
        """
        return TorquePerLength(meganewton_centimeters_per_meter, TorquePerLengthUnits.MeganewtonCentimeterPerMeter)

    
    @staticmethod
    def from_kilonewton_meters_per_meter(kilonewton_meters_per_meter: float):
        """
        Create a new instance of TorquePerLength from a value in kilonewton_meters_per_meter.

        

        :param meters: The TorquePerLength value in kilonewton_meters_per_meter.
        :type kilonewton_meters_per_meter: float
        :return: A new instance of TorquePerLength.
        :rtype: TorquePerLength
        """
        return TorquePerLength(kilonewton_meters_per_meter, TorquePerLengthUnits.KilonewtonMeterPerMeter)

    
    @staticmethod
    def from_meganewton_meters_per_meter(meganewton_meters_per_meter: float):
        """
        Create a new instance of TorquePerLength from a value in meganewton_meters_per_meter.

        

        :param meters: The TorquePerLength value in meganewton_meters_per_meter.
        :type meganewton_meters_per_meter: float
        :return: A new instance of TorquePerLength.
        :rtype: TorquePerLength
        """
        return TorquePerLength(meganewton_meters_per_meter, TorquePerLengthUnits.MeganewtonMeterPerMeter)

    
    @staticmethod
    def from_kilopound_force_inches_per_foot(kilopound_force_inches_per_foot: float):
        """
        Create a new instance of TorquePerLength from a value in kilopound_force_inches_per_foot.

        

        :param meters: The TorquePerLength value in kilopound_force_inches_per_foot.
        :type kilopound_force_inches_per_foot: float
        :return: A new instance of TorquePerLength.
        :rtype: TorquePerLength
        """
        return TorquePerLength(kilopound_force_inches_per_foot, TorquePerLengthUnits.KilopoundForceInchPerFoot)

    
    @staticmethod
    def from_megapound_force_inches_per_foot(megapound_force_inches_per_foot: float):
        """
        Create a new instance of TorquePerLength from a value in megapound_force_inches_per_foot.

        

        :param meters: The TorquePerLength value in megapound_force_inches_per_foot.
        :type megapound_force_inches_per_foot: float
        :return: A new instance of TorquePerLength.
        :rtype: TorquePerLength
        """
        return TorquePerLength(megapound_force_inches_per_foot, TorquePerLengthUnits.MegapoundForceInchPerFoot)

    
    @staticmethod
    def from_kilopound_force_feet_per_foot(kilopound_force_feet_per_foot: float):
        """
        Create a new instance of TorquePerLength from a value in kilopound_force_feet_per_foot.

        

        :param meters: The TorquePerLength value in kilopound_force_feet_per_foot.
        :type kilopound_force_feet_per_foot: float
        :return: A new instance of TorquePerLength.
        :rtype: TorquePerLength
        """
        return TorquePerLength(kilopound_force_feet_per_foot, TorquePerLengthUnits.KilopoundForceFootPerFoot)

    
    @staticmethod
    def from_megapound_force_feet_per_foot(megapound_force_feet_per_foot: float):
        """
        Create a new instance of TorquePerLength from a value in megapound_force_feet_per_foot.

        

        :param meters: The TorquePerLength value in megapound_force_feet_per_foot.
        :type megapound_force_feet_per_foot: float
        :return: A new instance of TorquePerLength.
        :rtype: TorquePerLength
        """
        return TorquePerLength(megapound_force_feet_per_foot, TorquePerLengthUnits.MegapoundForceFootPerFoot)

    
    @property
    def newton_millimeters_per_meter(self) -> float:
        """
        
        """
        if self.__newton_millimeters_per_meter != None:
            return self.__newton_millimeters_per_meter
        self.__newton_millimeters_per_meter = self.__convert_from_base(TorquePerLengthUnits.NewtonMillimeterPerMeter)
        return self.__newton_millimeters_per_meter

    
    @property
    def newton_centimeters_per_meter(self) -> float:
        """
        
        """
        if self.__newton_centimeters_per_meter != None:
            return self.__newton_centimeters_per_meter
        self.__newton_centimeters_per_meter = self.__convert_from_base(TorquePerLengthUnits.NewtonCentimeterPerMeter)
        return self.__newton_centimeters_per_meter

    
    @property
    def newton_meters_per_meter(self) -> float:
        """
        
        """
        if self.__newton_meters_per_meter != None:
            return self.__newton_meters_per_meter
        self.__newton_meters_per_meter = self.__convert_from_base(TorquePerLengthUnits.NewtonMeterPerMeter)
        return self.__newton_meters_per_meter

    
    @property
    def pound_force_inches_per_foot(self) -> float:
        """
        
        """
        if self.__pound_force_inches_per_foot != None:
            return self.__pound_force_inches_per_foot
        self.__pound_force_inches_per_foot = self.__convert_from_base(TorquePerLengthUnits.PoundForceInchPerFoot)
        return self.__pound_force_inches_per_foot

    
    @property
    def pound_force_feet_per_foot(self) -> float:
        """
        
        """
        if self.__pound_force_feet_per_foot != None:
            return self.__pound_force_feet_per_foot
        self.__pound_force_feet_per_foot = self.__convert_from_base(TorquePerLengthUnits.PoundForceFootPerFoot)
        return self.__pound_force_feet_per_foot

    
    @property
    def kilogram_force_millimeters_per_meter(self) -> float:
        """
        
        """
        if self.__kilogram_force_millimeters_per_meter != None:
            return self.__kilogram_force_millimeters_per_meter
        self.__kilogram_force_millimeters_per_meter = self.__convert_from_base(TorquePerLengthUnits.KilogramForceMillimeterPerMeter)
        return self.__kilogram_force_millimeters_per_meter

    
    @property
    def kilogram_force_centimeters_per_meter(self) -> float:
        """
        
        """
        if self.__kilogram_force_centimeters_per_meter != None:
            return self.__kilogram_force_centimeters_per_meter
        self.__kilogram_force_centimeters_per_meter = self.__convert_from_base(TorquePerLengthUnits.KilogramForceCentimeterPerMeter)
        return self.__kilogram_force_centimeters_per_meter

    
    @property
    def kilogram_force_meters_per_meter(self) -> float:
        """
        
        """
        if self.__kilogram_force_meters_per_meter != None:
            return self.__kilogram_force_meters_per_meter
        self.__kilogram_force_meters_per_meter = self.__convert_from_base(TorquePerLengthUnits.KilogramForceMeterPerMeter)
        return self.__kilogram_force_meters_per_meter

    
    @property
    def tonne_force_millimeters_per_meter(self) -> float:
        """
        
        """
        if self.__tonne_force_millimeters_per_meter != None:
            return self.__tonne_force_millimeters_per_meter
        self.__tonne_force_millimeters_per_meter = self.__convert_from_base(TorquePerLengthUnits.TonneForceMillimeterPerMeter)
        return self.__tonne_force_millimeters_per_meter

    
    @property
    def tonne_force_centimeters_per_meter(self) -> float:
        """
        
        """
        if self.__tonne_force_centimeters_per_meter != None:
            return self.__tonne_force_centimeters_per_meter
        self.__tonne_force_centimeters_per_meter = self.__convert_from_base(TorquePerLengthUnits.TonneForceCentimeterPerMeter)
        return self.__tonne_force_centimeters_per_meter

    
    @property
    def tonne_force_meters_per_meter(self) -> float:
        """
        
        """
        if self.__tonne_force_meters_per_meter != None:
            return self.__tonne_force_meters_per_meter
        self.__tonne_force_meters_per_meter = self.__convert_from_base(TorquePerLengthUnits.TonneForceMeterPerMeter)
        return self.__tonne_force_meters_per_meter

    
    @property
    def kilonewton_millimeters_per_meter(self) -> float:
        """
        
        """
        if self.__kilonewton_millimeters_per_meter != None:
            return self.__kilonewton_millimeters_per_meter
        self.__kilonewton_millimeters_per_meter = self.__convert_from_base(TorquePerLengthUnits.KilonewtonMillimeterPerMeter)
        return self.__kilonewton_millimeters_per_meter

    
    @property
    def meganewton_millimeters_per_meter(self) -> float:
        """
        
        """
        if self.__meganewton_millimeters_per_meter != None:
            return self.__meganewton_millimeters_per_meter
        self.__meganewton_millimeters_per_meter = self.__convert_from_base(TorquePerLengthUnits.MeganewtonMillimeterPerMeter)
        return self.__meganewton_millimeters_per_meter

    
    @property
    def kilonewton_centimeters_per_meter(self) -> float:
        """
        
        """
        if self.__kilonewton_centimeters_per_meter != None:
            return self.__kilonewton_centimeters_per_meter
        self.__kilonewton_centimeters_per_meter = self.__convert_from_base(TorquePerLengthUnits.KilonewtonCentimeterPerMeter)
        return self.__kilonewton_centimeters_per_meter

    
    @property
    def meganewton_centimeters_per_meter(self) -> float:
        """
        
        """
        if self.__meganewton_centimeters_per_meter != None:
            return self.__meganewton_centimeters_per_meter
        self.__meganewton_centimeters_per_meter = self.__convert_from_base(TorquePerLengthUnits.MeganewtonCentimeterPerMeter)
        return self.__meganewton_centimeters_per_meter

    
    @property
    def kilonewton_meters_per_meter(self) -> float:
        """
        
        """
        if self.__kilonewton_meters_per_meter != None:
            return self.__kilonewton_meters_per_meter
        self.__kilonewton_meters_per_meter = self.__convert_from_base(TorquePerLengthUnits.KilonewtonMeterPerMeter)
        return self.__kilonewton_meters_per_meter

    
    @property
    def meganewton_meters_per_meter(self) -> float:
        """
        
        """
        if self.__meganewton_meters_per_meter != None:
            return self.__meganewton_meters_per_meter
        self.__meganewton_meters_per_meter = self.__convert_from_base(TorquePerLengthUnits.MeganewtonMeterPerMeter)
        return self.__meganewton_meters_per_meter

    
    @property
    def kilopound_force_inches_per_foot(self) -> float:
        """
        
        """
        if self.__kilopound_force_inches_per_foot != None:
            return self.__kilopound_force_inches_per_foot
        self.__kilopound_force_inches_per_foot = self.__convert_from_base(TorquePerLengthUnits.KilopoundForceInchPerFoot)
        return self.__kilopound_force_inches_per_foot

    
    @property
    def megapound_force_inches_per_foot(self) -> float:
        """
        
        """
        if self.__megapound_force_inches_per_foot != None:
            return self.__megapound_force_inches_per_foot
        self.__megapound_force_inches_per_foot = self.__convert_from_base(TorquePerLengthUnits.MegapoundForceInchPerFoot)
        return self.__megapound_force_inches_per_foot

    
    @property
    def kilopound_force_feet_per_foot(self) -> float:
        """
        
        """
        if self.__kilopound_force_feet_per_foot != None:
            return self.__kilopound_force_feet_per_foot
        self.__kilopound_force_feet_per_foot = self.__convert_from_base(TorquePerLengthUnits.KilopoundForceFootPerFoot)
        return self.__kilopound_force_feet_per_foot

    
    @property
    def megapound_force_feet_per_foot(self) -> float:
        """
        
        """
        if self.__megapound_force_feet_per_foot != None:
            return self.__megapound_force_feet_per_foot
        self.__megapound_force_feet_per_foot = self.__convert_from_base(TorquePerLengthUnits.MegapoundForceFootPerFoot)
        return self.__megapound_force_feet_per_foot

    
    def to_string(self, unit: TorquePerLengthUnits = TorquePerLengthUnits.NewtonMeterPerMeter) -> str:
        """
        Format the TorquePerLength to string.
        Note! the default format for TorquePerLength is NewtonMeterPerMeter.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == TorquePerLengthUnits.NewtonMillimeterPerMeter:
            return f"""{self.newton_millimeters_per_meter} N·mm/m"""
        
        if unit == TorquePerLengthUnits.NewtonCentimeterPerMeter:
            return f"""{self.newton_centimeters_per_meter} N·cm/m"""
        
        if unit == TorquePerLengthUnits.NewtonMeterPerMeter:
            return f"""{self.newton_meters_per_meter} N·m/m"""
        
        if unit == TorquePerLengthUnits.PoundForceInchPerFoot:
            return f"""{self.pound_force_inches_per_foot} lbf·in/ft"""
        
        if unit == TorquePerLengthUnits.PoundForceFootPerFoot:
            return f"""{self.pound_force_feet_per_foot} lbf·ft/ft"""
        
        if unit == TorquePerLengthUnits.KilogramForceMillimeterPerMeter:
            return f"""{self.kilogram_force_millimeters_per_meter} kgf·mm/m"""
        
        if unit == TorquePerLengthUnits.KilogramForceCentimeterPerMeter:
            return f"""{self.kilogram_force_centimeters_per_meter} kgf·cm/m"""
        
        if unit == TorquePerLengthUnits.KilogramForceMeterPerMeter:
            return f"""{self.kilogram_force_meters_per_meter} kgf·m/m"""
        
        if unit == TorquePerLengthUnits.TonneForceMillimeterPerMeter:
            return f"""{self.tonne_force_millimeters_per_meter} tf·mm/m"""
        
        if unit == TorquePerLengthUnits.TonneForceCentimeterPerMeter:
            return f"""{self.tonne_force_centimeters_per_meter} tf·cm/m"""
        
        if unit == TorquePerLengthUnits.TonneForceMeterPerMeter:
            return f"""{self.tonne_force_meters_per_meter} tf·m/m"""
        
        if unit == TorquePerLengthUnits.KilonewtonMillimeterPerMeter:
            return f"""{self.kilonewton_millimeters_per_meter} kN·mm/m"""
        
        if unit == TorquePerLengthUnits.MeganewtonMillimeterPerMeter:
            return f"""{self.meganewton_millimeters_per_meter} MN·mm/m"""
        
        if unit == TorquePerLengthUnits.KilonewtonCentimeterPerMeter:
            return f"""{self.kilonewton_centimeters_per_meter} kN·cm/m"""
        
        if unit == TorquePerLengthUnits.MeganewtonCentimeterPerMeter:
            return f"""{self.meganewton_centimeters_per_meter} MN·cm/m"""
        
        if unit == TorquePerLengthUnits.KilonewtonMeterPerMeter:
            return f"""{self.kilonewton_meters_per_meter} kN·m/m"""
        
        if unit == TorquePerLengthUnits.MeganewtonMeterPerMeter:
            return f"""{self.meganewton_meters_per_meter} MN·m/m"""
        
        if unit == TorquePerLengthUnits.KilopoundForceInchPerFoot:
            return f"""{self.kilopound_force_inches_per_foot} klbf·in/ft"""
        
        if unit == TorquePerLengthUnits.MegapoundForceInchPerFoot:
            return f"""{self.megapound_force_inches_per_foot} Mlbf·in/ft"""
        
        if unit == TorquePerLengthUnits.KilopoundForceFootPerFoot:
            return f"""{self.kilopound_force_feet_per_foot} klbf·ft/ft"""
        
        if unit == TorquePerLengthUnits.MegapoundForceFootPerFoot:
            return f"""{self.megapound_force_feet_per_foot} Mlbf·ft/ft"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: TorquePerLengthUnits = TorquePerLengthUnits.NewtonMeterPerMeter) -> str:
        """
        Get TorquePerLength unit abbreviation.
        Note! the default abbreviation for TorquePerLength is NewtonMeterPerMeter.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == TorquePerLengthUnits.NewtonMillimeterPerMeter:
            return """N·mm/m"""
        
        if unit_abbreviation == TorquePerLengthUnits.NewtonCentimeterPerMeter:
            return """N·cm/m"""
        
        if unit_abbreviation == TorquePerLengthUnits.NewtonMeterPerMeter:
            return """N·m/m"""
        
        if unit_abbreviation == TorquePerLengthUnits.PoundForceInchPerFoot:
            return """lbf·in/ft"""
        
        if unit_abbreviation == TorquePerLengthUnits.PoundForceFootPerFoot:
            return """lbf·ft/ft"""
        
        if unit_abbreviation == TorquePerLengthUnits.KilogramForceMillimeterPerMeter:
            return """kgf·mm/m"""
        
        if unit_abbreviation == TorquePerLengthUnits.KilogramForceCentimeterPerMeter:
            return """kgf·cm/m"""
        
        if unit_abbreviation == TorquePerLengthUnits.KilogramForceMeterPerMeter:
            return """kgf·m/m"""
        
        if unit_abbreviation == TorquePerLengthUnits.TonneForceMillimeterPerMeter:
            return """tf·mm/m"""
        
        if unit_abbreviation == TorquePerLengthUnits.TonneForceCentimeterPerMeter:
            return """tf·cm/m"""
        
        if unit_abbreviation == TorquePerLengthUnits.TonneForceMeterPerMeter:
            return """tf·m/m"""
        
        if unit_abbreviation == TorquePerLengthUnits.KilonewtonMillimeterPerMeter:
            return """kN·mm/m"""
        
        if unit_abbreviation == TorquePerLengthUnits.MeganewtonMillimeterPerMeter:
            return """MN·mm/m"""
        
        if unit_abbreviation == TorquePerLengthUnits.KilonewtonCentimeterPerMeter:
            return """kN·cm/m"""
        
        if unit_abbreviation == TorquePerLengthUnits.MeganewtonCentimeterPerMeter:
            return """MN·cm/m"""
        
        if unit_abbreviation == TorquePerLengthUnits.KilonewtonMeterPerMeter:
            return """kN·m/m"""
        
        if unit_abbreviation == TorquePerLengthUnits.MeganewtonMeterPerMeter:
            return """MN·m/m"""
        
        if unit_abbreviation == TorquePerLengthUnits.KilopoundForceInchPerFoot:
            return """klbf·in/ft"""
        
        if unit_abbreviation == TorquePerLengthUnits.MegapoundForceInchPerFoot:
            return """Mlbf·in/ft"""
        
        if unit_abbreviation == TorquePerLengthUnits.KilopoundForceFootPerFoot:
            return """klbf·ft/ft"""
        
        if unit_abbreviation == TorquePerLengthUnits.MegapoundForceFootPerFoot:
            return """Mlbf·ft/ft"""
        
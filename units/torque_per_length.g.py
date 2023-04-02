from enum import Enum
import math
import string


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
        
        KiloNewtonMillimeterPerMeter = 'kilo_newton_millimeter_per_meter'
        """
            
        """
        
        MegaNewtonMillimeterPerMeter = 'mega_newton_millimeter_per_meter'
        """
            
        """
        
        KiloNewtonCentimeterPerMeter = 'kilo_newton_centimeter_per_meter'
        """
            
        """
        
        MegaNewtonCentimeterPerMeter = 'mega_newton_centimeter_per_meter'
        """
            
        """
        
        KiloNewtonMeterPerMeter = 'kilo_newton_meter_per_meter'
        """
            
        """
        
        MegaNewtonMeterPerMeter = 'mega_newton_meter_per_meter'
        """
            
        """
        
        KiloPoundForceInchPerFoot = 'kilo_pound_force_inch_per_foot'
        """
            
        """
        
        MegaPoundForceInchPerFoot = 'mega_pound_force_inch_per_foot'
        """
            
        """
        
        KiloPoundForceFootPerFoot = 'kilo_pound_force_foot_per_foot'
        """
            
        """
        
        MegaPoundForceFootPerFoot = 'mega_pound_force_foot_per_foot'
        """
            
        """
        
    
class TorquePerLength:
    """
    The magnitude of torque per unit length.

    Args:
        value (float): The value.
        from_unit (TorquePerLengthUnits): The TorquePerLength unit to create from, The default unit is NewtonMeterPerMeter
    """
    def __init__(self, value: float, from_unit: TorquePerLengthUnits = TorquePerLengthUnits.NewtonMeterPerMeter):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
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
        
        self.__kilo_newton_millimeters_per_meter = None
        
        self.__mega_newton_millimeters_per_meter = None
        
        self.__kilo_newton_centimeters_per_meter = None
        
        self.__mega_newton_centimeters_per_meter = None
        
        self.__kilo_newton_meters_per_meter = None
        
        self.__mega_newton_meters_per_meter = None
        
        self.__kilo_pound_force_inches_per_foot = None
        
        self.__mega_pound_force_inches_per_foot = None
        
        self.__kilo_pound_force_feet_per_foot = None
        
        self.__mega_pound_force_feet_per_foot = None
        

    def __convert_from_base(self, from_unit: TorquePerLengthUnits) -> float:
        value = self.__value
        
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
        
        if from_unit == TorquePerLengthUnits.KiloNewtonMillimeterPerMeter:
            return ((value * 1000) / 1000.0)
        
        if from_unit == TorquePerLengthUnits.MegaNewtonMillimeterPerMeter:
            return ((value * 1000) / 1000000.0)
        
        if from_unit == TorquePerLengthUnits.KiloNewtonCentimeterPerMeter:
            return ((value * 100) / 1000.0)
        
        if from_unit == TorquePerLengthUnits.MegaNewtonCentimeterPerMeter:
            return ((value * 100) / 1000000.0)
        
        if from_unit == TorquePerLengthUnits.KiloNewtonMeterPerMeter:
            return ((value) / 1000.0)
        
        if from_unit == TorquePerLengthUnits.MegaNewtonMeterPerMeter:
            return ((value) / 1000000.0)
        
        if from_unit == TorquePerLengthUnits.KiloPoundForceInchPerFoot:
            return ((value / 0.370685147638) / 1000.0)
        
        if from_unit == TorquePerLengthUnits.MegaPoundForceInchPerFoot:
            return ((value / 0.370685147638) / 1000000.0)
        
        if from_unit == TorquePerLengthUnits.KiloPoundForceFootPerFoot:
            return ((value / 4.44822161526) / 1000.0)
        
        if from_unit == TorquePerLengthUnits.MegaPoundForceFootPerFoot:
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
        
        if to_unit == TorquePerLengthUnits.KiloNewtonMillimeterPerMeter:
            return ((value * 0.001) * 1000.0)
        
        if to_unit == TorquePerLengthUnits.MegaNewtonMillimeterPerMeter:
            return ((value * 0.001) * 1000000.0)
        
        if to_unit == TorquePerLengthUnits.KiloNewtonCentimeterPerMeter:
            return ((value * 0.01) * 1000.0)
        
        if to_unit == TorquePerLengthUnits.MegaNewtonCentimeterPerMeter:
            return ((value * 0.01) * 1000000.0)
        
        if to_unit == TorquePerLengthUnits.KiloNewtonMeterPerMeter:
            return ((value) * 1000.0)
        
        if to_unit == TorquePerLengthUnits.MegaNewtonMeterPerMeter:
            return ((value) * 1000000.0)
        
        if to_unit == TorquePerLengthUnits.KiloPoundForceInchPerFoot:
            return ((value * 0.370685147638) * 1000.0)
        
        if to_unit == TorquePerLengthUnits.MegaPoundForceInchPerFoot:
            return ((value * 0.370685147638) * 1000000.0)
        
        if to_unit == TorquePerLengthUnits.KiloPoundForceFootPerFoot:
            return ((value * 4.44822161526) * 1000.0)
        
        if to_unit == TorquePerLengthUnits.MegaPoundForceFootPerFoot:
            return ((value * 4.44822161526) * 1000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
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
    def from_kilo_newton_millimeters_per_meter(kilo_newton_millimeters_per_meter: float):
        """
        Create a new instance of TorquePerLength from a value in kilo_newton_millimeters_per_meter.

        

        :param meters: The TorquePerLength value in kilo_newton_millimeters_per_meter.
        :type kilo_newton_millimeters_per_meter: float
        :return: A new instance of TorquePerLength.
        :rtype: TorquePerLength
        """
        return TorquePerLength(kilo_newton_millimeters_per_meter, TorquePerLengthUnits.KiloNewtonMillimeterPerMeter)

    
    @staticmethod
    def from_mega_newton_millimeters_per_meter(mega_newton_millimeters_per_meter: float):
        """
        Create a new instance of TorquePerLength from a value in mega_newton_millimeters_per_meter.

        

        :param meters: The TorquePerLength value in mega_newton_millimeters_per_meter.
        :type mega_newton_millimeters_per_meter: float
        :return: A new instance of TorquePerLength.
        :rtype: TorquePerLength
        """
        return TorquePerLength(mega_newton_millimeters_per_meter, TorquePerLengthUnits.MegaNewtonMillimeterPerMeter)

    
    @staticmethod
    def from_kilo_newton_centimeters_per_meter(kilo_newton_centimeters_per_meter: float):
        """
        Create a new instance of TorquePerLength from a value in kilo_newton_centimeters_per_meter.

        

        :param meters: The TorquePerLength value in kilo_newton_centimeters_per_meter.
        :type kilo_newton_centimeters_per_meter: float
        :return: A new instance of TorquePerLength.
        :rtype: TorquePerLength
        """
        return TorquePerLength(kilo_newton_centimeters_per_meter, TorquePerLengthUnits.KiloNewtonCentimeterPerMeter)

    
    @staticmethod
    def from_mega_newton_centimeters_per_meter(mega_newton_centimeters_per_meter: float):
        """
        Create a new instance of TorquePerLength from a value in mega_newton_centimeters_per_meter.

        

        :param meters: The TorquePerLength value in mega_newton_centimeters_per_meter.
        :type mega_newton_centimeters_per_meter: float
        :return: A new instance of TorquePerLength.
        :rtype: TorquePerLength
        """
        return TorquePerLength(mega_newton_centimeters_per_meter, TorquePerLengthUnits.MegaNewtonCentimeterPerMeter)

    
    @staticmethod
    def from_kilo_newton_meters_per_meter(kilo_newton_meters_per_meter: float):
        """
        Create a new instance of TorquePerLength from a value in kilo_newton_meters_per_meter.

        

        :param meters: The TorquePerLength value in kilo_newton_meters_per_meter.
        :type kilo_newton_meters_per_meter: float
        :return: A new instance of TorquePerLength.
        :rtype: TorquePerLength
        """
        return TorquePerLength(kilo_newton_meters_per_meter, TorquePerLengthUnits.KiloNewtonMeterPerMeter)

    
    @staticmethod
    def from_mega_newton_meters_per_meter(mega_newton_meters_per_meter: float):
        """
        Create a new instance of TorquePerLength from a value in mega_newton_meters_per_meter.

        

        :param meters: The TorquePerLength value in mega_newton_meters_per_meter.
        :type mega_newton_meters_per_meter: float
        :return: A new instance of TorquePerLength.
        :rtype: TorquePerLength
        """
        return TorquePerLength(mega_newton_meters_per_meter, TorquePerLengthUnits.MegaNewtonMeterPerMeter)

    
    @staticmethod
    def from_kilo_pound_force_inches_per_foot(kilo_pound_force_inches_per_foot: float):
        """
        Create a new instance of TorquePerLength from a value in kilo_pound_force_inches_per_foot.

        

        :param meters: The TorquePerLength value in kilo_pound_force_inches_per_foot.
        :type kilo_pound_force_inches_per_foot: float
        :return: A new instance of TorquePerLength.
        :rtype: TorquePerLength
        """
        return TorquePerLength(kilo_pound_force_inches_per_foot, TorquePerLengthUnits.KiloPoundForceInchPerFoot)

    
    @staticmethod
    def from_mega_pound_force_inches_per_foot(mega_pound_force_inches_per_foot: float):
        """
        Create a new instance of TorquePerLength from a value in mega_pound_force_inches_per_foot.

        

        :param meters: The TorquePerLength value in mega_pound_force_inches_per_foot.
        :type mega_pound_force_inches_per_foot: float
        :return: A new instance of TorquePerLength.
        :rtype: TorquePerLength
        """
        return TorquePerLength(mega_pound_force_inches_per_foot, TorquePerLengthUnits.MegaPoundForceInchPerFoot)

    
    @staticmethod
    def from_kilo_pound_force_feet_per_foot(kilo_pound_force_feet_per_foot: float):
        """
        Create a new instance of TorquePerLength from a value in kilo_pound_force_feet_per_foot.

        

        :param meters: The TorquePerLength value in kilo_pound_force_feet_per_foot.
        :type kilo_pound_force_feet_per_foot: float
        :return: A new instance of TorquePerLength.
        :rtype: TorquePerLength
        """
        return TorquePerLength(kilo_pound_force_feet_per_foot, TorquePerLengthUnits.KiloPoundForceFootPerFoot)

    
    @staticmethod
    def from_mega_pound_force_feet_per_foot(mega_pound_force_feet_per_foot: float):
        """
        Create a new instance of TorquePerLength from a value in mega_pound_force_feet_per_foot.

        

        :param meters: The TorquePerLength value in mega_pound_force_feet_per_foot.
        :type mega_pound_force_feet_per_foot: float
        :return: A new instance of TorquePerLength.
        :rtype: TorquePerLength
        """
        return TorquePerLength(mega_pound_force_feet_per_foot, TorquePerLengthUnits.MegaPoundForceFootPerFoot)

    
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
    def kilo_newton_millimeters_per_meter(self) -> float:
        """
        
        """
        if self.__kilo_newton_millimeters_per_meter != None:
            return self.__kilo_newton_millimeters_per_meter
        self.__kilo_newton_millimeters_per_meter = self.__convert_from_base(TorquePerLengthUnits.KiloNewtonMillimeterPerMeter)
        return self.__kilo_newton_millimeters_per_meter

    
    @property
    def mega_newton_millimeters_per_meter(self) -> float:
        """
        
        """
        if self.__mega_newton_millimeters_per_meter != None:
            return self.__mega_newton_millimeters_per_meter
        self.__mega_newton_millimeters_per_meter = self.__convert_from_base(TorquePerLengthUnits.MegaNewtonMillimeterPerMeter)
        return self.__mega_newton_millimeters_per_meter

    
    @property
    def kilo_newton_centimeters_per_meter(self) -> float:
        """
        
        """
        if self.__kilo_newton_centimeters_per_meter != None:
            return self.__kilo_newton_centimeters_per_meter
        self.__kilo_newton_centimeters_per_meter = self.__convert_from_base(TorquePerLengthUnits.KiloNewtonCentimeterPerMeter)
        return self.__kilo_newton_centimeters_per_meter

    
    @property
    def mega_newton_centimeters_per_meter(self) -> float:
        """
        
        """
        if self.__mega_newton_centimeters_per_meter != None:
            return self.__mega_newton_centimeters_per_meter
        self.__mega_newton_centimeters_per_meter = self.__convert_from_base(TorquePerLengthUnits.MegaNewtonCentimeterPerMeter)
        return self.__mega_newton_centimeters_per_meter

    
    @property
    def kilo_newton_meters_per_meter(self) -> float:
        """
        
        """
        if self.__kilo_newton_meters_per_meter != None:
            return self.__kilo_newton_meters_per_meter
        self.__kilo_newton_meters_per_meter = self.__convert_from_base(TorquePerLengthUnits.KiloNewtonMeterPerMeter)
        return self.__kilo_newton_meters_per_meter

    
    @property
    def mega_newton_meters_per_meter(self) -> float:
        """
        
        """
        if self.__mega_newton_meters_per_meter != None:
            return self.__mega_newton_meters_per_meter
        self.__mega_newton_meters_per_meter = self.__convert_from_base(TorquePerLengthUnits.MegaNewtonMeterPerMeter)
        return self.__mega_newton_meters_per_meter

    
    @property
    def kilo_pound_force_inches_per_foot(self) -> float:
        """
        
        """
        if self.__kilo_pound_force_inches_per_foot != None:
            return self.__kilo_pound_force_inches_per_foot
        self.__kilo_pound_force_inches_per_foot = self.__convert_from_base(TorquePerLengthUnits.KiloPoundForceInchPerFoot)
        return self.__kilo_pound_force_inches_per_foot

    
    @property
    def mega_pound_force_inches_per_foot(self) -> float:
        """
        
        """
        if self.__mega_pound_force_inches_per_foot != None:
            return self.__mega_pound_force_inches_per_foot
        self.__mega_pound_force_inches_per_foot = self.__convert_from_base(TorquePerLengthUnits.MegaPoundForceInchPerFoot)
        return self.__mega_pound_force_inches_per_foot

    
    @property
    def kilo_pound_force_feet_per_foot(self) -> float:
        """
        
        """
        if self.__kilo_pound_force_feet_per_foot != None:
            return self.__kilo_pound_force_feet_per_foot
        self.__kilo_pound_force_feet_per_foot = self.__convert_from_base(TorquePerLengthUnits.KiloPoundForceFootPerFoot)
        return self.__kilo_pound_force_feet_per_foot

    
    @property
    def mega_pound_force_feet_per_foot(self) -> float:
        """
        
        """
        if self.__mega_pound_force_feet_per_foot != None:
            return self.__mega_pound_force_feet_per_foot
        self.__mega_pound_force_feet_per_foot = self.__convert_from_base(TorquePerLengthUnits.MegaPoundForceFootPerFoot)
        return self.__mega_pound_force_feet_per_foot

    
    def to_string(self, unit: TorquePerLengthUnits = TorquePerLengthUnits.NewtonMeterPerMeter) -> string:
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
        
        if unit == TorquePerLengthUnits.KiloNewtonMillimeterPerMeter:
            return f"""{self.kilo_newton_millimeters_per_meter} """
        
        if unit == TorquePerLengthUnits.MegaNewtonMillimeterPerMeter:
            return f"""{self.mega_newton_millimeters_per_meter} """
        
        if unit == TorquePerLengthUnits.KiloNewtonCentimeterPerMeter:
            return f"""{self.kilo_newton_centimeters_per_meter} """
        
        if unit == TorquePerLengthUnits.MegaNewtonCentimeterPerMeter:
            return f"""{self.mega_newton_centimeters_per_meter} """
        
        if unit == TorquePerLengthUnits.KiloNewtonMeterPerMeter:
            return f"""{self.kilo_newton_meters_per_meter} """
        
        if unit == TorquePerLengthUnits.MegaNewtonMeterPerMeter:
            return f"""{self.mega_newton_meters_per_meter} """
        
        if unit == TorquePerLengthUnits.KiloPoundForceInchPerFoot:
            return f"""{self.kilo_pound_force_inches_per_foot} """
        
        if unit == TorquePerLengthUnits.MegaPoundForceInchPerFoot:
            return f"""{self.mega_pound_force_inches_per_foot} """
        
        if unit == TorquePerLengthUnits.KiloPoundForceFootPerFoot:
            return f"""{self.kilo_pound_force_feet_per_foot} """
        
        if unit == TorquePerLengthUnits.MegaPoundForceFootPerFoot:
            return f"""{self.mega_pound_force_feet_per_foot} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: TorquePerLengthUnits = TorquePerLengthUnits.NewtonMeterPerMeter) -> string:
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
        
        if unit_abbreviation == TorquePerLengthUnits.KiloNewtonMillimeterPerMeter:
            return """"""
        
        if unit_abbreviation == TorquePerLengthUnits.MegaNewtonMillimeterPerMeter:
            return """"""
        
        if unit_abbreviation == TorquePerLengthUnits.KiloNewtonCentimeterPerMeter:
            return """"""
        
        if unit_abbreviation == TorquePerLengthUnits.MegaNewtonCentimeterPerMeter:
            return """"""
        
        if unit_abbreviation == TorquePerLengthUnits.KiloNewtonMeterPerMeter:
            return """"""
        
        if unit_abbreviation == TorquePerLengthUnits.MegaNewtonMeterPerMeter:
            return """"""
        
        if unit_abbreviation == TorquePerLengthUnits.KiloPoundForceInchPerFoot:
            return """"""
        
        if unit_abbreviation == TorquePerLengthUnits.MegaPoundForceInchPerFoot:
            return """"""
        
        if unit_abbreviation == TorquePerLengthUnits.KiloPoundForceFootPerFoot:
            return """"""
        
        if unit_abbreviation == TorquePerLengthUnits.MegaPoundForceFootPerFoot:
            return """"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, TorquePerLength):
            raise TypeError("unsupported operand type(s) for +: 'TorquePerLength' and '{}'".format(type(other).__name__))
        return TorquePerLength(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, TorquePerLength):
            raise TypeError("unsupported operand type(s) for *: 'TorquePerLength' and '{}'".format(type(other).__name__))
        return TorquePerLength(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, TorquePerLength):
            raise TypeError("unsupported operand type(s) for -: 'TorquePerLength' and '{}'".format(type(other).__name__))
        return TorquePerLength(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, TorquePerLength):
            raise TypeError("unsupported operand type(s) for /: 'TorquePerLength' and '{}'".format(type(other).__name__))
        return TorquePerLength(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, TorquePerLength):
            raise TypeError("unsupported operand type(s) for %: 'TorquePerLength' and '{}'".format(type(other).__name__))
        return TorquePerLength(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, TorquePerLength):
            raise TypeError("unsupported operand type(s) for **: 'TorquePerLength' and '{}'".format(type(other).__name__))
        return TorquePerLength(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, TorquePerLength):
            raise TypeError("unsupported operand type(s) for ==: 'TorquePerLength' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, TorquePerLength):
            raise TypeError("unsupported operand type(s) for <: 'TorquePerLength' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, TorquePerLength):
            raise TypeError("unsupported operand type(s) for >: 'TorquePerLength' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, TorquePerLength):
            raise TypeError("unsupported operand type(s) for <=: 'TorquePerLength' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, TorquePerLength):
            raise TypeError("unsupported operand type(s) for >=: 'TorquePerLength' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value
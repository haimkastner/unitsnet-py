from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class RotationalStiffnessPerLengthUnits(Enum):
        """
            RotationalStiffnessPerLengthUnits enumeration
        """
        
        NewtonMeterPerRadianPerMeter = 'newton_meter_per_radian_per_meter'
        """
            
        """
        
        PoundForceFootPerDegreesPerFoot = 'pound_force_foot_per_degrees_per_foot'
        """
            
        """
        
        KilopoundForceFootPerDegreesPerFoot = 'kilopound_force_foot_per_degrees_per_foot'
        """
            
        """
        
        KilonewtonMeterPerRadianPerMeter = 'kilonewton_meter_per_radian_per_meter'
        """
            
        """
        
        MeganewtonMeterPerRadianPerMeter = 'meganewton_meter_per_radian_per_meter'
        """
            
        """
        

class RotationalStiffnessPerLength(AbstractMeasure):
    """
    https://en.wikipedia.org/wiki/Stiffness#Rotational_stiffness

    Args:
        value (float): The value.
        from_unit (RotationalStiffnessPerLengthUnits): The RotationalStiffnessPerLength unit to create from, The default unit is NewtonMeterPerRadianPerMeter
    """
    def __init__(self, value: float, from_unit: RotationalStiffnessPerLengthUnits = RotationalStiffnessPerLengthUnits.NewtonMeterPerRadianPerMeter):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__newton_meters_per_radian_per_meter = None
        
        self.__pound_force_feet_per_degrees_per_feet = None
        
        self.__kilopound_force_feet_per_degrees_per_feet = None
        
        self.__kilonewton_meters_per_radian_per_meter = None
        
        self.__meganewton_meters_per_radian_per_meter = None
        

    def convert(self, unit: RotationalStiffnessPerLengthUnits) -> float:
        return self.__convert_from_base(unit)

    def __convert_from_base(self, from_unit: RotationalStiffnessPerLengthUnits) -> float:
        value = self._value
        
        if from_unit == RotationalStiffnessPerLengthUnits.NewtonMeterPerRadianPerMeter:
            return (value)
        
        if from_unit == RotationalStiffnessPerLengthUnits.PoundForceFootPerDegreesPerFoot:
            return (value / 254.864324570)
        
        if from_unit == RotationalStiffnessPerLengthUnits.KilopoundForceFootPerDegreesPerFoot:
            return (value / 254864.324570)
        
        if from_unit == RotationalStiffnessPerLengthUnits.KilonewtonMeterPerRadianPerMeter:
            return ((value) / 1000.0)
        
        if from_unit == RotationalStiffnessPerLengthUnits.MeganewtonMeterPerRadianPerMeter:
            return ((value) / 1000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: RotationalStiffnessPerLengthUnits) -> float:
        
        if to_unit == RotationalStiffnessPerLengthUnits.NewtonMeterPerRadianPerMeter:
            return (value)
        
        if to_unit == RotationalStiffnessPerLengthUnits.PoundForceFootPerDegreesPerFoot:
            return (value * 254.864324570)
        
        if to_unit == RotationalStiffnessPerLengthUnits.KilopoundForceFootPerDegreesPerFoot:
            return (value * 254864.324570)
        
        if to_unit == RotationalStiffnessPerLengthUnits.KilonewtonMeterPerRadianPerMeter:
            return ((value) * 1000.0)
        
        if to_unit == RotationalStiffnessPerLengthUnits.MeganewtonMeterPerRadianPerMeter:
            return ((value) * 1000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_newton_meters_per_radian_per_meter(newton_meters_per_radian_per_meter: float):
        """
        Create a new instance of RotationalStiffnessPerLength from a value in newton_meters_per_radian_per_meter.

        

        :param meters: The RotationalStiffnessPerLength value in newton_meters_per_radian_per_meter.
        :type newton_meters_per_radian_per_meter: float
        :return: A new instance of RotationalStiffnessPerLength.
        :rtype: RotationalStiffnessPerLength
        """
        return RotationalStiffnessPerLength(newton_meters_per_radian_per_meter, RotationalStiffnessPerLengthUnits.NewtonMeterPerRadianPerMeter)

    
    @staticmethod
    def from_pound_force_feet_per_degrees_per_feet(pound_force_feet_per_degrees_per_feet: float):
        """
        Create a new instance of RotationalStiffnessPerLength from a value in pound_force_feet_per_degrees_per_feet.

        

        :param meters: The RotationalStiffnessPerLength value in pound_force_feet_per_degrees_per_feet.
        :type pound_force_feet_per_degrees_per_feet: float
        :return: A new instance of RotationalStiffnessPerLength.
        :rtype: RotationalStiffnessPerLength
        """
        return RotationalStiffnessPerLength(pound_force_feet_per_degrees_per_feet, RotationalStiffnessPerLengthUnits.PoundForceFootPerDegreesPerFoot)

    
    @staticmethod
    def from_kilopound_force_feet_per_degrees_per_feet(kilopound_force_feet_per_degrees_per_feet: float):
        """
        Create a new instance of RotationalStiffnessPerLength from a value in kilopound_force_feet_per_degrees_per_feet.

        

        :param meters: The RotationalStiffnessPerLength value in kilopound_force_feet_per_degrees_per_feet.
        :type kilopound_force_feet_per_degrees_per_feet: float
        :return: A new instance of RotationalStiffnessPerLength.
        :rtype: RotationalStiffnessPerLength
        """
        return RotationalStiffnessPerLength(kilopound_force_feet_per_degrees_per_feet, RotationalStiffnessPerLengthUnits.KilopoundForceFootPerDegreesPerFoot)

    
    @staticmethod
    def from_kilonewton_meters_per_radian_per_meter(kilonewton_meters_per_radian_per_meter: float):
        """
        Create a new instance of RotationalStiffnessPerLength from a value in kilonewton_meters_per_radian_per_meter.

        

        :param meters: The RotationalStiffnessPerLength value in kilonewton_meters_per_radian_per_meter.
        :type kilonewton_meters_per_radian_per_meter: float
        :return: A new instance of RotationalStiffnessPerLength.
        :rtype: RotationalStiffnessPerLength
        """
        return RotationalStiffnessPerLength(kilonewton_meters_per_radian_per_meter, RotationalStiffnessPerLengthUnits.KilonewtonMeterPerRadianPerMeter)

    
    @staticmethod
    def from_meganewton_meters_per_radian_per_meter(meganewton_meters_per_radian_per_meter: float):
        """
        Create a new instance of RotationalStiffnessPerLength from a value in meganewton_meters_per_radian_per_meter.

        

        :param meters: The RotationalStiffnessPerLength value in meganewton_meters_per_radian_per_meter.
        :type meganewton_meters_per_radian_per_meter: float
        :return: A new instance of RotationalStiffnessPerLength.
        :rtype: RotationalStiffnessPerLength
        """
        return RotationalStiffnessPerLength(meganewton_meters_per_radian_per_meter, RotationalStiffnessPerLengthUnits.MeganewtonMeterPerRadianPerMeter)

    
    @property
    def newton_meters_per_radian_per_meter(self) -> float:
        """
        
        """
        if self.__newton_meters_per_radian_per_meter != None:
            return self.__newton_meters_per_radian_per_meter
        self.__newton_meters_per_radian_per_meter = self.__convert_from_base(RotationalStiffnessPerLengthUnits.NewtonMeterPerRadianPerMeter)
        return self.__newton_meters_per_radian_per_meter

    
    @property
    def pound_force_feet_per_degrees_per_feet(self) -> float:
        """
        
        """
        if self.__pound_force_feet_per_degrees_per_feet != None:
            return self.__pound_force_feet_per_degrees_per_feet
        self.__pound_force_feet_per_degrees_per_feet = self.__convert_from_base(RotationalStiffnessPerLengthUnits.PoundForceFootPerDegreesPerFoot)
        return self.__pound_force_feet_per_degrees_per_feet

    
    @property
    def kilopound_force_feet_per_degrees_per_feet(self) -> float:
        """
        
        """
        if self.__kilopound_force_feet_per_degrees_per_feet != None:
            return self.__kilopound_force_feet_per_degrees_per_feet
        self.__kilopound_force_feet_per_degrees_per_feet = self.__convert_from_base(RotationalStiffnessPerLengthUnits.KilopoundForceFootPerDegreesPerFoot)
        return self.__kilopound_force_feet_per_degrees_per_feet

    
    @property
    def kilonewton_meters_per_radian_per_meter(self) -> float:
        """
        
        """
        if self.__kilonewton_meters_per_radian_per_meter != None:
            return self.__kilonewton_meters_per_radian_per_meter
        self.__kilonewton_meters_per_radian_per_meter = self.__convert_from_base(RotationalStiffnessPerLengthUnits.KilonewtonMeterPerRadianPerMeter)
        return self.__kilonewton_meters_per_radian_per_meter

    
    @property
    def meganewton_meters_per_radian_per_meter(self) -> float:
        """
        
        """
        if self.__meganewton_meters_per_radian_per_meter != None:
            return self.__meganewton_meters_per_radian_per_meter
        self.__meganewton_meters_per_radian_per_meter = self.__convert_from_base(RotationalStiffnessPerLengthUnits.MeganewtonMeterPerRadianPerMeter)
        return self.__meganewton_meters_per_radian_per_meter

    
    def to_string(self, unit: RotationalStiffnessPerLengthUnits = RotationalStiffnessPerLengthUnits.NewtonMeterPerRadianPerMeter) -> str:
        """
        Format the RotationalStiffnessPerLength to string.
        Note! the default format for RotationalStiffnessPerLength is NewtonMeterPerRadianPerMeter.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == RotationalStiffnessPerLengthUnits.NewtonMeterPerRadianPerMeter:
            return f"""{self.newton_meters_per_radian_per_meter} N·m/rad/m"""
        
        if unit == RotationalStiffnessPerLengthUnits.PoundForceFootPerDegreesPerFoot:
            return f"""{self.pound_force_feet_per_degrees_per_feet} lbf·ft/deg/ft"""
        
        if unit == RotationalStiffnessPerLengthUnits.KilopoundForceFootPerDegreesPerFoot:
            return f"""{self.kilopound_force_feet_per_degrees_per_feet} kipf·ft/°/ft"""
        
        if unit == RotationalStiffnessPerLengthUnits.KilonewtonMeterPerRadianPerMeter:
            return f"""{self.kilonewton_meters_per_radian_per_meter} kN·m/rad/m"""
        
        if unit == RotationalStiffnessPerLengthUnits.MeganewtonMeterPerRadianPerMeter:
            return f"""{self.meganewton_meters_per_radian_per_meter} MN·m/rad/m"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: RotationalStiffnessPerLengthUnits = RotationalStiffnessPerLengthUnits.NewtonMeterPerRadianPerMeter) -> str:
        """
        Get RotationalStiffnessPerLength unit abbreviation.
        Note! the default abbreviation for RotationalStiffnessPerLength is NewtonMeterPerRadianPerMeter.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == RotationalStiffnessPerLengthUnits.NewtonMeterPerRadianPerMeter:
            return """N·m/rad/m"""
        
        if unit_abbreviation == RotationalStiffnessPerLengthUnits.PoundForceFootPerDegreesPerFoot:
            return """lbf·ft/deg/ft"""
        
        if unit_abbreviation == RotationalStiffnessPerLengthUnits.KilopoundForceFootPerDegreesPerFoot:
            return """kipf·ft/°/ft"""
        
        if unit_abbreviation == RotationalStiffnessPerLengthUnits.KilonewtonMeterPerRadianPerMeter:
            return """kN·m/rad/m"""
        
        if unit_abbreviation == RotationalStiffnessPerLengthUnits.MeganewtonMeterPerRadianPerMeter:
            return """MN·m/rad/m"""
        
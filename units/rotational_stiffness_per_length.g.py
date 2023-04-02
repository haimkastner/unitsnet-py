from enum import Enum
import math
import string


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
        
        KiloNewtonMeterPerRadianPerMeter = 'kilo_newton_meter_per_radian_per_meter'
        """
            
        """
        
        MegaNewtonMeterPerRadianPerMeter = 'mega_newton_meter_per_radian_per_meter'
        """
            
        """
        
    
class RotationalStiffnessPerLength:
    """
    https://en.wikipedia.org/wiki/Stiffness#Rotational_stiffness

    Args:
        value (float): The value.
        from_unit (RotationalStiffnessPerLengthUnits): The RotationalStiffnessPerLength unit to create from, The default unit is NewtonMeterPerRadianPerMeter
    """
    def __init__(self, value: float, from_unit: RotationalStiffnessPerLengthUnits = RotationalStiffnessPerLengthUnits.NewtonMeterPerRadianPerMeter):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__newton_meters_per_radian_per_meter = None
        
        self.__pound_force_feet_per_degrees_per_feet = None
        
        self.__kilopound_force_feet_per_degrees_per_feet = None
        
        self.__kilo_newton_meters_per_radian_per_meter = None
        
        self.__mega_newton_meters_per_radian_per_meter = None
        

    def __convert_from_base(self, from_unit: RotationalStiffnessPerLengthUnits) -> float:
        value = self.__value
        
        if from_unit == RotationalStiffnessPerLengthUnits.NewtonMeterPerRadianPerMeter:
            return (value)
        
        if from_unit == RotationalStiffnessPerLengthUnits.PoundForceFootPerDegreesPerFoot:
            return (value / 254.864324570)
        
        if from_unit == RotationalStiffnessPerLengthUnits.KilopoundForceFootPerDegreesPerFoot:
            return (value / 254864.324570)
        
        if from_unit == RotationalStiffnessPerLengthUnits.KiloNewtonMeterPerRadianPerMeter:
            return ((value) / 1000.0)
        
        if from_unit == RotationalStiffnessPerLengthUnits.MegaNewtonMeterPerRadianPerMeter:
            return ((value) / 1000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: RotationalStiffnessPerLengthUnits) -> float:
        
        if to_unit == RotationalStiffnessPerLengthUnits.NewtonMeterPerRadianPerMeter:
            return (value)
        
        if to_unit == RotationalStiffnessPerLengthUnits.PoundForceFootPerDegreesPerFoot:
            return (value * 254.864324570)
        
        if to_unit == RotationalStiffnessPerLengthUnits.KilopoundForceFootPerDegreesPerFoot:
            return (value * 254864.324570)
        
        if to_unit == RotationalStiffnessPerLengthUnits.KiloNewtonMeterPerRadianPerMeter:
            return ((value) * 1000.0)
        
        if to_unit == RotationalStiffnessPerLengthUnits.MegaNewtonMeterPerRadianPerMeter:
            return ((value) * 1000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
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
    def from_kilo_newton_meters_per_radian_per_meter(kilo_newton_meters_per_radian_per_meter: float):
        """
        Create a new instance of RotationalStiffnessPerLength from a value in kilo_newton_meters_per_radian_per_meter.

        

        :param meters: The RotationalStiffnessPerLength value in kilo_newton_meters_per_radian_per_meter.
        :type kilo_newton_meters_per_radian_per_meter: float
        :return: A new instance of RotationalStiffnessPerLength.
        :rtype: RotationalStiffnessPerLength
        """
        return RotationalStiffnessPerLength(kilo_newton_meters_per_radian_per_meter, RotationalStiffnessPerLengthUnits.KiloNewtonMeterPerRadianPerMeter)

    
    @staticmethod
    def from_mega_newton_meters_per_radian_per_meter(mega_newton_meters_per_radian_per_meter: float):
        """
        Create a new instance of RotationalStiffnessPerLength from a value in mega_newton_meters_per_radian_per_meter.

        

        :param meters: The RotationalStiffnessPerLength value in mega_newton_meters_per_radian_per_meter.
        :type mega_newton_meters_per_radian_per_meter: float
        :return: A new instance of RotationalStiffnessPerLength.
        :rtype: RotationalStiffnessPerLength
        """
        return RotationalStiffnessPerLength(mega_newton_meters_per_radian_per_meter, RotationalStiffnessPerLengthUnits.MegaNewtonMeterPerRadianPerMeter)

    
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
    def kilo_newton_meters_per_radian_per_meter(self) -> float:
        """
        
        """
        if self.__kilo_newton_meters_per_radian_per_meter != None:
            return self.__kilo_newton_meters_per_radian_per_meter
        self.__kilo_newton_meters_per_radian_per_meter = self.__convert_from_base(RotationalStiffnessPerLengthUnits.KiloNewtonMeterPerRadianPerMeter)
        return self.__kilo_newton_meters_per_radian_per_meter

    
    @property
    def mega_newton_meters_per_radian_per_meter(self) -> float:
        """
        
        """
        if self.__mega_newton_meters_per_radian_per_meter != None:
            return self.__mega_newton_meters_per_radian_per_meter
        self.__mega_newton_meters_per_radian_per_meter = self.__convert_from_base(RotationalStiffnessPerLengthUnits.MegaNewtonMeterPerRadianPerMeter)
        return self.__mega_newton_meters_per_radian_per_meter

    
    def to_string(self, unit: RotationalStiffnessPerLengthUnits = RotationalStiffnessPerLengthUnits.NewtonMeterPerRadianPerMeter) -> string:
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
        
        if unit == RotationalStiffnessPerLengthUnits.KiloNewtonMeterPerRadianPerMeter:
            return f"""{self.kilo_newton_meters_per_radian_per_meter} """
        
        if unit == RotationalStiffnessPerLengthUnits.MegaNewtonMeterPerRadianPerMeter:
            return f"""{self.mega_newton_meters_per_radian_per_meter} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: RotationalStiffnessPerLengthUnits = RotationalStiffnessPerLengthUnits.NewtonMeterPerRadianPerMeter) -> string:
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
        
        if unit_abbreviation == RotationalStiffnessPerLengthUnits.KiloNewtonMeterPerRadianPerMeter:
            return """"""
        
        if unit_abbreviation == RotationalStiffnessPerLengthUnits.MegaNewtonMeterPerRadianPerMeter:
            return """"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, RotationalStiffnessPerLength):
            raise TypeError("unsupported operand type(s) for +: 'RotationalStiffnessPerLength' and '{}'".format(type(other).__name__))
        return RotationalStiffnessPerLength(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, RotationalStiffnessPerLength):
            raise TypeError("unsupported operand type(s) for *: 'RotationalStiffnessPerLength' and '{}'".format(type(other).__name__))
        return RotationalStiffnessPerLength(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, RotationalStiffnessPerLength):
            raise TypeError("unsupported operand type(s) for -: 'RotationalStiffnessPerLength' and '{}'".format(type(other).__name__))
        return RotationalStiffnessPerLength(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, RotationalStiffnessPerLength):
            raise TypeError("unsupported operand type(s) for /: 'RotationalStiffnessPerLength' and '{}'".format(type(other).__name__))
        return RotationalStiffnessPerLength(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, RotationalStiffnessPerLength):
            raise TypeError("unsupported operand type(s) for %: 'RotationalStiffnessPerLength' and '{}'".format(type(other).__name__))
        return RotationalStiffnessPerLength(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, RotationalStiffnessPerLength):
            raise TypeError("unsupported operand type(s) for **: 'RotationalStiffnessPerLength' and '{}'".format(type(other).__name__))
        return RotationalStiffnessPerLength(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, RotationalStiffnessPerLength):
            raise TypeError("unsupported operand type(s) for ==: 'RotationalStiffnessPerLength' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, RotationalStiffnessPerLength):
            raise TypeError("unsupported operand type(s) for <: 'RotationalStiffnessPerLength' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, RotationalStiffnessPerLength):
            raise TypeError("unsupported operand type(s) for >: 'RotationalStiffnessPerLength' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, RotationalStiffnessPerLength):
            raise TypeError("unsupported operand type(s) for <=: 'RotationalStiffnessPerLength' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, RotationalStiffnessPerLength):
            raise TypeError("unsupported operand type(s) for >=: 'RotationalStiffnessPerLength' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value
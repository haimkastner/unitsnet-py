from enum import Enum
import math
import string


class RotationalStiffnessUnits(Enum):
        """
            RotationalStiffnessUnits enumeration
        """
        
        NewtonMeterPerRadian = 'newton_meter_per_radian'
        """
            
        """
        
        PoundForceFootPerDegrees = 'pound_force_foot_per_degrees'
        """
            
        """
        
        KilopoundForceFootPerDegrees = 'kilopound_force_foot_per_degrees'
        """
            
        """
        
        NewtonMillimeterPerDegree = 'newton_millimeter_per_degree'
        """
            
        """
        
        NewtonMeterPerDegree = 'newton_meter_per_degree'
        """
            
        """
        
        NewtonMillimeterPerRadian = 'newton_millimeter_per_radian'
        """
            
        """
        
        PoundForceFeetPerRadian = 'pound_force_feet_per_radian'
        """
            
        """
        
        KiloNewtonMeterPerRadian = 'kilo_newton_meter_per_radian'
        """
            
        """
        
        MegaNewtonMeterPerRadian = 'mega_newton_meter_per_radian'
        """
            
        """
        
        NanoNewtonMillimeterPerDegree = 'nano_newton_millimeter_per_degree'
        """
            
        """
        
        MicroNewtonMillimeterPerDegree = 'micro_newton_millimeter_per_degree'
        """
            
        """
        
        MilliNewtonMillimeterPerDegree = 'milli_newton_millimeter_per_degree'
        """
            
        """
        
        CentiNewtonMillimeterPerDegree = 'centi_newton_millimeter_per_degree'
        """
            
        """
        
        DeciNewtonMillimeterPerDegree = 'deci_newton_millimeter_per_degree'
        """
            
        """
        
        DecaNewtonMillimeterPerDegree = 'deca_newton_millimeter_per_degree'
        """
            
        """
        
        KiloNewtonMillimeterPerDegree = 'kilo_newton_millimeter_per_degree'
        """
            
        """
        
        MegaNewtonMillimeterPerDegree = 'mega_newton_millimeter_per_degree'
        """
            
        """
        
        NanoNewtonMeterPerDegree = 'nano_newton_meter_per_degree'
        """
            
        """
        
        MicroNewtonMeterPerDegree = 'micro_newton_meter_per_degree'
        """
            
        """
        
        MilliNewtonMeterPerDegree = 'milli_newton_meter_per_degree'
        """
            
        """
        
        CentiNewtonMeterPerDegree = 'centi_newton_meter_per_degree'
        """
            
        """
        
        DeciNewtonMeterPerDegree = 'deci_newton_meter_per_degree'
        """
            
        """
        
        DecaNewtonMeterPerDegree = 'deca_newton_meter_per_degree'
        """
            
        """
        
        KiloNewtonMeterPerDegree = 'kilo_newton_meter_per_degree'
        """
            
        """
        
        MegaNewtonMeterPerDegree = 'mega_newton_meter_per_degree'
        """
            
        """
        
        NanoNewtonMillimeterPerRadian = 'nano_newton_millimeter_per_radian'
        """
            
        """
        
        MicroNewtonMillimeterPerRadian = 'micro_newton_millimeter_per_radian'
        """
            
        """
        
        MilliNewtonMillimeterPerRadian = 'milli_newton_millimeter_per_radian'
        """
            
        """
        
        CentiNewtonMillimeterPerRadian = 'centi_newton_millimeter_per_radian'
        """
            
        """
        
        DeciNewtonMillimeterPerRadian = 'deci_newton_millimeter_per_radian'
        """
            
        """
        
        DecaNewtonMillimeterPerRadian = 'deca_newton_millimeter_per_radian'
        """
            
        """
        
        KiloNewtonMillimeterPerRadian = 'kilo_newton_millimeter_per_radian'
        """
            
        """
        
        MegaNewtonMillimeterPerRadian = 'mega_newton_millimeter_per_radian'
        """
            
        """
        
    
class RotationalStiffness:
    """
    https://en.wikipedia.org/wiki/Stiffness#Rotational_stiffness

    Args:
        value (float): The value.
        from_unit (RotationalStiffnessUnits): The RotationalStiffness unit to create from, The default unit is NewtonMeterPerRadian
    """
    def __init__(self, value: float, from_unit: RotationalStiffnessUnits = RotationalStiffnessUnits.NewtonMeterPerRadian):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__newton_meters_per_radian = None
        
        self.__pound_force_feet_per_degrees = None
        
        self.__kilopound_force_feet_per_degrees = None
        
        self.__newton_millimeters_per_degree = None
        
        self.__newton_meters_per_degree = None
        
        self.__newton_millimeters_per_radian = None
        
        self.__pound_force_feet_per_radian = None
        
        self.__kilo_newton_meters_per_radian = None
        
        self.__mega_newton_meters_per_radian = None
        
        self.__nano_newton_millimeters_per_degree = None
        
        self.__micro_newton_millimeters_per_degree = None
        
        self.__milli_newton_millimeters_per_degree = None
        
        self.__centi_newton_millimeters_per_degree = None
        
        self.__deci_newton_millimeters_per_degree = None
        
        self.__deca_newton_millimeters_per_degree = None
        
        self.__kilo_newton_millimeters_per_degree = None
        
        self.__mega_newton_millimeters_per_degree = None
        
        self.__nano_newton_meters_per_degree = None
        
        self.__micro_newton_meters_per_degree = None
        
        self.__milli_newton_meters_per_degree = None
        
        self.__centi_newton_meters_per_degree = None
        
        self.__deci_newton_meters_per_degree = None
        
        self.__deca_newton_meters_per_degree = None
        
        self.__kilo_newton_meters_per_degree = None
        
        self.__mega_newton_meters_per_degree = None
        
        self.__nano_newton_millimeters_per_radian = None
        
        self.__micro_newton_millimeters_per_radian = None
        
        self.__milli_newton_millimeters_per_radian = None
        
        self.__centi_newton_millimeters_per_radian = None
        
        self.__deci_newton_millimeters_per_radian = None
        
        self.__deca_newton_millimeters_per_radian = None
        
        self.__kilo_newton_millimeters_per_radian = None
        
        self.__mega_newton_millimeters_per_radian = None
        

    def __convert_from_base(self, from_unit: RotationalStiffnessUnits) -> float:
        value = self.__value
        
        if from_unit == RotationalStiffnessUnits.NewtonMeterPerRadian:
            return (value)
        
        if from_unit == RotationalStiffnessUnits.PoundForceFootPerDegrees:
            return (value / 77.6826)
        
        if from_unit == RotationalStiffnessUnits.KilopoundForceFootPerDegrees:
            return (value / 77682.6)
        
        if from_unit == RotationalStiffnessUnits.NewtonMillimeterPerDegree:
            return (value / 180 * math.pi * 1000)
        
        if from_unit == RotationalStiffnessUnits.NewtonMeterPerDegree:
            return (value / (180 / math.pi))
        
        if from_unit == RotationalStiffnessUnits.NewtonMillimeterPerRadian:
            return (value * 1000)
        
        if from_unit == RotationalStiffnessUnits.PoundForceFeetPerRadian:
            return (value / 1.3558179483314)
        
        if from_unit == RotationalStiffnessUnits.KiloNewtonMeterPerRadian:
            return ((value) / 1000.0)
        
        if from_unit == RotationalStiffnessUnits.MegaNewtonMeterPerRadian:
            return ((value) / 1000000.0)
        
        if from_unit == RotationalStiffnessUnits.NanoNewtonMillimeterPerDegree:
            return ((value / 180 * math.pi * 1000) / 1e-09)
        
        if from_unit == RotationalStiffnessUnits.MicroNewtonMillimeterPerDegree:
            return ((value / 180 * math.pi * 1000) / 1e-06)
        
        if from_unit == RotationalStiffnessUnits.MilliNewtonMillimeterPerDegree:
            return ((value / 180 * math.pi * 1000) / 0.001)
        
        if from_unit == RotationalStiffnessUnits.CentiNewtonMillimeterPerDegree:
            return ((value / 180 * math.pi * 1000) / 0.01)
        
        if from_unit == RotationalStiffnessUnits.DeciNewtonMillimeterPerDegree:
            return ((value / 180 * math.pi * 1000) / 0.1)
        
        if from_unit == RotationalStiffnessUnits.DecaNewtonMillimeterPerDegree:
            return ((value / 180 * math.pi * 1000) / 10.0)
        
        if from_unit == RotationalStiffnessUnits.KiloNewtonMillimeterPerDegree:
            return ((value / 180 * math.pi * 1000) / 1000.0)
        
        if from_unit == RotationalStiffnessUnits.MegaNewtonMillimeterPerDegree:
            return ((value / 180 * math.pi * 1000) / 1000000.0)
        
        if from_unit == RotationalStiffnessUnits.NanoNewtonMeterPerDegree:
            return ((value / (180 / math.pi)) / 1e-09)
        
        if from_unit == RotationalStiffnessUnits.MicroNewtonMeterPerDegree:
            return ((value / (180 / math.pi)) / 1e-06)
        
        if from_unit == RotationalStiffnessUnits.MilliNewtonMeterPerDegree:
            return ((value / (180 / math.pi)) / 0.001)
        
        if from_unit == RotationalStiffnessUnits.CentiNewtonMeterPerDegree:
            return ((value / (180 / math.pi)) / 0.01)
        
        if from_unit == RotationalStiffnessUnits.DeciNewtonMeterPerDegree:
            return ((value / (180 / math.pi)) / 0.1)
        
        if from_unit == RotationalStiffnessUnits.DecaNewtonMeterPerDegree:
            return ((value / (180 / math.pi)) / 10.0)
        
        if from_unit == RotationalStiffnessUnits.KiloNewtonMeterPerDegree:
            return ((value / (180 / math.pi)) / 1000.0)
        
        if from_unit == RotationalStiffnessUnits.MegaNewtonMeterPerDegree:
            return ((value / (180 / math.pi)) / 1000000.0)
        
        if from_unit == RotationalStiffnessUnits.NanoNewtonMillimeterPerRadian:
            return ((value * 1000) / 1e-09)
        
        if from_unit == RotationalStiffnessUnits.MicroNewtonMillimeterPerRadian:
            return ((value * 1000) / 1e-06)
        
        if from_unit == RotationalStiffnessUnits.MilliNewtonMillimeterPerRadian:
            return ((value * 1000) / 0.001)
        
        if from_unit == RotationalStiffnessUnits.CentiNewtonMillimeterPerRadian:
            return ((value * 1000) / 0.01)
        
        if from_unit == RotationalStiffnessUnits.DeciNewtonMillimeterPerRadian:
            return ((value * 1000) / 0.1)
        
        if from_unit == RotationalStiffnessUnits.DecaNewtonMillimeterPerRadian:
            return ((value * 1000) / 10.0)
        
        if from_unit == RotationalStiffnessUnits.KiloNewtonMillimeterPerRadian:
            return ((value * 1000) / 1000.0)
        
        if from_unit == RotationalStiffnessUnits.MegaNewtonMillimeterPerRadian:
            return ((value * 1000) / 1000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: RotationalStiffnessUnits) -> float:
        
        if to_unit == RotationalStiffnessUnits.NewtonMeterPerRadian:
            return (value)
        
        if to_unit == RotationalStiffnessUnits.PoundForceFootPerDegrees:
            return (value * 77.6826)
        
        if to_unit == RotationalStiffnessUnits.KilopoundForceFootPerDegrees:
            return (value * 77682.6)
        
        if to_unit == RotationalStiffnessUnits.NewtonMillimeterPerDegree:
            return (value * 180 / math.pi * 0.001)
        
        if to_unit == RotationalStiffnessUnits.NewtonMeterPerDegree:
            return (value * (180 / math.pi))
        
        if to_unit == RotationalStiffnessUnits.NewtonMillimeterPerRadian:
            return (value * 0.001)
        
        if to_unit == RotationalStiffnessUnits.PoundForceFeetPerRadian:
            return (value * 1.3558179483314)
        
        if to_unit == RotationalStiffnessUnits.KiloNewtonMeterPerRadian:
            return ((value) * 1000.0)
        
        if to_unit == RotationalStiffnessUnits.MegaNewtonMeterPerRadian:
            return ((value) * 1000000.0)
        
        if to_unit == RotationalStiffnessUnits.NanoNewtonMillimeterPerDegree:
            return ((value * 180 / math.pi * 0.001) * 1e-09)
        
        if to_unit == RotationalStiffnessUnits.MicroNewtonMillimeterPerDegree:
            return ((value * 180 / math.pi * 0.001) * 1e-06)
        
        if to_unit == RotationalStiffnessUnits.MilliNewtonMillimeterPerDegree:
            return ((value * 180 / math.pi * 0.001) * 0.001)
        
        if to_unit == RotationalStiffnessUnits.CentiNewtonMillimeterPerDegree:
            return ((value * 180 / math.pi * 0.001) * 0.01)
        
        if to_unit == RotationalStiffnessUnits.DeciNewtonMillimeterPerDegree:
            return ((value * 180 / math.pi * 0.001) * 0.1)
        
        if to_unit == RotationalStiffnessUnits.DecaNewtonMillimeterPerDegree:
            return ((value * 180 / math.pi * 0.001) * 10.0)
        
        if to_unit == RotationalStiffnessUnits.KiloNewtonMillimeterPerDegree:
            return ((value * 180 / math.pi * 0.001) * 1000.0)
        
        if to_unit == RotationalStiffnessUnits.MegaNewtonMillimeterPerDegree:
            return ((value * 180 / math.pi * 0.001) * 1000000.0)
        
        if to_unit == RotationalStiffnessUnits.NanoNewtonMeterPerDegree:
            return ((value * (180 / math.pi)) * 1e-09)
        
        if to_unit == RotationalStiffnessUnits.MicroNewtonMeterPerDegree:
            return ((value * (180 / math.pi)) * 1e-06)
        
        if to_unit == RotationalStiffnessUnits.MilliNewtonMeterPerDegree:
            return ((value * (180 / math.pi)) * 0.001)
        
        if to_unit == RotationalStiffnessUnits.CentiNewtonMeterPerDegree:
            return ((value * (180 / math.pi)) * 0.01)
        
        if to_unit == RotationalStiffnessUnits.DeciNewtonMeterPerDegree:
            return ((value * (180 / math.pi)) * 0.1)
        
        if to_unit == RotationalStiffnessUnits.DecaNewtonMeterPerDegree:
            return ((value * (180 / math.pi)) * 10.0)
        
        if to_unit == RotationalStiffnessUnits.KiloNewtonMeterPerDegree:
            return ((value * (180 / math.pi)) * 1000.0)
        
        if to_unit == RotationalStiffnessUnits.MegaNewtonMeterPerDegree:
            return ((value * (180 / math.pi)) * 1000000.0)
        
        if to_unit == RotationalStiffnessUnits.NanoNewtonMillimeterPerRadian:
            return ((value * 0.001) * 1e-09)
        
        if to_unit == RotationalStiffnessUnits.MicroNewtonMillimeterPerRadian:
            return ((value * 0.001) * 1e-06)
        
        if to_unit == RotationalStiffnessUnits.MilliNewtonMillimeterPerRadian:
            return ((value * 0.001) * 0.001)
        
        if to_unit == RotationalStiffnessUnits.CentiNewtonMillimeterPerRadian:
            return ((value * 0.001) * 0.01)
        
        if to_unit == RotationalStiffnessUnits.DeciNewtonMillimeterPerRadian:
            return ((value * 0.001) * 0.1)
        
        if to_unit == RotationalStiffnessUnits.DecaNewtonMillimeterPerRadian:
            return ((value * 0.001) * 10.0)
        
        if to_unit == RotationalStiffnessUnits.KiloNewtonMillimeterPerRadian:
            return ((value * 0.001) * 1000.0)
        
        if to_unit == RotationalStiffnessUnits.MegaNewtonMillimeterPerRadian:
            return ((value * 0.001) * 1000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
    @staticmethod
    def from_newton_meters_per_radian(newton_meters_per_radian: float):
        """
        Create a new instance of RotationalStiffness from a value in newton_meters_per_radian.

        

        :param meters: The RotationalStiffness value in newton_meters_per_radian.
        :type newton_meters_per_radian: float
        :return: A new instance of RotationalStiffness.
        :rtype: RotationalStiffness
        """
        return RotationalStiffness(newton_meters_per_radian, RotationalStiffnessUnits.NewtonMeterPerRadian)

    
    @staticmethod
    def from_pound_force_feet_per_degrees(pound_force_feet_per_degrees: float):
        """
        Create a new instance of RotationalStiffness from a value in pound_force_feet_per_degrees.

        

        :param meters: The RotationalStiffness value in pound_force_feet_per_degrees.
        :type pound_force_feet_per_degrees: float
        :return: A new instance of RotationalStiffness.
        :rtype: RotationalStiffness
        """
        return RotationalStiffness(pound_force_feet_per_degrees, RotationalStiffnessUnits.PoundForceFootPerDegrees)

    
    @staticmethod
    def from_kilopound_force_feet_per_degrees(kilopound_force_feet_per_degrees: float):
        """
        Create a new instance of RotationalStiffness from a value in kilopound_force_feet_per_degrees.

        

        :param meters: The RotationalStiffness value in kilopound_force_feet_per_degrees.
        :type kilopound_force_feet_per_degrees: float
        :return: A new instance of RotationalStiffness.
        :rtype: RotationalStiffness
        """
        return RotationalStiffness(kilopound_force_feet_per_degrees, RotationalStiffnessUnits.KilopoundForceFootPerDegrees)

    
    @staticmethod
    def from_newton_millimeters_per_degree(newton_millimeters_per_degree: float):
        """
        Create a new instance of RotationalStiffness from a value in newton_millimeters_per_degree.

        

        :param meters: The RotationalStiffness value in newton_millimeters_per_degree.
        :type newton_millimeters_per_degree: float
        :return: A new instance of RotationalStiffness.
        :rtype: RotationalStiffness
        """
        return RotationalStiffness(newton_millimeters_per_degree, RotationalStiffnessUnits.NewtonMillimeterPerDegree)

    
    @staticmethod
    def from_newton_meters_per_degree(newton_meters_per_degree: float):
        """
        Create a new instance of RotationalStiffness from a value in newton_meters_per_degree.

        

        :param meters: The RotationalStiffness value in newton_meters_per_degree.
        :type newton_meters_per_degree: float
        :return: A new instance of RotationalStiffness.
        :rtype: RotationalStiffness
        """
        return RotationalStiffness(newton_meters_per_degree, RotationalStiffnessUnits.NewtonMeterPerDegree)

    
    @staticmethod
    def from_newton_millimeters_per_radian(newton_millimeters_per_radian: float):
        """
        Create a new instance of RotationalStiffness from a value in newton_millimeters_per_radian.

        

        :param meters: The RotationalStiffness value in newton_millimeters_per_radian.
        :type newton_millimeters_per_radian: float
        :return: A new instance of RotationalStiffness.
        :rtype: RotationalStiffness
        """
        return RotationalStiffness(newton_millimeters_per_radian, RotationalStiffnessUnits.NewtonMillimeterPerRadian)

    
    @staticmethod
    def from_pound_force_feet_per_radian(pound_force_feet_per_radian: float):
        """
        Create a new instance of RotationalStiffness from a value in pound_force_feet_per_radian.

        

        :param meters: The RotationalStiffness value in pound_force_feet_per_radian.
        :type pound_force_feet_per_radian: float
        :return: A new instance of RotationalStiffness.
        :rtype: RotationalStiffness
        """
        return RotationalStiffness(pound_force_feet_per_radian, RotationalStiffnessUnits.PoundForceFeetPerRadian)

    
    @staticmethod
    def from_kilo_newton_meters_per_radian(kilo_newton_meters_per_radian: float):
        """
        Create a new instance of RotationalStiffness from a value in kilo_newton_meters_per_radian.

        

        :param meters: The RotationalStiffness value in kilo_newton_meters_per_radian.
        :type kilo_newton_meters_per_radian: float
        :return: A new instance of RotationalStiffness.
        :rtype: RotationalStiffness
        """
        return RotationalStiffness(kilo_newton_meters_per_radian, RotationalStiffnessUnits.KiloNewtonMeterPerRadian)

    
    @staticmethod
    def from_mega_newton_meters_per_radian(mega_newton_meters_per_radian: float):
        """
        Create a new instance of RotationalStiffness from a value in mega_newton_meters_per_radian.

        

        :param meters: The RotationalStiffness value in mega_newton_meters_per_radian.
        :type mega_newton_meters_per_radian: float
        :return: A new instance of RotationalStiffness.
        :rtype: RotationalStiffness
        """
        return RotationalStiffness(mega_newton_meters_per_radian, RotationalStiffnessUnits.MegaNewtonMeterPerRadian)

    
    @staticmethod
    def from_nano_newton_millimeters_per_degree(nano_newton_millimeters_per_degree: float):
        """
        Create a new instance of RotationalStiffness from a value in nano_newton_millimeters_per_degree.

        

        :param meters: The RotationalStiffness value in nano_newton_millimeters_per_degree.
        :type nano_newton_millimeters_per_degree: float
        :return: A new instance of RotationalStiffness.
        :rtype: RotationalStiffness
        """
        return RotationalStiffness(nano_newton_millimeters_per_degree, RotationalStiffnessUnits.NanoNewtonMillimeterPerDegree)

    
    @staticmethod
    def from_micro_newton_millimeters_per_degree(micro_newton_millimeters_per_degree: float):
        """
        Create a new instance of RotationalStiffness from a value in micro_newton_millimeters_per_degree.

        

        :param meters: The RotationalStiffness value in micro_newton_millimeters_per_degree.
        :type micro_newton_millimeters_per_degree: float
        :return: A new instance of RotationalStiffness.
        :rtype: RotationalStiffness
        """
        return RotationalStiffness(micro_newton_millimeters_per_degree, RotationalStiffnessUnits.MicroNewtonMillimeterPerDegree)

    
    @staticmethod
    def from_milli_newton_millimeters_per_degree(milli_newton_millimeters_per_degree: float):
        """
        Create a new instance of RotationalStiffness from a value in milli_newton_millimeters_per_degree.

        

        :param meters: The RotationalStiffness value in milli_newton_millimeters_per_degree.
        :type milli_newton_millimeters_per_degree: float
        :return: A new instance of RotationalStiffness.
        :rtype: RotationalStiffness
        """
        return RotationalStiffness(milli_newton_millimeters_per_degree, RotationalStiffnessUnits.MilliNewtonMillimeterPerDegree)

    
    @staticmethod
    def from_centi_newton_millimeters_per_degree(centi_newton_millimeters_per_degree: float):
        """
        Create a new instance of RotationalStiffness from a value in centi_newton_millimeters_per_degree.

        

        :param meters: The RotationalStiffness value in centi_newton_millimeters_per_degree.
        :type centi_newton_millimeters_per_degree: float
        :return: A new instance of RotationalStiffness.
        :rtype: RotationalStiffness
        """
        return RotationalStiffness(centi_newton_millimeters_per_degree, RotationalStiffnessUnits.CentiNewtonMillimeterPerDegree)

    
    @staticmethod
    def from_deci_newton_millimeters_per_degree(deci_newton_millimeters_per_degree: float):
        """
        Create a new instance of RotationalStiffness from a value in deci_newton_millimeters_per_degree.

        

        :param meters: The RotationalStiffness value in deci_newton_millimeters_per_degree.
        :type deci_newton_millimeters_per_degree: float
        :return: A new instance of RotationalStiffness.
        :rtype: RotationalStiffness
        """
        return RotationalStiffness(deci_newton_millimeters_per_degree, RotationalStiffnessUnits.DeciNewtonMillimeterPerDegree)

    
    @staticmethod
    def from_deca_newton_millimeters_per_degree(deca_newton_millimeters_per_degree: float):
        """
        Create a new instance of RotationalStiffness from a value in deca_newton_millimeters_per_degree.

        

        :param meters: The RotationalStiffness value in deca_newton_millimeters_per_degree.
        :type deca_newton_millimeters_per_degree: float
        :return: A new instance of RotationalStiffness.
        :rtype: RotationalStiffness
        """
        return RotationalStiffness(deca_newton_millimeters_per_degree, RotationalStiffnessUnits.DecaNewtonMillimeterPerDegree)

    
    @staticmethod
    def from_kilo_newton_millimeters_per_degree(kilo_newton_millimeters_per_degree: float):
        """
        Create a new instance of RotationalStiffness from a value in kilo_newton_millimeters_per_degree.

        

        :param meters: The RotationalStiffness value in kilo_newton_millimeters_per_degree.
        :type kilo_newton_millimeters_per_degree: float
        :return: A new instance of RotationalStiffness.
        :rtype: RotationalStiffness
        """
        return RotationalStiffness(kilo_newton_millimeters_per_degree, RotationalStiffnessUnits.KiloNewtonMillimeterPerDegree)

    
    @staticmethod
    def from_mega_newton_millimeters_per_degree(mega_newton_millimeters_per_degree: float):
        """
        Create a new instance of RotationalStiffness from a value in mega_newton_millimeters_per_degree.

        

        :param meters: The RotationalStiffness value in mega_newton_millimeters_per_degree.
        :type mega_newton_millimeters_per_degree: float
        :return: A new instance of RotationalStiffness.
        :rtype: RotationalStiffness
        """
        return RotationalStiffness(mega_newton_millimeters_per_degree, RotationalStiffnessUnits.MegaNewtonMillimeterPerDegree)

    
    @staticmethod
    def from_nano_newton_meters_per_degree(nano_newton_meters_per_degree: float):
        """
        Create a new instance of RotationalStiffness from a value in nano_newton_meters_per_degree.

        

        :param meters: The RotationalStiffness value in nano_newton_meters_per_degree.
        :type nano_newton_meters_per_degree: float
        :return: A new instance of RotationalStiffness.
        :rtype: RotationalStiffness
        """
        return RotationalStiffness(nano_newton_meters_per_degree, RotationalStiffnessUnits.NanoNewtonMeterPerDegree)

    
    @staticmethod
    def from_micro_newton_meters_per_degree(micro_newton_meters_per_degree: float):
        """
        Create a new instance of RotationalStiffness from a value in micro_newton_meters_per_degree.

        

        :param meters: The RotationalStiffness value in micro_newton_meters_per_degree.
        :type micro_newton_meters_per_degree: float
        :return: A new instance of RotationalStiffness.
        :rtype: RotationalStiffness
        """
        return RotationalStiffness(micro_newton_meters_per_degree, RotationalStiffnessUnits.MicroNewtonMeterPerDegree)

    
    @staticmethod
    def from_milli_newton_meters_per_degree(milli_newton_meters_per_degree: float):
        """
        Create a new instance of RotationalStiffness from a value in milli_newton_meters_per_degree.

        

        :param meters: The RotationalStiffness value in milli_newton_meters_per_degree.
        :type milli_newton_meters_per_degree: float
        :return: A new instance of RotationalStiffness.
        :rtype: RotationalStiffness
        """
        return RotationalStiffness(milli_newton_meters_per_degree, RotationalStiffnessUnits.MilliNewtonMeterPerDegree)

    
    @staticmethod
    def from_centi_newton_meters_per_degree(centi_newton_meters_per_degree: float):
        """
        Create a new instance of RotationalStiffness from a value in centi_newton_meters_per_degree.

        

        :param meters: The RotationalStiffness value in centi_newton_meters_per_degree.
        :type centi_newton_meters_per_degree: float
        :return: A new instance of RotationalStiffness.
        :rtype: RotationalStiffness
        """
        return RotationalStiffness(centi_newton_meters_per_degree, RotationalStiffnessUnits.CentiNewtonMeterPerDegree)

    
    @staticmethod
    def from_deci_newton_meters_per_degree(deci_newton_meters_per_degree: float):
        """
        Create a new instance of RotationalStiffness from a value in deci_newton_meters_per_degree.

        

        :param meters: The RotationalStiffness value in deci_newton_meters_per_degree.
        :type deci_newton_meters_per_degree: float
        :return: A new instance of RotationalStiffness.
        :rtype: RotationalStiffness
        """
        return RotationalStiffness(deci_newton_meters_per_degree, RotationalStiffnessUnits.DeciNewtonMeterPerDegree)

    
    @staticmethod
    def from_deca_newton_meters_per_degree(deca_newton_meters_per_degree: float):
        """
        Create a new instance of RotationalStiffness from a value in deca_newton_meters_per_degree.

        

        :param meters: The RotationalStiffness value in deca_newton_meters_per_degree.
        :type deca_newton_meters_per_degree: float
        :return: A new instance of RotationalStiffness.
        :rtype: RotationalStiffness
        """
        return RotationalStiffness(deca_newton_meters_per_degree, RotationalStiffnessUnits.DecaNewtonMeterPerDegree)

    
    @staticmethod
    def from_kilo_newton_meters_per_degree(kilo_newton_meters_per_degree: float):
        """
        Create a new instance of RotationalStiffness from a value in kilo_newton_meters_per_degree.

        

        :param meters: The RotationalStiffness value in kilo_newton_meters_per_degree.
        :type kilo_newton_meters_per_degree: float
        :return: A new instance of RotationalStiffness.
        :rtype: RotationalStiffness
        """
        return RotationalStiffness(kilo_newton_meters_per_degree, RotationalStiffnessUnits.KiloNewtonMeterPerDegree)

    
    @staticmethod
    def from_mega_newton_meters_per_degree(mega_newton_meters_per_degree: float):
        """
        Create a new instance of RotationalStiffness from a value in mega_newton_meters_per_degree.

        

        :param meters: The RotationalStiffness value in mega_newton_meters_per_degree.
        :type mega_newton_meters_per_degree: float
        :return: A new instance of RotationalStiffness.
        :rtype: RotationalStiffness
        """
        return RotationalStiffness(mega_newton_meters_per_degree, RotationalStiffnessUnits.MegaNewtonMeterPerDegree)

    
    @staticmethod
    def from_nano_newton_millimeters_per_radian(nano_newton_millimeters_per_radian: float):
        """
        Create a new instance of RotationalStiffness from a value in nano_newton_millimeters_per_radian.

        

        :param meters: The RotationalStiffness value in nano_newton_millimeters_per_radian.
        :type nano_newton_millimeters_per_radian: float
        :return: A new instance of RotationalStiffness.
        :rtype: RotationalStiffness
        """
        return RotationalStiffness(nano_newton_millimeters_per_radian, RotationalStiffnessUnits.NanoNewtonMillimeterPerRadian)

    
    @staticmethod
    def from_micro_newton_millimeters_per_radian(micro_newton_millimeters_per_radian: float):
        """
        Create a new instance of RotationalStiffness from a value in micro_newton_millimeters_per_radian.

        

        :param meters: The RotationalStiffness value in micro_newton_millimeters_per_radian.
        :type micro_newton_millimeters_per_radian: float
        :return: A new instance of RotationalStiffness.
        :rtype: RotationalStiffness
        """
        return RotationalStiffness(micro_newton_millimeters_per_radian, RotationalStiffnessUnits.MicroNewtonMillimeterPerRadian)

    
    @staticmethod
    def from_milli_newton_millimeters_per_radian(milli_newton_millimeters_per_radian: float):
        """
        Create a new instance of RotationalStiffness from a value in milli_newton_millimeters_per_radian.

        

        :param meters: The RotationalStiffness value in milli_newton_millimeters_per_radian.
        :type milli_newton_millimeters_per_radian: float
        :return: A new instance of RotationalStiffness.
        :rtype: RotationalStiffness
        """
        return RotationalStiffness(milli_newton_millimeters_per_radian, RotationalStiffnessUnits.MilliNewtonMillimeterPerRadian)

    
    @staticmethod
    def from_centi_newton_millimeters_per_radian(centi_newton_millimeters_per_radian: float):
        """
        Create a new instance of RotationalStiffness from a value in centi_newton_millimeters_per_radian.

        

        :param meters: The RotationalStiffness value in centi_newton_millimeters_per_radian.
        :type centi_newton_millimeters_per_radian: float
        :return: A new instance of RotationalStiffness.
        :rtype: RotationalStiffness
        """
        return RotationalStiffness(centi_newton_millimeters_per_radian, RotationalStiffnessUnits.CentiNewtonMillimeterPerRadian)

    
    @staticmethod
    def from_deci_newton_millimeters_per_radian(deci_newton_millimeters_per_radian: float):
        """
        Create a new instance of RotationalStiffness from a value in deci_newton_millimeters_per_radian.

        

        :param meters: The RotationalStiffness value in deci_newton_millimeters_per_radian.
        :type deci_newton_millimeters_per_radian: float
        :return: A new instance of RotationalStiffness.
        :rtype: RotationalStiffness
        """
        return RotationalStiffness(deci_newton_millimeters_per_radian, RotationalStiffnessUnits.DeciNewtonMillimeterPerRadian)

    
    @staticmethod
    def from_deca_newton_millimeters_per_radian(deca_newton_millimeters_per_radian: float):
        """
        Create a new instance of RotationalStiffness from a value in deca_newton_millimeters_per_radian.

        

        :param meters: The RotationalStiffness value in deca_newton_millimeters_per_radian.
        :type deca_newton_millimeters_per_radian: float
        :return: A new instance of RotationalStiffness.
        :rtype: RotationalStiffness
        """
        return RotationalStiffness(deca_newton_millimeters_per_radian, RotationalStiffnessUnits.DecaNewtonMillimeterPerRadian)

    
    @staticmethod
    def from_kilo_newton_millimeters_per_radian(kilo_newton_millimeters_per_radian: float):
        """
        Create a new instance of RotationalStiffness from a value in kilo_newton_millimeters_per_radian.

        

        :param meters: The RotationalStiffness value in kilo_newton_millimeters_per_radian.
        :type kilo_newton_millimeters_per_radian: float
        :return: A new instance of RotationalStiffness.
        :rtype: RotationalStiffness
        """
        return RotationalStiffness(kilo_newton_millimeters_per_radian, RotationalStiffnessUnits.KiloNewtonMillimeterPerRadian)

    
    @staticmethod
    def from_mega_newton_millimeters_per_radian(mega_newton_millimeters_per_radian: float):
        """
        Create a new instance of RotationalStiffness from a value in mega_newton_millimeters_per_radian.

        

        :param meters: The RotationalStiffness value in mega_newton_millimeters_per_radian.
        :type mega_newton_millimeters_per_radian: float
        :return: A new instance of RotationalStiffness.
        :rtype: RotationalStiffness
        """
        return RotationalStiffness(mega_newton_millimeters_per_radian, RotationalStiffnessUnits.MegaNewtonMillimeterPerRadian)

    
    @property
    def newton_meters_per_radian(self) -> float:
        """
        
        """
        if self.__newton_meters_per_radian != None:
            return self.__newton_meters_per_radian
        self.__newton_meters_per_radian = self.__convert_from_base(RotationalStiffnessUnits.NewtonMeterPerRadian)
        return self.__newton_meters_per_radian

    
    @property
    def pound_force_feet_per_degrees(self) -> float:
        """
        
        """
        if self.__pound_force_feet_per_degrees != None:
            return self.__pound_force_feet_per_degrees
        self.__pound_force_feet_per_degrees = self.__convert_from_base(RotationalStiffnessUnits.PoundForceFootPerDegrees)
        return self.__pound_force_feet_per_degrees

    
    @property
    def kilopound_force_feet_per_degrees(self) -> float:
        """
        
        """
        if self.__kilopound_force_feet_per_degrees != None:
            return self.__kilopound_force_feet_per_degrees
        self.__kilopound_force_feet_per_degrees = self.__convert_from_base(RotationalStiffnessUnits.KilopoundForceFootPerDegrees)
        return self.__kilopound_force_feet_per_degrees

    
    @property
    def newton_millimeters_per_degree(self) -> float:
        """
        
        """
        if self.__newton_millimeters_per_degree != None:
            return self.__newton_millimeters_per_degree
        self.__newton_millimeters_per_degree = self.__convert_from_base(RotationalStiffnessUnits.NewtonMillimeterPerDegree)
        return self.__newton_millimeters_per_degree

    
    @property
    def newton_meters_per_degree(self) -> float:
        """
        
        """
        if self.__newton_meters_per_degree != None:
            return self.__newton_meters_per_degree
        self.__newton_meters_per_degree = self.__convert_from_base(RotationalStiffnessUnits.NewtonMeterPerDegree)
        return self.__newton_meters_per_degree

    
    @property
    def newton_millimeters_per_radian(self) -> float:
        """
        
        """
        if self.__newton_millimeters_per_radian != None:
            return self.__newton_millimeters_per_radian
        self.__newton_millimeters_per_radian = self.__convert_from_base(RotationalStiffnessUnits.NewtonMillimeterPerRadian)
        return self.__newton_millimeters_per_radian

    
    @property
    def pound_force_feet_per_radian(self) -> float:
        """
        
        """
        if self.__pound_force_feet_per_radian != None:
            return self.__pound_force_feet_per_radian
        self.__pound_force_feet_per_radian = self.__convert_from_base(RotationalStiffnessUnits.PoundForceFeetPerRadian)
        return self.__pound_force_feet_per_radian

    
    @property
    def kilo_newton_meters_per_radian(self) -> float:
        """
        
        """
        if self.__kilo_newton_meters_per_radian != None:
            return self.__kilo_newton_meters_per_radian
        self.__kilo_newton_meters_per_radian = self.__convert_from_base(RotationalStiffnessUnits.KiloNewtonMeterPerRadian)
        return self.__kilo_newton_meters_per_radian

    
    @property
    def mega_newton_meters_per_radian(self) -> float:
        """
        
        """
        if self.__mega_newton_meters_per_radian != None:
            return self.__mega_newton_meters_per_radian
        self.__mega_newton_meters_per_radian = self.__convert_from_base(RotationalStiffnessUnits.MegaNewtonMeterPerRadian)
        return self.__mega_newton_meters_per_radian

    
    @property
    def nano_newton_millimeters_per_degree(self) -> float:
        """
        
        """
        if self.__nano_newton_millimeters_per_degree != None:
            return self.__nano_newton_millimeters_per_degree
        self.__nano_newton_millimeters_per_degree = self.__convert_from_base(RotationalStiffnessUnits.NanoNewtonMillimeterPerDegree)
        return self.__nano_newton_millimeters_per_degree

    
    @property
    def micro_newton_millimeters_per_degree(self) -> float:
        """
        
        """
        if self.__micro_newton_millimeters_per_degree != None:
            return self.__micro_newton_millimeters_per_degree
        self.__micro_newton_millimeters_per_degree = self.__convert_from_base(RotationalStiffnessUnits.MicroNewtonMillimeterPerDegree)
        return self.__micro_newton_millimeters_per_degree

    
    @property
    def milli_newton_millimeters_per_degree(self) -> float:
        """
        
        """
        if self.__milli_newton_millimeters_per_degree != None:
            return self.__milli_newton_millimeters_per_degree
        self.__milli_newton_millimeters_per_degree = self.__convert_from_base(RotationalStiffnessUnits.MilliNewtonMillimeterPerDegree)
        return self.__milli_newton_millimeters_per_degree

    
    @property
    def centi_newton_millimeters_per_degree(self) -> float:
        """
        
        """
        if self.__centi_newton_millimeters_per_degree != None:
            return self.__centi_newton_millimeters_per_degree
        self.__centi_newton_millimeters_per_degree = self.__convert_from_base(RotationalStiffnessUnits.CentiNewtonMillimeterPerDegree)
        return self.__centi_newton_millimeters_per_degree

    
    @property
    def deci_newton_millimeters_per_degree(self) -> float:
        """
        
        """
        if self.__deci_newton_millimeters_per_degree != None:
            return self.__deci_newton_millimeters_per_degree
        self.__deci_newton_millimeters_per_degree = self.__convert_from_base(RotationalStiffnessUnits.DeciNewtonMillimeterPerDegree)
        return self.__deci_newton_millimeters_per_degree

    
    @property
    def deca_newton_millimeters_per_degree(self) -> float:
        """
        
        """
        if self.__deca_newton_millimeters_per_degree != None:
            return self.__deca_newton_millimeters_per_degree
        self.__deca_newton_millimeters_per_degree = self.__convert_from_base(RotationalStiffnessUnits.DecaNewtonMillimeterPerDegree)
        return self.__deca_newton_millimeters_per_degree

    
    @property
    def kilo_newton_millimeters_per_degree(self) -> float:
        """
        
        """
        if self.__kilo_newton_millimeters_per_degree != None:
            return self.__kilo_newton_millimeters_per_degree
        self.__kilo_newton_millimeters_per_degree = self.__convert_from_base(RotationalStiffnessUnits.KiloNewtonMillimeterPerDegree)
        return self.__kilo_newton_millimeters_per_degree

    
    @property
    def mega_newton_millimeters_per_degree(self) -> float:
        """
        
        """
        if self.__mega_newton_millimeters_per_degree != None:
            return self.__mega_newton_millimeters_per_degree
        self.__mega_newton_millimeters_per_degree = self.__convert_from_base(RotationalStiffnessUnits.MegaNewtonMillimeterPerDegree)
        return self.__mega_newton_millimeters_per_degree

    
    @property
    def nano_newton_meters_per_degree(self) -> float:
        """
        
        """
        if self.__nano_newton_meters_per_degree != None:
            return self.__nano_newton_meters_per_degree
        self.__nano_newton_meters_per_degree = self.__convert_from_base(RotationalStiffnessUnits.NanoNewtonMeterPerDegree)
        return self.__nano_newton_meters_per_degree

    
    @property
    def micro_newton_meters_per_degree(self) -> float:
        """
        
        """
        if self.__micro_newton_meters_per_degree != None:
            return self.__micro_newton_meters_per_degree
        self.__micro_newton_meters_per_degree = self.__convert_from_base(RotationalStiffnessUnits.MicroNewtonMeterPerDegree)
        return self.__micro_newton_meters_per_degree

    
    @property
    def milli_newton_meters_per_degree(self) -> float:
        """
        
        """
        if self.__milli_newton_meters_per_degree != None:
            return self.__milli_newton_meters_per_degree
        self.__milli_newton_meters_per_degree = self.__convert_from_base(RotationalStiffnessUnits.MilliNewtonMeterPerDegree)
        return self.__milli_newton_meters_per_degree

    
    @property
    def centi_newton_meters_per_degree(self) -> float:
        """
        
        """
        if self.__centi_newton_meters_per_degree != None:
            return self.__centi_newton_meters_per_degree
        self.__centi_newton_meters_per_degree = self.__convert_from_base(RotationalStiffnessUnits.CentiNewtonMeterPerDegree)
        return self.__centi_newton_meters_per_degree

    
    @property
    def deci_newton_meters_per_degree(self) -> float:
        """
        
        """
        if self.__deci_newton_meters_per_degree != None:
            return self.__deci_newton_meters_per_degree
        self.__deci_newton_meters_per_degree = self.__convert_from_base(RotationalStiffnessUnits.DeciNewtonMeterPerDegree)
        return self.__deci_newton_meters_per_degree

    
    @property
    def deca_newton_meters_per_degree(self) -> float:
        """
        
        """
        if self.__deca_newton_meters_per_degree != None:
            return self.__deca_newton_meters_per_degree
        self.__deca_newton_meters_per_degree = self.__convert_from_base(RotationalStiffnessUnits.DecaNewtonMeterPerDegree)
        return self.__deca_newton_meters_per_degree

    
    @property
    def kilo_newton_meters_per_degree(self) -> float:
        """
        
        """
        if self.__kilo_newton_meters_per_degree != None:
            return self.__kilo_newton_meters_per_degree
        self.__kilo_newton_meters_per_degree = self.__convert_from_base(RotationalStiffnessUnits.KiloNewtonMeterPerDegree)
        return self.__kilo_newton_meters_per_degree

    
    @property
    def mega_newton_meters_per_degree(self) -> float:
        """
        
        """
        if self.__mega_newton_meters_per_degree != None:
            return self.__mega_newton_meters_per_degree
        self.__mega_newton_meters_per_degree = self.__convert_from_base(RotationalStiffnessUnits.MegaNewtonMeterPerDegree)
        return self.__mega_newton_meters_per_degree

    
    @property
    def nano_newton_millimeters_per_radian(self) -> float:
        """
        
        """
        if self.__nano_newton_millimeters_per_radian != None:
            return self.__nano_newton_millimeters_per_radian
        self.__nano_newton_millimeters_per_radian = self.__convert_from_base(RotationalStiffnessUnits.NanoNewtonMillimeterPerRadian)
        return self.__nano_newton_millimeters_per_radian

    
    @property
    def micro_newton_millimeters_per_radian(self) -> float:
        """
        
        """
        if self.__micro_newton_millimeters_per_radian != None:
            return self.__micro_newton_millimeters_per_radian
        self.__micro_newton_millimeters_per_radian = self.__convert_from_base(RotationalStiffnessUnits.MicroNewtonMillimeterPerRadian)
        return self.__micro_newton_millimeters_per_radian

    
    @property
    def milli_newton_millimeters_per_radian(self) -> float:
        """
        
        """
        if self.__milli_newton_millimeters_per_radian != None:
            return self.__milli_newton_millimeters_per_radian
        self.__milli_newton_millimeters_per_radian = self.__convert_from_base(RotationalStiffnessUnits.MilliNewtonMillimeterPerRadian)
        return self.__milli_newton_millimeters_per_radian

    
    @property
    def centi_newton_millimeters_per_radian(self) -> float:
        """
        
        """
        if self.__centi_newton_millimeters_per_radian != None:
            return self.__centi_newton_millimeters_per_radian
        self.__centi_newton_millimeters_per_radian = self.__convert_from_base(RotationalStiffnessUnits.CentiNewtonMillimeterPerRadian)
        return self.__centi_newton_millimeters_per_radian

    
    @property
    def deci_newton_millimeters_per_radian(self) -> float:
        """
        
        """
        if self.__deci_newton_millimeters_per_radian != None:
            return self.__deci_newton_millimeters_per_radian
        self.__deci_newton_millimeters_per_radian = self.__convert_from_base(RotationalStiffnessUnits.DeciNewtonMillimeterPerRadian)
        return self.__deci_newton_millimeters_per_radian

    
    @property
    def deca_newton_millimeters_per_radian(self) -> float:
        """
        
        """
        if self.__deca_newton_millimeters_per_radian != None:
            return self.__deca_newton_millimeters_per_radian
        self.__deca_newton_millimeters_per_radian = self.__convert_from_base(RotationalStiffnessUnits.DecaNewtonMillimeterPerRadian)
        return self.__deca_newton_millimeters_per_radian

    
    @property
    def kilo_newton_millimeters_per_radian(self) -> float:
        """
        
        """
        if self.__kilo_newton_millimeters_per_radian != None:
            return self.__kilo_newton_millimeters_per_radian
        self.__kilo_newton_millimeters_per_radian = self.__convert_from_base(RotationalStiffnessUnits.KiloNewtonMillimeterPerRadian)
        return self.__kilo_newton_millimeters_per_radian

    
    @property
    def mega_newton_millimeters_per_radian(self) -> float:
        """
        
        """
        if self.__mega_newton_millimeters_per_radian != None:
            return self.__mega_newton_millimeters_per_radian
        self.__mega_newton_millimeters_per_radian = self.__convert_from_base(RotationalStiffnessUnits.MegaNewtonMillimeterPerRadian)
        return self.__mega_newton_millimeters_per_radian

    
    def to_string(self, unit: RotationalStiffnessUnits = RotationalStiffnessUnits.NewtonMeterPerRadian) -> string:
        """
        Format the RotationalStiffness to string.
        Note! the default format for RotationalStiffness is NewtonMeterPerRadian.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == RotationalStiffnessUnits.NewtonMeterPerRadian:
            return f"""{self.newton_meters_per_radian} N·m/rad"""
        
        if unit == RotationalStiffnessUnits.PoundForceFootPerDegrees:
            return f"""{self.pound_force_feet_per_degrees} lbf·ft/deg"""
        
        if unit == RotationalStiffnessUnits.KilopoundForceFootPerDegrees:
            return f"""{self.kilopound_force_feet_per_degrees} kipf·ft/°"""
        
        if unit == RotationalStiffnessUnits.NewtonMillimeterPerDegree:
            return f"""{self.newton_millimeters_per_degree} N·mm/deg"""
        
        if unit == RotationalStiffnessUnits.NewtonMeterPerDegree:
            return f"""{self.newton_meters_per_degree} N·m/deg"""
        
        if unit == RotationalStiffnessUnits.NewtonMillimeterPerRadian:
            return f"""{self.newton_millimeters_per_radian} N·mm/rad"""
        
        if unit == RotationalStiffnessUnits.PoundForceFeetPerRadian:
            return f"""{self.pound_force_feet_per_radian} lbf·ft/rad"""
        
        if unit == RotationalStiffnessUnits.KiloNewtonMeterPerRadian:
            return f"""{self.kilo_newton_meters_per_radian} """
        
        if unit == RotationalStiffnessUnits.MegaNewtonMeterPerRadian:
            return f"""{self.mega_newton_meters_per_radian} """
        
        if unit == RotationalStiffnessUnits.NanoNewtonMillimeterPerDegree:
            return f"""{self.nano_newton_millimeters_per_degree} """
        
        if unit == RotationalStiffnessUnits.MicroNewtonMillimeterPerDegree:
            return f"""{self.micro_newton_millimeters_per_degree} """
        
        if unit == RotationalStiffnessUnits.MilliNewtonMillimeterPerDegree:
            return f"""{self.milli_newton_millimeters_per_degree} """
        
        if unit == RotationalStiffnessUnits.CentiNewtonMillimeterPerDegree:
            return f"""{self.centi_newton_millimeters_per_degree} """
        
        if unit == RotationalStiffnessUnits.DeciNewtonMillimeterPerDegree:
            return f"""{self.deci_newton_millimeters_per_degree} """
        
        if unit == RotationalStiffnessUnits.DecaNewtonMillimeterPerDegree:
            return f"""{self.deca_newton_millimeters_per_degree} """
        
        if unit == RotationalStiffnessUnits.KiloNewtonMillimeterPerDegree:
            return f"""{self.kilo_newton_millimeters_per_degree} """
        
        if unit == RotationalStiffnessUnits.MegaNewtonMillimeterPerDegree:
            return f"""{self.mega_newton_millimeters_per_degree} """
        
        if unit == RotationalStiffnessUnits.NanoNewtonMeterPerDegree:
            return f"""{self.nano_newton_meters_per_degree} """
        
        if unit == RotationalStiffnessUnits.MicroNewtonMeterPerDegree:
            return f"""{self.micro_newton_meters_per_degree} """
        
        if unit == RotationalStiffnessUnits.MilliNewtonMeterPerDegree:
            return f"""{self.milli_newton_meters_per_degree} """
        
        if unit == RotationalStiffnessUnits.CentiNewtonMeterPerDegree:
            return f"""{self.centi_newton_meters_per_degree} """
        
        if unit == RotationalStiffnessUnits.DeciNewtonMeterPerDegree:
            return f"""{self.deci_newton_meters_per_degree} """
        
        if unit == RotationalStiffnessUnits.DecaNewtonMeterPerDegree:
            return f"""{self.deca_newton_meters_per_degree} """
        
        if unit == RotationalStiffnessUnits.KiloNewtonMeterPerDegree:
            return f"""{self.kilo_newton_meters_per_degree} """
        
        if unit == RotationalStiffnessUnits.MegaNewtonMeterPerDegree:
            return f"""{self.mega_newton_meters_per_degree} """
        
        if unit == RotationalStiffnessUnits.NanoNewtonMillimeterPerRadian:
            return f"""{self.nano_newton_millimeters_per_radian} """
        
        if unit == RotationalStiffnessUnits.MicroNewtonMillimeterPerRadian:
            return f"""{self.micro_newton_millimeters_per_radian} """
        
        if unit == RotationalStiffnessUnits.MilliNewtonMillimeterPerRadian:
            return f"""{self.milli_newton_millimeters_per_radian} """
        
        if unit == RotationalStiffnessUnits.CentiNewtonMillimeterPerRadian:
            return f"""{self.centi_newton_millimeters_per_radian} """
        
        if unit == RotationalStiffnessUnits.DeciNewtonMillimeterPerRadian:
            return f"""{self.deci_newton_millimeters_per_radian} """
        
        if unit == RotationalStiffnessUnits.DecaNewtonMillimeterPerRadian:
            return f"""{self.deca_newton_millimeters_per_radian} """
        
        if unit == RotationalStiffnessUnits.KiloNewtonMillimeterPerRadian:
            return f"""{self.kilo_newton_millimeters_per_radian} """
        
        if unit == RotationalStiffnessUnits.MegaNewtonMillimeterPerRadian:
            return f"""{self.mega_newton_millimeters_per_radian} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: RotationalStiffnessUnits = RotationalStiffnessUnits.NewtonMeterPerRadian) -> string:
        """
        Get RotationalStiffness unit abbreviation.
        Note! the default abbreviation for RotationalStiffness is NewtonMeterPerRadian.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == RotationalStiffnessUnits.NewtonMeterPerRadian:
            return """N·m/rad"""
        
        if unit_abbreviation == RotationalStiffnessUnits.PoundForceFootPerDegrees:
            return """lbf·ft/deg"""
        
        if unit_abbreviation == RotationalStiffnessUnits.KilopoundForceFootPerDegrees:
            return """kipf·ft/°"""
        
        if unit_abbreviation == RotationalStiffnessUnits.NewtonMillimeterPerDegree:
            return """N·mm/deg"""
        
        if unit_abbreviation == RotationalStiffnessUnits.NewtonMeterPerDegree:
            return """N·m/deg"""
        
        if unit_abbreviation == RotationalStiffnessUnits.NewtonMillimeterPerRadian:
            return """N·mm/rad"""
        
        if unit_abbreviation == RotationalStiffnessUnits.PoundForceFeetPerRadian:
            return """lbf·ft/rad"""
        
        if unit_abbreviation == RotationalStiffnessUnits.KiloNewtonMeterPerRadian:
            return """"""
        
        if unit_abbreviation == RotationalStiffnessUnits.MegaNewtonMeterPerRadian:
            return """"""
        
        if unit_abbreviation == RotationalStiffnessUnits.NanoNewtonMillimeterPerDegree:
            return """"""
        
        if unit_abbreviation == RotationalStiffnessUnits.MicroNewtonMillimeterPerDegree:
            return """"""
        
        if unit_abbreviation == RotationalStiffnessUnits.MilliNewtonMillimeterPerDegree:
            return """"""
        
        if unit_abbreviation == RotationalStiffnessUnits.CentiNewtonMillimeterPerDegree:
            return """"""
        
        if unit_abbreviation == RotationalStiffnessUnits.DeciNewtonMillimeterPerDegree:
            return """"""
        
        if unit_abbreviation == RotationalStiffnessUnits.DecaNewtonMillimeterPerDegree:
            return """"""
        
        if unit_abbreviation == RotationalStiffnessUnits.KiloNewtonMillimeterPerDegree:
            return """"""
        
        if unit_abbreviation == RotationalStiffnessUnits.MegaNewtonMillimeterPerDegree:
            return """"""
        
        if unit_abbreviation == RotationalStiffnessUnits.NanoNewtonMeterPerDegree:
            return """"""
        
        if unit_abbreviation == RotationalStiffnessUnits.MicroNewtonMeterPerDegree:
            return """"""
        
        if unit_abbreviation == RotationalStiffnessUnits.MilliNewtonMeterPerDegree:
            return """"""
        
        if unit_abbreviation == RotationalStiffnessUnits.CentiNewtonMeterPerDegree:
            return """"""
        
        if unit_abbreviation == RotationalStiffnessUnits.DeciNewtonMeterPerDegree:
            return """"""
        
        if unit_abbreviation == RotationalStiffnessUnits.DecaNewtonMeterPerDegree:
            return """"""
        
        if unit_abbreviation == RotationalStiffnessUnits.KiloNewtonMeterPerDegree:
            return """"""
        
        if unit_abbreviation == RotationalStiffnessUnits.MegaNewtonMeterPerDegree:
            return """"""
        
        if unit_abbreviation == RotationalStiffnessUnits.NanoNewtonMillimeterPerRadian:
            return """"""
        
        if unit_abbreviation == RotationalStiffnessUnits.MicroNewtonMillimeterPerRadian:
            return """"""
        
        if unit_abbreviation == RotationalStiffnessUnits.MilliNewtonMillimeterPerRadian:
            return """"""
        
        if unit_abbreviation == RotationalStiffnessUnits.CentiNewtonMillimeterPerRadian:
            return """"""
        
        if unit_abbreviation == RotationalStiffnessUnits.DeciNewtonMillimeterPerRadian:
            return """"""
        
        if unit_abbreviation == RotationalStiffnessUnits.DecaNewtonMillimeterPerRadian:
            return """"""
        
        if unit_abbreviation == RotationalStiffnessUnits.KiloNewtonMillimeterPerRadian:
            return """"""
        
        if unit_abbreviation == RotationalStiffnessUnits.MegaNewtonMillimeterPerRadian:
            return """"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, RotationalStiffness):
            raise TypeError("unsupported operand type(s) for +: 'RotationalStiffness' and '{}'".format(type(other).__name__))
        return RotationalStiffness(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, RotationalStiffness):
            raise TypeError("unsupported operand type(s) for *: 'RotationalStiffness' and '{}'".format(type(other).__name__))
        return RotationalStiffness(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, RotationalStiffness):
            raise TypeError("unsupported operand type(s) for -: 'RotationalStiffness' and '{}'".format(type(other).__name__))
        return RotationalStiffness(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, RotationalStiffness):
            raise TypeError("unsupported operand type(s) for /: 'RotationalStiffness' and '{}'".format(type(other).__name__))
        return RotationalStiffness(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, RotationalStiffness):
            raise TypeError("unsupported operand type(s) for %: 'RotationalStiffness' and '{}'".format(type(other).__name__))
        return RotationalStiffness(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, RotationalStiffness):
            raise TypeError("unsupported operand type(s) for **: 'RotationalStiffness' and '{}'".format(type(other).__name__))
        return RotationalStiffness(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, RotationalStiffness):
            raise TypeError("unsupported operand type(s) for ==: 'RotationalStiffness' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, RotationalStiffness):
            raise TypeError("unsupported operand type(s) for <: 'RotationalStiffness' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, RotationalStiffness):
            raise TypeError("unsupported operand type(s) for >: 'RotationalStiffness' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, RotationalStiffness):
            raise TypeError("unsupported operand type(s) for <=: 'RotationalStiffness' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, RotationalStiffness):
            raise TypeError("unsupported operand type(s) for >=: 'RotationalStiffness' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value
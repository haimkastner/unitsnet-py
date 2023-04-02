from enum import Enum
import math
import string


class SpecificWeightUnits(Enum):
        """
            SpecificWeightUnits enumeration
        """
        
        NewtonPerCubicMillimeter = 'newton_per_cubic_millimeter'
        """
            
        """
        
        NewtonPerCubicCentimeter = 'newton_per_cubic_centimeter'
        """
            
        """
        
        NewtonPerCubicMeter = 'newton_per_cubic_meter'
        """
            
        """
        
        KilogramForcePerCubicMillimeter = 'kilogram_force_per_cubic_millimeter'
        """
            
        """
        
        KilogramForcePerCubicCentimeter = 'kilogram_force_per_cubic_centimeter'
        """
            
        """
        
        KilogramForcePerCubicMeter = 'kilogram_force_per_cubic_meter'
        """
            
        """
        
        PoundForcePerCubicInch = 'pound_force_per_cubic_inch'
        """
            
        """
        
        PoundForcePerCubicFoot = 'pound_force_per_cubic_foot'
        """
            
        """
        
        TonneForcePerCubicMillimeter = 'tonne_force_per_cubic_millimeter'
        """
            
        """
        
        TonneForcePerCubicCentimeter = 'tonne_force_per_cubic_centimeter'
        """
            
        """
        
        TonneForcePerCubicMeter = 'tonne_force_per_cubic_meter'
        """
            
        """
        
        KiloNewtonPerCubicMillimeter = 'kilo_newton_per_cubic_millimeter'
        """
            
        """
        
        KiloNewtonPerCubicCentimeter = 'kilo_newton_per_cubic_centimeter'
        """
            
        """
        
        KiloNewtonPerCubicMeter = 'kilo_newton_per_cubic_meter'
        """
            
        """
        
        MegaNewtonPerCubicMeter = 'mega_newton_per_cubic_meter'
        """
            
        """
        
        KiloPoundForcePerCubicInch = 'kilo_pound_force_per_cubic_inch'
        """
            
        """
        
        KiloPoundForcePerCubicFoot = 'kilo_pound_force_per_cubic_foot'
        """
            
        """
        
    
class SpecificWeight:
    """
    The SpecificWeight, or more precisely, the volumetric weight density, of a substance is its weight per unit volume.

    Args:
        value (float): The value.
        from_unit (SpecificWeightUnits): The SpecificWeight unit to create from, The default unit is NewtonPerCubicMeter
    """
    def __init__(self, value: float, from_unit: SpecificWeightUnits = SpecificWeightUnits.NewtonPerCubicMeter):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__newtons_per_cubic_millimeter = None
        
        self.__newtons_per_cubic_centimeter = None
        
        self.__newtons_per_cubic_meter = None
        
        self.__kilograms_force_per_cubic_millimeter = None
        
        self.__kilograms_force_per_cubic_centimeter = None
        
        self.__kilograms_force_per_cubic_meter = None
        
        self.__pounds_force_per_cubic_inch = None
        
        self.__pounds_force_per_cubic_foot = None
        
        self.__tonnes_force_per_cubic_millimeter = None
        
        self.__tonnes_force_per_cubic_centimeter = None
        
        self.__tonnes_force_per_cubic_meter = None
        
        self.__kilo_newtons_per_cubic_millimeter = None
        
        self.__kilo_newtons_per_cubic_centimeter = None
        
        self.__kilo_newtons_per_cubic_meter = None
        
        self.__mega_newtons_per_cubic_meter = None
        
        self.__kilo_pounds_force_per_cubic_inch = None
        
        self.__kilo_pounds_force_per_cubic_foot = None
        

    def __convert_from_base(self, from_unit: SpecificWeightUnits) -> float:
        value = self.__value
        
        if from_unit == SpecificWeightUnits.NewtonPerCubicMillimeter:
            return (value * 0.000000001)
        
        if from_unit == SpecificWeightUnits.NewtonPerCubicCentimeter:
            return (value * 0.000001)
        
        if from_unit == SpecificWeightUnits.NewtonPerCubicMeter:
            return (value)
        
        if from_unit == SpecificWeightUnits.KilogramForcePerCubicMillimeter:
            return (value / 9.80665e9)
        
        if from_unit == SpecificWeightUnits.KilogramForcePerCubicCentimeter:
            return (value / 9.80665e6)
        
        if from_unit == SpecificWeightUnits.KilogramForcePerCubicMeter:
            return (value / 9.80665)
        
        if from_unit == SpecificWeightUnits.PoundForcePerCubicInch:
            return (value / 2.714471375263134e5)
        
        if from_unit == SpecificWeightUnits.PoundForcePerCubicFoot:
            return (value / 1.570874638462462e2)
        
        if from_unit == SpecificWeightUnits.TonneForcePerCubicMillimeter:
            return (value / 9.80665e12)
        
        if from_unit == SpecificWeightUnits.TonneForcePerCubicCentimeter:
            return (value / 9.80665e9)
        
        if from_unit == SpecificWeightUnits.TonneForcePerCubicMeter:
            return (value / 9.80665e3)
        
        if from_unit == SpecificWeightUnits.KiloNewtonPerCubicMillimeter:
            return ((value * 0.000000001) / 1000.0)
        
        if from_unit == SpecificWeightUnits.KiloNewtonPerCubicCentimeter:
            return ((value * 0.000001) / 1000.0)
        
        if from_unit == SpecificWeightUnits.KiloNewtonPerCubicMeter:
            return ((value) / 1000.0)
        
        if from_unit == SpecificWeightUnits.MegaNewtonPerCubicMeter:
            return ((value) / 1000000.0)
        
        if from_unit == SpecificWeightUnits.KiloPoundForcePerCubicInch:
            return ((value / 2.714471375263134e5) / 1000.0)
        
        if from_unit == SpecificWeightUnits.KiloPoundForcePerCubicFoot:
            return ((value / 1.570874638462462e2) / 1000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: SpecificWeightUnits) -> float:
        
        if to_unit == SpecificWeightUnits.NewtonPerCubicMillimeter:
            return (value * 1000000000)
        
        if to_unit == SpecificWeightUnits.NewtonPerCubicCentimeter:
            return (value * 1000000)
        
        if to_unit == SpecificWeightUnits.NewtonPerCubicMeter:
            return (value)
        
        if to_unit == SpecificWeightUnits.KilogramForcePerCubicMillimeter:
            return (value * 9.80665e9)
        
        if to_unit == SpecificWeightUnits.KilogramForcePerCubicCentimeter:
            return (value * 9.80665e6)
        
        if to_unit == SpecificWeightUnits.KilogramForcePerCubicMeter:
            return (value * 9.80665)
        
        if to_unit == SpecificWeightUnits.PoundForcePerCubicInch:
            return (value * 2.714471375263134e5)
        
        if to_unit == SpecificWeightUnits.PoundForcePerCubicFoot:
            return (value * 1.570874638462462e2)
        
        if to_unit == SpecificWeightUnits.TonneForcePerCubicMillimeter:
            return (value * 9.80665e12)
        
        if to_unit == SpecificWeightUnits.TonneForcePerCubicCentimeter:
            return (value * 9.80665e9)
        
        if to_unit == SpecificWeightUnits.TonneForcePerCubicMeter:
            return (value * 9.80665e3)
        
        if to_unit == SpecificWeightUnits.KiloNewtonPerCubicMillimeter:
            return ((value * 1000000000) * 1000.0)
        
        if to_unit == SpecificWeightUnits.KiloNewtonPerCubicCentimeter:
            return ((value * 1000000) * 1000.0)
        
        if to_unit == SpecificWeightUnits.KiloNewtonPerCubicMeter:
            return ((value) * 1000.0)
        
        if to_unit == SpecificWeightUnits.MegaNewtonPerCubicMeter:
            return ((value) * 1000000.0)
        
        if to_unit == SpecificWeightUnits.KiloPoundForcePerCubicInch:
            return ((value * 2.714471375263134e5) * 1000.0)
        
        if to_unit == SpecificWeightUnits.KiloPoundForcePerCubicFoot:
            return ((value * 1.570874638462462e2) * 1000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
    @staticmethod
    def from_newtons_per_cubic_millimeter(newtons_per_cubic_millimeter: float):
        """
        Create a new instance of SpecificWeight from a value in newtons_per_cubic_millimeter.

        

        :param meters: The SpecificWeight value in newtons_per_cubic_millimeter.
        :type newtons_per_cubic_millimeter: float
        :return: A new instance of SpecificWeight.
        :rtype: SpecificWeight
        """
        return SpecificWeight(newtons_per_cubic_millimeter, SpecificWeightUnits.NewtonPerCubicMillimeter)

    
    @staticmethod
    def from_newtons_per_cubic_centimeter(newtons_per_cubic_centimeter: float):
        """
        Create a new instance of SpecificWeight from a value in newtons_per_cubic_centimeter.

        

        :param meters: The SpecificWeight value in newtons_per_cubic_centimeter.
        :type newtons_per_cubic_centimeter: float
        :return: A new instance of SpecificWeight.
        :rtype: SpecificWeight
        """
        return SpecificWeight(newtons_per_cubic_centimeter, SpecificWeightUnits.NewtonPerCubicCentimeter)

    
    @staticmethod
    def from_newtons_per_cubic_meter(newtons_per_cubic_meter: float):
        """
        Create a new instance of SpecificWeight from a value in newtons_per_cubic_meter.

        

        :param meters: The SpecificWeight value in newtons_per_cubic_meter.
        :type newtons_per_cubic_meter: float
        :return: A new instance of SpecificWeight.
        :rtype: SpecificWeight
        """
        return SpecificWeight(newtons_per_cubic_meter, SpecificWeightUnits.NewtonPerCubicMeter)

    
    @staticmethod
    def from_kilograms_force_per_cubic_millimeter(kilograms_force_per_cubic_millimeter: float):
        """
        Create a new instance of SpecificWeight from a value in kilograms_force_per_cubic_millimeter.

        

        :param meters: The SpecificWeight value in kilograms_force_per_cubic_millimeter.
        :type kilograms_force_per_cubic_millimeter: float
        :return: A new instance of SpecificWeight.
        :rtype: SpecificWeight
        """
        return SpecificWeight(kilograms_force_per_cubic_millimeter, SpecificWeightUnits.KilogramForcePerCubicMillimeter)

    
    @staticmethod
    def from_kilograms_force_per_cubic_centimeter(kilograms_force_per_cubic_centimeter: float):
        """
        Create a new instance of SpecificWeight from a value in kilograms_force_per_cubic_centimeter.

        

        :param meters: The SpecificWeight value in kilograms_force_per_cubic_centimeter.
        :type kilograms_force_per_cubic_centimeter: float
        :return: A new instance of SpecificWeight.
        :rtype: SpecificWeight
        """
        return SpecificWeight(kilograms_force_per_cubic_centimeter, SpecificWeightUnits.KilogramForcePerCubicCentimeter)

    
    @staticmethod
    def from_kilograms_force_per_cubic_meter(kilograms_force_per_cubic_meter: float):
        """
        Create a new instance of SpecificWeight from a value in kilograms_force_per_cubic_meter.

        

        :param meters: The SpecificWeight value in kilograms_force_per_cubic_meter.
        :type kilograms_force_per_cubic_meter: float
        :return: A new instance of SpecificWeight.
        :rtype: SpecificWeight
        """
        return SpecificWeight(kilograms_force_per_cubic_meter, SpecificWeightUnits.KilogramForcePerCubicMeter)

    
    @staticmethod
    def from_pounds_force_per_cubic_inch(pounds_force_per_cubic_inch: float):
        """
        Create a new instance of SpecificWeight from a value in pounds_force_per_cubic_inch.

        

        :param meters: The SpecificWeight value in pounds_force_per_cubic_inch.
        :type pounds_force_per_cubic_inch: float
        :return: A new instance of SpecificWeight.
        :rtype: SpecificWeight
        """
        return SpecificWeight(pounds_force_per_cubic_inch, SpecificWeightUnits.PoundForcePerCubicInch)

    
    @staticmethod
    def from_pounds_force_per_cubic_foot(pounds_force_per_cubic_foot: float):
        """
        Create a new instance of SpecificWeight from a value in pounds_force_per_cubic_foot.

        

        :param meters: The SpecificWeight value in pounds_force_per_cubic_foot.
        :type pounds_force_per_cubic_foot: float
        :return: A new instance of SpecificWeight.
        :rtype: SpecificWeight
        """
        return SpecificWeight(pounds_force_per_cubic_foot, SpecificWeightUnits.PoundForcePerCubicFoot)

    
    @staticmethod
    def from_tonnes_force_per_cubic_millimeter(tonnes_force_per_cubic_millimeter: float):
        """
        Create a new instance of SpecificWeight from a value in tonnes_force_per_cubic_millimeter.

        

        :param meters: The SpecificWeight value in tonnes_force_per_cubic_millimeter.
        :type tonnes_force_per_cubic_millimeter: float
        :return: A new instance of SpecificWeight.
        :rtype: SpecificWeight
        """
        return SpecificWeight(tonnes_force_per_cubic_millimeter, SpecificWeightUnits.TonneForcePerCubicMillimeter)

    
    @staticmethod
    def from_tonnes_force_per_cubic_centimeter(tonnes_force_per_cubic_centimeter: float):
        """
        Create a new instance of SpecificWeight from a value in tonnes_force_per_cubic_centimeter.

        

        :param meters: The SpecificWeight value in tonnes_force_per_cubic_centimeter.
        :type tonnes_force_per_cubic_centimeter: float
        :return: A new instance of SpecificWeight.
        :rtype: SpecificWeight
        """
        return SpecificWeight(tonnes_force_per_cubic_centimeter, SpecificWeightUnits.TonneForcePerCubicCentimeter)

    
    @staticmethod
    def from_tonnes_force_per_cubic_meter(tonnes_force_per_cubic_meter: float):
        """
        Create a new instance of SpecificWeight from a value in tonnes_force_per_cubic_meter.

        

        :param meters: The SpecificWeight value in tonnes_force_per_cubic_meter.
        :type tonnes_force_per_cubic_meter: float
        :return: A new instance of SpecificWeight.
        :rtype: SpecificWeight
        """
        return SpecificWeight(tonnes_force_per_cubic_meter, SpecificWeightUnits.TonneForcePerCubicMeter)

    
    @staticmethod
    def from_kilo_newtons_per_cubic_millimeter(kilo_newtons_per_cubic_millimeter: float):
        """
        Create a new instance of SpecificWeight from a value in kilo_newtons_per_cubic_millimeter.

        

        :param meters: The SpecificWeight value in kilo_newtons_per_cubic_millimeter.
        :type kilo_newtons_per_cubic_millimeter: float
        :return: A new instance of SpecificWeight.
        :rtype: SpecificWeight
        """
        return SpecificWeight(kilo_newtons_per_cubic_millimeter, SpecificWeightUnits.KiloNewtonPerCubicMillimeter)

    
    @staticmethod
    def from_kilo_newtons_per_cubic_centimeter(kilo_newtons_per_cubic_centimeter: float):
        """
        Create a new instance of SpecificWeight from a value in kilo_newtons_per_cubic_centimeter.

        

        :param meters: The SpecificWeight value in kilo_newtons_per_cubic_centimeter.
        :type kilo_newtons_per_cubic_centimeter: float
        :return: A new instance of SpecificWeight.
        :rtype: SpecificWeight
        """
        return SpecificWeight(kilo_newtons_per_cubic_centimeter, SpecificWeightUnits.KiloNewtonPerCubicCentimeter)

    
    @staticmethod
    def from_kilo_newtons_per_cubic_meter(kilo_newtons_per_cubic_meter: float):
        """
        Create a new instance of SpecificWeight from a value in kilo_newtons_per_cubic_meter.

        

        :param meters: The SpecificWeight value in kilo_newtons_per_cubic_meter.
        :type kilo_newtons_per_cubic_meter: float
        :return: A new instance of SpecificWeight.
        :rtype: SpecificWeight
        """
        return SpecificWeight(kilo_newtons_per_cubic_meter, SpecificWeightUnits.KiloNewtonPerCubicMeter)

    
    @staticmethod
    def from_mega_newtons_per_cubic_meter(mega_newtons_per_cubic_meter: float):
        """
        Create a new instance of SpecificWeight from a value in mega_newtons_per_cubic_meter.

        

        :param meters: The SpecificWeight value in mega_newtons_per_cubic_meter.
        :type mega_newtons_per_cubic_meter: float
        :return: A new instance of SpecificWeight.
        :rtype: SpecificWeight
        """
        return SpecificWeight(mega_newtons_per_cubic_meter, SpecificWeightUnits.MegaNewtonPerCubicMeter)

    
    @staticmethod
    def from_kilo_pounds_force_per_cubic_inch(kilo_pounds_force_per_cubic_inch: float):
        """
        Create a new instance of SpecificWeight from a value in kilo_pounds_force_per_cubic_inch.

        

        :param meters: The SpecificWeight value in kilo_pounds_force_per_cubic_inch.
        :type kilo_pounds_force_per_cubic_inch: float
        :return: A new instance of SpecificWeight.
        :rtype: SpecificWeight
        """
        return SpecificWeight(kilo_pounds_force_per_cubic_inch, SpecificWeightUnits.KiloPoundForcePerCubicInch)

    
    @staticmethod
    def from_kilo_pounds_force_per_cubic_foot(kilo_pounds_force_per_cubic_foot: float):
        """
        Create a new instance of SpecificWeight from a value in kilo_pounds_force_per_cubic_foot.

        

        :param meters: The SpecificWeight value in kilo_pounds_force_per_cubic_foot.
        :type kilo_pounds_force_per_cubic_foot: float
        :return: A new instance of SpecificWeight.
        :rtype: SpecificWeight
        """
        return SpecificWeight(kilo_pounds_force_per_cubic_foot, SpecificWeightUnits.KiloPoundForcePerCubicFoot)

    
    @property
    def newtons_per_cubic_millimeter(self) -> float:
        """
        
        """
        if self.__newtons_per_cubic_millimeter != None:
            return self.__newtons_per_cubic_millimeter
        self.__newtons_per_cubic_millimeter = self.__convert_from_base(SpecificWeightUnits.NewtonPerCubicMillimeter)
        return self.__newtons_per_cubic_millimeter

    
    @property
    def newtons_per_cubic_centimeter(self) -> float:
        """
        
        """
        if self.__newtons_per_cubic_centimeter != None:
            return self.__newtons_per_cubic_centimeter
        self.__newtons_per_cubic_centimeter = self.__convert_from_base(SpecificWeightUnits.NewtonPerCubicCentimeter)
        return self.__newtons_per_cubic_centimeter

    
    @property
    def newtons_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__newtons_per_cubic_meter != None:
            return self.__newtons_per_cubic_meter
        self.__newtons_per_cubic_meter = self.__convert_from_base(SpecificWeightUnits.NewtonPerCubicMeter)
        return self.__newtons_per_cubic_meter

    
    @property
    def kilograms_force_per_cubic_millimeter(self) -> float:
        """
        
        """
        if self.__kilograms_force_per_cubic_millimeter != None:
            return self.__kilograms_force_per_cubic_millimeter
        self.__kilograms_force_per_cubic_millimeter = self.__convert_from_base(SpecificWeightUnits.KilogramForcePerCubicMillimeter)
        return self.__kilograms_force_per_cubic_millimeter

    
    @property
    def kilograms_force_per_cubic_centimeter(self) -> float:
        """
        
        """
        if self.__kilograms_force_per_cubic_centimeter != None:
            return self.__kilograms_force_per_cubic_centimeter
        self.__kilograms_force_per_cubic_centimeter = self.__convert_from_base(SpecificWeightUnits.KilogramForcePerCubicCentimeter)
        return self.__kilograms_force_per_cubic_centimeter

    
    @property
    def kilograms_force_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__kilograms_force_per_cubic_meter != None:
            return self.__kilograms_force_per_cubic_meter
        self.__kilograms_force_per_cubic_meter = self.__convert_from_base(SpecificWeightUnits.KilogramForcePerCubicMeter)
        return self.__kilograms_force_per_cubic_meter

    
    @property
    def pounds_force_per_cubic_inch(self) -> float:
        """
        
        """
        if self.__pounds_force_per_cubic_inch != None:
            return self.__pounds_force_per_cubic_inch
        self.__pounds_force_per_cubic_inch = self.__convert_from_base(SpecificWeightUnits.PoundForcePerCubicInch)
        return self.__pounds_force_per_cubic_inch

    
    @property
    def pounds_force_per_cubic_foot(self) -> float:
        """
        
        """
        if self.__pounds_force_per_cubic_foot != None:
            return self.__pounds_force_per_cubic_foot
        self.__pounds_force_per_cubic_foot = self.__convert_from_base(SpecificWeightUnits.PoundForcePerCubicFoot)
        return self.__pounds_force_per_cubic_foot

    
    @property
    def tonnes_force_per_cubic_millimeter(self) -> float:
        """
        
        """
        if self.__tonnes_force_per_cubic_millimeter != None:
            return self.__tonnes_force_per_cubic_millimeter
        self.__tonnes_force_per_cubic_millimeter = self.__convert_from_base(SpecificWeightUnits.TonneForcePerCubicMillimeter)
        return self.__tonnes_force_per_cubic_millimeter

    
    @property
    def tonnes_force_per_cubic_centimeter(self) -> float:
        """
        
        """
        if self.__tonnes_force_per_cubic_centimeter != None:
            return self.__tonnes_force_per_cubic_centimeter
        self.__tonnes_force_per_cubic_centimeter = self.__convert_from_base(SpecificWeightUnits.TonneForcePerCubicCentimeter)
        return self.__tonnes_force_per_cubic_centimeter

    
    @property
    def tonnes_force_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__tonnes_force_per_cubic_meter != None:
            return self.__tonnes_force_per_cubic_meter
        self.__tonnes_force_per_cubic_meter = self.__convert_from_base(SpecificWeightUnits.TonneForcePerCubicMeter)
        return self.__tonnes_force_per_cubic_meter

    
    @property
    def kilo_newtons_per_cubic_millimeter(self) -> float:
        """
        
        """
        if self.__kilo_newtons_per_cubic_millimeter != None:
            return self.__kilo_newtons_per_cubic_millimeter
        self.__kilo_newtons_per_cubic_millimeter = self.__convert_from_base(SpecificWeightUnits.KiloNewtonPerCubicMillimeter)
        return self.__kilo_newtons_per_cubic_millimeter

    
    @property
    def kilo_newtons_per_cubic_centimeter(self) -> float:
        """
        
        """
        if self.__kilo_newtons_per_cubic_centimeter != None:
            return self.__kilo_newtons_per_cubic_centimeter
        self.__kilo_newtons_per_cubic_centimeter = self.__convert_from_base(SpecificWeightUnits.KiloNewtonPerCubicCentimeter)
        return self.__kilo_newtons_per_cubic_centimeter

    
    @property
    def kilo_newtons_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__kilo_newtons_per_cubic_meter != None:
            return self.__kilo_newtons_per_cubic_meter
        self.__kilo_newtons_per_cubic_meter = self.__convert_from_base(SpecificWeightUnits.KiloNewtonPerCubicMeter)
        return self.__kilo_newtons_per_cubic_meter

    
    @property
    def mega_newtons_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__mega_newtons_per_cubic_meter != None:
            return self.__mega_newtons_per_cubic_meter
        self.__mega_newtons_per_cubic_meter = self.__convert_from_base(SpecificWeightUnits.MegaNewtonPerCubicMeter)
        return self.__mega_newtons_per_cubic_meter

    
    @property
    def kilo_pounds_force_per_cubic_inch(self) -> float:
        """
        
        """
        if self.__kilo_pounds_force_per_cubic_inch != None:
            return self.__kilo_pounds_force_per_cubic_inch
        self.__kilo_pounds_force_per_cubic_inch = self.__convert_from_base(SpecificWeightUnits.KiloPoundForcePerCubicInch)
        return self.__kilo_pounds_force_per_cubic_inch

    
    @property
    def kilo_pounds_force_per_cubic_foot(self) -> float:
        """
        
        """
        if self.__kilo_pounds_force_per_cubic_foot != None:
            return self.__kilo_pounds_force_per_cubic_foot
        self.__kilo_pounds_force_per_cubic_foot = self.__convert_from_base(SpecificWeightUnits.KiloPoundForcePerCubicFoot)
        return self.__kilo_pounds_force_per_cubic_foot

    
    def to_string(self, unit: SpecificWeightUnits = SpecificWeightUnits.NewtonPerCubicMeter) -> string:
        """
        Format the SpecificWeight to string.
        Note! the default format for SpecificWeight is NewtonPerCubicMeter.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == SpecificWeightUnits.NewtonPerCubicMillimeter:
            return f"""{self.newtons_per_cubic_millimeter} N/mm³"""
        
        if unit == SpecificWeightUnits.NewtonPerCubicCentimeter:
            return f"""{self.newtons_per_cubic_centimeter} N/cm³"""
        
        if unit == SpecificWeightUnits.NewtonPerCubicMeter:
            return f"""{self.newtons_per_cubic_meter} N/m³"""
        
        if unit == SpecificWeightUnits.KilogramForcePerCubicMillimeter:
            return f"""{self.kilograms_force_per_cubic_millimeter} kgf/mm³"""
        
        if unit == SpecificWeightUnits.KilogramForcePerCubicCentimeter:
            return f"""{self.kilograms_force_per_cubic_centimeter} kgf/cm³"""
        
        if unit == SpecificWeightUnits.KilogramForcePerCubicMeter:
            return f"""{self.kilograms_force_per_cubic_meter} kgf/m³"""
        
        if unit == SpecificWeightUnits.PoundForcePerCubicInch:
            return f"""{self.pounds_force_per_cubic_inch} lbf/in³"""
        
        if unit == SpecificWeightUnits.PoundForcePerCubicFoot:
            return f"""{self.pounds_force_per_cubic_foot} lbf/ft³"""
        
        if unit == SpecificWeightUnits.TonneForcePerCubicMillimeter:
            return f"""{self.tonnes_force_per_cubic_millimeter} tf/mm³"""
        
        if unit == SpecificWeightUnits.TonneForcePerCubicCentimeter:
            return f"""{self.tonnes_force_per_cubic_centimeter} tf/cm³"""
        
        if unit == SpecificWeightUnits.TonneForcePerCubicMeter:
            return f"""{self.tonnes_force_per_cubic_meter} tf/m³"""
        
        if unit == SpecificWeightUnits.KiloNewtonPerCubicMillimeter:
            return f"""{self.kilo_newtons_per_cubic_millimeter} """
        
        if unit == SpecificWeightUnits.KiloNewtonPerCubicCentimeter:
            return f"""{self.kilo_newtons_per_cubic_centimeter} """
        
        if unit == SpecificWeightUnits.KiloNewtonPerCubicMeter:
            return f"""{self.kilo_newtons_per_cubic_meter} """
        
        if unit == SpecificWeightUnits.MegaNewtonPerCubicMeter:
            return f"""{self.mega_newtons_per_cubic_meter} """
        
        if unit == SpecificWeightUnits.KiloPoundForcePerCubicInch:
            return f"""{self.kilo_pounds_force_per_cubic_inch} """
        
        if unit == SpecificWeightUnits.KiloPoundForcePerCubicFoot:
            return f"""{self.kilo_pounds_force_per_cubic_foot} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: SpecificWeightUnits = SpecificWeightUnits.NewtonPerCubicMeter) -> string:
        """
        Get SpecificWeight unit abbreviation.
        Note! the default abbreviation for SpecificWeight is NewtonPerCubicMeter.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == SpecificWeightUnits.NewtonPerCubicMillimeter:
            return """N/mm³"""
        
        if unit_abbreviation == SpecificWeightUnits.NewtonPerCubicCentimeter:
            return """N/cm³"""
        
        if unit_abbreviation == SpecificWeightUnits.NewtonPerCubicMeter:
            return """N/m³"""
        
        if unit_abbreviation == SpecificWeightUnits.KilogramForcePerCubicMillimeter:
            return """kgf/mm³"""
        
        if unit_abbreviation == SpecificWeightUnits.KilogramForcePerCubicCentimeter:
            return """kgf/cm³"""
        
        if unit_abbreviation == SpecificWeightUnits.KilogramForcePerCubicMeter:
            return """kgf/m³"""
        
        if unit_abbreviation == SpecificWeightUnits.PoundForcePerCubicInch:
            return """lbf/in³"""
        
        if unit_abbreviation == SpecificWeightUnits.PoundForcePerCubicFoot:
            return """lbf/ft³"""
        
        if unit_abbreviation == SpecificWeightUnits.TonneForcePerCubicMillimeter:
            return """tf/mm³"""
        
        if unit_abbreviation == SpecificWeightUnits.TonneForcePerCubicCentimeter:
            return """tf/cm³"""
        
        if unit_abbreviation == SpecificWeightUnits.TonneForcePerCubicMeter:
            return """tf/m³"""
        
        if unit_abbreviation == SpecificWeightUnits.KiloNewtonPerCubicMillimeter:
            return """"""
        
        if unit_abbreviation == SpecificWeightUnits.KiloNewtonPerCubicCentimeter:
            return """"""
        
        if unit_abbreviation == SpecificWeightUnits.KiloNewtonPerCubicMeter:
            return """"""
        
        if unit_abbreviation == SpecificWeightUnits.MegaNewtonPerCubicMeter:
            return """"""
        
        if unit_abbreviation == SpecificWeightUnits.KiloPoundForcePerCubicInch:
            return """"""
        
        if unit_abbreviation == SpecificWeightUnits.KiloPoundForcePerCubicFoot:
            return """"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, SpecificWeight):
            raise TypeError("unsupported operand type(s) for +: 'SpecificWeight' and '{}'".format(type(other).__name__))
        return SpecificWeight(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, SpecificWeight):
            raise TypeError("unsupported operand type(s) for *: 'SpecificWeight' and '{}'".format(type(other).__name__))
        return SpecificWeight(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, SpecificWeight):
            raise TypeError("unsupported operand type(s) for -: 'SpecificWeight' and '{}'".format(type(other).__name__))
        return SpecificWeight(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, SpecificWeight):
            raise TypeError("unsupported operand type(s) for /: 'SpecificWeight' and '{}'".format(type(other).__name__))
        return SpecificWeight(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, SpecificWeight):
            raise TypeError("unsupported operand type(s) for %: 'SpecificWeight' and '{}'".format(type(other).__name__))
        return SpecificWeight(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, SpecificWeight):
            raise TypeError("unsupported operand type(s) for **: 'SpecificWeight' and '{}'".format(type(other).__name__))
        return SpecificWeight(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, SpecificWeight):
            raise TypeError("unsupported operand type(s) for ==: 'SpecificWeight' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, SpecificWeight):
            raise TypeError("unsupported operand type(s) for <: 'SpecificWeight' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, SpecificWeight):
            raise TypeError("unsupported operand type(s) for >: 'SpecificWeight' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, SpecificWeight):
            raise TypeError("unsupported operand type(s) for <=: 'SpecificWeight' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, SpecificWeight):
            raise TypeError("unsupported operand type(s) for >=: 'SpecificWeight' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value
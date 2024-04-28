from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class SpecificWeightUnits(Enum):
        """
            SpecificWeightUnits enumeration
        """
        
        NewtonPerCubicMillimeter = 'NewtonPerCubicMillimeter'
        """
            
        """
        
        NewtonPerCubicCentimeter = 'NewtonPerCubicCentimeter'
        """
            
        """
        
        NewtonPerCubicMeter = 'NewtonPerCubicMeter'
        """
            
        """
        
        KilogramForcePerCubicMillimeter = 'KilogramForcePerCubicMillimeter'
        """
            
        """
        
        KilogramForcePerCubicCentimeter = 'KilogramForcePerCubicCentimeter'
        """
            
        """
        
        KilogramForcePerCubicMeter = 'KilogramForcePerCubicMeter'
        """
            
        """
        
        PoundForcePerCubicInch = 'PoundForcePerCubicInch'
        """
            
        """
        
        PoundForcePerCubicFoot = 'PoundForcePerCubicFoot'
        """
            
        """
        
        TonneForcePerCubicMillimeter = 'TonneForcePerCubicMillimeter'
        """
            
        """
        
        TonneForcePerCubicCentimeter = 'TonneForcePerCubicCentimeter'
        """
            
        """
        
        TonneForcePerCubicMeter = 'TonneForcePerCubicMeter'
        """
            
        """
        
        KilonewtonPerCubicMillimeter = 'KilonewtonPerCubicMillimeter'
        """
            
        """
        
        KilonewtonPerCubicCentimeter = 'KilonewtonPerCubicCentimeter'
        """
            
        """
        
        KilonewtonPerCubicMeter = 'KilonewtonPerCubicMeter'
        """
            
        """
        
        MeganewtonPerCubicMeter = 'MeganewtonPerCubicMeter'
        """
            
        """
        
        KilopoundForcePerCubicInch = 'KilopoundForcePerCubicInch'
        """
            
        """
        
        KilopoundForcePerCubicFoot = 'KilopoundForcePerCubicFoot'
        """
            
        """
        

class SpecificWeightDto:
    """
    A DTO representation of a SpecificWeight

    Attributes:
        value (float): The value of the SpecificWeight.
        unit (SpecificWeightUnits): The specific unit that the SpecificWeight value is representing.
    """

    def __init__(self, value: float, unit: SpecificWeightUnits):
        """
        Create a new DTO representation of a SpecificWeight

        Parameters:
            value (float): The value of the SpecificWeight.
            unit (SpecificWeightUnits): The specific unit that the SpecificWeight value is representing.
        """
        self.value: float = value
        """
        The value of the SpecificWeight
        """
        self.unit: SpecificWeightUnits = unit
        """
        The specific unit that the SpecificWeight value is representing
        """

    def to_json(self):
        """
        Get a SpecificWeight DTO JSON object representing the current unit.

        :return: JSON object represents SpecificWeight DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "NewtonPerCubicMeter"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of SpecificWeight DTO from a json representation.

        :param data: The SpecificWeight DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "NewtonPerCubicMeter"}
        :return: A new instance of SpecificWeightDto.
        :rtype: SpecificWeightDto
        """
        return SpecificWeightDto(value=data["value"], unit=SpecificWeightUnits(data["unit"]))


class SpecificWeight(AbstractMeasure):
    """
    The SpecificWeight, or more precisely, the volumetric weight density, of a substance is its weight per unit volume.

    Args:
        value (float): The value.
        from_unit (SpecificWeightUnits): The SpecificWeight unit to create from, The default unit is NewtonPerCubicMeter
    """
    def __init__(self, value: float, from_unit: SpecificWeightUnits = SpecificWeightUnits.NewtonPerCubicMeter):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
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
        
        self.__kilonewtons_per_cubic_millimeter = None
        
        self.__kilonewtons_per_cubic_centimeter = None
        
        self.__kilonewtons_per_cubic_meter = None
        
        self.__meganewtons_per_cubic_meter = None
        
        self.__kilopounds_force_per_cubic_inch = None
        
        self.__kilopounds_force_per_cubic_foot = None
        

    def convert(self, unit: SpecificWeightUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: SpecificWeightUnits = SpecificWeightUnits.NewtonPerCubicMeter) -> SpecificWeightDto:
        """
        Get a new instance of SpecificWeight DTO representing the current unit.

        :param hold_in_unit: The specific SpecificWeight unit to store the SpecificWeight value in the DTO representation.
        :type hold_in_unit: SpecificWeightUnits
        :return: A new instance of SpecificWeightDto.
        :rtype: SpecificWeightDto
        """
        return SpecificWeightDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: SpecificWeightUnits = SpecificWeightUnits.NewtonPerCubicMeter):
        """
        Get a SpecificWeight DTO JSON object representing the current unit.

        :param hold_in_unit: The specific SpecificWeight unit to store the SpecificWeight value in the DTO representation.
        :type hold_in_unit: SpecificWeightUnits
        :return: JSON object represents SpecificWeight DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "NewtonPerCubicMeter"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(specific_weight_dto: SpecificWeightDto):
        """
        Obtain a new instance of SpecificWeight from a DTO unit object.

        :param specific_weight_dto: The SpecificWeight DTO representation.
        :type specific_weight_dto: SpecificWeightDto
        :return: A new instance of SpecificWeight.
        :rtype: SpecificWeight
        """
        return SpecificWeight(specific_weight_dto.value, specific_weight_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of SpecificWeight from a DTO unit json representation.

        :param data: The SpecificWeight DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "NewtonPerCubicMeter"}
        :return: A new instance of SpecificWeight.
        :rtype: SpecificWeight
        """
        return SpecificWeight.from_dto(SpecificWeightDto.from_json(data))

    def __convert_from_base(self, from_unit: SpecificWeightUnits) -> float:
        value = self._value
        
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
        
        if from_unit == SpecificWeightUnits.KilonewtonPerCubicMillimeter:
            return ((value * 0.000000001) / 1000.0)
        
        if from_unit == SpecificWeightUnits.KilonewtonPerCubicCentimeter:
            return ((value * 0.000001) / 1000.0)
        
        if from_unit == SpecificWeightUnits.KilonewtonPerCubicMeter:
            return ((value) / 1000.0)
        
        if from_unit == SpecificWeightUnits.MeganewtonPerCubicMeter:
            return ((value) / 1000000.0)
        
        if from_unit == SpecificWeightUnits.KilopoundForcePerCubicInch:
            return ((value / 2.714471375263134e5) / 1000.0)
        
        if from_unit == SpecificWeightUnits.KilopoundForcePerCubicFoot:
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
        
        if to_unit == SpecificWeightUnits.KilonewtonPerCubicMillimeter:
            return ((value * 1000000000) * 1000.0)
        
        if to_unit == SpecificWeightUnits.KilonewtonPerCubicCentimeter:
            return ((value * 1000000) * 1000.0)
        
        if to_unit == SpecificWeightUnits.KilonewtonPerCubicMeter:
            return ((value) * 1000.0)
        
        if to_unit == SpecificWeightUnits.MeganewtonPerCubicMeter:
            return ((value) * 1000000.0)
        
        if to_unit == SpecificWeightUnits.KilopoundForcePerCubicInch:
            return ((value * 2.714471375263134e5) * 1000.0)
        
        if to_unit == SpecificWeightUnits.KilopoundForcePerCubicFoot:
            return ((value * 1.570874638462462e2) * 1000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
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
    def from_kilonewtons_per_cubic_millimeter(kilonewtons_per_cubic_millimeter: float):
        """
        Create a new instance of SpecificWeight from a value in kilonewtons_per_cubic_millimeter.

        

        :param meters: The SpecificWeight value in kilonewtons_per_cubic_millimeter.
        :type kilonewtons_per_cubic_millimeter: float
        :return: A new instance of SpecificWeight.
        :rtype: SpecificWeight
        """
        return SpecificWeight(kilonewtons_per_cubic_millimeter, SpecificWeightUnits.KilonewtonPerCubicMillimeter)

    
    @staticmethod
    def from_kilonewtons_per_cubic_centimeter(kilonewtons_per_cubic_centimeter: float):
        """
        Create a new instance of SpecificWeight from a value in kilonewtons_per_cubic_centimeter.

        

        :param meters: The SpecificWeight value in kilonewtons_per_cubic_centimeter.
        :type kilonewtons_per_cubic_centimeter: float
        :return: A new instance of SpecificWeight.
        :rtype: SpecificWeight
        """
        return SpecificWeight(kilonewtons_per_cubic_centimeter, SpecificWeightUnits.KilonewtonPerCubicCentimeter)

    
    @staticmethod
    def from_kilonewtons_per_cubic_meter(kilonewtons_per_cubic_meter: float):
        """
        Create a new instance of SpecificWeight from a value in kilonewtons_per_cubic_meter.

        

        :param meters: The SpecificWeight value in kilonewtons_per_cubic_meter.
        :type kilonewtons_per_cubic_meter: float
        :return: A new instance of SpecificWeight.
        :rtype: SpecificWeight
        """
        return SpecificWeight(kilonewtons_per_cubic_meter, SpecificWeightUnits.KilonewtonPerCubicMeter)

    
    @staticmethod
    def from_meganewtons_per_cubic_meter(meganewtons_per_cubic_meter: float):
        """
        Create a new instance of SpecificWeight from a value in meganewtons_per_cubic_meter.

        

        :param meters: The SpecificWeight value in meganewtons_per_cubic_meter.
        :type meganewtons_per_cubic_meter: float
        :return: A new instance of SpecificWeight.
        :rtype: SpecificWeight
        """
        return SpecificWeight(meganewtons_per_cubic_meter, SpecificWeightUnits.MeganewtonPerCubicMeter)

    
    @staticmethod
    def from_kilopounds_force_per_cubic_inch(kilopounds_force_per_cubic_inch: float):
        """
        Create a new instance of SpecificWeight from a value in kilopounds_force_per_cubic_inch.

        

        :param meters: The SpecificWeight value in kilopounds_force_per_cubic_inch.
        :type kilopounds_force_per_cubic_inch: float
        :return: A new instance of SpecificWeight.
        :rtype: SpecificWeight
        """
        return SpecificWeight(kilopounds_force_per_cubic_inch, SpecificWeightUnits.KilopoundForcePerCubicInch)

    
    @staticmethod
    def from_kilopounds_force_per_cubic_foot(kilopounds_force_per_cubic_foot: float):
        """
        Create a new instance of SpecificWeight from a value in kilopounds_force_per_cubic_foot.

        

        :param meters: The SpecificWeight value in kilopounds_force_per_cubic_foot.
        :type kilopounds_force_per_cubic_foot: float
        :return: A new instance of SpecificWeight.
        :rtype: SpecificWeight
        """
        return SpecificWeight(kilopounds_force_per_cubic_foot, SpecificWeightUnits.KilopoundForcePerCubicFoot)

    
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
    def kilonewtons_per_cubic_millimeter(self) -> float:
        """
        
        """
        if self.__kilonewtons_per_cubic_millimeter != None:
            return self.__kilonewtons_per_cubic_millimeter
        self.__kilonewtons_per_cubic_millimeter = self.__convert_from_base(SpecificWeightUnits.KilonewtonPerCubicMillimeter)
        return self.__kilonewtons_per_cubic_millimeter

    
    @property
    def kilonewtons_per_cubic_centimeter(self) -> float:
        """
        
        """
        if self.__kilonewtons_per_cubic_centimeter != None:
            return self.__kilonewtons_per_cubic_centimeter
        self.__kilonewtons_per_cubic_centimeter = self.__convert_from_base(SpecificWeightUnits.KilonewtonPerCubicCentimeter)
        return self.__kilonewtons_per_cubic_centimeter

    
    @property
    def kilonewtons_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__kilonewtons_per_cubic_meter != None:
            return self.__kilonewtons_per_cubic_meter
        self.__kilonewtons_per_cubic_meter = self.__convert_from_base(SpecificWeightUnits.KilonewtonPerCubicMeter)
        return self.__kilonewtons_per_cubic_meter

    
    @property
    def meganewtons_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__meganewtons_per_cubic_meter != None:
            return self.__meganewtons_per_cubic_meter
        self.__meganewtons_per_cubic_meter = self.__convert_from_base(SpecificWeightUnits.MeganewtonPerCubicMeter)
        return self.__meganewtons_per_cubic_meter

    
    @property
    def kilopounds_force_per_cubic_inch(self) -> float:
        """
        
        """
        if self.__kilopounds_force_per_cubic_inch != None:
            return self.__kilopounds_force_per_cubic_inch
        self.__kilopounds_force_per_cubic_inch = self.__convert_from_base(SpecificWeightUnits.KilopoundForcePerCubicInch)
        return self.__kilopounds_force_per_cubic_inch

    
    @property
    def kilopounds_force_per_cubic_foot(self) -> float:
        """
        
        """
        if self.__kilopounds_force_per_cubic_foot != None:
            return self.__kilopounds_force_per_cubic_foot
        self.__kilopounds_force_per_cubic_foot = self.__convert_from_base(SpecificWeightUnits.KilopoundForcePerCubicFoot)
        return self.__kilopounds_force_per_cubic_foot

    
    def to_string(self, unit: SpecificWeightUnits = SpecificWeightUnits.NewtonPerCubicMeter, fractional_digits: int = None) -> str:
        """
        Format the SpecificWeight to a string.
        
        Note: the default format for SpecificWeight is NewtonPerCubicMeter.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the SpecificWeight. Default is 'NewtonPerCubicMeter'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == SpecificWeightUnits.NewtonPerCubicMillimeter:
            return f"""{super()._truncate_fraction_digits(self.newtons_per_cubic_millimeter, fractional_digits)} N/mm³"""
        
        if unit == SpecificWeightUnits.NewtonPerCubicCentimeter:
            return f"""{super()._truncate_fraction_digits(self.newtons_per_cubic_centimeter, fractional_digits)} N/cm³"""
        
        if unit == SpecificWeightUnits.NewtonPerCubicMeter:
            return f"""{super()._truncate_fraction_digits(self.newtons_per_cubic_meter, fractional_digits)} N/m³"""
        
        if unit == SpecificWeightUnits.KilogramForcePerCubicMillimeter:
            return f"""{super()._truncate_fraction_digits(self.kilograms_force_per_cubic_millimeter, fractional_digits)} kgf/mm³"""
        
        if unit == SpecificWeightUnits.KilogramForcePerCubicCentimeter:
            return f"""{super()._truncate_fraction_digits(self.kilograms_force_per_cubic_centimeter, fractional_digits)} kgf/cm³"""
        
        if unit == SpecificWeightUnits.KilogramForcePerCubicMeter:
            return f"""{super()._truncate_fraction_digits(self.kilograms_force_per_cubic_meter, fractional_digits)} kgf/m³"""
        
        if unit == SpecificWeightUnits.PoundForcePerCubicInch:
            return f"""{super()._truncate_fraction_digits(self.pounds_force_per_cubic_inch, fractional_digits)} lbf/in³"""
        
        if unit == SpecificWeightUnits.PoundForcePerCubicFoot:
            return f"""{super()._truncate_fraction_digits(self.pounds_force_per_cubic_foot, fractional_digits)} lbf/ft³"""
        
        if unit == SpecificWeightUnits.TonneForcePerCubicMillimeter:
            return f"""{super()._truncate_fraction_digits(self.tonnes_force_per_cubic_millimeter, fractional_digits)} tf/mm³"""
        
        if unit == SpecificWeightUnits.TonneForcePerCubicCentimeter:
            return f"""{super()._truncate_fraction_digits(self.tonnes_force_per_cubic_centimeter, fractional_digits)} tf/cm³"""
        
        if unit == SpecificWeightUnits.TonneForcePerCubicMeter:
            return f"""{super()._truncate_fraction_digits(self.tonnes_force_per_cubic_meter, fractional_digits)} tf/m³"""
        
        if unit == SpecificWeightUnits.KilonewtonPerCubicMillimeter:
            return f"""{super()._truncate_fraction_digits(self.kilonewtons_per_cubic_millimeter, fractional_digits)} kN/mm³"""
        
        if unit == SpecificWeightUnits.KilonewtonPerCubicCentimeter:
            return f"""{super()._truncate_fraction_digits(self.kilonewtons_per_cubic_centimeter, fractional_digits)} kN/cm³"""
        
        if unit == SpecificWeightUnits.KilonewtonPerCubicMeter:
            return f"""{super()._truncate_fraction_digits(self.kilonewtons_per_cubic_meter, fractional_digits)} kN/m³"""
        
        if unit == SpecificWeightUnits.MeganewtonPerCubicMeter:
            return f"""{super()._truncate_fraction_digits(self.meganewtons_per_cubic_meter, fractional_digits)} MN/m³"""
        
        if unit == SpecificWeightUnits.KilopoundForcePerCubicInch:
            return f"""{super()._truncate_fraction_digits(self.kilopounds_force_per_cubic_inch, fractional_digits)} klbf/in³"""
        
        if unit == SpecificWeightUnits.KilopoundForcePerCubicFoot:
            return f"""{super()._truncate_fraction_digits(self.kilopounds_force_per_cubic_foot, fractional_digits)} klbf/ft³"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: SpecificWeightUnits = SpecificWeightUnits.NewtonPerCubicMeter) -> str:
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
        
        if unit_abbreviation == SpecificWeightUnits.KilonewtonPerCubicMillimeter:
            return """kN/mm³"""
        
        if unit_abbreviation == SpecificWeightUnits.KilonewtonPerCubicCentimeter:
            return """kN/cm³"""
        
        if unit_abbreviation == SpecificWeightUnits.KilonewtonPerCubicMeter:
            return """kN/m³"""
        
        if unit_abbreviation == SpecificWeightUnits.MeganewtonPerCubicMeter:
            return """MN/m³"""
        
        if unit_abbreviation == SpecificWeightUnits.KilopoundForcePerCubicInch:
            return """klbf/in³"""
        
        if unit_abbreviation == SpecificWeightUnits.KilopoundForcePerCubicFoot:
            return """klbf/ft³"""
        
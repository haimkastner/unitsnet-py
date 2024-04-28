from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class ForcePerLengthUnits(Enum):
        """
            ForcePerLengthUnits enumeration
        """
        
        NewtonPerMeter = 'NewtonPerMeter'
        """
            
        """
        
        NewtonPerCentimeter = 'NewtonPerCentimeter'
        """
            
        """
        
        NewtonPerMillimeter = 'NewtonPerMillimeter'
        """
            
        """
        
        KilogramForcePerMeter = 'KilogramForcePerMeter'
        """
            
        """
        
        KilogramForcePerCentimeter = 'KilogramForcePerCentimeter'
        """
            
        """
        
        KilogramForcePerMillimeter = 'KilogramForcePerMillimeter'
        """
            
        """
        
        TonneForcePerMeter = 'TonneForcePerMeter'
        """
            
        """
        
        TonneForcePerCentimeter = 'TonneForcePerCentimeter'
        """
            
        """
        
        TonneForcePerMillimeter = 'TonneForcePerMillimeter'
        """
            
        """
        
        PoundForcePerFoot = 'PoundForcePerFoot'
        """
            
        """
        
        PoundForcePerInch = 'PoundForcePerInch'
        """
            
        """
        
        PoundForcePerYard = 'PoundForcePerYard'
        """
            
        """
        
        KilopoundForcePerFoot = 'KilopoundForcePerFoot'
        """
            
        """
        
        KilopoundForcePerInch = 'KilopoundForcePerInch'
        """
            
        """
        
        NanonewtonPerMeter = 'NanonewtonPerMeter'
        """
            
        """
        
        MicronewtonPerMeter = 'MicronewtonPerMeter'
        """
            
        """
        
        MillinewtonPerMeter = 'MillinewtonPerMeter'
        """
            
        """
        
        CentinewtonPerMeter = 'CentinewtonPerMeter'
        """
            
        """
        
        DecinewtonPerMeter = 'DecinewtonPerMeter'
        """
            
        """
        
        DecanewtonPerMeter = 'DecanewtonPerMeter'
        """
            
        """
        
        KilonewtonPerMeter = 'KilonewtonPerMeter'
        """
            
        """
        
        MeganewtonPerMeter = 'MeganewtonPerMeter'
        """
            
        """
        
        NanonewtonPerCentimeter = 'NanonewtonPerCentimeter'
        """
            
        """
        
        MicronewtonPerCentimeter = 'MicronewtonPerCentimeter'
        """
            
        """
        
        MillinewtonPerCentimeter = 'MillinewtonPerCentimeter'
        """
            
        """
        
        CentinewtonPerCentimeter = 'CentinewtonPerCentimeter'
        """
            
        """
        
        DecinewtonPerCentimeter = 'DecinewtonPerCentimeter'
        """
            
        """
        
        DecanewtonPerCentimeter = 'DecanewtonPerCentimeter'
        """
            
        """
        
        KilonewtonPerCentimeter = 'KilonewtonPerCentimeter'
        """
            
        """
        
        MeganewtonPerCentimeter = 'MeganewtonPerCentimeter'
        """
            
        """
        
        NanonewtonPerMillimeter = 'NanonewtonPerMillimeter'
        """
            
        """
        
        MicronewtonPerMillimeter = 'MicronewtonPerMillimeter'
        """
            
        """
        
        MillinewtonPerMillimeter = 'MillinewtonPerMillimeter'
        """
            
        """
        
        CentinewtonPerMillimeter = 'CentinewtonPerMillimeter'
        """
            
        """
        
        DecinewtonPerMillimeter = 'DecinewtonPerMillimeter'
        """
            
        """
        
        DecanewtonPerMillimeter = 'DecanewtonPerMillimeter'
        """
            
        """
        
        KilonewtonPerMillimeter = 'KilonewtonPerMillimeter'
        """
            
        """
        
        MeganewtonPerMillimeter = 'MeganewtonPerMillimeter'
        """
            
        """
        

class ForcePerLengthDto:
    """
    A DTO representation of a ForcePerLength

    Attributes:
        value (float): The value of the ForcePerLength.
        unit (ForcePerLengthUnits): The specific unit that the ForcePerLength value is representing.
    """

    def __init__(self, value: float, unit: ForcePerLengthUnits):
        """
        Create a new DTO representation of a ForcePerLength

        Parameters:
            value (float): The value of the ForcePerLength.
            unit (ForcePerLengthUnits): The specific unit that the ForcePerLength value is representing.
        """
        self.value: float = value
        """
        The value of the ForcePerLength
        """
        self.unit: ForcePerLengthUnits = unit
        """
        The specific unit that the ForcePerLength value is representing
        """

    def to_json(self):
        """
        Get a ForcePerLength DTO JSON object representing the current unit.

        :return: JSON object represents ForcePerLength DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "NewtonPerMeter"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of ForcePerLength DTO from a json representation.

        :param data: The ForcePerLength DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "NewtonPerMeter"}
        :return: A new instance of ForcePerLengthDto.
        :rtype: ForcePerLengthDto
        """
        return ForcePerLengthDto(value=data["value"], unit=ForcePerLengthUnits(data["unit"]))


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

    def to_dto(self, hold_in_unit: ForcePerLengthUnits = ForcePerLengthUnits.NewtonPerMeter) -> ForcePerLengthDto:
        """
        Get a new instance of ForcePerLength DTO representing the current unit.

        :param hold_in_unit: The specific ForcePerLength unit to store the ForcePerLength value in the DTO representation.
        :type hold_in_unit: ForcePerLengthUnits
        :return: A new instance of ForcePerLengthDto.
        :rtype: ForcePerLengthDto
        """
        return ForcePerLengthDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: ForcePerLengthUnits = ForcePerLengthUnits.NewtonPerMeter):
        """
        Get a ForcePerLength DTO JSON object representing the current unit.

        :param hold_in_unit: The specific ForcePerLength unit to store the ForcePerLength value in the DTO representation.
        :type hold_in_unit: ForcePerLengthUnits
        :return: JSON object represents ForcePerLength DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "NewtonPerMeter"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(force_per_length_dto: ForcePerLengthDto):
        """
        Obtain a new instance of ForcePerLength from a DTO unit object.

        :param force_per_length_dto: The ForcePerLength DTO representation.
        :type force_per_length_dto: ForcePerLengthDto
        :return: A new instance of ForcePerLength.
        :rtype: ForcePerLength
        """
        return ForcePerLength(force_per_length_dto.value, force_per_length_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of ForcePerLength from a DTO unit json representation.

        :param data: The ForcePerLength DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "NewtonPerMeter"}
        :return: A new instance of ForcePerLength.
        :rtype: ForcePerLength
        """
        return ForcePerLength.from_dto(ForcePerLengthDto.from_json(data))

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

    
    def to_string(self, unit: ForcePerLengthUnits = ForcePerLengthUnits.NewtonPerMeter, fractional_digits: int = None) -> str:
        """
        Format the ForcePerLength to a string.
        
        Note: the default format for ForcePerLength is NewtonPerMeter.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the ForcePerLength. Default is 'NewtonPerMeter'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == ForcePerLengthUnits.NewtonPerMeter:
            return f"""{super()._truncate_fraction_digits(self.newtons_per_meter, fractional_digits)} N/m"""
        
        if unit == ForcePerLengthUnits.NewtonPerCentimeter:
            return f"""{super()._truncate_fraction_digits(self.newtons_per_centimeter, fractional_digits)} N/cm"""
        
        if unit == ForcePerLengthUnits.NewtonPerMillimeter:
            return f"""{super()._truncate_fraction_digits(self.newtons_per_millimeter, fractional_digits)} N/mm"""
        
        if unit == ForcePerLengthUnits.KilogramForcePerMeter:
            return f"""{super()._truncate_fraction_digits(self.kilograms_force_per_meter, fractional_digits)} kgf/m"""
        
        if unit == ForcePerLengthUnits.KilogramForcePerCentimeter:
            return f"""{super()._truncate_fraction_digits(self.kilograms_force_per_centimeter, fractional_digits)} kgf/cm"""
        
        if unit == ForcePerLengthUnits.KilogramForcePerMillimeter:
            return f"""{super()._truncate_fraction_digits(self.kilograms_force_per_millimeter, fractional_digits)} kgf/mm"""
        
        if unit == ForcePerLengthUnits.TonneForcePerMeter:
            return f"""{super()._truncate_fraction_digits(self.tonnes_force_per_meter, fractional_digits)} tf/m"""
        
        if unit == ForcePerLengthUnits.TonneForcePerCentimeter:
            return f"""{super()._truncate_fraction_digits(self.tonnes_force_per_centimeter, fractional_digits)} tf/cm"""
        
        if unit == ForcePerLengthUnits.TonneForcePerMillimeter:
            return f"""{super()._truncate_fraction_digits(self.tonnes_force_per_millimeter, fractional_digits)} tf/mm"""
        
        if unit == ForcePerLengthUnits.PoundForcePerFoot:
            return f"""{super()._truncate_fraction_digits(self.pounds_force_per_foot, fractional_digits)} lbf/ft"""
        
        if unit == ForcePerLengthUnits.PoundForcePerInch:
            return f"""{super()._truncate_fraction_digits(self.pounds_force_per_inch, fractional_digits)} lbf/in"""
        
        if unit == ForcePerLengthUnits.PoundForcePerYard:
            return f"""{super()._truncate_fraction_digits(self.pounds_force_per_yard, fractional_digits)} lbf/yd"""
        
        if unit == ForcePerLengthUnits.KilopoundForcePerFoot:
            return f"""{super()._truncate_fraction_digits(self.kilopounds_force_per_foot, fractional_digits)} kipf/ft"""
        
        if unit == ForcePerLengthUnits.KilopoundForcePerInch:
            return f"""{super()._truncate_fraction_digits(self.kilopounds_force_per_inch, fractional_digits)} kipf/in"""
        
        if unit == ForcePerLengthUnits.NanonewtonPerMeter:
            return f"""{super()._truncate_fraction_digits(self.nanonewtons_per_meter, fractional_digits)} nN/m"""
        
        if unit == ForcePerLengthUnits.MicronewtonPerMeter:
            return f"""{super()._truncate_fraction_digits(self.micronewtons_per_meter, fractional_digits)} μN/m"""
        
        if unit == ForcePerLengthUnits.MillinewtonPerMeter:
            return f"""{super()._truncate_fraction_digits(self.millinewtons_per_meter, fractional_digits)} mN/m"""
        
        if unit == ForcePerLengthUnits.CentinewtonPerMeter:
            return f"""{super()._truncate_fraction_digits(self.centinewtons_per_meter, fractional_digits)} cN/m"""
        
        if unit == ForcePerLengthUnits.DecinewtonPerMeter:
            return f"""{super()._truncate_fraction_digits(self.decinewtons_per_meter, fractional_digits)} dN/m"""
        
        if unit == ForcePerLengthUnits.DecanewtonPerMeter:
            return f"""{super()._truncate_fraction_digits(self.decanewtons_per_meter, fractional_digits)} daN/m"""
        
        if unit == ForcePerLengthUnits.KilonewtonPerMeter:
            return f"""{super()._truncate_fraction_digits(self.kilonewtons_per_meter, fractional_digits)} kN/m"""
        
        if unit == ForcePerLengthUnits.MeganewtonPerMeter:
            return f"""{super()._truncate_fraction_digits(self.meganewtons_per_meter, fractional_digits)} MN/m"""
        
        if unit == ForcePerLengthUnits.NanonewtonPerCentimeter:
            return f"""{super()._truncate_fraction_digits(self.nanonewtons_per_centimeter, fractional_digits)} nN/cm"""
        
        if unit == ForcePerLengthUnits.MicronewtonPerCentimeter:
            return f"""{super()._truncate_fraction_digits(self.micronewtons_per_centimeter, fractional_digits)} μN/cm"""
        
        if unit == ForcePerLengthUnits.MillinewtonPerCentimeter:
            return f"""{super()._truncate_fraction_digits(self.millinewtons_per_centimeter, fractional_digits)} mN/cm"""
        
        if unit == ForcePerLengthUnits.CentinewtonPerCentimeter:
            return f"""{super()._truncate_fraction_digits(self.centinewtons_per_centimeter, fractional_digits)} cN/cm"""
        
        if unit == ForcePerLengthUnits.DecinewtonPerCentimeter:
            return f"""{super()._truncate_fraction_digits(self.decinewtons_per_centimeter, fractional_digits)} dN/cm"""
        
        if unit == ForcePerLengthUnits.DecanewtonPerCentimeter:
            return f"""{super()._truncate_fraction_digits(self.decanewtons_per_centimeter, fractional_digits)} daN/cm"""
        
        if unit == ForcePerLengthUnits.KilonewtonPerCentimeter:
            return f"""{super()._truncate_fraction_digits(self.kilonewtons_per_centimeter, fractional_digits)} kN/cm"""
        
        if unit == ForcePerLengthUnits.MeganewtonPerCentimeter:
            return f"""{super()._truncate_fraction_digits(self.meganewtons_per_centimeter, fractional_digits)} MN/cm"""
        
        if unit == ForcePerLengthUnits.NanonewtonPerMillimeter:
            return f"""{super()._truncate_fraction_digits(self.nanonewtons_per_millimeter, fractional_digits)} nN/mm"""
        
        if unit == ForcePerLengthUnits.MicronewtonPerMillimeter:
            return f"""{super()._truncate_fraction_digits(self.micronewtons_per_millimeter, fractional_digits)} μN/mm"""
        
        if unit == ForcePerLengthUnits.MillinewtonPerMillimeter:
            return f"""{super()._truncate_fraction_digits(self.millinewtons_per_millimeter, fractional_digits)} mN/mm"""
        
        if unit == ForcePerLengthUnits.CentinewtonPerMillimeter:
            return f"""{super()._truncate_fraction_digits(self.centinewtons_per_millimeter, fractional_digits)} cN/mm"""
        
        if unit == ForcePerLengthUnits.DecinewtonPerMillimeter:
            return f"""{super()._truncate_fraction_digits(self.decinewtons_per_millimeter, fractional_digits)} dN/mm"""
        
        if unit == ForcePerLengthUnits.DecanewtonPerMillimeter:
            return f"""{super()._truncate_fraction_digits(self.decanewtons_per_millimeter, fractional_digits)} daN/mm"""
        
        if unit == ForcePerLengthUnits.KilonewtonPerMillimeter:
            return f"""{super()._truncate_fraction_digits(self.kilonewtons_per_millimeter, fractional_digits)} kN/mm"""
        
        if unit == ForcePerLengthUnits.MeganewtonPerMillimeter:
            return f"""{super()._truncate_fraction_digits(self.meganewtons_per_millimeter, fractional_digits)} MN/mm"""
        
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
        
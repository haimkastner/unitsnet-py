from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class TorqueUnits(Enum):
        """
            TorqueUnits enumeration
        """
        
        NewtonMillimeter = 'NewtonMillimeter'
        """
            
        """
        
        NewtonCentimeter = 'NewtonCentimeter'
        """
            
        """
        
        NewtonMeter = 'NewtonMeter'
        """
            
        """
        
        PoundalFoot = 'PoundalFoot'
        """
            
        """
        
        PoundForceInch = 'PoundForceInch'
        """
            
        """
        
        PoundForceFoot = 'PoundForceFoot'
        """
            
        """
        
        GramForceMillimeter = 'GramForceMillimeter'
        """
            
        """
        
        GramForceCentimeter = 'GramForceCentimeter'
        """
            
        """
        
        GramForceMeter = 'GramForceMeter'
        """
            
        """
        
        KilogramForceMillimeter = 'KilogramForceMillimeter'
        """
            
        """
        
        KilogramForceCentimeter = 'KilogramForceCentimeter'
        """
            
        """
        
        KilogramForceMeter = 'KilogramForceMeter'
        """
            
        """
        
        TonneForceMillimeter = 'TonneForceMillimeter'
        """
            
        """
        
        TonneForceCentimeter = 'TonneForceCentimeter'
        """
            
        """
        
        TonneForceMeter = 'TonneForceMeter'
        """
            
        """
        
        KilonewtonMillimeter = 'KilonewtonMillimeter'
        """
            
        """
        
        MeganewtonMillimeter = 'MeganewtonMillimeter'
        """
            
        """
        
        KilonewtonCentimeter = 'KilonewtonCentimeter'
        """
            
        """
        
        MeganewtonCentimeter = 'MeganewtonCentimeter'
        """
            
        """
        
        KilonewtonMeter = 'KilonewtonMeter'
        """
            
        """
        
        MeganewtonMeter = 'MeganewtonMeter'
        """
            
        """
        
        KilopoundForceInch = 'KilopoundForceInch'
        """
            
        """
        
        MegapoundForceInch = 'MegapoundForceInch'
        """
            
        """
        
        KilopoundForceFoot = 'KilopoundForceFoot'
        """
            
        """
        
        MegapoundForceFoot = 'MegapoundForceFoot'
        """
            
        """
        

class TorqueDto:
    """
    A DTO representation of a Torque

    Attributes:
        value (float): The value of the Torque.
        unit (TorqueUnits): The specific unit that the Torque value is representing.
    """

    def __init__(self, value: float, unit: TorqueUnits):
        """
        Create a new DTO representation of a Torque

        Parameters:
            value (float): The value of the Torque.
            unit (TorqueUnits): The specific unit that the Torque value is representing.
        """
        self.value: float = value
        """
        The value of the Torque
        """
        self.unit: TorqueUnits = unit
        """
        The specific unit that the Torque value is representing
        """

    def to_json(self):
        """
        Get a Torque DTO JSON object representing the current unit.

        :return: JSON object represents Torque DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "NewtonMeter"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of Torque DTO from a json representation.

        :param data: The Torque DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "NewtonMeter"}
        :return: A new instance of TorqueDto.
        :rtype: TorqueDto
        """
        return TorqueDto(value=data["value"], unit=TorqueUnits(data["unit"]))


class Torque(AbstractMeasure):
    """
    Torque, moment or moment of force (see the terminology below), is the tendency of a force to rotate an object about an axis,[1] fulcrum, or pivot. Just as a force is a push or a pull, a torque can be thought of as a twist to an object. Mathematically, torque is defined as the cross product of the lever-arm distance and force, which tends to produce rotation. Loosely speaking, torque is a measure of the turning force on an object such as a bolt or a flywheel. For example, pushing or pulling the handle of a wrench connected to a nut or bolt produces a torque (turning force) that loosens or tightens the nut or bolt.

    Args:
        value (float): The value.
        from_unit (TorqueUnits): The Torque unit to create from, The default unit is NewtonMeter
    """
    def __init__(self, value: float, from_unit: TorqueUnits = TorqueUnits.NewtonMeter):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__newton_millimeters = None
        
        self.__newton_centimeters = None
        
        self.__newton_meters = None
        
        self.__poundal_feet = None
        
        self.__pound_force_inches = None
        
        self.__pound_force_feet = None
        
        self.__gram_force_millimeters = None
        
        self.__gram_force_centimeters = None
        
        self.__gram_force_meters = None
        
        self.__kilogram_force_millimeters = None
        
        self.__kilogram_force_centimeters = None
        
        self.__kilogram_force_meters = None
        
        self.__tonne_force_millimeters = None
        
        self.__tonne_force_centimeters = None
        
        self.__tonne_force_meters = None
        
        self.__kilonewton_millimeters = None
        
        self.__meganewton_millimeters = None
        
        self.__kilonewton_centimeters = None
        
        self.__meganewton_centimeters = None
        
        self.__kilonewton_meters = None
        
        self.__meganewton_meters = None
        
        self.__kilopound_force_inches = None
        
        self.__megapound_force_inches = None
        
        self.__kilopound_force_feet = None
        
        self.__megapound_force_feet = None
        

    def convert(self, unit: TorqueUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: TorqueUnits = TorqueUnits.NewtonMeter) -> TorqueDto:
        """
        Get a new instance of Torque DTO representing the current unit.

        :param hold_in_unit: The specific Torque unit to store the Torque value in the DTO representation.
        :type hold_in_unit: TorqueUnits
        :return: A new instance of TorqueDto.
        :rtype: TorqueDto
        """
        return TorqueDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: TorqueUnits = TorqueUnits.NewtonMeter):
        """
        Get a Torque DTO JSON object representing the current unit.

        :param hold_in_unit: The specific Torque unit to store the Torque value in the DTO representation.
        :type hold_in_unit: TorqueUnits
        :return: JSON object represents Torque DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "NewtonMeter"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(torque_dto: TorqueDto):
        """
        Obtain a new instance of Torque from a DTO unit object.

        :param torque_dto: The Torque DTO representation.
        :type torque_dto: TorqueDto
        :return: A new instance of Torque.
        :rtype: Torque
        """
        return Torque(torque_dto.value, torque_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of Torque from a DTO unit json representation.

        :param data: The Torque DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "NewtonMeter"}
        :return: A new instance of Torque.
        :rtype: Torque
        """
        return Torque.from_dto(TorqueDto.from_json(data))

    def __convert_from_base(self, from_unit: TorqueUnits) -> float:
        value = self._value
        
        if from_unit == TorqueUnits.NewtonMillimeter:
            return (value * 1000)
        
        if from_unit == TorqueUnits.NewtonCentimeter:
            return (value * 100)
        
        if from_unit == TorqueUnits.NewtonMeter:
            return (value)
        
        if from_unit == TorqueUnits.PoundalFoot:
            return (value / 4.21401100938048e-2)
        
        if from_unit == TorqueUnits.PoundForceInch:
            return (value / 1.129848290276167e-1)
        
        if from_unit == TorqueUnits.PoundForceFoot:
            return (value / 1.3558179483314)
        
        if from_unit == TorqueUnits.GramForceMillimeter:
            return (value / 9.80665e-6)
        
        if from_unit == TorqueUnits.GramForceCentimeter:
            return (value / 9.80665e-5)
        
        if from_unit == TorqueUnits.GramForceMeter:
            return (value / 9.80665e-3)
        
        if from_unit == TorqueUnits.KilogramForceMillimeter:
            return (value / 9.80665e-3)
        
        if from_unit == TorqueUnits.KilogramForceCentimeter:
            return (value / 9.80665e-2)
        
        if from_unit == TorqueUnits.KilogramForceMeter:
            return (value / 9.80665)
        
        if from_unit == TorqueUnits.TonneForceMillimeter:
            return (value / 9.80665)
        
        if from_unit == TorqueUnits.TonneForceCentimeter:
            return (value / 9.80665e1)
        
        if from_unit == TorqueUnits.TonneForceMeter:
            return (value / 9.80665e3)
        
        if from_unit == TorqueUnits.KilonewtonMillimeter:
            return ((value * 1000) / 1000.0)
        
        if from_unit == TorqueUnits.MeganewtonMillimeter:
            return ((value * 1000) / 1000000.0)
        
        if from_unit == TorqueUnits.KilonewtonCentimeter:
            return ((value * 100) / 1000.0)
        
        if from_unit == TorqueUnits.MeganewtonCentimeter:
            return ((value * 100) / 1000000.0)
        
        if from_unit == TorqueUnits.KilonewtonMeter:
            return ((value) / 1000.0)
        
        if from_unit == TorqueUnits.MeganewtonMeter:
            return ((value) / 1000000.0)
        
        if from_unit == TorqueUnits.KilopoundForceInch:
            return ((value / 1.129848290276167e-1) / 1000.0)
        
        if from_unit == TorqueUnits.MegapoundForceInch:
            return ((value / 1.129848290276167e-1) / 1000000.0)
        
        if from_unit == TorqueUnits.KilopoundForceFoot:
            return ((value / 1.3558179483314) / 1000.0)
        
        if from_unit == TorqueUnits.MegapoundForceFoot:
            return ((value / 1.3558179483314) / 1000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: TorqueUnits) -> float:
        
        if to_unit == TorqueUnits.NewtonMillimeter:
            return (value * 0.001)
        
        if to_unit == TorqueUnits.NewtonCentimeter:
            return (value * 0.01)
        
        if to_unit == TorqueUnits.NewtonMeter:
            return (value)
        
        if to_unit == TorqueUnits.PoundalFoot:
            return (value * 4.21401100938048e-2)
        
        if to_unit == TorqueUnits.PoundForceInch:
            return (value * 1.129848290276167e-1)
        
        if to_unit == TorqueUnits.PoundForceFoot:
            return (value * 1.3558179483314)
        
        if to_unit == TorqueUnits.GramForceMillimeter:
            return (value * 9.80665e-6)
        
        if to_unit == TorqueUnits.GramForceCentimeter:
            return (value * 9.80665e-5)
        
        if to_unit == TorqueUnits.GramForceMeter:
            return (value * 9.80665e-3)
        
        if to_unit == TorqueUnits.KilogramForceMillimeter:
            return (value * 9.80665e-3)
        
        if to_unit == TorqueUnits.KilogramForceCentimeter:
            return (value * 9.80665e-2)
        
        if to_unit == TorqueUnits.KilogramForceMeter:
            return (value * 9.80665)
        
        if to_unit == TorqueUnits.TonneForceMillimeter:
            return (value * 9.80665)
        
        if to_unit == TorqueUnits.TonneForceCentimeter:
            return (value * 9.80665e1)
        
        if to_unit == TorqueUnits.TonneForceMeter:
            return (value * 9.80665e3)
        
        if to_unit == TorqueUnits.KilonewtonMillimeter:
            return ((value * 0.001) * 1000.0)
        
        if to_unit == TorqueUnits.MeganewtonMillimeter:
            return ((value * 0.001) * 1000000.0)
        
        if to_unit == TorqueUnits.KilonewtonCentimeter:
            return ((value * 0.01) * 1000.0)
        
        if to_unit == TorqueUnits.MeganewtonCentimeter:
            return ((value * 0.01) * 1000000.0)
        
        if to_unit == TorqueUnits.KilonewtonMeter:
            return ((value) * 1000.0)
        
        if to_unit == TorqueUnits.MeganewtonMeter:
            return ((value) * 1000000.0)
        
        if to_unit == TorqueUnits.KilopoundForceInch:
            return ((value * 1.129848290276167e-1) * 1000.0)
        
        if to_unit == TorqueUnits.MegapoundForceInch:
            return ((value * 1.129848290276167e-1) * 1000000.0)
        
        if to_unit == TorqueUnits.KilopoundForceFoot:
            return ((value * 1.3558179483314) * 1000.0)
        
        if to_unit == TorqueUnits.MegapoundForceFoot:
            return ((value * 1.3558179483314) * 1000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_newton_millimeters(newton_millimeters: float):
        """
        Create a new instance of Torque from a value in newton_millimeters.

        

        :param meters: The Torque value in newton_millimeters.
        :type newton_millimeters: float
        :return: A new instance of Torque.
        :rtype: Torque
        """
        return Torque(newton_millimeters, TorqueUnits.NewtonMillimeter)

    
    @staticmethod
    def from_newton_centimeters(newton_centimeters: float):
        """
        Create a new instance of Torque from a value in newton_centimeters.

        

        :param meters: The Torque value in newton_centimeters.
        :type newton_centimeters: float
        :return: A new instance of Torque.
        :rtype: Torque
        """
        return Torque(newton_centimeters, TorqueUnits.NewtonCentimeter)

    
    @staticmethod
    def from_newton_meters(newton_meters: float):
        """
        Create a new instance of Torque from a value in newton_meters.

        

        :param meters: The Torque value in newton_meters.
        :type newton_meters: float
        :return: A new instance of Torque.
        :rtype: Torque
        """
        return Torque(newton_meters, TorqueUnits.NewtonMeter)

    
    @staticmethod
    def from_poundal_feet(poundal_feet: float):
        """
        Create a new instance of Torque from a value in poundal_feet.

        

        :param meters: The Torque value in poundal_feet.
        :type poundal_feet: float
        :return: A new instance of Torque.
        :rtype: Torque
        """
        return Torque(poundal_feet, TorqueUnits.PoundalFoot)

    
    @staticmethod
    def from_pound_force_inches(pound_force_inches: float):
        """
        Create a new instance of Torque from a value in pound_force_inches.

        

        :param meters: The Torque value in pound_force_inches.
        :type pound_force_inches: float
        :return: A new instance of Torque.
        :rtype: Torque
        """
        return Torque(pound_force_inches, TorqueUnits.PoundForceInch)

    
    @staticmethod
    def from_pound_force_feet(pound_force_feet: float):
        """
        Create a new instance of Torque from a value in pound_force_feet.

        

        :param meters: The Torque value in pound_force_feet.
        :type pound_force_feet: float
        :return: A new instance of Torque.
        :rtype: Torque
        """
        return Torque(pound_force_feet, TorqueUnits.PoundForceFoot)

    
    @staticmethod
    def from_gram_force_millimeters(gram_force_millimeters: float):
        """
        Create a new instance of Torque from a value in gram_force_millimeters.

        

        :param meters: The Torque value in gram_force_millimeters.
        :type gram_force_millimeters: float
        :return: A new instance of Torque.
        :rtype: Torque
        """
        return Torque(gram_force_millimeters, TorqueUnits.GramForceMillimeter)

    
    @staticmethod
    def from_gram_force_centimeters(gram_force_centimeters: float):
        """
        Create a new instance of Torque from a value in gram_force_centimeters.

        

        :param meters: The Torque value in gram_force_centimeters.
        :type gram_force_centimeters: float
        :return: A new instance of Torque.
        :rtype: Torque
        """
        return Torque(gram_force_centimeters, TorqueUnits.GramForceCentimeter)

    
    @staticmethod
    def from_gram_force_meters(gram_force_meters: float):
        """
        Create a new instance of Torque from a value in gram_force_meters.

        

        :param meters: The Torque value in gram_force_meters.
        :type gram_force_meters: float
        :return: A new instance of Torque.
        :rtype: Torque
        """
        return Torque(gram_force_meters, TorqueUnits.GramForceMeter)

    
    @staticmethod
    def from_kilogram_force_millimeters(kilogram_force_millimeters: float):
        """
        Create a new instance of Torque from a value in kilogram_force_millimeters.

        

        :param meters: The Torque value in kilogram_force_millimeters.
        :type kilogram_force_millimeters: float
        :return: A new instance of Torque.
        :rtype: Torque
        """
        return Torque(kilogram_force_millimeters, TorqueUnits.KilogramForceMillimeter)

    
    @staticmethod
    def from_kilogram_force_centimeters(kilogram_force_centimeters: float):
        """
        Create a new instance of Torque from a value in kilogram_force_centimeters.

        

        :param meters: The Torque value in kilogram_force_centimeters.
        :type kilogram_force_centimeters: float
        :return: A new instance of Torque.
        :rtype: Torque
        """
        return Torque(kilogram_force_centimeters, TorqueUnits.KilogramForceCentimeter)

    
    @staticmethod
    def from_kilogram_force_meters(kilogram_force_meters: float):
        """
        Create a new instance of Torque from a value in kilogram_force_meters.

        

        :param meters: The Torque value in kilogram_force_meters.
        :type kilogram_force_meters: float
        :return: A new instance of Torque.
        :rtype: Torque
        """
        return Torque(kilogram_force_meters, TorqueUnits.KilogramForceMeter)

    
    @staticmethod
    def from_tonne_force_millimeters(tonne_force_millimeters: float):
        """
        Create a new instance of Torque from a value in tonne_force_millimeters.

        

        :param meters: The Torque value in tonne_force_millimeters.
        :type tonne_force_millimeters: float
        :return: A new instance of Torque.
        :rtype: Torque
        """
        return Torque(tonne_force_millimeters, TorqueUnits.TonneForceMillimeter)

    
    @staticmethod
    def from_tonne_force_centimeters(tonne_force_centimeters: float):
        """
        Create a new instance of Torque from a value in tonne_force_centimeters.

        

        :param meters: The Torque value in tonne_force_centimeters.
        :type tonne_force_centimeters: float
        :return: A new instance of Torque.
        :rtype: Torque
        """
        return Torque(tonne_force_centimeters, TorqueUnits.TonneForceCentimeter)

    
    @staticmethod
    def from_tonne_force_meters(tonne_force_meters: float):
        """
        Create a new instance of Torque from a value in tonne_force_meters.

        

        :param meters: The Torque value in tonne_force_meters.
        :type tonne_force_meters: float
        :return: A new instance of Torque.
        :rtype: Torque
        """
        return Torque(tonne_force_meters, TorqueUnits.TonneForceMeter)

    
    @staticmethod
    def from_kilonewton_millimeters(kilonewton_millimeters: float):
        """
        Create a new instance of Torque from a value in kilonewton_millimeters.

        

        :param meters: The Torque value in kilonewton_millimeters.
        :type kilonewton_millimeters: float
        :return: A new instance of Torque.
        :rtype: Torque
        """
        return Torque(kilonewton_millimeters, TorqueUnits.KilonewtonMillimeter)

    
    @staticmethod
    def from_meganewton_millimeters(meganewton_millimeters: float):
        """
        Create a new instance of Torque from a value in meganewton_millimeters.

        

        :param meters: The Torque value in meganewton_millimeters.
        :type meganewton_millimeters: float
        :return: A new instance of Torque.
        :rtype: Torque
        """
        return Torque(meganewton_millimeters, TorqueUnits.MeganewtonMillimeter)

    
    @staticmethod
    def from_kilonewton_centimeters(kilonewton_centimeters: float):
        """
        Create a new instance of Torque from a value in kilonewton_centimeters.

        

        :param meters: The Torque value in kilonewton_centimeters.
        :type kilonewton_centimeters: float
        :return: A new instance of Torque.
        :rtype: Torque
        """
        return Torque(kilonewton_centimeters, TorqueUnits.KilonewtonCentimeter)

    
    @staticmethod
    def from_meganewton_centimeters(meganewton_centimeters: float):
        """
        Create a new instance of Torque from a value in meganewton_centimeters.

        

        :param meters: The Torque value in meganewton_centimeters.
        :type meganewton_centimeters: float
        :return: A new instance of Torque.
        :rtype: Torque
        """
        return Torque(meganewton_centimeters, TorqueUnits.MeganewtonCentimeter)

    
    @staticmethod
    def from_kilonewton_meters(kilonewton_meters: float):
        """
        Create a new instance of Torque from a value in kilonewton_meters.

        

        :param meters: The Torque value in kilonewton_meters.
        :type kilonewton_meters: float
        :return: A new instance of Torque.
        :rtype: Torque
        """
        return Torque(kilonewton_meters, TorqueUnits.KilonewtonMeter)

    
    @staticmethod
    def from_meganewton_meters(meganewton_meters: float):
        """
        Create a new instance of Torque from a value in meganewton_meters.

        

        :param meters: The Torque value in meganewton_meters.
        :type meganewton_meters: float
        :return: A new instance of Torque.
        :rtype: Torque
        """
        return Torque(meganewton_meters, TorqueUnits.MeganewtonMeter)

    
    @staticmethod
    def from_kilopound_force_inches(kilopound_force_inches: float):
        """
        Create a new instance of Torque from a value in kilopound_force_inches.

        

        :param meters: The Torque value in kilopound_force_inches.
        :type kilopound_force_inches: float
        :return: A new instance of Torque.
        :rtype: Torque
        """
        return Torque(kilopound_force_inches, TorqueUnits.KilopoundForceInch)

    
    @staticmethod
    def from_megapound_force_inches(megapound_force_inches: float):
        """
        Create a new instance of Torque from a value in megapound_force_inches.

        

        :param meters: The Torque value in megapound_force_inches.
        :type megapound_force_inches: float
        :return: A new instance of Torque.
        :rtype: Torque
        """
        return Torque(megapound_force_inches, TorqueUnits.MegapoundForceInch)

    
    @staticmethod
    def from_kilopound_force_feet(kilopound_force_feet: float):
        """
        Create a new instance of Torque from a value in kilopound_force_feet.

        

        :param meters: The Torque value in kilopound_force_feet.
        :type kilopound_force_feet: float
        :return: A new instance of Torque.
        :rtype: Torque
        """
        return Torque(kilopound_force_feet, TorqueUnits.KilopoundForceFoot)

    
    @staticmethod
    def from_megapound_force_feet(megapound_force_feet: float):
        """
        Create a new instance of Torque from a value in megapound_force_feet.

        

        :param meters: The Torque value in megapound_force_feet.
        :type megapound_force_feet: float
        :return: A new instance of Torque.
        :rtype: Torque
        """
        return Torque(megapound_force_feet, TorqueUnits.MegapoundForceFoot)

    
    @property
    def newton_millimeters(self) -> float:
        """
        
        """
        if self.__newton_millimeters != None:
            return self.__newton_millimeters
        self.__newton_millimeters = self.__convert_from_base(TorqueUnits.NewtonMillimeter)
        return self.__newton_millimeters

    
    @property
    def newton_centimeters(self) -> float:
        """
        
        """
        if self.__newton_centimeters != None:
            return self.__newton_centimeters
        self.__newton_centimeters = self.__convert_from_base(TorqueUnits.NewtonCentimeter)
        return self.__newton_centimeters

    
    @property
    def newton_meters(self) -> float:
        """
        
        """
        if self.__newton_meters != None:
            return self.__newton_meters
        self.__newton_meters = self.__convert_from_base(TorqueUnits.NewtonMeter)
        return self.__newton_meters

    
    @property
    def poundal_feet(self) -> float:
        """
        
        """
        if self.__poundal_feet != None:
            return self.__poundal_feet
        self.__poundal_feet = self.__convert_from_base(TorqueUnits.PoundalFoot)
        return self.__poundal_feet

    
    @property
    def pound_force_inches(self) -> float:
        """
        
        """
        if self.__pound_force_inches != None:
            return self.__pound_force_inches
        self.__pound_force_inches = self.__convert_from_base(TorqueUnits.PoundForceInch)
        return self.__pound_force_inches

    
    @property
    def pound_force_feet(self) -> float:
        """
        
        """
        if self.__pound_force_feet != None:
            return self.__pound_force_feet
        self.__pound_force_feet = self.__convert_from_base(TorqueUnits.PoundForceFoot)
        return self.__pound_force_feet

    
    @property
    def gram_force_millimeters(self) -> float:
        """
        
        """
        if self.__gram_force_millimeters != None:
            return self.__gram_force_millimeters
        self.__gram_force_millimeters = self.__convert_from_base(TorqueUnits.GramForceMillimeter)
        return self.__gram_force_millimeters

    
    @property
    def gram_force_centimeters(self) -> float:
        """
        
        """
        if self.__gram_force_centimeters != None:
            return self.__gram_force_centimeters
        self.__gram_force_centimeters = self.__convert_from_base(TorqueUnits.GramForceCentimeter)
        return self.__gram_force_centimeters

    
    @property
    def gram_force_meters(self) -> float:
        """
        
        """
        if self.__gram_force_meters != None:
            return self.__gram_force_meters
        self.__gram_force_meters = self.__convert_from_base(TorqueUnits.GramForceMeter)
        return self.__gram_force_meters

    
    @property
    def kilogram_force_millimeters(self) -> float:
        """
        
        """
        if self.__kilogram_force_millimeters != None:
            return self.__kilogram_force_millimeters
        self.__kilogram_force_millimeters = self.__convert_from_base(TorqueUnits.KilogramForceMillimeter)
        return self.__kilogram_force_millimeters

    
    @property
    def kilogram_force_centimeters(self) -> float:
        """
        
        """
        if self.__kilogram_force_centimeters != None:
            return self.__kilogram_force_centimeters
        self.__kilogram_force_centimeters = self.__convert_from_base(TorqueUnits.KilogramForceCentimeter)
        return self.__kilogram_force_centimeters

    
    @property
    def kilogram_force_meters(self) -> float:
        """
        
        """
        if self.__kilogram_force_meters != None:
            return self.__kilogram_force_meters
        self.__kilogram_force_meters = self.__convert_from_base(TorqueUnits.KilogramForceMeter)
        return self.__kilogram_force_meters

    
    @property
    def tonne_force_millimeters(self) -> float:
        """
        
        """
        if self.__tonne_force_millimeters != None:
            return self.__tonne_force_millimeters
        self.__tonne_force_millimeters = self.__convert_from_base(TorqueUnits.TonneForceMillimeter)
        return self.__tonne_force_millimeters

    
    @property
    def tonne_force_centimeters(self) -> float:
        """
        
        """
        if self.__tonne_force_centimeters != None:
            return self.__tonne_force_centimeters
        self.__tonne_force_centimeters = self.__convert_from_base(TorqueUnits.TonneForceCentimeter)
        return self.__tonne_force_centimeters

    
    @property
    def tonne_force_meters(self) -> float:
        """
        
        """
        if self.__tonne_force_meters != None:
            return self.__tonne_force_meters
        self.__tonne_force_meters = self.__convert_from_base(TorqueUnits.TonneForceMeter)
        return self.__tonne_force_meters

    
    @property
    def kilonewton_millimeters(self) -> float:
        """
        
        """
        if self.__kilonewton_millimeters != None:
            return self.__kilonewton_millimeters
        self.__kilonewton_millimeters = self.__convert_from_base(TorqueUnits.KilonewtonMillimeter)
        return self.__kilonewton_millimeters

    
    @property
    def meganewton_millimeters(self) -> float:
        """
        
        """
        if self.__meganewton_millimeters != None:
            return self.__meganewton_millimeters
        self.__meganewton_millimeters = self.__convert_from_base(TorqueUnits.MeganewtonMillimeter)
        return self.__meganewton_millimeters

    
    @property
    def kilonewton_centimeters(self) -> float:
        """
        
        """
        if self.__kilonewton_centimeters != None:
            return self.__kilonewton_centimeters
        self.__kilonewton_centimeters = self.__convert_from_base(TorqueUnits.KilonewtonCentimeter)
        return self.__kilonewton_centimeters

    
    @property
    def meganewton_centimeters(self) -> float:
        """
        
        """
        if self.__meganewton_centimeters != None:
            return self.__meganewton_centimeters
        self.__meganewton_centimeters = self.__convert_from_base(TorqueUnits.MeganewtonCentimeter)
        return self.__meganewton_centimeters

    
    @property
    def kilonewton_meters(self) -> float:
        """
        
        """
        if self.__kilonewton_meters != None:
            return self.__kilonewton_meters
        self.__kilonewton_meters = self.__convert_from_base(TorqueUnits.KilonewtonMeter)
        return self.__kilonewton_meters

    
    @property
    def meganewton_meters(self) -> float:
        """
        
        """
        if self.__meganewton_meters != None:
            return self.__meganewton_meters
        self.__meganewton_meters = self.__convert_from_base(TorqueUnits.MeganewtonMeter)
        return self.__meganewton_meters

    
    @property
    def kilopound_force_inches(self) -> float:
        """
        
        """
        if self.__kilopound_force_inches != None:
            return self.__kilopound_force_inches
        self.__kilopound_force_inches = self.__convert_from_base(TorqueUnits.KilopoundForceInch)
        return self.__kilopound_force_inches

    
    @property
    def megapound_force_inches(self) -> float:
        """
        
        """
        if self.__megapound_force_inches != None:
            return self.__megapound_force_inches
        self.__megapound_force_inches = self.__convert_from_base(TorqueUnits.MegapoundForceInch)
        return self.__megapound_force_inches

    
    @property
    def kilopound_force_feet(self) -> float:
        """
        
        """
        if self.__kilopound_force_feet != None:
            return self.__kilopound_force_feet
        self.__kilopound_force_feet = self.__convert_from_base(TorqueUnits.KilopoundForceFoot)
        return self.__kilopound_force_feet

    
    @property
    def megapound_force_feet(self) -> float:
        """
        
        """
        if self.__megapound_force_feet != None:
            return self.__megapound_force_feet
        self.__megapound_force_feet = self.__convert_from_base(TorqueUnits.MegapoundForceFoot)
        return self.__megapound_force_feet

    
    def to_string(self, unit: TorqueUnits = TorqueUnits.NewtonMeter, fractional_digits: int = None) -> str:
        """
        Format the Torque to a string.
        
        Note: the default format for Torque is NewtonMeter.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the Torque. Default is 'NewtonMeter'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == TorqueUnits.NewtonMillimeter:
            return f"""{super()._truncate_fraction_digits(self.newton_millimeters, fractional_digits)} N·mm"""
        
        if unit == TorqueUnits.NewtonCentimeter:
            return f"""{super()._truncate_fraction_digits(self.newton_centimeters, fractional_digits)} N·cm"""
        
        if unit == TorqueUnits.NewtonMeter:
            return f"""{super()._truncate_fraction_digits(self.newton_meters, fractional_digits)} N·m"""
        
        if unit == TorqueUnits.PoundalFoot:
            return f"""{super()._truncate_fraction_digits(self.poundal_feet, fractional_digits)} pdl·ft"""
        
        if unit == TorqueUnits.PoundForceInch:
            return f"""{super()._truncate_fraction_digits(self.pound_force_inches, fractional_digits)} lbf·in"""
        
        if unit == TorqueUnits.PoundForceFoot:
            return f"""{super()._truncate_fraction_digits(self.pound_force_feet, fractional_digits)} lbf·ft"""
        
        if unit == TorqueUnits.GramForceMillimeter:
            return f"""{super()._truncate_fraction_digits(self.gram_force_millimeters, fractional_digits)} gf·mm"""
        
        if unit == TorqueUnits.GramForceCentimeter:
            return f"""{super()._truncate_fraction_digits(self.gram_force_centimeters, fractional_digits)} gf·cm"""
        
        if unit == TorqueUnits.GramForceMeter:
            return f"""{super()._truncate_fraction_digits(self.gram_force_meters, fractional_digits)} gf·m"""
        
        if unit == TorqueUnits.KilogramForceMillimeter:
            return f"""{super()._truncate_fraction_digits(self.kilogram_force_millimeters, fractional_digits)} kgf·mm"""
        
        if unit == TorqueUnits.KilogramForceCentimeter:
            return f"""{super()._truncate_fraction_digits(self.kilogram_force_centimeters, fractional_digits)} kgf·cm"""
        
        if unit == TorqueUnits.KilogramForceMeter:
            return f"""{super()._truncate_fraction_digits(self.kilogram_force_meters, fractional_digits)} kgf·m"""
        
        if unit == TorqueUnits.TonneForceMillimeter:
            return f"""{super()._truncate_fraction_digits(self.tonne_force_millimeters, fractional_digits)} tf·mm"""
        
        if unit == TorqueUnits.TonneForceCentimeter:
            return f"""{super()._truncate_fraction_digits(self.tonne_force_centimeters, fractional_digits)} tf·cm"""
        
        if unit == TorqueUnits.TonneForceMeter:
            return f"""{super()._truncate_fraction_digits(self.tonne_force_meters, fractional_digits)} tf·m"""
        
        if unit == TorqueUnits.KilonewtonMillimeter:
            return f"""{super()._truncate_fraction_digits(self.kilonewton_millimeters, fractional_digits)} kN·mm"""
        
        if unit == TorqueUnits.MeganewtonMillimeter:
            return f"""{super()._truncate_fraction_digits(self.meganewton_millimeters, fractional_digits)} MN·mm"""
        
        if unit == TorqueUnits.KilonewtonCentimeter:
            return f"""{super()._truncate_fraction_digits(self.kilonewton_centimeters, fractional_digits)} kN·cm"""
        
        if unit == TorqueUnits.MeganewtonCentimeter:
            return f"""{super()._truncate_fraction_digits(self.meganewton_centimeters, fractional_digits)} MN·cm"""
        
        if unit == TorqueUnits.KilonewtonMeter:
            return f"""{super()._truncate_fraction_digits(self.kilonewton_meters, fractional_digits)} kN·m"""
        
        if unit == TorqueUnits.MeganewtonMeter:
            return f"""{super()._truncate_fraction_digits(self.meganewton_meters, fractional_digits)} MN·m"""
        
        if unit == TorqueUnits.KilopoundForceInch:
            return f"""{super()._truncate_fraction_digits(self.kilopound_force_inches, fractional_digits)} klbf·in"""
        
        if unit == TorqueUnits.MegapoundForceInch:
            return f"""{super()._truncate_fraction_digits(self.megapound_force_inches, fractional_digits)} Mlbf·in"""
        
        if unit == TorqueUnits.KilopoundForceFoot:
            return f"""{super()._truncate_fraction_digits(self.kilopound_force_feet, fractional_digits)} klbf·ft"""
        
        if unit == TorqueUnits.MegapoundForceFoot:
            return f"""{super()._truncate_fraction_digits(self.megapound_force_feet, fractional_digits)} Mlbf·ft"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: TorqueUnits = TorqueUnits.NewtonMeter) -> str:
        """
        Get Torque unit abbreviation.
        Note! the default abbreviation for Torque is NewtonMeter.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == TorqueUnits.NewtonMillimeter:
            return """N·mm"""
        
        if unit_abbreviation == TorqueUnits.NewtonCentimeter:
            return """N·cm"""
        
        if unit_abbreviation == TorqueUnits.NewtonMeter:
            return """N·m"""
        
        if unit_abbreviation == TorqueUnits.PoundalFoot:
            return """pdl·ft"""
        
        if unit_abbreviation == TorqueUnits.PoundForceInch:
            return """lbf·in"""
        
        if unit_abbreviation == TorqueUnits.PoundForceFoot:
            return """lbf·ft"""
        
        if unit_abbreviation == TorqueUnits.GramForceMillimeter:
            return """gf·mm"""
        
        if unit_abbreviation == TorqueUnits.GramForceCentimeter:
            return """gf·cm"""
        
        if unit_abbreviation == TorqueUnits.GramForceMeter:
            return """gf·m"""
        
        if unit_abbreviation == TorqueUnits.KilogramForceMillimeter:
            return """kgf·mm"""
        
        if unit_abbreviation == TorqueUnits.KilogramForceCentimeter:
            return """kgf·cm"""
        
        if unit_abbreviation == TorqueUnits.KilogramForceMeter:
            return """kgf·m"""
        
        if unit_abbreviation == TorqueUnits.TonneForceMillimeter:
            return """tf·mm"""
        
        if unit_abbreviation == TorqueUnits.TonneForceCentimeter:
            return """tf·cm"""
        
        if unit_abbreviation == TorqueUnits.TonneForceMeter:
            return """tf·m"""
        
        if unit_abbreviation == TorqueUnits.KilonewtonMillimeter:
            return """kN·mm"""
        
        if unit_abbreviation == TorqueUnits.MeganewtonMillimeter:
            return """MN·mm"""
        
        if unit_abbreviation == TorqueUnits.KilonewtonCentimeter:
            return """kN·cm"""
        
        if unit_abbreviation == TorqueUnits.MeganewtonCentimeter:
            return """MN·cm"""
        
        if unit_abbreviation == TorqueUnits.KilonewtonMeter:
            return """kN·m"""
        
        if unit_abbreviation == TorqueUnits.MeganewtonMeter:
            return """MN·m"""
        
        if unit_abbreviation == TorqueUnits.KilopoundForceInch:
            return """klbf·in"""
        
        if unit_abbreviation == TorqueUnits.MegapoundForceInch:
            return """Mlbf·in"""
        
        if unit_abbreviation == TorqueUnits.KilopoundForceFoot:
            return """klbf·ft"""
        
        if unit_abbreviation == TorqueUnits.MegapoundForceFoot:
            return """Mlbf·ft"""
        
from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class MassMomentOfInertiaUnits(Enum):
        """
            MassMomentOfInertiaUnits enumeration
        """
        
        GramSquareMeter = 'GramSquareMeter'
        """
            
        """
        
        GramSquareDecimeter = 'GramSquareDecimeter'
        """
            
        """
        
        GramSquareCentimeter = 'GramSquareCentimeter'
        """
            
        """
        
        GramSquareMillimeter = 'GramSquareMillimeter'
        """
            
        """
        
        TonneSquareMeter = 'TonneSquareMeter'
        """
            
        """
        
        TonneSquareDecimeter = 'TonneSquareDecimeter'
        """
            
        """
        
        TonneSquareCentimeter = 'TonneSquareCentimeter'
        """
            
        """
        
        TonneSquareMilimeter = 'TonneSquareMilimeter'
        """
            
        """
        
        PoundSquareFoot = 'PoundSquareFoot'
        """
            
        """
        
        PoundSquareInch = 'PoundSquareInch'
        """
            
        """
        
        SlugSquareFoot = 'SlugSquareFoot'
        """
            
        """
        
        SlugSquareInch = 'SlugSquareInch'
        """
            
        """
        
        MilligramSquareMeter = 'MilligramSquareMeter'
        """
            
        """
        
        KilogramSquareMeter = 'KilogramSquareMeter'
        """
            
        """
        
        MilligramSquareDecimeter = 'MilligramSquareDecimeter'
        """
            
        """
        
        KilogramSquareDecimeter = 'KilogramSquareDecimeter'
        """
            
        """
        
        MilligramSquareCentimeter = 'MilligramSquareCentimeter'
        """
            
        """
        
        KilogramSquareCentimeter = 'KilogramSquareCentimeter'
        """
            
        """
        
        MilligramSquareMillimeter = 'MilligramSquareMillimeter'
        """
            
        """
        
        KilogramSquareMillimeter = 'KilogramSquareMillimeter'
        """
            
        """
        
        KilotonneSquareMeter = 'KilotonneSquareMeter'
        """
            
        """
        
        MegatonneSquareMeter = 'MegatonneSquareMeter'
        """
            
        """
        
        KilotonneSquareDecimeter = 'KilotonneSquareDecimeter'
        """
            
        """
        
        MegatonneSquareDecimeter = 'MegatonneSquareDecimeter'
        """
            
        """
        
        KilotonneSquareCentimeter = 'KilotonneSquareCentimeter'
        """
            
        """
        
        MegatonneSquareCentimeter = 'MegatonneSquareCentimeter'
        """
            
        """
        
        KilotonneSquareMilimeter = 'KilotonneSquareMilimeter'
        """
            
        """
        
        MegatonneSquareMilimeter = 'MegatonneSquareMilimeter'
        """
            
        """
        

class MassMomentOfInertiaDto:
    """
    A DTO representation of a MassMomentOfInertia

    Attributes:
        value (float): The value of the MassMomentOfInertia.
        unit (MassMomentOfInertiaUnits): The specific unit that the MassMomentOfInertia value is representing.
    """

    def __init__(self, value: float, unit: MassMomentOfInertiaUnits):
        """
        Create a new DTO representation of a MassMomentOfInertia

        Parameters:
            value (float): The value of the MassMomentOfInertia.
            unit (MassMomentOfInertiaUnits): The specific unit that the MassMomentOfInertia value is representing.
        """
        self.value: float = value
        """
        The value of the MassMomentOfInertia
        """
        self.unit: MassMomentOfInertiaUnits = unit
        """
        The specific unit that the MassMomentOfInertia value is representing
        """

    def to_json(self):
        """
        Get a MassMomentOfInertia DTO JSON object representing the current unit.

        :return: JSON object represents MassMomentOfInertia DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "KilogramSquareMeter"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of MassMomentOfInertia DTO from a json representation.

        :param data: The MassMomentOfInertia DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "KilogramSquareMeter"}
        :return: A new instance of MassMomentOfInertiaDto.
        :rtype: MassMomentOfInertiaDto
        """
        return MassMomentOfInertiaDto(value=data["value"], unit=MassMomentOfInertiaUnits(data["unit"]))


class MassMomentOfInertia(AbstractMeasure):
    """
    A property of body reflects how its mass is distributed with regard to an axis.

    Args:
        value (float): The value.
        from_unit (MassMomentOfInertiaUnits): The MassMomentOfInertia unit to create from, The default unit is KilogramSquareMeter
    """
    def __init__(self, value: float, from_unit: MassMomentOfInertiaUnits = MassMomentOfInertiaUnits.KilogramSquareMeter):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__gram_square_meters = None
        
        self.__gram_square_decimeters = None
        
        self.__gram_square_centimeters = None
        
        self.__gram_square_millimeters = None
        
        self.__tonne_square_meters = None
        
        self.__tonne_square_decimeters = None
        
        self.__tonne_square_centimeters = None
        
        self.__tonne_square_milimeters = None
        
        self.__pound_square_feet = None
        
        self.__pound_square_inches = None
        
        self.__slug_square_feet = None
        
        self.__slug_square_inches = None
        
        self.__milligram_square_meters = None
        
        self.__kilogram_square_meters = None
        
        self.__milligram_square_decimeters = None
        
        self.__kilogram_square_decimeters = None
        
        self.__milligram_square_centimeters = None
        
        self.__kilogram_square_centimeters = None
        
        self.__milligram_square_millimeters = None
        
        self.__kilogram_square_millimeters = None
        
        self.__kilotonne_square_meters = None
        
        self.__megatonne_square_meters = None
        
        self.__kilotonne_square_decimeters = None
        
        self.__megatonne_square_decimeters = None
        
        self.__kilotonne_square_centimeters = None
        
        self.__megatonne_square_centimeters = None
        
        self.__kilotonne_square_milimeters = None
        
        self.__megatonne_square_milimeters = None
        

    def convert(self, unit: MassMomentOfInertiaUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: MassMomentOfInertiaUnits = MassMomentOfInertiaUnits.KilogramSquareMeter) -> MassMomentOfInertiaDto:
        """
        Get a new instance of MassMomentOfInertia DTO representing the current unit.

        :param hold_in_unit: The specific MassMomentOfInertia unit to store the MassMomentOfInertia value in the DTO representation.
        :type hold_in_unit: MassMomentOfInertiaUnits
        :return: A new instance of MassMomentOfInertiaDto.
        :rtype: MassMomentOfInertiaDto
        """
        return MassMomentOfInertiaDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: MassMomentOfInertiaUnits = MassMomentOfInertiaUnits.KilogramSquareMeter):
        """
        Get a MassMomentOfInertia DTO JSON object representing the current unit.

        :param hold_in_unit: The specific MassMomentOfInertia unit to store the MassMomentOfInertia value in the DTO representation.
        :type hold_in_unit: MassMomentOfInertiaUnits
        :return: JSON object represents MassMomentOfInertia DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "KilogramSquareMeter"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(mass_moment_of_inertia_dto: MassMomentOfInertiaDto):
        """
        Obtain a new instance of MassMomentOfInertia from a DTO unit object.

        :param mass_moment_of_inertia_dto: The MassMomentOfInertia DTO representation.
        :type mass_moment_of_inertia_dto: MassMomentOfInertiaDto
        :return: A new instance of MassMomentOfInertia.
        :rtype: MassMomentOfInertia
        """
        return MassMomentOfInertia(mass_moment_of_inertia_dto.value, mass_moment_of_inertia_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of MassMomentOfInertia from a DTO unit json representation.

        :param data: The MassMomentOfInertia DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "KilogramSquareMeter"}
        :return: A new instance of MassMomentOfInertia.
        :rtype: MassMomentOfInertia
        """
        return MassMomentOfInertia.from_dto(MassMomentOfInertiaDto.from_json(data))

    def __convert_from_base(self, from_unit: MassMomentOfInertiaUnits) -> float:
        value = self._value
        
        if from_unit == MassMomentOfInertiaUnits.GramSquareMeter:
            return (value * 1e3)
        
        if from_unit == MassMomentOfInertiaUnits.GramSquareDecimeter:
            return (value * 1e5)
        
        if from_unit == MassMomentOfInertiaUnits.GramSquareCentimeter:
            return (value * 1e7)
        
        if from_unit == MassMomentOfInertiaUnits.GramSquareMillimeter:
            return (value * 1e9)
        
        if from_unit == MassMomentOfInertiaUnits.TonneSquareMeter:
            return (value * 1e-3)
        
        if from_unit == MassMomentOfInertiaUnits.TonneSquareDecimeter:
            return (value * 1e-1)
        
        if from_unit == MassMomentOfInertiaUnits.TonneSquareCentimeter:
            return (value * 1e1)
        
        if from_unit == MassMomentOfInertiaUnits.TonneSquareMilimeter:
            return (value * 1e3)
        
        if from_unit == MassMomentOfInertiaUnits.PoundSquareFoot:
            return (value / 4.21401101e-2)
        
        if from_unit == MassMomentOfInertiaUnits.PoundSquareInch:
            return (value / 2.9263965e-4)
        
        if from_unit == MassMomentOfInertiaUnits.SlugSquareFoot:
            return (value / 1.3558179619)
        
        if from_unit == MassMomentOfInertiaUnits.SlugSquareInch:
            return (value / 9.41540242e-3)
        
        if from_unit == MassMomentOfInertiaUnits.MilligramSquareMeter:
            return ((value * 1e3) / 0.001)
        
        if from_unit == MassMomentOfInertiaUnits.KilogramSquareMeter:
            return ((value * 1e3) / 1000.0)
        
        if from_unit == MassMomentOfInertiaUnits.MilligramSquareDecimeter:
            return ((value * 1e5) / 0.001)
        
        if from_unit == MassMomentOfInertiaUnits.KilogramSquareDecimeter:
            return ((value * 1e5) / 1000.0)
        
        if from_unit == MassMomentOfInertiaUnits.MilligramSquareCentimeter:
            return ((value * 1e7) / 0.001)
        
        if from_unit == MassMomentOfInertiaUnits.KilogramSquareCentimeter:
            return ((value * 1e7) / 1000.0)
        
        if from_unit == MassMomentOfInertiaUnits.MilligramSquareMillimeter:
            return ((value * 1e9) / 0.001)
        
        if from_unit == MassMomentOfInertiaUnits.KilogramSquareMillimeter:
            return ((value * 1e9) / 1000.0)
        
        if from_unit == MassMomentOfInertiaUnits.KilotonneSquareMeter:
            return ((value * 1e-3) / 1000.0)
        
        if from_unit == MassMomentOfInertiaUnits.MegatonneSquareMeter:
            return ((value * 1e-3) / 1000000.0)
        
        if from_unit == MassMomentOfInertiaUnits.KilotonneSquareDecimeter:
            return ((value * 1e-1) / 1000.0)
        
        if from_unit == MassMomentOfInertiaUnits.MegatonneSquareDecimeter:
            return ((value * 1e-1) / 1000000.0)
        
        if from_unit == MassMomentOfInertiaUnits.KilotonneSquareCentimeter:
            return ((value * 1e1) / 1000.0)
        
        if from_unit == MassMomentOfInertiaUnits.MegatonneSquareCentimeter:
            return ((value * 1e1) / 1000000.0)
        
        if from_unit == MassMomentOfInertiaUnits.KilotonneSquareMilimeter:
            return ((value * 1e3) / 1000.0)
        
        if from_unit == MassMomentOfInertiaUnits.MegatonneSquareMilimeter:
            return ((value * 1e3) / 1000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: MassMomentOfInertiaUnits) -> float:
        
        if to_unit == MassMomentOfInertiaUnits.GramSquareMeter:
            return (value / 1e3)
        
        if to_unit == MassMomentOfInertiaUnits.GramSquareDecimeter:
            return (value / 1e5)
        
        if to_unit == MassMomentOfInertiaUnits.GramSquareCentimeter:
            return (value / 1e7)
        
        if to_unit == MassMomentOfInertiaUnits.GramSquareMillimeter:
            return (value / 1e9)
        
        if to_unit == MassMomentOfInertiaUnits.TonneSquareMeter:
            return (value / 1e-3)
        
        if to_unit == MassMomentOfInertiaUnits.TonneSquareDecimeter:
            return (value / 1e-1)
        
        if to_unit == MassMomentOfInertiaUnits.TonneSquareCentimeter:
            return (value / 1e1)
        
        if to_unit == MassMomentOfInertiaUnits.TonneSquareMilimeter:
            return (value / 1e3)
        
        if to_unit == MassMomentOfInertiaUnits.PoundSquareFoot:
            return (value * 4.21401101e-2)
        
        if to_unit == MassMomentOfInertiaUnits.PoundSquareInch:
            return (value * 2.9263965e-4)
        
        if to_unit == MassMomentOfInertiaUnits.SlugSquareFoot:
            return (value * 1.3558179619)
        
        if to_unit == MassMomentOfInertiaUnits.SlugSquareInch:
            return (value * 9.41540242e-3)
        
        if to_unit == MassMomentOfInertiaUnits.MilligramSquareMeter:
            return ((value / 1e3) * 0.001)
        
        if to_unit == MassMomentOfInertiaUnits.KilogramSquareMeter:
            return ((value / 1e3) * 1000.0)
        
        if to_unit == MassMomentOfInertiaUnits.MilligramSquareDecimeter:
            return ((value / 1e5) * 0.001)
        
        if to_unit == MassMomentOfInertiaUnits.KilogramSquareDecimeter:
            return ((value / 1e5) * 1000.0)
        
        if to_unit == MassMomentOfInertiaUnits.MilligramSquareCentimeter:
            return ((value / 1e7) * 0.001)
        
        if to_unit == MassMomentOfInertiaUnits.KilogramSquareCentimeter:
            return ((value / 1e7) * 1000.0)
        
        if to_unit == MassMomentOfInertiaUnits.MilligramSquareMillimeter:
            return ((value / 1e9) * 0.001)
        
        if to_unit == MassMomentOfInertiaUnits.KilogramSquareMillimeter:
            return ((value / 1e9) * 1000.0)
        
        if to_unit == MassMomentOfInertiaUnits.KilotonneSquareMeter:
            return ((value / 1e-3) * 1000.0)
        
        if to_unit == MassMomentOfInertiaUnits.MegatonneSquareMeter:
            return ((value / 1e-3) * 1000000.0)
        
        if to_unit == MassMomentOfInertiaUnits.KilotonneSquareDecimeter:
            return ((value / 1e-1) * 1000.0)
        
        if to_unit == MassMomentOfInertiaUnits.MegatonneSquareDecimeter:
            return ((value / 1e-1) * 1000000.0)
        
        if to_unit == MassMomentOfInertiaUnits.KilotonneSquareCentimeter:
            return ((value / 1e1) * 1000.0)
        
        if to_unit == MassMomentOfInertiaUnits.MegatonneSquareCentimeter:
            return ((value / 1e1) * 1000000.0)
        
        if to_unit == MassMomentOfInertiaUnits.KilotonneSquareMilimeter:
            return ((value / 1e3) * 1000.0)
        
        if to_unit == MassMomentOfInertiaUnits.MegatonneSquareMilimeter:
            return ((value / 1e3) * 1000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_gram_square_meters(gram_square_meters: float):
        """
        Create a new instance of MassMomentOfInertia from a value in gram_square_meters.

        

        :param meters: The MassMomentOfInertia value in gram_square_meters.
        :type gram_square_meters: float
        :return: A new instance of MassMomentOfInertia.
        :rtype: MassMomentOfInertia
        """
        return MassMomentOfInertia(gram_square_meters, MassMomentOfInertiaUnits.GramSquareMeter)

    
    @staticmethod
    def from_gram_square_decimeters(gram_square_decimeters: float):
        """
        Create a new instance of MassMomentOfInertia from a value in gram_square_decimeters.

        

        :param meters: The MassMomentOfInertia value in gram_square_decimeters.
        :type gram_square_decimeters: float
        :return: A new instance of MassMomentOfInertia.
        :rtype: MassMomentOfInertia
        """
        return MassMomentOfInertia(gram_square_decimeters, MassMomentOfInertiaUnits.GramSquareDecimeter)

    
    @staticmethod
    def from_gram_square_centimeters(gram_square_centimeters: float):
        """
        Create a new instance of MassMomentOfInertia from a value in gram_square_centimeters.

        

        :param meters: The MassMomentOfInertia value in gram_square_centimeters.
        :type gram_square_centimeters: float
        :return: A new instance of MassMomentOfInertia.
        :rtype: MassMomentOfInertia
        """
        return MassMomentOfInertia(gram_square_centimeters, MassMomentOfInertiaUnits.GramSquareCentimeter)

    
    @staticmethod
    def from_gram_square_millimeters(gram_square_millimeters: float):
        """
        Create a new instance of MassMomentOfInertia from a value in gram_square_millimeters.

        

        :param meters: The MassMomentOfInertia value in gram_square_millimeters.
        :type gram_square_millimeters: float
        :return: A new instance of MassMomentOfInertia.
        :rtype: MassMomentOfInertia
        """
        return MassMomentOfInertia(gram_square_millimeters, MassMomentOfInertiaUnits.GramSquareMillimeter)

    
    @staticmethod
    def from_tonne_square_meters(tonne_square_meters: float):
        """
        Create a new instance of MassMomentOfInertia from a value in tonne_square_meters.

        

        :param meters: The MassMomentOfInertia value in tonne_square_meters.
        :type tonne_square_meters: float
        :return: A new instance of MassMomentOfInertia.
        :rtype: MassMomentOfInertia
        """
        return MassMomentOfInertia(tonne_square_meters, MassMomentOfInertiaUnits.TonneSquareMeter)

    
    @staticmethod
    def from_tonne_square_decimeters(tonne_square_decimeters: float):
        """
        Create a new instance of MassMomentOfInertia from a value in tonne_square_decimeters.

        

        :param meters: The MassMomentOfInertia value in tonne_square_decimeters.
        :type tonne_square_decimeters: float
        :return: A new instance of MassMomentOfInertia.
        :rtype: MassMomentOfInertia
        """
        return MassMomentOfInertia(tonne_square_decimeters, MassMomentOfInertiaUnits.TonneSquareDecimeter)

    
    @staticmethod
    def from_tonne_square_centimeters(tonne_square_centimeters: float):
        """
        Create a new instance of MassMomentOfInertia from a value in tonne_square_centimeters.

        

        :param meters: The MassMomentOfInertia value in tonne_square_centimeters.
        :type tonne_square_centimeters: float
        :return: A new instance of MassMomentOfInertia.
        :rtype: MassMomentOfInertia
        """
        return MassMomentOfInertia(tonne_square_centimeters, MassMomentOfInertiaUnits.TonneSquareCentimeter)

    
    @staticmethod
    def from_tonne_square_milimeters(tonne_square_milimeters: float):
        """
        Create a new instance of MassMomentOfInertia from a value in tonne_square_milimeters.

        

        :param meters: The MassMomentOfInertia value in tonne_square_milimeters.
        :type tonne_square_milimeters: float
        :return: A new instance of MassMomentOfInertia.
        :rtype: MassMomentOfInertia
        """
        return MassMomentOfInertia(tonne_square_milimeters, MassMomentOfInertiaUnits.TonneSquareMilimeter)

    
    @staticmethod
    def from_pound_square_feet(pound_square_feet: float):
        """
        Create a new instance of MassMomentOfInertia from a value in pound_square_feet.

        

        :param meters: The MassMomentOfInertia value in pound_square_feet.
        :type pound_square_feet: float
        :return: A new instance of MassMomentOfInertia.
        :rtype: MassMomentOfInertia
        """
        return MassMomentOfInertia(pound_square_feet, MassMomentOfInertiaUnits.PoundSquareFoot)

    
    @staticmethod
    def from_pound_square_inches(pound_square_inches: float):
        """
        Create a new instance of MassMomentOfInertia from a value in pound_square_inches.

        

        :param meters: The MassMomentOfInertia value in pound_square_inches.
        :type pound_square_inches: float
        :return: A new instance of MassMomentOfInertia.
        :rtype: MassMomentOfInertia
        """
        return MassMomentOfInertia(pound_square_inches, MassMomentOfInertiaUnits.PoundSquareInch)

    
    @staticmethod
    def from_slug_square_feet(slug_square_feet: float):
        """
        Create a new instance of MassMomentOfInertia from a value in slug_square_feet.

        

        :param meters: The MassMomentOfInertia value in slug_square_feet.
        :type slug_square_feet: float
        :return: A new instance of MassMomentOfInertia.
        :rtype: MassMomentOfInertia
        """
        return MassMomentOfInertia(slug_square_feet, MassMomentOfInertiaUnits.SlugSquareFoot)

    
    @staticmethod
    def from_slug_square_inches(slug_square_inches: float):
        """
        Create a new instance of MassMomentOfInertia from a value in slug_square_inches.

        

        :param meters: The MassMomentOfInertia value in slug_square_inches.
        :type slug_square_inches: float
        :return: A new instance of MassMomentOfInertia.
        :rtype: MassMomentOfInertia
        """
        return MassMomentOfInertia(slug_square_inches, MassMomentOfInertiaUnits.SlugSquareInch)

    
    @staticmethod
    def from_milligram_square_meters(milligram_square_meters: float):
        """
        Create a new instance of MassMomentOfInertia from a value in milligram_square_meters.

        

        :param meters: The MassMomentOfInertia value in milligram_square_meters.
        :type milligram_square_meters: float
        :return: A new instance of MassMomentOfInertia.
        :rtype: MassMomentOfInertia
        """
        return MassMomentOfInertia(milligram_square_meters, MassMomentOfInertiaUnits.MilligramSquareMeter)

    
    @staticmethod
    def from_kilogram_square_meters(kilogram_square_meters: float):
        """
        Create a new instance of MassMomentOfInertia from a value in kilogram_square_meters.

        

        :param meters: The MassMomentOfInertia value in kilogram_square_meters.
        :type kilogram_square_meters: float
        :return: A new instance of MassMomentOfInertia.
        :rtype: MassMomentOfInertia
        """
        return MassMomentOfInertia(kilogram_square_meters, MassMomentOfInertiaUnits.KilogramSquareMeter)

    
    @staticmethod
    def from_milligram_square_decimeters(milligram_square_decimeters: float):
        """
        Create a new instance of MassMomentOfInertia from a value in milligram_square_decimeters.

        

        :param meters: The MassMomentOfInertia value in milligram_square_decimeters.
        :type milligram_square_decimeters: float
        :return: A new instance of MassMomentOfInertia.
        :rtype: MassMomentOfInertia
        """
        return MassMomentOfInertia(milligram_square_decimeters, MassMomentOfInertiaUnits.MilligramSquareDecimeter)

    
    @staticmethod
    def from_kilogram_square_decimeters(kilogram_square_decimeters: float):
        """
        Create a new instance of MassMomentOfInertia from a value in kilogram_square_decimeters.

        

        :param meters: The MassMomentOfInertia value in kilogram_square_decimeters.
        :type kilogram_square_decimeters: float
        :return: A new instance of MassMomentOfInertia.
        :rtype: MassMomentOfInertia
        """
        return MassMomentOfInertia(kilogram_square_decimeters, MassMomentOfInertiaUnits.KilogramSquareDecimeter)

    
    @staticmethod
    def from_milligram_square_centimeters(milligram_square_centimeters: float):
        """
        Create a new instance of MassMomentOfInertia from a value in milligram_square_centimeters.

        

        :param meters: The MassMomentOfInertia value in milligram_square_centimeters.
        :type milligram_square_centimeters: float
        :return: A new instance of MassMomentOfInertia.
        :rtype: MassMomentOfInertia
        """
        return MassMomentOfInertia(milligram_square_centimeters, MassMomentOfInertiaUnits.MilligramSquareCentimeter)

    
    @staticmethod
    def from_kilogram_square_centimeters(kilogram_square_centimeters: float):
        """
        Create a new instance of MassMomentOfInertia from a value in kilogram_square_centimeters.

        

        :param meters: The MassMomentOfInertia value in kilogram_square_centimeters.
        :type kilogram_square_centimeters: float
        :return: A new instance of MassMomentOfInertia.
        :rtype: MassMomentOfInertia
        """
        return MassMomentOfInertia(kilogram_square_centimeters, MassMomentOfInertiaUnits.KilogramSquareCentimeter)

    
    @staticmethod
    def from_milligram_square_millimeters(milligram_square_millimeters: float):
        """
        Create a new instance of MassMomentOfInertia from a value in milligram_square_millimeters.

        

        :param meters: The MassMomentOfInertia value in milligram_square_millimeters.
        :type milligram_square_millimeters: float
        :return: A new instance of MassMomentOfInertia.
        :rtype: MassMomentOfInertia
        """
        return MassMomentOfInertia(milligram_square_millimeters, MassMomentOfInertiaUnits.MilligramSquareMillimeter)

    
    @staticmethod
    def from_kilogram_square_millimeters(kilogram_square_millimeters: float):
        """
        Create a new instance of MassMomentOfInertia from a value in kilogram_square_millimeters.

        

        :param meters: The MassMomentOfInertia value in kilogram_square_millimeters.
        :type kilogram_square_millimeters: float
        :return: A new instance of MassMomentOfInertia.
        :rtype: MassMomentOfInertia
        """
        return MassMomentOfInertia(kilogram_square_millimeters, MassMomentOfInertiaUnits.KilogramSquareMillimeter)

    
    @staticmethod
    def from_kilotonne_square_meters(kilotonne_square_meters: float):
        """
        Create a new instance of MassMomentOfInertia from a value in kilotonne_square_meters.

        

        :param meters: The MassMomentOfInertia value in kilotonne_square_meters.
        :type kilotonne_square_meters: float
        :return: A new instance of MassMomentOfInertia.
        :rtype: MassMomentOfInertia
        """
        return MassMomentOfInertia(kilotonne_square_meters, MassMomentOfInertiaUnits.KilotonneSquareMeter)

    
    @staticmethod
    def from_megatonne_square_meters(megatonne_square_meters: float):
        """
        Create a new instance of MassMomentOfInertia from a value in megatonne_square_meters.

        

        :param meters: The MassMomentOfInertia value in megatonne_square_meters.
        :type megatonne_square_meters: float
        :return: A new instance of MassMomentOfInertia.
        :rtype: MassMomentOfInertia
        """
        return MassMomentOfInertia(megatonne_square_meters, MassMomentOfInertiaUnits.MegatonneSquareMeter)

    
    @staticmethod
    def from_kilotonne_square_decimeters(kilotonne_square_decimeters: float):
        """
        Create a new instance of MassMomentOfInertia from a value in kilotonne_square_decimeters.

        

        :param meters: The MassMomentOfInertia value in kilotonne_square_decimeters.
        :type kilotonne_square_decimeters: float
        :return: A new instance of MassMomentOfInertia.
        :rtype: MassMomentOfInertia
        """
        return MassMomentOfInertia(kilotonne_square_decimeters, MassMomentOfInertiaUnits.KilotonneSquareDecimeter)

    
    @staticmethod
    def from_megatonne_square_decimeters(megatonne_square_decimeters: float):
        """
        Create a new instance of MassMomentOfInertia from a value in megatonne_square_decimeters.

        

        :param meters: The MassMomentOfInertia value in megatonne_square_decimeters.
        :type megatonne_square_decimeters: float
        :return: A new instance of MassMomentOfInertia.
        :rtype: MassMomentOfInertia
        """
        return MassMomentOfInertia(megatonne_square_decimeters, MassMomentOfInertiaUnits.MegatonneSquareDecimeter)

    
    @staticmethod
    def from_kilotonne_square_centimeters(kilotonne_square_centimeters: float):
        """
        Create a new instance of MassMomentOfInertia from a value in kilotonne_square_centimeters.

        

        :param meters: The MassMomentOfInertia value in kilotonne_square_centimeters.
        :type kilotonne_square_centimeters: float
        :return: A new instance of MassMomentOfInertia.
        :rtype: MassMomentOfInertia
        """
        return MassMomentOfInertia(kilotonne_square_centimeters, MassMomentOfInertiaUnits.KilotonneSquareCentimeter)

    
    @staticmethod
    def from_megatonne_square_centimeters(megatonne_square_centimeters: float):
        """
        Create a new instance of MassMomentOfInertia from a value in megatonne_square_centimeters.

        

        :param meters: The MassMomentOfInertia value in megatonne_square_centimeters.
        :type megatonne_square_centimeters: float
        :return: A new instance of MassMomentOfInertia.
        :rtype: MassMomentOfInertia
        """
        return MassMomentOfInertia(megatonne_square_centimeters, MassMomentOfInertiaUnits.MegatonneSquareCentimeter)

    
    @staticmethod
    def from_kilotonne_square_milimeters(kilotonne_square_milimeters: float):
        """
        Create a new instance of MassMomentOfInertia from a value in kilotonne_square_milimeters.

        

        :param meters: The MassMomentOfInertia value in kilotonne_square_milimeters.
        :type kilotonne_square_milimeters: float
        :return: A new instance of MassMomentOfInertia.
        :rtype: MassMomentOfInertia
        """
        return MassMomentOfInertia(kilotonne_square_milimeters, MassMomentOfInertiaUnits.KilotonneSquareMilimeter)

    
    @staticmethod
    def from_megatonne_square_milimeters(megatonne_square_milimeters: float):
        """
        Create a new instance of MassMomentOfInertia from a value in megatonne_square_milimeters.

        

        :param meters: The MassMomentOfInertia value in megatonne_square_milimeters.
        :type megatonne_square_milimeters: float
        :return: A new instance of MassMomentOfInertia.
        :rtype: MassMomentOfInertia
        """
        return MassMomentOfInertia(megatonne_square_milimeters, MassMomentOfInertiaUnits.MegatonneSquareMilimeter)

    
    @property
    def gram_square_meters(self) -> float:
        """
        
        """
        if self.__gram_square_meters != None:
            return self.__gram_square_meters
        self.__gram_square_meters = self.__convert_from_base(MassMomentOfInertiaUnits.GramSquareMeter)
        return self.__gram_square_meters

    
    @property
    def gram_square_decimeters(self) -> float:
        """
        
        """
        if self.__gram_square_decimeters != None:
            return self.__gram_square_decimeters
        self.__gram_square_decimeters = self.__convert_from_base(MassMomentOfInertiaUnits.GramSquareDecimeter)
        return self.__gram_square_decimeters

    
    @property
    def gram_square_centimeters(self) -> float:
        """
        
        """
        if self.__gram_square_centimeters != None:
            return self.__gram_square_centimeters
        self.__gram_square_centimeters = self.__convert_from_base(MassMomentOfInertiaUnits.GramSquareCentimeter)
        return self.__gram_square_centimeters

    
    @property
    def gram_square_millimeters(self) -> float:
        """
        
        """
        if self.__gram_square_millimeters != None:
            return self.__gram_square_millimeters
        self.__gram_square_millimeters = self.__convert_from_base(MassMomentOfInertiaUnits.GramSquareMillimeter)
        return self.__gram_square_millimeters

    
    @property
    def tonne_square_meters(self) -> float:
        """
        
        """
        if self.__tonne_square_meters != None:
            return self.__tonne_square_meters
        self.__tonne_square_meters = self.__convert_from_base(MassMomentOfInertiaUnits.TonneSquareMeter)
        return self.__tonne_square_meters

    
    @property
    def tonne_square_decimeters(self) -> float:
        """
        
        """
        if self.__tonne_square_decimeters != None:
            return self.__tonne_square_decimeters
        self.__tonne_square_decimeters = self.__convert_from_base(MassMomentOfInertiaUnits.TonneSquareDecimeter)
        return self.__tonne_square_decimeters

    
    @property
    def tonne_square_centimeters(self) -> float:
        """
        
        """
        if self.__tonne_square_centimeters != None:
            return self.__tonne_square_centimeters
        self.__tonne_square_centimeters = self.__convert_from_base(MassMomentOfInertiaUnits.TonneSquareCentimeter)
        return self.__tonne_square_centimeters

    
    @property
    def tonne_square_milimeters(self) -> float:
        """
        
        """
        if self.__tonne_square_milimeters != None:
            return self.__tonne_square_milimeters
        self.__tonne_square_milimeters = self.__convert_from_base(MassMomentOfInertiaUnits.TonneSquareMilimeter)
        return self.__tonne_square_milimeters

    
    @property
    def pound_square_feet(self) -> float:
        """
        
        """
        if self.__pound_square_feet != None:
            return self.__pound_square_feet
        self.__pound_square_feet = self.__convert_from_base(MassMomentOfInertiaUnits.PoundSquareFoot)
        return self.__pound_square_feet

    
    @property
    def pound_square_inches(self) -> float:
        """
        
        """
        if self.__pound_square_inches != None:
            return self.__pound_square_inches
        self.__pound_square_inches = self.__convert_from_base(MassMomentOfInertiaUnits.PoundSquareInch)
        return self.__pound_square_inches

    
    @property
    def slug_square_feet(self) -> float:
        """
        
        """
        if self.__slug_square_feet != None:
            return self.__slug_square_feet
        self.__slug_square_feet = self.__convert_from_base(MassMomentOfInertiaUnits.SlugSquareFoot)
        return self.__slug_square_feet

    
    @property
    def slug_square_inches(self) -> float:
        """
        
        """
        if self.__slug_square_inches != None:
            return self.__slug_square_inches
        self.__slug_square_inches = self.__convert_from_base(MassMomentOfInertiaUnits.SlugSquareInch)
        return self.__slug_square_inches

    
    @property
    def milligram_square_meters(self) -> float:
        """
        
        """
        if self.__milligram_square_meters != None:
            return self.__milligram_square_meters
        self.__milligram_square_meters = self.__convert_from_base(MassMomentOfInertiaUnits.MilligramSquareMeter)
        return self.__milligram_square_meters

    
    @property
    def kilogram_square_meters(self) -> float:
        """
        
        """
        if self.__kilogram_square_meters != None:
            return self.__kilogram_square_meters
        self.__kilogram_square_meters = self.__convert_from_base(MassMomentOfInertiaUnits.KilogramSquareMeter)
        return self.__kilogram_square_meters

    
    @property
    def milligram_square_decimeters(self) -> float:
        """
        
        """
        if self.__milligram_square_decimeters != None:
            return self.__milligram_square_decimeters
        self.__milligram_square_decimeters = self.__convert_from_base(MassMomentOfInertiaUnits.MilligramSquareDecimeter)
        return self.__milligram_square_decimeters

    
    @property
    def kilogram_square_decimeters(self) -> float:
        """
        
        """
        if self.__kilogram_square_decimeters != None:
            return self.__kilogram_square_decimeters
        self.__kilogram_square_decimeters = self.__convert_from_base(MassMomentOfInertiaUnits.KilogramSquareDecimeter)
        return self.__kilogram_square_decimeters

    
    @property
    def milligram_square_centimeters(self) -> float:
        """
        
        """
        if self.__milligram_square_centimeters != None:
            return self.__milligram_square_centimeters
        self.__milligram_square_centimeters = self.__convert_from_base(MassMomentOfInertiaUnits.MilligramSquareCentimeter)
        return self.__milligram_square_centimeters

    
    @property
    def kilogram_square_centimeters(self) -> float:
        """
        
        """
        if self.__kilogram_square_centimeters != None:
            return self.__kilogram_square_centimeters
        self.__kilogram_square_centimeters = self.__convert_from_base(MassMomentOfInertiaUnits.KilogramSquareCentimeter)
        return self.__kilogram_square_centimeters

    
    @property
    def milligram_square_millimeters(self) -> float:
        """
        
        """
        if self.__milligram_square_millimeters != None:
            return self.__milligram_square_millimeters
        self.__milligram_square_millimeters = self.__convert_from_base(MassMomentOfInertiaUnits.MilligramSquareMillimeter)
        return self.__milligram_square_millimeters

    
    @property
    def kilogram_square_millimeters(self) -> float:
        """
        
        """
        if self.__kilogram_square_millimeters != None:
            return self.__kilogram_square_millimeters
        self.__kilogram_square_millimeters = self.__convert_from_base(MassMomentOfInertiaUnits.KilogramSquareMillimeter)
        return self.__kilogram_square_millimeters

    
    @property
    def kilotonne_square_meters(self) -> float:
        """
        
        """
        if self.__kilotonne_square_meters != None:
            return self.__kilotonne_square_meters
        self.__kilotonne_square_meters = self.__convert_from_base(MassMomentOfInertiaUnits.KilotonneSquareMeter)
        return self.__kilotonne_square_meters

    
    @property
    def megatonne_square_meters(self) -> float:
        """
        
        """
        if self.__megatonne_square_meters != None:
            return self.__megatonne_square_meters
        self.__megatonne_square_meters = self.__convert_from_base(MassMomentOfInertiaUnits.MegatonneSquareMeter)
        return self.__megatonne_square_meters

    
    @property
    def kilotonne_square_decimeters(self) -> float:
        """
        
        """
        if self.__kilotonne_square_decimeters != None:
            return self.__kilotonne_square_decimeters
        self.__kilotonne_square_decimeters = self.__convert_from_base(MassMomentOfInertiaUnits.KilotonneSquareDecimeter)
        return self.__kilotonne_square_decimeters

    
    @property
    def megatonne_square_decimeters(self) -> float:
        """
        
        """
        if self.__megatonne_square_decimeters != None:
            return self.__megatonne_square_decimeters
        self.__megatonne_square_decimeters = self.__convert_from_base(MassMomentOfInertiaUnits.MegatonneSquareDecimeter)
        return self.__megatonne_square_decimeters

    
    @property
    def kilotonne_square_centimeters(self) -> float:
        """
        
        """
        if self.__kilotonne_square_centimeters != None:
            return self.__kilotonne_square_centimeters
        self.__kilotonne_square_centimeters = self.__convert_from_base(MassMomentOfInertiaUnits.KilotonneSquareCentimeter)
        return self.__kilotonne_square_centimeters

    
    @property
    def megatonne_square_centimeters(self) -> float:
        """
        
        """
        if self.__megatonne_square_centimeters != None:
            return self.__megatonne_square_centimeters
        self.__megatonne_square_centimeters = self.__convert_from_base(MassMomentOfInertiaUnits.MegatonneSquareCentimeter)
        return self.__megatonne_square_centimeters

    
    @property
    def kilotonne_square_milimeters(self) -> float:
        """
        
        """
        if self.__kilotonne_square_milimeters != None:
            return self.__kilotonne_square_milimeters
        self.__kilotonne_square_milimeters = self.__convert_from_base(MassMomentOfInertiaUnits.KilotonneSquareMilimeter)
        return self.__kilotonne_square_milimeters

    
    @property
    def megatonne_square_milimeters(self) -> float:
        """
        
        """
        if self.__megatonne_square_milimeters != None:
            return self.__megatonne_square_milimeters
        self.__megatonne_square_milimeters = self.__convert_from_base(MassMomentOfInertiaUnits.MegatonneSquareMilimeter)
        return self.__megatonne_square_milimeters

    
    def to_string(self, unit: MassMomentOfInertiaUnits = MassMomentOfInertiaUnits.KilogramSquareMeter, fractional_digits: int = None) -> str:
        """
        Format the MassMomentOfInertia to a string.
        
        Note: the default format for MassMomentOfInertia is KilogramSquareMeter.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the MassMomentOfInertia. Default is 'KilogramSquareMeter'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == MassMomentOfInertiaUnits.GramSquareMeter:
            return f"""{super()._truncate_fraction_digits(self.gram_square_meters, fractional_digits)} g·m²"""
        
        if unit == MassMomentOfInertiaUnits.GramSquareDecimeter:
            return f"""{super()._truncate_fraction_digits(self.gram_square_decimeters, fractional_digits)} g·dm²"""
        
        if unit == MassMomentOfInertiaUnits.GramSquareCentimeter:
            return f"""{super()._truncate_fraction_digits(self.gram_square_centimeters, fractional_digits)} g·cm²"""
        
        if unit == MassMomentOfInertiaUnits.GramSquareMillimeter:
            return f"""{super()._truncate_fraction_digits(self.gram_square_millimeters, fractional_digits)} g·mm²"""
        
        if unit == MassMomentOfInertiaUnits.TonneSquareMeter:
            return f"""{super()._truncate_fraction_digits(self.tonne_square_meters, fractional_digits)} t·m²"""
        
        if unit == MassMomentOfInertiaUnits.TonneSquareDecimeter:
            return f"""{super()._truncate_fraction_digits(self.tonne_square_decimeters, fractional_digits)} t·dm²"""
        
        if unit == MassMomentOfInertiaUnits.TonneSquareCentimeter:
            return f"""{super()._truncate_fraction_digits(self.tonne_square_centimeters, fractional_digits)} t·cm²"""
        
        if unit == MassMomentOfInertiaUnits.TonneSquareMilimeter:
            return f"""{super()._truncate_fraction_digits(self.tonne_square_milimeters, fractional_digits)} t·mm²"""
        
        if unit == MassMomentOfInertiaUnits.PoundSquareFoot:
            return f"""{super()._truncate_fraction_digits(self.pound_square_feet, fractional_digits)} lb·ft²"""
        
        if unit == MassMomentOfInertiaUnits.PoundSquareInch:
            return f"""{super()._truncate_fraction_digits(self.pound_square_inches, fractional_digits)} lb·in²"""
        
        if unit == MassMomentOfInertiaUnits.SlugSquareFoot:
            return f"""{super()._truncate_fraction_digits(self.slug_square_feet, fractional_digits)} slug·ft²"""
        
        if unit == MassMomentOfInertiaUnits.SlugSquareInch:
            return f"""{super()._truncate_fraction_digits(self.slug_square_inches, fractional_digits)} slug·in²"""
        
        if unit == MassMomentOfInertiaUnits.MilligramSquareMeter:
            return f"""{super()._truncate_fraction_digits(self.milligram_square_meters, fractional_digits)} mg·m²"""
        
        if unit == MassMomentOfInertiaUnits.KilogramSquareMeter:
            return f"""{super()._truncate_fraction_digits(self.kilogram_square_meters, fractional_digits)} kg·m²"""
        
        if unit == MassMomentOfInertiaUnits.MilligramSquareDecimeter:
            return f"""{super()._truncate_fraction_digits(self.milligram_square_decimeters, fractional_digits)} mg·dm²"""
        
        if unit == MassMomentOfInertiaUnits.KilogramSquareDecimeter:
            return f"""{super()._truncate_fraction_digits(self.kilogram_square_decimeters, fractional_digits)} kg·dm²"""
        
        if unit == MassMomentOfInertiaUnits.MilligramSquareCentimeter:
            return f"""{super()._truncate_fraction_digits(self.milligram_square_centimeters, fractional_digits)} mg·cm²"""
        
        if unit == MassMomentOfInertiaUnits.KilogramSquareCentimeter:
            return f"""{super()._truncate_fraction_digits(self.kilogram_square_centimeters, fractional_digits)} kg·cm²"""
        
        if unit == MassMomentOfInertiaUnits.MilligramSquareMillimeter:
            return f"""{super()._truncate_fraction_digits(self.milligram_square_millimeters, fractional_digits)} mg·mm²"""
        
        if unit == MassMomentOfInertiaUnits.KilogramSquareMillimeter:
            return f"""{super()._truncate_fraction_digits(self.kilogram_square_millimeters, fractional_digits)} kg·mm²"""
        
        if unit == MassMomentOfInertiaUnits.KilotonneSquareMeter:
            return f"""{super()._truncate_fraction_digits(self.kilotonne_square_meters, fractional_digits)} kt·m²"""
        
        if unit == MassMomentOfInertiaUnits.MegatonneSquareMeter:
            return f"""{super()._truncate_fraction_digits(self.megatonne_square_meters, fractional_digits)} Mt·m²"""
        
        if unit == MassMomentOfInertiaUnits.KilotonneSquareDecimeter:
            return f"""{super()._truncate_fraction_digits(self.kilotonne_square_decimeters, fractional_digits)} kt·dm²"""
        
        if unit == MassMomentOfInertiaUnits.MegatonneSquareDecimeter:
            return f"""{super()._truncate_fraction_digits(self.megatonne_square_decimeters, fractional_digits)} Mt·dm²"""
        
        if unit == MassMomentOfInertiaUnits.KilotonneSquareCentimeter:
            return f"""{super()._truncate_fraction_digits(self.kilotonne_square_centimeters, fractional_digits)} kt·cm²"""
        
        if unit == MassMomentOfInertiaUnits.MegatonneSquareCentimeter:
            return f"""{super()._truncate_fraction_digits(self.megatonne_square_centimeters, fractional_digits)} Mt·cm²"""
        
        if unit == MassMomentOfInertiaUnits.KilotonneSquareMilimeter:
            return f"""{super()._truncate_fraction_digits(self.kilotonne_square_milimeters, fractional_digits)} kt·mm²"""
        
        if unit == MassMomentOfInertiaUnits.MegatonneSquareMilimeter:
            return f"""{super()._truncate_fraction_digits(self.megatonne_square_milimeters, fractional_digits)} Mt·mm²"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: MassMomentOfInertiaUnits = MassMomentOfInertiaUnits.KilogramSquareMeter) -> str:
        """
        Get MassMomentOfInertia unit abbreviation.
        Note! the default abbreviation for MassMomentOfInertia is KilogramSquareMeter.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == MassMomentOfInertiaUnits.GramSquareMeter:
            return """g·m²"""
        
        if unit_abbreviation == MassMomentOfInertiaUnits.GramSquareDecimeter:
            return """g·dm²"""
        
        if unit_abbreviation == MassMomentOfInertiaUnits.GramSquareCentimeter:
            return """g·cm²"""
        
        if unit_abbreviation == MassMomentOfInertiaUnits.GramSquareMillimeter:
            return """g·mm²"""
        
        if unit_abbreviation == MassMomentOfInertiaUnits.TonneSquareMeter:
            return """t·m²"""
        
        if unit_abbreviation == MassMomentOfInertiaUnits.TonneSquareDecimeter:
            return """t·dm²"""
        
        if unit_abbreviation == MassMomentOfInertiaUnits.TonneSquareCentimeter:
            return """t·cm²"""
        
        if unit_abbreviation == MassMomentOfInertiaUnits.TonneSquareMilimeter:
            return """t·mm²"""
        
        if unit_abbreviation == MassMomentOfInertiaUnits.PoundSquareFoot:
            return """lb·ft²"""
        
        if unit_abbreviation == MassMomentOfInertiaUnits.PoundSquareInch:
            return """lb·in²"""
        
        if unit_abbreviation == MassMomentOfInertiaUnits.SlugSquareFoot:
            return """slug·ft²"""
        
        if unit_abbreviation == MassMomentOfInertiaUnits.SlugSquareInch:
            return """slug·in²"""
        
        if unit_abbreviation == MassMomentOfInertiaUnits.MilligramSquareMeter:
            return """mg·m²"""
        
        if unit_abbreviation == MassMomentOfInertiaUnits.KilogramSquareMeter:
            return """kg·m²"""
        
        if unit_abbreviation == MassMomentOfInertiaUnits.MilligramSquareDecimeter:
            return """mg·dm²"""
        
        if unit_abbreviation == MassMomentOfInertiaUnits.KilogramSquareDecimeter:
            return """kg·dm²"""
        
        if unit_abbreviation == MassMomentOfInertiaUnits.MilligramSquareCentimeter:
            return """mg·cm²"""
        
        if unit_abbreviation == MassMomentOfInertiaUnits.KilogramSquareCentimeter:
            return """kg·cm²"""
        
        if unit_abbreviation == MassMomentOfInertiaUnits.MilligramSquareMillimeter:
            return """mg·mm²"""
        
        if unit_abbreviation == MassMomentOfInertiaUnits.KilogramSquareMillimeter:
            return """kg·mm²"""
        
        if unit_abbreviation == MassMomentOfInertiaUnits.KilotonneSquareMeter:
            return """kt·m²"""
        
        if unit_abbreviation == MassMomentOfInertiaUnits.MegatonneSquareMeter:
            return """Mt·m²"""
        
        if unit_abbreviation == MassMomentOfInertiaUnits.KilotonneSquareDecimeter:
            return """kt·dm²"""
        
        if unit_abbreviation == MassMomentOfInertiaUnits.MegatonneSquareDecimeter:
            return """Mt·dm²"""
        
        if unit_abbreviation == MassMomentOfInertiaUnits.KilotonneSquareCentimeter:
            return """kt·cm²"""
        
        if unit_abbreviation == MassMomentOfInertiaUnits.MegatonneSquareCentimeter:
            return """Mt·cm²"""
        
        if unit_abbreviation == MassMomentOfInertiaUnits.KilotonneSquareMilimeter:
            return """kt·mm²"""
        
        if unit_abbreviation == MassMomentOfInertiaUnits.MegatonneSquareMilimeter:
            return """Mt·mm²"""
        
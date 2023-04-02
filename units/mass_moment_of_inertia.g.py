from enum import Enum
import math
import string


class MassMomentOfInertiaUnits(Enum):
        """
            MassMomentOfInertiaUnits enumeration
        """
        
        GramSquareMeter = 'gram_square_meter'
        """
            
        """
        
        GramSquareDecimeter = 'gram_square_decimeter'
        """
            
        """
        
        GramSquareCentimeter = 'gram_square_centimeter'
        """
            
        """
        
        GramSquareMillimeter = 'gram_square_millimeter'
        """
            
        """
        
        TonneSquareMeter = 'tonne_square_meter'
        """
            
        """
        
        TonneSquareDecimeter = 'tonne_square_decimeter'
        """
            
        """
        
        TonneSquareCentimeter = 'tonne_square_centimeter'
        """
            
        """
        
        TonneSquareMilimeter = 'tonne_square_milimeter'
        """
            
        """
        
        PoundSquareFoot = 'pound_square_foot'
        """
            
        """
        
        PoundSquareInch = 'pound_square_inch'
        """
            
        """
        
        SlugSquareFoot = 'slug_square_foot'
        """
            
        """
        
        SlugSquareInch = 'slug_square_inch'
        """
            
        """
        
        MilliGramSquareMeter = 'milli_gram_square_meter'
        """
            
        """
        
        KiloGramSquareMeter = 'kilo_gram_square_meter'
        """
            
        """
        
        MilliGramSquareDecimeter = 'milli_gram_square_decimeter'
        """
            
        """
        
        KiloGramSquareDecimeter = 'kilo_gram_square_decimeter'
        """
            
        """
        
        MilliGramSquareCentimeter = 'milli_gram_square_centimeter'
        """
            
        """
        
        KiloGramSquareCentimeter = 'kilo_gram_square_centimeter'
        """
            
        """
        
        MilliGramSquareMillimeter = 'milli_gram_square_millimeter'
        """
            
        """
        
        KiloGramSquareMillimeter = 'kilo_gram_square_millimeter'
        """
            
        """
        
        KiloTonneSquareMeter = 'kilo_tonne_square_meter'
        """
            
        """
        
        MegaTonneSquareMeter = 'mega_tonne_square_meter'
        """
            
        """
        
        KiloTonneSquareDecimeter = 'kilo_tonne_square_decimeter'
        """
            
        """
        
        MegaTonneSquareDecimeter = 'mega_tonne_square_decimeter'
        """
            
        """
        
        KiloTonneSquareCentimeter = 'kilo_tonne_square_centimeter'
        """
            
        """
        
        MegaTonneSquareCentimeter = 'mega_tonne_square_centimeter'
        """
            
        """
        
        KiloTonneSquareMilimeter = 'kilo_tonne_square_milimeter'
        """
            
        """
        
        MegaTonneSquareMilimeter = 'mega_tonne_square_milimeter'
        """
            
        """
        
    
class MassMomentOfInertia:
    """
    A property of body reflects how its mass is distributed with regard to an axis.

    Args:
        value (float): The value.
        from_unit (MassMomentOfInertiaUnits): The MassMomentOfInertia unit to create from, The default unit is KilogramSquareMeter
    """
    def __init__(self, value: float, from_unit: MassMomentOfInertiaUnits = MassMomentOfInertiaUnits.KilogramSquareMeter):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
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
        
        self.__milli_gram_square_meters = None
        
        self.__kilo_gram_square_meters = None
        
        self.__milli_gram_square_decimeters = None
        
        self.__kilo_gram_square_decimeters = None
        
        self.__milli_gram_square_centimeters = None
        
        self.__kilo_gram_square_centimeters = None
        
        self.__milli_gram_square_millimeters = None
        
        self.__kilo_gram_square_millimeters = None
        
        self.__kilo_tonne_square_meters = None
        
        self.__mega_tonne_square_meters = None
        
        self.__kilo_tonne_square_decimeters = None
        
        self.__mega_tonne_square_decimeters = None
        
        self.__kilo_tonne_square_centimeters = None
        
        self.__mega_tonne_square_centimeters = None
        
        self.__kilo_tonne_square_milimeters = None
        
        self.__mega_tonne_square_milimeters = None
        

    def __convert_from_base(self, from_unit: MassMomentOfInertiaUnits) -> float:
        value = self.__value
        
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
        
        if from_unit == MassMomentOfInertiaUnits.MilliGramSquareMeter:
            return ((value * 1e3) / 0.001)
        
        if from_unit == MassMomentOfInertiaUnits.KiloGramSquareMeter:
            return ((value * 1e3) / 1000.0)
        
        if from_unit == MassMomentOfInertiaUnits.MilliGramSquareDecimeter:
            return ((value * 1e5) / 0.001)
        
        if from_unit == MassMomentOfInertiaUnits.KiloGramSquareDecimeter:
            return ((value * 1e5) / 1000.0)
        
        if from_unit == MassMomentOfInertiaUnits.MilliGramSquareCentimeter:
            return ((value * 1e7) / 0.001)
        
        if from_unit == MassMomentOfInertiaUnits.KiloGramSquareCentimeter:
            return ((value * 1e7) / 1000.0)
        
        if from_unit == MassMomentOfInertiaUnits.MilliGramSquareMillimeter:
            return ((value * 1e9) / 0.001)
        
        if from_unit == MassMomentOfInertiaUnits.KiloGramSquareMillimeter:
            return ((value * 1e9) / 1000.0)
        
        if from_unit == MassMomentOfInertiaUnits.KiloTonneSquareMeter:
            return ((value * 1e-3) / 1000.0)
        
        if from_unit == MassMomentOfInertiaUnits.MegaTonneSquareMeter:
            return ((value * 1e-3) / 1000000.0)
        
        if from_unit == MassMomentOfInertiaUnits.KiloTonneSquareDecimeter:
            return ((value * 1e-1) / 1000.0)
        
        if from_unit == MassMomentOfInertiaUnits.MegaTonneSquareDecimeter:
            return ((value * 1e-1) / 1000000.0)
        
        if from_unit == MassMomentOfInertiaUnits.KiloTonneSquareCentimeter:
            return ((value * 1e1) / 1000.0)
        
        if from_unit == MassMomentOfInertiaUnits.MegaTonneSquareCentimeter:
            return ((value * 1e1) / 1000000.0)
        
        if from_unit == MassMomentOfInertiaUnits.KiloTonneSquareMilimeter:
            return ((value * 1e3) / 1000.0)
        
        if from_unit == MassMomentOfInertiaUnits.MegaTonneSquareMilimeter:
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
        
        if to_unit == MassMomentOfInertiaUnits.MilliGramSquareMeter:
            return ((value / 1e3) * 0.001)
        
        if to_unit == MassMomentOfInertiaUnits.KiloGramSquareMeter:
            return ((value / 1e3) * 1000.0)
        
        if to_unit == MassMomentOfInertiaUnits.MilliGramSquareDecimeter:
            return ((value / 1e5) * 0.001)
        
        if to_unit == MassMomentOfInertiaUnits.KiloGramSquareDecimeter:
            return ((value / 1e5) * 1000.0)
        
        if to_unit == MassMomentOfInertiaUnits.MilliGramSquareCentimeter:
            return ((value / 1e7) * 0.001)
        
        if to_unit == MassMomentOfInertiaUnits.KiloGramSquareCentimeter:
            return ((value / 1e7) * 1000.0)
        
        if to_unit == MassMomentOfInertiaUnits.MilliGramSquareMillimeter:
            return ((value / 1e9) * 0.001)
        
        if to_unit == MassMomentOfInertiaUnits.KiloGramSquareMillimeter:
            return ((value / 1e9) * 1000.0)
        
        if to_unit == MassMomentOfInertiaUnits.KiloTonneSquareMeter:
            return ((value / 1e-3) * 1000.0)
        
        if to_unit == MassMomentOfInertiaUnits.MegaTonneSquareMeter:
            return ((value / 1e-3) * 1000000.0)
        
        if to_unit == MassMomentOfInertiaUnits.KiloTonneSquareDecimeter:
            return ((value / 1e-1) * 1000.0)
        
        if to_unit == MassMomentOfInertiaUnits.MegaTonneSquareDecimeter:
            return ((value / 1e-1) * 1000000.0)
        
        if to_unit == MassMomentOfInertiaUnits.KiloTonneSquareCentimeter:
            return ((value / 1e1) * 1000.0)
        
        if to_unit == MassMomentOfInertiaUnits.MegaTonneSquareCentimeter:
            return ((value / 1e1) * 1000000.0)
        
        if to_unit == MassMomentOfInertiaUnits.KiloTonneSquareMilimeter:
            return ((value / 1e3) * 1000.0)
        
        if to_unit == MassMomentOfInertiaUnits.MegaTonneSquareMilimeter:
            return ((value / 1e3) * 1000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
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
    def from_milli_gram_square_meters(milli_gram_square_meters: float):
        """
        Create a new instance of MassMomentOfInertia from a value in milli_gram_square_meters.

        

        :param meters: The MassMomentOfInertia value in milli_gram_square_meters.
        :type milli_gram_square_meters: float
        :return: A new instance of MassMomentOfInertia.
        :rtype: MassMomentOfInertia
        """
        return MassMomentOfInertia(milli_gram_square_meters, MassMomentOfInertiaUnits.MilliGramSquareMeter)

    
    @staticmethod
    def from_kilo_gram_square_meters(kilo_gram_square_meters: float):
        """
        Create a new instance of MassMomentOfInertia from a value in kilo_gram_square_meters.

        

        :param meters: The MassMomentOfInertia value in kilo_gram_square_meters.
        :type kilo_gram_square_meters: float
        :return: A new instance of MassMomentOfInertia.
        :rtype: MassMomentOfInertia
        """
        return MassMomentOfInertia(kilo_gram_square_meters, MassMomentOfInertiaUnits.KiloGramSquareMeter)

    
    @staticmethod
    def from_milli_gram_square_decimeters(milli_gram_square_decimeters: float):
        """
        Create a new instance of MassMomentOfInertia from a value in milli_gram_square_decimeters.

        

        :param meters: The MassMomentOfInertia value in milli_gram_square_decimeters.
        :type milli_gram_square_decimeters: float
        :return: A new instance of MassMomentOfInertia.
        :rtype: MassMomentOfInertia
        """
        return MassMomentOfInertia(milli_gram_square_decimeters, MassMomentOfInertiaUnits.MilliGramSquareDecimeter)

    
    @staticmethod
    def from_kilo_gram_square_decimeters(kilo_gram_square_decimeters: float):
        """
        Create a new instance of MassMomentOfInertia from a value in kilo_gram_square_decimeters.

        

        :param meters: The MassMomentOfInertia value in kilo_gram_square_decimeters.
        :type kilo_gram_square_decimeters: float
        :return: A new instance of MassMomentOfInertia.
        :rtype: MassMomentOfInertia
        """
        return MassMomentOfInertia(kilo_gram_square_decimeters, MassMomentOfInertiaUnits.KiloGramSquareDecimeter)

    
    @staticmethod
    def from_milli_gram_square_centimeters(milli_gram_square_centimeters: float):
        """
        Create a new instance of MassMomentOfInertia from a value in milli_gram_square_centimeters.

        

        :param meters: The MassMomentOfInertia value in milli_gram_square_centimeters.
        :type milli_gram_square_centimeters: float
        :return: A new instance of MassMomentOfInertia.
        :rtype: MassMomentOfInertia
        """
        return MassMomentOfInertia(milli_gram_square_centimeters, MassMomentOfInertiaUnits.MilliGramSquareCentimeter)

    
    @staticmethod
    def from_kilo_gram_square_centimeters(kilo_gram_square_centimeters: float):
        """
        Create a new instance of MassMomentOfInertia from a value in kilo_gram_square_centimeters.

        

        :param meters: The MassMomentOfInertia value in kilo_gram_square_centimeters.
        :type kilo_gram_square_centimeters: float
        :return: A new instance of MassMomentOfInertia.
        :rtype: MassMomentOfInertia
        """
        return MassMomentOfInertia(kilo_gram_square_centimeters, MassMomentOfInertiaUnits.KiloGramSquareCentimeter)

    
    @staticmethod
    def from_milli_gram_square_millimeters(milli_gram_square_millimeters: float):
        """
        Create a new instance of MassMomentOfInertia from a value in milli_gram_square_millimeters.

        

        :param meters: The MassMomentOfInertia value in milli_gram_square_millimeters.
        :type milli_gram_square_millimeters: float
        :return: A new instance of MassMomentOfInertia.
        :rtype: MassMomentOfInertia
        """
        return MassMomentOfInertia(milli_gram_square_millimeters, MassMomentOfInertiaUnits.MilliGramSquareMillimeter)

    
    @staticmethod
    def from_kilo_gram_square_millimeters(kilo_gram_square_millimeters: float):
        """
        Create a new instance of MassMomentOfInertia from a value in kilo_gram_square_millimeters.

        

        :param meters: The MassMomentOfInertia value in kilo_gram_square_millimeters.
        :type kilo_gram_square_millimeters: float
        :return: A new instance of MassMomentOfInertia.
        :rtype: MassMomentOfInertia
        """
        return MassMomentOfInertia(kilo_gram_square_millimeters, MassMomentOfInertiaUnits.KiloGramSquareMillimeter)

    
    @staticmethod
    def from_kilo_tonne_square_meters(kilo_tonne_square_meters: float):
        """
        Create a new instance of MassMomentOfInertia from a value in kilo_tonne_square_meters.

        

        :param meters: The MassMomentOfInertia value in kilo_tonne_square_meters.
        :type kilo_tonne_square_meters: float
        :return: A new instance of MassMomentOfInertia.
        :rtype: MassMomentOfInertia
        """
        return MassMomentOfInertia(kilo_tonne_square_meters, MassMomentOfInertiaUnits.KiloTonneSquareMeter)

    
    @staticmethod
    def from_mega_tonne_square_meters(mega_tonne_square_meters: float):
        """
        Create a new instance of MassMomentOfInertia from a value in mega_tonne_square_meters.

        

        :param meters: The MassMomentOfInertia value in mega_tonne_square_meters.
        :type mega_tonne_square_meters: float
        :return: A new instance of MassMomentOfInertia.
        :rtype: MassMomentOfInertia
        """
        return MassMomentOfInertia(mega_tonne_square_meters, MassMomentOfInertiaUnits.MegaTonneSquareMeter)

    
    @staticmethod
    def from_kilo_tonne_square_decimeters(kilo_tonne_square_decimeters: float):
        """
        Create a new instance of MassMomentOfInertia from a value in kilo_tonne_square_decimeters.

        

        :param meters: The MassMomentOfInertia value in kilo_tonne_square_decimeters.
        :type kilo_tonne_square_decimeters: float
        :return: A new instance of MassMomentOfInertia.
        :rtype: MassMomentOfInertia
        """
        return MassMomentOfInertia(kilo_tonne_square_decimeters, MassMomentOfInertiaUnits.KiloTonneSquareDecimeter)

    
    @staticmethod
    def from_mega_tonne_square_decimeters(mega_tonne_square_decimeters: float):
        """
        Create a new instance of MassMomentOfInertia from a value in mega_tonne_square_decimeters.

        

        :param meters: The MassMomentOfInertia value in mega_tonne_square_decimeters.
        :type mega_tonne_square_decimeters: float
        :return: A new instance of MassMomentOfInertia.
        :rtype: MassMomentOfInertia
        """
        return MassMomentOfInertia(mega_tonne_square_decimeters, MassMomentOfInertiaUnits.MegaTonneSquareDecimeter)

    
    @staticmethod
    def from_kilo_tonne_square_centimeters(kilo_tonne_square_centimeters: float):
        """
        Create a new instance of MassMomentOfInertia from a value in kilo_tonne_square_centimeters.

        

        :param meters: The MassMomentOfInertia value in kilo_tonne_square_centimeters.
        :type kilo_tonne_square_centimeters: float
        :return: A new instance of MassMomentOfInertia.
        :rtype: MassMomentOfInertia
        """
        return MassMomentOfInertia(kilo_tonne_square_centimeters, MassMomentOfInertiaUnits.KiloTonneSquareCentimeter)

    
    @staticmethod
    def from_mega_tonne_square_centimeters(mega_tonne_square_centimeters: float):
        """
        Create a new instance of MassMomentOfInertia from a value in mega_tonne_square_centimeters.

        

        :param meters: The MassMomentOfInertia value in mega_tonne_square_centimeters.
        :type mega_tonne_square_centimeters: float
        :return: A new instance of MassMomentOfInertia.
        :rtype: MassMomentOfInertia
        """
        return MassMomentOfInertia(mega_tonne_square_centimeters, MassMomentOfInertiaUnits.MegaTonneSquareCentimeter)

    
    @staticmethod
    def from_kilo_tonne_square_milimeters(kilo_tonne_square_milimeters: float):
        """
        Create a new instance of MassMomentOfInertia from a value in kilo_tonne_square_milimeters.

        

        :param meters: The MassMomentOfInertia value in kilo_tonne_square_milimeters.
        :type kilo_tonne_square_milimeters: float
        :return: A new instance of MassMomentOfInertia.
        :rtype: MassMomentOfInertia
        """
        return MassMomentOfInertia(kilo_tonne_square_milimeters, MassMomentOfInertiaUnits.KiloTonneSquareMilimeter)

    
    @staticmethod
    def from_mega_tonne_square_milimeters(mega_tonne_square_milimeters: float):
        """
        Create a new instance of MassMomentOfInertia from a value in mega_tonne_square_milimeters.

        

        :param meters: The MassMomentOfInertia value in mega_tonne_square_milimeters.
        :type mega_tonne_square_milimeters: float
        :return: A new instance of MassMomentOfInertia.
        :rtype: MassMomentOfInertia
        """
        return MassMomentOfInertia(mega_tonne_square_milimeters, MassMomentOfInertiaUnits.MegaTonneSquareMilimeter)

    
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
    def milli_gram_square_meters(self) -> float:
        """
        
        """
        if self.__milli_gram_square_meters != None:
            return self.__milli_gram_square_meters
        self.__milli_gram_square_meters = self.__convert_from_base(MassMomentOfInertiaUnits.MilliGramSquareMeter)
        return self.__milli_gram_square_meters

    
    @property
    def kilo_gram_square_meters(self) -> float:
        """
        
        """
        if self.__kilo_gram_square_meters != None:
            return self.__kilo_gram_square_meters
        self.__kilo_gram_square_meters = self.__convert_from_base(MassMomentOfInertiaUnits.KiloGramSquareMeter)
        return self.__kilo_gram_square_meters

    
    @property
    def milli_gram_square_decimeters(self) -> float:
        """
        
        """
        if self.__milli_gram_square_decimeters != None:
            return self.__milli_gram_square_decimeters
        self.__milli_gram_square_decimeters = self.__convert_from_base(MassMomentOfInertiaUnits.MilliGramSquareDecimeter)
        return self.__milli_gram_square_decimeters

    
    @property
    def kilo_gram_square_decimeters(self) -> float:
        """
        
        """
        if self.__kilo_gram_square_decimeters != None:
            return self.__kilo_gram_square_decimeters
        self.__kilo_gram_square_decimeters = self.__convert_from_base(MassMomentOfInertiaUnits.KiloGramSquareDecimeter)
        return self.__kilo_gram_square_decimeters

    
    @property
    def milli_gram_square_centimeters(self) -> float:
        """
        
        """
        if self.__milli_gram_square_centimeters != None:
            return self.__milli_gram_square_centimeters
        self.__milli_gram_square_centimeters = self.__convert_from_base(MassMomentOfInertiaUnits.MilliGramSquareCentimeter)
        return self.__milli_gram_square_centimeters

    
    @property
    def kilo_gram_square_centimeters(self) -> float:
        """
        
        """
        if self.__kilo_gram_square_centimeters != None:
            return self.__kilo_gram_square_centimeters
        self.__kilo_gram_square_centimeters = self.__convert_from_base(MassMomentOfInertiaUnits.KiloGramSquareCentimeter)
        return self.__kilo_gram_square_centimeters

    
    @property
    def milli_gram_square_millimeters(self) -> float:
        """
        
        """
        if self.__milli_gram_square_millimeters != None:
            return self.__milli_gram_square_millimeters
        self.__milli_gram_square_millimeters = self.__convert_from_base(MassMomentOfInertiaUnits.MilliGramSquareMillimeter)
        return self.__milli_gram_square_millimeters

    
    @property
    def kilo_gram_square_millimeters(self) -> float:
        """
        
        """
        if self.__kilo_gram_square_millimeters != None:
            return self.__kilo_gram_square_millimeters
        self.__kilo_gram_square_millimeters = self.__convert_from_base(MassMomentOfInertiaUnits.KiloGramSquareMillimeter)
        return self.__kilo_gram_square_millimeters

    
    @property
    def kilo_tonne_square_meters(self) -> float:
        """
        
        """
        if self.__kilo_tonne_square_meters != None:
            return self.__kilo_tonne_square_meters
        self.__kilo_tonne_square_meters = self.__convert_from_base(MassMomentOfInertiaUnits.KiloTonneSquareMeter)
        return self.__kilo_tonne_square_meters

    
    @property
    def mega_tonne_square_meters(self) -> float:
        """
        
        """
        if self.__mega_tonne_square_meters != None:
            return self.__mega_tonne_square_meters
        self.__mega_tonne_square_meters = self.__convert_from_base(MassMomentOfInertiaUnits.MegaTonneSquareMeter)
        return self.__mega_tonne_square_meters

    
    @property
    def kilo_tonne_square_decimeters(self) -> float:
        """
        
        """
        if self.__kilo_tonne_square_decimeters != None:
            return self.__kilo_tonne_square_decimeters
        self.__kilo_tonne_square_decimeters = self.__convert_from_base(MassMomentOfInertiaUnits.KiloTonneSquareDecimeter)
        return self.__kilo_tonne_square_decimeters

    
    @property
    def mega_tonne_square_decimeters(self) -> float:
        """
        
        """
        if self.__mega_tonne_square_decimeters != None:
            return self.__mega_tonne_square_decimeters
        self.__mega_tonne_square_decimeters = self.__convert_from_base(MassMomentOfInertiaUnits.MegaTonneSquareDecimeter)
        return self.__mega_tonne_square_decimeters

    
    @property
    def kilo_tonne_square_centimeters(self) -> float:
        """
        
        """
        if self.__kilo_tonne_square_centimeters != None:
            return self.__kilo_tonne_square_centimeters
        self.__kilo_tonne_square_centimeters = self.__convert_from_base(MassMomentOfInertiaUnits.KiloTonneSquareCentimeter)
        return self.__kilo_tonne_square_centimeters

    
    @property
    def mega_tonne_square_centimeters(self) -> float:
        """
        
        """
        if self.__mega_tonne_square_centimeters != None:
            return self.__mega_tonne_square_centimeters
        self.__mega_tonne_square_centimeters = self.__convert_from_base(MassMomentOfInertiaUnits.MegaTonneSquareCentimeter)
        return self.__mega_tonne_square_centimeters

    
    @property
    def kilo_tonne_square_milimeters(self) -> float:
        """
        
        """
        if self.__kilo_tonne_square_milimeters != None:
            return self.__kilo_tonne_square_milimeters
        self.__kilo_tonne_square_milimeters = self.__convert_from_base(MassMomentOfInertiaUnits.KiloTonneSquareMilimeter)
        return self.__kilo_tonne_square_milimeters

    
    @property
    def mega_tonne_square_milimeters(self) -> float:
        """
        
        """
        if self.__mega_tonne_square_milimeters != None:
            return self.__mega_tonne_square_milimeters
        self.__mega_tonne_square_milimeters = self.__convert_from_base(MassMomentOfInertiaUnits.MegaTonneSquareMilimeter)
        return self.__mega_tonne_square_milimeters

    
    def to_string(self, unit: MassMomentOfInertiaUnits = MassMomentOfInertiaUnits.KilogramSquareMeter) -> string:
        """
        Format the MassMomentOfInertia to string.
        Note! the default format for MassMomentOfInertia is KilogramSquareMeter.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == MassMomentOfInertiaUnits.GramSquareMeter:
            return f"""{self.gram_square_meters} g·m²"""
        
        if unit == MassMomentOfInertiaUnits.GramSquareDecimeter:
            return f"""{self.gram_square_decimeters} g·dm²"""
        
        if unit == MassMomentOfInertiaUnits.GramSquareCentimeter:
            return f"""{self.gram_square_centimeters} g·cm²"""
        
        if unit == MassMomentOfInertiaUnits.GramSquareMillimeter:
            return f"""{self.gram_square_millimeters} g·mm²"""
        
        if unit == MassMomentOfInertiaUnits.TonneSquareMeter:
            return f"""{self.tonne_square_meters} t·m²"""
        
        if unit == MassMomentOfInertiaUnits.TonneSquareDecimeter:
            return f"""{self.tonne_square_decimeters} t·dm²"""
        
        if unit == MassMomentOfInertiaUnits.TonneSquareCentimeter:
            return f"""{self.tonne_square_centimeters} t·cm²"""
        
        if unit == MassMomentOfInertiaUnits.TonneSquareMilimeter:
            return f"""{self.tonne_square_milimeters} t·mm²"""
        
        if unit == MassMomentOfInertiaUnits.PoundSquareFoot:
            return f"""{self.pound_square_feet} lb·ft²"""
        
        if unit == MassMomentOfInertiaUnits.PoundSquareInch:
            return f"""{self.pound_square_inches} lb·in²"""
        
        if unit == MassMomentOfInertiaUnits.SlugSquareFoot:
            return f"""{self.slug_square_feet} slug·ft²"""
        
        if unit == MassMomentOfInertiaUnits.SlugSquareInch:
            return f"""{self.slug_square_inches} slug·in²"""
        
        if unit == MassMomentOfInertiaUnits.MilliGramSquareMeter:
            return f"""{self.milli_gram_square_meters} """
        
        if unit == MassMomentOfInertiaUnits.KiloGramSquareMeter:
            return f"""{self.kilo_gram_square_meters} """
        
        if unit == MassMomentOfInertiaUnits.MilliGramSquareDecimeter:
            return f"""{self.milli_gram_square_decimeters} """
        
        if unit == MassMomentOfInertiaUnits.KiloGramSquareDecimeter:
            return f"""{self.kilo_gram_square_decimeters} """
        
        if unit == MassMomentOfInertiaUnits.MilliGramSquareCentimeter:
            return f"""{self.milli_gram_square_centimeters} """
        
        if unit == MassMomentOfInertiaUnits.KiloGramSquareCentimeter:
            return f"""{self.kilo_gram_square_centimeters} """
        
        if unit == MassMomentOfInertiaUnits.MilliGramSquareMillimeter:
            return f"""{self.milli_gram_square_millimeters} """
        
        if unit == MassMomentOfInertiaUnits.KiloGramSquareMillimeter:
            return f"""{self.kilo_gram_square_millimeters} """
        
        if unit == MassMomentOfInertiaUnits.KiloTonneSquareMeter:
            return f"""{self.kilo_tonne_square_meters} """
        
        if unit == MassMomentOfInertiaUnits.MegaTonneSquareMeter:
            return f"""{self.mega_tonne_square_meters} """
        
        if unit == MassMomentOfInertiaUnits.KiloTonneSquareDecimeter:
            return f"""{self.kilo_tonne_square_decimeters} """
        
        if unit == MassMomentOfInertiaUnits.MegaTonneSquareDecimeter:
            return f"""{self.mega_tonne_square_decimeters} """
        
        if unit == MassMomentOfInertiaUnits.KiloTonneSquareCentimeter:
            return f"""{self.kilo_tonne_square_centimeters} """
        
        if unit == MassMomentOfInertiaUnits.MegaTonneSquareCentimeter:
            return f"""{self.mega_tonne_square_centimeters} """
        
        if unit == MassMomentOfInertiaUnits.KiloTonneSquareMilimeter:
            return f"""{self.kilo_tonne_square_milimeters} """
        
        if unit == MassMomentOfInertiaUnits.MegaTonneSquareMilimeter:
            return f"""{self.mega_tonne_square_milimeters} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: MassMomentOfInertiaUnits = MassMomentOfInertiaUnits.KilogramSquareMeter) -> string:
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
        
        if unit_abbreviation == MassMomentOfInertiaUnits.MilliGramSquareMeter:
            return """"""
        
        if unit_abbreviation == MassMomentOfInertiaUnits.KiloGramSquareMeter:
            return """"""
        
        if unit_abbreviation == MassMomentOfInertiaUnits.MilliGramSquareDecimeter:
            return """"""
        
        if unit_abbreviation == MassMomentOfInertiaUnits.KiloGramSquareDecimeter:
            return """"""
        
        if unit_abbreviation == MassMomentOfInertiaUnits.MilliGramSquareCentimeter:
            return """"""
        
        if unit_abbreviation == MassMomentOfInertiaUnits.KiloGramSquareCentimeter:
            return """"""
        
        if unit_abbreviation == MassMomentOfInertiaUnits.MilliGramSquareMillimeter:
            return """"""
        
        if unit_abbreviation == MassMomentOfInertiaUnits.KiloGramSquareMillimeter:
            return """"""
        
        if unit_abbreviation == MassMomentOfInertiaUnits.KiloTonneSquareMeter:
            return """"""
        
        if unit_abbreviation == MassMomentOfInertiaUnits.MegaTonneSquareMeter:
            return """"""
        
        if unit_abbreviation == MassMomentOfInertiaUnits.KiloTonneSquareDecimeter:
            return """"""
        
        if unit_abbreviation == MassMomentOfInertiaUnits.MegaTonneSquareDecimeter:
            return """"""
        
        if unit_abbreviation == MassMomentOfInertiaUnits.KiloTonneSquareCentimeter:
            return """"""
        
        if unit_abbreviation == MassMomentOfInertiaUnits.MegaTonneSquareCentimeter:
            return """"""
        
        if unit_abbreviation == MassMomentOfInertiaUnits.KiloTonneSquareMilimeter:
            return """"""
        
        if unit_abbreviation == MassMomentOfInertiaUnits.MegaTonneSquareMilimeter:
            return """"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, MassMomentOfInertia):
            raise TypeError("unsupported operand type(s) for +: 'MassMomentOfInertia' and '{}'".format(type(other).__name__))
        return MassMomentOfInertia(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, MassMomentOfInertia):
            raise TypeError("unsupported operand type(s) for *: 'MassMomentOfInertia' and '{}'".format(type(other).__name__))
        return MassMomentOfInertia(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, MassMomentOfInertia):
            raise TypeError("unsupported operand type(s) for -: 'MassMomentOfInertia' and '{}'".format(type(other).__name__))
        return MassMomentOfInertia(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, MassMomentOfInertia):
            raise TypeError("unsupported operand type(s) for /: 'MassMomentOfInertia' and '{}'".format(type(other).__name__))
        return MassMomentOfInertia(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, MassMomentOfInertia):
            raise TypeError("unsupported operand type(s) for %: 'MassMomentOfInertia' and '{}'".format(type(other).__name__))
        return MassMomentOfInertia(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, MassMomentOfInertia):
            raise TypeError("unsupported operand type(s) for **: 'MassMomentOfInertia' and '{}'".format(type(other).__name__))
        return MassMomentOfInertia(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, MassMomentOfInertia):
            raise TypeError("unsupported operand type(s) for ==: 'MassMomentOfInertia' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, MassMomentOfInertia):
            raise TypeError("unsupported operand type(s) for <: 'MassMomentOfInertia' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, MassMomentOfInertia):
            raise TypeError("unsupported operand type(s) for >: 'MassMomentOfInertia' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, MassMomentOfInertia):
            raise TypeError("unsupported operand type(s) for <=: 'MassMomentOfInertia' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, MassMomentOfInertia):
            raise TypeError("unsupported operand type(s) for >=: 'MassMomentOfInertia' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value
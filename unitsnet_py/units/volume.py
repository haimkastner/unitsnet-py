from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class VolumeUnits(Enum):
        """
            VolumeUnits enumeration
        """
        
        Liter = 'liter'
        """
            
        """
        
        CubicMeter = 'cubic_meter'
        """
            
        """
        
        CubicKilometer = 'cubic_kilometer'
        """
            
        """
        
        CubicHectometer = 'cubic_hectometer'
        """
            
        """
        
        CubicDecimeter = 'cubic_decimeter'
        """
            
        """
        
        CubicCentimeter = 'cubic_centimeter'
        """
            
        """
        
        CubicMillimeter = 'cubic_millimeter'
        """
            
        """
        
        CubicMicrometer = 'cubic_micrometer'
        """
            
        """
        
        CubicMile = 'cubic_mile'
        """
            
        """
        
        CubicYard = 'cubic_yard'
        """
            
        """
        
        CubicFoot = 'cubic_foot'
        """
            
        """
        
        CubicInch = 'cubic_inch'
        """
            
        """
        
        ImperialGallon = 'imperial_gallon'
        """
            The British imperial gallon (frequently called simply "gallon") is defined as exactly 4.54609 litres.
        """
        
        ImperialOunce = 'imperial_ounce'
        """
            
        """
        
        UsGallon = 'us_gallon'
        """
            The US liquid gallon (frequently called simply "gallon") is legally defined as 231 cubic inches, which is exactly 3.785411784 litres.
        """
        
        UsOunce = 'us_ounce'
        """
            
        """
        
        UsTablespoon = 'us_tablespoon'
        """
            
        """
        
        AuTablespoon = 'au_tablespoon'
        """
            
        """
        
        UkTablespoon = 'uk_tablespoon'
        """
            
        """
        
        MetricTeaspoon = 'metric_teaspoon'
        """
            
        """
        
        UsTeaspoon = 'us_teaspoon'
        """
            
        """
        
        MetricCup = 'metric_cup'
        """
            
        """
        
        UsCustomaryCup = 'us_customary_cup'
        """
            
        """
        
        UsLegalCup = 'us_legal_cup'
        """
            
        """
        
        OilBarrel = 'oil_barrel'
        """
            
        """
        
        UsBeerBarrel = 'us_beer_barrel'
        """
            
        """
        
        ImperialBeerBarrel = 'imperial_beer_barrel'
        """
            
        """
        
        UsQuart = 'us_quart'
        """
            
        """
        
        ImperialQuart = 'imperial_quart'
        """
            
        """
        
        UsPint = 'us_pint'
        """
            
        """
        
        AcreFoot = 'acre_foot'
        """
            
        """
        
        ImperialPint = 'imperial_pint'
        """
            
        """
        
        BoardFoot = 'board_foot'
        """
            
        """
        
        Nanoliter = 'nanoliter'
        """
            
        """
        
        Microliter = 'microliter'
        """
            
        """
        
        Milliliter = 'milliliter'
        """
            
        """
        
        Centiliter = 'centiliter'
        """
            
        """
        
        Deciliter = 'deciliter'
        """
            
        """
        
        Decaliter = 'decaliter'
        """
            
        """
        
        Hectoliter = 'hectoliter'
        """
            
        """
        
        Kiloliter = 'kiloliter'
        """
            
        """
        
        Megaliter = 'megaliter'
        """
            
        """
        
        HectocubicMeter = 'hectocubic_meter'
        """
            
        """
        
        KilocubicMeter = 'kilocubic_meter'
        """
            
        """
        
        HectocubicFoot = 'hectocubic_foot'
        """
            
        """
        
        KilocubicFoot = 'kilocubic_foot'
        """
            
        """
        
        MegacubicFoot = 'megacubic_foot'
        """
            
        """
        
        KiloimperialGallon = 'kiloimperial_gallon'
        """
            
        """
        
        MegaimperialGallon = 'megaimperial_gallon'
        """
            
        """
        
        DecausGallon = 'decaus_gallon'
        """
            
        """
        
        DeciusGallon = 'decius_gallon'
        """
            
        """
        
        HectousGallon = 'hectous_gallon'
        """
            
        """
        
        KilousGallon = 'kilous_gallon'
        """
            
        """
        
        MegausGallon = 'megaus_gallon'
        """
            
        """
        

class Volume(AbstractMeasure):
    """
    Volume is the quantity of three-dimensional space enclosed by some closed boundary, for example, the space that a substance (solid, liquid, gas, or plasma) or shape occupies or contains.[1] Volume is often quantified numerically using the SI derived unit, the cubic metre. The volume of a container is generally understood to be the capacity of the container, i. e. the amount of fluid (gas or liquid) that the container could hold, rather than the amount of space the container itself displaces.

    Args:
        value (float): The value.
        from_unit (VolumeUnits): The Volume unit to create from, The default unit is CubicMeter
    """
    def __init__(self, value: float, from_unit: VolumeUnits = VolumeUnits.CubicMeter):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__liters = None
        
        self.__cubic_meters = None
        
        self.__cubic_kilometers = None
        
        self.__cubic_hectometers = None
        
        self.__cubic_decimeters = None
        
        self.__cubic_centimeters = None
        
        self.__cubic_millimeters = None
        
        self.__cubic_micrometers = None
        
        self.__cubic_miles = None
        
        self.__cubic_yards = None
        
        self.__cubic_feet = None
        
        self.__cubic_inches = None
        
        self.__imperial_gallons = None
        
        self.__imperial_ounces = None
        
        self.__us_gallons = None
        
        self.__us_ounces = None
        
        self.__us_tablespoons = None
        
        self.__au_tablespoons = None
        
        self.__uk_tablespoons = None
        
        self.__metric_teaspoons = None
        
        self.__us_teaspoons = None
        
        self.__metric_cups = None
        
        self.__us_customary_cups = None
        
        self.__us_legal_cups = None
        
        self.__oil_barrels = None
        
        self.__us_beer_barrels = None
        
        self.__imperial_beer_barrels = None
        
        self.__us_quarts = None
        
        self.__imperial_quarts = None
        
        self.__us_pints = None
        
        self.__acre_feet = None
        
        self.__imperial_pints = None
        
        self.__board_feet = None
        
        self.__nanoliters = None
        
        self.__microliters = None
        
        self.__milliliters = None
        
        self.__centiliters = None
        
        self.__deciliters = None
        
        self.__decaliters = None
        
        self.__hectoliters = None
        
        self.__kiloliters = None
        
        self.__megaliters = None
        
        self.__hectocubic_meters = None
        
        self.__kilocubic_meters = None
        
        self.__hectocubic_feet = None
        
        self.__kilocubic_feet = None
        
        self.__megacubic_feet = None
        
        self.__kiloimperial_gallons = None
        
        self.__megaimperial_gallons = None
        
        self.__decaus_gallons = None
        
        self.__decius_gallons = None
        
        self.__hectous_gallons = None
        
        self.__kilous_gallons = None
        
        self.__megaus_gallons = None
        

    def convert(self, unit: VolumeUnits) -> float:
        return self.__convert_from_base(unit)

    def __convert_from_base(self, from_unit: VolumeUnits) -> float:
        value = self._value
        
        if from_unit == VolumeUnits.Liter:
            return (value * 1e3)
        
        if from_unit == VolumeUnits.CubicMeter:
            return (value)
        
        if from_unit == VolumeUnits.CubicKilometer:
            return (value / 1e9)
        
        if from_unit == VolumeUnits.CubicHectometer:
            return (value / 1e6)
        
        if from_unit == VolumeUnits.CubicDecimeter:
            return (value * 1e3)
        
        if from_unit == VolumeUnits.CubicCentimeter:
            return (value * 1e6)
        
        if from_unit == VolumeUnits.CubicMillimeter:
            return (value * 1e9)
        
        if from_unit == VolumeUnits.CubicMicrometer:
            return (value * 1e18)
        
        if from_unit == VolumeUnits.CubicMile:
            return (value / 4.16818182544058e9)
        
        if from_unit == VolumeUnits.CubicYard:
            return (value / 0.764554858)
        
        if from_unit == VolumeUnits.CubicFoot:
            return (value / 2.8316846592e-2)
        
        if from_unit == VolumeUnits.CubicInch:
            return (value / 1.6387064e-5)
        
        if from_unit == VolumeUnits.ImperialGallon:
            return (value / 0.00454609)
        
        if from_unit == VolumeUnits.ImperialOunce:
            return (value / 2.8413062499962901241875439064617e-5)
        
        if from_unit == VolumeUnits.UsGallon:
            return (value / 0.003785411784)
        
        if from_unit == VolumeUnits.UsOunce:
            return (value / 2.957352956253760505068307980135e-5)
        
        if from_unit == VolumeUnits.UsTablespoon:
            return (value / 1.478676478125e-5)
        
        if from_unit == VolumeUnits.AuTablespoon:
            return (value / 2e-5)
        
        if from_unit == VolumeUnits.UkTablespoon:
            return (value / 1.5e-5)
        
        if from_unit == VolumeUnits.MetricTeaspoon:
            return (value / 0.5e-5)
        
        if from_unit == VolumeUnits.UsTeaspoon:
            return (value / 4.92892159375e-6)
        
        if from_unit == VolumeUnits.MetricCup:
            return (value / 0.00025)
        
        if from_unit == VolumeUnits.UsCustomaryCup:
            return (value / 0.0002365882365)
        
        if from_unit == VolumeUnits.UsLegalCup:
            return (value / 0.00024)
        
        if from_unit == VolumeUnits.OilBarrel:
            return (value / 0.158987294928)
        
        if from_unit == VolumeUnits.UsBeerBarrel:
            return (value / 0.1173477658)
        
        if from_unit == VolumeUnits.ImperialBeerBarrel:
            return (value / 0.16365924)
        
        if from_unit == VolumeUnits.UsQuart:
            return (value / 9.46352946e-4)
        
        if from_unit == VolumeUnits.ImperialQuart:
            return (value / 1.1365225e-3)
        
        if from_unit == VolumeUnits.UsPint:
            return (value / 4.73176473e-4)
        
        if from_unit == VolumeUnits.AcreFoot:
            return (value * 0.000810714)
        
        if from_unit == VolumeUnits.ImperialPint:
            return (value / 5.6826125e-4)
        
        if from_unit == VolumeUnits.BoardFoot:
            return (value / 2.3597372158e-3)
        
        if from_unit == VolumeUnits.Nanoliter:
            return ((value * 1e3) / 1e-09)
        
        if from_unit == VolumeUnits.Microliter:
            return ((value * 1e3) / 1e-06)
        
        if from_unit == VolumeUnits.Milliliter:
            return ((value * 1e3) / 0.001)
        
        if from_unit == VolumeUnits.Centiliter:
            return ((value * 1e3) / 0.01)
        
        if from_unit == VolumeUnits.Deciliter:
            return ((value * 1e3) / 0.1)
        
        if from_unit == VolumeUnits.Decaliter:
            return ((value * 1e3) / 10.0)
        
        if from_unit == VolumeUnits.Hectoliter:
            return ((value * 1e3) / 100.0)
        
        if from_unit == VolumeUnits.Kiloliter:
            return ((value * 1e3) / 1000.0)
        
        if from_unit == VolumeUnits.Megaliter:
            return ((value * 1e3) / 1000000.0)
        
        if from_unit == VolumeUnits.HectocubicMeter:
            return ((value) / 100.0)
        
        if from_unit == VolumeUnits.KilocubicMeter:
            return ((value) / 1000.0)
        
        if from_unit == VolumeUnits.HectocubicFoot:
            return ((value / 2.8316846592e-2) / 100.0)
        
        if from_unit == VolumeUnits.KilocubicFoot:
            return ((value / 2.8316846592e-2) / 1000.0)
        
        if from_unit == VolumeUnits.MegacubicFoot:
            return ((value / 2.8316846592e-2) / 1000000.0)
        
        if from_unit == VolumeUnits.KiloimperialGallon:
            return ((value / 0.00454609) / 1000.0)
        
        if from_unit == VolumeUnits.MegaimperialGallon:
            return ((value / 0.00454609) / 1000000.0)
        
        if from_unit == VolumeUnits.DecausGallon:
            return ((value / 0.003785411784) / 10.0)
        
        if from_unit == VolumeUnits.DeciusGallon:
            return ((value / 0.003785411784) / 0.1)
        
        if from_unit == VolumeUnits.HectousGallon:
            return ((value / 0.003785411784) / 100.0)
        
        if from_unit == VolumeUnits.KilousGallon:
            return ((value / 0.003785411784) / 1000.0)
        
        if from_unit == VolumeUnits.MegausGallon:
            return ((value / 0.003785411784) / 1000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: VolumeUnits) -> float:
        
        if to_unit == VolumeUnits.Liter:
            return (value / 1e3)
        
        if to_unit == VolumeUnits.CubicMeter:
            return (value)
        
        if to_unit == VolumeUnits.CubicKilometer:
            return (value * 1e9)
        
        if to_unit == VolumeUnits.CubicHectometer:
            return (value * 1e6)
        
        if to_unit == VolumeUnits.CubicDecimeter:
            return (value / 1e3)
        
        if to_unit == VolumeUnits.CubicCentimeter:
            return (value / 1e6)
        
        if to_unit == VolumeUnits.CubicMillimeter:
            return (value / 1e9)
        
        if to_unit == VolumeUnits.CubicMicrometer:
            return (value / 1e18)
        
        if to_unit == VolumeUnits.CubicMile:
            return (value * 4.16818182544058e9)
        
        if to_unit == VolumeUnits.CubicYard:
            return (value * 0.764554858)
        
        if to_unit == VolumeUnits.CubicFoot:
            return (value * 2.8316846592e-2)
        
        if to_unit == VolumeUnits.CubicInch:
            return (value * 1.6387064e-5)
        
        if to_unit == VolumeUnits.ImperialGallon:
            return (value * 0.00454609)
        
        if to_unit == VolumeUnits.ImperialOunce:
            return (value * 2.8413062499962901241875439064617e-5)
        
        if to_unit == VolumeUnits.UsGallon:
            return (value * 0.003785411784)
        
        if to_unit == VolumeUnits.UsOunce:
            return (value * 2.957352956253760505068307980135e-5)
        
        if to_unit == VolumeUnits.UsTablespoon:
            return (value * 1.478676478125e-5)
        
        if to_unit == VolumeUnits.AuTablespoon:
            return (value * 2e-5)
        
        if to_unit == VolumeUnits.UkTablespoon:
            return (value * 1.5e-5)
        
        if to_unit == VolumeUnits.MetricTeaspoon:
            return (value * 0.5e-5)
        
        if to_unit == VolumeUnits.UsTeaspoon:
            return (value * 4.92892159375e-6)
        
        if to_unit == VolumeUnits.MetricCup:
            return (value * 0.00025)
        
        if to_unit == VolumeUnits.UsCustomaryCup:
            return (value * 0.0002365882365)
        
        if to_unit == VolumeUnits.UsLegalCup:
            return (value * 0.00024)
        
        if to_unit == VolumeUnits.OilBarrel:
            return (value * 0.158987294928)
        
        if to_unit == VolumeUnits.UsBeerBarrel:
            return (value * 0.1173477658)
        
        if to_unit == VolumeUnits.ImperialBeerBarrel:
            return (value * 0.16365924)
        
        if to_unit == VolumeUnits.UsQuart:
            return (value * 9.46352946e-4)
        
        if to_unit == VolumeUnits.ImperialQuart:
            return (value * 1.1365225e-3)
        
        if to_unit == VolumeUnits.UsPint:
            return (value * 4.73176473e-4)
        
        if to_unit == VolumeUnits.AcreFoot:
            return (value / 0.000810714)
        
        if to_unit == VolumeUnits.ImperialPint:
            return (value * 5.6826125e-4)
        
        if to_unit == VolumeUnits.BoardFoot:
            return (value * 2.3597372158e-3)
        
        if to_unit == VolumeUnits.Nanoliter:
            return ((value / 1e3) * 1e-09)
        
        if to_unit == VolumeUnits.Microliter:
            return ((value / 1e3) * 1e-06)
        
        if to_unit == VolumeUnits.Milliliter:
            return ((value / 1e3) * 0.001)
        
        if to_unit == VolumeUnits.Centiliter:
            return ((value / 1e3) * 0.01)
        
        if to_unit == VolumeUnits.Deciliter:
            return ((value / 1e3) * 0.1)
        
        if to_unit == VolumeUnits.Decaliter:
            return ((value / 1e3) * 10.0)
        
        if to_unit == VolumeUnits.Hectoliter:
            return ((value / 1e3) * 100.0)
        
        if to_unit == VolumeUnits.Kiloliter:
            return ((value / 1e3) * 1000.0)
        
        if to_unit == VolumeUnits.Megaliter:
            return ((value / 1e3) * 1000000.0)
        
        if to_unit == VolumeUnits.HectocubicMeter:
            return ((value) * 100.0)
        
        if to_unit == VolumeUnits.KilocubicMeter:
            return ((value) * 1000.0)
        
        if to_unit == VolumeUnits.HectocubicFoot:
            return ((value * 2.8316846592e-2) * 100.0)
        
        if to_unit == VolumeUnits.KilocubicFoot:
            return ((value * 2.8316846592e-2) * 1000.0)
        
        if to_unit == VolumeUnits.MegacubicFoot:
            return ((value * 2.8316846592e-2) * 1000000.0)
        
        if to_unit == VolumeUnits.KiloimperialGallon:
            return ((value * 0.00454609) * 1000.0)
        
        if to_unit == VolumeUnits.MegaimperialGallon:
            return ((value * 0.00454609) * 1000000.0)
        
        if to_unit == VolumeUnits.DecausGallon:
            return ((value * 0.003785411784) * 10.0)
        
        if to_unit == VolumeUnits.DeciusGallon:
            return ((value * 0.003785411784) * 0.1)
        
        if to_unit == VolumeUnits.HectousGallon:
            return ((value * 0.003785411784) * 100.0)
        
        if to_unit == VolumeUnits.KilousGallon:
            return ((value * 0.003785411784) * 1000.0)
        
        if to_unit == VolumeUnits.MegausGallon:
            return ((value * 0.003785411784) * 1000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_liters(liters: float):
        """
        Create a new instance of Volume from a value in liters.

        

        :param meters: The Volume value in liters.
        :type liters: float
        :return: A new instance of Volume.
        :rtype: Volume
        """
        return Volume(liters, VolumeUnits.Liter)

    
    @staticmethod
    def from_cubic_meters(cubic_meters: float):
        """
        Create a new instance of Volume from a value in cubic_meters.

        

        :param meters: The Volume value in cubic_meters.
        :type cubic_meters: float
        :return: A new instance of Volume.
        :rtype: Volume
        """
        return Volume(cubic_meters, VolumeUnits.CubicMeter)

    
    @staticmethod
    def from_cubic_kilometers(cubic_kilometers: float):
        """
        Create a new instance of Volume from a value in cubic_kilometers.

        

        :param meters: The Volume value in cubic_kilometers.
        :type cubic_kilometers: float
        :return: A new instance of Volume.
        :rtype: Volume
        """
        return Volume(cubic_kilometers, VolumeUnits.CubicKilometer)

    
    @staticmethod
    def from_cubic_hectometers(cubic_hectometers: float):
        """
        Create a new instance of Volume from a value in cubic_hectometers.

        

        :param meters: The Volume value in cubic_hectometers.
        :type cubic_hectometers: float
        :return: A new instance of Volume.
        :rtype: Volume
        """
        return Volume(cubic_hectometers, VolumeUnits.CubicHectometer)

    
    @staticmethod
    def from_cubic_decimeters(cubic_decimeters: float):
        """
        Create a new instance of Volume from a value in cubic_decimeters.

        

        :param meters: The Volume value in cubic_decimeters.
        :type cubic_decimeters: float
        :return: A new instance of Volume.
        :rtype: Volume
        """
        return Volume(cubic_decimeters, VolumeUnits.CubicDecimeter)

    
    @staticmethod
    def from_cubic_centimeters(cubic_centimeters: float):
        """
        Create a new instance of Volume from a value in cubic_centimeters.

        

        :param meters: The Volume value in cubic_centimeters.
        :type cubic_centimeters: float
        :return: A new instance of Volume.
        :rtype: Volume
        """
        return Volume(cubic_centimeters, VolumeUnits.CubicCentimeter)

    
    @staticmethod
    def from_cubic_millimeters(cubic_millimeters: float):
        """
        Create a new instance of Volume from a value in cubic_millimeters.

        

        :param meters: The Volume value in cubic_millimeters.
        :type cubic_millimeters: float
        :return: A new instance of Volume.
        :rtype: Volume
        """
        return Volume(cubic_millimeters, VolumeUnits.CubicMillimeter)

    
    @staticmethod
    def from_cubic_micrometers(cubic_micrometers: float):
        """
        Create a new instance of Volume from a value in cubic_micrometers.

        

        :param meters: The Volume value in cubic_micrometers.
        :type cubic_micrometers: float
        :return: A new instance of Volume.
        :rtype: Volume
        """
        return Volume(cubic_micrometers, VolumeUnits.CubicMicrometer)

    
    @staticmethod
    def from_cubic_miles(cubic_miles: float):
        """
        Create a new instance of Volume from a value in cubic_miles.

        

        :param meters: The Volume value in cubic_miles.
        :type cubic_miles: float
        :return: A new instance of Volume.
        :rtype: Volume
        """
        return Volume(cubic_miles, VolumeUnits.CubicMile)

    
    @staticmethod
    def from_cubic_yards(cubic_yards: float):
        """
        Create a new instance of Volume from a value in cubic_yards.

        

        :param meters: The Volume value in cubic_yards.
        :type cubic_yards: float
        :return: A new instance of Volume.
        :rtype: Volume
        """
        return Volume(cubic_yards, VolumeUnits.CubicYard)

    
    @staticmethod
    def from_cubic_feet(cubic_feet: float):
        """
        Create a new instance of Volume from a value in cubic_feet.

        

        :param meters: The Volume value in cubic_feet.
        :type cubic_feet: float
        :return: A new instance of Volume.
        :rtype: Volume
        """
        return Volume(cubic_feet, VolumeUnits.CubicFoot)

    
    @staticmethod
    def from_cubic_inches(cubic_inches: float):
        """
        Create a new instance of Volume from a value in cubic_inches.

        

        :param meters: The Volume value in cubic_inches.
        :type cubic_inches: float
        :return: A new instance of Volume.
        :rtype: Volume
        """
        return Volume(cubic_inches, VolumeUnits.CubicInch)

    
    @staticmethod
    def from_imperial_gallons(imperial_gallons: float):
        """
        Create a new instance of Volume from a value in imperial_gallons.

        The British imperial gallon (frequently called simply "gallon") is defined as exactly 4.54609 litres.

        :param meters: The Volume value in imperial_gallons.
        :type imperial_gallons: float
        :return: A new instance of Volume.
        :rtype: Volume
        """
        return Volume(imperial_gallons, VolumeUnits.ImperialGallon)

    
    @staticmethod
    def from_imperial_ounces(imperial_ounces: float):
        """
        Create a new instance of Volume from a value in imperial_ounces.

        

        :param meters: The Volume value in imperial_ounces.
        :type imperial_ounces: float
        :return: A new instance of Volume.
        :rtype: Volume
        """
        return Volume(imperial_ounces, VolumeUnits.ImperialOunce)

    
    @staticmethod
    def from_us_gallons(us_gallons: float):
        """
        Create a new instance of Volume from a value in us_gallons.

        The US liquid gallon (frequently called simply "gallon") is legally defined as 231 cubic inches, which is exactly 3.785411784 litres.

        :param meters: The Volume value in us_gallons.
        :type us_gallons: float
        :return: A new instance of Volume.
        :rtype: Volume
        """
        return Volume(us_gallons, VolumeUnits.UsGallon)

    
    @staticmethod
    def from_us_ounces(us_ounces: float):
        """
        Create a new instance of Volume from a value in us_ounces.

        

        :param meters: The Volume value in us_ounces.
        :type us_ounces: float
        :return: A new instance of Volume.
        :rtype: Volume
        """
        return Volume(us_ounces, VolumeUnits.UsOunce)

    
    @staticmethod
    def from_us_tablespoons(us_tablespoons: float):
        """
        Create a new instance of Volume from a value in us_tablespoons.

        

        :param meters: The Volume value in us_tablespoons.
        :type us_tablespoons: float
        :return: A new instance of Volume.
        :rtype: Volume
        """
        return Volume(us_tablespoons, VolumeUnits.UsTablespoon)

    
    @staticmethod
    def from_au_tablespoons(au_tablespoons: float):
        """
        Create a new instance of Volume from a value in au_tablespoons.

        

        :param meters: The Volume value in au_tablespoons.
        :type au_tablespoons: float
        :return: A new instance of Volume.
        :rtype: Volume
        """
        return Volume(au_tablespoons, VolumeUnits.AuTablespoon)

    
    @staticmethod
    def from_uk_tablespoons(uk_tablespoons: float):
        """
        Create a new instance of Volume from a value in uk_tablespoons.

        

        :param meters: The Volume value in uk_tablespoons.
        :type uk_tablespoons: float
        :return: A new instance of Volume.
        :rtype: Volume
        """
        return Volume(uk_tablespoons, VolumeUnits.UkTablespoon)

    
    @staticmethod
    def from_metric_teaspoons(metric_teaspoons: float):
        """
        Create a new instance of Volume from a value in metric_teaspoons.

        

        :param meters: The Volume value in metric_teaspoons.
        :type metric_teaspoons: float
        :return: A new instance of Volume.
        :rtype: Volume
        """
        return Volume(metric_teaspoons, VolumeUnits.MetricTeaspoon)

    
    @staticmethod
    def from_us_teaspoons(us_teaspoons: float):
        """
        Create a new instance of Volume from a value in us_teaspoons.

        

        :param meters: The Volume value in us_teaspoons.
        :type us_teaspoons: float
        :return: A new instance of Volume.
        :rtype: Volume
        """
        return Volume(us_teaspoons, VolumeUnits.UsTeaspoon)

    
    @staticmethod
    def from_metric_cups(metric_cups: float):
        """
        Create a new instance of Volume from a value in metric_cups.

        

        :param meters: The Volume value in metric_cups.
        :type metric_cups: float
        :return: A new instance of Volume.
        :rtype: Volume
        """
        return Volume(metric_cups, VolumeUnits.MetricCup)

    
    @staticmethod
    def from_us_customary_cups(us_customary_cups: float):
        """
        Create a new instance of Volume from a value in us_customary_cups.

        

        :param meters: The Volume value in us_customary_cups.
        :type us_customary_cups: float
        :return: A new instance of Volume.
        :rtype: Volume
        """
        return Volume(us_customary_cups, VolumeUnits.UsCustomaryCup)

    
    @staticmethod
    def from_us_legal_cups(us_legal_cups: float):
        """
        Create a new instance of Volume from a value in us_legal_cups.

        

        :param meters: The Volume value in us_legal_cups.
        :type us_legal_cups: float
        :return: A new instance of Volume.
        :rtype: Volume
        """
        return Volume(us_legal_cups, VolumeUnits.UsLegalCup)

    
    @staticmethod
    def from_oil_barrels(oil_barrels: float):
        """
        Create a new instance of Volume from a value in oil_barrels.

        

        :param meters: The Volume value in oil_barrels.
        :type oil_barrels: float
        :return: A new instance of Volume.
        :rtype: Volume
        """
        return Volume(oil_barrels, VolumeUnits.OilBarrel)

    
    @staticmethod
    def from_us_beer_barrels(us_beer_barrels: float):
        """
        Create a new instance of Volume from a value in us_beer_barrels.

        

        :param meters: The Volume value in us_beer_barrels.
        :type us_beer_barrels: float
        :return: A new instance of Volume.
        :rtype: Volume
        """
        return Volume(us_beer_barrels, VolumeUnits.UsBeerBarrel)

    
    @staticmethod
    def from_imperial_beer_barrels(imperial_beer_barrels: float):
        """
        Create a new instance of Volume from a value in imperial_beer_barrels.

        

        :param meters: The Volume value in imperial_beer_barrels.
        :type imperial_beer_barrels: float
        :return: A new instance of Volume.
        :rtype: Volume
        """
        return Volume(imperial_beer_barrels, VolumeUnits.ImperialBeerBarrel)

    
    @staticmethod
    def from_us_quarts(us_quarts: float):
        """
        Create a new instance of Volume from a value in us_quarts.

        

        :param meters: The Volume value in us_quarts.
        :type us_quarts: float
        :return: A new instance of Volume.
        :rtype: Volume
        """
        return Volume(us_quarts, VolumeUnits.UsQuart)

    
    @staticmethod
    def from_imperial_quarts(imperial_quarts: float):
        """
        Create a new instance of Volume from a value in imperial_quarts.

        

        :param meters: The Volume value in imperial_quarts.
        :type imperial_quarts: float
        :return: A new instance of Volume.
        :rtype: Volume
        """
        return Volume(imperial_quarts, VolumeUnits.ImperialQuart)

    
    @staticmethod
    def from_us_pints(us_pints: float):
        """
        Create a new instance of Volume from a value in us_pints.

        

        :param meters: The Volume value in us_pints.
        :type us_pints: float
        :return: A new instance of Volume.
        :rtype: Volume
        """
        return Volume(us_pints, VolumeUnits.UsPint)

    
    @staticmethod
    def from_acre_feet(acre_feet: float):
        """
        Create a new instance of Volume from a value in acre_feet.

        

        :param meters: The Volume value in acre_feet.
        :type acre_feet: float
        :return: A new instance of Volume.
        :rtype: Volume
        """
        return Volume(acre_feet, VolumeUnits.AcreFoot)

    
    @staticmethod
    def from_imperial_pints(imperial_pints: float):
        """
        Create a new instance of Volume from a value in imperial_pints.

        

        :param meters: The Volume value in imperial_pints.
        :type imperial_pints: float
        :return: A new instance of Volume.
        :rtype: Volume
        """
        return Volume(imperial_pints, VolumeUnits.ImperialPint)

    
    @staticmethod
    def from_board_feet(board_feet: float):
        """
        Create a new instance of Volume from a value in board_feet.

        

        :param meters: The Volume value in board_feet.
        :type board_feet: float
        :return: A new instance of Volume.
        :rtype: Volume
        """
        return Volume(board_feet, VolumeUnits.BoardFoot)

    
    @staticmethod
    def from_nanoliters(nanoliters: float):
        """
        Create a new instance of Volume from a value in nanoliters.

        

        :param meters: The Volume value in nanoliters.
        :type nanoliters: float
        :return: A new instance of Volume.
        :rtype: Volume
        """
        return Volume(nanoliters, VolumeUnits.Nanoliter)

    
    @staticmethod
    def from_microliters(microliters: float):
        """
        Create a new instance of Volume from a value in microliters.

        

        :param meters: The Volume value in microliters.
        :type microliters: float
        :return: A new instance of Volume.
        :rtype: Volume
        """
        return Volume(microliters, VolumeUnits.Microliter)

    
    @staticmethod
    def from_milliliters(milliliters: float):
        """
        Create a new instance of Volume from a value in milliliters.

        

        :param meters: The Volume value in milliliters.
        :type milliliters: float
        :return: A new instance of Volume.
        :rtype: Volume
        """
        return Volume(milliliters, VolumeUnits.Milliliter)

    
    @staticmethod
    def from_centiliters(centiliters: float):
        """
        Create a new instance of Volume from a value in centiliters.

        

        :param meters: The Volume value in centiliters.
        :type centiliters: float
        :return: A new instance of Volume.
        :rtype: Volume
        """
        return Volume(centiliters, VolumeUnits.Centiliter)

    
    @staticmethod
    def from_deciliters(deciliters: float):
        """
        Create a new instance of Volume from a value in deciliters.

        

        :param meters: The Volume value in deciliters.
        :type deciliters: float
        :return: A new instance of Volume.
        :rtype: Volume
        """
        return Volume(deciliters, VolumeUnits.Deciliter)

    
    @staticmethod
    def from_decaliters(decaliters: float):
        """
        Create a new instance of Volume from a value in decaliters.

        

        :param meters: The Volume value in decaliters.
        :type decaliters: float
        :return: A new instance of Volume.
        :rtype: Volume
        """
        return Volume(decaliters, VolumeUnits.Decaliter)

    
    @staticmethod
    def from_hectoliters(hectoliters: float):
        """
        Create a new instance of Volume from a value in hectoliters.

        

        :param meters: The Volume value in hectoliters.
        :type hectoliters: float
        :return: A new instance of Volume.
        :rtype: Volume
        """
        return Volume(hectoliters, VolumeUnits.Hectoliter)

    
    @staticmethod
    def from_kiloliters(kiloliters: float):
        """
        Create a new instance of Volume from a value in kiloliters.

        

        :param meters: The Volume value in kiloliters.
        :type kiloliters: float
        :return: A new instance of Volume.
        :rtype: Volume
        """
        return Volume(kiloliters, VolumeUnits.Kiloliter)

    
    @staticmethod
    def from_megaliters(megaliters: float):
        """
        Create a new instance of Volume from a value in megaliters.

        

        :param meters: The Volume value in megaliters.
        :type megaliters: float
        :return: A new instance of Volume.
        :rtype: Volume
        """
        return Volume(megaliters, VolumeUnits.Megaliter)

    
    @staticmethod
    def from_hectocubic_meters(hectocubic_meters: float):
        """
        Create a new instance of Volume from a value in hectocubic_meters.

        

        :param meters: The Volume value in hectocubic_meters.
        :type hectocubic_meters: float
        :return: A new instance of Volume.
        :rtype: Volume
        """
        return Volume(hectocubic_meters, VolumeUnits.HectocubicMeter)

    
    @staticmethod
    def from_kilocubic_meters(kilocubic_meters: float):
        """
        Create a new instance of Volume from a value in kilocubic_meters.

        

        :param meters: The Volume value in kilocubic_meters.
        :type kilocubic_meters: float
        :return: A new instance of Volume.
        :rtype: Volume
        """
        return Volume(kilocubic_meters, VolumeUnits.KilocubicMeter)

    
    @staticmethod
    def from_hectocubic_feet(hectocubic_feet: float):
        """
        Create a new instance of Volume from a value in hectocubic_feet.

        

        :param meters: The Volume value in hectocubic_feet.
        :type hectocubic_feet: float
        :return: A new instance of Volume.
        :rtype: Volume
        """
        return Volume(hectocubic_feet, VolumeUnits.HectocubicFoot)

    
    @staticmethod
    def from_kilocubic_feet(kilocubic_feet: float):
        """
        Create a new instance of Volume from a value in kilocubic_feet.

        

        :param meters: The Volume value in kilocubic_feet.
        :type kilocubic_feet: float
        :return: A new instance of Volume.
        :rtype: Volume
        """
        return Volume(kilocubic_feet, VolumeUnits.KilocubicFoot)

    
    @staticmethod
    def from_megacubic_feet(megacubic_feet: float):
        """
        Create a new instance of Volume from a value in megacubic_feet.

        

        :param meters: The Volume value in megacubic_feet.
        :type megacubic_feet: float
        :return: A new instance of Volume.
        :rtype: Volume
        """
        return Volume(megacubic_feet, VolumeUnits.MegacubicFoot)

    
    @staticmethod
    def from_kiloimperial_gallons(kiloimperial_gallons: float):
        """
        Create a new instance of Volume from a value in kiloimperial_gallons.

        

        :param meters: The Volume value in kiloimperial_gallons.
        :type kiloimperial_gallons: float
        :return: A new instance of Volume.
        :rtype: Volume
        """
        return Volume(kiloimperial_gallons, VolumeUnits.KiloimperialGallon)

    
    @staticmethod
    def from_megaimperial_gallons(megaimperial_gallons: float):
        """
        Create a new instance of Volume from a value in megaimperial_gallons.

        

        :param meters: The Volume value in megaimperial_gallons.
        :type megaimperial_gallons: float
        :return: A new instance of Volume.
        :rtype: Volume
        """
        return Volume(megaimperial_gallons, VolumeUnits.MegaimperialGallon)

    
    @staticmethod
    def from_decaus_gallons(decaus_gallons: float):
        """
        Create a new instance of Volume from a value in decaus_gallons.

        

        :param meters: The Volume value in decaus_gallons.
        :type decaus_gallons: float
        :return: A new instance of Volume.
        :rtype: Volume
        """
        return Volume(decaus_gallons, VolumeUnits.DecausGallon)

    
    @staticmethod
    def from_decius_gallons(decius_gallons: float):
        """
        Create a new instance of Volume from a value in decius_gallons.

        

        :param meters: The Volume value in decius_gallons.
        :type decius_gallons: float
        :return: A new instance of Volume.
        :rtype: Volume
        """
        return Volume(decius_gallons, VolumeUnits.DeciusGallon)

    
    @staticmethod
    def from_hectous_gallons(hectous_gallons: float):
        """
        Create a new instance of Volume from a value in hectous_gallons.

        

        :param meters: The Volume value in hectous_gallons.
        :type hectous_gallons: float
        :return: A new instance of Volume.
        :rtype: Volume
        """
        return Volume(hectous_gallons, VolumeUnits.HectousGallon)

    
    @staticmethod
    def from_kilous_gallons(kilous_gallons: float):
        """
        Create a new instance of Volume from a value in kilous_gallons.

        

        :param meters: The Volume value in kilous_gallons.
        :type kilous_gallons: float
        :return: A new instance of Volume.
        :rtype: Volume
        """
        return Volume(kilous_gallons, VolumeUnits.KilousGallon)

    
    @staticmethod
    def from_megaus_gallons(megaus_gallons: float):
        """
        Create a new instance of Volume from a value in megaus_gallons.

        

        :param meters: The Volume value in megaus_gallons.
        :type megaus_gallons: float
        :return: A new instance of Volume.
        :rtype: Volume
        """
        return Volume(megaus_gallons, VolumeUnits.MegausGallon)

    
    @property
    def liters(self) -> float:
        """
        
        """
        if self.__liters != None:
            return self.__liters
        self.__liters = self.__convert_from_base(VolumeUnits.Liter)
        return self.__liters

    
    @property
    def cubic_meters(self) -> float:
        """
        
        """
        if self.__cubic_meters != None:
            return self.__cubic_meters
        self.__cubic_meters = self.__convert_from_base(VolumeUnits.CubicMeter)
        return self.__cubic_meters

    
    @property
    def cubic_kilometers(self) -> float:
        """
        
        """
        if self.__cubic_kilometers != None:
            return self.__cubic_kilometers
        self.__cubic_kilometers = self.__convert_from_base(VolumeUnits.CubicKilometer)
        return self.__cubic_kilometers

    
    @property
    def cubic_hectometers(self) -> float:
        """
        
        """
        if self.__cubic_hectometers != None:
            return self.__cubic_hectometers
        self.__cubic_hectometers = self.__convert_from_base(VolumeUnits.CubicHectometer)
        return self.__cubic_hectometers

    
    @property
    def cubic_decimeters(self) -> float:
        """
        
        """
        if self.__cubic_decimeters != None:
            return self.__cubic_decimeters
        self.__cubic_decimeters = self.__convert_from_base(VolumeUnits.CubicDecimeter)
        return self.__cubic_decimeters

    
    @property
    def cubic_centimeters(self) -> float:
        """
        
        """
        if self.__cubic_centimeters != None:
            return self.__cubic_centimeters
        self.__cubic_centimeters = self.__convert_from_base(VolumeUnits.CubicCentimeter)
        return self.__cubic_centimeters

    
    @property
    def cubic_millimeters(self) -> float:
        """
        
        """
        if self.__cubic_millimeters != None:
            return self.__cubic_millimeters
        self.__cubic_millimeters = self.__convert_from_base(VolumeUnits.CubicMillimeter)
        return self.__cubic_millimeters

    
    @property
    def cubic_micrometers(self) -> float:
        """
        
        """
        if self.__cubic_micrometers != None:
            return self.__cubic_micrometers
        self.__cubic_micrometers = self.__convert_from_base(VolumeUnits.CubicMicrometer)
        return self.__cubic_micrometers

    
    @property
    def cubic_miles(self) -> float:
        """
        
        """
        if self.__cubic_miles != None:
            return self.__cubic_miles
        self.__cubic_miles = self.__convert_from_base(VolumeUnits.CubicMile)
        return self.__cubic_miles

    
    @property
    def cubic_yards(self) -> float:
        """
        
        """
        if self.__cubic_yards != None:
            return self.__cubic_yards
        self.__cubic_yards = self.__convert_from_base(VolumeUnits.CubicYard)
        return self.__cubic_yards

    
    @property
    def cubic_feet(self) -> float:
        """
        
        """
        if self.__cubic_feet != None:
            return self.__cubic_feet
        self.__cubic_feet = self.__convert_from_base(VolumeUnits.CubicFoot)
        return self.__cubic_feet

    
    @property
    def cubic_inches(self) -> float:
        """
        
        """
        if self.__cubic_inches != None:
            return self.__cubic_inches
        self.__cubic_inches = self.__convert_from_base(VolumeUnits.CubicInch)
        return self.__cubic_inches

    
    @property
    def imperial_gallons(self) -> float:
        """
        The British imperial gallon (frequently called simply "gallon") is defined as exactly 4.54609 litres.
        """
        if self.__imperial_gallons != None:
            return self.__imperial_gallons
        self.__imperial_gallons = self.__convert_from_base(VolumeUnits.ImperialGallon)
        return self.__imperial_gallons

    
    @property
    def imperial_ounces(self) -> float:
        """
        
        """
        if self.__imperial_ounces != None:
            return self.__imperial_ounces
        self.__imperial_ounces = self.__convert_from_base(VolumeUnits.ImperialOunce)
        return self.__imperial_ounces

    
    @property
    def us_gallons(self) -> float:
        """
        The US liquid gallon (frequently called simply "gallon") is legally defined as 231 cubic inches, which is exactly 3.785411784 litres.
        """
        if self.__us_gallons != None:
            return self.__us_gallons
        self.__us_gallons = self.__convert_from_base(VolumeUnits.UsGallon)
        return self.__us_gallons

    
    @property
    def us_ounces(self) -> float:
        """
        
        """
        if self.__us_ounces != None:
            return self.__us_ounces
        self.__us_ounces = self.__convert_from_base(VolumeUnits.UsOunce)
        return self.__us_ounces

    
    @property
    def us_tablespoons(self) -> float:
        """
        
        """
        if self.__us_tablespoons != None:
            return self.__us_tablespoons
        self.__us_tablespoons = self.__convert_from_base(VolumeUnits.UsTablespoon)
        return self.__us_tablespoons

    
    @property
    def au_tablespoons(self) -> float:
        """
        
        """
        if self.__au_tablespoons != None:
            return self.__au_tablespoons
        self.__au_tablespoons = self.__convert_from_base(VolumeUnits.AuTablespoon)
        return self.__au_tablespoons

    
    @property
    def uk_tablespoons(self) -> float:
        """
        
        """
        if self.__uk_tablespoons != None:
            return self.__uk_tablespoons
        self.__uk_tablespoons = self.__convert_from_base(VolumeUnits.UkTablespoon)
        return self.__uk_tablespoons

    
    @property
    def metric_teaspoons(self) -> float:
        """
        
        """
        if self.__metric_teaspoons != None:
            return self.__metric_teaspoons
        self.__metric_teaspoons = self.__convert_from_base(VolumeUnits.MetricTeaspoon)
        return self.__metric_teaspoons

    
    @property
    def us_teaspoons(self) -> float:
        """
        
        """
        if self.__us_teaspoons != None:
            return self.__us_teaspoons
        self.__us_teaspoons = self.__convert_from_base(VolumeUnits.UsTeaspoon)
        return self.__us_teaspoons

    
    @property
    def metric_cups(self) -> float:
        """
        
        """
        if self.__metric_cups != None:
            return self.__metric_cups
        self.__metric_cups = self.__convert_from_base(VolumeUnits.MetricCup)
        return self.__metric_cups

    
    @property
    def us_customary_cups(self) -> float:
        """
        
        """
        if self.__us_customary_cups != None:
            return self.__us_customary_cups
        self.__us_customary_cups = self.__convert_from_base(VolumeUnits.UsCustomaryCup)
        return self.__us_customary_cups

    
    @property
    def us_legal_cups(self) -> float:
        """
        
        """
        if self.__us_legal_cups != None:
            return self.__us_legal_cups
        self.__us_legal_cups = self.__convert_from_base(VolumeUnits.UsLegalCup)
        return self.__us_legal_cups

    
    @property
    def oil_barrels(self) -> float:
        """
        
        """
        if self.__oil_barrels != None:
            return self.__oil_barrels
        self.__oil_barrels = self.__convert_from_base(VolumeUnits.OilBarrel)
        return self.__oil_barrels

    
    @property
    def us_beer_barrels(self) -> float:
        """
        
        """
        if self.__us_beer_barrels != None:
            return self.__us_beer_barrels
        self.__us_beer_barrels = self.__convert_from_base(VolumeUnits.UsBeerBarrel)
        return self.__us_beer_barrels

    
    @property
    def imperial_beer_barrels(self) -> float:
        """
        
        """
        if self.__imperial_beer_barrels != None:
            return self.__imperial_beer_barrels
        self.__imperial_beer_barrels = self.__convert_from_base(VolumeUnits.ImperialBeerBarrel)
        return self.__imperial_beer_barrels

    
    @property
    def us_quarts(self) -> float:
        """
        
        """
        if self.__us_quarts != None:
            return self.__us_quarts
        self.__us_quarts = self.__convert_from_base(VolumeUnits.UsQuart)
        return self.__us_quarts

    
    @property
    def imperial_quarts(self) -> float:
        """
        
        """
        if self.__imperial_quarts != None:
            return self.__imperial_quarts
        self.__imperial_quarts = self.__convert_from_base(VolumeUnits.ImperialQuart)
        return self.__imperial_quarts

    
    @property
    def us_pints(self) -> float:
        """
        
        """
        if self.__us_pints != None:
            return self.__us_pints
        self.__us_pints = self.__convert_from_base(VolumeUnits.UsPint)
        return self.__us_pints

    
    @property
    def acre_feet(self) -> float:
        """
        
        """
        if self.__acre_feet != None:
            return self.__acre_feet
        self.__acre_feet = self.__convert_from_base(VolumeUnits.AcreFoot)
        return self.__acre_feet

    
    @property
    def imperial_pints(self) -> float:
        """
        
        """
        if self.__imperial_pints != None:
            return self.__imperial_pints
        self.__imperial_pints = self.__convert_from_base(VolumeUnits.ImperialPint)
        return self.__imperial_pints

    
    @property
    def board_feet(self) -> float:
        """
        
        """
        if self.__board_feet != None:
            return self.__board_feet
        self.__board_feet = self.__convert_from_base(VolumeUnits.BoardFoot)
        return self.__board_feet

    
    @property
    def nanoliters(self) -> float:
        """
        
        """
        if self.__nanoliters != None:
            return self.__nanoliters
        self.__nanoliters = self.__convert_from_base(VolumeUnits.Nanoliter)
        return self.__nanoliters

    
    @property
    def microliters(self) -> float:
        """
        
        """
        if self.__microliters != None:
            return self.__microliters
        self.__microliters = self.__convert_from_base(VolumeUnits.Microliter)
        return self.__microliters

    
    @property
    def milliliters(self) -> float:
        """
        
        """
        if self.__milliliters != None:
            return self.__milliliters
        self.__milliliters = self.__convert_from_base(VolumeUnits.Milliliter)
        return self.__milliliters

    
    @property
    def centiliters(self) -> float:
        """
        
        """
        if self.__centiliters != None:
            return self.__centiliters
        self.__centiliters = self.__convert_from_base(VolumeUnits.Centiliter)
        return self.__centiliters

    
    @property
    def deciliters(self) -> float:
        """
        
        """
        if self.__deciliters != None:
            return self.__deciliters
        self.__deciliters = self.__convert_from_base(VolumeUnits.Deciliter)
        return self.__deciliters

    
    @property
    def decaliters(self) -> float:
        """
        
        """
        if self.__decaliters != None:
            return self.__decaliters
        self.__decaliters = self.__convert_from_base(VolumeUnits.Decaliter)
        return self.__decaliters

    
    @property
    def hectoliters(self) -> float:
        """
        
        """
        if self.__hectoliters != None:
            return self.__hectoliters
        self.__hectoliters = self.__convert_from_base(VolumeUnits.Hectoliter)
        return self.__hectoliters

    
    @property
    def kiloliters(self) -> float:
        """
        
        """
        if self.__kiloliters != None:
            return self.__kiloliters
        self.__kiloliters = self.__convert_from_base(VolumeUnits.Kiloliter)
        return self.__kiloliters

    
    @property
    def megaliters(self) -> float:
        """
        
        """
        if self.__megaliters != None:
            return self.__megaliters
        self.__megaliters = self.__convert_from_base(VolumeUnits.Megaliter)
        return self.__megaliters

    
    @property
    def hectocubic_meters(self) -> float:
        """
        
        """
        if self.__hectocubic_meters != None:
            return self.__hectocubic_meters
        self.__hectocubic_meters = self.__convert_from_base(VolumeUnits.HectocubicMeter)
        return self.__hectocubic_meters

    
    @property
    def kilocubic_meters(self) -> float:
        """
        
        """
        if self.__kilocubic_meters != None:
            return self.__kilocubic_meters
        self.__kilocubic_meters = self.__convert_from_base(VolumeUnits.KilocubicMeter)
        return self.__kilocubic_meters

    
    @property
    def hectocubic_feet(self) -> float:
        """
        
        """
        if self.__hectocubic_feet != None:
            return self.__hectocubic_feet
        self.__hectocubic_feet = self.__convert_from_base(VolumeUnits.HectocubicFoot)
        return self.__hectocubic_feet

    
    @property
    def kilocubic_feet(self) -> float:
        """
        
        """
        if self.__kilocubic_feet != None:
            return self.__kilocubic_feet
        self.__kilocubic_feet = self.__convert_from_base(VolumeUnits.KilocubicFoot)
        return self.__kilocubic_feet

    
    @property
    def megacubic_feet(self) -> float:
        """
        
        """
        if self.__megacubic_feet != None:
            return self.__megacubic_feet
        self.__megacubic_feet = self.__convert_from_base(VolumeUnits.MegacubicFoot)
        return self.__megacubic_feet

    
    @property
    def kiloimperial_gallons(self) -> float:
        """
        
        """
        if self.__kiloimperial_gallons != None:
            return self.__kiloimperial_gallons
        self.__kiloimperial_gallons = self.__convert_from_base(VolumeUnits.KiloimperialGallon)
        return self.__kiloimperial_gallons

    
    @property
    def megaimperial_gallons(self) -> float:
        """
        
        """
        if self.__megaimperial_gallons != None:
            return self.__megaimperial_gallons
        self.__megaimperial_gallons = self.__convert_from_base(VolumeUnits.MegaimperialGallon)
        return self.__megaimperial_gallons

    
    @property
    def decaus_gallons(self) -> float:
        """
        
        """
        if self.__decaus_gallons != None:
            return self.__decaus_gallons
        self.__decaus_gallons = self.__convert_from_base(VolumeUnits.DecausGallon)
        return self.__decaus_gallons

    
    @property
    def decius_gallons(self) -> float:
        """
        
        """
        if self.__decius_gallons != None:
            return self.__decius_gallons
        self.__decius_gallons = self.__convert_from_base(VolumeUnits.DeciusGallon)
        return self.__decius_gallons

    
    @property
    def hectous_gallons(self) -> float:
        """
        
        """
        if self.__hectous_gallons != None:
            return self.__hectous_gallons
        self.__hectous_gallons = self.__convert_from_base(VolumeUnits.HectousGallon)
        return self.__hectous_gallons

    
    @property
    def kilous_gallons(self) -> float:
        """
        
        """
        if self.__kilous_gallons != None:
            return self.__kilous_gallons
        self.__kilous_gallons = self.__convert_from_base(VolumeUnits.KilousGallon)
        return self.__kilous_gallons

    
    @property
    def megaus_gallons(self) -> float:
        """
        
        """
        if self.__megaus_gallons != None:
            return self.__megaus_gallons
        self.__megaus_gallons = self.__convert_from_base(VolumeUnits.MegausGallon)
        return self.__megaus_gallons

    
    def to_string(self, unit: VolumeUnits = VolumeUnits.CubicMeter) -> str:
        """
        Format the Volume to string.
        Note! the default format for Volume is CubicMeter.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == VolumeUnits.Liter:
            return f"""{self.liters} l"""
        
        if unit == VolumeUnits.CubicMeter:
            return f"""{self.cubic_meters} m³"""
        
        if unit == VolumeUnits.CubicKilometer:
            return f"""{self.cubic_kilometers} km³"""
        
        if unit == VolumeUnits.CubicHectometer:
            return f"""{self.cubic_hectometers} hm³"""
        
        if unit == VolumeUnits.CubicDecimeter:
            return f"""{self.cubic_decimeters} dm³"""
        
        if unit == VolumeUnits.CubicCentimeter:
            return f"""{self.cubic_centimeters} cm³"""
        
        if unit == VolumeUnits.CubicMillimeter:
            return f"""{self.cubic_millimeters} mm³"""
        
        if unit == VolumeUnits.CubicMicrometer:
            return f"""{self.cubic_micrometers} µm³"""
        
        if unit == VolumeUnits.CubicMile:
            return f"""{self.cubic_miles} mi³"""
        
        if unit == VolumeUnits.CubicYard:
            return f"""{self.cubic_yards} yd³"""
        
        if unit == VolumeUnits.CubicFoot:
            return f"""{self.cubic_feet} ft³"""
        
        if unit == VolumeUnits.CubicInch:
            return f"""{self.cubic_inches} in³"""
        
        if unit == VolumeUnits.ImperialGallon:
            return f"""{self.imperial_gallons} gal (imp.)"""
        
        if unit == VolumeUnits.ImperialOunce:
            return f"""{self.imperial_ounces} oz (imp.)"""
        
        if unit == VolumeUnits.UsGallon:
            return f"""{self.us_gallons} gal (U.S.)"""
        
        if unit == VolumeUnits.UsOunce:
            return f"""{self.us_ounces} oz (U.S.)"""
        
        if unit == VolumeUnits.UsTablespoon:
            return f"""{self.us_tablespoons} """
        
        if unit == VolumeUnits.AuTablespoon:
            return f"""{self.au_tablespoons} """
        
        if unit == VolumeUnits.UkTablespoon:
            return f"""{self.uk_tablespoons} """
        
        if unit == VolumeUnits.MetricTeaspoon:
            return f"""{self.metric_teaspoons} tsp"""
        
        if unit == VolumeUnits.UsTeaspoon:
            return f"""{self.us_teaspoons} """
        
        if unit == VolumeUnits.MetricCup:
            return f"""{self.metric_cups} """
        
        if unit == VolumeUnits.UsCustomaryCup:
            return f"""{self.us_customary_cups} """
        
        if unit == VolumeUnits.UsLegalCup:
            return f"""{self.us_legal_cups} """
        
        if unit == VolumeUnits.OilBarrel:
            return f"""{self.oil_barrels} bbl"""
        
        if unit == VolumeUnits.UsBeerBarrel:
            return f"""{self.us_beer_barrels} bl (U.S.)"""
        
        if unit == VolumeUnits.ImperialBeerBarrel:
            return f"""{self.imperial_beer_barrels} bl (imp.)"""
        
        if unit == VolumeUnits.UsQuart:
            return f"""{self.us_quarts} qt (U.S.)"""
        
        if unit == VolumeUnits.ImperialQuart:
            return f"""{self.imperial_quarts} qt (imp.)"""
        
        if unit == VolumeUnits.UsPint:
            return f"""{self.us_pints} pt (U.S.)"""
        
        if unit == VolumeUnits.AcreFoot:
            return f"""{self.acre_feet} ac-ft"""
        
        if unit == VolumeUnits.ImperialPint:
            return f"""{self.imperial_pints} pt (imp.)"""
        
        if unit == VolumeUnits.BoardFoot:
            return f"""{self.board_feet} bf"""
        
        if unit == VolumeUnits.Nanoliter:
            return f"""{self.nanoliters} nl"""
        
        if unit == VolumeUnits.Microliter:
            return f"""{self.microliters} μl"""
        
        if unit == VolumeUnits.Milliliter:
            return f"""{self.milliliters} ml"""
        
        if unit == VolumeUnits.Centiliter:
            return f"""{self.centiliters} cl"""
        
        if unit == VolumeUnits.Deciliter:
            return f"""{self.deciliters} dl"""
        
        if unit == VolumeUnits.Decaliter:
            return f"""{self.decaliters} dal"""
        
        if unit == VolumeUnits.Hectoliter:
            return f"""{self.hectoliters} hl"""
        
        if unit == VolumeUnits.Kiloliter:
            return f"""{self.kiloliters} kl"""
        
        if unit == VolumeUnits.Megaliter:
            return f"""{self.megaliters} Ml"""
        
        if unit == VolumeUnits.HectocubicMeter:
            return f"""{self.hectocubic_meters} hm³"""
        
        if unit == VolumeUnits.KilocubicMeter:
            return f"""{self.kilocubic_meters} km³"""
        
        if unit == VolumeUnits.HectocubicFoot:
            return f"""{self.hectocubic_feet} hft³"""
        
        if unit == VolumeUnits.KilocubicFoot:
            return f"""{self.kilocubic_feet} kft³"""
        
        if unit == VolumeUnits.MegacubicFoot:
            return f"""{self.megacubic_feet} Mft³"""
        
        if unit == VolumeUnits.KiloimperialGallon:
            return f"""{self.kiloimperial_gallons} kgal (imp.)"""
        
        if unit == VolumeUnits.MegaimperialGallon:
            return f"""{self.megaimperial_gallons} Mgal (imp.)"""
        
        if unit == VolumeUnits.DecausGallon:
            return f"""{self.decaus_gallons} dagal (U.S.)"""
        
        if unit == VolumeUnits.DeciusGallon:
            return f"""{self.decius_gallons} dgal (U.S.)"""
        
        if unit == VolumeUnits.HectousGallon:
            return f"""{self.hectous_gallons} hgal (U.S.)"""
        
        if unit == VolumeUnits.KilousGallon:
            return f"""{self.kilous_gallons} kgal (U.S.)"""
        
        if unit == VolumeUnits.MegausGallon:
            return f"""{self.megaus_gallons} Mgal (U.S.)"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: VolumeUnits = VolumeUnits.CubicMeter) -> str:
        """
        Get Volume unit abbreviation.
        Note! the default abbreviation for Volume is CubicMeter.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == VolumeUnits.Liter:
            return """l"""
        
        if unit_abbreviation == VolumeUnits.CubicMeter:
            return """m³"""
        
        if unit_abbreviation == VolumeUnits.CubicKilometer:
            return """km³"""
        
        if unit_abbreviation == VolumeUnits.CubicHectometer:
            return """hm³"""
        
        if unit_abbreviation == VolumeUnits.CubicDecimeter:
            return """dm³"""
        
        if unit_abbreviation == VolumeUnits.CubicCentimeter:
            return """cm³"""
        
        if unit_abbreviation == VolumeUnits.CubicMillimeter:
            return """mm³"""
        
        if unit_abbreviation == VolumeUnits.CubicMicrometer:
            return """µm³"""
        
        if unit_abbreviation == VolumeUnits.CubicMile:
            return """mi³"""
        
        if unit_abbreviation == VolumeUnits.CubicYard:
            return """yd³"""
        
        if unit_abbreviation == VolumeUnits.CubicFoot:
            return """ft³"""
        
        if unit_abbreviation == VolumeUnits.CubicInch:
            return """in³"""
        
        if unit_abbreviation == VolumeUnits.ImperialGallon:
            return """gal (imp.)"""
        
        if unit_abbreviation == VolumeUnits.ImperialOunce:
            return """oz (imp.)"""
        
        if unit_abbreviation == VolumeUnits.UsGallon:
            return """gal (U.S.)"""
        
        if unit_abbreviation == VolumeUnits.UsOunce:
            return """oz (U.S.)"""
        
        if unit_abbreviation == VolumeUnits.UsTablespoon:
            return """"""
        
        if unit_abbreviation == VolumeUnits.AuTablespoon:
            return """"""
        
        if unit_abbreviation == VolumeUnits.UkTablespoon:
            return """"""
        
        if unit_abbreviation == VolumeUnits.MetricTeaspoon:
            return """tsp"""
        
        if unit_abbreviation == VolumeUnits.UsTeaspoon:
            return """"""
        
        if unit_abbreviation == VolumeUnits.MetricCup:
            return """"""
        
        if unit_abbreviation == VolumeUnits.UsCustomaryCup:
            return """"""
        
        if unit_abbreviation == VolumeUnits.UsLegalCup:
            return """"""
        
        if unit_abbreviation == VolumeUnits.OilBarrel:
            return """bbl"""
        
        if unit_abbreviation == VolumeUnits.UsBeerBarrel:
            return """bl (U.S.)"""
        
        if unit_abbreviation == VolumeUnits.ImperialBeerBarrel:
            return """bl (imp.)"""
        
        if unit_abbreviation == VolumeUnits.UsQuart:
            return """qt (U.S.)"""
        
        if unit_abbreviation == VolumeUnits.ImperialQuart:
            return """qt (imp.)"""
        
        if unit_abbreviation == VolumeUnits.UsPint:
            return """pt (U.S.)"""
        
        if unit_abbreviation == VolumeUnits.AcreFoot:
            return """ac-ft"""
        
        if unit_abbreviation == VolumeUnits.ImperialPint:
            return """pt (imp.)"""
        
        if unit_abbreviation == VolumeUnits.BoardFoot:
            return """bf"""
        
        if unit_abbreviation == VolumeUnits.Nanoliter:
            return """nl"""
        
        if unit_abbreviation == VolumeUnits.Microliter:
            return """μl"""
        
        if unit_abbreviation == VolumeUnits.Milliliter:
            return """ml"""
        
        if unit_abbreviation == VolumeUnits.Centiliter:
            return """cl"""
        
        if unit_abbreviation == VolumeUnits.Deciliter:
            return """dl"""
        
        if unit_abbreviation == VolumeUnits.Decaliter:
            return """dal"""
        
        if unit_abbreviation == VolumeUnits.Hectoliter:
            return """hl"""
        
        if unit_abbreviation == VolumeUnits.Kiloliter:
            return """kl"""
        
        if unit_abbreviation == VolumeUnits.Megaliter:
            return """Ml"""
        
        if unit_abbreviation == VolumeUnits.HectocubicMeter:
            return """hm³"""
        
        if unit_abbreviation == VolumeUnits.KilocubicMeter:
            return """km³"""
        
        if unit_abbreviation == VolumeUnits.HectocubicFoot:
            return """hft³"""
        
        if unit_abbreviation == VolumeUnits.KilocubicFoot:
            return """kft³"""
        
        if unit_abbreviation == VolumeUnits.MegacubicFoot:
            return """Mft³"""
        
        if unit_abbreviation == VolumeUnits.KiloimperialGallon:
            return """kgal (imp.)"""
        
        if unit_abbreviation == VolumeUnits.MegaimperialGallon:
            return """Mgal (imp.)"""
        
        if unit_abbreviation == VolumeUnits.DecausGallon:
            return """dagal (U.S.)"""
        
        if unit_abbreviation == VolumeUnits.DeciusGallon:
            return """dgal (U.S.)"""
        
        if unit_abbreviation == VolumeUnits.HectousGallon:
            return """hgal (U.S.)"""
        
        if unit_abbreviation == VolumeUnits.KilousGallon:
            return """kgal (U.S.)"""
        
        if unit_abbreviation == VolumeUnits.MegausGallon:
            return """Mgal (U.S.)"""
        
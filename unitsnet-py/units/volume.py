from enum import Enum
import math
import string


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
            
        """
        
        ImperialOunce = 'imperial_ounce'
        """
            
        """
        
        UsGallon = 'us_gallon'
        """
            
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
        
        NanoLiter = 'nano_liter'
        """
            
        """
        
        MicroLiter = 'micro_liter'
        """
            
        """
        
        MilliLiter = 'milli_liter'
        """
            
        """
        
        CentiLiter = 'centi_liter'
        """
            
        """
        
        DeciLiter = 'deci_liter'
        """
            
        """
        
        DecaLiter = 'deca_liter'
        """
            
        """
        
        HectoLiter = 'hecto_liter'
        """
            
        """
        
        KiloLiter = 'kilo_liter'
        """
            
        """
        
        MegaLiter = 'mega_liter'
        """
            
        """
        
        HectoCubicMeter = 'hecto_cubic_meter'
        """
            
        """
        
        KiloCubicMeter = 'kilo_cubic_meter'
        """
            
        """
        
        HectoCubicFoot = 'hecto_cubic_foot'
        """
            
        """
        
        KiloCubicFoot = 'kilo_cubic_foot'
        """
            
        """
        
        MegaCubicFoot = 'mega_cubic_foot'
        """
            
        """
        
        KiloImperialGallon = 'kilo_imperial_gallon'
        """
            
        """
        
        MegaImperialGallon = 'mega_imperial_gallon'
        """
            
        """
        
        DecaUsGallon = 'deca_us_gallon'
        """
            
        """
        
        DeciUsGallon = 'deci_us_gallon'
        """
            
        """
        
        HectoUsGallon = 'hecto_us_gallon'
        """
            
        """
        
        KiloUsGallon = 'kilo_us_gallon'
        """
            
        """
        
        MegaUsGallon = 'mega_us_gallon'
        """
            
        """
        

class Volume:
    """
    Volume is the quantity of three-dimensional space enclosed by some closed boundary, for example, the space that a substance (solid, liquid, gas, or plasma) or shape occupies or contains.[1] Volume is often quantified numerically using the SI derived unit, the cubic metre. The volume of a container is generally understood to be the capacity of the container, i. e. the amount of fluid (gas or liquid) that the container could hold, rather than the amount of space the container itself displaces.

    Args:
        value (float): The value.
        from_unit (VolumeUnits): The Volume unit to create from, The default unit is CubicMeter
    """
    def __init__(self, value: float, from_unit: VolumeUnits = VolumeUnits.CubicMeter):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
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
        
        self.__us_pints = None
        
        self.__acre_feet = None
        
        self.__imperial_pints = None
        
        self.__board_feet = None
        
        self.__nano_liters = None
        
        self.__micro_liters = None
        
        self.__milli_liters = None
        
        self.__centi_liters = None
        
        self.__deci_liters = None
        
        self.__deca_liters = None
        
        self.__hecto_liters = None
        
        self.__kilo_liters = None
        
        self.__mega_liters = None
        
        self.__hecto_cubic_meters = None
        
        self.__kilo_cubic_meters = None
        
        self.__hecto_cubic_feet = None
        
        self.__kilo_cubic_feet = None
        
        self.__mega_cubic_feet = None
        
        self.__kilo_imperial_gallons = None
        
        self.__mega_imperial_gallons = None
        
        self.__deca_us_gallons = None
        
        self.__deci_us_gallons = None
        
        self.__hecto_us_gallons = None
        
        self.__kilo_us_gallons = None
        
        self.__mega_us_gallons = None
        

    def __convert_from_base(self, from_unit: VolumeUnits) -> float:
        value = self.__value
        
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
            return (value / (1.6387 * 1e-5))
        
        if from_unit == VolumeUnits.ImperialGallon:
            return (value / 0.00454609000000181429905810072407)
        
        if from_unit == VolumeUnits.ImperialOunce:
            return (value / 2.8413062499962901241875439064617e-5)
        
        if from_unit == VolumeUnits.UsGallon:
            return (value / 0.00378541)
        
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
        
        if from_unit == VolumeUnits.UsPint:
            return (value / 4.73176473e-4)
        
        if from_unit == VolumeUnits.AcreFoot:
            return (value * 0.000810714)
        
        if from_unit == VolumeUnits.ImperialPint:
            return (value / 5.6826125e-4)
        
        if from_unit == VolumeUnits.BoardFoot:
            return (value / 2.3597372158e-3)
        
        if from_unit == VolumeUnits.NanoLiter:
            return ((value * 1e3) / 1e-09)
        
        if from_unit == VolumeUnits.MicroLiter:
            return ((value * 1e3) / 1e-06)
        
        if from_unit == VolumeUnits.MilliLiter:
            return ((value * 1e3) / 0.001)
        
        if from_unit == VolumeUnits.CentiLiter:
            return ((value * 1e3) / 0.01)
        
        if from_unit == VolumeUnits.DeciLiter:
            return ((value * 1e3) / 0.1)
        
        if from_unit == VolumeUnits.DecaLiter:
            return ((value * 1e3) / 10.0)
        
        if from_unit == VolumeUnits.HectoLiter:
            return ((value * 1e3) / 100.0)
        
        if from_unit == VolumeUnits.KiloLiter:
            return ((value * 1e3) / 1000.0)
        
        if from_unit == VolumeUnits.MegaLiter:
            return ((value * 1e3) / 1000000.0)
        
        if from_unit == VolumeUnits.HectoCubicMeter:
            return ((value) / 100.0)
        
        if from_unit == VolumeUnits.KiloCubicMeter:
            return ((value) / 1000.0)
        
        if from_unit == VolumeUnits.HectoCubicFoot:
            return ((value / 2.8316846592e-2) / 100.0)
        
        if from_unit == VolumeUnits.KiloCubicFoot:
            return ((value / 2.8316846592e-2) / 1000.0)
        
        if from_unit == VolumeUnits.MegaCubicFoot:
            return ((value / 2.8316846592e-2) / 1000000.0)
        
        if from_unit == VolumeUnits.KiloImperialGallon:
            return ((value / 0.00454609000000181429905810072407) / 1000.0)
        
        if from_unit == VolumeUnits.MegaImperialGallon:
            return ((value / 0.00454609000000181429905810072407) / 1000000.0)
        
        if from_unit == VolumeUnits.DecaUsGallon:
            return ((value / 0.00378541) / 10.0)
        
        if from_unit == VolumeUnits.DeciUsGallon:
            return ((value / 0.00378541) / 0.1)
        
        if from_unit == VolumeUnits.HectoUsGallon:
            return ((value / 0.00378541) / 100.0)
        
        if from_unit == VolumeUnits.KiloUsGallon:
            return ((value / 0.00378541) / 1000.0)
        
        if from_unit == VolumeUnits.MegaUsGallon:
            return ((value / 0.00378541) / 1000000.0)
        
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
            return (value * 1.6387 * 1e-5)
        
        if to_unit == VolumeUnits.ImperialGallon:
            return (value * 0.00454609000000181429905810072407)
        
        if to_unit == VolumeUnits.ImperialOunce:
            return (value * 2.8413062499962901241875439064617e-5)
        
        if to_unit == VolumeUnits.UsGallon:
            return (value * 0.00378541)
        
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
        
        if to_unit == VolumeUnits.UsPint:
            return (value * 4.73176473e-4)
        
        if to_unit == VolumeUnits.AcreFoot:
            return (value / 0.000810714)
        
        if to_unit == VolumeUnits.ImperialPint:
            return (value * 5.6826125e-4)
        
        if to_unit == VolumeUnits.BoardFoot:
            return (value * 2.3597372158e-3)
        
        if to_unit == VolumeUnits.NanoLiter:
            return ((value / 1e3) * 1e-09)
        
        if to_unit == VolumeUnits.MicroLiter:
            return ((value / 1e3) * 1e-06)
        
        if to_unit == VolumeUnits.MilliLiter:
            return ((value / 1e3) * 0.001)
        
        if to_unit == VolumeUnits.CentiLiter:
            return ((value / 1e3) * 0.01)
        
        if to_unit == VolumeUnits.DeciLiter:
            return ((value / 1e3) * 0.1)
        
        if to_unit == VolumeUnits.DecaLiter:
            return ((value / 1e3) * 10.0)
        
        if to_unit == VolumeUnits.HectoLiter:
            return ((value / 1e3) * 100.0)
        
        if to_unit == VolumeUnits.KiloLiter:
            return ((value / 1e3) * 1000.0)
        
        if to_unit == VolumeUnits.MegaLiter:
            return ((value / 1e3) * 1000000.0)
        
        if to_unit == VolumeUnits.HectoCubicMeter:
            return ((value) * 100.0)
        
        if to_unit == VolumeUnits.KiloCubicMeter:
            return ((value) * 1000.0)
        
        if to_unit == VolumeUnits.HectoCubicFoot:
            return ((value * 2.8316846592e-2) * 100.0)
        
        if to_unit == VolumeUnits.KiloCubicFoot:
            return ((value * 2.8316846592e-2) * 1000.0)
        
        if to_unit == VolumeUnits.MegaCubicFoot:
            return ((value * 2.8316846592e-2) * 1000000.0)
        
        if to_unit == VolumeUnits.KiloImperialGallon:
            return ((value * 0.00454609000000181429905810072407) * 1000.0)
        
        if to_unit == VolumeUnits.MegaImperialGallon:
            return ((value * 0.00454609000000181429905810072407) * 1000000.0)
        
        if to_unit == VolumeUnits.DecaUsGallon:
            return ((value * 0.00378541) * 10.0)
        
        if to_unit == VolumeUnits.DeciUsGallon:
            return ((value * 0.00378541) * 0.1)
        
        if to_unit == VolumeUnits.HectoUsGallon:
            return ((value * 0.00378541) * 100.0)
        
        if to_unit == VolumeUnits.KiloUsGallon:
            return ((value * 0.00378541) * 1000.0)
        
        if to_unit == VolumeUnits.MegaUsGallon:
            return ((value * 0.00378541) * 1000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
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
    def from_nano_liters(nano_liters: float):
        """
        Create a new instance of Volume from a value in nano_liters.

        

        :param meters: The Volume value in nano_liters.
        :type nano_liters: float
        :return: A new instance of Volume.
        :rtype: Volume
        """
        return Volume(nano_liters, VolumeUnits.NanoLiter)

    
    @staticmethod
    def from_micro_liters(micro_liters: float):
        """
        Create a new instance of Volume from a value in micro_liters.

        

        :param meters: The Volume value in micro_liters.
        :type micro_liters: float
        :return: A new instance of Volume.
        :rtype: Volume
        """
        return Volume(micro_liters, VolumeUnits.MicroLiter)

    
    @staticmethod
    def from_milli_liters(milli_liters: float):
        """
        Create a new instance of Volume from a value in milli_liters.

        

        :param meters: The Volume value in milli_liters.
        :type milli_liters: float
        :return: A new instance of Volume.
        :rtype: Volume
        """
        return Volume(milli_liters, VolumeUnits.MilliLiter)

    
    @staticmethod
    def from_centi_liters(centi_liters: float):
        """
        Create a new instance of Volume from a value in centi_liters.

        

        :param meters: The Volume value in centi_liters.
        :type centi_liters: float
        :return: A new instance of Volume.
        :rtype: Volume
        """
        return Volume(centi_liters, VolumeUnits.CentiLiter)

    
    @staticmethod
    def from_deci_liters(deci_liters: float):
        """
        Create a new instance of Volume from a value in deci_liters.

        

        :param meters: The Volume value in deci_liters.
        :type deci_liters: float
        :return: A new instance of Volume.
        :rtype: Volume
        """
        return Volume(deci_liters, VolumeUnits.DeciLiter)

    
    @staticmethod
    def from_deca_liters(deca_liters: float):
        """
        Create a new instance of Volume from a value in deca_liters.

        

        :param meters: The Volume value in deca_liters.
        :type deca_liters: float
        :return: A new instance of Volume.
        :rtype: Volume
        """
        return Volume(deca_liters, VolumeUnits.DecaLiter)

    
    @staticmethod
    def from_hecto_liters(hecto_liters: float):
        """
        Create a new instance of Volume from a value in hecto_liters.

        

        :param meters: The Volume value in hecto_liters.
        :type hecto_liters: float
        :return: A new instance of Volume.
        :rtype: Volume
        """
        return Volume(hecto_liters, VolumeUnits.HectoLiter)

    
    @staticmethod
    def from_kilo_liters(kilo_liters: float):
        """
        Create a new instance of Volume from a value in kilo_liters.

        

        :param meters: The Volume value in kilo_liters.
        :type kilo_liters: float
        :return: A new instance of Volume.
        :rtype: Volume
        """
        return Volume(kilo_liters, VolumeUnits.KiloLiter)

    
    @staticmethod
    def from_mega_liters(mega_liters: float):
        """
        Create a new instance of Volume from a value in mega_liters.

        

        :param meters: The Volume value in mega_liters.
        :type mega_liters: float
        :return: A new instance of Volume.
        :rtype: Volume
        """
        return Volume(mega_liters, VolumeUnits.MegaLiter)

    
    @staticmethod
    def from_hecto_cubic_meters(hecto_cubic_meters: float):
        """
        Create a new instance of Volume from a value in hecto_cubic_meters.

        

        :param meters: The Volume value in hecto_cubic_meters.
        :type hecto_cubic_meters: float
        :return: A new instance of Volume.
        :rtype: Volume
        """
        return Volume(hecto_cubic_meters, VolumeUnits.HectoCubicMeter)

    
    @staticmethod
    def from_kilo_cubic_meters(kilo_cubic_meters: float):
        """
        Create a new instance of Volume from a value in kilo_cubic_meters.

        

        :param meters: The Volume value in kilo_cubic_meters.
        :type kilo_cubic_meters: float
        :return: A new instance of Volume.
        :rtype: Volume
        """
        return Volume(kilo_cubic_meters, VolumeUnits.KiloCubicMeter)

    
    @staticmethod
    def from_hecto_cubic_feet(hecto_cubic_feet: float):
        """
        Create a new instance of Volume from a value in hecto_cubic_feet.

        

        :param meters: The Volume value in hecto_cubic_feet.
        :type hecto_cubic_feet: float
        :return: A new instance of Volume.
        :rtype: Volume
        """
        return Volume(hecto_cubic_feet, VolumeUnits.HectoCubicFoot)

    
    @staticmethod
    def from_kilo_cubic_feet(kilo_cubic_feet: float):
        """
        Create a new instance of Volume from a value in kilo_cubic_feet.

        

        :param meters: The Volume value in kilo_cubic_feet.
        :type kilo_cubic_feet: float
        :return: A new instance of Volume.
        :rtype: Volume
        """
        return Volume(kilo_cubic_feet, VolumeUnits.KiloCubicFoot)

    
    @staticmethod
    def from_mega_cubic_feet(mega_cubic_feet: float):
        """
        Create a new instance of Volume from a value in mega_cubic_feet.

        

        :param meters: The Volume value in mega_cubic_feet.
        :type mega_cubic_feet: float
        :return: A new instance of Volume.
        :rtype: Volume
        """
        return Volume(mega_cubic_feet, VolumeUnits.MegaCubicFoot)

    
    @staticmethod
    def from_kilo_imperial_gallons(kilo_imperial_gallons: float):
        """
        Create a new instance of Volume from a value in kilo_imperial_gallons.

        

        :param meters: The Volume value in kilo_imperial_gallons.
        :type kilo_imperial_gallons: float
        :return: A new instance of Volume.
        :rtype: Volume
        """
        return Volume(kilo_imperial_gallons, VolumeUnits.KiloImperialGallon)

    
    @staticmethod
    def from_mega_imperial_gallons(mega_imperial_gallons: float):
        """
        Create a new instance of Volume from a value in mega_imperial_gallons.

        

        :param meters: The Volume value in mega_imperial_gallons.
        :type mega_imperial_gallons: float
        :return: A new instance of Volume.
        :rtype: Volume
        """
        return Volume(mega_imperial_gallons, VolumeUnits.MegaImperialGallon)

    
    @staticmethod
    def from_deca_us_gallons(deca_us_gallons: float):
        """
        Create a new instance of Volume from a value in deca_us_gallons.

        

        :param meters: The Volume value in deca_us_gallons.
        :type deca_us_gallons: float
        :return: A new instance of Volume.
        :rtype: Volume
        """
        return Volume(deca_us_gallons, VolumeUnits.DecaUsGallon)

    
    @staticmethod
    def from_deci_us_gallons(deci_us_gallons: float):
        """
        Create a new instance of Volume from a value in deci_us_gallons.

        

        :param meters: The Volume value in deci_us_gallons.
        :type deci_us_gallons: float
        :return: A new instance of Volume.
        :rtype: Volume
        """
        return Volume(deci_us_gallons, VolumeUnits.DeciUsGallon)

    
    @staticmethod
    def from_hecto_us_gallons(hecto_us_gallons: float):
        """
        Create a new instance of Volume from a value in hecto_us_gallons.

        

        :param meters: The Volume value in hecto_us_gallons.
        :type hecto_us_gallons: float
        :return: A new instance of Volume.
        :rtype: Volume
        """
        return Volume(hecto_us_gallons, VolumeUnits.HectoUsGallon)

    
    @staticmethod
    def from_kilo_us_gallons(kilo_us_gallons: float):
        """
        Create a new instance of Volume from a value in kilo_us_gallons.

        

        :param meters: The Volume value in kilo_us_gallons.
        :type kilo_us_gallons: float
        :return: A new instance of Volume.
        :rtype: Volume
        """
        return Volume(kilo_us_gallons, VolumeUnits.KiloUsGallon)

    
    @staticmethod
    def from_mega_us_gallons(mega_us_gallons: float):
        """
        Create a new instance of Volume from a value in mega_us_gallons.

        

        :param meters: The Volume value in mega_us_gallons.
        :type mega_us_gallons: float
        :return: A new instance of Volume.
        :rtype: Volume
        """
        return Volume(mega_us_gallons, VolumeUnits.MegaUsGallon)

    
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
    def nano_liters(self) -> float:
        """
        
        """
        if self.__nano_liters != None:
            return self.__nano_liters
        self.__nano_liters = self.__convert_from_base(VolumeUnits.NanoLiter)
        return self.__nano_liters

    
    @property
    def micro_liters(self) -> float:
        """
        
        """
        if self.__micro_liters != None:
            return self.__micro_liters
        self.__micro_liters = self.__convert_from_base(VolumeUnits.MicroLiter)
        return self.__micro_liters

    
    @property
    def milli_liters(self) -> float:
        """
        
        """
        if self.__milli_liters != None:
            return self.__milli_liters
        self.__milli_liters = self.__convert_from_base(VolumeUnits.MilliLiter)
        return self.__milli_liters

    
    @property
    def centi_liters(self) -> float:
        """
        
        """
        if self.__centi_liters != None:
            return self.__centi_liters
        self.__centi_liters = self.__convert_from_base(VolumeUnits.CentiLiter)
        return self.__centi_liters

    
    @property
    def deci_liters(self) -> float:
        """
        
        """
        if self.__deci_liters != None:
            return self.__deci_liters
        self.__deci_liters = self.__convert_from_base(VolumeUnits.DeciLiter)
        return self.__deci_liters

    
    @property
    def deca_liters(self) -> float:
        """
        
        """
        if self.__deca_liters != None:
            return self.__deca_liters
        self.__deca_liters = self.__convert_from_base(VolumeUnits.DecaLiter)
        return self.__deca_liters

    
    @property
    def hecto_liters(self) -> float:
        """
        
        """
        if self.__hecto_liters != None:
            return self.__hecto_liters
        self.__hecto_liters = self.__convert_from_base(VolumeUnits.HectoLiter)
        return self.__hecto_liters

    
    @property
    def kilo_liters(self) -> float:
        """
        
        """
        if self.__kilo_liters != None:
            return self.__kilo_liters
        self.__kilo_liters = self.__convert_from_base(VolumeUnits.KiloLiter)
        return self.__kilo_liters

    
    @property
    def mega_liters(self) -> float:
        """
        
        """
        if self.__mega_liters != None:
            return self.__mega_liters
        self.__mega_liters = self.__convert_from_base(VolumeUnits.MegaLiter)
        return self.__mega_liters

    
    @property
    def hecto_cubic_meters(self) -> float:
        """
        
        """
        if self.__hecto_cubic_meters != None:
            return self.__hecto_cubic_meters
        self.__hecto_cubic_meters = self.__convert_from_base(VolumeUnits.HectoCubicMeter)
        return self.__hecto_cubic_meters

    
    @property
    def kilo_cubic_meters(self) -> float:
        """
        
        """
        if self.__kilo_cubic_meters != None:
            return self.__kilo_cubic_meters
        self.__kilo_cubic_meters = self.__convert_from_base(VolumeUnits.KiloCubicMeter)
        return self.__kilo_cubic_meters

    
    @property
    def hecto_cubic_feet(self) -> float:
        """
        
        """
        if self.__hecto_cubic_feet != None:
            return self.__hecto_cubic_feet
        self.__hecto_cubic_feet = self.__convert_from_base(VolumeUnits.HectoCubicFoot)
        return self.__hecto_cubic_feet

    
    @property
    def kilo_cubic_feet(self) -> float:
        """
        
        """
        if self.__kilo_cubic_feet != None:
            return self.__kilo_cubic_feet
        self.__kilo_cubic_feet = self.__convert_from_base(VolumeUnits.KiloCubicFoot)
        return self.__kilo_cubic_feet

    
    @property
    def mega_cubic_feet(self) -> float:
        """
        
        """
        if self.__mega_cubic_feet != None:
            return self.__mega_cubic_feet
        self.__mega_cubic_feet = self.__convert_from_base(VolumeUnits.MegaCubicFoot)
        return self.__mega_cubic_feet

    
    @property
    def kilo_imperial_gallons(self) -> float:
        """
        
        """
        if self.__kilo_imperial_gallons != None:
            return self.__kilo_imperial_gallons
        self.__kilo_imperial_gallons = self.__convert_from_base(VolumeUnits.KiloImperialGallon)
        return self.__kilo_imperial_gallons

    
    @property
    def mega_imperial_gallons(self) -> float:
        """
        
        """
        if self.__mega_imperial_gallons != None:
            return self.__mega_imperial_gallons
        self.__mega_imperial_gallons = self.__convert_from_base(VolumeUnits.MegaImperialGallon)
        return self.__mega_imperial_gallons

    
    @property
    def deca_us_gallons(self) -> float:
        """
        
        """
        if self.__deca_us_gallons != None:
            return self.__deca_us_gallons
        self.__deca_us_gallons = self.__convert_from_base(VolumeUnits.DecaUsGallon)
        return self.__deca_us_gallons

    
    @property
    def deci_us_gallons(self) -> float:
        """
        
        """
        if self.__deci_us_gallons != None:
            return self.__deci_us_gallons
        self.__deci_us_gallons = self.__convert_from_base(VolumeUnits.DeciUsGallon)
        return self.__deci_us_gallons

    
    @property
    def hecto_us_gallons(self) -> float:
        """
        
        """
        if self.__hecto_us_gallons != None:
            return self.__hecto_us_gallons
        self.__hecto_us_gallons = self.__convert_from_base(VolumeUnits.HectoUsGallon)
        return self.__hecto_us_gallons

    
    @property
    def kilo_us_gallons(self) -> float:
        """
        
        """
        if self.__kilo_us_gallons != None:
            return self.__kilo_us_gallons
        self.__kilo_us_gallons = self.__convert_from_base(VolumeUnits.KiloUsGallon)
        return self.__kilo_us_gallons

    
    @property
    def mega_us_gallons(self) -> float:
        """
        
        """
        if self.__mega_us_gallons != None:
            return self.__mega_us_gallons
        self.__mega_us_gallons = self.__convert_from_base(VolumeUnits.MegaUsGallon)
        return self.__mega_us_gallons

    
    def to_string(self, unit: VolumeUnits = VolumeUnits.CubicMeter) -> string:
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
        
        if unit == VolumeUnits.UsPint:
            return f"""{self.us_pints} pt (U.S.)"""
        
        if unit == VolumeUnits.AcreFoot:
            return f"""{self.acre_feet} ac-ft"""
        
        if unit == VolumeUnits.ImperialPint:
            return f"""{self.imperial_pints} pt (imp.)"""
        
        if unit == VolumeUnits.BoardFoot:
            return f"""{self.board_feet} bf"""
        
        if unit == VolumeUnits.NanoLiter:
            return f"""{self.nano_liters} """
        
        if unit == VolumeUnits.MicroLiter:
            return f"""{self.micro_liters} """
        
        if unit == VolumeUnits.MilliLiter:
            return f"""{self.milli_liters} """
        
        if unit == VolumeUnits.CentiLiter:
            return f"""{self.centi_liters} """
        
        if unit == VolumeUnits.DeciLiter:
            return f"""{self.deci_liters} """
        
        if unit == VolumeUnits.DecaLiter:
            return f"""{self.deca_liters} """
        
        if unit == VolumeUnits.HectoLiter:
            return f"""{self.hecto_liters} """
        
        if unit == VolumeUnits.KiloLiter:
            return f"""{self.kilo_liters} """
        
        if unit == VolumeUnits.MegaLiter:
            return f"""{self.mega_liters} """
        
        if unit == VolumeUnits.HectoCubicMeter:
            return f"""{self.hecto_cubic_meters} """
        
        if unit == VolumeUnits.KiloCubicMeter:
            return f"""{self.kilo_cubic_meters} """
        
        if unit == VolumeUnits.HectoCubicFoot:
            return f"""{self.hecto_cubic_feet} """
        
        if unit == VolumeUnits.KiloCubicFoot:
            return f"""{self.kilo_cubic_feet} """
        
        if unit == VolumeUnits.MegaCubicFoot:
            return f"""{self.mega_cubic_feet} """
        
        if unit == VolumeUnits.KiloImperialGallon:
            return f"""{self.kilo_imperial_gallons} """
        
        if unit == VolumeUnits.MegaImperialGallon:
            return f"""{self.mega_imperial_gallons} """
        
        if unit == VolumeUnits.DecaUsGallon:
            return f"""{self.deca_us_gallons} """
        
        if unit == VolumeUnits.DeciUsGallon:
            return f"""{self.deci_us_gallons} """
        
        if unit == VolumeUnits.HectoUsGallon:
            return f"""{self.hecto_us_gallons} """
        
        if unit == VolumeUnits.KiloUsGallon:
            return f"""{self.kilo_us_gallons} """
        
        if unit == VolumeUnits.MegaUsGallon:
            return f"""{self.mega_us_gallons} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: VolumeUnits = VolumeUnits.CubicMeter) -> string:
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
        
        if unit_abbreviation == VolumeUnits.UsPint:
            return """pt (U.S.)"""
        
        if unit_abbreviation == VolumeUnits.AcreFoot:
            return """ac-ft"""
        
        if unit_abbreviation == VolumeUnits.ImperialPint:
            return """pt (imp.)"""
        
        if unit_abbreviation == VolumeUnits.BoardFoot:
            return """bf"""
        
        if unit_abbreviation == VolumeUnits.NanoLiter:
            return """"""
        
        if unit_abbreviation == VolumeUnits.MicroLiter:
            return """"""
        
        if unit_abbreviation == VolumeUnits.MilliLiter:
            return """"""
        
        if unit_abbreviation == VolumeUnits.CentiLiter:
            return """"""
        
        if unit_abbreviation == VolumeUnits.DeciLiter:
            return """"""
        
        if unit_abbreviation == VolumeUnits.DecaLiter:
            return """"""
        
        if unit_abbreviation == VolumeUnits.HectoLiter:
            return """"""
        
        if unit_abbreviation == VolumeUnits.KiloLiter:
            return """"""
        
        if unit_abbreviation == VolumeUnits.MegaLiter:
            return """"""
        
        if unit_abbreviation == VolumeUnits.HectoCubicMeter:
            return """"""
        
        if unit_abbreviation == VolumeUnits.KiloCubicMeter:
            return """"""
        
        if unit_abbreviation == VolumeUnits.HectoCubicFoot:
            return """"""
        
        if unit_abbreviation == VolumeUnits.KiloCubicFoot:
            return """"""
        
        if unit_abbreviation == VolumeUnits.MegaCubicFoot:
            return """"""
        
        if unit_abbreviation == VolumeUnits.KiloImperialGallon:
            return """"""
        
        if unit_abbreviation == VolumeUnits.MegaImperialGallon:
            return """"""
        
        if unit_abbreviation == VolumeUnits.DecaUsGallon:
            return """"""
        
        if unit_abbreviation == VolumeUnits.DeciUsGallon:
            return """"""
        
        if unit_abbreviation == VolumeUnits.HectoUsGallon:
            return """"""
        
        if unit_abbreviation == VolumeUnits.KiloUsGallon:
            return """"""
        
        if unit_abbreviation == VolumeUnits.MegaUsGallon:
            return """"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, Volume):
            raise TypeError("unsupported operand type(s) for +: 'Volume' and '{}'".format(type(other).__name__))
        return Volume(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, Volume):
            raise TypeError("unsupported operand type(s) for *: 'Volume' and '{}'".format(type(other).__name__))
        return Volume(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, Volume):
            raise TypeError("unsupported operand type(s) for -: 'Volume' and '{}'".format(type(other).__name__))
        return Volume(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, Volume):
            raise TypeError("unsupported operand type(s) for /: 'Volume' and '{}'".format(type(other).__name__))
        return Volume(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, Volume):
            raise TypeError("unsupported operand type(s) for %: 'Volume' and '{}'".format(type(other).__name__))
        return Volume(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, Volume):
            raise TypeError("unsupported operand type(s) for **: 'Volume' and '{}'".format(type(other).__name__))
        return Volume(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, Volume):
            raise TypeError("unsupported operand type(s) for ==: 'Volume' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, Volume):
            raise TypeError("unsupported operand type(s) for <: 'Volume' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, Volume):
            raise TypeError("unsupported operand type(s) for >: 'Volume' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, Volume):
            raise TypeError("unsupported operand type(s) for <=: 'Volume' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, Volume):
            raise TypeError("unsupported operand type(s) for >=: 'Volume' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value
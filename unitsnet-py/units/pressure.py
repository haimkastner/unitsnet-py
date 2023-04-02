from enum import Enum
import math
import string


class PressureUnits(Enum):
        """
            PressureUnits enumeration
        """
        
        Pascal = 'pascal'
        """
            
        """
        
        Atmosphere = 'atmosphere'
        """
            
        """
        
        Bar = 'bar'
        """
            
        """
        
        KilogramForcePerSquareMeter = 'kilogram_force_per_square_meter'
        """
            
        """
        
        KilogramForcePerSquareCentimeter = 'kilogram_force_per_square_centimeter'
        """
            
        """
        
        KilogramForcePerSquareMillimeter = 'kilogram_force_per_square_millimeter'
        """
            
        """
        
        NewtonPerSquareMeter = 'newton_per_square_meter'
        """
            
        """
        
        NewtonPerSquareCentimeter = 'newton_per_square_centimeter'
        """
            
        """
        
        NewtonPerSquareMillimeter = 'newton_per_square_millimeter'
        """
            
        """
        
        TechnicalAtmosphere = 'technical_atmosphere'
        """
            
        """
        
        Torr = 'torr'
        """
            
        """
        
        PoundForcePerSquareInch = 'pound_force_per_square_inch'
        """
            
        """
        
        PoundForcePerSquareMil = 'pound_force_per_square_mil'
        """
            
        """
        
        PoundForcePerSquareFoot = 'pound_force_per_square_foot'
        """
            
        """
        
        TonneForcePerSquareMillimeter = 'tonne_force_per_square_millimeter'
        """
            
        """
        
        TonneForcePerSquareMeter = 'tonne_force_per_square_meter'
        """
            
        """
        
        MeterOfHead = 'meter_of_head'
        """
            
        """
        
        TonneForcePerSquareCentimeter = 'tonne_force_per_square_centimeter'
        """
            
        """
        
        FootOfHead = 'foot_of_head'
        """
            
        """
        
        MillimeterOfMercury = 'millimeter_of_mercury'
        """
            
        """
        
        InchOfMercury = 'inch_of_mercury'
        """
            
        """
        
        DynePerSquareCentimeter = 'dyne_per_square_centimeter'
        """
            
        """
        
        PoundPerInchSecondSquared = 'pound_per_inch_second_squared'
        """
            
        """
        
        MeterOfWaterColumn = 'meter_of_water_column'
        """
            
        """
        
        InchOfWaterColumn = 'inch_of_water_column'
        """
            
        """
        
        MeterOfElevation = 'meter_of_elevation'
        """
            
        """
        
        FootOfElevation = 'foot_of_elevation'
        """
            
        """
        
        Micropascal = 'micropascal'
        """
            
        """
        
        Millipascal = 'millipascal'
        """
            
        """
        
        Decapascal = 'decapascal'
        """
            
        """
        
        Hectopascal = 'hectopascal'
        """
            
        """
        
        Kilopascal = 'kilopascal'
        """
            
        """
        
        Megapascal = 'megapascal'
        """
            
        """
        
        Gigapascal = 'gigapascal'
        """
            
        """
        
        Microbar = 'microbar'
        """
            
        """
        
        Millibar = 'millibar'
        """
            
        """
        
        Centibar = 'centibar'
        """
            
        """
        
        Decibar = 'decibar'
        """
            
        """
        
        Kilobar = 'kilobar'
        """
            
        """
        
        Megabar = 'megabar'
        """
            
        """
        
        KilonewtonPerSquareMeter = 'kilonewton_per_square_meter'
        """
            
        """
        
        MeganewtonPerSquareMeter = 'meganewton_per_square_meter'
        """
            
        """
        
        KilonewtonPerSquareCentimeter = 'kilonewton_per_square_centimeter'
        """
            
        """
        
        KilonewtonPerSquareMillimeter = 'kilonewton_per_square_millimeter'
        """
            
        """
        
        KilopoundForcePerSquareInch = 'kilopound_force_per_square_inch'
        """
            
        """
        
        KilopoundForcePerSquareMil = 'kilopound_force_per_square_mil'
        """
            
        """
        
        KilopoundForcePerSquareFoot = 'kilopound_force_per_square_foot'
        """
            
        """
        
        MillimeterOfWaterColumn = 'millimeter_of_water_column'
        """
            
        """
        
        CentimeterOfWaterColumn = 'centimeter_of_water_column'
        """
            
        """
        

class Pressure:
    """
    Pressure (symbol: P or p) is the ratio of force to the area over which that force is distributed. Pressure is force per unit area applied in a direction perpendicular to the surface of an object. Gauge pressure (also spelled gage pressure)[a] is the pressure relative to the local atmospheric or ambient pressure. Pressure is measured in any unit of force divided by any unit of area. The SI unit of pressure is the newton per square metre, which is called the pascal (Pa) after the seventeenth-century philosopher and scientist Blaise Pascal. A pressure of 1 Pa is small; it approximately equals the pressure exerted by a dollar bill resting flat on a table. Everyday pressures are often stated in kilopascals (1 kPa = 1000 Pa).

    Args:
        value (float): The value.
        from_unit (PressureUnits): The Pressure unit to create from, The default unit is Pascal
    """
    def __init__(self, value: float, from_unit: PressureUnits = PressureUnits.Pascal):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__pascals = None
        
        self.__atmospheres = None
        
        self.__bars = None
        
        self.__kilograms_force_per_square_meter = None
        
        self.__kilograms_force_per_square_centimeter = None
        
        self.__kilograms_force_per_square_millimeter = None
        
        self.__newtons_per_square_meter = None
        
        self.__newtons_per_square_centimeter = None
        
        self.__newtons_per_square_millimeter = None
        
        self.__technical_atmospheres = None
        
        self.__torrs = None
        
        self.__pounds_force_per_square_inch = None
        
        self.__pounds_force_per_square_mil = None
        
        self.__pounds_force_per_square_foot = None
        
        self.__tonnes_force_per_square_millimeter = None
        
        self.__tonnes_force_per_square_meter = None
        
        self.__meters_of_head = None
        
        self.__tonnes_force_per_square_centimeter = None
        
        self.__feet_of_head = None
        
        self.__millimeters_of_mercury = None
        
        self.__inches_of_mercury = None
        
        self.__dynes_per_square_centimeter = None
        
        self.__pounds_per_inch_second_squared = None
        
        self.__meters_of_water_column = None
        
        self.__inches_of_water_column = None
        
        self.__meters_of_elevation = None
        
        self.__feet_of_elevation = None
        
        self.__micropascals = None
        
        self.__millipascals = None
        
        self.__decapascals = None
        
        self.__hectopascals = None
        
        self.__kilopascals = None
        
        self.__megapascals = None
        
        self.__gigapascals = None
        
        self.__microbars = None
        
        self.__millibars = None
        
        self.__centibars = None
        
        self.__decibars = None
        
        self.__kilobars = None
        
        self.__megabars = None
        
        self.__kilonewtons_per_square_meter = None
        
        self.__meganewtons_per_square_meter = None
        
        self.__kilonewtons_per_square_centimeter = None
        
        self.__kilonewtons_per_square_millimeter = None
        
        self.__kilopounds_force_per_square_inch = None
        
        self.__kilopounds_force_per_square_mil = None
        
        self.__kilopounds_force_per_square_foot = None
        
        self.__millimeters_of_water_column = None
        
        self.__centimeters_of_water_column = None
        

    def __convert_from_base(self, from_unit: PressureUnits) -> float:
        value = self.__value
        
        if from_unit == PressureUnits.Pascal:
            return (value)
        
        if from_unit == PressureUnits.Atmosphere:
            return (value / (1.01325 * 1e5))
        
        if from_unit == PressureUnits.Bar:
            return (value / 1e5)
        
        if from_unit == PressureUnits.KilogramForcePerSquareMeter:
            return (value * 0.101971619222242)
        
        if from_unit == PressureUnits.KilogramForcePerSquareCentimeter:
            return (value / 9.80665e4)
        
        if from_unit == PressureUnits.KilogramForcePerSquareMillimeter:
            return (value / 9.80665e6)
        
        if from_unit == PressureUnits.NewtonPerSquareMeter:
            return (value)
        
        if from_unit == PressureUnits.NewtonPerSquareCentimeter:
            return (value / 1e4)
        
        if from_unit == PressureUnits.NewtonPerSquareMillimeter:
            return (value / 1e6)
        
        if from_unit == PressureUnits.TechnicalAtmosphere:
            return (value / (9.80680592331 * 1e4))
        
        if from_unit == PressureUnits.Torr:
            return (value / (1.3332266752 * 1e2))
        
        if from_unit == PressureUnits.PoundForcePerSquareInch:
            return (value / 6.894757293168361e3)
        
        if from_unit == PressureUnits.PoundForcePerSquareMil:
            return (value / 6.894757293168361e9)
        
        if from_unit == PressureUnits.PoundForcePerSquareFoot:
            return (value / 4.788025898033584e1)
        
        if from_unit == PressureUnits.TonneForcePerSquareMillimeter:
            return (value / 9.80665e9)
        
        if from_unit == PressureUnits.TonneForcePerSquareMeter:
            return (value / 9.80665e3)
        
        if from_unit == PressureUnits.MeterOfHead:
            return (value * 0.0001019977334)
        
        if from_unit == PressureUnits.TonneForcePerSquareCentimeter:
            return (value / 9.80665e7)
        
        if from_unit == PressureUnits.FootOfHead:
            return (value * 0.000334552565551)
        
        if from_unit == PressureUnits.MillimeterOfMercury:
            return (value * 7.50061561302643e-3)
        
        if from_unit == PressureUnits.InchOfMercury:
            return (value * 2.95299830714159e-4)
        
        if from_unit == PressureUnits.DynePerSquareCentimeter:
            return (value / 1.0e-1)
        
        if from_unit == PressureUnits.PoundPerInchSecondSquared:
            return (value / 1.785796732283465e1)
        
        if from_unit == PressureUnits.MeterOfWaterColumn:
            return (value / 9.806650000000272e3)
        
        if from_unit == PressureUnits.InchOfWaterColumn:
            return (value / 249.08890833333)
        
        if from_unit == PressureUnits.MeterOfElevation:
            return ((1.0 - math.pow(value / 101325.0, 0.190284)) * 44307.69396)
        
        if from_unit == PressureUnits.FootOfElevation:
            return ((1.0 - math.pow(value / 101325.0, 0.190284)) * 145366.45)
        
        if from_unit == PressureUnits.Micropascal:
            return ((value) / 1e-06)
        
        if from_unit == PressureUnits.Millipascal:
            return ((value) / 0.001)
        
        if from_unit == PressureUnits.Decapascal:
            return ((value) / 10.0)
        
        if from_unit == PressureUnits.Hectopascal:
            return ((value) / 100.0)
        
        if from_unit == PressureUnits.Kilopascal:
            return ((value) / 1000.0)
        
        if from_unit == PressureUnits.Megapascal:
            return ((value) / 1000000.0)
        
        if from_unit == PressureUnits.Gigapascal:
            return ((value) / 1000000000.0)
        
        if from_unit == PressureUnits.Microbar:
            return ((value / 1e5) / 1e-06)
        
        if from_unit == PressureUnits.Millibar:
            return ((value / 1e5) / 0.001)
        
        if from_unit == PressureUnits.Centibar:
            return ((value / 1e5) / 0.01)
        
        if from_unit == PressureUnits.Decibar:
            return ((value / 1e5) / 0.1)
        
        if from_unit == PressureUnits.Kilobar:
            return ((value / 1e5) / 1000.0)
        
        if from_unit == PressureUnits.Megabar:
            return ((value / 1e5) / 1000000.0)
        
        if from_unit == PressureUnits.KilonewtonPerSquareMeter:
            return ((value) / 1000.0)
        
        if from_unit == PressureUnits.MeganewtonPerSquareMeter:
            return ((value) / 1000000.0)
        
        if from_unit == PressureUnits.KilonewtonPerSquareCentimeter:
            return ((value / 1e4) / 1000.0)
        
        if from_unit == PressureUnits.KilonewtonPerSquareMillimeter:
            return ((value / 1e6) / 1000.0)
        
        if from_unit == PressureUnits.KilopoundForcePerSquareInch:
            return ((value / 6.894757293168361e3) / 1000.0)
        
        if from_unit == PressureUnits.KilopoundForcePerSquareMil:
            return ((value / 6.894757293168361e9) / 1000.0)
        
        if from_unit == PressureUnits.KilopoundForcePerSquareFoot:
            return ((value / 4.788025898033584e1) / 1000.0)
        
        if from_unit == PressureUnits.MillimeterOfWaterColumn:
            return ((value / 9.806650000000272e3) / 0.001)
        
        if from_unit == PressureUnits.CentimeterOfWaterColumn:
            return ((value / 9.806650000000272e3) / 0.01)
        
        return None


    def __convert_to_base(self, value: float, to_unit: PressureUnits) -> float:
        
        if to_unit == PressureUnits.Pascal:
            return (value)
        
        if to_unit == PressureUnits.Atmosphere:
            return (value * 1.01325 * 1e5)
        
        if to_unit == PressureUnits.Bar:
            return (value * 1e5)
        
        if to_unit == PressureUnits.KilogramForcePerSquareMeter:
            return (value * 9.80665019960652)
        
        if to_unit == PressureUnits.KilogramForcePerSquareCentimeter:
            return (value * 9.80665e4)
        
        if to_unit == PressureUnits.KilogramForcePerSquareMillimeter:
            return (value * 9.80665e6)
        
        if to_unit == PressureUnits.NewtonPerSquareMeter:
            return (value)
        
        if to_unit == PressureUnits.NewtonPerSquareCentimeter:
            return (value * 1e4)
        
        if to_unit == PressureUnits.NewtonPerSquareMillimeter:
            return (value * 1e6)
        
        if to_unit == PressureUnits.TechnicalAtmosphere:
            return (value * 9.80680592331 * 1e4)
        
        if to_unit == PressureUnits.Torr:
            return (value * 1.3332266752 * 1e2)
        
        if to_unit == PressureUnits.PoundForcePerSquareInch:
            return (value * 6.894757293168361e3)
        
        if to_unit == PressureUnits.PoundForcePerSquareMil:
            return (value * 6.894757293168361e9)
        
        if to_unit == PressureUnits.PoundForcePerSquareFoot:
            return (value * 4.788025898033584e1)
        
        if to_unit == PressureUnits.TonneForcePerSquareMillimeter:
            return (value * 9.80665e9)
        
        if to_unit == PressureUnits.TonneForcePerSquareMeter:
            return (value * 9.80665e3)
        
        if to_unit == PressureUnits.MeterOfHead:
            return (value * 9804.139432)
        
        if to_unit == PressureUnits.TonneForcePerSquareCentimeter:
            return (value * 9.80665e7)
        
        if to_unit == PressureUnits.FootOfHead:
            return (value * 2989.0669)
        
        if to_unit == PressureUnits.MillimeterOfMercury:
            return (value / 7.50061561302643e-3)
        
        if to_unit == PressureUnits.InchOfMercury:
            return (value / 2.95299830714159e-4)
        
        if to_unit == PressureUnits.DynePerSquareCentimeter:
            return (value * 1.0e-1)
        
        if to_unit == PressureUnits.PoundPerInchSecondSquared:
            return (value * 1.785796732283465e1)
        
        if to_unit == PressureUnits.MeterOfWaterColumn:
            return (value * 9.806650000000272e3)
        
        if to_unit == PressureUnits.InchOfWaterColumn:
            return (value * 249.08890833333)
        
        if to_unit == PressureUnits.MeterOfElevation:
            return (math.pow(1.0 - (value / 44307.69396), 5.2553026003237266401799415610351) * 101325.0)
        
        if to_unit == PressureUnits.FootOfElevation:
            return (math.pow(1.0 - (value / 145366.45), 5.2553026003237266401799415610351) * 101325.0)
        
        if to_unit == PressureUnits.Micropascal:
            return ((value) * 1e-06)
        
        if to_unit == PressureUnits.Millipascal:
            return ((value) * 0.001)
        
        if to_unit == PressureUnits.Decapascal:
            return ((value) * 10.0)
        
        if to_unit == PressureUnits.Hectopascal:
            return ((value) * 100.0)
        
        if to_unit == PressureUnits.Kilopascal:
            return ((value) * 1000.0)
        
        if to_unit == PressureUnits.Megapascal:
            return ((value) * 1000000.0)
        
        if to_unit == PressureUnits.Gigapascal:
            return ((value) * 1000000000.0)
        
        if to_unit == PressureUnits.Microbar:
            return ((value * 1e5) * 1e-06)
        
        if to_unit == PressureUnits.Millibar:
            return ((value * 1e5) * 0.001)
        
        if to_unit == PressureUnits.Centibar:
            return ((value * 1e5) * 0.01)
        
        if to_unit == PressureUnits.Decibar:
            return ((value * 1e5) * 0.1)
        
        if to_unit == PressureUnits.Kilobar:
            return ((value * 1e5) * 1000.0)
        
        if to_unit == PressureUnits.Megabar:
            return ((value * 1e5) * 1000000.0)
        
        if to_unit == PressureUnits.KilonewtonPerSquareMeter:
            return ((value) * 1000.0)
        
        if to_unit == PressureUnits.MeganewtonPerSquareMeter:
            return ((value) * 1000000.0)
        
        if to_unit == PressureUnits.KilonewtonPerSquareCentimeter:
            return ((value * 1e4) * 1000.0)
        
        if to_unit == PressureUnits.KilonewtonPerSquareMillimeter:
            return ((value * 1e6) * 1000.0)
        
        if to_unit == PressureUnits.KilopoundForcePerSquareInch:
            return ((value * 6.894757293168361e3) * 1000.0)
        
        if to_unit == PressureUnits.KilopoundForcePerSquareMil:
            return ((value * 6.894757293168361e9) * 1000.0)
        
        if to_unit == PressureUnits.KilopoundForcePerSquareFoot:
            return ((value * 4.788025898033584e1) * 1000.0)
        
        if to_unit == PressureUnits.MillimeterOfWaterColumn:
            return ((value * 9.806650000000272e3) * 0.001)
        
        if to_unit == PressureUnits.CentimeterOfWaterColumn:
            return ((value * 9.806650000000272e3) * 0.01)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
    @staticmethod
    def from_pascals(pascals: float):
        """
        Create a new instance of Pressure from a value in pascals.

        

        :param meters: The Pressure value in pascals.
        :type pascals: float
        :return: A new instance of Pressure.
        :rtype: Pressure
        """
        return Pressure(pascals, PressureUnits.Pascal)

    
    @staticmethod
    def from_atmospheres(atmospheres: float):
        """
        Create a new instance of Pressure from a value in atmospheres.

        

        :param meters: The Pressure value in atmospheres.
        :type atmospheres: float
        :return: A new instance of Pressure.
        :rtype: Pressure
        """
        return Pressure(atmospheres, PressureUnits.Atmosphere)

    
    @staticmethod
    def from_bars(bars: float):
        """
        Create a new instance of Pressure from a value in bars.

        

        :param meters: The Pressure value in bars.
        :type bars: float
        :return: A new instance of Pressure.
        :rtype: Pressure
        """
        return Pressure(bars, PressureUnits.Bar)

    
    @staticmethod
    def from_kilograms_force_per_square_meter(kilograms_force_per_square_meter: float):
        """
        Create a new instance of Pressure from a value in kilograms_force_per_square_meter.

        

        :param meters: The Pressure value in kilograms_force_per_square_meter.
        :type kilograms_force_per_square_meter: float
        :return: A new instance of Pressure.
        :rtype: Pressure
        """
        return Pressure(kilograms_force_per_square_meter, PressureUnits.KilogramForcePerSquareMeter)

    
    @staticmethod
    def from_kilograms_force_per_square_centimeter(kilograms_force_per_square_centimeter: float):
        """
        Create a new instance of Pressure from a value in kilograms_force_per_square_centimeter.

        

        :param meters: The Pressure value in kilograms_force_per_square_centimeter.
        :type kilograms_force_per_square_centimeter: float
        :return: A new instance of Pressure.
        :rtype: Pressure
        """
        return Pressure(kilograms_force_per_square_centimeter, PressureUnits.KilogramForcePerSquareCentimeter)

    
    @staticmethod
    def from_kilograms_force_per_square_millimeter(kilograms_force_per_square_millimeter: float):
        """
        Create a new instance of Pressure from a value in kilograms_force_per_square_millimeter.

        

        :param meters: The Pressure value in kilograms_force_per_square_millimeter.
        :type kilograms_force_per_square_millimeter: float
        :return: A new instance of Pressure.
        :rtype: Pressure
        """
        return Pressure(kilograms_force_per_square_millimeter, PressureUnits.KilogramForcePerSquareMillimeter)

    
    @staticmethod
    def from_newtons_per_square_meter(newtons_per_square_meter: float):
        """
        Create a new instance of Pressure from a value in newtons_per_square_meter.

        

        :param meters: The Pressure value in newtons_per_square_meter.
        :type newtons_per_square_meter: float
        :return: A new instance of Pressure.
        :rtype: Pressure
        """
        return Pressure(newtons_per_square_meter, PressureUnits.NewtonPerSquareMeter)

    
    @staticmethod
    def from_newtons_per_square_centimeter(newtons_per_square_centimeter: float):
        """
        Create a new instance of Pressure from a value in newtons_per_square_centimeter.

        

        :param meters: The Pressure value in newtons_per_square_centimeter.
        :type newtons_per_square_centimeter: float
        :return: A new instance of Pressure.
        :rtype: Pressure
        """
        return Pressure(newtons_per_square_centimeter, PressureUnits.NewtonPerSquareCentimeter)

    
    @staticmethod
    def from_newtons_per_square_millimeter(newtons_per_square_millimeter: float):
        """
        Create a new instance of Pressure from a value in newtons_per_square_millimeter.

        

        :param meters: The Pressure value in newtons_per_square_millimeter.
        :type newtons_per_square_millimeter: float
        :return: A new instance of Pressure.
        :rtype: Pressure
        """
        return Pressure(newtons_per_square_millimeter, PressureUnits.NewtonPerSquareMillimeter)

    
    @staticmethod
    def from_technical_atmospheres(technical_atmospheres: float):
        """
        Create a new instance of Pressure from a value in technical_atmospheres.

        

        :param meters: The Pressure value in technical_atmospheres.
        :type technical_atmospheres: float
        :return: A new instance of Pressure.
        :rtype: Pressure
        """
        return Pressure(technical_atmospheres, PressureUnits.TechnicalAtmosphere)

    
    @staticmethod
    def from_torrs(torrs: float):
        """
        Create a new instance of Pressure from a value in torrs.

        

        :param meters: The Pressure value in torrs.
        :type torrs: float
        :return: A new instance of Pressure.
        :rtype: Pressure
        """
        return Pressure(torrs, PressureUnits.Torr)

    
    @staticmethod
    def from_pounds_force_per_square_inch(pounds_force_per_square_inch: float):
        """
        Create a new instance of Pressure from a value in pounds_force_per_square_inch.

        

        :param meters: The Pressure value in pounds_force_per_square_inch.
        :type pounds_force_per_square_inch: float
        :return: A new instance of Pressure.
        :rtype: Pressure
        """
        return Pressure(pounds_force_per_square_inch, PressureUnits.PoundForcePerSquareInch)

    
    @staticmethod
    def from_pounds_force_per_square_mil(pounds_force_per_square_mil: float):
        """
        Create a new instance of Pressure from a value in pounds_force_per_square_mil.

        

        :param meters: The Pressure value in pounds_force_per_square_mil.
        :type pounds_force_per_square_mil: float
        :return: A new instance of Pressure.
        :rtype: Pressure
        """
        return Pressure(pounds_force_per_square_mil, PressureUnits.PoundForcePerSquareMil)

    
    @staticmethod
    def from_pounds_force_per_square_foot(pounds_force_per_square_foot: float):
        """
        Create a new instance of Pressure from a value in pounds_force_per_square_foot.

        

        :param meters: The Pressure value in pounds_force_per_square_foot.
        :type pounds_force_per_square_foot: float
        :return: A new instance of Pressure.
        :rtype: Pressure
        """
        return Pressure(pounds_force_per_square_foot, PressureUnits.PoundForcePerSquareFoot)

    
    @staticmethod
    def from_tonnes_force_per_square_millimeter(tonnes_force_per_square_millimeter: float):
        """
        Create a new instance of Pressure from a value in tonnes_force_per_square_millimeter.

        

        :param meters: The Pressure value in tonnes_force_per_square_millimeter.
        :type tonnes_force_per_square_millimeter: float
        :return: A new instance of Pressure.
        :rtype: Pressure
        """
        return Pressure(tonnes_force_per_square_millimeter, PressureUnits.TonneForcePerSquareMillimeter)

    
    @staticmethod
    def from_tonnes_force_per_square_meter(tonnes_force_per_square_meter: float):
        """
        Create a new instance of Pressure from a value in tonnes_force_per_square_meter.

        

        :param meters: The Pressure value in tonnes_force_per_square_meter.
        :type tonnes_force_per_square_meter: float
        :return: A new instance of Pressure.
        :rtype: Pressure
        """
        return Pressure(tonnes_force_per_square_meter, PressureUnits.TonneForcePerSquareMeter)

    
    @staticmethod
    def from_meters_of_head(meters_of_head: float):
        """
        Create a new instance of Pressure from a value in meters_of_head.

        

        :param meters: The Pressure value in meters_of_head.
        :type meters_of_head: float
        :return: A new instance of Pressure.
        :rtype: Pressure
        """
        return Pressure(meters_of_head, PressureUnits.MeterOfHead)

    
    @staticmethod
    def from_tonnes_force_per_square_centimeter(tonnes_force_per_square_centimeter: float):
        """
        Create a new instance of Pressure from a value in tonnes_force_per_square_centimeter.

        

        :param meters: The Pressure value in tonnes_force_per_square_centimeter.
        :type tonnes_force_per_square_centimeter: float
        :return: A new instance of Pressure.
        :rtype: Pressure
        """
        return Pressure(tonnes_force_per_square_centimeter, PressureUnits.TonneForcePerSquareCentimeter)

    
    @staticmethod
    def from_feet_of_head(feet_of_head: float):
        """
        Create a new instance of Pressure from a value in feet_of_head.

        

        :param meters: The Pressure value in feet_of_head.
        :type feet_of_head: float
        :return: A new instance of Pressure.
        :rtype: Pressure
        """
        return Pressure(feet_of_head, PressureUnits.FootOfHead)

    
    @staticmethod
    def from_millimeters_of_mercury(millimeters_of_mercury: float):
        """
        Create a new instance of Pressure from a value in millimeters_of_mercury.

        

        :param meters: The Pressure value in millimeters_of_mercury.
        :type millimeters_of_mercury: float
        :return: A new instance of Pressure.
        :rtype: Pressure
        """
        return Pressure(millimeters_of_mercury, PressureUnits.MillimeterOfMercury)

    
    @staticmethod
    def from_inches_of_mercury(inches_of_mercury: float):
        """
        Create a new instance of Pressure from a value in inches_of_mercury.

        

        :param meters: The Pressure value in inches_of_mercury.
        :type inches_of_mercury: float
        :return: A new instance of Pressure.
        :rtype: Pressure
        """
        return Pressure(inches_of_mercury, PressureUnits.InchOfMercury)

    
    @staticmethod
    def from_dynes_per_square_centimeter(dynes_per_square_centimeter: float):
        """
        Create a new instance of Pressure from a value in dynes_per_square_centimeter.

        

        :param meters: The Pressure value in dynes_per_square_centimeter.
        :type dynes_per_square_centimeter: float
        :return: A new instance of Pressure.
        :rtype: Pressure
        """
        return Pressure(dynes_per_square_centimeter, PressureUnits.DynePerSquareCentimeter)

    
    @staticmethod
    def from_pounds_per_inch_second_squared(pounds_per_inch_second_squared: float):
        """
        Create a new instance of Pressure from a value in pounds_per_inch_second_squared.

        

        :param meters: The Pressure value in pounds_per_inch_second_squared.
        :type pounds_per_inch_second_squared: float
        :return: A new instance of Pressure.
        :rtype: Pressure
        """
        return Pressure(pounds_per_inch_second_squared, PressureUnits.PoundPerInchSecondSquared)

    
    @staticmethod
    def from_meters_of_water_column(meters_of_water_column: float):
        """
        Create a new instance of Pressure from a value in meters_of_water_column.

        

        :param meters: The Pressure value in meters_of_water_column.
        :type meters_of_water_column: float
        :return: A new instance of Pressure.
        :rtype: Pressure
        """
        return Pressure(meters_of_water_column, PressureUnits.MeterOfWaterColumn)

    
    @staticmethod
    def from_inches_of_water_column(inches_of_water_column: float):
        """
        Create a new instance of Pressure from a value in inches_of_water_column.

        

        :param meters: The Pressure value in inches_of_water_column.
        :type inches_of_water_column: float
        :return: A new instance of Pressure.
        :rtype: Pressure
        """
        return Pressure(inches_of_water_column, PressureUnits.InchOfWaterColumn)

    
    @staticmethod
    def from_meters_of_elevation(meters_of_elevation: float):
        """
        Create a new instance of Pressure from a value in meters_of_elevation.

        

        :param meters: The Pressure value in meters_of_elevation.
        :type meters_of_elevation: float
        :return: A new instance of Pressure.
        :rtype: Pressure
        """
        return Pressure(meters_of_elevation, PressureUnits.MeterOfElevation)

    
    @staticmethod
    def from_feet_of_elevation(feet_of_elevation: float):
        """
        Create a new instance of Pressure from a value in feet_of_elevation.

        

        :param meters: The Pressure value in feet_of_elevation.
        :type feet_of_elevation: float
        :return: A new instance of Pressure.
        :rtype: Pressure
        """
        return Pressure(feet_of_elevation, PressureUnits.FootOfElevation)

    
    @staticmethod
    def from_micropascals(micropascals: float):
        """
        Create a new instance of Pressure from a value in micropascals.

        

        :param meters: The Pressure value in micropascals.
        :type micropascals: float
        :return: A new instance of Pressure.
        :rtype: Pressure
        """
        return Pressure(micropascals, PressureUnits.Micropascal)

    
    @staticmethod
    def from_millipascals(millipascals: float):
        """
        Create a new instance of Pressure from a value in millipascals.

        

        :param meters: The Pressure value in millipascals.
        :type millipascals: float
        :return: A new instance of Pressure.
        :rtype: Pressure
        """
        return Pressure(millipascals, PressureUnits.Millipascal)

    
    @staticmethod
    def from_decapascals(decapascals: float):
        """
        Create a new instance of Pressure from a value in decapascals.

        

        :param meters: The Pressure value in decapascals.
        :type decapascals: float
        :return: A new instance of Pressure.
        :rtype: Pressure
        """
        return Pressure(decapascals, PressureUnits.Decapascal)

    
    @staticmethod
    def from_hectopascals(hectopascals: float):
        """
        Create a new instance of Pressure from a value in hectopascals.

        

        :param meters: The Pressure value in hectopascals.
        :type hectopascals: float
        :return: A new instance of Pressure.
        :rtype: Pressure
        """
        return Pressure(hectopascals, PressureUnits.Hectopascal)

    
    @staticmethod
    def from_kilopascals(kilopascals: float):
        """
        Create a new instance of Pressure from a value in kilopascals.

        

        :param meters: The Pressure value in kilopascals.
        :type kilopascals: float
        :return: A new instance of Pressure.
        :rtype: Pressure
        """
        return Pressure(kilopascals, PressureUnits.Kilopascal)

    
    @staticmethod
    def from_megapascals(megapascals: float):
        """
        Create a new instance of Pressure from a value in megapascals.

        

        :param meters: The Pressure value in megapascals.
        :type megapascals: float
        :return: A new instance of Pressure.
        :rtype: Pressure
        """
        return Pressure(megapascals, PressureUnits.Megapascal)

    
    @staticmethod
    def from_gigapascals(gigapascals: float):
        """
        Create a new instance of Pressure from a value in gigapascals.

        

        :param meters: The Pressure value in gigapascals.
        :type gigapascals: float
        :return: A new instance of Pressure.
        :rtype: Pressure
        """
        return Pressure(gigapascals, PressureUnits.Gigapascal)

    
    @staticmethod
    def from_microbars(microbars: float):
        """
        Create a new instance of Pressure from a value in microbars.

        

        :param meters: The Pressure value in microbars.
        :type microbars: float
        :return: A new instance of Pressure.
        :rtype: Pressure
        """
        return Pressure(microbars, PressureUnits.Microbar)

    
    @staticmethod
    def from_millibars(millibars: float):
        """
        Create a new instance of Pressure from a value in millibars.

        

        :param meters: The Pressure value in millibars.
        :type millibars: float
        :return: A new instance of Pressure.
        :rtype: Pressure
        """
        return Pressure(millibars, PressureUnits.Millibar)

    
    @staticmethod
    def from_centibars(centibars: float):
        """
        Create a new instance of Pressure from a value in centibars.

        

        :param meters: The Pressure value in centibars.
        :type centibars: float
        :return: A new instance of Pressure.
        :rtype: Pressure
        """
        return Pressure(centibars, PressureUnits.Centibar)

    
    @staticmethod
    def from_decibars(decibars: float):
        """
        Create a new instance of Pressure from a value in decibars.

        

        :param meters: The Pressure value in decibars.
        :type decibars: float
        :return: A new instance of Pressure.
        :rtype: Pressure
        """
        return Pressure(decibars, PressureUnits.Decibar)

    
    @staticmethod
    def from_kilobars(kilobars: float):
        """
        Create a new instance of Pressure from a value in kilobars.

        

        :param meters: The Pressure value in kilobars.
        :type kilobars: float
        :return: A new instance of Pressure.
        :rtype: Pressure
        """
        return Pressure(kilobars, PressureUnits.Kilobar)

    
    @staticmethod
    def from_megabars(megabars: float):
        """
        Create a new instance of Pressure from a value in megabars.

        

        :param meters: The Pressure value in megabars.
        :type megabars: float
        :return: A new instance of Pressure.
        :rtype: Pressure
        """
        return Pressure(megabars, PressureUnits.Megabar)

    
    @staticmethod
    def from_kilonewtons_per_square_meter(kilonewtons_per_square_meter: float):
        """
        Create a new instance of Pressure from a value in kilonewtons_per_square_meter.

        

        :param meters: The Pressure value in kilonewtons_per_square_meter.
        :type kilonewtons_per_square_meter: float
        :return: A new instance of Pressure.
        :rtype: Pressure
        """
        return Pressure(kilonewtons_per_square_meter, PressureUnits.KilonewtonPerSquareMeter)

    
    @staticmethod
    def from_meganewtons_per_square_meter(meganewtons_per_square_meter: float):
        """
        Create a new instance of Pressure from a value in meganewtons_per_square_meter.

        

        :param meters: The Pressure value in meganewtons_per_square_meter.
        :type meganewtons_per_square_meter: float
        :return: A new instance of Pressure.
        :rtype: Pressure
        """
        return Pressure(meganewtons_per_square_meter, PressureUnits.MeganewtonPerSquareMeter)

    
    @staticmethod
    def from_kilonewtons_per_square_centimeter(kilonewtons_per_square_centimeter: float):
        """
        Create a new instance of Pressure from a value in kilonewtons_per_square_centimeter.

        

        :param meters: The Pressure value in kilonewtons_per_square_centimeter.
        :type kilonewtons_per_square_centimeter: float
        :return: A new instance of Pressure.
        :rtype: Pressure
        """
        return Pressure(kilonewtons_per_square_centimeter, PressureUnits.KilonewtonPerSquareCentimeter)

    
    @staticmethod
    def from_kilonewtons_per_square_millimeter(kilonewtons_per_square_millimeter: float):
        """
        Create a new instance of Pressure from a value in kilonewtons_per_square_millimeter.

        

        :param meters: The Pressure value in kilonewtons_per_square_millimeter.
        :type kilonewtons_per_square_millimeter: float
        :return: A new instance of Pressure.
        :rtype: Pressure
        """
        return Pressure(kilonewtons_per_square_millimeter, PressureUnits.KilonewtonPerSquareMillimeter)

    
    @staticmethod
    def from_kilopounds_force_per_square_inch(kilopounds_force_per_square_inch: float):
        """
        Create a new instance of Pressure from a value in kilopounds_force_per_square_inch.

        

        :param meters: The Pressure value in kilopounds_force_per_square_inch.
        :type kilopounds_force_per_square_inch: float
        :return: A new instance of Pressure.
        :rtype: Pressure
        """
        return Pressure(kilopounds_force_per_square_inch, PressureUnits.KilopoundForcePerSquareInch)

    
    @staticmethod
    def from_kilopounds_force_per_square_mil(kilopounds_force_per_square_mil: float):
        """
        Create a new instance of Pressure from a value in kilopounds_force_per_square_mil.

        

        :param meters: The Pressure value in kilopounds_force_per_square_mil.
        :type kilopounds_force_per_square_mil: float
        :return: A new instance of Pressure.
        :rtype: Pressure
        """
        return Pressure(kilopounds_force_per_square_mil, PressureUnits.KilopoundForcePerSquareMil)

    
    @staticmethod
    def from_kilopounds_force_per_square_foot(kilopounds_force_per_square_foot: float):
        """
        Create a new instance of Pressure from a value in kilopounds_force_per_square_foot.

        

        :param meters: The Pressure value in kilopounds_force_per_square_foot.
        :type kilopounds_force_per_square_foot: float
        :return: A new instance of Pressure.
        :rtype: Pressure
        """
        return Pressure(kilopounds_force_per_square_foot, PressureUnits.KilopoundForcePerSquareFoot)

    
    @staticmethod
    def from_millimeters_of_water_column(millimeters_of_water_column: float):
        """
        Create a new instance of Pressure from a value in millimeters_of_water_column.

        

        :param meters: The Pressure value in millimeters_of_water_column.
        :type millimeters_of_water_column: float
        :return: A new instance of Pressure.
        :rtype: Pressure
        """
        return Pressure(millimeters_of_water_column, PressureUnits.MillimeterOfWaterColumn)

    
    @staticmethod
    def from_centimeters_of_water_column(centimeters_of_water_column: float):
        """
        Create a new instance of Pressure from a value in centimeters_of_water_column.

        

        :param meters: The Pressure value in centimeters_of_water_column.
        :type centimeters_of_water_column: float
        :return: A new instance of Pressure.
        :rtype: Pressure
        """
        return Pressure(centimeters_of_water_column, PressureUnits.CentimeterOfWaterColumn)

    
    @property
    def pascals(self) -> float:
        """
        
        """
        if self.__pascals != None:
            return self.__pascals
        self.__pascals = self.__convert_from_base(PressureUnits.Pascal)
        return self.__pascals

    
    @property
    def atmospheres(self) -> float:
        """
        
        """
        if self.__atmospheres != None:
            return self.__atmospheres
        self.__atmospheres = self.__convert_from_base(PressureUnits.Atmosphere)
        return self.__atmospheres

    
    @property
    def bars(self) -> float:
        """
        
        """
        if self.__bars != None:
            return self.__bars
        self.__bars = self.__convert_from_base(PressureUnits.Bar)
        return self.__bars

    
    @property
    def kilograms_force_per_square_meter(self) -> float:
        """
        
        """
        if self.__kilograms_force_per_square_meter != None:
            return self.__kilograms_force_per_square_meter
        self.__kilograms_force_per_square_meter = self.__convert_from_base(PressureUnits.KilogramForcePerSquareMeter)
        return self.__kilograms_force_per_square_meter

    
    @property
    def kilograms_force_per_square_centimeter(self) -> float:
        """
        
        """
        if self.__kilograms_force_per_square_centimeter != None:
            return self.__kilograms_force_per_square_centimeter
        self.__kilograms_force_per_square_centimeter = self.__convert_from_base(PressureUnits.KilogramForcePerSquareCentimeter)
        return self.__kilograms_force_per_square_centimeter

    
    @property
    def kilograms_force_per_square_millimeter(self) -> float:
        """
        
        """
        if self.__kilograms_force_per_square_millimeter != None:
            return self.__kilograms_force_per_square_millimeter
        self.__kilograms_force_per_square_millimeter = self.__convert_from_base(PressureUnits.KilogramForcePerSquareMillimeter)
        return self.__kilograms_force_per_square_millimeter

    
    @property
    def newtons_per_square_meter(self) -> float:
        """
        
        """
        if self.__newtons_per_square_meter != None:
            return self.__newtons_per_square_meter
        self.__newtons_per_square_meter = self.__convert_from_base(PressureUnits.NewtonPerSquareMeter)
        return self.__newtons_per_square_meter

    
    @property
    def newtons_per_square_centimeter(self) -> float:
        """
        
        """
        if self.__newtons_per_square_centimeter != None:
            return self.__newtons_per_square_centimeter
        self.__newtons_per_square_centimeter = self.__convert_from_base(PressureUnits.NewtonPerSquareCentimeter)
        return self.__newtons_per_square_centimeter

    
    @property
    def newtons_per_square_millimeter(self) -> float:
        """
        
        """
        if self.__newtons_per_square_millimeter != None:
            return self.__newtons_per_square_millimeter
        self.__newtons_per_square_millimeter = self.__convert_from_base(PressureUnits.NewtonPerSquareMillimeter)
        return self.__newtons_per_square_millimeter

    
    @property
    def technical_atmospheres(self) -> float:
        """
        
        """
        if self.__technical_atmospheres != None:
            return self.__technical_atmospheres
        self.__technical_atmospheres = self.__convert_from_base(PressureUnits.TechnicalAtmosphere)
        return self.__technical_atmospheres

    
    @property
    def torrs(self) -> float:
        """
        
        """
        if self.__torrs != None:
            return self.__torrs
        self.__torrs = self.__convert_from_base(PressureUnits.Torr)
        return self.__torrs

    
    @property
    def pounds_force_per_square_inch(self) -> float:
        """
        
        """
        if self.__pounds_force_per_square_inch != None:
            return self.__pounds_force_per_square_inch
        self.__pounds_force_per_square_inch = self.__convert_from_base(PressureUnits.PoundForcePerSquareInch)
        return self.__pounds_force_per_square_inch

    
    @property
    def pounds_force_per_square_mil(self) -> float:
        """
        
        """
        if self.__pounds_force_per_square_mil != None:
            return self.__pounds_force_per_square_mil
        self.__pounds_force_per_square_mil = self.__convert_from_base(PressureUnits.PoundForcePerSquareMil)
        return self.__pounds_force_per_square_mil

    
    @property
    def pounds_force_per_square_foot(self) -> float:
        """
        
        """
        if self.__pounds_force_per_square_foot != None:
            return self.__pounds_force_per_square_foot
        self.__pounds_force_per_square_foot = self.__convert_from_base(PressureUnits.PoundForcePerSquareFoot)
        return self.__pounds_force_per_square_foot

    
    @property
    def tonnes_force_per_square_millimeter(self) -> float:
        """
        
        """
        if self.__tonnes_force_per_square_millimeter != None:
            return self.__tonnes_force_per_square_millimeter
        self.__tonnes_force_per_square_millimeter = self.__convert_from_base(PressureUnits.TonneForcePerSquareMillimeter)
        return self.__tonnes_force_per_square_millimeter

    
    @property
    def tonnes_force_per_square_meter(self) -> float:
        """
        
        """
        if self.__tonnes_force_per_square_meter != None:
            return self.__tonnes_force_per_square_meter
        self.__tonnes_force_per_square_meter = self.__convert_from_base(PressureUnits.TonneForcePerSquareMeter)
        return self.__tonnes_force_per_square_meter

    
    @property
    def meters_of_head(self) -> float:
        """
        
        """
        if self.__meters_of_head != None:
            return self.__meters_of_head
        self.__meters_of_head = self.__convert_from_base(PressureUnits.MeterOfHead)
        return self.__meters_of_head

    
    @property
    def tonnes_force_per_square_centimeter(self) -> float:
        """
        
        """
        if self.__tonnes_force_per_square_centimeter != None:
            return self.__tonnes_force_per_square_centimeter
        self.__tonnes_force_per_square_centimeter = self.__convert_from_base(PressureUnits.TonneForcePerSquareCentimeter)
        return self.__tonnes_force_per_square_centimeter

    
    @property
    def feet_of_head(self) -> float:
        """
        
        """
        if self.__feet_of_head != None:
            return self.__feet_of_head
        self.__feet_of_head = self.__convert_from_base(PressureUnits.FootOfHead)
        return self.__feet_of_head

    
    @property
    def millimeters_of_mercury(self) -> float:
        """
        
        """
        if self.__millimeters_of_mercury != None:
            return self.__millimeters_of_mercury
        self.__millimeters_of_mercury = self.__convert_from_base(PressureUnits.MillimeterOfMercury)
        return self.__millimeters_of_mercury

    
    @property
    def inches_of_mercury(self) -> float:
        """
        
        """
        if self.__inches_of_mercury != None:
            return self.__inches_of_mercury
        self.__inches_of_mercury = self.__convert_from_base(PressureUnits.InchOfMercury)
        return self.__inches_of_mercury

    
    @property
    def dynes_per_square_centimeter(self) -> float:
        """
        
        """
        if self.__dynes_per_square_centimeter != None:
            return self.__dynes_per_square_centimeter
        self.__dynes_per_square_centimeter = self.__convert_from_base(PressureUnits.DynePerSquareCentimeter)
        return self.__dynes_per_square_centimeter

    
    @property
    def pounds_per_inch_second_squared(self) -> float:
        """
        
        """
        if self.__pounds_per_inch_second_squared != None:
            return self.__pounds_per_inch_second_squared
        self.__pounds_per_inch_second_squared = self.__convert_from_base(PressureUnits.PoundPerInchSecondSquared)
        return self.__pounds_per_inch_second_squared

    
    @property
    def meters_of_water_column(self) -> float:
        """
        
        """
        if self.__meters_of_water_column != None:
            return self.__meters_of_water_column
        self.__meters_of_water_column = self.__convert_from_base(PressureUnits.MeterOfWaterColumn)
        return self.__meters_of_water_column

    
    @property
    def inches_of_water_column(self) -> float:
        """
        
        """
        if self.__inches_of_water_column != None:
            return self.__inches_of_water_column
        self.__inches_of_water_column = self.__convert_from_base(PressureUnits.InchOfWaterColumn)
        return self.__inches_of_water_column

    
    @property
    def meters_of_elevation(self) -> float:
        """
        
        """
        if self.__meters_of_elevation != None:
            return self.__meters_of_elevation
        self.__meters_of_elevation = self.__convert_from_base(PressureUnits.MeterOfElevation)
        return self.__meters_of_elevation

    
    @property
    def feet_of_elevation(self) -> float:
        """
        
        """
        if self.__feet_of_elevation != None:
            return self.__feet_of_elevation
        self.__feet_of_elevation = self.__convert_from_base(PressureUnits.FootOfElevation)
        return self.__feet_of_elevation

    
    @property
    def micropascals(self) -> float:
        """
        
        """
        if self.__micropascals != None:
            return self.__micropascals
        self.__micropascals = self.__convert_from_base(PressureUnits.Micropascal)
        return self.__micropascals

    
    @property
    def millipascals(self) -> float:
        """
        
        """
        if self.__millipascals != None:
            return self.__millipascals
        self.__millipascals = self.__convert_from_base(PressureUnits.Millipascal)
        return self.__millipascals

    
    @property
    def decapascals(self) -> float:
        """
        
        """
        if self.__decapascals != None:
            return self.__decapascals
        self.__decapascals = self.__convert_from_base(PressureUnits.Decapascal)
        return self.__decapascals

    
    @property
    def hectopascals(self) -> float:
        """
        
        """
        if self.__hectopascals != None:
            return self.__hectopascals
        self.__hectopascals = self.__convert_from_base(PressureUnits.Hectopascal)
        return self.__hectopascals

    
    @property
    def kilopascals(self) -> float:
        """
        
        """
        if self.__kilopascals != None:
            return self.__kilopascals
        self.__kilopascals = self.__convert_from_base(PressureUnits.Kilopascal)
        return self.__kilopascals

    
    @property
    def megapascals(self) -> float:
        """
        
        """
        if self.__megapascals != None:
            return self.__megapascals
        self.__megapascals = self.__convert_from_base(PressureUnits.Megapascal)
        return self.__megapascals

    
    @property
    def gigapascals(self) -> float:
        """
        
        """
        if self.__gigapascals != None:
            return self.__gigapascals
        self.__gigapascals = self.__convert_from_base(PressureUnits.Gigapascal)
        return self.__gigapascals

    
    @property
    def microbars(self) -> float:
        """
        
        """
        if self.__microbars != None:
            return self.__microbars
        self.__microbars = self.__convert_from_base(PressureUnits.Microbar)
        return self.__microbars

    
    @property
    def millibars(self) -> float:
        """
        
        """
        if self.__millibars != None:
            return self.__millibars
        self.__millibars = self.__convert_from_base(PressureUnits.Millibar)
        return self.__millibars

    
    @property
    def centibars(self) -> float:
        """
        
        """
        if self.__centibars != None:
            return self.__centibars
        self.__centibars = self.__convert_from_base(PressureUnits.Centibar)
        return self.__centibars

    
    @property
    def decibars(self) -> float:
        """
        
        """
        if self.__decibars != None:
            return self.__decibars
        self.__decibars = self.__convert_from_base(PressureUnits.Decibar)
        return self.__decibars

    
    @property
    def kilobars(self) -> float:
        """
        
        """
        if self.__kilobars != None:
            return self.__kilobars
        self.__kilobars = self.__convert_from_base(PressureUnits.Kilobar)
        return self.__kilobars

    
    @property
    def megabars(self) -> float:
        """
        
        """
        if self.__megabars != None:
            return self.__megabars
        self.__megabars = self.__convert_from_base(PressureUnits.Megabar)
        return self.__megabars

    
    @property
    def kilonewtons_per_square_meter(self) -> float:
        """
        
        """
        if self.__kilonewtons_per_square_meter != None:
            return self.__kilonewtons_per_square_meter
        self.__kilonewtons_per_square_meter = self.__convert_from_base(PressureUnits.KilonewtonPerSquareMeter)
        return self.__kilonewtons_per_square_meter

    
    @property
    def meganewtons_per_square_meter(self) -> float:
        """
        
        """
        if self.__meganewtons_per_square_meter != None:
            return self.__meganewtons_per_square_meter
        self.__meganewtons_per_square_meter = self.__convert_from_base(PressureUnits.MeganewtonPerSquareMeter)
        return self.__meganewtons_per_square_meter

    
    @property
    def kilonewtons_per_square_centimeter(self) -> float:
        """
        
        """
        if self.__kilonewtons_per_square_centimeter != None:
            return self.__kilonewtons_per_square_centimeter
        self.__kilonewtons_per_square_centimeter = self.__convert_from_base(PressureUnits.KilonewtonPerSquareCentimeter)
        return self.__kilonewtons_per_square_centimeter

    
    @property
    def kilonewtons_per_square_millimeter(self) -> float:
        """
        
        """
        if self.__kilonewtons_per_square_millimeter != None:
            return self.__kilonewtons_per_square_millimeter
        self.__kilonewtons_per_square_millimeter = self.__convert_from_base(PressureUnits.KilonewtonPerSquareMillimeter)
        return self.__kilonewtons_per_square_millimeter

    
    @property
    def kilopounds_force_per_square_inch(self) -> float:
        """
        
        """
        if self.__kilopounds_force_per_square_inch != None:
            return self.__kilopounds_force_per_square_inch
        self.__kilopounds_force_per_square_inch = self.__convert_from_base(PressureUnits.KilopoundForcePerSquareInch)
        return self.__kilopounds_force_per_square_inch

    
    @property
    def kilopounds_force_per_square_mil(self) -> float:
        """
        
        """
        if self.__kilopounds_force_per_square_mil != None:
            return self.__kilopounds_force_per_square_mil
        self.__kilopounds_force_per_square_mil = self.__convert_from_base(PressureUnits.KilopoundForcePerSquareMil)
        return self.__kilopounds_force_per_square_mil

    
    @property
    def kilopounds_force_per_square_foot(self) -> float:
        """
        
        """
        if self.__kilopounds_force_per_square_foot != None:
            return self.__kilopounds_force_per_square_foot
        self.__kilopounds_force_per_square_foot = self.__convert_from_base(PressureUnits.KilopoundForcePerSquareFoot)
        return self.__kilopounds_force_per_square_foot

    
    @property
    def millimeters_of_water_column(self) -> float:
        """
        
        """
        if self.__millimeters_of_water_column != None:
            return self.__millimeters_of_water_column
        self.__millimeters_of_water_column = self.__convert_from_base(PressureUnits.MillimeterOfWaterColumn)
        return self.__millimeters_of_water_column

    
    @property
    def centimeters_of_water_column(self) -> float:
        """
        
        """
        if self.__centimeters_of_water_column != None:
            return self.__centimeters_of_water_column
        self.__centimeters_of_water_column = self.__convert_from_base(PressureUnits.CentimeterOfWaterColumn)
        return self.__centimeters_of_water_column

    
    def to_string(self, unit: PressureUnits = PressureUnits.Pascal) -> string:
        """
        Format the Pressure to string.
        Note! the default format for Pressure is Pascal.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == PressureUnits.Pascal:
            return f"""{self.pascals} Pa"""
        
        if unit == PressureUnits.Atmosphere:
            return f"""{self.atmospheres} atm"""
        
        if unit == PressureUnits.Bar:
            return f"""{self.bars} bar"""
        
        if unit == PressureUnits.KilogramForcePerSquareMeter:
            return f"""{self.kilograms_force_per_square_meter} kgf/m²"""
        
        if unit == PressureUnits.KilogramForcePerSquareCentimeter:
            return f"""{self.kilograms_force_per_square_centimeter} kgf/cm²"""
        
        if unit == PressureUnits.KilogramForcePerSquareMillimeter:
            return f"""{self.kilograms_force_per_square_millimeter} kgf/mm²"""
        
        if unit == PressureUnits.NewtonPerSquareMeter:
            return f"""{self.newtons_per_square_meter} N/m²"""
        
        if unit == PressureUnits.NewtonPerSquareCentimeter:
            return f"""{self.newtons_per_square_centimeter} N/cm²"""
        
        if unit == PressureUnits.NewtonPerSquareMillimeter:
            return f"""{self.newtons_per_square_millimeter} N/mm²"""
        
        if unit == PressureUnits.TechnicalAtmosphere:
            return f"""{self.technical_atmospheres} at"""
        
        if unit == PressureUnits.Torr:
            return f"""{self.torrs} torr"""
        
        if unit == PressureUnits.PoundForcePerSquareInch:
            return f"""{self.pounds_force_per_square_inch} psi"""
        
        if unit == PressureUnits.PoundForcePerSquareMil:
            return f"""{self.pounds_force_per_square_mil} lb/mil²"""
        
        if unit == PressureUnits.PoundForcePerSquareFoot:
            return f"""{self.pounds_force_per_square_foot} lb/ft²"""
        
        if unit == PressureUnits.TonneForcePerSquareMillimeter:
            return f"""{self.tonnes_force_per_square_millimeter} tf/mm²"""
        
        if unit == PressureUnits.TonneForcePerSquareMeter:
            return f"""{self.tonnes_force_per_square_meter} tf/m²"""
        
        if unit == PressureUnits.MeterOfHead:
            return f"""{self.meters_of_head} m of head"""
        
        if unit == PressureUnits.TonneForcePerSquareCentimeter:
            return f"""{self.tonnes_force_per_square_centimeter} tf/cm²"""
        
        if unit == PressureUnits.FootOfHead:
            return f"""{self.feet_of_head} ft of head"""
        
        if unit == PressureUnits.MillimeterOfMercury:
            return f"""{self.millimeters_of_mercury} mmHg"""
        
        if unit == PressureUnits.InchOfMercury:
            return f"""{self.inches_of_mercury} inHg"""
        
        if unit == PressureUnits.DynePerSquareCentimeter:
            return f"""{self.dynes_per_square_centimeter} dyn/cm²"""
        
        if unit == PressureUnits.PoundPerInchSecondSquared:
            return f"""{self.pounds_per_inch_second_squared} lbm/(in·s²)"""
        
        if unit == PressureUnits.MeterOfWaterColumn:
            return f"""{self.meters_of_water_column} mH₂O"""
        
        if unit == PressureUnits.InchOfWaterColumn:
            return f"""{self.inches_of_water_column} inH2O"""
        
        if unit == PressureUnits.MeterOfElevation:
            return f"""{self.meters_of_elevation} m of elevation"""
        
        if unit == PressureUnits.FootOfElevation:
            return f"""{self.feet_of_elevation} ft of elevation"""
        
        if unit == PressureUnits.Micropascal:
            return f"""{self.micropascals} """
        
        if unit == PressureUnits.Millipascal:
            return f"""{self.millipascals} """
        
        if unit == PressureUnits.Decapascal:
            return f"""{self.decapascals} """
        
        if unit == PressureUnits.Hectopascal:
            return f"""{self.hectopascals} """
        
        if unit == PressureUnits.Kilopascal:
            return f"""{self.kilopascals} """
        
        if unit == PressureUnits.Megapascal:
            return f"""{self.megapascals} """
        
        if unit == PressureUnits.Gigapascal:
            return f"""{self.gigapascals} """
        
        if unit == PressureUnits.Microbar:
            return f"""{self.microbars} """
        
        if unit == PressureUnits.Millibar:
            return f"""{self.millibars} """
        
        if unit == PressureUnits.Centibar:
            return f"""{self.centibars} """
        
        if unit == PressureUnits.Decibar:
            return f"""{self.decibars} """
        
        if unit == PressureUnits.Kilobar:
            return f"""{self.kilobars} """
        
        if unit == PressureUnits.Megabar:
            return f"""{self.megabars} """
        
        if unit == PressureUnits.KilonewtonPerSquareMeter:
            return f"""{self.kilonewtons_per_square_meter} """
        
        if unit == PressureUnits.MeganewtonPerSquareMeter:
            return f"""{self.meganewtons_per_square_meter} """
        
        if unit == PressureUnits.KilonewtonPerSquareCentimeter:
            return f"""{self.kilonewtons_per_square_centimeter} """
        
        if unit == PressureUnits.KilonewtonPerSquareMillimeter:
            return f"""{self.kilonewtons_per_square_millimeter} """
        
        if unit == PressureUnits.KilopoundForcePerSquareInch:
            return f"""{self.kilopounds_force_per_square_inch} """
        
        if unit == PressureUnits.KilopoundForcePerSquareMil:
            return f"""{self.kilopounds_force_per_square_mil} """
        
        if unit == PressureUnits.KilopoundForcePerSquareFoot:
            return f"""{self.kilopounds_force_per_square_foot} """
        
        if unit == PressureUnits.MillimeterOfWaterColumn:
            return f"""{self.millimeters_of_water_column} """
        
        if unit == PressureUnits.CentimeterOfWaterColumn:
            return f"""{self.centimeters_of_water_column} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: PressureUnits = PressureUnits.Pascal) -> string:
        """
        Get Pressure unit abbreviation.
        Note! the default abbreviation for Pressure is Pascal.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == PressureUnits.Pascal:
            return """Pa"""
        
        if unit_abbreviation == PressureUnits.Atmosphere:
            return """atm"""
        
        if unit_abbreviation == PressureUnits.Bar:
            return """bar"""
        
        if unit_abbreviation == PressureUnits.KilogramForcePerSquareMeter:
            return """kgf/m²"""
        
        if unit_abbreviation == PressureUnits.KilogramForcePerSquareCentimeter:
            return """kgf/cm²"""
        
        if unit_abbreviation == PressureUnits.KilogramForcePerSquareMillimeter:
            return """kgf/mm²"""
        
        if unit_abbreviation == PressureUnits.NewtonPerSquareMeter:
            return """N/m²"""
        
        if unit_abbreviation == PressureUnits.NewtonPerSquareCentimeter:
            return """N/cm²"""
        
        if unit_abbreviation == PressureUnits.NewtonPerSquareMillimeter:
            return """N/mm²"""
        
        if unit_abbreviation == PressureUnits.TechnicalAtmosphere:
            return """at"""
        
        if unit_abbreviation == PressureUnits.Torr:
            return """torr"""
        
        if unit_abbreviation == PressureUnits.PoundForcePerSquareInch:
            return """psi"""
        
        if unit_abbreviation == PressureUnits.PoundForcePerSquareMil:
            return """lb/mil²"""
        
        if unit_abbreviation == PressureUnits.PoundForcePerSquareFoot:
            return """lb/ft²"""
        
        if unit_abbreviation == PressureUnits.TonneForcePerSquareMillimeter:
            return """tf/mm²"""
        
        if unit_abbreviation == PressureUnits.TonneForcePerSquareMeter:
            return """tf/m²"""
        
        if unit_abbreviation == PressureUnits.MeterOfHead:
            return """m of head"""
        
        if unit_abbreviation == PressureUnits.TonneForcePerSquareCentimeter:
            return """tf/cm²"""
        
        if unit_abbreviation == PressureUnits.FootOfHead:
            return """ft of head"""
        
        if unit_abbreviation == PressureUnits.MillimeterOfMercury:
            return """mmHg"""
        
        if unit_abbreviation == PressureUnits.InchOfMercury:
            return """inHg"""
        
        if unit_abbreviation == PressureUnits.DynePerSquareCentimeter:
            return """dyn/cm²"""
        
        if unit_abbreviation == PressureUnits.PoundPerInchSecondSquared:
            return """lbm/(in·s²)"""
        
        if unit_abbreviation == PressureUnits.MeterOfWaterColumn:
            return """mH₂O"""
        
        if unit_abbreviation == PressureUnits.InchOfWaterColumn:
            return """inH2O"""
        
        if unit_abbreviation == PressureUnits.MeterOfElevation:
            return """m of elevation"""
        
        if unit_abbreviation == PressureUnits.FootOfElevation:
            return """ft of elevation"""
        
        if unit_abbreviation == PressureUnits.Micropascal:
            return """"""
        
        if unit_abbreviation == PressureUnits.Millipascal:
            return """"""
        
        if unit_abbreviation == PressureUnits.Decapascal:
            return """"""
        
        if unit_abbreviation == PressureUnits.Hectopascal:
            return """"""
        
        if unit_abbreviation == PressureUnits.Kilopascal:
            return """"""
        
        if unit_abbreviation == PressureUnits.Megapascal:
            return """"""
        
        if unit_abbreviation == PressureUnits.Gigapascal:
            return """"""
        
        if unit_abbreviation == PressureUnits.Microbar:
            return """"""
        
        if unit_abbreviation == PressureUnits.Millibar:
            return """"""
        
        if unit_abbreviation == PressureUnits.Centibar:
            return """"""
        
        if unit_abbreviation == PressureUnits.Decibar:
            return """"""
        
        if unit_abbreviation == PressureUnits.Kilobar:
            return """"""
        
        if unit_abbreviation == PressureUnits.Megabar:
            return """"""
        
        if unit_abbreviation == PressureUnits.KilonewtonPerSquareMeter:
            return """"""
        
        if unit_abbreviation == PressureUnits.MeganewtonPerSquareMeter:
            return """"""
        
        if unit_abbreviation == PressureUnits.KilonewtonPerSquareCentimeter:
            return """"""
        
        if unit_abbreviation == PressureUnits.KilonewtonPerSquareMillimeter:
            return """"""
        
        if unit_abbreviation == PressureUnits.KilopoundForcePerSquareInch:
            return """"""
        
        if unit_abbreviation == PressureUnits.KilopoundForcePerSquareMil:
            return """"""
        
        if unit_abbreviation == PressureUnits.KilopoundForcePerSquareFoot:
            return """"""
        
        if unit_abbreviation == PressureUnits.MillimeterOfWaterColumn:
            return """"""
        
        if unit_abbreviation == PressureUnits.CentimeterOfWaterColumn:
            return """"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, Pressure):
            raise TypeError("unsupported operand type(s) for +: 'Pressure' and '{}'".format(type(other).__name__))
        return Pressure(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, Pressure):
            raise TypeError("unsupported operand type(s) for *: 'Pressure' and '{}'".format(type(other).__name__))
        return Pressure(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, Pressure):
            raise TypeError("unsupported operand type(s) for -: 'Pressure' and '{}'".format(type(other).__name__))
        return Pressure(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, Pressure):
            raise TypeError("unsupported operand type(s) for /: 'Pressure' and '{}'".format(type(other).__name__))
        return Pressure(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, Pressure):
            raise TypeError("unsupported operand type(s) for %: 'Pressure' and '{}'".format(type(other).__name__))
        return Pressure(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, Pressure):
            raise TypeError("unsupported operand type(s) for **: 'Pressure' and '{}'".format(type(other).__name__))
        return Pressure(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, Pressure):
            raise TypeError("unsupported operand type(s) for ==: 'Pressure' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, Pressure):
            raise TypeError("unsupported operand type(s) for <: 'Pressure' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, Pressure):
            raise TypeError("unsupported operand type(s) for >: 'Pressure' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, Pressure):
            raise TypeError("unsupported operand type(s) for <=: 'Pressure' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, Pressure):
            raise TypeError("unsupported operand type(s) for >=: 'Pressure' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value
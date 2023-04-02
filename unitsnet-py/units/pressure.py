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
        
        MicroPascal = 'micro_pascal'
        """
            
        """
        
        MilliPascal = 'milli_pascal'
        """
            
        """
        
        DecaPascal = 'deca_pascal'
        """
            
        """
        
        HectoPascal = 'hecto_pascal'
        """
            
        """
        
        KiloPascal = 'kilo_pascal'
        """
            
        """
        
        MegaPascal = 'mega_pascal'
        """
            
        """
        
        GigaPascal = 'giga_pascal'
        """
            
        """
        
        MicroBar = 'micro_bar'
        """
            
        """
        
        MilliBar = 'milli_bar'
        """
            
        """
        
        CentiBar = 'centi_bar'
        """
            
        """
        
        DeciBar = 'deci_bar'
        """
            
        """
        
        KiloBar = 'kilo_bar'
        """
            
        """
        
        MegaBar = 'mega_bar'
        """
            
        """
        
        KiloNewtonPerSquareMeter = 'kilo_newton_per_square_meter'
        """
            
        """
        
        MegaNewtonPerSquareMeter = 'mega_newton_per_square_meter'
        """
            
        """
        
        KiloNewtonPerSquareCentimeter = 'kilo_newton_per_square_centimeter'
        """
            
        """
        
        KiloNewtonPerSquareMillimeter = 'kilo_newton_per_square_millimeter'
        """
            
        """
        
        KiloPoundForcePerSquareInch = 'kilo_pound_force_per_square_inch'
        """
            
        """
        
        KiloPoundForcePerSquareMil = 'kilo_pound_force_per_square_mil'
        """
            
        """
        
        KiloPoundForcePerSquareFoot = 'kilo_pound_force_per_square_foot'
        """
            
        """
        
        MilliMeterOfWaterColumn = 'milli_meter_of_water_column'
        """
            
        """
        
        CentiMeterOfWaterColumn = 'centi_meter_of_water_column'
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
        
        self.__micro_pascals = None
        
        self.__milli_pascals = None
        
        self.__deca_pascals = None
        
        self.__hecto_pascals = None
        
        self.__kilo_pascals = None
        
        self.__mega_pascals = None
        
        self.__giga_pascals = None
        
        self.__micro_bars = None
        
        self.__milli_bars = None
        
        self.__centi_bars = None
        
        self.__deci_bars = None
        
        self.__kilo_bars = None
        
        self.__mega_bars = None
        
        self.__kilo_newtons_per_square_meter = None
        
        self.__mega_newtons_per_square_meter = None
        
        self.__kilo_newtons_per_square_centimeter = None
        
        self.__kilo_newtons_per_square_millimeter = None
        
        self.__kilo_pounds_force_per_square_inch = None
        
        self.__kilo_pounds_force_per_square_mil = None
        
        self.__kilo_pounds_force_per_square_foot = None
        
        self.__milli_meters_of_water_column = None
        
        self.__centi_meters_of_water_column = None
        

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
        
        if from_unit == PressureUnits.MicroPascal:
            return ((value) / 1e-06)
        
        if from_unit == PressureUnits.MilliPascal:
            return ((value) / 0.001)
        
        if from_unit == PressureUnits.DecaPascal:
            return ((value) / 10.0)
        
        if from_unit == PressureUnits.HectoPascal:
            return ((value) / 100.0)
        
        if from_unit == PressureUnits.KiloPascal:
            return ((value) / 1000.0)
        
        if from_unit == PressureUnits.MegaPascal:
            return ((value) / 1000000.0)
        
        if from_unit == PressureUnits.GigaPascal:
            return ((value) / 1000000000.0)
        
        if from_unit == PressureUnits.MicroBar:
            return ((value / 1e5) / 1e-06)
        
        if from_unit == PressureUnits.MilliBar:
            return ((value / 1e5) / 0.001)
        
        if from_unit == PressureUnits.CentiBar:
            return ((value / 1e5) / 0.01)
        
        if from_unit == PressureUnits.DeciBar:
            return ((value / 1e5) / 0.1)
        
        if from_unit == PressureUnits.KiloBar:
            return ((value / 1e5) / 1000.0)
        
        if from_unit == PressureUnits.MegaBar:
            return ((value / 1e5) / 1000000.0)
        
        if from_unit == PressureUnits.KiloNewtonPerSquareMeter:
            return ((value) / 1000.0)
        
        if from_unit == PressureUnits.MegaNewtonPerSquareMeter:
            return ((value) / 1000000.0)
        
        if from_unit == PressureUnits.KiloNewtonPerSquareCentimeter:
            return ((value / 1e4) / 1000.0)
        
        if from_unit == PressureUnits.KiloNewtonPerSquareMillimeter:
            return ((value / 1e6) / 1000.0)
        
        if from_unit == PressureUnits.KiloPoundForcePerSquareInch:
            return ((value / 6.894757293168361e3) / 1000.0)
        
        if from_unit == PressureUnits.KiloPoundForcePerSquareMil:
            return ((value / 6.894757293168361e9) / 1000.0)
        
        if from_unit == PressureUnits.KiloPoundForcePerSquareFoot:
            return ((value / 4.788025898033584e1) / 1000.0)
        
        if from_unit == PressureUnits.MilliMeterOfWaterColumn:
            return ((value / 9.806650000000272e3) / 0.001)
        
        if from_unit == PressureUnits.CentiMeterOfWaterColumn:
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
        
        if to_unit == PressureUnits.MicroPascal:
            return ((value) * 1e-06)
        
        if to_unit == PressureUnits.MilliPascal:
            return ((value) * 0.001)
        
        if to_unit == PressureUnits.DecaPascal:
            return ((value) * 10.0)
        
        if to_unit == PressureUnits.HectoPascal:
            return ((value) * 100.0)
        
        if to_unit == PressureUnits.KiloPascal:
            return ((value) * 1000.0)
        
        if to_unit == PressureUnits.MegaPascal:
            return ((value) * 1000000.0)
        
        if to_unit == PressureUnits.GigaPascal:
            return ((value) * 1000000000.0)
        
        if to_unit == PressureUnits.MicroBar:
            return ((value * 1e5) * 1e-06)
        
        if to_unit == PressureUnits.MilliBar:
            return ((value * 1e5) * 0.001)
        
        if to_unit == PressureUnits.CentiBar:
            return ((value * 1e5) * 0.01)
        
        if to_unit == PressureUnits.DeciBar:
            return ((value * 1e5) * 0.1)
        
        if to_unit == PressureUnits.KiloBar:
            return ((value * 1e5) * 1000.0)
        
        if to_unit == PressureUnits.MegaBar:
            return ((value * 1e5) * 1000000.0)
        
        if to_unit == PressureUnits.KiloNewtonPerSquareMeter:
            return ((value) * 1000.0)
        
        if to_unit == PressureUnits.MegaNewtonPerSquareMeter:
            return ((value) * 1000000.0)
        
        if to_unit == PressureUnits.KiloNewtonPerSquareCentimeter:
            return ((value * 1e4) * 1000.0)
        
        if to_unit == PressureUnits.KiloNewtonPerSquareMillimeter:
            return ((value * 1e6) * 1000.0)
        
        if to_unit == PressureUnits.KiloPoundForcePerSquareInch:
            return ((value * 6.894757293168361e3) * 1000.0)
        
        if to_unit == PressureUnits.KiloPoundForcePerSquareMil:
            return ((value * 6.894757293168361e9) * 1000.0)
        
        if to_unit == PressureUnits.KiloPoundForcePerSquareFoot:
            return ((value * 4.788025898033584e1) * 1000.0)
        
        if to_unit == PressureUnits.MilliMeterOfWaterColumn:
            return ((value * 9.806650000000272e3) * 0.001)
        
        if to_unit == PressureUnits.CentiMeterOfWaterColumn:
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
    def from_micro_pascals(micro_pascals: float):
        """
        Create a new instance of Pressure from a value in micro_pascals.

        

        :param meters: The Pressure value in micro_pascals.
        :type micro_pascals: float
        :return: A new instance of Pressure.
        :rtype: Pressure
        """
        return Pressure(micro_pascals, PressureUnits.MicroPascal)

    
    @staticmethod
    def from_milli_pascals(milli_pascals: float):
        """
        Create a new instance of Pressure from a value in milli_pascals.

        

        :param meters: The Pressure value in milli_pascals.
        :type milli_pascals: float
        :return: A new instance of Pressure.
        :rtype: Pressure
        """
        return Pressure(milli_pascals, PressureUnits.MilliPascal)

    
    @staticmethod
    def from_deca_pascals(deca_pascals: float):
        """
        Create a new instance of Pressure from a value in deca_pascals.

        

        :param meters: The Pressure value in deca_pascals.
        :type deca_pascals: float
        :return: A new instance of Pressure.
        :rtype: Pressure
        """
        return Pressure(deca_pascals, PressureUnits.DecaPascal)

    
    @staticmethod
    def from_hecto_pascals(hecto_pascals: float):
        """
        Create a new instance of Pressure from a value in hecto_pascals.

        

        :param meters: The Pressure value in hecto_pascals.
        :type hecto_pascals: float
        :return: A new instance of Pressure.
        :rtype: Pressure
        """
        return Pressure(hecto_pascals, PressureUnits.HectoPascal)

    
    @staticmethod
    def from_kilo_pascals(kilo_pascals: float):
        """
        Create a new instance of Pressure from a value in kilo_pascals.

        

        :param meters: The Pressure value in kilo_pascals.
        :type kilo_pascals: float
        :return: A new instance of Pressure.
        :rtype: Pressure
        """
        return Pressure(kilo_pascals, PressureUnits.KiloPascal)

    
    @staticmethod
    def from_mega_pascals(mega_pascals: float):
        """
        Create a new instance of Pressure from a value in mega_pascals.

        

        :param meters: The Pressure value in mega_pascals.
        :type mega_pascals: float
        :return: A new instance of Pressure.
        :rtype: Pressure
        """
        return Pressure(mega_pascals, PressureUnits.MegaPascal)

    
    @staticmethod
    def from_giga_pascals(giga_pascals: float):
        """
        Create a new instance of Pressure from a value in giga_pascals.

        

        :param meters: The Pressure value in giga_pascals.
        :type giga_pascals: float
        :return: A new instance of Pressure.
        :rtype: Pressure
        """
        return Pressure(giga_pascals, PressureUnits.GigaPascal)

    
    @staticmethod
    def from_micro_bars(micro_bars: float):
        """
        Create a new instance of Pressure from a value in micro_bars.

        

        :param meters: The Pressure value in micro_bars.
        :type micro_bars: float
        :return: A new instance of Pressure.
        :rtype: Pressure
        """
        return Pressure(micro_bars, PressureUnits.MicroBar)

    
    @staticmethod
    def from_milli_bars(milli_bars: float):
        """
        Create a new instance of Pressure from a value in milli_bars.

        

        :param meters: The Pressure value in milli_bars.
        :type milli_bars: float
        :return: A new instance of Pressure.
        :rtype: Pressure
        """
        return Pressure(milli_bars, PressureUnits.MilliBar)

    
    @staticmethod
    def from_centi_bars(centi_bars: float):
        """
        Create a new instance of Pressure from a value in centi_bars.

        

        :param meters: The Pressure value in centi_bars.
        :type centi_bars: float
        :return: A new instance of Pressure.
        :rtype: Pressure
        """
        return Pressure(centi_bars, PressureUnits.CentiBar)

    
    @staticmethod
    def from_deci_bars(deci_bars: float):
        """
        Create a new instance of Pressure from a value in deci_bars.

        

        :param meters: The Pressure value in deci_bars.
        :type deci_bars: float
        :return: A new instance of Pressure.
        :rtype: Pressure
        """
        return Pressure(deci_bars, PressureUnits.DeciBar)

    
    @staticmethod
    def from_kilo_bars(kilo_bars: float):
        """
        Create a new instance of Pressure from a value in kilo_bars.

        

        :param meters: The Pressure value in kilo_bars.
        :type kilo_bars: float
        :return: A new instance of Pressure.
        :rtype: Pressure
        """
        return Pressure(kilo_bars, PressureUnits.KiloBar)

    
    @staticmethod
    def from_mega_bars(mega_bars: float):
        """
        Create a new instance of Pressure from a value in mega_bars.

        

        :param meters: The Pressure value in mega_bars.
        :type mega_bars: float
        :return: A new instance of Pressure.
        :rtype: Pressure
        """
        return Pressure(mega_bars, PressureUnits.MegaBar)

    
    @staticmethod
    def from_kilo_newtons_per_square_meter(kilo_newtons_per_square_meter: float):
        """
        Create a new instance of Pressure from a value in kilo_newtons_per_square_meter.

        

        :param meters: The Pressure value in kilo_newtons_per_square_meter.
        :type kilo_newtons_per_square_meter: float
        :return: A new instance of Pressure.
        :rtype: Pressure
        """
        return Pressure(kilo_newtons_per_square_meter, PressureUnits.KiloNewtonPerSquareMeter)

    
    @staticmethod
    def from_mega_newtons_per_square_meter(mega_newtons_per_square_meter: float):
        """
        Create a new instance of Pressure from a value in mega_newtons_per_square_meter.

        

        :param meters: The Pressure value in mega_newtons_per_square_meter.
        :type mega_newtons_per_square_meter: float
        :return: A new instance of Pressure.
        :rtype: Pressure
        """
        return Pressure(mega_newtons_per_square_meter, PressureUnits.MegaNewtonPerSquareMeter)

    
    @staticmethod
    def from_kilo_newtons_per_square_centimeter(kilo_newtons_per_square_centimeter: float):
        """
        Create a new instance of Pressure from a value in kilo_newtons_per_square_centimeter.

        

        :param meters: The Pressure value in kilo_newtons_per_square_centimeter.
        :type kilo_newtons_per_square_centimeter: float
        :return: A new instance of Pressure.
        :rtype: Pressure
        """
        return Pressure(kilo_newtons_per_square_centimeter, PressureUnits.KiloNewtonPerSquareCentimeter)

    
    @staticmethod
    def from_kilo_newtons_per_square_millimeter(kilo_newtons_per_square_millimeter: float):
        """
        Create a new instance of Pressure from a value in kilo_newtons_per_square_millimeter.

        

        :param meters: The Pressure value in kilo_newtons_per_square_millimeter.
        :type kilo_newtons_per_square_millimeter: float
        :return: A new instance of Pressure.
        :rtype: Pressure
        """
        return Pressure(kilo_newtons_per_square_millimeter, PressureUnits.KiloNewtonPerSquareMillimeter)

    
    @staticmethod
    def from_kilo_pounds_force_per_square_inch(kilo_pounds_force_per_square_inch: float):
        """
        Create a new instance of Pressure from a value in kilo_pounds_force_per_square_inch.

        

        :param meters: The Pressure value in kilo_pounds_force_per_square_inch.
        :type kilo_pounds_force_per_square_inch: float
        :return: A new instance of Pressure.
        :rtype: Pressure
        """
        return Pressure(kilo_pounds_force_per_square_inch, PressureUnits.KiloPoundForcePerSquareInch)

    
    @staticmethod
    def from_kilo_pounds_force_per_square_mil(kilo_pounds_force_per_square_mil: float):
        """
        Create a new instance of Pressure from a value in kilo_pounds_force_per_square_mil.

        

        :param meters: The Pressure value in kilo_pounds_force_per_square_mil.
        :type kilo_pounds_force_per_square_mil: float
        :return: A new instance of Pressure.
        :rtype: Pressure
        """
        return Pressure(kilo_pounds_force_per_square_mil, PressureUnits.KiloPoundForcePerSquareMil)

    
    @staticmethod
    def from_kilo_pounds_force_per_square_foot(kilo_pounds_force_per_square_foot: float):
        """
        Create a new instance of Pressure from a value in kilo_pounds_force_per_square_foot.

        

        :param meters: The Pressure value in kilo_pounds_force_per_square_foot.
        :type kilo_pounds_force_per_square_foot: float
        :return: A new instance of Pressure.
        :rtype: Pressure
        """
        return Pressure(kilo_pounds_force_per_square_foot, PressureUnits.KiloPoundForcePerSquareFoot)

    
    @staticmethod
    def from_milli_meters_of_water_column(milli_meters_of_water_column: float):
        """
        Create a new instance of Pressure from a value in milli_meters_of_water_column.

        

        :param meters: The Pressure value in milli_meters_of_water_column.
        :type milli_meters_of_water_column: float
        :return: A new instance of Pressure.
        :rtype: Pressure
        """
        return Pressure(milli_meters_of_water_column, PressureUnits.MilliMeterOfWaterColumn)

    
    @staticmethod
    def from_centi_meters_of_water_column(centi_meters_of_water_column: float):
        """
        Create a new instance of Pressure from a value in centi_meters_of_water_column.

        

        :param meters: The Pressure value in centi_meters_of_water_column.
        :type centi_meters_of_water_column: float
        :return: A new instance of Pressure.
        :rtype: Pressure
        """
        return Pressure(centi_meters_of_water_column, PressureUnits.CentiMeterOfWaterColumn)

    
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
    def micro_pascals(self) -> float:
        """
        
        """
        if self.__micro_pascals != None:
            return self.__micro_pascals
        self.__micro_pascals = self.__convert_from_base(PressureUnits.MicroPascal)
        return self.__micro_pascals

    
    @property
    def milli_pascals(self) -> float:
        """
        
        """
        if self.__milli_pascals != None:
            return self.__milli_pascals
        self.__milli_pascals = self.__convert_from_base(PressureUnits.MilliPascal)
        return self.__milli_pascals

    
    @property
    def deca_pascals(self) -> float:
        """
        
        """
        if self.__deca_pascals != None:
            return self.__deca_pascals
        self.__deca_pascals = self.__convert_from_base(PressureUnits.DecaPascal)
        return self.__deca_pascals

    
    @property
    def hecto_pascals(self) -> float:
        """
        
        """
        if self.__hecto_pascals != None:
            return self.__hecto_pascals
        self.__hecto_pascals = self.__convert_from_base(PressureUnits.HectoPascal)
        return self.__hecto_pascals

    
    @property
    def kilo_pascals(self) -> float:
        """
        
        """
        if self.__kilo_pascals != None:
            return self.__kilo_pascals
        self.__kilo_pascals = self.__convert_from_base(PressureUnits.KiloPascal)
        return self.__kilo_pascals

    
    @property
    def mega_pascals(self) -> float:
        """
        
        """
        if self.__mega_pascals != None:
            return self.__mega_pascals
        self.__mega_pascals = self.__convert_from_base(PressureUnits.MegaPascal)
        return self.__mega_pascals

    
    @property
    def giga_pascals(self) -> float:
        """
        
        """
        if self.__giga_pascals != None:
            return self.__giga_pascals
        self.__giga_pascals = self.__convert_from_base(PressureUnits.GigaPascal)
        return self.__giga_pascals

    
    @property
    def micro_bars(self) -> float:
        """
        
        """
        if self.__micro_bars != None:
            return self.__micro_bars
        self.__micro_bars = self.__convert_from_base(PressureUnits.MicroBar)
        return self.__micro_bars

    
    @property
    def milli_bars(self) -> float:
        """
        
        """
        if self.__milli_bars != None:
            return self.__milli_bars
        self.__milli_bars = self.__convert_from_base(PressureUnits.MilliBar)
        return self.__milli_bars

    
    @property
    def centi_bars(self) -> float:
        """
        
        """
        if self.__centi_bars != None:
            return self.__centi_bars
        self.__centi_bars = self.__convert_from_base(PressureUnits.CentiBar)
        return self.__centi_bars

    
    @property
    def deci_bars(self) -> float:
        """
        
        """
        if self.__deci_bars != None:
            return self.__deci_bars
        self.__deci_bars = self.__convert_from_base(PressureUnits.DeciBar)
        return self.__deci_bars

    
    @property
    def kilo_bars(self) -> float:
        """
        
        """
        if self.__kilo_bars != None:
            return self.__kilo_bars
        self.__kilo_bars = self.__convert_from_base(PressureUnits.KiloBar)
        return self.__kilo_bars

    
    @property
    def mega_bars(self) -> float:
        """
        
        """
        if self.__mega_bars != None:
            return self.__mega_bars
        self.__mega_bars = self.__convert_from_base(PressureUnits.MegaBar)
        return self.__mega_bars

    
    @property
    def kilo_newtons_per_square_meter(self) -> float:
        """
        
        """
        if self.__kilo_newtons_per_square_meter != None:
            return self.__kilo_newtons_per_square_meter
        self.__kilo_newtons_per_square_meter = self.__convert_from_base(PressureUnits.KiloNewtonPerSquareMeter)
        return self.__kilo_newtons_per_square_meter

    
    @property
    def mega_newtons_per_square_meter(self) -> float:
        """
        
        """
        if self.__mega_newtons_per_square_meter != None:
            return self.__mega_newtons_per_square_meter
        self.__mega_newtons_per_square_meter = self.__convert_from_base(PressureUnits.MegaNewtonPerSquareMeter)
        return self.__mega_newtons_per_square_meter

    
    @property
    def kilo_newtons_per_square_centimeter(self) -> float:
        """
        
        """
        if self.__kilo_newtons_per_square_centimeter != None:
            return self.__kilo_newtons_per_square_centimeter
        self.__kilo_newtons_per_square_centimeter = self.__convert_from_base(PressureUnits.KiloNewtonPerSquareCentimeter)
        return self.__kilo_newtons_per_square_centimeter

    
    @property
    def kilo_newtons_per_square_millimeter(self) -> float:
        """
        
        """
        if self.__kilo_newtons_per_square_millimeter != None:
            return self.__kilo_newtons_per_square_millimeter
        self.__kilo_newtons_per_square_millimeter = self.__convert_from_base(PressureUnits.KiloNewtonPerSquareMillimeter)
        return self.__kilo_newtons_per_square_millimeter

    
    @property
    def kilo_pounds_force_per_square_inch(self) -> float:
        """
        
        """
        if self.__kilo_pounds_force_per_square_inch != None:
            return self.__kilo_pounds_force_per_square_inch
        self.__kilo_pounds_force_per_square_inch = self.__convert_from_base(PressureUnits.KiloPoundForcePerSquareInch)
        return self.__kilo_pounds_force_per_square_inch

    
    @property
    def kilo_pounds_force_per_square_mil(self) -> float:
        """
        
        """
        if self.__kilo_pounds_force_per_square_mil != None:
            return self.__kilo_pounds_force_per_square_mil
        self.__kilo_pounds_force_per_square_mil = self.__convert_from_base(PressureUnits.KiloPoundForcePerSquareMil)
        return self.__kilo_pounds_force_per_square_mil

    
    @property
    def kilo_pounds_force_per_square_foot(self) -> float:
        """
        
        """
        if self.__kilo_pounds_force_per_square_foot != None:
            return self.__kilo_pounds_force_per_square_foot
        self.__kilo_pounds_force_per_square_foot = self.__convert_from_base(PressureUnits.KiloPoundForcePerSquareFoot)
        return self.__kilo_pounds_force_per_square_foot

    
    @property
    def milli_meters_of_water_column(self) -> float:
        """
        
        """
        if self.__milli_meters_of_water_column != None:
            return self.__milli_meters_of_water_column
        self.__milli_meters_of_water_column = self.__convert_from_base(PressureUnits.MilliMeterOfWaterColumn)
        return self.__milli_meters_of_water_column

    
    @property
    def centi_meters_of_water_column(self) -> float:
        """
        
        """
        if self.__centi_meters_of_water_column != None:
            return self.__centi_meters_of_water_column
        self.__centi_meters_of_water_column = self.__convert_from_base(PressureUnits.CentiMeterOfWaterColumn)
        return self.__centi_meters_of_water_column

    
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
        
        if unit == PressureUnits.MicroPascal:
            return f"""{self.micro_pascals} """
        
        if unit == PressureUnits.MilliPascal:
            return f"""{self.milli_pascals} """
        
        if unit == PressureUnits.DecaPascal:
            return f"""{self.deca_pascals} """
        
        if unit == PressureUnits.HectoPascal:
            return f"""{self.hecto_pascals} """
        
        if unit == PressureUnits.KiloPascal:
            return f"""{self.kilo_pascals} """
        
        if unit == PressureUnits.MegaPascal:
            return f"""{self.mega_pascals} """
        
        if unit == PressureUnits.GigaPascal:
            return f"""{self.giga_pascals} """
        
        if unit == PressureUnits.MicroBar:
            return f"""{self.micro_bars} """
        
        if unit == PressureUnits.MilliBar:
            return f"""{self.milli_bars} """
        
        if unit == PressureUnits.CentiBar:
            return f"""{self.centi_bars} """
        
        if unit == PressureUnits.DeciBar:
            return f"""{self.deci_bars} """
        
        if unit == PressureUnits.KiloBar:
            return f"""{self.kilo_bars} """
        
        if unit == PressureUnits.MegaBar:
            return f"""{self.mega_bars} """
        
        if unit == PressureUnits.KiloNewtonPerSquareMeter:
            return f"""{self.kilo_newtons_per_square_meter} """
        
        if unit == PressureUnits.MegaNewtonPerSquareMeter:
            return f"""{self.mega_newtons_per_square_meter} """
        
        if unit == PressureUnits.KiloNewtonPerSquareCentimeter:
            return f"""{self.kilo_newtons_per_square_centimeter} """
        
        if unit == PressureUnits.KiloNewtonPerSquareMillimeter:
            return f"""{self.kilo_newtons_per_square_millimeter} """
        
        if unit == PressureUnits.KiloPoundForcePerSquareInch:
            return f"""{self.kilo_pounds_force_per_square_inch} """
        
        if unit == PressureUnits.KiloPoundForcePerSquareMil:
            return f"""{self.kilo_pounds_force_per_square_mil} """
        
        if unit == PressureUnits.KiloPoundForcePerSquareFoot:
            return f"""{self.kilo_pounds_force_per_square_foot} """
        
        if unit == PressureUnits.MilliMeterOfWaterColumn:
            return f"""{self.milli_meters_of_water_column} """
        
        if unit == PressureUnits.CentiMeterOfWaterColumn:
            return f"""{self.centi_meters_of_water_column} """
        
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
        
        if unit_abbreviation == PressureUnits.MicroPascal:
            return """"""
        
        if unit_abbreviation == PressureUnits.MilliPascal:
            return """"""
        
        if unit_abbreviation == PressureUnits.DecaPascal:
            return """"""
        
        if unit_abbreviation == PressureUnits.HectoPascal:
            return """"""
        
        if unit_abbreviation == PressureUnits.KiloPascal:
            return """"""
        
        if unit_abbreviation == PressureUnits.MegaPascal:
            return """"""
        
        if unit_abbreviation == PressureUnits.GigaPascal:
            return """"""
        
        if unit_abbreviation == PressureUnits.MicroBar:
            return """"""
        
        if unit_abbreviation == PressureUnits.MilliBar:
            return """"""
        
        if unit_abbreviation == PressureUnits.CentiBar:
            return """"""
        
        if unit_abbreviation == PressureUnits.DeciBar:
            return """"""
        
        if unit_abbreviation == PressureUnits.KiloBar:
            return """"""
        
        if unit_abbreviation == PressureUnits.MegaBar:
            return """"""
        
        if unit_abbreviation == PressureUnits.KiloNewtonPerSquareMeter:
            return """"""
        
        if unit_abbreviation == PressureUnits.MegaNewtonPerSquareMeter:
            return """"""
        
        if unit_abbreviation == PressureUnits.KiloNewtonPerSquareCentimeter:
            return """"""
        
        if unit_abbreviation == PressureUnits.KiloNewtonPerSquareMillimeter:
            return """"""
        
        if unit_abbreviation == PressureUnits.KiloPoundForcePerSquareInch:
            return """"""
        
        if unit_abbreviation == PressureUnits.KiloPoundForcePerSquareMil:
            return """"""
        
        if unit_abbreviation == PressureUnits.KiloPoundForcePerSquareFoot:
            return """"""
        
        if unit_abbreviation == PressureUnits.MilliMeterOfWaterColumn:
            return """"""
        
        if unit_abbreviation == PressureUnits.CentiMeterOfWaterColumn:
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
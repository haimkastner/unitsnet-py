from enum import Enum
import math
import string


class EnergyUnits(Enum):
        """
            EnergyUnits enumeration
        """
        
        Joule = 'joule'
        """
            
        """
        
        Calorie = 'calorie'
        """
            
        """
        
        BritishThermalUnit = 'british_thermal_unit'
        """
            
        """
        
        ElectronVolt = 'electron_volt'
        """
            
        """
        
        FootPound = 'foot_pound'
        """
            
        """
        
        Erg = 'erg'
        """
            
        """
        
        WattHour = 'watt_hour'
        """
            
        """
        
        WattDay = 'watt_day'
        """
            
        """
        
        ThermEc = 'therm_ec'
        """
            
        """
        
        ThermUs = 'therm_us'
        """
            
        """
        
        ThermImperial = 'therm_imperial'
        """
            
        """
        
        HorsepowerHour = 'horsepower_hour'
        """
            
        """
        
        MilliJoule = 'milli_joule'
        """
            
        """
        
        KiloJoule = 'kilo_joule'
        """
            
        """
        
        MegaJoule = 'mega_joule'
        """
            
        """
        
        GigaJoule = 'giga_joule'
        """
            
        """
        
        TeraJoule = 'tera_joule'
        """
            
        """
        
        PetaJoule = 'peta_joule'
        """
            
        """
        
        KiloCalorie = 'kilo_calorie'
        """
            
        """
        
        MegaCalorie = 'mega_calorie'
        """
            
        """
        
        KiloBritishThermalUnit = 'kilo_british_thermal_unit'
        """
            
        """
        
        MegaBritishThermalUnit = 'mega_british_thermal_unit'
        """
            
        """
        
        GigaBritishThermalUnit = 'giga_british_thermal_unit'
        """
            
        """
        
        KiloElectronVolt = 'kilo_electron_volt'
        """
            
        """
        
        MegaElectronVolt = 'mega_electron_volt'
        """
            
        """
        
        GigaElectronVolt = 'giga_electron_volt'
        """
            
        """
        
        TeraElectronVolt = 'tera_electron_volt'
        """
            
        """
        
        KiloWattHour = 'kilo_watt_hour'
        """
            
        """
        
        MegaWattHour = 'mega_watt_hour'
        """
            
        """
        
        GigaWattHour = 'giga_watt_hour'
        """
            
        """
        
        TeraWattHour = 'tera_watt_hour'
        """
            
        """
        
        KiloWattDay = 'kilo_watt_day'
        """
            
        """
        
        MegaWattDay = 'mega_watt_day'
        """
            
        """
        
        GigaWattDay = 'giga_watt_day'
        """
            
        """
        
        TeraWattDay = 'tera_watt_day'
        """
            
        """
        
        DecaThermEc = 'deca_therm_ec'
        """
            
        """
        
        DecaThermUs = 'deca_therm_us'
        """
            
        """
        
        DecaThermImperial = 'deca_therm_imperial'
        """
            
        """
        

class Energy:
    """
    The joule, symbol J, is a derived unit of energy, work, or amount of heat in the International System of Units. It is equal to the energy transferred (or work done) when applying a force of one newton through a distance of one metre (1 newton metre or N·m), or in passing an electric current of one ampere through a resistance of one ohm for one second. Many other units of energy are included. Please do not confuse this definition of the calorie with the one colloquially used by the food industry, the large calorie, which is equivalent to 1 kcal. Thermochemical definition of the calorie is used. For BTU, the IT definition is used.

    Args:
        value (float): The value.
        from_unit (EnergyUnits): The Energy unit to create from, The default unit is Joule
    """
    def __init__(self, value: float, from_unit: EnergyUnits = EnergyUnits.Joule):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__joules = None
        
        self.__calories = None
        
        self.__british_thermal_units = None
        
        self.__electron_volts = None
        
        self.__foot_pounds = None
        
        self.__ergs = None
        
        self.__watt_hours = None
        
        self.__watt_days = None
        
        self.__therms_ec = None
        
        self.__therms_us = None
        
        self.__therms_imperial = None
        
        self.__horsepower_hours = None
        
        self.__milli_joules = None
        
        self.__kilo_joules = None
        
        self.__mega_joules = None
        
        self.__giga_joules = None
        
        self.__tera_joules = None
        
        self.__peta_joules = None
        
        self.__kilo_calories = None
        
        self.__mega_calories = None
        
        self.__kilo_british_thermal_units = None
        
        self.__mega_british_thermal_units = None
        
        self.__giga_british_thermal_units = None
        
        self.__kilo_electron_volts = None
        
        self.__mega_electron_volts = None
        
        self.__giga_electron_volts = None
        
        self.__tera_electron_volts = None
        
        self.__kilo_watt_hours = None
        
        self.__mega_watt_hours = None
        
        self.__giga_watt_hours = None
        
        self.__tera_watt_hours = None
        
        self.__kilo_watt_days = None
        
        self.__mega_watt_days = None
        
        self.__giga_watt_days = None
        
        self.__tera_watt_days = None
        
        self.__deca_therms_ec = None
        
        self.__deca_therms_us = None
        
        self.__deca_therms_imperial = None
        

    def __convert_from_base(self, from_unit: EnergyUnits) -> float:
        value = self.__value
        
        if from_unit == EnergyUnits.Joule:
            return (value)
        
        if from_unit == EnergyUnits.Calorie:
            return (value / 4.184)
        
        if from_unit == EnergyUnits.BritishThermalUnit:
            return (value / 1055.05585262)
        
        if from_unit == EnergyUnits.ElectronVolt:
            return (value / 1.602176565e-19)
        
        if from_unit == EnergyUnits.FootPound:
            return (value / 1.355817948)
        
        if from_unit == EnergyUnits.Erg:
            return (value / 1e-7)
        
        if from_unit == EnergyUnits.WattHour:
            return (value / 3600)
        
        if from_unit == EnergyUnits.WattDay:
            return (value / (24 * 3600))
        
        if from_unit == EnergyUnits.ThermEc:
            return (value / 1.05505585262e8)
        
        if from_unit == EnergyUnits.ThermUs:
            return (value / 1.054804e8)
        
        if from_unit == EnergyUnits.ThermImperial:
            return (value / 1.05505585257348e8)
        
        if from_unit == EnergyUnits.HorsepowerHour:
            return (value / 2.6845195377e6)
        
        if from_unit == EnergyUnits.MilliJoule:
            return ((value) / 0.001)
        
        if from_unit == EnergyUnits.KiloJoule:
            return ((value) / 1000.0)
        
        if from_unit == EnergyUnits.MegaJoule:
            return ((value) / 1000000.0)
        
        if from_unit == EnergyUnits.GigaJoule:
            return ((value) / 1000000000.0)
        
        if from_unit == EnergyUnits.TeraJoule:
            return ((value) / 1000000000000.0)
        
        if from_unit == EnergyUnits.PetaJoule:
            return ((value) / 1000000000000000.0)
        
        if from_unit == EnergyUnits.KiloCalorie:
            return ((value / 4.184) / 1000.0)
        
        if from_unit == EnergyUnits.MegaCalorie:
            return ((value / 4.184) / 1000000.0)
        
        if from_unit == EnergyUnits.KiloBritishThermalUnit:
            return ((value / 1055.05585262) / 1000.0)
        
        if from_unit == EnergyUnits.MegaBritishThermalUnit:
            return ((value / 1055.05585262) / 1000000.0)
        
        if from_unit == EnergyUnits.GigaBritishThermalUnit:
            return ((value / 1055.05585262) / 1000000000.0)
        
        if from_unit == EnergyUnits.KiloElectronVolt:
            return ((value / 1.602176565e-19) / 1000.0)
        
        if from_unit == EnergyUnits.MegaElectronVolt:
            return ((value / 1.602176565e-19) / 1000000.0)
        
        if from_unit == EnergyUnits.GigaElectronVolt:
            return ((value / 1.602176565e-19) / 1000000000.0)
        
        if from_unit == EnergyUnits.TeraElectronVolt:
            return ((value / 1.602176565e-19) / 1000000000000.0)
        
        if from_unit == EnergyUnits.KiloWattHour:
            return ((value / 3600) / 1000.0)
        
        if from_unit == EnergyUnits.MegaWattHour:
            return ((value / 3600) / 1000000.0)
        
        if from_unit == EnergyUnits.GigaWattHour:
            return ((value / 3600) / 1000000000.0)
        
        if from_unit == EnergyUnits.TeraWattHour:
            return ((value / 3600) / 1000000000000.0)
        
        if from_unit == EnergyUnits.KiloWattDay:
            return ((value / (24 * 3600)) / 1000.0)
        
        if from_unit == EnergyUnits.MegaWattDay:
            return ((value / (24 * 3600)) / 1000000.0)
        
        if from_unit == EnergyUnits.GigaWattDay:
            return ((value / (24 * 3600)) / 1000000000.0)
        
        if from_unit == EnergyUnits.TeraWattDay:
            return ((value / (24 * 3600)) / 1000000000000.0)
        
        if from_unit == EnergyUnits.DecaThermEc:
            return ((value / 1.05505585262e8) / 10.0)
        
        if from_unit == EnergyUnits.DecaThermUs:
            return ((value / 1.054804e8) / 10.0)
        
        if from_unit == EnergyUnits.DecaThermImperial:
            return ((value / 1.05505585257348e8) / 10.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: EnergyUnits) -> float:
        
        if to_unit == EnergyUnits.Joule:
            return (value)
        
        if to_unit == EnergyUnits.Calorie:
            return (value * 4.184)
        
        if to_unit == EnergyUnits.BritishThermalUnit:
            return (value * 1055.05585262)
        
        if to_unit == EnergyUnits.ElectronVolt:
            return (value * 1.602176565e-19)
        
        if to_unit == EnergyUnits.FootPound:
            return (value * 1.355817948)
        
        if to_unit == EnergyUnits.Erg:
            return (value * 1e-7)
        
        if to_unit == EnergyUnits.WattHour:
            return (value * 3600)
        
        if to_unit == EnergyUnits.WattDay:
            return (value * 24 * 3600)
        
        if to_unit == EnergyUnits.ThermEc:
            return (value * 1.05505585262e8)
        
        if to_unit == EnergyUnits.ThermUs:
            return (value * 1.054804e8)
        
        if to_unit == EnergyUnits.ThermImperial:
            return (value * 1.05505585257348e8)
        
        if to_unit == EnergyUnits.HorsepowerHour:
            return (value * 2.6845195377e6)
        
        if to_unit == EnergyUnits.MilliJoule:
            return ((value) * 0.001)
        
        if to_unit == EnergyUnits.KiloJoule:
            return ((value) * 1000.0)
        
        if to_unit == EnergyUnits.MegaJoule:
            return ((value) * 1000000.0)
        
        if to_unit == EnergyUnits.GigaJoule:
            return ((value) * 1000000000.0)
        
        if to_unit == EnergyUnits.TeraJoule:
            return ((value) * 1000000000000.0)
        
        if to_unit == EnergyUnits.PetaJoule:
            return ((value) * 1000000000000000.0)
        
        if to_unit == EnergyUnits.KiloCalorie:
            return ((value * 4.184) * 1000.0)
        
        if to_unit == EnergyUnits.MegaCalorie:
            return ((value * 4.184) * 1000000.0)
        
        if to_unit == EnergyUnits.KiloBritishThermalUnit:
            return ((value * 1055.05585262) * 1000.0)
        
        if to_unit == EnergyUnits.MegaBritishThermalUnit:
            return ((value * 1055.05585262) * 1000000.0)
        
        if to_unit == EnergyUnits.GigaBritishThermalUnit:
            return ((value * 1055.05585262) * 1000000000.0)
        
        if to_unit == EnergyUnits.KiloElectronVolt:
            return ((value * 1.602176565e-19) * 1000.0)
        
        if to_unit == EnergyUnits.MegaElectronVolt:
            return ((value * 1.602176565e-19) * 1000000.0)
        
        if to_unit == EnergyUnits.GigaElectronVolt:
            return ((value * 1.602176565e-19) * 1000000000.0)
        
        if to_unit == EnergyUnits.TeraElectronVolt:
            return ((value * 1.602176565e-19) * 1000000000000.0)
        
        if to_unit == EnergyUnits.KiloWattHour:
            return ((value * 3600) * 1000.0)
        
        if to_unit == EnergyUnits.MegaWattHour:
            return ((value * 3600) * 1000000.0)
        
        if to_unit == EnergyUnits.GigaWattHour:
            return ((value * 3600) * 1000000000.0)
        
        if to_unit == EnergyUnits.TeraWattHour:
            return ((value * 3600) * 1000000000000.0)
        
        if to_unit == EnergyUnits.KiloWattDay:
            return ((value * 24 * 3600) * 1000.0)
        
        if to_unit == EnergyUnits.MegaWattDay:
            return ((value * 24 * 3600) * 1000000.0)
        
        if to_unit == EnergyUnits.GigaWattDay:
            return ((value * 24 * 3600) * 1000000000.0)
        
        if to_unit == EnergyUnits.TeraWattDay:
            return ((value * 24 * 3600) * 1000000000000.0)
        
        if to_unit == EnergyUnits.DecaThermEc:
            return ((value * 1.05505585262e8) * 10.0)
        
        if to_unit == EnergyUnits.DecaThermUs:
            return ((value * 1.054804e8) * 10.0)
        
        if to_unit == EnergyUnits.DecaThermImperial:
            return ((value * 1.05505585257348e8) * 10.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
    @staticmethod
    def from_joules(joules: float):
        """
        Create a new instance of Energy from a value in joules.

        

        :param meters: The Energy value in joules.
        :type joules: float
        :return: A new instance of Energy.
        :rtype: Energy
        """
        return Energy(joules, EnergyUnits.Joule)

    
    @staticmethod
    def from_calories(calories: float):
        """
        Create a new instance of Energy from a value in calories.

        

        :param meters: The Energy value in calories.
        :type calories: float
        :return: A new instance of Energy.
        :rtype: Energy
        """
        return Energy(calories, EnergyUnits.Calorie)

    
    @staticmethod
    def from_british_thermal_units(british_thermal_units: float):
        """
        Create a new instance of Energy from a value in british_thermal_units.

        

        :param meters: The Energy value in british_thermal_units.
        :type british_thermal_units: float
        :return: A new instance of Energy.
        :rtype: Energy
        """
        return Energy(british_thermal_units, EnergyUnits.BritishThermalUnit)

    
    @staticmethod
    def from_electron_volts(electron_volts: float):
        """
        Create a new instance of Energy from a value in electron_volts.

        

        :param meters: The Energy value in electron_volts.
        :type electron_volts: float
        :return: A new instance of Energy.
        :rtype: Energy
        """
        return Energy(electron_volts, EnergyUnits.ElectronVolt)

    
    @staticmethod
    def from_foot_pounds(foot_pounds: float):
        """
        Create a new instance of Energy from a value in foot_pounds.

        

        :param meters: The Energy value in foot_pounds.
        :type foot_pounds: float
        :return: A new instance of Energy.
        :rtype: Energy
        """
        return Energy(foot_pounds, EnergyUnits.FootPound)

    
    @staticmethod
    def from_ergs(ergs: float):
        """
        Create a new instance of Energy from a value in ergs.

        

        :param meters: The Energy value in ergs.
        :type ergs: float
        :return: A new instance of Energy.
        :rtype: Energy
        """
        return Energy(ergs, EnergyUnits.Erg)

    
    @staticmethod
    def from_watt_hours(watt_hours: float):
        """
        Create a new instance of Energy from a value in watt_hours.

        

        :param meters: The Energy value in watt_hours.
        :type watt_hours: float
        :return: A new instance of Energy.
        :rtype: Energy
        """
        return Energy(watt_hours, EnergyUnits.WattHour)

    
    @staticmethod
    def from_watt_days(watt_days: float):
        """
        Create a new instance of Energy from a value in watt_days.

        

        :param meters: The Energy value in watt_days.
        :type watt_days: float
        :return: A new instance of Energy.
        :rtype: Energy
        """
        return Energy(watt_days, EnergyUnits.WattDay)

    
    @staticmethod
    def from_therms_ec(therms_ec: float):
        """
        Create a new instance of Energy from a value in therms_ec.

        

        :param meters: The Energy value in therms_ec.
        :type therms_ec: float
        :return: A new instance of Energy.
        :rtype: Energy
        """
        return Energy(therms_ec, EnergyUnits.ThermEc)

    
    @staticmethod
    def from_therms_us(therms_us: float):
        """
        Create a new instance of Energy from a value in therms_us.

        

        :param meters: The Energy value in therms_us.
        :type therms_us: float
        :return: A new instance of Energy.
        :rtype: Energy
        """
        return Energy(therms_us, EnergyUnits.ThermUs)

    
    @staticmethod
    def from_therms_imperial(therms_imperial: float):
        """
        Create a new instance of Energy from a value in therms_imperial.

        

        :param meters: The Energy value in therms_imperial.
        :type therms_imperial: float
        :return: A new instance of Energy.
        :rtype: Energy
        """
        return Energy(therms_imperial, EnergyUnits.ThermImperial)

    
    @staticmethod
    def from_horsepower_hours(horsepower_hours: float):
        """
        Create a new instance of Energy from a value in horsepower_hours.

        

        :param meters: The Energy value in horsepower_hours.
        :type horsepower_hours: float
        :return: A new instance of Energy.
        :rtype: Energy
        """
        return Energy(horsepower_hours, EnergyUnits.HorsepowerHour)

    
    @staticmethod
    def from_milli_joules(milli_joules: float):
        """
        Create a new instance of Energy from a value in milli_joules.

        

        :param meters: The Energy value in milli_joules.
        :type milli_joules: float
        :return: A new instance of Energy.
        :rtype: Energy
        """
        return Energy(milli_joules, EnergyUnits.MilliJoule)

    
    @staticmethod
    def from_kilo_joules(kilo_joules: float):
        """
        Create a new instance of Energy from a value in kilo_joules.

        

        :param meters: The Energy value in kilo_joules.
        :type kilo_joules: float
        :return: A new instance of Energy.
        :rtype: Energy
        """
        return Energy(kilo_joules, EnergyUnits.KiloJoule)

    
    @staticmethod
    def from_mega_joules(mega_joules: float):
        """
        Create a new instance of Energy from a value in mega_joules.

        

        :param meters: The Energy value in mega_joules.
        :type mega_joules: float
        :return: A new instance of Energy.
        :rtype: Energy
        """
        return Energy(mega_joules, EnergyUnits.MegaJoule)

    
    @staticmethod
    def from_giga_joules(giga_joules: float):
        """
        Create a new instance of Energy from a value in giga_joules.

        

        :param meters: The Energy value in giga_joules.
        :type giga_joules: float
        :return: A new instance of Energy.
        :rtype: Energy
        """
        return Energy(giga_joules, EnergyUnits.GigaJoule)

    
    @staticmethod
    def from_tera_joules(tera_joules: float):
        """
        Create a new instance of Energy from a value in tera_joules.

        

        :param meters: The Energy value in tera_joules.
        :type tera_joules: float
        :return: A new instance of Energy.
        :rtype: Energy
        """
        return Energy(tera_joules, EnergyUnits.TeraJoule)

    
    @staticmethod
    def from_peta_joules(peta_joules: float):
        """
        Create a new instance of Energy from a value in peta_joules.

        

        :param meters: The Energy value in peta_joules.
        :type peta_joules: float
        :return: A new instance of Energy.
        :rtype: Energy
        """
        return Energy(peta_joules, EnergyUnits.PetaJoule)

    
    @staticmethod
    def from_kilo_calories(kilo_calories: float):
        """
        Create a new instance of Energy from a value in kilo_calories.

        

        :param meters: The Energy value in kilo_calories.
        :type kilo_calories: float
        :return: A new instance of Energy.
        :rtype: Energy
        """
        return Energy(kilo_calories, EnergyUnits.KiloCalorie)

    
    @staticmethod
    def from_mega_calories(mega_calories: float):
        """
        Create a new instance of Energy from a value in mega_calories.

        

        :param meters: The Energy value in mega_calories.
        :type mega_calories: float
        :return: A new instance of Energy.
        :rtype: Energy
        """
        return Energy(mega_calories, EnergyUnits.MegaCalorie)

    
    @staticmethod
    def from_kilo_british_thermal_units(kilo_british_thermal_units: float):
        """
        Create a new instance of Energy from a value in kilo_british_thermal_units.

        

        :param meters: The Energy value in kilo_british_thermal_units.
        :type kilo_british_thermal_units: float
        :return: A new instance of Energy.
        :rtype: Energy
        """
        return Energy(kilo_british_thermal_units, EnergyUnits.KiloBritishThermalUnit)

    
    @staticmethod
    def from_mega_british_thermal_units(mega_british_thermal_units: float):
        """
        Create a new instance of Energy from a value in mega_british_thermal_units.

        

        :param meters: The Energy value in mega_british_thermal_units.
        :type mega_british_thermal_units: float
        :return: A new instance of Energy.
        :rtype: Energy
        """
        return Energy(mega_british_thermal_units, EnergyUnits.MegaBritishThermalUnit)

    
    @staticmethod
    def from_giga_british_thermal_units(giga_british_thermal_units: float):
        """
        Create a new instance of Energy from a value in giga_british_thermal_units.

        

        :param meters: The Energy value in giga_british_thermal_units.
        :type giga_british_thermal_units: float
        :return: A new instance of Energy.
        :rtype: Energy
        """
        return Energy(giga_british_thermal_units, EnergyUnits.GigaBritishThermalUnit)

    
    @staticmethod
    def from_kilo_electron_volts(kilo_electron_volts: float):
        """
        Create a new instance of Energy from a value in kilo_electron_volts.

        

        :param meters: The Energy value in kilo_electron_volts.
        :type kilo_electron_volts: float
        :return: A new instance of Energy.
        :rtype: Energy
        """
        return Energy(kilo_electron_volts, EnergyUnits.KiloElectronVolt)

    
    @staticmethod
    def from_mega_electron_volts(mega_electron_volts: float):
        """
        Create a new instance of Energy from a value in mega_electron_volts.

        

        :param meters: The Energy value in mega_electron_volts.
        :type mega_electron_volts: float
        :return: A new instance of Energy.
        :rtype: Energy
        """
        return Energy(mega_electron_volts, EnergyUnits.MegaElectronVolt)

    
    @staticmethod
    def from_giga_electron_volts(giga_electron_volts: float):
        """
        Create a new instance of Energy from a value in giga_electron_volts.

        

        :param meters: The Energy value in giga_electron_volts.
        :type giga_electron_volts: float
        :return: A new instance of Energy.
        :rtype: Energy
        """
        return Energy(giga_electron_volts, EnergyUnits.GigaElectronVolt)

    
    @staticmethod
    def from_tera_electron_volts(tera_electron_volts: float):
        """
        Create a new instance of Energy from a value in tera_electron_volts.

        

        :param meters: The Energy value in tera_electron_volts.
        :type tera_electron_volts: float
        :return: A new instance of Energy.
        :rtype: Energy
        """
        return Energy(tera_electron_volts, EnergyUnits.TeraElectronVolt)

    
    @staticmethod
    def from_kilo_watt_hours(kilo_watt_hours: float):
        """
        Create a new instance of Energy from a value in kilo_watt_hours.

        

        :param meters: The Energy value in kilo_watt_hours.
        :type kilo_watt_hours: float
        :return: A new instance of Energy.
        :rtype: Energy
        """
        return Energy(kilo_watt_hours, EnergyUnits.KiloWattHour)

    
    @staticmethod
    def from_mega_watt_hours(mega_watt_hours: float):
        """
        Create a new instance of Energy from a value in mega_watt_hours.

        

        :param meters: The Energy value in mega_watt_hours.
        :type mega_watt_hours: float
        :return: A new instance of Energy.
        :rtype: Energy
        """
        return Energy(mega_watt_hours, EnergyUnits.MegaWattHour)

    
    @staticmethod
    def from_giga_watt_hours(giga_watt_hours: float):
        """
        Create a new instance of Energy from a value in giga_watt_hours.

        

        :param meters: The Energy value in giga_watt_hours.
        :type giga_watt_hours: float
        :return: A new instance of Energy.
        :rtype: Energy
        """
        return Energy(giga_watt_hours, EnergyUnits.GigaWattHour)

    
    @staticmethod
    def from_tera_watt_hours(tera_watt_hours: float):
        """
        Create a new instance of Energy from a value in tera_watt_hours.

        

        :param meters: The Energy value in tera_watt_hours.
        :type tera_watt_hours: float
        :return: A new instance of Energy.
        :rtype: Energy
        """
        return Energy(tera_watt_hours, EnergyUnits.TeraWattHour)

    
    @staticmethod
    def from_kilo_watt_days(kilo_watt_days: float):
        """
        Create a new instance of Energy from a value in kilo_watt_days.

        

        :param meters: The Energy value in kilo_watt_days.
        :type kilo_watt_days: float
        :return: A new instance of Energy.
        :rtype: Energy
        """
        return Energy(kilo_watt_days, EnergyUnits.KiloWattDay)

    
    @staticmethod
    def from_mega_watt_days(mega_watt_days: float):
        """
        Create a new instance of Energy from a value in mega_watt_days.

        

        :param meters: The Energy value in mega_watt_days.
        :type mega_watt_days: float
        :return: A new instance of Energy.
        :rtype: Energy
        """
        return Energy(mega_watt_days, EnergyUnits.MegaWattDay)

    
    @staticmethod
    def from_giga_watt_days(giga_watt_days: float):
        """
        Create a new instance of Energy from a value in giga_watt_days.

        

        :param meters: The Energy value in giga_watt_days.
        :type giga_watt_days: float
        :return: A new instance of Energy.
        :rtype: Energy
        """
        return Energy(giga_watt_days, EnergyUnits.GigaWattDay)

    
    @staticmethod
    def from_tera_watt_days(tera_watt_days: float):
        """
        Create a new instance of Energy from a value in tera_watt_days.

        

        :param meters: The Energy value in tera_watt_days.
        :type tera_watt_days: float
        :return: A new instance of Energy.
        :rtype: Energy
        """
        return Energy(tera_watt_days, EnergyUnits.TeraWattDay)

    
    @staticmethod
    def from_deca_therms_ec(deca_therms_ec: float):
        """
        Create a new instance of Energy from a value in deca_therms_ec.

        

        :param meters: The Energy value in deca_therms_ec.
        :type deca_therms_ec: float
        :return: A new instance of Energy.
        :rtype: Energy
        """
        return Energy(deca_therms_ec, EnergyUnits.DecaThermEc)

    
    @staticmethod
    def from_deca_therms_us(deca_therms_us: float):
        """
        Create a new instance of Energy from a value in deca_therms_us.

        

        :param meters: The Energy value in deca_therms_us.
        :type deca_therms_us: float
        :return: A new instance of Energy.
        :rtype: Energy
        """
        return Energy(deca_therms_us, EnergyUnits.DecaThermUs)

    
    @staticmethod
    def from_deca_therms_imperial(deca_therms_imperial: float):
        """
        Create a new instance of Energy from a value in deca_therms_imperial.

        

        :param meters: The Energy value in deca_therms_imperial.
        :type deca_therms_imperial: float
        :return: A new instance of Energy.
        :rtype: Energy
        """
        return Energy(deca_therms_imperial, EnergyUnits.DecaThermImperial)

    
    @property
    def joules(self) -> float:
        """
        
        """
        if self.__joules != None:
            return self.__joules
        self.__joules = self.__convert_from_base(EnergyUnits.Joule)
        return self.__joules

    
    @property
    def calories(self) -> float:
        """
        
        """
        if self.__calories != None:
            return self.__calories
        self.__calories = self.__convert_from_base(EnergyUnits.Calorie)
        return self.__calories

    
    @property
    def british_thermal_units(self) -> float:
        """
        
        """
        if self.__british_thermal_units != None:
            return self.__british_thermal_units
        self.__british_thermal_units = self.__convert_from_base(EnergyUnits.BritishThermalUnit)
        return self.__british_thermal_units

    
    @property
    def electron_volts(self) -> float:
        """
        
        """
        if self.__electron_volts != None:
            return self.__electron_volts
        self.__electron_volts = self.__convert_from_base(EnergyUnits.ElectronVolt)
        return self.__electron_volts

    
    @property
    def foot_pounds(self) -> float:
        """
        
        """
        if self.__foot_pounds != None:
            return self.__foot_pounds
        self.__foot_pounds = self.__convert_from_base(EnergyUnits.FootPound)
        return self.__foot_pounds

    
    @property
    def ergs(self) -> float:
        """
        
        """
        if self.__ergs != None:
            return self.__ergs
        self.__ergs = self.__convert_from_base(EnergyUnits.Erg)
        return self.__ergs

    
    @property
    def watt_hours(self) -> float:
        """
        
        """
        if self.__watt_hours != None:
            return self.__watt_hours
        self.__watt_hours = self.__convert_from_base(EnergyUnits.WattHour)
        return self.__watt_hours

    
    @property
    def watt_days(self) -> float:
        """
        
        """
        if self.__watt_days != None:
            return self.__watt_days
        self.__watt_days = self.__convert_from_base(EnergyUnits.WattDay)
        return self.__watt_days

    
    @property
    def therms_ec(self) -> float:
        """
        
        """
        if self.__therms_ec != None:
            return self.__therms_ec
        self.__therms_ec = self.__convert_from_base(EnergyUnits.ThermEc)
        return self.__therms_ec

    
    @property
    def therms_us(self) -> float:
        """
        
        """
        if self.__therms_us != None:
            return self.__therms_us
        self.__therms_us = self.__convert_from_base(EnergyUnits.ThermUs)
        return self.__therms_us

    
    @property
    def therms_imperial(self) -> float:
        """
        
        """
        if self.__therms_imperial != None:
            return self.__therms_imperial
        self.__therms_imperial = self.__convert_from_base(EnergyUnits.ThermImperial)
        return self.__therms_imperial

    
    @property
    def horsepower_hours(self) -> float:
        """
        
        """
        if self.__horsepower_hours != None:
            return self.__horsepower_hours
        self.__horsepower_hours = self.__convert_from_base(EnergyUnits.HorsepowerHour)
        return self.__horsepower_hours

    
    @property
    def milli_joules(self) -> float:
        """
        
        """
        if self.__milli_joules != None:
            return self.__milli_joules
        self.__milli_joules = self.__convert_from_base(EnergyUnits.MilliJoule)
        return self.__milli_joules

    
    @property
    def kilo_joules(self) -> float:
        """
        
        """
        if self.__kilo_joules != None:
            return self.__kilo_joules
        self.__kilo_joules = self.__convert_from_base(EnergyUnits.KiloJoule)
        return self.__kilo_joules

    
    @property
    def mega_joules(self) -> float:
        """
        
        """
        if self.__mega_joules != None:
            return self.__mega_joules
        self.__mega_joules = self.__convert_from_base(EnergyUnits.MegaJoule)
        return self.__mega_joules

    
    @property
    def giga_joules(self) -> float:
        """
        
        """
        if self.__giga_joules != None:
            return self.__giga_joules
        self.__giga_joules = self.__convert_from_base(EnergyUnits.GigaJoule)
        return self.__giga_joules

    
    @property
    def tera_joules(self) -> float:
        """
        
        """
        if self.__tera_joules != None:
            return self.__tera_joules
        self.__tera_joules = self.__convert_from_base(EnergyUnits.TeraJoule)
        return self.__tera_joules

    
    @property
    def peta_joules(self) -> float:
        """
        
        """
        if self.__peta_joules != None:
            return self.__peta_joules
        self.__peta_joules = self.__convert_from_base(EnergyUnits.PetaJoule)
        return self.__peta_joules

    
    @property
    def kilo_calories(self) -> float:
        """
        
        """
        if self.__kilo_calories != None:
            return self.__kilo_calories
        self.__kilo_calories = self.__convert_from_base(EnergyUnits.KiloCalorie)
        return self.__kilo_calories

    
    @property
    def mega_calories(self) -> float:
        """
        
        """
        if self.__mega_calories != None:
            return self.__mega_calories
        self.__mega_calories = self.__convert_from_base(EnergyUnits.MegaCalorie)
        return self.__mega_calories

    
    @property
    def kilo_british_thermal_units(self) -> float:
        """
        
        """
        if self.__kilo_british_thermal_units != None:
            return self.__kilo_british_thermal_units
        self.__kilo_british_thermal_units = self.__convert_from_base(EnergyUnits.KiloBritishThermalUnit)
        return self.__kilo_british_thermal_units

    
    @property
    def mega_british_thermal_units(self) -> float:
        """
        
        """
        if self.__mega_british_thermal_units != None:
            return self.__mega_british_thermal_units
        self.__mega_british_thermal_units = self.__convert_from_base(EnergyUnits.MegaBritishThermalUnit)
        return self.__mega_british_thermal_units

    
    @property
    def giga_british_thermal_units(self) -> float:
        """
        
        """
        if self.__giga_british_thermal_units != None:
            return self.__giga_british_thermal_units
        self.__giga_british_thermal_units = self.__convert_from_base(EnergyUnits.GigaBritishThermalUnit)
        return self.__giga_british_thermal_units

    
    @property
    def kilo_electron_volts(self) -> float:
        """
        
        """
        if self.__kilo_electron_volts != None:
            return self.__kilo_electron_volts
        self.__kilo_electron_volts = self.__convert_from_base(EnergyUnits.KiloElectronVolt)
        return self.__kilo_electron_volts

    
    @property
    def mega_electron_volts(self) -> float:
        """
        
        """
        if self.__mega_electron_volts != None:
            return self.__mega_electron_volts
        self.__mega_electron_volts = self.__convert_from_base(EnergyUnits.MegaElectronVolt)
        return self.__mega_electron_volts

    
    @property
    def giga_electron_volts(self) -> float:
        """
        
        """
        if self.__giga_electron_volts != None:
            return self.__giga_electron_volts
        self.__giga_electron_volts = self.__convert_from_base(EnergyUnits.GigaElectronVolt)
        return self.__giga_electron_volts

    
    @property
    def tera_electron_volts(self) -> float:
        """
        
        """
        if self.__tera_electron_volts != None:
            return self.__tera_electron_volts
        self.__tera_electron_volts = self.__convert_from_base(EnergyUnits.TeraElectronVolt)
        return self.__tera_electron_volts

    
    @property
    def kilo_watt_hours(self) -> float:
        """
        
        """
        if self.__kilo_watt_hours != None:
            return self.__kilo_watt_hours
        self.__kilo_watt_hours = self.__convert_from_base(EnergyUnits.KiloWattHour)
        return self.__kilo_watt_hours

    
    @property
    def mega_watt_hours(self) -> float:
        """
        
        """
        if self.__mega_watt_hours != None:
            return self.__mega_watt_hours
        self.__mega_watt_hours = self.__convert_from_base(EnergyUnits.MegaWattHour)
        return self.__mega_watt_hours

    
    @property
    def giga_watt_hours(self) -> float:
        """
        
        """
        if self.__giga_watt_hours != None:
            return self.__giga_watt_hours
        self.__giga_watt_hours = self.__convert_from_base(EnergyUnits.GigaWattHour)
        return self.__giga_watt_hours

    
    @property
    def tera_watt_hours(self) -> float:
        """
        
        """
        if self.__tera_watt_hours != None:
            return self.__tera_watt_hours
        self.__tera_watt_hours = self.__convert_from_base(EnergyUnits.TeraWattHour)
        return self.__tera_watt_hours

    
    @property
    def kilo_watt_days(self) -> float:
        """
        
        """
        if self.__kilo_watt_days != None:
            return self.__kilo_watt_days
        self.__kilo_watt_days = self.__convert_from_base(EnergyUnits.KiloWattDay)
        return self.__kilo_watt_days

    
    @property
    def mega_watt_days(self) -> float:
        """
        
        """
        if self.__mega_watt_days != None:
            return self.__mega_watt_days
        self.__mega_watt_days = self.__convert_from_base(EnergyUnits.MegaWattDay)
        return self.__mega_watt_days

    
    @property
    def giga_watt_days(self) -> float:
        """
        
        """
        if self.__giga_watt_days != None:
            return self.__giga_watt_days
        self.__giga_watt_days = self.__convert_from_base(EnergyUnits.GigaWattDay)
        return self.__giga_watt_days

    
    @property
    def tera_watt_days(self) -> float:
        """
        
        """
        if self.__tera_watt_days != None:
            return self.__tera_watt_days
        self.__tera_watt_days = self.__convert_from_base(EnergyUnits.TeraWattDay)
        return self.__tera_watt_days

    
    @property
    def deca_therms_ec(self) -> float:
        """
        
        """
        if self.__deca_therms_ec != None:
            return self.__deca_therms_ec
        self.__deca_therms_ec = self.__convert_from_base(EnergyUnits.DecaThermEc)
        return self.__deca_therms_ec

    
    @property
    def deca_therms_us(self) -> float:
        """
        
        """
        if self.__deca_therms_us != None:
            return self.__deca_therms_us
        self.__deca_therms_us = self.__convert_from_base(EnergyUnits.DecaThermUs)
        return self.__deca_therms_us

    
    @property
    def deca_therms_imperial(self) -> float:
        """
        
        """
        if self.__deca_therms_imperial != None:
            return self.__deca_therms_imperial
        self.__deca_therms_imperial = self.__convert_from_base(EnergyUnits.DecaThermImperial)
        return self.__deca_therms_imperial

    
    def to_string(self, unit: EnergyUnits = EnergyUnits.Joule) -> string:
        """
        Format the Energy to string.
        Note! the default format for Energy is Joule.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == EnergyUnits.Joule:
            return f"""{self.joules} J"""
        
        if unit == EnergyUnits.Calorie:
            return f"""{self.calories} cal"""
        
        if unit == EnergyUnits.BritishThermalUnit:
            return f"""{self.british_thermal_units} BTU"""
        
        if unit == EnergyUnits.ElectronVolt:
            return f"""{self.electron_volts} eV"""
        
        if unit == EnergyUnits.FootPound:
            return f"""{self.foot_pounds} ft·lb"""
        
        if unit == EnergyUnits.Erg:
            return f"""{self.ergs} erg"""
        
        if unit == EnergyUnits.WattHour:
            return f"""{self.watt_hours} Wh"""
        
        if unit == EnergyUnits.WattDay:
            return f"""{self.watt_days} Wd"""
        
        if unit == EnergyUnits.ThermEc:
            return f"""{self.therms_ec} th (E.C.)"""
        
        if unit == EnergyUnits.ThermUs:
            return f"""{self.therms_us} th (U.S.)"""
        
        if unit == EnergyUnits.ThermImperial:
            return f"""{self.therms_imperial} th (imp.)"""
        
        if unit == EnergyUnits.HorsepowerHour:
            return f"""{self.horsepower_hours} hp·h"""
        
        if unit == EnergyUnits.MilliJoule:
            return f"""{self.milli_joules} """
        
        if unit == EnergyUnits.KiloJoule:
            return f"""{self.kilo_joules} """
        
        if unit == EnergyUnits.MegaJoule:
            return f"""{self.mega_joules} """
        
        if unit == EnergyUnits.GigaJoule:
            return f"""{self.giga_joules} """
        
        if unit == EnergyUnits.TeraJoule:
            return f"""{self.tera_joules} """
        
        if unit == EnergyUnits.PetaJoule:
            return f"""{self.peta_joules} """
        
        if unit == EnergyUnits.KiloCalorie:
            return f"""{self.kilo_calories} """
        
        if unit == EnergyUnits.MegaCalorie:
            return f"""{self.mega_calories} """
        
        if unit == EnergyUnits.KiloBritishThermalUnit:
            return f"""{self.kilo_british_thermal_units} """
        
        if unit == EnergyUnits.MegaBritishThermalUnit:
            return f"""{self.mega_british_thermal_units} """
        
        if unit == EnergyUnits.GigaBritishThermalUnit:
            return f"""{self.giga_british_thermal_units} """
        
        if unit == EnergyUnits.KiloElectronVolt:
            return f"""{self.kilo_electron_volts} """
        
        if unit == EnergyUnits.MegaElectronVolt:
            return f"""{self.mega_electron_volts} """
        
        if unit == EnergyUnits.GigaElectronVolt:
            return f"""{self.giga_electron_volts} """
        
        if unit == EnergyUnits.TeraElectronVolt:
            return f"""{self.tera_electron_volts} """
        
        if unit == EnergyUnits.KiloWattHour:
            return f"""{self.kilo_watt_hours} """
        
        if unit == EnergyUnits.MegaWattHour:
            return f"""{self.mega_watt_hours} """
        
        if unit == EnergyUnits.GigaWattHour:
            return f"""{self.giga_watt_hours} """
        
        if unit == EnergyUnits.TeraWattHour:
            return f"""{self.tera_watt_hours} """
        
        if unit == EnergyUnits.KiloWattDay:
            return f"""{self.kilo_watt_days} """
        
        if unit == EnergyUnits.MegaWattDay:
            return f"""{self.mega_watt_days} """
        
        if unit == EnergyUnits.GigaWattDay:
            return f"""{self.giga_watt_days} """
        
        if unit == EnergyUnits.TeraWattDay:
            return f"""{self.tera_watt_days} """
        
        if unit == EnergyUnits.DecaThermEc:
            return f"""{self.deca_therms_ec} """
        
        if unit == EnergyUnits.DecaThermUs:
            return f"""{self.deca_therms_us} """
        
        if unit == EnergyUnits.DecaThermImperial:
            return f"""{self.deca_therms_imperial} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: EnergyUnits = EnergyUnits.Joule) -> string:
        """
        Get Energy unit abbreviation.
        Note! the default abbreviation for Energy is Joule.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == EnergyUnits.Joule:
            return """J"""
        
        if unit_abbreviation == EnergyUnits.Calorie:
            return """cal"""
        
        if unit_abbreviation == EnergyUnits.BritishThermalUnit:
            return """BTU"""
        
        if unit_abbreviation == EnergyUnits.ElectronVolt:
            return """eV"""
        
        if unit_abbreviation == EnergyUnits.FootPound:
            return """ft·lb"""
        
        if unit_abbreviation == EnergyUnits.Erg:
            return """erg"""
        
        if unit_abbreviation == EnergyUnits.WattHour:
            return """Wh"""
        
        if unit_abbreviation == EnergyUnits.WattDay:
            return """Wd"""
        
        if unit_abbreviation == EnergyUnits.ThermEc:
            return """th (E.C.)"""
        
        if unit_abbreviation == EnergyUnits.ThermUs:
            return """th (U.S.)"""
        
        if unit_abbreviation == EnergyUnits.ThermImperial:
            return """th (imp.)"""
        
        if unit_abbreviation == EnergyUnits.HorsepowerHour:
            return """hp·h"""
        
        if unit_abbreviation == EnergyUnits.MilliJoule:
            return """"""
        
        if unit_abbreviation == EnergyUnits.KiloJoule:
            return """"""
        
        if unit_abbreviation == EnergyUnits.MegaJoule:
            return """"""
        
        if unit_abbreviation == EnergyUnits.GigaJoule:
            return """"""
        
        if unit_abbreviation == EnergyUnits.TeraJoule:
            return """"""
        
        if unit_abbreviation == EnergyUnits.PetaJoule:
            return """"""
        
        if unit_abbreviation == EnergyUnits.KiloCalorie:
            return """"""
        
        if unit_abbreviation == EnergyUnits.MegaCalorie:
            return """"""
        
        if unit_abbreviation == EnergyUnits.KiloBritishThermalUnit:
            return """"""
        
        if unit_abbreviation == EnergyUnits.MegaBritishThermalUnit:
            return """"""
        
        if unit_abbreviation == EnergyUnits.GigaBritishThermalUnit:
            return """"""
        
        if unit_abbreviation == EnergyUnits.KiloElectronVolt:
            return """"""
        
        if unit_abbreviation == EnergyUnits.MegaElectronVolt:
            return """"""
        
        if unit_abbreviation == EnergyUnits.GigaElectronVolt:
            return """"""
        
        if unit_abbreviation == EnergyUnits.TeraElectronVolt:
            return """"""
        
        if unit_abbreviation == EnergyUnits.KiloWattHour:
            return """"""
        
        if unit_abbreviation == EnergyUnits.MegaWattHour:
            return """"""
        
        if unit_abbreviation == EnergyUnits.GigaWattHour:
            return """"""
        
        if unit_abbreviation == EnergyUnits.TeraWattHour:
            return """"""
        
        if unit_abbreviation == EnergyUnits.KiloWattDay:
            return """"""
        
        if unit_abbreviation == EnergyUnits.MegaWattDay:
            return """"""
        
        if unit_abbreviation == EnergyUnits.GigaWattDay:
            return """"""
        
        if unit_abbreviation == EnergyUnits.TeraWattDay:
            return """"""
        
        if unit_abbreviation == EnergyUnits.DecaThermEc:
            return """"""
        
        if unit_abbreviation == EnergyUnits.DecaThermUs:
            return """"""
        
        if unit_abbreviation == EnergyUnits.DecaThermImperial:
            return """"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, Energy):
            raise TypeError("unsupported operand type(s) for +: 'Energy' and '{}'".format(type(other).__name__))
        return Energy(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, Energy):
            raise TypeError("unsupported operand type(s) for *: 'Energy' and '{}'".format(type(other).__name__))
        return Energy(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, Energy):
            raise TypeError("unsupported operand type(s) for -: 'Energy' and '{}'".format(type(other).__name__))
        return Energy(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, Energy):
            raise TypeError("unsupported operand type(s) for /: 'Energy' and '{}'".format(type(other).__name__))
        return Energy(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, Energy):
            raise TypeError("unsupported operand type(s) for %: 'Energy' and '{}'".format(type(other).__name__))
        return Energy(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, Energy):
            raise TypeError("unsupported operand type(s) for **: 'Energy' and '{}'".format(type(other).__name__))
        return Energy(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, Energy):
            raise TypeError("unsupported operand type(s) for ==: 'Energy' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, Energy):
            raise TypeError("unsupported operand type(s) for <: 'Energy' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, Energy):
            raise TypeError("unsupported operand type(s) for >: 'Energy' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, Energy):
            raise TypeError("unsupported operand type(s) for <=: 'Energy' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, Energy):
            raise TypeError("unsupported operand type(s) for >=: 'Energy' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value
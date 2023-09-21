from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



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
        
        Nanojoule = 'nanojoule'
        """
            
        """
        
        Microjoule = 'microjoule'
        """
            
        """
        
        Millijoule = 'millijoule'
        """
            
        """
        
        Kilojoule = 'kilojoule'
        """
            
        """
        
        Megajoule = 'megajoule'
        """
            
        """
        
        Gigajoule = 'gigajoule'
        """
            
        """
        
        Terajoule = 'terajoule'
        """
            
        """
        
        Petajoule = 'petajoule'
        """
            
        """
        
        Kilocalorie = 'kilocalorie'
        """
            
        """
        
        Megacalorie = 'megacalorie'
        """
            
        """
        
        KilobritishThermalUnit = 'kilobritish_thermal_unit'
        """
            
        """
        
        MegabritishThermalUnit = 'megabritish_thermal_unit'
        """
            
        """
        
        GigabritishThermalUnit = 'gigabritish_thermal_unit'
        """
            
        """
        
        KiloelectronVolt = 'kiloelectron_volt'
        """
            
        """
        
        MegaelectronVolt = 'megaelectron_volt'
        """
            
        """
        
        GigaelectronVolt = 'gigaelectron_volt'
        """
            
        """
        
        TeraelectronVolt = 'teraelectron_volt'
        """
            
        """
        
        KilowattHour = 'kilowatt_hour'
        """
            
        """
        
        MegawattHour = 'megawatt_hour'
        """
            
        """
        
        GigawattHour = 'gigawatt_hour'
        """
            
        """
        
        TerawattHour = 'terawatt_hour'
        """
            
        """
        
        KilowattDay = 'kilowatt_day'
        """
            
        """
        
        MegawattDay = 'megawatt_day'
        """
            
        """
        
        GigawattDay = 'gigawatt_day'
        """
            
        """
        
        TerawattDay = 'terawatt_day'
        """
            
        """
        
        DecathermEc = 'decatherm_ec'
        """
            
        """
        
        DecathermUs = 'decatherm_us'
        """
            
        """
        
        DecathermImperial = 'decatherm_imperial'
        """
            
        """
        

class Energy(AbstractMeasure):
    """
    The joule, symbol J, is a derived unit of energy, work, or amount of heat in the International System of Units. It is equal to the energy transferred (or work done) when applying a force of one newton through a distance of one metre (1 newton metre or N·m), or in passing an electric current of one ampere through a resistance of one ohm for one second. Many other units of energy are included. Please do not confuse this definition of the calorie with the one colloquially used by the food industry, the large calorie, which is equivalent to 1 kcal. Thermochemical definition of the calorie is used. For BTU, the IT definition is used.

    Args:
        value (float): The value.
        from_unit (EnergyUnits): The Energy unit to create from, The default unit is Joule
    """
    def __init__(self, value: float, from_unit: EnergyUnits = EnergyUnits.Joule):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
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
        
        self.__nanojoules = None
        
        self.__microjoules = None
        
        self.__millijoules = None
        
        self.__kilojoules = None
        
        self.__megajoules = None
        
        self.__gigajoules = None
        
        self.__terajoules = None
        
        self.__petajoules = None
        
        self.__kilocalories = None
        
        self.__megacalories = None
        
        self.__kilobritish_thermal_units = None
        
        self.__megabritish_thermal_units = None
        
        self.__gigabritish_thermal_units = None
        
        self.__kiloelectron_volts = None
        
        self.__megaelectron_volts = None
        
        self.__gigaelectron_volts = None
        
        self.__teraelectron_volts = None
        
        self.__kilowatt_hours = None
        
        self.__megawatt_hours = None
        
        self.__gigawatt_hours = None
        
        self.__terawatt_hours = None
        
        self.__kilowatt_days = None
        
        self.__megawatt_days = None
        
        self.__gigawatt_days = None
        
        self.__terawatt_days = None
        
        self.__decatherms_ec = None
        
        self.__decatherms_us = None
        
        self.__decatherms_imperial = None
        

    def convert(self, unit: EnergyUnits) -> float:
        return self.__convert_from_base(unit)

    def __convert_from_base(self, from_unit: EnergyUnits) -> float:
        value = self._value
        
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
        
        if from_unit == EnergyUnits.Nanojoule:
            return ((value) / 1e-09)
        
        if from_unit == EnergyUnits.Microjoule:
            return ((value) / 1e-06)
        
        if from_unit == EnergyUnits.Millijoule:
            return ((value) / 0.001)
        
        if from_unit == EnergyUnits.Kilojoule:
            return ((value) / 1000.0)
        
        if from_unit == EnergyUnits.Megajoule:
            return ((value) / 1000000.0)
        
        if from_unit == EnergyUnits.Gigajoule:
            return ((value) / 1000000000.0)
        
        if from_unit == EnergyUnits.Terajoule:
            return ((value) / 1000000000000.0)
        
        if from_unit == EnergyUnits.Petajoule:
            return ((value) / 1000000000000000.0)
        
        if from_unit == EnergyUnits.Kilocalorie:
            return ((value / 4.184) / 1000.0)
        
        if from_unit == EnergyUnits.Megacalorie:
            return ((value / 4.184) / 1000000.0)
        
        if from_unit == EnergyUnits.KilobritishThermalUnit:
            return ((value / 1055.05585262) / 1000.0)
        
        if from_unit == EnergyUnits.MegabritishThermalUnit:
            return ((value / 1055.05585262) / 1000000.0)
        
        if from_unit == EnergyUnits.GigabritishThermalUnit:
            return ((value / 1055.05585262) / 1000000000.0)
        
        if from_unit == EnergyUnits.KiloelectronVolt:
            return ((value / 1.602176565e-19) / 1000.0)
        
        if from_unit == EnergyUnits.MegaelectronVolt:
            return ((value / 1.602176565e-19) / 1000000.0)
        
        if from_unit == EnergyUnits.GigaelectronVolt:
            return ((value / 1.602176565e-19) / 1000000000.0)
        
        if from_unit == EnergyUnits.TeraelectronVolt:
            return ((value / 1.602176565e-19) / 1000000000000.0)
        
        if from_unit == EnergyUnits.KilowattHour:
            return ((value / 3600) / 1000.0)
        
        if from_unit == EnergyUnits.MegawattHour:
            return ((value / 3600) / 1000000.0)
        
        if from_unit == EnergyUnits.GigawattHour:
            return ((value / 3600) / 1000000000.0)
        
        if from_unit == EnergyUnits.TerawattHour:
            return ((value / 3600) / 1000000000000.0)
        
        if from_unit == EnergyUnits.KilowattDay:
            return ((value / (24 * 3600)) / 1000.0)
        
        if from_unit == EnergyUnits.MegawattDay:
            return ((value / (24 * 3600)) / 1000000.0)
        
        if from_unit == EnergyUnits.GigawattDay:
            return ((value / (24 * 3600)) / 1000000000.0)
        
        if from_unit == EnergyUnits.TerawattDay:
            return ((value / (24 * 3600)) / 1000000000000.0)
        
        if from_unit == EnergyUnits.DecathermEc:
            return ((value / 1.05505585262e8) / 10.0)
        
        if from_unit == EnergyUnits.DecathermUs:
            return ((value / 1.054804e8) / 10.0)
        
        if from_unit == EnergyUnits.DecathermImperial:
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
        
        if to_unit == EnergyUnits.Nanojoule:
            return ((value) * 1e-09)
        
        if to_unit == EnergyUnits.Microjoule:
            return ((value) * 1e-06)
        
        if to_unit == EnergyUnits.Millijoule:
            return ((value) * 0.001)
        
        if to_unit == EnergyUnits.Kilojoule:
            return ((value) * 1000.0)
        
        if to_unit == EnergyUnits.Megajoule:
            return ((value) * 1000000.0)
        
        if to_unit == EnergyUnits.Gigajoule:
            return ((value) * 1000000000.0)
        
        if to_unit == EnergyUnits.Terajoule:
            return ((value) * 1000000000000.0)
        
        if to_unit == EnergyUnits.Petajoule:
            return ((value) * 1000000000000000.0)
        
        if to_unit == EnergyUnits.Kilocalorie:
            return ((value * 4.184) * 1000.0)
        
        if to_unit == EnergyUnits.Megacalorie:
            return ((value * 4.184) * 1000000.0)
        
        if to_unit == EnergyUnits.KilobritishThermalUnit:
            return ((value * 1055.05585262) * 1000.0)
        
        if to_unit == EnergyUnits.MegabritishThermalUnit:
            return ((value * 1055.05585262) * 1000000.0)
        
        if to_unit == EnergyUnits.GigabritishThermalUnit:
            return ((value * 1055.05585262) * 1000000000.0)
        
        if to_unit == EnergyUnits.KiloelectronVolt:
            return ((value * 1.602176565e-19) * 1000.0)
        
        if to_unit == EnergyUnits.MegaelectronVolt:
            return ((value * 1.602176565e-19) * 1000000.0)
        
        if to_unit == EnergyUnits.GigaelectronVolt:
            return ((value * 1.602176565e-19) * 1000000000.0)
        
        if to_unit == EnergyUnits.TeraelectronVolt:
            return ((value * 1.602176565e-19) * 1000000000000.0)
        
        if to_unit == EnergyUnits.KilowattHour:
            return ((value * 3600) * 1000.0)
        
        if to_unit == EnergyUnits.MegawattHour:
            return ((value * 3600) * 1000000.0)
        
        if to_unit == EnergyUnits.GigawattHour:
            return ((value * 3600) * 1000000000.0)
        
        if to_unit == EnergyUnits.TerawattHour:
            return ((value * 3600) * 1000000000000.0)
        
        if to_unit == EnergyUnits.KilowattDay:
            return ((value * 24 * 3600) * 1000.0)
        
        if to_unit == EnergyUnits.MegawattDay:
            return ((value * 24 * 3600) * 1000000.0)
        
        if to_unit == EnergyUnits.GigawattDay:
            return ((value * 24 * 3600) * 1000000000.0)
        
        if to_unit == EnergyUnits.TerawattDay:
            return ((value * 24 * 3600) * 1000000000000.0)
        
        if to_unit == EnergyUnits.DecathermEc:
            return ((value * 1.05505585262e8) * 10.0)
        
        if to_unit == EnergyUnits.DecathermUs:
            return ((value * 1.054804e8) * 10.0)
        
        if to_unit == EnergyUnits.DecathermImperial:
            return ((value * 1.05505585257348e8) * 10.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
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
    def from_nanojoules(nanojoules: float):
        """
        Create a new instance of Energy from a value in nanojoules.

        

        :param meters: The Energy value in nanojoules.
        :type nanojoules: float
        :return: A new instance of Energy.
        :rtype: Energy
        """
        return Energy(nanojoules, EnergyUnits.Nanojoule)

    
    @staticmethod
    def from_microjoules(microjoules: float):
        """
        Create a new instance of Energy from a value in microjoules.

        

        :param meters: The Energy value in microjoules.
        :type microjoules: float
        :return: A new instance of Energy.
        :rtype: Energy
        """
        return Energy(microjoules, EnergyUnits.Microjoule)

    
    @staticmethod
    def from_millijoules(millijoules: float):
        """
        Create a new instance of Energy from a value in millijoules.

        

        :param meters: The Energy value in millijoules.
        :type millijoules: float
        :return: A new instance of Energy.
        :rtype: Energy
        """
        return Energy(millijoules, EnergyUnits.Millijoule)

    
    @staticmethod
    def from_kilojoules(kilojoules: float):
        """
        Create a new instance of Energy from a value in kilojoules.

        

        :param meters: The Energy value in kilojoules.
        :type kilojoules: float
        :return: A new instance of Energy.
        :rtype: Energy
        """
        return Energy(kilojoules, EnergyUnits.Kilojoule)

    
    @staticmethod
    def from_megajoules(megajoules: float):
        """
        Create a new instance of Energy from a value in megajoules.

        

        :param meters: The Energy value in megajoules.
        :type megajoules: float
        :return: A new instance of Energy.
        :rtype: Energy
        """
        return Energy(megajoules, EnergyUnits.Megajoule)

    
    @staticmethod
    def from_gigajoules(gigajoules: float):
        """
        Create a new instance of Energy from a value in gigajoules.

        

        :param meters: The Energy value in gigajoules.
        :type gigajoules: float
        :return: A new instance of Energy.
        :rtype: Energy
        """
        return Energy(gigajoules, EnergyUnits.Gigajoule)

    
    @staticmethod
    def from_terajoules(terajoules: float):
        """
        Create a new instance of Energy from a value in terajoules.

        

        :param meters: The Energy value in terajoules.
        :type terajoules: float
        :return: A new instance of Energy.
        :rtype: Energy
        """
        return Energy(terajoules, EnergyUnits.Terajoule)

    
    @staticmethod
    def from_petajoules(petajoules: float):
        """
        Create a new instance of Energy from a value in petajoules.

        

        :param meters: The Energy value in petajoules.
        :type petajoules: float
        :return: A new instance of Energy.
        :rtype: Energy
        """
        return Energy(petajoules, EnergyUnits.Petajoule)

    
    @staticmethod
    def from_kilocalories(kilocalories: float):
        """
        Create a new instance of Energy from a value in kilocalories.

        

        :param meters: The Energy value in kilocalories.
        :type kilocalories: float
        :return: A new instance of Energy.
        :rtype: Energy
        """
        return Energy(kilocalories, EnergyUnits.Kilocalorie)

    
    @staticmethod
    def from_megacalories(megacalories: float):
        """
        Create a new instance of Energy from a value in megacalories.

        

        :param meters: The Energy value in megacalories.
        :type megacalories: float
        :return: A new instance of Energy.
        :rtype: Energy
        """
        return Energy(megacalories, EnergyUnits.Megacalorie)

    
    @staticmethod
    def from_kilobritish_thermal_units(kilobritish_thermal_units: float):
        """
        Create a new instance of Energy from a value in kilobritish_thermal_units.

        

        :param meters: The Energy value in kilobritish_thermal_units.
        :type kilobritish_thermal_units: float
        :return: A new instance of Energy.
        :rtype: Energy
        """
        return Energy(kilobritish_thermal_units, EnergyUnits.KilobritishThermalUnit)

    
    @staticmethod
    def from_megabritish_thermal_units(megabritish_thermal_units: float):
        """
        Create a new instance of Energy from a value in megabritish_thermal_units.

        

        :param meters: The Energy value in megabritish_thermal_units.
        :type megabritish_thermal_units: float
        :return: A new instance of Energy.
        :rtype: Energy
        """
        return Energy(megabritish_thermal_units, EnergyUnits.MegabritishThermalUnit)

    
    @staticmethod
    def from_gigabritish_thermal_units(gigabritish_thermal_units: float):
        """
        Create a new instance of Energy from a value in gigabritish_thermal_units.

        

        :param meters: The Energy value in gigabritish_thermal_units.
        :type gigabritish_thermal_units: float
        :return: A new instance of Energy.
        :rtype: Energy
        """
        return Energy(gigabritish_thermal_units, EnergyUnits.GigabritishThermalUnit)

    
    @staticmethod
    def from_kiloelectron_volts(kiloelectron_volts: float):
        """
        Create a new instance of Energy from a value in kiloelectron_volts.

        

        :param meters: The Energy value in kiloelectron_volts.
        :type kiloelectron_volts: float
        :return: A new instance of Energy.
        :rtype: Energy
        """
        return Energy(kiloelectron_volts, EnergyUnits.KiloelectronVolt)

    
    @staticmethod
    def from_megaelectron_volts(megaelectron_volts: float):
        """
        Create a new instance of Energy from a value in megaelectron_volts.

        

        :param meters: The Energy value in megaelectron_volts.
        :type megaelectron_volts: float
        :return: A new instance of Energy.
        :rtype: Energy
        """
        return Energy(megaelectron_volts, EnergyUnits.MegaelectronVolt)

    
    @staticmethod
    def from_gigaelectron_volts(gigaelectron_volts: float):
        """
        Create a new instance of Energy from a value in gigaelectron_volts.

        

        :param meters: The Energy value in gigaelectron_volts.
        :type gigaelectron_volts: float
        :return: A new instance of Energy.
        :rtype: Energy
        """
        return Energy(gigaelectron_volts, EnergyUnits.GigaelectronVolt)

    
    @staticmethod
    def from_teraelectron_volts(teraelectron_volts: float):
        """
        Create a new instance of Energy from a value in teraelectron_volts.

        

        :param meters: The Energy value in teraelectron_volts.
        :type teraelectron_volts: float
        :return: A new instance of Energy.
        :rtype: Energy
        """
        return Energy(teraelectron_volts, EnergyUnits.TeraelectronVolt)

    
    @staticmethod
    def from_kilowatt_hours(kilowatt_hours: float):
        """
        Create a new instance of Energy from a value in kilowatt_hours.

        

        :param meters: The Energy value in kilowatt_hours.
        :type kilowatt_hours: float
        :return: A new instance of Energy.
        :rtype: Energy
        """
        return Energy(kilowatt_hours, EnergyUnits.KilowattHour)

    
    @staticmethod
    def from_megawatt_hours(megawatt_hours: float):
        """
        Create a new instance of Energy from a value in megawatt_hours.

        

        :param meters: The Energy value in megawatt_hours.
        :type megawatt_hours: float
        :return: A new instance of Energy.
        :rtype: Energy
        """
        return Energy(megawatt_hours, EnergyUnits.MegawattHour)

    
    @staticmethod
    def from_gigawatt_hours(gigawatt_hours: float):
        """
        Create a new instance of Energy from a value in gigawatt_hours.

        

        :param meters: The Energy value in gigawatt_hours.
        :type gigawatt_hours: float
        :return: A new instance of Energy.
        :rtype: Energy
        """
        return Energy(gigawatt_hours, EnergyUnits.GigawattHour)

    
    @staticmethod
    def from_terawatt_hours(terawatt_hours: float):
        """
        Create a new instance of Energy from a value in terawatt_hours.

        

        :param meters: The Energy value in terawatt_hours.
        :type terawatt_hours: float
        :return: A new instance of Energy.
        :rtype: Energy
        """
        return Energy(terawatt_hours, EnergyUnits.TerawattHour)

    
    @staticmethod
    def from_kilowatt_days(kilowatt_days: float):
        """
        Create a new instance of Energy from a value in kilowatt_days.

        

        :param meters: The Energy value in kilowatt_days.
        :type kilowatt_days: float
        :return: A new instance of Energy.
        :rtype: Energy
        """
        return Energy(kilowatt_days, EnergyUnits.KilowattDay)

    
    @staticmethod
    def from_megawatt_days(megawatt_days: float):
        """
        Create a new instance of Energy from a value in megawatt_days.

        

        :param meters: The Energy value in megawatt_days.
        :type megawatt_days: float
        :return: A new instance of Energy.
        :rtype: Energy
        """
        return Energy(megawatt_days, EnergyUnits.MegawattDay)

    
    @staticmethod
    def from_gigawatt_days(gigawatt_days: float):
        """
        Create a new instance of Energy from a value in gigawatt_days.

        

        :param meters: The Energy value in gigawatt_days.
        :type gigawatt_days: float
        :return: A new instance of Energy.
        :rtype: Energy
        """
        return Energy(gigawatt_days, EnergyUnits.GigawattDay)

    
    @staticmethod
    def from_terawatt_days(terawatt_days: float):
        """
        Create a new instance of Energy from a value in terawatt_days.

        

        :param meters: The Energy value in terawatt_days.
        :type terawatt_days: float
        :return: A new instance of Energy.
        :rtype: Energy
        """
        return Energy(terawatt_days, EnergyUnits.TerawattDay)

    
    @staticmethod
    def from_decatherms_ec(decatherms_ec: float):
        """
        Create a new instance of Energy from a value in decatherms_ec.

        

        :param meters: The Energy value in decatherms_ec.
        :type decatherms_ec: float
        :return: A new instance of Energy.
        :rtype: Energy
        """
        return Energy(decatherms_ec, EnergyUnits.DecathermEc)

    
    @staticmethod
    def from_decatherms_us(decatherms_us: float):
        """
        Create a new instance of Energy from a value in decatherms_us.

        

        :param meters: The Energy value in decatherms_us.
        :type decatherms_us: float
        :return: A new instance of Energy.
        :rtype: Energy
        """
        return Energy(decatherms_us, EnergyUnits.DecathermUs)

    
    @staticmethod
    def from_decatherms_imperial(decatherms_imperial: float):
        """
        Create a new instance of Energy from a value in decatherms_imperial.

        

        :param meters: The Energy value in decatherms_imperial.
        :type decatherms_imperial: float
        :return: A new instance of Energy.
        :rtype: Energy
        """
        return Energy(decatherms_imperial, EnergyUnits.DecathermImperial)

    
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
    def nanojoules(self) -> float:
        """
        
        """
        if self.__nanojoules != None:
            return self.__nanojoules
        self.__nanojoules = self.__convert_from_base(EnergyUnits.Nanojoule)
        return self.__nanojoules

    
    @property
    def microjoules(self) -> float:
        """
        
        """
        if self.__microjoules != None:
            return self.__microjoules
        self.__microjoules = self.__convert_from_base(EnergyUnits.Microjoule)
        return self.__microjoules

    
    @property
    def millijoules(self) -> float:
        """
        
        """
        if self.__millijoules != None:
            return self.__millijoules
        self.__millijoules = self.__convert_from_base(EnergyUnits.Millijoule)
        return self.__millijoules

    
    @property
    def kilojoules(self) -> float:
        """
        
        """
        if self.__kilojoules != None:
            return self.__kilojoules
        self.__kilojoules = self.__convert_from_base(EnergyUnits.Kilojoule)
        return self.__kilojoules

    
    @property
    def megajoules(self) -> float:
        """
        
        """
        if self.__megajoules != None:
            return self.__megajoules
        self.__megajoules = self.__convert_from_base(EnergyUnits.Megajoule)
        return self.__megajoules

    
    @property
    def gigajoules(self) -> float:
        """
        
        """
        if self.__gigajoules != None:
            return self.__gigajoules
        self.__gigajoules = self.__convert_from_base(EnergyUnits.Gigajoule)
        return self.__gigajoules

    
    @property
    def terajoules(self) -> float:
        """
        
        """
        if self.__terajoules != None:
            return self.__terajoules
        self.__terajoules = self.__convert_from_base(EnergyUnits.Terajoule)
        return self.__terajoules

    
    @property
    def petajoules(self) -> float:
        """
        
        """
        if self.__petajoules != None:
            return self.__petajoules
        self.__petajoules = self.__convert_from_base(EnergyUnits.Petajoule)
        return self.__petajoules

    
    @property
    def kilocalories(self) -> float:
        """
        
        """
        if self.__kilocalories != None:
            return self.__kilocalories
        self.__kilocalories = self.__convert_from_base(EnergyUnits.Kilocalorie)
        return self.__kilocalories

    
    @property
    def megacalories(self) -> float:
        """
        
        """
        if self.__megacalories != None:
            return self.__megacalories
        self.__megacalories = self.__convert_from_base(EnergyUnits.Megacalorie)
        return self.__megacalories

    
    @property
    def kilobritish_thermal_units(self) -> float:
        """
        
        """
        if self.__kilobritish_thermal_units != None:
            return self.__kilobritish_thermal_units
        self.__kilobritish_thermal_units = self.__convert_from_base(EnergyUnits.KilobritishThermalUnit)
        return self.__kilobritish_thermal_units

    
    @property
    def megabritish_thermal_units(self) -> float:
        """
        
        """
        if self.__megabritish_thermal_units != None:
            return self.__megabritish_thermal_units
        self.__megabritish_thermal_units = self.__convert_from_base(EnergyUnits.MegabritishThermalUnit)
        return self.__megabritish_thermal_units

    
    @property
    def gigabritish_thermal_units(self) -> float:
        """
        
        """
        if self.__gigabritish_thermal_units != None:
            return self.__gigabritish_thermal_units
        self.__gigabritish_thermal_units = self.__convert_from_base(EnergyUnits.GigabritishThermalUnit)
        return self.__gigabritish_thermal_units

    
    @property
    def kiloelectron_volts(self) -> float:
        """
        
        """
        if self.__kiloelectron_volts != None:
            return self.__kiloelectron_volts
        self.__kiloelectron_volts = self.__convert_from_base(EnergyUnits.KiloelectronVolt)
        return self.__kiloelectron_volts

    
    @property
    def megaelectron_volts(self) -> float:
        """
        
        """
        if self.__megaelectron_volts != None:
            return self.__megaelectron_volts
        self.__megaelectron_volts = self.__convert_from_base(EnergyUnits.MegaelectronVolt)
        return self.__megaelectron_volts

    
    @property
    def gigaelectron_volts(self) -> float:
        """
        
        """
        if self.__gigaelectron_volts != None:
            return self.__gigaelectron_volts
        self.__gigaelectron_volts = self.__convert_from_base(EnergyUnits.GigaelectronVolt)
        return self.__gigaelectron_volts

    
    @property
    def teraelectron_volts(self) -> float:
        """
        
        """
        if self.__teraelectron_volts != None:
            return self.__teraelectron_volts
        self.__teraelectron_volts = self.__convert_from_base(EnergyUnits.TeraelectronVolt)
        return self.__teraelectron_volts

    
    @property
    def kilowatt_hours(self) -> float:
        """
        
        """
        if self.__kilowatt_hours != None:
            return self.__kilowatt_hours
        self.__kilowatt_hours = self.__convert_from_base(EnergyUnits.KilowattHour)
        return self.__kilowatt_hours

    
    @property
    def megawatt_hours(self) -> float:
        """
        
        """
        if self.__megawatt_hours != None:
            return self.__megawatt_hours
        self.__megawatt_hours = self.__convert_from_base(EnergyUnits.MegawattHour)
        return self.__megawatt_hours

    
    @property
    def gigawatt_hours(self) -> float:
        """
        
        """
        if self.__gigawatt_hours != None:
            return self.__gigawatt_hours
        self.__gigawatt_hours = self.__convert_from_base(EnergyUnits.GigawattHour)
        return self.__gigawatt_hours

    
    @property
    def terawatt_hours(self) -> float:
        """
        
        """
        if self.__terawatt_hours != None:
            return self.__terawatt_hours
        self.__terawatt_hours = self.__convert_from_base(EnergyUnits.TerawattHour)
        return self.__terawatt_hours

    
    @property
    def kilowatt_days(self) -> float:
        """
        
        """
        if self.__kilowatt_days != None:
            return self.__kilowatt_days
        self.__kilowatt_days = self.__convert_from_base(EnergyUnits.KilowattDay)
        return self.__kilowatt_days

    
    @property
    def megawatt_days(self) -> float:
        """
        
        """
        if self.__megawatt_days != None:
            return self.__megawatt_days
        self.__megawatt_days = self.__convert_from_base(EnergyUnits.MegawattDay)
        return self.__megawatt_days

    
    @property
    def gigawatt_days(self) -> float:
        """
        
        """
        if self.__gigawatt_days != None:
            return self.__gigawatt_days
        self.__gigawatt_days = self.__convert_from_base(EnergyUnits.GigawattDay)
        return self.__gigawatt_days

    
    @property
    def terawatt_days(self) -> float:
        """
        
        """
        if self.__terawatt_days != None:
            return self.__terawatt_days
        self.__terawatt_days = self.__convert_from_base(EnergyUnits.TerawattDay)
        return self.__terawatt_days

    
    @property
    def decatherms_ec(self) -> float:
        """
        
        """
        if self.__decatherms_ec != None:
            return self.__decatherms_ec
        self.__decatherms_ec = self.__convert_from_base(EnergyUnits.DecathermEc)
        return self.__decatherms_ec

    
    @property
    def decatherms_us(self) -> float:
        """
        
        """
        if self.__decatherms_us != None:
            return self.__decatherms_us
        self.__decatherms_us = self.__convert_from_base(EnergyUnits.DecathermUs)
        return self.__decatherms_us

    
    @property
    def decatherms_imperial(self) -> float:
        """
        
        """
        if self.__decatherms_imperial != None:
            return self.__decatherms_imperial
        self.__decatherms_imperial = self.__convert_from_base(EnergyUnits.DecathermImperial)
        return self.__decatherms_imperial

    
    def to_string(self, unit: EnergyUnits = EnergyUnits.Joule) -> str:
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
        
        if unit == EnergyUnits.Nanojoule:
            return f"""{self.nanojoules} nJ"""
        
        if unit == EnergyUnits.Microjoule:
            return f"""{self.microjoules} μJ"""
        
        if unit == EnergyUnits.Millijoule:
            return f"""{self.millijoules} mJ"""
        
        if unit == EnergyUnits.Kilojoule:
            return f"""{self.kilojoules} kJ"""
        
        if unit == EnergyUnits.Megajoule:
            return f"""{self.megajoules} MJ"""
        
        if unit == EnergyUnits.Gigajoule:
            return f"""{self.gigajoules} GJ"""
        
        if unit == EnergyUnits.Terajoule:
            return f"""{self.terajoules} TJ"""
        
        if unit == EnergyUnits.Petajoule:
            return f"""{self.petajoules} PJ"""
        
        if unit == EnergyUnits.Kilocalorie:
            return f"""{self.kilocalories} kcal"""
        
        if unit == EnergyUnits.Megacalorie:
            return f"""{self.megacalories} Mcal"""
        
        if unit == EnergyUnits.KilobritishThermalUnit:
            return f"""{self.kilobritish_thermal_units} kBTU"""
        
        if unit == EnergyUnits.MegabritishThermalUnit:
            return f"""{self.megabritish_thermal_units} MBTU"""
        
        if unit == EnergyUnits.GigabritishThermalUnit:
            return f"""{self.gigabritish_thermal_units} GBTU"""
        
        if unit == EnergyUnits.KiloelectronVolt:
            return f"""{self.kiloelectron_volts} keV"""
        
        if unit == EnergyUnits.MegaelectronVolt:
            return f"""{self.megaelectron_volts} MeV"""
        
        if unit == EnergyUnits.GigaelectronVolt:
            return f"""{self.gigaelectron_volts} GeV"""
        
        if unit == EnergyUnits.TeraelectronVolt:
            return f"""{self.teraelectron_volts} TeV"""
        
        if unit == EnergyUnits.KilowattHour:
            return f"""{self.kilowatt_hours} kWh"""
        
        if unit == EnergyUnits.MegawattHour:
            return f"""{self.megawatt_hours} MWh"""
        
        if unit == EnergyUnits.GigawattHour:
            return f"""{self.gigawatt_hours} GWh"""
        
        if unit == EnergyUnits.TerawattHour:
            return f"""{self.terawatt_hours} TWh"""
        
        if unit == EnergyUnits.KilowattDay:
            return f"""{self.kilowatt_days} kWd"""
        
        if unit == EnergyUnits.MegawattDay:
            return f"""{self.megawatt_days} MWd"""
        
        if unit == EnergyUnits.GigawattDay:
            return f"""{self.gigawatt_days} GWd"""
        
        if unit == EnergyUnits.TerawattDay:
            return f"""{self.terawatt_days} TWd"""
        
        if unit == EnergyUnits.DecathermEc:
            return f"""{self.decatherms_ec} dath (E.C.)"""
        
        if unit == EnergyUnits.DecathermUs:
            return f"""{self.decatherms_us} dath (U.S.)"""
        
        if unit == EnergyUnits.DecathermImperial:
            return f"""{self.decatherms_imperial} dath (imp.)"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: EnergyUnits = EnergyUnits.Joule) -> str:
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
        
        if unit_abbreviation == EnergyUnits.Nanojoule:
            return """nJ"""
        
        if unit_abbreviation == EnergyUnits.Microjoule:
            return """μJ"""
        
        if unit_abbreviation == EnergyUnits.Millijoule:
            return """mJ"""
        
        if unit_abbreviation == EnergyUnits.Kilojoule:
            return """kJ"""
        
        if unit_abbreviation == EnergyUnits.Megajoule:
            return """MJ"""
        
        if unit_abbreviation == EnergyUnits.Gigajoule:
            return """GJ"""
        
        if unit_abbreviation == EnergyUnits.Terajoule:
            return """TJ"""
        
        if unit_abbreviation == EnergyUnits.Petajoule:
            return """PJ"""
        
        if unit_abbreviation == EnergyUnits.Kilocalorie:
            return """kcal"""
        
        if unit_abbreviation == EnergyUnits.Megacalorie:
            return """Mcal"""
        
        if unit_abbreviation == EnergyUnits.KilobritishThermalUnit:
            return """kBTU"""
        
        if unit_abbreviation == EnergyUnits.MegabritishThermalUnit:
            return """MBTU"""
        
        if unit_abbreviation == EnergyUnits.GigabritishThermalUnit:
            return """GBTU"""
        
        if unit_abbreviation == EnergyUnits.KiloelectronVolt:
            return """keV"""
        
        if unit_abbreviation == EnergyUnits.MegaelectronVolt:
            return """MeV"""
        
        if unit_abbreviation == EnergyUnits.GigaelectronVolt:
            return """GeV"""
        
        if unit_abbreviation == EnergyUnits.TeraelectronVolt:
            return """TeV"""
        
        if unit_abbreviation == EnergyUnits.KilowattHour:
            return """kWh"""
        
        if unit_abbreviation == EnergyUnits.MegawattHour:
            return """MWh"""
        
        if unit_abbreviation == EnergyUnits.GigawattHour:
            return """GWh"""
        
        if unit_abbreviation == EnergyUnits.TerawattHour:
            return """TWh"""
        
        if unit_abbreviation == EnergyUnits.KilowattDay:
            return """kWd"""
        
        if unit_abbreviation == EnergyUnits.MegawattDay:
            return """MWd"""
        
        if unit_abbreviation == EnergyUnits.GigawattDay:
            return """GWd"""
        
        if unit_abbreviation == EnergyUnits.TerawattDay:
            return """TWd"""
        
        if unit_abbreviation == EnergyUnits.DecathermEc:
            return """dath (E.C.)"""
        
        if unit_abbreviation == EnergyUnits.DecathermUs:
            return """dath (U.S.)"""
        
        if unit_abbreviation == EnergyUnits.DecathermImperial:
            return """dath (imp.)"""
        
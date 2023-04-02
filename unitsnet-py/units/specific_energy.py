from enum import Enum
import math
import string


class SpecificEnergyUnits(Enum):
        """
            SpecificEnergyUnits enumeration
        """
        
        JoulePerKilogram = 'joule_per_kilogram'
        """
            
        """
        
        MegaJoulePerTonne = 'mega_joule_per_tonne'
        """
            
        """
        
        CaloriePerGram = 'calorie_per_gram'
        """
            
        """
        
        WattHourPerKilogram = 'watt_hour_per_kilogram'
        """
            
        """
        
        WattDayPerKilogram = 'watt_day_per_kilogram'
        """
            
        """
        
        WattDayPerTonne = 'watt_day_per_tonne'
        """
            
        """
        
        WattDayPerShortTon = 'watt_day_per_short_ton'
        """
            
        """
        
        WattHourPerPound = 'watt_hour_per_pound'
        """
            
        """
        
        BtuPerPound = 'btu_per_pound'
        """
            
        """
        
        KiloJoulePerKilogram = 'kilo_joule_per_kilogram'
        """
            
        """
        
        MegaJoulePerKilogram = 'mega_joule_per_kilogram'
        """
            
        """
        
        KiloCaloriePerGram = 'kilo_calorie_per_gram'
        """
            
        """
        
        KiloWattHourPerKilogram = 'kilo_watt_hour_per_kilogram'
        """
            
        """
        
        MegaWattHourPerKilogram = 'mega_watt_hour_per_kilogram'
        """
            
        """
        
        GigaWattHourPerKilogram = 'giga_watt_hour_per_kilogram'
        """
            
        """
        
        KiloWattDayPerKilogram = 'kilo_watt_day_per_kilogram'
        """
            
        """
        
        MegaWattDayPerKilogram = 'mega_watt_day_per_kilogram'
        """
            
        """
        
        GigaWattDayPerKilogram = 'giga_watt_day_per_kilogram'
        """
            
        """
        
        TeraWattDayPerKilogram = 'tera_watt_day_per_kilogram'
        """
            
        """
        
        KiloWattDayPerTonne = 'kilo_watt_day_per_tonne'
        """
            
        """
        
        MegaWattDayPerTonne = 'mega_watt_day_per_tonne'
        """
            
        """
        
        GigaWattDayPerTonne = 'giga_watt_day_per_tonne'
        """
            
        """
        
        TeraWattDayPerTonne = 'tera_watt_day_per_tonne'
        """
            
        """
        
        KiloWattDayPerShortTon = 'kilo_watt_day_per_short_ton'
        """
            
        """
        
        MegaWattDayPerShortTon = 'mega_watt_day_per_short_ton'
        """
            
        """
        
        GigaWattDayPerShortTon = 'giga_watt_day_per_short_ton'
        """
            
        """
        
        TeraWattDayPerShortTon = 'tera_watt_day_per_short_ton'
        """
            
        """
        
        KiloWattHourPerPound = 'kilo_watt_hour_per_pound'
        """
            
        """
        
        MegaWattHourPerPound = 'mega_watt_hour_per_pound'
        """
            
        """
        
        GigaWattHourPerPound = 'giga_watt_hour_per_pound'
        """
            
        """
        

class SpecificEnergy:
    """
    The SpecificEnergy

    Args:
        value (float): The value.
        from_unit (SpecificEnergyUnits): The SpecificEnergy unit to create from, The default unit is JoulePerKilogram
    """
    def __init__(self, value: float, from_unit: SpecificEnergyUnits = SpecificEnergyUnits.JoulePerKilogram):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__joules_per_kilogram = None
        
        self.__mega_joules_per_tonne = None
        
        self.__calories_per_gram = None
        
        self.__watt_hours_per_kilogram = None
        
        self.__watt_days_per_kilogram = None
        
        self.__watt_days_per_tonne = None
        
        self.__watt_days_per_short_ton = None
        
        self.__watt_hours_per_pound = None
        
        self.__btu_per_pound = None
        
        self.__kilo_joules_per_kilogram = None
        
        self.__mega_joules_per_kilogram = None
        
        self.__kilo_calories_per_gram = None
        
        self.__kilo_watt_hours_per_kilogram = None
        
        self.__mega_watt_hours_per_kilogram = None
        
        self.__giga_watt_hours_per_kilogram = None
        
        self.__kilo_watt_days_per_kilogram = None
        
        self.__mega_watt_days_per_kilogram = None
        
        self.__giga_watt_days_per_kilogram = None
        
        self.__tera_watt_days_per_kilogram = None
        
        self.__kilo_watt_days_per_tonne = None
        
        self.__mega_watt_days_per_tonne = None
        
        self.__giga_watt_days_per_tonne = None
        
        self.__tera_watt_days_per_tonne = None
        
        self.__kilo_watt_days_per_short_ton = None
        
        self.__mega_watt_days_per_short_ton = None
        
        self.__giga_watt_days_per_short_ton = None
        
        self.__tera_watt_days_per_short_ton = None
        
        self.__kilo_watt_hours_per_pound = None
        
        self.__mega_watt_hours_per_pound = None
        
        self.__giga_watt_hours_per_pound = None
        

    def __convert_from_base(self, from_unit: SpecificEnergyUnits) -> float:
        value = self.__value
        
        if from_unit == SpecificEnergyUnits.JoulePerKilogram:
            return (value)
        
        if from_unit == SpecificEnergyUnits.MegaJoulePerTonne:
            return (value / 1e3)
        
        if from_unit == SpecificEnergyUnits.CaloriePerGram:
            return (value / 4.184e3)
        
        if from_unit == SpecificEnergyUnits.WattHourPerKilogram:
            return (value / 3.6e3)
        
        if from_unit == SpecificEnergyUnits.WattDayPerKilogram:
            return (value / (24 * 3.6e3))
        
        if from_unit == SpecificEnergyUnits.WattDayPerTonne:
            return (value / ((24 * 3.6e3) / 1e3))
        
        if from_unit == SpecificEnergyUnits.WattDayPerShortTon:
            return (value / ((24 * 3.6e3) / 9.0718474e2))
        
        if from_unit == SpecificEnergyUnits.WattHourPerPound:
            return (value / 7.93664e3)
        
        if from_unit == SpecificEnergyUnits.BtuPerPound:
            return (value / 2326.000075362)
        
        if from_unit == SpecificEnergyUnits.KiloJoulePerKilogram:
            return ((value) / 1000.0)
        
        if from_unit == SpecificEnergyUnits.MegaJoulePerKilogram:
            return ((value) / 1000000.0)
        
        if from_unit == SpecificEnergyUnits.KiloCaloriePerGram:
            return ((value / 4.184e3) / 1000.0)
        
        if from_unit == SpecificEnergyUnits.KiloWattHourPerKilogram:
            return ((value / 3.6e3) / 1000.0)
        
        if from_unit == SpecificEnergyUnits.MegaWattHourPerKilogram:
            return ((value / 3.6e3) / 1000000.0)
        
        if from_unit == SpecificEnergyUnits.GigaWattHourPerKilogram:
            return ((value / 3.6e3) / 1000000000.0)
        
        if from_unit == SpecificEnergyUnits.KiloWattDayPerKilogram:
            return ((value / (24 * 3.6e3)) / 1000.0)
        
        if from_unit == SpecificEnergyUnits.MegaWattDayPerKilogram:
            return ((value / (24 * 3.6e3)) / 1000000.0)
        
        if from_unit == SpecificEnergyUnits.GigaWattDayPerKilogram:
            return ((value / (24 * 3.6e3)) / 1000000000.0)
        
        if from_unit == SpecificEnergyUnits.TeraWattDayPerKilogram:
            return ((value / (24 * 3.6e3)) / 1000000000000.0)
        
        if from_unit == SpecificEnergyUnits.KiloWattDayPerTonne:
            return ((value / ((24 * 3.6e3) / 1e3)) / 1000.0)
        
        if from_unit == SpecificEnergyUnits.MegaWattDayPerTonne:
            return ((value / ((24 * 3.6e3) / 1e3)) / 1000000.0)
        
        if from_unit == SpecificEnergyUnits.GigaWattDayPerTonne:
            return ((value / ((24 * 3.6e3) / 1e3)) / 1000000000.0)
        
        if from_unit == SpecificEnergyUnits.TeraWattDayPerTonne:
            return ((value / ((24 * 3.6e3) / 1e3)) / 1000000000000.0)
        
        if from_unit == SpecificEnergyUnits.KiloWattDayPerShortTon:
            return ((value / ((24 * 3.6e3) / 9.0718474e2)) / 1000.0)
        
        if from_unit == SpecificEnergyUnits.MegaWattDayPerShortTon:
            return ((value / ((24 * 3.6e3) / 9.0718474e2)) / 1000000.0)
        
        if from_unit == SpecificEnergyUnits.GigaWattDayPerShortTon:
            return ((value / ((24 * 3.6e3) / 9.0718474e2)) / 1000000000.0)
        
        if from_unit == SpecificEnergyUnits.TeraWattDayPerShortTon:
            return ((value / ((24 * 3.6e3) / 9.0718474e2)) / 1000000000000.0)
        
        if from_unit == SpecificEnergyUnits.KiloWattHourPerPound:
            return ((value / 7.93664e3) / 1000.0)
        
        if from_unit == SpecificEnergyUnits.MegaWattHourPerPound:
            return ((value / 7.93664e3) / 1000000.0)
        
        if from_unit == SpecificEnergyUnits.GigaWattHourPerPound:
            return ((value / 7.93664e3) / 1000000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: SpecificEnergyUnits) -> float:
        
        if to_unit == SpecificEnergyUnits.JoulePerKilogram:
            return (value)
        
        if to_unit == SpecificEnergyUnits.MegaJoulePerTonne:
            return (value * 1e3)
        
        if to_unit == SpecificEnergyUnits.CaloriePerGram:
            return (value * 4.184e3)
        
        if to_unit == SpecificEnergyUnits.WattHourPerKilogram:
            return (value * 3.6e3)
        
        if to_unit == SpecificEnergyUnits.WattDayPerKilogram:
            return (value * (24 * 3.6e3))
        
        if to_unit == SpecificEnergyUnits.WattDayPerTonne:
            return (value * ((24 * 3.6e3) / 1e3))
        
        if to_unit == SpecificEnergyUnits.WattDayPerShortTon:
            return (value * ((24 * 3.6e3) / 9.0718474e2))
        
        if to_unit == SpecificEnergyUnits.WattHourPerPound:
            return (value * 7.93664e3)
        
        if to_unit == SpecificEnergyUnits.BtuPerPound:
            return (value * 2326.000075362)
        
        if to_unit == SpecificEnergyUnits.KiloJoulePerKilogram:
            return ((value) * 1000.0)
        
        if to_unit == SpecificEnergyUnits.MegaJoulePerKilogram:
            return ((value) * 1000000.0)
        
        if to_unit == SpecificEnergyUnits.KiloCaloriePerGram:
            return ((value * 4.184e3) * 1000.0)
        
        if to_unit == SpecificEnergyUnits.KiloWattHourPerKilogram:
            return ((value * 3.6e3) * 1000.0)
        
        if to_unit == SpecificEnergyUnits.MegaWattHourPerKilogram:
            return ((value * 3.6e3) * 1000000.0)
        
        if to_unit == SpecificEnergyUnits.GigaWattHourPerKilogram:
            return ((value * 3.6e3) * 1000000000.0)
        
        if to_unit == SpecificEnergyUnits.KiloWattDayPerKilogram:
            return ((value * (24 * 3.6e3)) * 1000.0)
        
        if to_unit == SpecificEnergyUnits.MegaWattDayPerKilogram:
            return ((value * (24 * 3.6e3)) * 1000000.0)
        
        if to_unit == SpecificEnergyUnits.GigaWattDayPerKilogram:
            return ((value * (24 * 3.6e3)) * 1000000000.0)
        
        if to_unit == SpecificEnergyUnits.TeraWattDayPerKilogram:
            return ((value * (24 * 3.6e3)) * 1000000000000.0)
        
        if to_unit == SpecificEnergyUnits.KiloWattDayPerTonne:
            return ((value * ((24 * 3.6e3) / 1e3)) * 1000.0)
        
        if to_unit == SpecificEnergyUnits.MegaWattDayPerTonne:
            return ((value * ((24 * 3.6e3) / 1e3)) * 1000000.0)
        
        if to_unit == SpecificEnergyUnits.GigaWattDayPerTonne:
            return ((value * ((24 * 3.6e3) / 1e3)) * 1000000000.0)
        
        if to_unit == SpecificEnergyUnits.TeraWattDayPerTonne:
            return ((value * ((24 * 3.6e3) / 1e3)) * 1000000000000.0)
        
        if to_unit == SpecificEnergyUnits.KiloWattDayPerShortTon:
            return ((value * ((24 * 3.6e3) / 9.0718474e2)) * 1000.0)
        
        if to_unit == SpecificEnergyUnits.MegaWattDayPerShortTon:
            return ((value * ((24 * 3.6e3) / 9.0718474e2)) * 1000000.0)
        
        if to_unit == SpecificEnergyUnits.GigaWattDayPerShortTon:
            return ((value * ((24 * 3.6e3) / 9.0718474e2)) * 1000000000.0)
        
        if to_unit == SpecificEnergyUnits.TeraWattDayPerShortTon:
            return ((value * ((24 * 3.6e3) / 9.0718474e2)) * 1000000000000.0)
        
        if to_unit == SpecificEnergyUnits.KiloWattHourPerPound:
            return ((value * 7.93664e3) * 1000.0)
        
        if to_unit == SpecificEnergyUnits.MegaWattHourPerPound:
            return ((value * 7.93664e3) * 1000000.0)
        
        if to_unit == SpecificEnergyUnits.GigaWattHourPerPound:
            return ((value * 7.93664e3) * 1000000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
    @staticmethod
    def from_joules_per_kilogram(joules_per_kilogram: float):
        """
        Create a new instance of SpecificEnergy from a value in joules_per_kilogram.

        

        :param meters: The SpecificEnergy value in joules_per_kilogram.
        :type joules_per_kilogram: float
        :return: A new instance of SpecificEnergy.
        :rtype: SpecificEnergy
        """
        return SpecificEnergy(joules_per_kilogram, SpecificEnergyUnits.JoulePerKilogram)

    
    @staticmethod
    def from_mega_joules_per_tonne(mega_joules_per_tonne: float):
        """
        Create a new instance of SpecificEnergy from a value in mega_joules_per_tonne.

        

        :param meters: The SpecificEnergy value in mega_joules_per_tonne.
        :type mega_joules_per_tonne: float
        :return: A new instance of SpecificEnergy.
        :rtype: SpecificEnergy
        """
        return SpecificEnergy(mega_joules_per_tonne, SpecificEnergyUnits.MegaJoulePerTonne)

    
    @staticmethod
    def from_calories_per_gram(calories_per_gram: float):
        """
        Create a new instance of SpecificEnergy from a value in calories_per_gram.

        

        :param meters: The SpecificEnergy value in calories_per_gram.
        :type calories_per_gram: float
        :return: A new instance of SpecificEnergy.
        :rtype: SpecificEnergy
        """
        return SpecificEnergy(calories_per_gram, SpecificEnergyUnits.CaloriePerGram)

    
    @staticmethod
    def from_watt_hours_per_kilogram(watt_hours_per_kilogram: float):
        """
        Create a new instance of SpecificEnergy from a value in watt_hours_per_kilogram.

        

        :param meters: The SpecificEnergy value in watt_hours_per_kilogram.
        :type watt_hours_per_kilogram: float
        :return: A new instance of SpecificEnergy.
        :rtype: SpecificEnergy
        """
        return SpecificEnergy(watt_hours_per_kilogram, SpecificEnergyUnits.WattHourPerKilogram)

    
    @staticmethod
    def from_watt_days_per_kilogram(watt_days_per_kilogram: float):
        """
        Create a new instance of SpecificEnergy from a value in watt_days_per_kilogram.

        

        :param meters: The SpecificEnergy value in watt_days_per_kilogram.
        :type watt_days_per_kilogram: float
        :return: A new instance of SpecificEnergy.
        :rtype: SpecificEnergy
        """
        return SpecificEnergy(watt_days_per_kilogram, SpecificEnergyUnits.WattDayPerKilogram)

    
    @staticmethod
    def from_watt_days_per_tonne(watt_days_per_tonne: float):
        """
        Create a new instance of SpecificEnergy from a value in watt_days_per_tonne.

        

        :param meters: The SpecificEnergy value in watt_days_per_tonne.
        :type watt_days_per_tonne: float
        :return: A new instance of SpecificEnergy.
        :rtype: SpecificEnergy
        """
        return SpecificEnergy(watt_days_per_tonne, SpecificEnergyUnits.WattDayPerTonne)

    
    @staticmethod
    def from_watt_days_per_short_ton(watt_days_per_short_ton: float):
        """
        Create a new instance of SpecificEnergy from a value in watt_days_per_short_ton.

        

        :param meters: The SpecificEnergy value in watt_days_per_short_ton.
        :type watt_days_per_short_ton: float
        :return: A new instance of SpecificEnergy.
        :rtype: SpecificEnergy
        """
        return SpecificEnergy(watt_days_per_short_ton, SpecificEnergyUnits.WattDayPerShortTon)

    
    @staticmethod
    def from_watt_hours_per_pound(watt_hours_per_pound: float):
        """
        Create a new instance of SpecificEnergy from a value in watt_hours_per_pound.

        

        :param meters: The SpecificEnergy value in watt_hours_per_pound.
        :type watt_hours_per_pound: float
        :return: A new instance of SpecificEnergy.
        :rtype: SpecificEnergy
        """
        return SpecificEnergy(watt_hours_per_pound, SpecificEnergyUnits.WattHourPerPound)

    
    @staticmethod
    def from_btu_per_pound(btu_per_pound: float):
        """
        Create a new instance of SpecificEnergy from a value in btu_per_pound.

        

        :param meters: The SpecificEnergy value in btu_per_pound.
        :type btu_per_pound: float
        :return: A new instance of SpecificEnergy.
        :rtype: SpecificEnergy
        """
        return SpecificEnergy(btu_per_pound, SpecificEnergyUnits.BtuPerPound)

    
    @staticmethod
    def from_kilo_joules_per_kilogram(kilo_joules_per_kilogram: float):
        """
        Create a new instance of SpecificEnergy from a value in kilo_joules_per_kilogram.

        

        :param meters: The SpecificEnergy value in kilo_joules_per_kilogram.
        :type kilo_joules_per_kilogram: float
        :return: A new instance of SpecificEnergy.
        :rtype: SpecificEnergy
        """
        return SpecificEnergy(kilo_joules_per_kilogram, SpecificEnergyUnits.KiloJoulePerKilogram)

    
    @staticmethod
    def from_mega_joules_per_kilogram(mega_joules_per_kilogram: float):
        """
        Create a new instance of SpecificEnergy from a value in mega_joules_per_kilogram.

        

        :param meters: The SpecificEnergy value in mega_joules_per_kilogram.
        :type mega_joules_per_kilogram: float
        :return: A new instance of SpecificEnergy.
        :rtype: SpecificEnergy
        """
        return SpecificEnergy(mega_joules_per_kilogram, SpecificEnergyUnits.MegaJoulePerKilogram)

    
    @staticmethod
    def from_kilo_calories_per_gram(kilo_calories_per_gram: float):
        """
        Create a new instance of SpecificEnergy from a value in kilo_calories_per_gram.

        

        :param meters: The SpecificEnergy value in kilo_calories_per_gram.
        :type kilo_calories_per_gram: float
        :return: A new instance of SpecificEnergy.
        :rtype: SpecificEnergy
        """
        return SpecificEnergy(kilo_calories_per_gram, SpecificEnergyUnits.KiloCaloriePerGram)

    
    @staticmethod
    def from_kilo_watt_hours_per_kilogram(kilo_watt_hours_per_kilogram: float):
        """
        Create a new instance of SpecificEnergy from a value in kilo_watt_hours_per_kilogram.

        

        :param meters: The SpecificEnergy value in kilo_watt_hours_per_kilogram.
        :type kilo_watt_hours_per_kilogram: float
        :return: A new instance of SpecificEnergy.
        :rtype: SpecificEnergy
        """
        return SpecificEnergy(kilo_watt_hours_per_kilogram, SpecificEnergyUnits.KiloWattHourPerKilogram)

    
    @staticmethod
    def from_mega_watt_hours_per_kilogram(mega_watt_hours_per_kilogram: float):
        """
        Create a new instance of SpecificEnergy from a value in mega_watt_hours_per_kilogram.

        

        :param meters: The SpecificEnergy value in mega_watt_hours_per_kilogram.
        :type mega_watt_hours_per_kilogram: float
        :return: A new instance of SpecificEnergy.
        :rtype: SpecificEnergy
        """
        return SpecificEnergy(mega_watt_hours_per_kilogram, SpecificEnergyUnits.MegaWattHourPerKilogram)

    
    @staticmethod
    def from_giga_watt_hours_per_kilogram(giga_watt_hours_per_kilogram: float):
        """
        Create a new instance of SpecificEnergy from a value in giga_watt_hours_per_kilogram.

        

        :param meters: The SpecificEnergy value in giga_watt_hours_per_kilogram.
        :type giga_watt_hours_per_kilogram: float
        :return: A new instance of SpecificEnergy.
        :rtype: SpecificEnergy
        """
        return SpecificEnergy(giga_watt_hours_per_kilogram, SpecificEnergyUnits.GigaWattHourPerKilogram)

    
    @staticmethod
    def from_kilo_watt_days_per_kilogram(kilo_watt_days_per_kilogram: float):
        """
        Create a new instance of SpecificEnergy from a value in kilo_watt_days_per_kilogram.

        

        :param meters: The SpecificEnergy value in kilo_watt_days_per_kilogram.
        :type kilo_watt_days_per_kilogram: float
        :return: A new instance of SpecificEnergy.
        :rtype: SpecificEnergy
        """
        return SpecificEnergy(kilo_watt_days_per_kilogram, SpecificEnergyUnits.KiloWattDayPerKilogram)

    
    @staticmethod
    def from_mega_watt_days_per_kilogram(mega_watt_days_per_kilogram: float):
        """
        Create a new instance of SpecificEnergy from a value in mega_watt_days_per_kilogram.

        

        :param meters: The SpecificEnergy value in mega_watt_days_per_kilogram.
        :type mega_watt_days_per_kilogram: float
        :return: A new instance of SpecificEnergy.
        :rtype: SpecificEnergy
        """
        return SpecificEnergy(mega_watt_days_per_kilogram, SpecificEnergyUnits.MegaWattDayPerKilogram)

    
    @staticmethod
    def from_giga_watt_days_per_kilogram(giga_watt_days_per_kilogram: float):
        """
        Create a new instance of SpecificEnergy from a value in giga_watt_days_per_kilogram.

        

        :param meters: The SpecificEnergy value in giga_watt_days_per_kilogram.
        :type giga_watt_days_per_kilogram: float
        :return: A new instance of SpecificEnergy.
        :rtype: SpecificEnergy
        """
        return SpecificEnergy(giga_watt_days_per_kilogram, SpecificEnergyUnits.GigaWattDayPerKilogram)

    
    @staticmethod
    def from_tera_watt_days_per_kilogram(tera_watt_days_per_kilogram: float):
        """
        Create a new instance of SpecificEnergy from a value in tera_watt_days_per_kilogram.

        

        :param meters: The SpecificEnergy value in tera_watt_days_per_kilogram.
        :type tera_watt_days_per_kilogram: float
        :return: A new instance of SpecificEnergy.
        :rtype: SpecificEnergy
        """
        return SpecificEnergy(tera_watt_days_per_kilogram, SpecificEnergyUnits.TeraWattDayPerKilogram)

    
    @staticmethod
    def from_kilo_watt_days_per_tonne(kilo_watt_days_per_tonne: float):
        """
        Create a new instance of SpecificEnergy from a value in kilo_watt_days_per_tonne.

        

        :param meters: The SpecificEnergy value in kilo_watt_days_per_tonne.
        :type kilo_watt_days_per_tonne: float
        :return: A new instance of SpecificEnergy.
        :rtype: SpecificEnergy
        """
        return SpecificEnergy(kilo_watt_days_per_tonne, SpecificEnergyUnits.KiloWattDayPerTonne)

    
    @staticmethod
    def from_mega_watt_days_per_tonne(mega_watt_days_per_tonne: float):
        """
        Create a new instance of SpecificEnergy from a value in mega_watt_days_per_tonne.

        

        :param meters: The SpecificEnergy value in mega_watt_days_per_tonne.
        :type mega_watt_days_per_tonne: float
        :return: A new instance of SpecificEnergy.
        :rtype: SpecificEnergy
        """
        return SpecificEnergy(mega_watt_days_per_tonne, SpecificEnergyUnits.MegaWattDayPerTonne)

    
    @staticmethod
    def from_giga_watt_days_per_tonne(giga_watt_days_per_tonne: float):
        """
        Create a new instance of SpecificEnergy from a value in giga_watt_days_per_tonne.

        

        :param meters: The SpecificEnergy value in giga_watt_days_per_tonne.
        :type giga_watt_days_per_tonne: float
        :return: A new instance of SpecificEnergy.
        :rtype: SpecificEnergy
        """
        return SpecificEnergy(giga_watt_days_per_tonne, SpecificEnergyUnits.GigaWattDayPerTonne)

    
    @staticmethod
    def from_tera_watt_days_per_tonne(tera_watt_days_per_tonne: float):
        """
        Create a new instance of SpecificEnergy from a value in tera_watt_days_per_tonne.

        

        :param meters: The SpecificEnergy value in tera_watt_days_per_tonne.
        :type tera_watt_days_per_tonne: float
        :return: A new instance of SpecificEnergy.
        :rtype: SpecificEnergy
        """
        return SpecificEnergy(tera_watt_days_per_tonne, SpecificEnergyUnits.TeraWattDayPerTonne)

    
    @staticmethod
    def from_kilo_watt_days_per_short_ton(kilo_watt_days_per_short_ton: float):
        """
        Create a new instance of SpecificEnergy from a value in kilo_watt_days_per_short_ton.

        

        :param meters: The SpecificEnergy value in kilo_watt_days_per_short_ton.
        :type kilo_watt_days_per_short_ton: float
        :return: A new instance of SpecificEnergy.
        :rtype: SpecificEnergy
        """
        return SpecificEnergy(kilo_watt_days_per_short_ton, SpecificEnergyUnits.KiloWattDayPerShortTon)

    
    @staticmethod
    def from_mega_watt_days_per_short_ton(mega_watt_days_per_short_ton: float):
        """
        Create a new instance of SpecificEnergy from a value in mega_watt_days_per_short_ton.

        

        :param meters: The SpecificEnergy value in mega_watt_days_per_short_ton.
        :type mega_watt_days_per_short_ton: float
        :return: A new instance of SpecificEnergy.
        :rtype: SpecificEnergy
        """
        return SpecificEnergy(mega_watt_days_per_short_ton, SpecificEnergyUnits.MegaWattDayPerShortTon)

    
    @staticmethod
    def from_giga_watt_days_per_short_ton(giga_watt_days_per_short_ton: float):
        """
        Create a new instance of SpecificEnergy from a value in giga_watt_days_per_short_ton.

        

        :param meters: The SpecificEnergy value in giga_watt_days_per_short_ton.
        :type giga_watt_days_per_short_ton: float
        :return: A new instance of SpecificEnergy.
        :rtype: SpecificEnergy
        """
        return SpecificEnergy(giga_watt_days_per_short_ton, SpecificEnergyUnits.GigaWattDayPerShortTon)

    
    @staticmethod
    def from_tera_watt_days_per_short_ton(tera_watt_days_per_short_ton: float):
        """
        Create a new instance of SpecificEnergy from a value in tera_watt_days_per_short_ton.

        

        :param meters: The SpecificEnergy value in tera_watt_days_per_short_ton.
        :type tera_watt_days_per_short_ton: float
        :return: A new instance of SpecificEnergy.
        :rtype: SpecificEnergy
        """
        return SpecificEnergy(tera_watt_days_per_short_ton, SpecificEnergyUnits.TeraWattDayPerShortTon)

    
    @staticmethod
    def from_kilo_watt_hours_per_pound(kilo_watt_hours_per_pound: float):
        """
        Create a new instance of SpecificEnergy from a value in kilo_watt_hours_per_pound.

        

        :param meters: The SpecificEnergy value in kilo_watt_hours_per_pound.
        :type kilo_watt_hours_per_pound: float
        :return: A new instance of SpecificEnergy.
        :rtype: SpecificEnergy
        """
        return SpecificEnergy(kilo_watt_hours_per_pound, SpecificEnergyUnits.KiloWattHourPerPound)

    
    @staticmethod
    def from_mega_watt_hours_per_pound(mega_watt_hours_per_pound: float):
        """
        Create a new instance of SpecificEnergy from a value in mega_watt_hours_per_pound.

        

        :param meters: The SpecificEnergy value in mega_watt_hours_per_pound.
        :type mega_watt_hours_per_pound: float
        :return: A new instance of SpecificEnergy.
        :rtype: SpecificEnergy
        """
        return SpecificEnergy(mega_watt_hours_per_pound, SpecificEnergyUnits.MegaWattHourPerPound)

    
    @staticmethod
    def from_giga_watt_hours_per_pound(giga_watt_hours_per_pound: float):
        """
        Create a new instance of SpecificEnergy from a value in giga_watt_hours_per_pound.

        

        :param meters: The SpecificEnergy value in giga_watt_hours_per_pound.
        :type giga_watt_hours_per_pound: float
        :return: A new instance of SpecificEnergy.
        :rtype: SpecificEnergy
        """
        return SpecificEnergy(giga_watt_hours_per_pound, SpecificEnergyUnits.GigaWattHourPerPound)

    
    @property
    def joules_per_kilogram(self) -> float:
        """
        
        """
        if self.__joules_per_kilogram != None:
            return self.__joules_per_kilogram
        self.__joules_per_kilogram = self.__convert_from_base(SpecificEnergyUnits.JoulePerKilogram)
        return self.__joules_per_kilogram

    
    @property
    def mega_joules_per_tonne(self) -> float:
        """
        
        """
        if self.__mega_joules_per_tonne != None:
            return self.__mega_joules_per_tonne
        self.__mega_joules_per_tonne = self.__convert_from_base(SpecificEnergyUnits.MegaJoulePerTonne)
        return self.__mega_joules_per_tonne

    
    @property
    def calories_per_gram(self) -> float:
        """
        
        """
        if self.__calories_per_gram != None:
            return self.__calories_per_gram
        self.__calories_per_gram = self.__convert_from_base(SpecificEnergyUnits.CaloriePerGram)
        return self.__calories_per_gram

    
    @property
    def watt_hours_per_kilogram(self) -> float:
        """
        
        """
        if self.__watt_hours_per_kilogram != None:
            return self.__watt_hours_per_kilogram
        self.__watt_hours_per_kilogram = self.__convert_from_base(SpecificEnergyUnits.WattHourPerKilogram)
        return self.__watt_hours_per_kilogram

    
    @property
    def watt_days_per_kilogram(self) -> float:
        """
        
        """
        if self.__watt_days_per_kilogram != None:
            return self.__watt_days_per_kilogram
        self.__watt_days_per_kilogram = self.__convert_from_base(SpecificEnergyUnits.WattDayPerKilogram)
        return self.__watt_days_per_kilogram

    
    @property
    def watt_days_per_tonne(self) -> float:
        """
        
        """
        if self.__watt_days_per_tonne != None:
            return self.__watt_days_per_tonne
        self.__watt_days_per_tonne = self.__convert_from_base(SpecificEnergyUnits.WattDayPerTonne)
        return self.__watt_days_per_tonne

    
    @property
    def watt_days_per_short_ton(self) -> float:
        """
        
        """
        if self.__watt_days_per_short_ton != None:
            return self.__watt_days_per_short_ton
        self.__watt_days_per_short_ton = self.__convert_from_base(SpecificEnergyUnits.WattDayPerShortTon)
        return self.__watt_days_per_short_ton

    
    @property
    def watt_hours_per_pound(self) -> float:
        """
        
        """
        if self.__watt_hours_per_pound != None:
            return self.__watt_hours_per_pound
        self.__watt_hours_per_pound = self.__convert_from_base(SpecificEnergyUnits.WattHourPerPound)
        return self.__watt_hours_per_pound

    
    @property
    def btu_per_pound(self) -> float:
        """
        
        """
        if self.__btu_per_pound != None:
            return self.__btu_per_pound
        self.__btu_per_pound = self.__convert_from_base(SpecificEnergyUnits.BtuPerPound)
        return self.__btu_per_pound

    
    @property
    def kilo_joules_per_kilogram(self) -> float:
        """
        
        """
        if self.__kilo_joules_per_kilogram != None:
            return self.__kilo_joules_per_kilogram
        self.__kilo_joules_per_kilogram = self.__convert_from_base(SpecificEnergyUnits.KiloJoulePerKilogram)
        return self.__kilo_joules_per_kilogram

    
    @property
    def mega_joules_per_kilogram(self) -> float:
        """
        
        """
        if self.__mega_joules_per_kilogram != None:
            return self.__mega_joules_per_kilogram
        self.__mega_joules_per_kilogram = self.__convert_from_base(SpecificEnergyUnits.MegaJoulePerKilogram)
        return self.__mega_joules_per_kilogram

    
    @property
    def kilo_calories_per_gram(self) -> float:
        """
        
        """
        if self.__kilo_calories_per_gram != None:
            return self.__kilo_calories_per_gram
        self.__kilo_calories_per_gram = self.__convert_from_base(SpecificEnergyUnits.KiloCaloriePerGram)
        return self.__kilo_calories_per_gram

    
    @property
    def kilo_watt_hours_per_kilogram(self) -> float:
        """
        
        """
        if self.__kilo_watt_hours_per_kilogram != None:
            return self.__kilo_watt_hours_per_kilogram
        self.__kilo_watt_hours_per_kilogram = self.__convert_from_base(SpecificEnergyUnits.KiloWattHourPerKilogram)
        return self.__kilo_watt_hours_per_kilogram

    
    @property
    def mega_watt_hours_per_kilogram(self) -> float:
        """
        
        """
        if self.__mega_watt_hours_per_kilogram != None:
            return self.__mega_watt_hours_per_kilogram
        self.__mega_watt_hours_per_kilogram = self.__convert_from_base(SpecificEnergyUnits.MegaWattHourPerKilogram)
        return self.__mega_watt_hours_per_kilogram

    
    @property
    def giga_watt_hours_per_kilogram(self) -> float:
        """
        
        """
        if self.__giga_watt_hours_per_kilogram != None:
            return self.__giga_watt_hours_per_kilogram
        self.__giga_watt_hours_per_kilogram = self.__convert_from_base(SpecificEnergyUnits.GigaWattHourPerKilogram)
        return self.__giga_watt_hours_per_kilogram

    
    @property
    def kilo_watt_days_per_kilogram(self) -> float:
        """
        
        """
        if self.__kilo_watt_days_per_kilogram != None:
            return self.__kilo_watt_days_per_kilogram
        self.__kilo_watt_days_per_kilogram = self.__convert_from_base(SpecificEnergyUnits.KiloWattDayPerKilogram)
        return self.__kilo_watt_days_per_kilogram

    
    @property
    def mega_watt_days_per_kilogram(self) -> float:
        """
        
        """
        if self.__mega_watt_days_per_kilogram != None:
            return self.__mega_watt_days_per_kilogram
        self.__mega_watt_days_per_kilogram = self.__convert_from_base(SpecificEnergyUnits.MegaWattDayPerKilogram)
        return self.__mega_watt_days_per_kilogram

    
    @property
    def giga_watt_days_per_kilogram(self) -> float:
        """
        
        """
        if self.__giga_watt_days_per_kilogram != None:
            return self.__giga_watt_days_per_kilogram
        self.__giga_watt_days_per_kilogram = self.__convert_from_base(SpecificEnergyUnits.GigaWattDayPerKilogram)
        return self.__giga_watt_days_per_kilogram

    
    @property
    def tera_watt_days_per_kilogram(self) -> float:
        """
        
        """
        if self.__tera_watt_days_per_kilogram != None:
            return self.__tera_watt_days_per_kilogram
        self.__tera_watt_days_per_kilogram = self.__convert_from_base(SpecificEnergyUnits.TeraWattDayPerKilogram)
        return self.__tera_watt_days_per_kilogram

    
    @property
    def kilo_watt_days_per_tonne(self) -> float:
        """
        
        """
        if self.__kilo_watt_days_per_tonne != None:
            return self.__kilo_watt_days_per_tonne
        self.__kilo_watt_days_per_tonne = self.__convert_from_base(SpecificEnergyUnits.KiloWattDayPerTonne)
        return self.__kilo_watt_days_per_tonne

    
    @property
    def mega_watt_days_per_tonne(self) -> float:
        """
        
        """
        if self.__mega_watt_days_per_tonne != None:
            return self.__mega_watt_days_per_tonne
        self.__mega_watt_days_per_tonne = self.__convert_from_base(SpecificEnergyUnits.MegaWattDayPerTonne)
        return self.__mega_watt_days_per_tonne

    
    @property
    def giga_watt_days_per_tonne(self) -> float:
        """
        
        """
        if self.__giga_watt_days_per_tonne != None:
            return self.__giga_watt_days_per_tonne
        self.__giga_watt_days_per_tonne = self.__convert_from_base(SpecificEnergyUnits.GigaWattDayPerTonne)
        return self.__giga_watt_days_per_tonne

    
    @property
    def tera_watt_days_per_tonne(self) -> float:
        """
        
        """
        if self.__tera_watt_days_per_tonne != None:
            return self.__tera_watt_days_per_tonne
        self.__tera_watt_days_per_tonne = self.__convert_from_base(SpecificEnergyUnits.TeraWattDayPerTonne)
        return self.__tera_watt_days_per_tonne

    
    @property
    def kilo_watt_days_per_short_ton(self) -> float:
        """
        
        """
        if self.__kilo_watt_days_per_short_ton != None:
            return self.__kilo_watt_days_per_short_ton
        self.__kilo_watt_days_per_short_ton = self.__convert_from_base(SpecificEnergyUnits.KiloWattDayPerShortTon)
        return self.__kilo_watt_days_per_short_ton

    
    @property
    def mega_watt_days_per_short_ton(self) -> float:
        """
        
        """
        if self.__mega_watt_days_per_short_ton != None:
            return self.__mega_watt_days_per_short_ton
        self.__mega_watt_days_per_short_ton = self.__convert_from_base(SpecificEnergyUnits.MegaWattDayPerShortTon)
        return self.__mega_watt_days_per_short_ton

    
    @property
    def giga_watt_days_per_short_ton(self) -> float:
        """
        
        """
        if self.__giga_watt_days_per_short_ton != None:
            return self.__giga_watt_days_per_short_ton
        self.__giga_watt_days_per_short_ton = self.__convert_from_base(SpecificEnergyUnits.GigaWattDayPerShortTon)
        return self.__giga_watt_days_per_short_ton

    
    @property
    def tera_watt_days_per_short_ton(self) -> float:
        """
        
        """
        if self.__tera_watt_days_per_short_ton != None:
            return self.__tera_watt_days_per_short_ton
        self.__tera_watt_days_per_short_ton = self.__convert_from_base(SpecificEnergyUnits.TeraWattDayPerShortTon)
        return self.__tera_watt_days_per_short_ton

    
    @property
    def kilo_watt_hours_per_pound(self) -> float:
        """
        
        """
        if self.__kilo_watt_hours_per_pound != None:
            return self.__kilo_watt_hours_per_pound
        self.__kilo_watt_hours_per_pound = self.__convert_from_base(SpecificEnergyUnits.KiloWattHourPerPound)
        return self.__kilo_watt_hours_per_pound

    
    @property
    def mega_watt_hours_per_pound(self) -> float:
        """
        
        """
        if self.__mega_watt_hours_per_pound != None:
            return self.__mega_watt_hours_per_pound
        self.__mega_watt_hours_per_pound = self.__convert_from_base(SpecificEnergyUnits.MegaWattHourPerPound)
        return self.__mega_watt_hours_per_pound

    
    @property
    def giga_watt_hours_per_pound(self) -> float:
        """
        
        """
        if self.__giga_watt_hours_per_pound != None:
            return self.__giga_watt_hours_per_pound
        self.__giga_watt_hours_per_pound = self.__convert_from_base(SpecificEnergyUnits.GigaWattHourPerPound)
        return self.__giga_watt_hours_per_pound

    
    def to_string(self, unit: SpecificEnergyUnits = SpecificEnergyUnits.JoulePerKilogram) -> string:
        """
        Format the SpecificEnergy to string.
        Note! the default format for SpecificEnergy is JoulePerKilogram.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == SpecificEnergyUnits.JoulePerKilogram:
            return f"""{self.joules_per_kilogram} J/kg"""
        
        if unit == SpecificEnergyUnits.MegaJoulePerTonne:
            return f"""{self.mega_joules_per_tonne} MJ/t"""
        
        if unit == SpecificEnergyUnits.CaloriePerGram:
            return f"""{self.calories_per_gram} cal/g"""
        
        if unit == SpecificEnergyUnits.WattHourPerKilogram:
            return f"""{self.watt_hours_per_kilogram} Wh/kg"""
        
        if unit == SpecificEnergyUnits.WattDayPerKilogram:
            return f"""{self.watt_days_per_kilogram} Wd/kg"""
        
        if unit == SpecificEnergyUnits.WattDayPerTonne:
            return f"""{self.watt_days_per_tonne} Wd/t"""
        
        if unit == SpecificEnergyUnits.WattDayPerShortTon:
            return f"""{self.watt_days_per_short_ton} Wd/ST"""
        
        if unit == SpecificEnergyUnits.WattHourPerPound:
            return f"""{self.watt_hours_per_pound} Wh/lbs"""
        
        if unit == SpecificEnergyUnits.BtuPerPound:
            return f"""{self.btu_per_pound} btu/lb"""
        
        if unit == SpecificEnergyUnits.KiloJoulePerKilogram:
            return f"""{self.kilo_joules_per_kilogram} """
        
        if unit == SpecificEnergyUnits.MegaJoulePerKilogram:
            return f"""{self.mega_joules_per_kilogram} """
        
        if unit == SpecificEnergyUnits.KiloCaloriePerGram:
            return f"""{self.kilo_calories_per_gram} """
        
        if unit == SpecificEnergyUnits.KiloWattHourPerKilogram:
            return f"""{self.kilo_watt_hours_per_kilogram} """
        
        if unit == SpecificEnergyUnits.MegaWattHourPerKilogram:
            return f"""{self.mega_watt_hours_per_kilogram} """
        
        if unit == SpecificEnergyUnits.GigaWattHourPerKilogram:
            return f"""{self.giga_watt_hours_per_kilogram} """
        
        if unit == SpecificEnergyUnits.KiloWattDayPerKilogram:
            return f"""{self.kilo_watt_days_per_kilogram} """
        
        if unit == SpecificEnergyUnits.MegaWattDayPerKilogram:
            return f"""{self.mega_watt_days_per_kilogram} """
        
        if unit == SpecificEnergyUnits.GigaWattDayPerKilogram:
            return f"""{self.giga_watt_days_per_kilogram} """
        
        if unit == SpecificEnergyUnits.TeraWattDayPerKilogram:
            return f"""{self.tera_watt_days_per_kilogram} """
        
        if unit == SpecificEnergyUnits.KiloWattDayPerTonne:
            return f"""{self.kilo_watt_days_per_tonne} """
        
        if unit == SpecificEnergyUnits.MegaWattDayPerTonne:
            return f"""{self.mega_watt_days_per_tonne} """
        
        if unit == SpecificEnergyUnits.GigaWattDayPerTonne:
            return f"""{self.giga_watt_days_per_tonne} """
        
        if unit == SpecificEnergyUnits.TeraWattDayPerTonne:
            return f"""{self.tera_watt_days_per_tonne} """
        
        if unit == SpecificEnergyUnits.KiloWattDayPerShortTon:
            return f"""{self.kilo_watt_days_per_short_ton} """
        
        if unit == SpecificEnergyUnits.MegaWattDayPerShortTon:
            return f"""{self.mega_watt_days_per_short_ton} """
        
        if unit == SpecificEnergyUnits.GigaWattDayPerShortTon:
            return f"""{self.giga_watt_days_per_short_ton} """
        
        if unit == SpecificEnergyUnits.TeraWattDayPerShortTon:
            return f"""{self.tera_watt_days_per_short_ton} """
        
        if unit == SpecificEnergyUnits.KiloWattHourPerPound:
            return f"""{self.kilo_watt_hours_per_pound} """
        
        if unit == SpecificEnergyUnits.MegaWattHourPerPound:
            return f"""{self.mega_watt_hours_per_pound} """
        
        if unit == SpecificEnergyUnits.GigaWattHourPerPound:
            return f"""{self.giga_watt_hours_per_pound} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: SpecificEnergyUnits = SpecificEnergyUnits.JoulePerKilogram) -> string:
        """
        Get SpecificEnergy unit abbreviation.
        Note! the default abbreviation for SpecificEnergy is JoulePerKilogram.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == SpecificEnergyUnits.JoulePerKilogram:
            return """J/kg"""
        
        if unit_abbreviation == SpecificEnergyUnits.MegaJoulePerTonne:
            return """MJ/t"""
        
        if unit_abbreviation == SpecificEnergyUnits.CaloriePerGram:
            return """cal/g"""
        
        if unit_abbreviation == SpecificEnergyUnits.WattHourPerKilogram:
            return """Wh/kg"""
        
        if unit_abbreviation == SpecificEnergyUnits.WattDayPerKilogram:
            return """Wd/kg"""
        
        if unit_abbreviation == SpecificEnergyUnits.WattDayPerTonne:
            return """Wd/t"""
        
        if unit_abbreviation == SpecificEnergyUnits.WattDayPerShortTon:
            return """Wd/ST"""
        
        if unit_abbreviation == SpecificEnergyUnits.WattHourPerPound:
            return """Wh/lbs"""
        
        if unit_abbreviation == SpecificEnergyUnits.BtuPerPound:
            return """btu/lb"""
        
        if unit_abbreviation == SpecificEnergyUnits.KiloJoulePerKilogram:
            return """"""
        
        if unit_abbreviation == SpecificEnergyUnits.MegaJoulePerKilogram:
            return """"""
        
        if unit_abbreviation == SpecificEnergyUnits.KiloCaloriePerGram:
            return """"""
        
        if unit_abbreviation == SpecificEnergyUnits.KiloWattHourPerKilogram:
            return """"""
        
        if unit_abbreviation == SpecificEnergyUnits.MegaWattHourPerKilogram:
            return """"""
        
        if unit_abbreviation == SpecificEnergyUnits.GigaWattHourPerKilogram:
            return """"""
        
        if unit_abbreviation == SpecificEnergyUnits.KiloWattDayPerKilogram:
            return """"""
        
        if unit_abbreviation == SpecificEnergyUnits.MegaWattDayPerKilogram:
            return """"""
        
        if unit_abbreviation == SpecificEnergyUnits.GigaWattDayPerKilogram:
            return """"""
        
        if unit_abbreviation == SpecificEnergyUnits.TeraWattDayPerKilogram:
            return """"""
        
        if unit_abbreviation == SpecificEnergyUnits.KiloWattDayPerTonne:
            return """"""
        
        if unit_abbreviation == SpecificEnergyUnits.MegaWattDayPerTonne:
            return """"""
        
        if unit_abbreviation == SpecificEnergyUnits.GigaWattDayPerTonne:
            return """"""
        
        if unit_abbreviation == SpecificEnergyUnits.TeraWattDayPerTonne:
            return """"""
        
        if unit_abbreviation == SpecificEnergyUnits.KiloWattDayPerShortTon:
            return """"""
        
        if unit_abbreviation == SpecificEnergyUnits.MegaWattDayPerShortTon:
            return """"""
        
        if unit_abbreviation == SpecificEnergyUnits.GigaWattDayPerShortTon:
            return """"""
        
        if unit_abbreviation == SpecificEnergyUnits.TeraWattDayPerShortTon:
            return """"""
        
        if unit_abbreviation == SpecificEnergyUnits.KiloWattHourPerPound:
            return """"""
        
        if unit_abbreviation == SpecificEnergyUnits.MegaWattHourPerPound:
            return """"""
        
        if unit_abbreviation == SpecificEnergyUnits.GigaWattHourPerPound:
            return """"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, SpecificEnergy):
            raise TypeError("unsupported operand type(s) for +: 'SpecificEnergy' and '{}'".format(type(other).__name__))
        return SpecificEnergy(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, SpecificEnergy):
            raise TypeError("unsupported operand type(s) for *: 'SpecificEnergy' and '{}'".format(type(other).__name__))
        return SpecificEnergy(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, SpecificEnergy):
            raise TypeError("unsupported operand type(s) for -: 'SpecificEnergy' and '{}'".format(type(other).__name__))
        return SpecificEnergy(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, SpecificEnergy):
            raise TypeError("unsupported operand type(s) for /: 'SpecificEnergy' and '{}'".format(type(other).__name__))
        return SpecificEnergy(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, SpecificEnergy):
            raise TypeError("unsupported operand type(s) for %: 'SpecificEnergy' and '{}'".format(type(other).__name__))
        return SpecificEnergy(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, SpecificEnergy):
            raise TypeError("unsupported operand type(s) for **: 'SpecificEnergy' and '{}'".format(type(other).__name__))
        return SpecificEnergy(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, SpecificEnergy):
            raise TypeError("unsupported operand type(s) for ==: 'SpecificEnergy' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, SpecificEnergy):
            raise TypeError("unsupported operand type(s) for <: 'SpecificEnergy' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, SpecificEnergy):
            raise TypeError("unsupported operand type(s) for >: 'SpecificEnergy' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, SpecificEnergy):
            raise TypeError("unsupported operand type(s) for <=: 'SpecificEnergy' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, SpecificEnergy):
            raise TypeError("unsupported operand type(s) for >=: 'SpecificEnergy' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value
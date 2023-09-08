from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



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
        
        KilojoulePerKilogram = 'kilojoule_per_kilogram'
        """
            
        """
        
        MegajoulePerKilogram = 'megajoule_per_kilogram'
        """
            
        """
        
        KilocaloriePerGram = 'kilocalorie_per_gram'
        """
            
        """
        
        KilowattHourPerKilogram = 'kilowatt_hour_per_kilogram'
        """
            
        """
        
        MegawattHourPerKilogram = 'megawatt_hour_per_kilogram'
        """
            
        """
        
        GigawattHourPerKilogram = 'gigawatt_hour_per_kilogram'
        """
            
        """
        
        KilowattDayPerKilogram = 'kilowatt_day_per_kilogram'
        """
            
        """
        
        MegawattDayPerKilogram = 'megawatt_day_per_kilogram'
        """
            
        """
        
        GigawattDayPerKilogram = 'gigawatt_day_per_kilogram'
        """
            
        """
        
        TerawattDayPerKilogram = 'terawatt_day_per_kilogram'
        """
            
        """
        
        KilowattDayPerTonne = 'kilowatt_day_per_tonne'
        """
            
        """
        
        MegawattDayPerTonne = 'megawatt_day_per_tonne'
        """
            
        """
        
        GigawattDayPerTonne = 'gigawatt_day_per_tonne'
        """
            
        """
        
        TerawattDayPerTonne = 'terawatt_day_per_tonne'
        """
            
        """
        
        KilowattDayPerShortTon = 'kilowatt_day_per_short_ton'
        """
            
        """
        
        MegawattDayPerShortTon = 'megawatt_day_per_short_ton'
        """
            
        """
        
        GigawattDayPerShortTon = 'gigawatt_day_per_short_ton'
        """
            
        """
        
        TerawattDayPerShortTon = 'terawatt_day_per_short_ton'
        """
            
        """
        
        KilowattHourPerPound = 'kilowatt_hour_per_pound'
        """
            
        """
        
        MegawattHourPerPound = 'megawatt_hour_per_pound'
        """
            
        """
        
        GigawattHourPerPound = 'gigawatt_hour_per_pound'
        """
            
        """
        

class SpecificEnergy(AbstractMeasure):
    """
    The SpecificEnergy

    Args:
        value (float): The value.
        from_unit (SpecificEnergyUnits): The SpecificEnergy unit to create from, The default unit is JoulePerKilogram
    """
    def __init__(self, value: float, from_unit: SpecificEnergyUnits = SpecificEnergyUnits.JoulePerKilogram):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__joules_per_kilogram = None
        
        self.__mega_joules_per_tonne = None
        
        self.__calories_per_gram = None
        
        self.__watt_hours_per_kilogram = None
        
        self.__watt_days_per_kilogram = None
        
        self.__watt_days_per_tonne = None
        
        self.__watt_days_per_short_ton = None
        
        self.__watt_hours_per_pound = None
        
        self.__btu_per_pound = None
        
        self.__kilojoules_per_kilogram = None
        
        self.__megajoules_per_kilogram = None
        
        self.__kilocalories_per_gram = None
        
        self.__kilowatt_hours_per_kilogram = None
        
        self.__megawatt_hours_per_kilogram = None
        
        self.__gigawatt_hours_per_kilogram = None
        
        self.__kilowatt_days_per_kilogram = None
        
        self.__megawatt_days_per_kilogram = None
        
        self.__gigawatt_days_per_kilogram = None
        
        self.__terawatt_days_per_kilogram = None
        
        self.__kilowatt_days_per_tonne = None
        
        self.__megawatt_days_per_tonne = None
        
        self.__gigawatt_days_per_tonne = None
        
        self.__terawatt_days_per_tonne = None
        
        self.__kilowatt_days_per_short_ton = None
        
        self.__megawatt_days_per_short_ton = None
        
        self.__gigawatt_days_per_short_ton = None
        
        self.__terawatt_days_per_short_ton = None
        
        self.__kilowatt_hours_per_pound = None
        
        self.__megawatt_hours_per_pound = None
        
        self.__gigawatt_hours_per_pound = None
        

    def convert(self, unit: SpecificEnergyUnits) -> float:
        return self.__convert_from_base(unit)

    def __convert_from_base(self, from_unit: SpecificEnergyUnits) -> float:
        value = self._value
        
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
        
        if from_unit == SpecificEnergyUnits.KilojoulePerKilogram:
            return ((value) / 1000.0)
        
        if from_unit == SpecificEnergyUnits.MegajoulePerKilogram:
            return ((value) / 1000000.0)
        
        if from_unit == SpecificEnergyUnits.KilocaloriePerGram:
            return ((value / 4.184e3) / 1000.0)
        
        if from_unit == SpecificEnergyUnits.KilowattHourPerKilogram:
            return ((value / 3.6e3) / 1000.0)
        
        if from_unit == SpecificEnergyUnits.MegawattHourPerKilogram:
            return ((value / 3.6e3) / 1000000.0)
        
        if from_unit == SpecificEnergyUnits.GigawattHourPerKilogram:
            return ((value / 3.6e3) / 1000000000.0)
        
        if from_unit == SpecificEnergyUnits.KilowattDayPerKilogram:
            return ((value / (24 * 3.6e3)) / 1000.0)
        
        if from_unit == SpecificEnergyUnits.MegawattDayPerKilogram:
            return ((value / (24 * 3.6e3)) / 1000000.0)
        
        if from_unit == SpecificEnergyUnits.GigawattDayPerKilogram:
            return ((value / (24 * 3.6e3)) / 1000000000.0)
        
        if from_unit == SpecificEnergyUnits.TerawattDayPerKilogram:
            return ((value / (24 * 3.6e3)) / 1000000000000.0)
        
        if from_unit == SpecificEnergyUnits.KilowattDayPerTonne:
            return ((value / ((24 * 3.6e3) / 1e3)) / 1000.0)
        
        if from_unit == SpecificEnergyUnits.MegawattDayPerTonne:
            return ((value / ((24 * 3.6e3) / 1e3)) / 1000000.0)
        
        if from_unit == SpecificEnergyUnits.GigawattDayPerTonne:
            return ((value / ((24 * 3.6e3) / 1e3)) / 1000000000.0)
        
        if from_unit == SpecificEnergyUnits.TerawattDayPerTonne:
            return ((value / ((24 * 3.6e3) / 1e3)) / 1000000000000.0)
        
        if from_unit == SpecificEnergyUnits.KilowattDayPerShortTon:
            return ((value / ((24 * 3.6e3) / 9.0718474e2)) / 1000.0)
        
        if from_unit == SpecificEnergyUnits.MegawattDayPerShortTon:
            return ((value / ((24 * 3.6e3) / 9.0718474e2)) / 1000000.0)
        
        if from_unit == SpecificEnergyUnits.GigawattDayPerShortTon:
            return ((value / ((24 * 3.6e3) / 9.0718474e2)) / 1000000000.0)
        
        if from_unit == SpecificEnergyUnits.TerawattDayPerShortTon:
            return ((value / ((24 * 3.6e3) / 9.0718474e2)) / 1000000000000.0)
        
        if from_unit == SpecificEnergyUnits.KilowattHourPerPound:
            return ((value / 7.93664e3) / 1000.0)
        
        if from_unit == SpecificEnergyUnits.MegawattHourPerPound:
            return ((value / 7.93664e3) / 1000000.0)
        
        if from_unit == SpecificEnergyUnits.GigawattHourPerPound:
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
        
        if to_unit == SpecificEnergyUnits.KilojoulePerKilogram:
            return ((value) * 1000.0)
        
        if to_unit == SpecificEnergyUnits.MegajoulePerKilogram:
            return ((value) * 1000000.0)
        
        if to_unit == SpecificEnergyUnits.KilocaloriePerGram:
            return ((value * 4.184e3) * 1000.0)
        
        if to_unit == SpecificEnergyUnits.KilowattHourPerKilogram:
            return ((value * 3.6e3) * 1000.0)
        
        if to_unit == SpecificEnergyUnits.MegawattHourPerKilogram:
            return ((value * 3.6e3) * 1000000.0)
        
        if to_unit == SpecificEnergyUnits.GigawattHourPerKilogram:
            return ((value * 3.6e3) * 1000000000.0)
        
        if to_unit == SpecificEnergyUnits.KilowattDayPerKilogram:
            return ((value * (24 * 3.6e3)) * 1000.0)
        
        if to_unit == SpecificEnergyUnits.MegawattDayPerKilogram:
            return ((value * (24 * 3.6e3)) * 1000000.0)
        
        if to_unit == SpecificEnergyUnits.GigawattDayPerKilogram:
            return ((value * (24 * 3.6e3)) * 1000000000.0)
        
        if to_unit == SpecificEnergyUnits.TerawattDayPerKilogram:
            return ((value * (24 * 3.6e3)) * 1000000000000.0)
        
        if to_unit == SpecificEnergyUnits.KilowattDayPerTonne:
            return ((value * ((24 * 3.6e3) / 1e3)) * 1000.0)
        
        if to_unit == SpecificEnergyUnits.MegawattDayPerTonne:
            return ((value * ((24 * 3.6e3) / 1e3)) * 1000000.0)
        
        if to_unit == SpecificEnergyUnits.GigawattDayPerTonne:
            return ((value * ((24 * 3.6e3) / 1e3)) * 1000000000.0)
        
        if to_unit == SpecificEnergyUnits.TerawattDayPerTonne:
            return ((value * ((24 * 3.6e3) / 1e3)) * 1000000000000.0)
        
        if to_unit == SpecificEnergyUnits.KilowattDayPerShortTon:
            return ((value * ((24 * 3.6e3) / 9.0718474e2)) * 1000.0)
        
        if to_unit == SpecificEnergyUnits.MegawattDayPerShortTon:
            return ((value * ((24 * 3.6e3) / 9.0718474e2)) * 1000000.0)
        
        if to_unit == SpecificEnergyUnits.GigawattDayPerShortTon:
            return ((value * ((24 * 3.6e3) / 9.0718474e2)) * 1000000000.0)
        
        if to_unit == SpecificEnergyUnits.TerawattDayPerShortTon:
            return ((value * ((24 * 3.6e3) / 9.0718474e2)) * 1000000000000.0)
        
        if to_unit == SpecificEnergyUnits.KilowattHourPerPound:
            return ((value * 7.93664e3) * 1000.0)
        
        if to_unit == SpecificEnergyUnits.MegawattHourPerPound:
            return ((value * 7.93664e3) * 1000000.0)
        
        if to_unit == SpecificEnergyUnits.GigawattHourPerPound:
            return ((value * 7.93664e3) * 1000000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
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
    def from_kilojoules_per_kilogram(kilojoules_per_kilogram: float):
        """
        Create a new instance of SpecificEnergy from a value in kilojoules_per_kilogram.

        

        :param meters: The SpecificEnergy value in kilojoules_per_kilogram.
        :type kilojoules_per_kilogram: float
        :return: A new instance of SpecificEnergy.
        :rtype: SpecificEnergy
        """
        return SpecificEnergy(kilojoules_per_kilogram, SpecificEnergyUnits.KilojoulePerKilogram)

    
    @staticmethod
    def from_megajoules_per_kilogram(megajoules_per_kilogram: float):
        """
        Create a new instance of SpecificEnergy from a value in megajoules_per_kilogram.

        

        :param meters: The SpecificEnergy value in megajoules_per_kilogram.
        :type megajoules_per_kilogram: float
        :return: A new instance of SpecificEnergy.
        :rtype: SpecificEnergy
        """
        return SpecificEnergy(megajoules_per_kilogram, SpecificEnergyUnits.MegajoulePerKilogram)

    
    @staticmethod
    def from_kilocalories_per_gram(kilocalories_per_gram: float):
        """
        Create a new instance of SpecificEnergy from a value in kilocalories_per_gram.

        

        :param meters: The SpecificEnergy value in kilocalories_per_gram.
        :type kilocalories_per_gram: float
        :return: A new instance of SpecificEnergy.
        :rtype: SpecificEnergy
        """
        return SpecificEnergy(kilocalories_per_gram, SpecificEnergyUnits.KilocaloriePerGram)

    
    @staticmethod
    def from_kilowatt_hours_per_kilogram(kilowatt_hours_per_kilogram: float):
        """
        Create a new instance of SpecificEnergy from a value in kilowatt_hours_per_kilogram.

        

        :param meters: The SpecificEnergy value in kilowatt_hours_per_kilogram.
        :type kilowatt_hours_per_kilogram: float
        :return: A new instance of SpecificEnergy.
        :rtype: SpecificEnergy
        """
        return SpecificEnergy(kilowatt_hours_per_kilogram, SpecificEnergyUnits.KilowattHourPerKilogram)

    
    @staticmethod
    def from_megawatt_hours_per_kilogram(megawatt_hours_per_kilogram: float):
        """
        Create a new instance of SpecificEnergy from a value in megawatt_hours_per_kilogram.

        

        :param meters: The SpecificEnergy value in megawatt_hours_per_kilogram.
        :type megawatt_hours_per_kilogram: float
        :return: A new instance of SpecificEnergy.
        :rtype: SpecificEnergy
        """
        return SpecificEnergy(megawatt_hours_per_kilogram, SpecificEnergyUnits.MegawattHourPerKilogram)

    
    @staticmethod
    def from_gigawatt_hours_per_kilogram(gigawatt_hours_per_kilogram: float):
        """
        Create a new instance of SpecificEnergy from a value in gigawatt_hours_per_kilogram.

        

        :param meters: The SpecificEnergy value in gigawatt_hours_per_kilogram.
        :type gigawatt_hours_per_kilogram: float
        :return: A new instance of SpecificEnergy.
        :rtype: SpecificEnergy
        """
        return SpecificEnergy(gigawatt_hours_per_kilogram, SpecificEnergyUnits.GigawattHourPerKilogram)

    
    @staticmethod
    def from_kilowatt_days_per_kilogram(kilowatt_days_per_kilogram: float):
        """
        Create a new instance of SpecificEnergy from a value in kilowatt_days_per_kilogram.

        

        :param meters: The SpecificEnergy value in kilowatt_days_per_kilogram.
        :type kilowatt_days_per_kilogram: float
        :return: A new instance of SpecificEnergy.
        :rtype: SpecificEnergy
        """
        return SpecificEnergy(kilowatt_days_per_kilogram, SpecificEnergyUnits.KilowattDayPerKilogram)

    
    @staticmethod
    def from_megawatt_days_per_kilogram(megawatt_days_per_kilogram: float):
        """
        Create a new instance of SpecificEnergy from a value in megawatt_days_per_kilogram.

        

        :param meters: The SpecificEnergy value in megawatt_days_per_kilogram.
        :type megawatt_days_per_kilogram: float
        :return: A new instance of SpecificEnergy.
        :rtype: SpecificEnergy
        """
        return SpecificEnergy(megawatt_days_per_kilogram, SpecificEnergyUnits.MegawattDayPerKilogram)

    
    @staticmethod
    def from_gigawatt_days_per_kilogram(gigawatt_days_per_kilogram: float):
        """
        Create a new instance of SpecificEnergy from a value in gigawatt_days_per_kilogram.

        

        :param meters: The SpecificEnergy value in gigawatt_days_per_kilogram.
        :type gigawatt_days_per_kilogram: float
        :return: A new instance of SpecificEnergy.
        :rtype: SpecificEnergy
        """
        return SpecificEnergy(gigawatt_days_per_kilogram, SpecificEnergyUnits.GigawattDayPerKilogram)

    
    @staticmethod
    def from_terawatt_days_per_kilogram(terawatt_days_per_kilogram: float):
        """
        Create a new instance of SpecificEnergy from a value in terawatt_days_per_kilogram.

        

        :param meters: The SpecificEnergy value in terawatt_days_per_kilogram.
        :type terawatt_days_per_kilogram: float
        :return: A new instance of SpecificEnergy.
        :rtype: SpecificEnergy
        """
        return SpecificEnergy(terawatt_days_per_kilogram, SpecificEnergyUnits.TerawattDayPerKilogram)

    
    @staticmethod
    def from_kilowatt_days_per_tonne(kilowatt_days_per_tonne: float):
        """
        Create a new instance of SpecificEnergy from a value in kilowatt_days_per_tonne.

        

        :param meters: The SpecificEnergy value in kilowatt_days_per_tonne.
        :type kilowatt_days_per_tonne: float
        :return: A new instance of SpecificEnergy.
        :rtype: SpecificEnergy
        """
        return SpecificEnergy(kilowatt_days_per_tonne, SpecificEnergyUnits.KilowattDayPerTonne)

    
    @staticmethod
    def from_megawatt_days_per_tonne(megawatt_days_per_tonne: float):
        """
        Create a new instance of SpecificEnergy from a value in megawatt_days_per_tonne.

        

        :param meters: The SpecificEnergy value in megawatt_days_per_tonne.
        :type megawatt_days_per_tonne: float
        :return: A new instance of SpecificEnergy.
        :rtype: SpecificEnergy
        """
        return SpecificEnergy(megawatt_days_per_tonne, SpecificEnergyUnits.MegawattDayPerTonne)

    
    @staticmethod
    def from_gigawatt_days_per_tonne(gigawatt_days_per_tonne: float):
        """
        Create a new instance of SpecificEnergy from a value in gigawatt_days_per_tonne.

        

        :param meters: The SpecificEnergy value in gigawatt_days_per_tonne.
        :type gigawatt_days_per_tonne: float
        :return: A new instance of SpecificEnergy.
        :rtype: SpecificEnergy
        """
        return SpecificEnergy(gigawatt_days_per_tonne, SpecificEnergyUnits.GigawattDayPerTonne)

    
    @staticmethod
    def from_terawatt_days_per_tonne(terawatt_days_per_tonne: float):
        """
        Create a new instance of SpecificEnergy from a value in terawatt_days_per_tonne.

        

        :param meters: The SpecificEnergy value in terawatt_days_per_tonne.
        :type terawatt_days_per_tonne: float
        :return: A new instance of SpecificEnergy.
        :rtype: SpecificEnergy
        """
        return SpecificEnergy(terawatt_days_per_tonne, SpecificEnergyUnits.TerawattDayPerTonne)

    
    @staticmethod
    def from_kilowatt_days_per_short_ton(kilowatt_days_per_short_ton: float):
        """
        Create a new instance of SpecificEnergy from a value in kilowatt_days_per_short_ton.

        

        :param meters: The SpecificEnergy value in kilowatt_days_per_short_ton.
        :type kilowatt_days_per_short_ton: float
        :return: A new instance of SpecificEnergy.
        :rtype: SpecificEnergy
        """
        return SpecificEnergy(kilowatt_days_per_short_ton, SpecificEnergyUnits.KilowattDayPerShortTon)

    
    @staticmethod
    def from_megawatt_days_per_short_ton(megawatt_days_per_short_ton: float):
        """
        Create a new instance of SpecificEnergy from a value in megawatt_days_per_short_ton.

        

        :param meters: The SpecificEnergy value in megawatt_days_per_short_ton.
        :type megawatt_days_per_short_ton: float
        :return: A new instance of SpecificEnergy.
        :rtype: SpecificEnergy
        """
        return SpecificEnergy(megawatt_days_per_short_ton, SpecificEnergyUnits.MegawattDayPerShortTon)

    
    @staticmethod
    def from_gigawatt_days_per_short_ton(gigawatt_days_per_short_ton: float):
        """
        Create a new instance of SpecificEnergy from a value in gigawatt_days_per_short_ton.

        

        :param meters: The SpecificEnergy value in gigawatt_days_per_short_ton.
        :type gigawatt_days_per_short_ton: float
        :return: A new instance of SpecificEnergy.
        :rtype: SpecificEnergy
        """
        return SpecificEnergy(gigawatt_days_per_short_ton, SpecificEnergyUnits.GigawattDayPerShortTon)

    
    @staticmethod
    def from_terawatt_days_per_short_ton(terawatt_days_per_short_ton: float):
        """
        Create a new instance of SpecificEnergy from a value in terawatt_days_per_short_ton.

        

        :param meters: The SpecificEnergy value in terawatt_days_per_short_ton.
        :type terawatt_days_per_short_ton: float
        :return: A new instance of SpecificEnergy.
        :rtype: SpecificEnergy
        """
        return SpecificEnergy(terawatt_days_per_short_ton, SpecificEnergyUnits.TerawattDayPerShortTon)

    
    @staticmethod
    def from_kilowatt_hours_per_pound(kilowatt_hours_per_pound: float):
        """
        Create a new instance of SpecificEnergy from a value in kilowatt_hours_per_pound.

        

        :param meters: The SpecificEnergy value in kilowatt_hours_per_pound.
        :type kilowatt_hours_per_pound: float
        :return: A new instance of SpecificEnergy.
        :rtype: SpecificEnergy
        """
        return SpecificEnergy(kilowatt_hours_per_pound, SpecificEnergyUnits.KilowattHourPerPound)

    
    @staticmethod
    def from_megawatt_hours_per_pound(megawatt_hours_per_pound: float):
        """
        Create a new instance of SpecificEnergy from a value in megawatt_hours_per_pound.

        

        :param meters: The SpecificEnergy value in megawatt_hours_per_pound.
        :type megawatt_hours_per_pound: float
        :return: A new instance of SpecificEnergy.
        :rtype: SpecificEnergy
        """
        return SpecificEnergy(megawatt_hours_per_pound, SpecificEnergyUnits.MegawattHourPerPound)

    
    @staticmethod
    def from_gigawatt_hours_per_pound(gigawatt_hours_per_pound: float):
        """
        Create a new instance of SpecificEnergy from a value in gigawatt_hours_per_pound.

        

        :param meters: The SpecificEnergy value in gigawatt_hours_per_pound.
        :type gigawatt_hours_per_pound: float
        :return: A new instance of SpecificEnergy.
        :rtype: SpecificEnergy
        """
        return SpecificEnergy(gigawatt_hours_per_pound, SpecificEnergyUnits.GigawattHourPerPound)

    
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
    def kilojoules_per_kilogram(self) -> float:
        """
        
        """
        if self.__kilojoules_per_kilogram != None:
            return self.__kilojoules_per_kilogram
        self.__kilojoules_per_kilogram = self.__convert_from_base(SpecificEnergyUnits.KilojoulePerKilogram)
        return self.__kilojoules_per_kilogram

    
    @property
    def megajoules_per_kilogram(self) -> float:
        """
        
        """
        if self.__megajoules_per_kilogram != None:
            return self.__megajoules_per_kilogram
        self.__megajoules_per_kilogram = self.__convert_from_base(SpecificEnergyUnits.MegajoulePerKilogram)
        return self.__megajoules_per_kilogram

    
    @property
    def kilocalories_per_gram(self) -> float:
        """
        
        """
        if self.__kilocalories_per_gram != None:
            return self.__kilocalories_per_gram
        self.__kilocalories_per_gram = self.__convert_from_base(SpecificEnergyUnits.KilocaloriePerGram)
        return self.__kilocalories_per_gram

    
    @property
    def kilowatt_hours_per_kilogram(self) -> float:
        """
        
        """
        if self.__kilowatt_hours_per_kilogram != None:
            return self.__kilowatt_hours_per_kilogram
        self.__kilowatt_hours_per_kilogram = self.__convert_from_base(SpecificEnergyUnits.KilowattHourPerKilogram)
        return self.__kilowatt_hours_per_kilogram

    
    @property
    def megawatt_hours_per_kilogram(self) -> float:
        """
        
        """
        if self.__megawatt_hours_per_kilogram != None:
            return self.__megawatt_hours_per_kilogram
        self.__megawatt_hours_per_kilogram = self.__convert_from_base(SpecificEnergyUnits.MegawattHourPerKilogram)
        return self.__megawatt_hours_per_kilogram

    
    @property
    def gigawatt_hours_per_kilogram(self) -> float:
        """
        
        """
        if self.__gigawatt_hours_per_kilogram != None:
            return self.__gigawatt_hours_per_kilogram
        self.__gigawatt_hours_per_kilogram = self.__convert_from_base(SpecificEnergyUnits.GigawattHourPerKilogram)
        return self.__gigawatt_hours_per_kilogram

    
    @property
    def kilowatt_days_per_kilogram(self) -> float:
        """
        
        """
        if self.__kilowatt_days_per_kilogram != None:
            return self.__kilowatt_days_per_kilogram
        self.__kilowatt_days_per_kilogram = self.__convert_from_base(SpecificEnergyUnits.KilowattDayPerKilogram)
        return self.__kilowatt_days_per_kilogram

    
    @property
    def megawatt_days_per_kilogram(self) -> float:
        """
        
        """
        if self.__megawatt_days_per_kilogram != None:
            return self.__megawatt_days_per_kilogram
        self.__megawatt_days_per_kilogram = self.__convert_from_base(SpecificEnergyUnits.MegawattDayPerKilogram)
        return self.__megawatt_days_per_kilogram

    
    @property
    def gigawatt_days_per_kilogram(self) -> float:
        """
        
        """
        if self.__gigawatt_days_per_kilogram != None:
            return self.__gigawatt_days_per_kilogram
        self.__gigawatt_days_per_kilogram = self.__convert_from_base(SpecificEnergyUnits.GigawattDayPerKilogram)
        return self.__gigawatt_days_per_kilogram

    
    @property
    def terawatt_days_per_kilogram(self) -> float:
        """
        
        """
        if self.__terawatt_days_per_kilogram != None:
            return self.__terawatt_days_per_kilogram
        self.__terawatt_days_per_kilogram = self.__convert_from_base(SpecificEnergyUnits.TerawattDayPerKilogram)
        return self.__terawatt_days_per_kilogram

    
    @property
    def kilowatt_days_per_tonne(self) -> float:
        """
        
        """
        if self.__kilowatt_days_per_tonne != None:
            return self.__kilowatt_days_per_tonne
        self.__kilowatt_days_per_tonne = self.__convert_from_base(SpecificEnergyUnits.KilowattDayPerTonne)
        return self.__kilowatt_days_per_tonne

    
    @property
    def megawatt_days_per_tonne(self) -> float:
        """
        
        """
        if self.__megawatt_days_per_tonne != None:
            return self.__megawatt_days_per_tonne
        self.__megawatt_days_per_tonne = self.__convert_from_base(SpecificEnergyUnits.MegawattDayPerTonne)
        return self.__megawatt_days_per_tonne

    
    @property
    def gigawatt_days_per_tonne(self) -> float:
        """
        
        """
        if self.__gigawatt_days_per_tonne != None:
            return self.__gigawatt_days_per_tonne
        self.__gigawatt_days_per_tonne = self.__convert_from_base(SpecificEnergyUnits.GigawattDayPerTonne)
        return self.__gigawatt_days_per_tonne

    
    @property
    def terawatt_days_per_tonne(self) -> float:
        """
        
        """
        if self.__terawatt_days_per_tonne != None:
            return self.__terawatt_days_per_tonne
        self.__terawatt_days_per_tonne = self.__convert_from_base(SpecificEnergyUnits.TerawattDayPerTonne)
        return self.__terawatt_days_per_tonne

    
    @property
    def kilowatt_days_per_short_ton(self) -> float:
        """
        
        """
        if self.__kilowatt_days_per_short_ton != None:
            return self.__kilowatt_days_per_short_ton
        self.__kilowatt_days_per_short_ton = self.__convert_from_base(SpecificEnergyUnits.KilowattDayPerShortTon)
        return self.__kilowatt_days_per_short_ton

    
    @property
    def megawatt_days_per_short_ton(self) -> float:
        """
        
        """
        if self.__megawatt_days_per_short_ton != None:
            return self.__megawatt_days_per_short_ton
        self.__megawatt_days_per_short_ton = self.__convert_from_base(SpecificEnergyUnits.MegawattDayPerShortTon)
        return self.__megawatt_days_per_short_ton

    
    @property
    def gigawatt_days_per_short_ton(self) -> float:
        """
        
        """
        if self.__gigawatt_days_per_short_ton != None:
            return self.__gigawatt_days_per_short_ton
        self.__gigawatt_days_per_short_ton = self.__convert_from_base(SpecificEnergyUnits.GigawattDayPerShortTon)
        return self.__gigawatt_days_per_short_ton

    
    @property
    def terawatt_days_per_short_ton(self) -> float:
        """
        
        """
        if self.__terawatt_days_per_short_ton != None:
            return self.__terawatt_days_per_short_ton
        self.__terawatt_days_per_short_ton = self.__convert_from_base(SpecificEnergyUnits.TerawattDayPerShortTon)
        return self.__terawatt_days_per_short_ton

    
    @property
    def kilowatt_hours_per_pound(self) -> float:
        """
        
        """
        if self.__kilowatt_hours_per_pound != None:
            return self.__kilowatt_hours_per_pound
        self.__kilowatt_hours_per_pound = self.__convert_from_base(SpecificEnergyUnits.KilowattHourPerPound)
        return self.__kilowatt_hours_per_pound

    
    @property
    def megawatt_hours_per_pound(self) -> float:
        """
        
        """
        if self.__megawatt_hours_per_pound != None:
            return self.__megawatt_hours_per_pound
        self.__megawatt_hours_per_pound = self.__convert_from_base(SpecificEnergyUnits.MegawattHourPerPound)
        return self.__megawatt_hours_per_pound

    
    @property
    def gigawatt_hours_per_pound(self) -> float:
        """
        
        """
        if self.__gigawatt_hours_per_pound != None:
            return self.__gigawatt_hours_per_pound
        self.__gigawatt_hours_per_pound = self.__convert_from_base(SpecificEnergyUnits.GigawattHourPerPound)
        return self.__gigawatt_hours_per_pound

    
    def to_string(self, unit: SpecificEnergyUnits = SpecificEnergyUnits.JoulePerKilogram) -> str:
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
        
        if unit == SpecificEnergyUnits.KilojoulePerKilogram:
            return f"""{self.kilojoules_per_kilogram} kJ/kg"""
        
        if unit == SpecificEnergyUnits.MegajoulePerKilogram:
            return f"""{self.megajoules_per_kilogram} MJ/kg"""
        
        if unit == SpecificEnergyUnits.KilocaloriePerGram:
            return f"""{self.kilocalories_per_gram} kcal/g"""
        
        if unit == SpecificEnergyUnits.KilowattHourPerKilogram:
            return f"""{self.kilowatt_hours_per_kilogram} kWh/kg"""
        
        if unit == SpecificEnergyUnits.MegawattHourPerKilogram:
            return f"""{self.megawatt_hours_per_kilogram} MWh/kg"""
        
        if unit == SpecificEnergyUnits.GigawattHourPerKilogram:
            return f"""{self.gigawatt_hours_per_kilogram} GWh/kg"""
        
        if unit == SpecificEnergyUnits.KilowattDayPerKilogram:
            return f"""{self.kilowatt_days_per_kilogram} kWd/kg"""
        
        if unit == SpecificEnergyUnits.MegawattDayPerKilogram:
            return f"""{self.megawatt_days_per_kilogram} MWd/kg"""
        
        if unit == SpecificEnergyUnits.GigawattDayPerKilogram:
            return f"""{self.gigawatt_days_per_kilogram} GWd/kg"""
        
        if unit == SpecificEnergyUnits.TerawattDayPerKilogram:
            return f"""{self.terawatt_days_per_kilogram} TWd/kg"""
        
        if unit == SpecificEnergyUnits.KilowattDayPerTonne:
            return f"""{self.kilowatt_days_per_tonne} kWd/t"""
        
        if unit == SpecificEnergyUnits.MegawattDayPerTonne:
            return f"""{self.megawatt_days_per_tonne} MWd/t"""
        
        if unit == SpecificEnergyUnits.GigawattDayPerTonne:
            return f"""{self.gigawatt_days_per_tonne} GWd/t"""
        
        if unit == SpecificEnergyUnits.TerawattDayPerTonne:
            return f"""{self.terawatt_days_per_tonne} TWd/t"""
        
        if unit == SpecificEnergyUnits.KilowattDayPerShortTon:
            return f"""{self.kilowatt_days_per_short_ton} kWd/ST"""
        
        if unit == SpecificEnergyUnits.MegawattDayPerShortTon:
            return f"""{self.megawatt_days_per_short_ton} MWd/ST"""
        
        if unit == SpecificEnergyUnits.GigawattDayPerShortTon:
            return f"""{self.gigawatt_days_per_short_ton} GWd/ST"""
        
        if unit == SpecificEnergyUnits.TerawattDayPerShortTon:
            return f"""{self.terawatt_days_per_short_ton} TWd/ST"""
        
        if unit == SpecificEnergyUnits.KilowattHourPerPound:
            return f"""{self.kilowatt_hours_per_pound} kWh/lbs"""
        
        if unit == SpecificEnergyUnits.MegawattHourPerPound:
            return f"""{self.megawatt_hours_per_pound} MWh/lbs"""
        
        if unit == SpecificEnergyUnits.GigawattHourPerPound:
            return f"""{self.gigawatt_hours_per_pound} GWh/lbs"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: SpecificEnergyUnits = SpecificEnergyUnits.JoulePerKilogram) -> str:
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
        
        if unit_abbreviation == SpecificEnergyUnits.KilojoulePerKilogram:
            return """kJ/kg"""
        
        if unit_abbreviation == SpecificEnergyUnits.MegajoulePerKilogram:
            return """MJ/kg"""
        
        if unit_abbreviation == SpecificEnergyUnits.KilocaloriePerGram:
            return """kcal/g"""
        
        if unit_abbreviation == SpecificEnergyUnits.KilowattHourPerKilogram:
            return """kWh/kg"""
        
        if unit_abbreviation == SpecificEnergyUnits.MegawattHourPerKilogram:
            return """MWh/kg"""
        
        if unit_abbreviation == SpecificEnergyUnits.GigawattHourPerKilogram:
            return """GWh/kg"""
        
        if unit_abbreviation == SpecificEnergyUnits.KilowattDayPerKilogram:
            return """kWd/kg"""
        
        if unit_abbreviation == SpecificEnergyUnits.MegawattDayPerKilogram:
            return """MWd/kg"""
        
        if unit_abbreviation == SpecificEnergyUnits.GigawattDayPerKilogram:
            return """GWd/kg"""
        
        if unit_abbreviation == SpecificEnergyUnits.TerawattDayPerKilogram:
            return """TWd/kg"""
        
        if unit_abbreviation == SpecificEnergyUnits.KilowattDayPerTonne:
            return """kWd/t"""
        
        if unit_abbreviation == SpecificEnergyUnits.MegawattDayPerTonne:
            return """MWd/t"""
        
        if unit_abbreviation == SpecificEnergyUnits.GigawattDayPerTonne:
            return """GWd/t"""
        
        if unit_abbreviation == SpecificEnergyUnits.TerawattDayPerTonne:
            return """TWd/t"""
        
        if unit_abbreviation == SpecificEnergyUnits.KilowattDayPerShortTon:
            return """kWd/ST"""
        
        if unit_abbreviation == SpecificEnergyUnits.MegawattDayPerShortTon:
            return """MWd/ST"""
        
        if unit_abbreviation == SpecificEnergyUnits.GigawattDayPerShortTon:
            return """GWd/ST"""
        
        if unit_abbreviation == SpecificEnergyUnits.TerawattDayPerShortTon:
            return """TWd/ST"""
        
        if unit_abbreviation == SpecificEnergyUnits.KilowattHourPerPound:
            return """kWh/lbs"""
        
        if unit_abbreviation == SpecificEnergyUnits.MegawattHourPerPound:
            return """MWh/lbs"""
        
        if unit_abbreviation == SpecificEnergyUnits.GigawattHourPerPound:
            return """GWh/lbs"""
        
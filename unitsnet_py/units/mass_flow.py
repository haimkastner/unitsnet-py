from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class MassFlowUnits(Enum):
        """
            MassFlowUnits enumeration
        """
        
        GramPerSecond = 'GramPerSecond'
        """
            
        """
        
        GramPerDay = 'GramPerDay'
        """
            
        """
        
        GramPerHour = 'GramPerHour'
        """
            
        """
        
        KilogramPerHour = 'KilogramPerHour'
        """
            
        """
        
        KilogramPerMinute = 'KilogramPerMinute'
        """
            
        """
        
        TonnePerHour = 'TonnePerHour'
        """
            
        """
        
        PoundPerDay = 'PoundPerDay'
        """
            
        """
        
        PoundPerHour = 'PoundPerHour'
        """
            
        """
        
        PoundPerMinute = 'PoundPerMinute'
        """
            
        """
        
        PoundPerSecond = 'PoundPerSecond'
        """
            
        """
        
        TonnePerDay = 'TonnePerDay'
        """
            
        """
        
        ShortTonPerHour = 'ShortTonPerHour'
        """
            
        """
        
        NanogramPerSecond = 'NanogramPerSecond'
        """
            
        """
        
        MicrogramPerSecond = 'MicrogramPerSecond'
        """
            
        """
        
        MilligramPerSecond = 'MilligramPerSecond'
        """
            
        """
        
        CentigramPerSecond = 'CentigramPerSecond'
        """
            
        """
        
        DecigramPerSecond = 'DecigramPerSecond'
        """
            
        """
        
        DecagramPerSecond = 'DecagramPerSecond'
        """
            
        """
        
        HectogramPerSecond = 'HectogramPerSecond'
        """
            
        """
        
        KilogramPerSecond = 'KilogramPerSecond'
        """
            
        """
        
        NanogramPerDay = 'NanogramPerDay'
        """
            
        """
        
        MicrogramPerDay = 'MicrogramPerDay'
        """
            
        """
        
        MilligramPerDay = 'MilligramPerDay'
        """
            
        """
        
        CentigramPerDay = 'CentigramPerDay'
        """
            
        """
        
        DecigramPerDay = 'DecigramPerDay'
        """
            
        """
        
        DecagramPerDay = 'DecagramPerDay'
        """
            
        """
        
        HectogramPerDay = 'HectogramPerDay'
        """
            
        """
        
        KilogramPerDay = 'KilogramPerDay'
        """
            
        """
        
        MegagramPerDay = 'MegagramPerDay'
        """
            
        """
        
        MegapoundPerDay = 'MegapoundPerDay'
        """
            
        """
        
        MegapoundPerHour = 'MegapoundPerHour'
        """
            
        """
        
        MegapoundPerMinute = 'MegapoundPerMinute'
        """
            
        """
        
        MegapoundPerSecond = 'MegapoundPerSecond'
        """
            
        """
        

class MassFlowDto:
    """
    A DTO representation of a MassFlow

    Attributes:
        value (float): The value of the MassFlow.
        unit (MassFlowUnits): The specific unit that the MassFlow value is representing.
    """

    def __init__(self, value: float, unit: MassFlowUnits):
        """
        Create a new DTO representation of a MassFlow

        Parameters:
            value (float): The value of the MassFlow.
            unit (MassFlowUnits): The specific unit that the MassFlow value is representing.
        """
        self.value: float = value
        """
        The value of the MassFlow
        """
        self.unit: MassFlowUnits = unit
        """
        The specific unit that the MassFlow value is representing
        """

    def to_json(self):
        """
        Get a MassFlow DTO JSON object representing the current unit.

        :return: JSON object represents MassFlow DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "GramPerSecond"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of MassFlow DTO from a json representation.

        :param data: The MassFlow DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "GramPerSecond"}
        :return: A new instance of MassFlowDto.
        :rtype: MassFlowDto
        """
        return MassFlowDto(value=data["value"], unit=MassFlowUnits(data["unit"]))


class MassFlow(AbstractMeasure):
    """
    Mass flow is the ratio of the mass change to the time during which the change occurred (value of mass changes per unit time).

    Args:
        value (float): The value.
        from_unit (MassFlowUnits): The MassFlow unit to create from, The default unit is GramPerSecond
    """
    def __init__(self, value: float, from_unit: MassFlowUnits = MassFlowUnits.GramPerSecond):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__grams_per_second = None
        
        self.__grams_per_day = None
        
        self.__grams_per_hour = None
        
        self.__kilograms_per_hour = None
        
        self.__kilograms_per_minute = None
        
        self.__tonnes_per_hour = None
        
        self.__pounds_per_day = None
        
        self.__pounds_per_hour = None
        
        self.__pounds_per_minute = None
        
        self.__pounds_per_second = None
        
        self.__tonnes_per_day = None
        
        self.__short_tons_per_hour = None
        
        self.__nanograms_per_second = None
        
        self.__micrograms_per_second = None
        
        self.__milligrams_per_second = None
        
        self.__centigrams_per_second = None
        
        self.__decigrams_per_second = None
        
        self.__decagrams_per_second = None
        
        self.__hectograms_per_second = None
        
        self.__kilograms_per_second = None
        
        self.__nanograms_per_day = None
        
        self.__micrograms_per_day = None
        
        self.__milligrams_per_day = None
        
        self.__centigrams_per_day = None
        
        self.__decigrams_per_day = None
        
        self.__decagrams_per_day = None
        
        self.__hectograms_per_day = None
        
        self.__kilograms_per_day = None
        
        self.__megagrams_per_day = None
        
        self.__megapounds_per_day = None
        
        self.__megapounds_per_hour = None
        
        self.__megapounds_per_minute = None
        
        self.__megapounds_per_second = None
        

    def convert(self, unit: MassFlowUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: MassFlowUnits = MassFlowUnits.GramPerSecond) -> MassFlowDto:
        """
        Get a new instance of MassFlow DTO representing the current unit.

        :param hold_in_unit: The specific MassFlow unit to store the MassFlow value in the DTO representation.
        :type hold_in_unit: MassFlowUnits
        :return: A new instance of MassFlowDto.
        :rtype: MassFlowDto
        """
        return MassFlowDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: MassFlowUnits = MassFlowUnits.GramPerSecond):
        """
        Get a MassFlow DTO JSON object representing the current unit.

        :param hold_in_unit: The specific MassFlow unit to store the MassFlow value in the DTO representation.
        :type hold_in_unit: MassFlowUnits
        :return: JSON object represents MassFlow DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "GramPerSecond"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(mass_flow_dto: MassFlowDto):
        """
        Obtain a new instance of MassFlow from a DTO unit object.

        :param mass_flow_dto: The MassFlow DTO representation.
        :type mass_flow_dto: MassFlowDto
        :return: A new instance of MassFlow.
        :rtype: MassFlow
        """
        return MassFlow(mass_flow_dto.value, mass_flow_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of MassFlow from a DTO unit json representation.

        :param data: The MassFlow DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "GramPerSecond"}
        :return: A new instance of MassFlow.
        :rtype: MassFlow
        """
        return MassFlow.from_dto(MassFlowDto.from_json(data))

    def __convert_from_base(self, from_unit: MassFlowUnits) -> float:
        value = self._value
        
        if from_unit == MassFlowUnits.GramPerSecond:
            return (value)
        
        if from_unit == MassFlowUnits.GramPerDay:
            return (value * 86400)
        
        if from_unit == MassFlowUnits.GramPerHour:
            return (value * 3600)
        
        if from_unit == MassFlowUnits.KilogramPerHour:
            return (value * 3.6)
        
        if from_unit == MassFlowUnits.KilogramPerMinute:
            return (value * 0.06)
        
        if from_unit == MassFlowUnits.TonnePerHour:
            return (value * 3.6 / 1000)
        
        if from_unit == MassFlowUnits.PoundPerDay:
            return (value * 190.47936)
        
        if from_unit == MassFlowUnits.PoundPerHour:
            return (value * 7.93664)
        
        if from_unit == MassFlowUnits.PoundPerMinute:
            return (value * 0.132277)
        
        if from_unit == MassFlowUnits.PoundPerSecond:
            return (value / 453.59237)
        
        if from_unit == MassFlowUnits.TonnePerDay:
            return (value * 0.0864000)
        
        if from_unit == MassFlowUnits.ShortTonPerHour:
            return (value / 251.9957611)
        
        if from_unit == MassFlowUnits.NanogramPerSecond:
            return ((value) / 1e-09)
        
        if from_unit == MassFlowUnits.MicrogramPerSecond:
            return ((value) / 1e-06)
        
        if from_unit == MassFlowUnits.MilligramPerSecond:
            return ((value) / 0.001)
        
        if from_unit == MassFlowUnits.CentigramPerSecond:
            return ((value) / 0.01)
        
        if from_unit == MassFlowUnits.DecigramPerSecond:
            return ((value) / 0.1)
        
        if from_unit == MassFlowUnits.DecagramPerSecond:
            return ((value) / 10.0)
        
        if from_unit == MassFlowUnits.HectogramPerSecond:
            return ((value) / 100.0)
        
        if from_unit == MassFlowUnits.KilogramPerSecond:
            return ((value) / 1000.0)
        
        if from_unit == MassFlowUnits.NanogramPerDay:
            return ((value * 86400) / 1e-09)
        
        if from_unit == MassFlowUnits.MicrogramPerDay:
            return ((value * 86400) / 1e-06)
        
        if from_unit == MassFlowUnits.MilligramPerDay:
            return ((value * 86400) / 0.001)
        
        if from_unit == MassFlowUnits.CentigramPerDay:
            return ((value * 86400) / 0.01)
        
        if from_unit == MassFlowUnits.DecigramPerDay:
            return ((value * 86400) / 0.1)
        
        if from_unit == MassFlowUnits.DecagramPerDay:
            return ((value * 86400) / 10.0)
        
        if from_unit == MassFlowUnits.HectogramPerDay:
            return ((value * 86400) / 100.0)
        
        if from_unit == MassFlowUnits.KilogramPerDay:
            return ((value * 86400) / 1000.0)
        
        if from_unit == MassFlowUnits.MegagramPerDay:
            return ((value * 86400) / 1000000.0)
        
        if from_unit == MassFlowUnits.MegapoundPerDay:
            return ((value * 190.47936) / 1000000.0)
        
        if from_unit == MassFlowUnits.MegapoundPerHour:
            return ((value * 7.93664) / 1000000.0)
        
        if from_unit == MassFlowUnits.MegapoundPerMinute:
            return ((value * 0.132277) / 1000000.0)
        
        if from_unit == MassFlowUnits.MegapoundPerSecond:
            return ((value / 453.59237) / 1000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: MassFlowUnits) -> float:
        
        if to_unit == MassFlowUnits.GramPerSecond:
            return (value)
        
        if to_unit == MassFlowUnits.GramPerDay:
            return (value / 86400)
        
        if to_unit == MassFlowUnits.GramPerHour:
            return (value / 3600)
        
        if to_unit == MassFlowUnits.KilogramPerHour:
            return (value / 3.6)
        
        if to_unit == MassFlowUnits.KilogramPerMinute:
            return (value / 0.06)
        
        if to_unit == MassFlowUnits.TonnePerHour:
            return (1000 * value / 3.6)
        
        if to_unit == MassFlowUnits.PoundPerDay:
            return (value / 190.47936)
        
        if to_unit == MassFlowUnits.PoundPerHour:
            return (value / 7.93664)
        
        if to_unit == MassFlowUnits.PoundPerMinute:
            return (value / 0.132277)
        
        if to_unit == MassFlowUnits.PoundPerSecond:
            return (value * 453.59237)
        
        if to_unit == MassFlowUnits.TonnePerDay:
            return (value / 0.0864000)
        
        if to_unit == MassFlowUnits.ShortTonPerHour:
            return (value * 251.9957611)
        
        if to_unit == MassFlowUnits.NanogramPerSecond:
            return ((value) * 1e-09)
        
        if to_unit == MassFlowUnits.MicrogramPerSecond:
            return ((value) * 1e-06)
        
        if to_unit == MassFlowUnits.MilligramPerSecond:
            return ((value) * 0.001)
        
        if to_unit == MassFlowUnits.CentigramPerSecond:
            return ((value) * 0.01)
        
        if to_unit == MassFlowUnits.DecigramPerSecond:
            return ((value) * 0.1)
        
        if to_unit == MassFlowUnits.DecagramPerSecond:
            return ((value) * 10.0)
        
        if to_unit == MassFlowUnits.HectogramPerSecond:
            return ((value) * 100.0)
        
        if to_unit == MassFlowUnits.KilogramPerSecond:
            return ((value) * 1000.0)
        
        if to_unit == MassFlowUnits.NanogramPerDay:
            return ((value / 86400) * 1e-09)
        
        if to_unit == MassFlowUnits.MicrogramPerDay:
            return ((value / 86400) * 1e-06)
        
        if to_unit == MassFlowUnits.MilligramPerDay:
            return ((value / 86400) * 0.001)
        
        if to_unit == MassFlowUnits.CentigramPerDay:
            return ((value / 86400) * 0.01)
        
        if to_unit == MassFlowUnits.DecigramPerDay:
            return ((value / 86400) * 0.1)
        
        if to_unit == MassFlowUnits.DecagramPerDay:
            return ((value / 86400) * 10.0)
        
        if to_unit == MassFlowUnits.HectogramPerDay:
            return ((value / 86400) * 100.0)
        
        if to_unit == MassFlowUnits.KilogramPerDay:
            return ((value / 86400) * 1000.0)
        
        if to_unit == MassFlowUnits.MegagramPerDay:
            return ((value / 86400) * 1000000.0)
        
        if to_unit == MassFlowUnits.MegapoundPerDay:
            return ((value / 190.47936) * 1000000.0)
        
        if to_unit == MassFlowUnits.MegapoundPerHour:
            return ((value / 7.93664) * 1000000.0)
        
        if to_unit == MassFlowUnits.MegapoundPerMinute:
            return ((value / 0.132277) * 1000000.0)
        
        if to_unit == MassFlowUnits.MegapoundPerSecond:
            return ((value * 453.59237) * 1000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_grams_per_second(grams_per_second: float):
        """
        Create a new instance of MassFlow from a value in grams_per_second.

        

        :param meters: The MassFlow value in grams_per_second.
        :type grams_per_second: float
        :return: A new instance of MassFlow.
        :rtype: MassFlow
        """
        return MassFlow(grams_per_second, MassFlowUnits.GramPerSecond)

    
    @staticmethod
    def from_grams_per_day(grams_per_day: float):
        """
        Create a new instance of MassFlow from a value in grams_per_day.

        

        :param meters: The MassFlow value in grams_per_day.
        :type grams_per_day: float
        :return: A new instance of MassFlow.
        :rtype: MassFlow
        """
        return MassFlow(grams_per_day, MassFlowUnits.GramPerDay)

    
    @staticmethod
    def from_grams_per_hour(grams_per_hour: float):
        """
        Create a new instance of MassFlow from a value in grams_per_hour.

        

        :param meters: The MassFlow value in grams_per_hour.
        :type grams_per_hour: float
        :return: A new instance of MassFlow.
        :rtype: MassFlow
        """
        return MassFlow(grams_per_hour, MassFlowUnits.GramPerHour)

    
    @staticmethod
    def from_kilograms_per_hour(kilograms_per_hour: float):
        """
        Create a new instance of MassFlow from a value in kilograms_per_hour.

        

        :param meters: The MassFlow value in kilograms_per_hour.
        :type kilograms_per_hour: float
        :return: A new instance of MassFlow.
        :rtype: MassFlow
        """
        return MassFlow(kilograms_per_hour, MassFlowUnits.KilogramPerHour)

    
    @staticmethod
    def from_kilograms_per_minute(kilograms_per_minute: float):
        """
        Create a new instance of MassFlow from a value in kilograms_per_minute.

        

        :param meters: The MassFlow value in kilograms_per_minute.
        :type kilograms_per_minute: float
        :return: A new instance of MassFlow.
        :rtype: MassFlow
        """
        return MassFlow(kilograms_per_minute, MassFlowUnits.KilogramPerMinute)

    
    @staticmethod
    def from_tonnes_per_hour(tonnes_per_hour: float):
        """
        Create a new instance of MassFlow from a value in tonnes_per_hour.

        

        :param meters: The MassFlow value in tonnes_per_hour.
        :type tonnes_per_hour: float
        :return: A new instance of MassFlow.
        :rtype: MassFlow
        """
        return MassFlow(tonnes_per_hour, MassFlowUnits.TonnePerHour)

    
    @staticmethod
    def from_pounds_per_day(pounds_per_day: float):
        """
        Create a new instance of MassFlow from a value in pounds_per_day.

        

        :param meters: The MassFlow value in pounds_per_day.
        :type pounds_per_day: float
        :return: A new instance of MassFlow.
        :rtype: MassFlow
        """
        return MassFlow(pounds_per_day, MassFlowUnits.PoundPerDay)

    
    @staticmethod
    def from_pounds_per_hour(pounds_per_hour: float):
        """
        Create a new instance of MassFlow from a value in pounds_per_hour.

        

        :param meters: The MassFlow value in pounds_per_hour.
        :type pounds_per_hour: float
        :return: A new instance of MassFlow.
        :rtype: MassFlow
        """
        return MassFlow(pounds_per_hour, MassFlowUnits.PoundPerHour)

    
    @staticmethod
    def from_pounds_per_minute(pounds_per_minute: float):
        """
        Create a new instance of MassFlow from a value in pounds_per_minute.

        

        :param meters: The MassFlow value in pounds_per_minute.
        :type pounds_per_minute: float
        :return: A new instance of MassFlow.
        :rtype: MassFlow
        """
        return MassFlow(pounds_per_minute, MassFlowUnits.PoundPerMinute)

    
    @staticmethod
    def from_pounds_per_second(pounds_per_second: float):
        """
        Create a new instance of MassFlow from a value in pounds_per_second.

        

        :param meters: The MassFlow value in pounds_per_second.
        :type pounds_per_second: float
        :return: A new instance of MassFlow.
        :rtype: MassFlow
        """
        return MassFlow(pounds_per_second, MassFlowUnits.PoundPerSecond)

    
    @staticmethod
    def from_tonnes_per_day(tonnes_per_day: float):
        """
        Create a new instance of MassFlow from a value in tonnes_per_day.

        

        :param meters: The MassFlow value in tonnes_per_day.
        :type tonnes_per_day: float
        :return: A new instance of MassFlow.
        :rtype: MassFlow
        """
        return MassFlow(tonnes_per_day, MassFlowUnits.TonnePerDay)

    
    @staticmethod
    def from_short_tons_per_hour(short_tons_per_hour: float):
        """
        Create a new instance of MassFlow from a value in short_tons_per_hour.

        

        :param meters: The MassFlow value in short_tons_per_hour.
        :type short_tons_per_hour: float
        :return: A new instance of MassFlow.
        :rtype: MassFlow
        """
        return MassFlow(short_tons_per_hour, MassFlowUnits.ShortTonPerHour)

    
    @staticmethod
    def from_nanograms_per_second(nanograms_per_second: float):
        """
        Create a new instance of MassFlow from a value in nanograms_per_second.

        

        :param meters: The MassFlow value in nanograms_per_second.
        :type nanograms_per_second: float
        :return: A new instance of MassFlow.
        :rtype: MassFlow
        """
        return MassFlow(nanograms_per_second, MassFlowUnits.NanogramPerSecond)

    
    @staticmethod
    def from_micrograms_per_second(micrograms_per_second: float):
        """
        Create a new instance of MassFlow from a value in micrograms_per_second.

        

        :param meters: The MassFlow value in micrograms_per_second.
        :type micrograms_per_second: float
        :return: A new instance of MassFlow.
        :rtype: MassFlow
        """
        return MassFlow(micrograms_per_second, MassFlowUnits.MicrogramPerSecond)

    
    @staticmethod
    def from_milligrams_per_second(milligrams_per_second: float):
        """
        Create a new instance of MassFlow from a value in milligrams_per_second.

        

        :param meters: The MassFlow value in milligrams_per_second.
        :type milligrams_per_second: float
        :return: A new instance of MassFlow.
        :rtype: MassFlow
        """
        return MassFlow(milligrams_per_second, MassFlowUnits.MilligramPerSecond)

    
    @staticmethod
    def from_centigrams_per_second(centigrams_per_second: float):
        """
        Create a new instance of MassFlow from a value in centigrams_per_second.

        

        :param meters: The MassFlow value in centigrams_per_second.
        :type centigrams_per_second: float
        :return: A new instance of MassFlow.
        :rtype: MassFlow
        """
        return MassFlow(centigrams_per_second, MassFlowUnits.CentigramPerSecond)

    
    @staticmethod
    def from_decigrams_per_second(decigrams_per_second: float):
        """
        Create a new instance of MassFlow from a value in decigrams_per_second.

        

        :param meters: The MassFlow value in decigrams_per_second.
        :type decigrams_per_second: float
        :return: A new instance of MassFlow.
        :rtype: MassFlow
        """
        return MassFlow(decigrams_per_second, MassFlowUnits.DecigramPerSecond)

    
    @staticmethod
    def from_decagrams_per_second(decagrams_per_second: float):
        """
        Create a new instance of MassFlow from a value in decagrams_per_second.

        

        :param meters: The MassFlow value in decagrams_per_second.
        :type decagrams_per_second: float
        :return: A new instance of MassFlow.
        :rtype: MassFlow
        """
        return MassFlow(decagrams_per_second, MassFlowUnits.DecagramPerSecond)

    
    @staticmethod
    def from_hectograms_per_second(hectograms_per_second: float):
        """
        Create a new instance of MassFlow from a value in hectograms_per_second.

        

        :param meters: The MassFlow value in hectograms_per_second.
        :type hectograms_per_second: float
        :return: A new instance of MassFlow.
        :rtype: MassFlow
        """
        return MassFlow(hectograms_per_second, MassFlowUnits.HectogramPerSecond)

    
    @staticmethod
    def from_kilograms_per_second(kilograms_per_second: float):
        """
        Create a new instance of MassFlow from a value in kilograms_per_second.

        

        :param meters: The MassFlow value in kilograms_per_second.
        :type kilograms_per_second: float
        :return: A new instance of MassFlow.
        :rtype: MassFlow
        """
        return MassFlow(kilograms_per_second, MassFlowUnits.KilogramPerSecond)

    
    @staticmethod
    def from_nanograms_per_day(nanograms_per_day: float):
        """
        Create a new instance of MassFlow from a value in nanograms_per_day.

        

        :param meters: The MassFlow value in nanograms_per_day.
        :type nanograms_per_day: float
        :return: A new instance of MassFlow.
        :rtype: MassFlow
        """
        return MassFlow(nanograms_per_day, MassFlowUnits.NanogramPerDay)

    
    @staticmethod
    def from_micrograms_per_day(micrograms_per_day: float):
        """
        Create a new instance of MassFlow from a value in micrograms_per_day.

        

        :param meters: The MassFlow value in micrograms_per_day.
        :type micrograms_per_day: float
        :return: A new instance of MassFlow.
        :rtype: MassFlow
        """
        return MassFlow(micrograms_per_day, MassFlowUnits.MicrogramPerDay)

    
    @staticmethod
    def from_milligrams_per_day(milligrams_per_day: float):
        """
        Create a new instance of MassFlow from a value in milligrams_per_day.

        

        :param meters: The MassFlow value in milligrams_per_day.
        :type milligrams_per_day: float
        :return: A new instance of MassFlow.
        :rtype: MassFlow
        """
        return MassFlow(milligrams_per_day, MassFlowUnits.MilligramPerDay)

    
    @staticmethod
    def from_centigrams_per_day(centigrams_per_day: float):
        """
        Create a new instance of MassFlow from a value in centigrams_per_day.

        

        :param meters: The MassFlow value in centigrams_per_day.
        :type centigrams_per_day: float
        :return: A new instance of MassFlow.
        :rtype: MassFlow
        """
        return MassFlow(centigrams_per_day, MassFlowUnits.CentigramPerDay)

    
    @staticmethod
    def from_decigrams_per_day(decigrams_per_day: float):
        """
        Create a new instance of MassFlow from a value in decigrams_per_day.

        

        :param meters: The MassFlow value in decigrams_per_day.
        :type decigrams_per_day: float
        :return: A new instance of MassFlow.
        :rtype: MassFlow
        """
        return MassFlow(decigrams_per_day, MassFlowUnits.DecigramPerDay)

    
    @staticmethod
    def from_decagrams_per_day(decagrams_per_day: float):
        """
        Create a new instance of MassFlow from a value in decagrams_per_day.

        

        :param meters: The MassFlow value in decagrams_per_day.
        :type decagrams_per_day: float
        :return: A new instance of MassFlow.
        :rtype: MassFlow
        """
        return MassFlow(decagrams_per_day, MassFlowUnits.DecagramPerDay)

    
    @staticmethod
    def from_hectograms_per_day(hectograms_per_day: float):
        """
        Create a new instance of MassFlow from a value in hectograms_per_day.

        

        :param meters: The MassFlow value in hectograms_per_day.
        :type hectograms_per_day: float
        :return: A new instance of MassFlow.
        :rtype: MassFlow
        """
        return MassFlow(hectograms_per_day, MassFlowUnits.HectogramPerDay)

    
    @staticmethod
    def from_kilograms_per_day(kilograms_per_day: float):
        """
        Create a new instance of MassFlow from a value in kilograms_per_day.

        

        :param meters: The MassFlow value in kilograms_per_day.
        :type kilograms_per_day: float
        :return: A new instance of MassFlow.
        :rtype: MassFlow
        """
        return MassFlow(kilograms_per_day, MassFlowUnits.KilogramPerDay)

    
    @staticmethod
    def from_megagrams_per_day(megagrams_per_day: float):
        """
        Create a new instance of MassFlow from a value in megagrams_per_day.

        

        :param meters: The MassFlow value in megagrams_per_day.
        :type megagrams_per_day: float
        :return: A new instance of MassFlow.
        :rtype: MassFlow
        """
        return MassFlow(megagrams_per_day, MassFlowUnits.MegagramPerDay)

    
    @staticmethod
    def from_megapounds_per_day(megapounds_per_day: float):
        """
        Create a new instance of MassFlow from a value in megapounds_per_day.

        

        :param meters: The MassFlow value in megapounds_per_day.
        :type megapounds_per_day: float
        :return: A new instance of MassFlow.
        :rtype: MassFlow
        """
        return MassFlow(megapounds_per_day, MassFlowUnits.MegapoundPerDay)

    
    @staticmethod
    def from_megapounds_per_hour(megapounds_per_hour: float):
        """
        Create a new instance of MassFlow from a value in megapounds_per_hour.

        

        :param meters: The MassFlow value in megapounds_per_hour.
        :type megapounds_per_hour: float
        :return: A new instance of MassFlow.
        :rtype: MassFlow
        """
        return MassFlow(megapounds_per_hour, MassFlowUnits.MegapoundPerHour)

    
    @staticmethod
    def from_megapounds_per_minute(megapounds_per_minute: float):
        """
        Create a new instance of MassFlow from a value in megapounds_per_minute.

        

        :param meters: The MassFlow value in megapounds_per_minute.
        :type megapounds_per_minute: float
        :return: A new instance of MassFlow.
        :rtype: MassFlow
        """
        return MassFlow(megapounds_per_minute, MassFlowUnits.MegapoundPerMinute)

    
    @staticmethod
    def from_megapounds_per_second(megapounds_per_second: float):
        """
        Create a new instance of MassFlow from a value in megapounds_per_second.

        

        :param meters: The MassFlow value in megapounds_per_second.
        :type megapounds_per_second: float
        :return: A new instance of MassFlow.
        :rtype: MassFlow
        """
        return MassFlow(megapounds_per_second, MassFlowUnits.MegapoundPerSecond)

    
    @property
    def grams_per_second(self) -> float:
        """
        
        """
        if self.__grams_per_second != None:
            return self.__grams_per_second
        self.__grams_per_second = self.__convert_from_base(MassFlowUnits.GramPerSecond)
        return self.__grams_per_second

    
    @property
    def grams_per_day(self) -> float:
        """
        
        """
        if self.__grams_per_day != None:
            return self.__grams_per_day
        self.__grams_per_day = self.__convert_from_base(MassFlowUnits.GramPerDay)
        return self.__grams_per_day

    
    @property
    def grams_per_hour(self) -> float:
        """
        
        """
        if self.__grams_per_hour != None:
            return self.__grams_per_hour
        self.__grams_per_hour = self.__convert_from_base(MassFlowUnits.GramPerHour)
        return self.__grams_per_hour

    
    @property
    def kilograms_per_hour(self) -> float:
        """
        
        """
        if self.__kilograms_per_hour != None:
            return self.__kilograms_per_hour
        self.__kilograms_per_hour = self.__convert_from_base(MassFlowUnits.KilogramPerHour)
        return self.__kilograms_per_hour

    
    @property
    def kilograms_per_minute(self) -> float:
        """
        
        """
        if self.__kilograms_per_minute != None:
            return self.__kilograms_per_minute
        self.__kilograms_per_minute = self.__convert_from_base(MassFlowUnits.KilogramPerMinute)
        return self.__kilograms_per_minute

    
    @property
    def tonnes_per_hour(self) -> float:
        """
        
        """
        if self.__tonnes_per_hour != None:
            return self.__tonnes_per_hour
        self.__tonnes_per_hour = self.__convert_from_base(MassFlowUnits.TonnePerHour)
        return self.__tonnes_per_hour

    
    @property
    def pounds_per_day(self) -> float:
        """
        
        """
        if self.__pounds_per_day != None:
            return self.__pounds_per_day
        self.__pounds_per_day = self.__convert_from_base(MassFlowUnits.PoundPerDay)
        return self.__pounds_per_day

    
    @property
    def pounds_per_hour(self) -> float:
        """
        
        """
        if self.__pounds_per_hour != None:
            return self.__pounds_per_hour
        self.__pounds_per_hour = self.__convert_from_base(MassFlowUnits.PoundPerHour)
        return self.__pounds_per_hour

    
    @property
    def pounds_per_minute(self) -> float:
        """
        
        """
        if self.__pounds_per_minute != None:
            return self.__pounds_per_minute
        self.__pounds_per_minute = self.__convert_from_base(MassFlowUnits.PoundPerMinute)
        return self.__pounds_per_minute

    
    @property
    def pounds_per_second(self) -> float:
        """
        
        """
        if self.__pounds_per_second != None:
            return self.__pounds_per_second
        self.__pounds_per_second = self.__convert_from_base(MassFlowUnits.PoundPerSecond)
        return self.__pounds_per_second

    
    @property
    def tonnes_per_day(self) -> float:
        """
        
        """
        if self.__tonnes_per_day != None:
            return self.__tonnes_per_day
        self.__tonnes_per_day = self.__convert_from_base(MassFlowUnits.TonnePerDay)
        return self.__tonnes_per_day

    
    @property
    def short_tons_per_hour(self) -> float:
        """
        
        """
        if self.__short_tons_per_hour != None:
            return self.__short_tons_per_hour
        self.__short_tons_per_hour = self.__convert_from_base(MassFlowUnits.ShortTonPerHour)
        return self.__short_tons_per_hour

    
    @property
    def nanograms_per_second(self) -> float:
        """
        
        """
        if self.__nanograms_per_second != None:
            return self.__nanograms_per_second
        self.__nanograms_per_second = self.__convert_from_base(MassFlowUnits.NanogramPerSecond)
        return self.__nanograms_per_second

    
    @property
    def micrograms_per_second(self) -> float:
        """
        
        """
        if self.__micrograms_per_second != None:
            return self.__micrograms_per_second
        self.__micrograms_per_second = self.__convert_from_base(MassFlowUnits.MicrogramPerSecond)
        return self.__micrograms_per_second

    
    @property
    def milligrams_per_second(self) -> float:
        """
        
        """
        if self.__milligrams_per_second != None:
            return self.__milligrams_per_second
        self.__milligrams_per_second = self.__convert_from_base(MassFlowUnits.MilligramPerSecond)
        return self.__milligrams_per_second

    
    @property
    def centigrams_per_second(self) -> float:
        """
        
        """
        if self.__centigrams_per_second != None:
            return self.__centigrams_per_second
        self.__centigrams_per_second = self.__convert_from_base(MassFlowUnits.CentigramPerSecond)
        return self.__centigrams_per_second

    
    @property
    def decigrams_per_second(self) -> float:
        """
        
        """
        if self.__decigrams_per_second != None:
            return self.__decigrams_per_second
        self.__decigrams_per_second = self.__convert_from_base(MassFlowUnits.DecigramPerSecond)
        return self.__decigrams_per_second

    
    @property
    def decagrams_per_second(self) -> float:
        """
        
        """
        if self.__decagrams_per_second != None:
            return self.__decagrams_per_second
        self.__decagrams_per_second = self.__convert_from_base(MassFlowUnits.DecagramPerSecond)
        return self.__decagrams_per_second

    
    @property
    def hectograms_per_second(self) -> float:
        """
        
        """
        if self.__hectograms_per_second != None:
            return self.__hectograms_per_second
        self.__hectograms_per_second = self.__convert_from_base(MassFlowUnits.HectogramPerSecond)
        return self.__hectograms_per_second

    
    @property
    def kilograms_per_second(self) -> float:
        """
        
        """
        if self.__kilograms_per_second != None:
            return self.__kilograms_per_second
        self.__kilograms_per_second = self.__convert_from_base(MassFlowUnits.KilogramPerSecond)
        return self.__kilograms_per_second

    
    @property
    def nanograms_per_day(self) -> float:
        """
        
        """
        if self.__nanograms_per_day != None:
            return self.__nanograms_per_day
        self.__nanograms_per_day = self.__convert_from_base(MassFlowUnits.NanogramPerDay)
        return self.__nanograms_per_day

    
    @property
    def micrograms_per_day(self) -> float:
        """
        
        """
        if self.__micrograms_per_day != None:
            return self.__micrograms_per_day
        self.__micrograms_per_day = self.__convert_from_base(MassFlowUnits.MicrogramPerDay)
        return self.__micrograms_per_day

    
    @property
    def milligrams_per_day(self) -> float:
        """
        
        """
        if self.__milligrams_per_day != None:
            return self.__milligrams_per_day
        self.__milligrams_per_day = self.__convert_from_base(MassFlowUnits.MilligramPerDay)
        return self.__milligrams_per_day

    
    @property
    def centigrams_per_day(self) -> float:
        """
        
        """
        if self.__centigrams_per_day != None:
            return self.__centigrams_per_day
        self.__centigrams_per_day = self.__convert_from_base(MassFlowUnits.CentigramPerDay)
        return self.__centigrams_per_day

    
    @property
    def decigrams_per_day(self) -> float:
        """
        
        """
        if self.__decigrams_per_day != None:
            return self.__decigrams_per_day
        self.__decigrams_per_day = self.__convert_from_base(MassFlowUnits.DecigramPerDay)
        return self.__decigrams_per_day

    
    @property
    def decagrams_per_day(self) -> float:
        """
        
        """
        if self.__decagrams_per_day != None:
            return self.__decagrams_per_day
        self.__decagrams_per_day = self.__convert_from_base(MassFlowUnits.DecagramPerDay)
        return self.__decagrams_per_day

    
    @property
    def hectograms_per_day(self) -> float:
        """
        
        """
        if self.__hectograms_per_day != None:
            return self.__hectograms_per_day
        self.__hectograms_per_day = self.__convert_from_base(MassFlowUnits.HectogramPerDay)
        return self.__hectograms_per_day

    
    @property
    def kilograms_per_day(self) -> float:
        """
        
        """
        if self.__kilograms_per_day != None:
            return self.__kilograms_per_day
        self.__kilograms_per_day = self.__convert_from_base(MassFlowUnits.KilogramPerDay)
        return self.__kilograms_per_day

    
    @property
    def megagrams_per_day(self) -> float:
        """
        
        """
        if self.__megagrams_per_day != None:
            return self.__megagrams_per_day
        self.__megagrams_per_day = self.__convert_from_base(MassFlowUnits.MegagramPerDay)
        return self.__megagrams_per_day

    
    @property
    def megapounds_per_day(self) -> float:
        """
        
        """
        if self.__megapounds_per_day != None:
            return self.__megapounds_per_day
        self.__megapounds_per_day = self.__convert_from_base(MassFlowUnits.MegapoundPerDay)
        return self.__megapounds_per_day

    
    @property
    def megapounds_per_hour(self) -> float:
        """
        
        """
        if self.__megapounds_per_hour != None:
            return self.__megapounds_per_hour
        self.__megapounds_per_hour = self.__convert_from_base(MassFlowUnits.MegapoundPerHour)
        return self.__megapounds_per_hour

    
    @property
    def megapounds_per_minute(self) -> float:
        """
        
        """
        if self.__megapounds_per_minute != None:
            return self.__megapounds_per_minute
        self.__megapounds_per_minute = self.__convert_from_base(MassFlowUnits.MegapoundPerMinute)
        return self.__megapounds_per_minute

    
    @property
    def megapounds_per_second(self) -> float:
        """
        
        """
        if self.__megapounds_per_second != None:
            return self.__megapounds_per_second
        self.__megapounds_per_second = self.__convert_from_base(MassFlowUnits.MegapoundPerSecond)
        return self.__megapounds_per_second

    
    def to_string(self, unit: MassFlowUnits = MassFlowUnits.GramPerSecond, fractional_digits: int = None) -> str:
        """
        Format the MassFlow to a string.
        
        Note: the default format for MassFlow is GramPerSecond.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the MassFlow. Default is 'GramPerSecond'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == MassFlowUnits.GramPerSecond:
            return f"""{super()._truncate_fraction_digits(self.grams_per_second, fractional_digits)} g/s"""
        
        if unit == MassFlowUnits.GramPerDay:
            return f"""{super()._truncate_fraction_digits(self.grams_per_day, fractional_digits)} g/d"""
        
        if unit == MassFlowUnits.GramPerHour:
            return f"""{super()._truncate_fraction_digits(self.grams_per_hour, fractional_digits)} g/h"""
        
        if unit == MassFlowUnits.KilogramPerHour:
            return f"""{super()._truncate_fraction_digits(self.kilograms_per_hour, fractional_digits)} kg/h"""
        
        if unit == MassFlowUnits.KilogramPerMinute:
            return f"""{super()._truncate_fraction_digits(self.kilograms_per_minute, fractional_digits)} kg/min"""
        
        if unit == MassFlowUnits.TonnePerHour:
            return f"""{super()._truncate_fraction_digits(self.tonnes_per_hour, fractional_digits)} t/h"""
        
        if unit == MassFlowUnits.PoundPerDay:
            return f"""{super()._truncate_fraction_digits(self.pounds_per_day, fractional_digits)} lb/d"""
        
        if unit == MassFlowUnits.PoundPerHour:
            return f"""{super()._truncate_fraction_digits(self.pounds_per_hour, fractional_digits)} lb/h"""
        
        if unit == MassFlowUnits.PoundPerMinute:
            return f"""{super()._truncate_fraction_digits(self.pounds_per_minute, fractional_digits)} lb/min"""
        
        if unit == MassFlowUnits.PoundPerSecond:
            return f"""{super()._truncate_fraction_digits(self.pounds_per_second, fractional_digits)} lb/s"""
        
        if unit == MassFlowUnits.TonnePerDay:
            return f"""{super()._truncate_fraction_digits(self.tonnes_per_day, fractional_digits)} t/d"""
        
        if unit == MassFlowUnits.ShortTonPerHour:
            return f"""{super()._truncate_fraction_digits(self.short_tons_per_hour, fractional_digits)} short tn/h"""
        
        if unit == MassFlowUnits.NanogramPerSecond:
            return f"""{super()._truncate_fraction_digits(self.nanograms_per_second, fractional_digits)} ng/s"""
        
        if unit == MassFlowUnits.MicrogramPerSecond:
            return f"""{super()._truncate_fraction_digits(self.micrograms_per_second, fractional_digits)} μg/s"""
        
        if unit == MassFlowUnits.MilligramPerSecond:
            return f"""{super()._truncate_fraction_digits(self.milligrams_per_second, fractional_digits)} mg/s"""
        
        if unit == MassFlowUnits.CentigramPerSecond:
            return f"""{super()._truncate_fraction_digits(self.centigrams_per_second, fractional_digits)} cg/s"""
        
        if unit == MassFlowUnits.DecigramPerSecond:
            return f"""{super()._truncate_fraction_digits(self.decigrams_per_second, fractional_digits)} dg/s"""
        
        if unit == MassFlowUnits.DecagramPerSecond:
            return f"""{super()._truncate_fraction_digits(self.decagrams_per_second, fractional_digits)} dag/s"""
        
        if unit == MassFlowUnits.HectogramPerSecond:
            return f"""{super()._truncate_fraction_digits(self.hectograms_per_second, fractional_digits)} hg/s"""
        
        if unit == MassFlowUnits.KilogramPerSecond:
            return f"""{super()._truncate_fraction_digits(self.kilograms_per_second, fractional_digits)} kg/s"""
        
        if unit == MassFlowUnits.NanogramPerDay:
            return f"""{super()._truncate_fraction_digits(self.nanograms_per_day, fractional_digits)} ng/d"""
        
        if unit == MassFlowUnits.MicrogramPerDay:
            return f"""{super()._truncate_fraction_digits(self.micrograms_per_day, fractional_digits)} μg/d"""
        
        if unit == MassFlowUnits.MilligramPerDay:
            return f"""{super()._truncate_fraction_digits(self.milligrams_per_day, fractional_digits)} mg/d"""
        
        if unit == MassFlowUnits.CentigramPerDay:
            return f"""{super()._truncate_fraction_digits(self.centigrams_per_day, fractional_digits)} cg/d"""
        
        if unit == MassFlowUnits.DecigramPerDay:
            return f"""{super()._truncate_fraction_digits(self.decigrams_per_day, fractional_digits)} dg/d"""
        
        if unit == MassFlowUnits.DecagramPerDay:
            return f"""{super()._truncate_fraction_digits(self.decagrams_per_day, fractional_digits)} dag/d"""
        
        if unit == MassFlowUnits.HectogramPerDay:
            return f"""{super()._truncate_fraction_digits(self.hectograms_per_day, fractional_digits)} hg/d"""
        
        if unit == MassFlowUnits.KilogramPerDay:
            return f"""{super()._truncate_fraction_digits(self.kilograms_per_day, fractional_digits)} kg/d"""
        
        if unit == MassFlowUnits.MegagramPerDay:
            return f"""{super()._truncate_fraction_digits(self.megagrams_per_day, fractional_digits)} Mg/d"""
        
        if unit == MassFlowUnits.MegapoundPerDay:
            return f"""{super()._truncate_fraction_digits(self.megapounds_per_day, fractional_digits)} Mlb/d"""
        
        if unit == MassFlowUnits.MegapoundPerHour:
            return f"""{super()._truncate_fraction_digits(self.megapounds_per_hour, fractional_digits)} Mlb/h"""
        
        if unit == MassFlowUnits.MegapoundPerMinute:
            return f"""{super()._truncate_fraction_digits(self.megapounds_per_minute, fractional_digits)} Mlb/min"""
        
        if unit == MassFlowUnits.MegapoundPerSecond:
            return f"""{super()._truncate_fraction_digits(self.megapounds_per_second, fractional_digits)} Mlb/s"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: MassFlowUnits = MassFlowUnits.GramPerSecond) -> str:
        """
        Get MassFlow unit abbreviation.
        Note! the default abbreviation for MassFlow is GramPerSecond.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == MassFlowUnits.GramPerSecond:
            return """g/s"""
        
        if unit_abbreviation == MassFlowUnits.GramPerDay:
            return """g/d"""
        
        if unit_abbreviation == MassFlowUnits.GramPerHour:
            return """g/h"""
        
        if unit_abbreviation == MassFlowUnits.KilogramPerHour:
            return """kg/h"""
        
        if unit_abbreviation == MassFlowUnits.KilogramPerMinute:
            return """kg/min"""
        
        if unit_abbreviation == MassFlowUnits.TonnePerHour:
            return """t/h"""
        
        if unit_abbreviation == MassFlowUnits.PoundPerDay:
            return """lb/d"""
        
        if unit_abbreviation == MassFlowUnits.PoundPerHour:
            return """lb/h"""
        
        if unit_abbreviation == MassFlowUnits.PoundPerMinute:
            return """lb/min"""
        
        if unit_abbreviation == MassFlowUnits.PoundPerSecond:
            return """lb/s"""
        
        if unit_abbreviation == MassFlowUnits.TonnePerDay:
            return """t/d"""
        
        if unit_abbreviation == MassFlowUnits.ShortTonPerHour:
            return """short tn/h"""
        
        if unit_abbreviation == MassFlowUnits.NanogramPerSecond:
            return """ng/s"""
        
        if unit_abbreviation == MassFlowUnits.MicrogramPerSecond:
            return """μg/s"""
        
        if unit_abbreviation == MassFlowUnits.MilligramPerSecond:
            return """mg/s"""
        
        if unit_abbreviation == MassFlowUnits.CentigramPerSecond:
            return """cg/s"""
        
        if unit_abbreviation == MassFlowUnits.DecigramPerSecond:
            return """dg/s"""
        
        if unit_abbreviation == MassFlowUnits.DecagramPerSecond:
            return """dag/s"""
        
        if unit_abbreviation == MassFlowUnits.HectogramPerSecond:
            return """hg/s"""
        
        if unit_abbreviation == MassFlowUnits.KilogramPerSecond:
            return """kg/s"""
        
        if unit_abbreviation == MassFlowUnits.NanogramPerDay:
            return """ng/d"""
        
        if unit_abbreviation == MassFlowUnits.MicrogramPerDay:
            return """μg/d"""
        
        if unit_abbreviation == MassFlowUnits.MilligramPerDay:
            return """mg/d"""
        
        if unit_abbreviation == MassFlowUnits.CentigramPerDay:
            return """cg/d"""
        
        if unit_abbreviation == MassFlowUnits.DecigramPerDay:
            return """dg/d"""
        
        if unit_abbreviation == MassFlowUnits.DecagramPerDay:
            return """dag/d"""
        
        if unit_abbreviation == MassFlowUnits.HectogramPerDay:
            return """hg/d"""
        
        if unit_abbreviation == MassFlowUnits.KilogramPerDay:
            return """kg/d"""
        
        if unit_abbreviation == MassFlowUnits.MegagramPerDay:
            return """Mg/d"""
        
        if unit_abbreviation == MassFlowUnits.MegapoundPerDay:
            return """Mlb/d"""
        
        if unit_abbreviation == MassFlowUnits.MegapoundPerHour:
            return """Mlb/h"""
        
        if unit_abbreviation == MassFlowUnits.MegapoundPerMinute:
            return """Mlb/min"""
        
        if unit_abbreviation == MassFlowUnits.MegapoundPerSecond:
            return """Mlb/s"""
        
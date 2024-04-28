from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class MolarFlowUnits(Enum):
        """
            MolarFlowUnits enumeration
        """
        
        MolePerSecond = 'MolePerSecond'
        """
            
        """
        
        MolePerMinute = 'MolePerMinute'
        """
            
        """
        
        MolePerHour = 'MolePerHour'
        """
            
        """
        
        PoundMolePerSecond = 'PoundMolePerSecond'
        """
            
        """
        
        PoundMolePerMinute = 'PoundMolePerMinute'
        """
            
        """
        
        PoundMolePerHour = 'PoundMolePerHour'
        """
            
        """
        
        KilomolePerSecond = 'KilomolePerSecond'
        """
            
        """
        
        KilomolePerMinute = 'KilomolePerMinute'
        """
            
        """
        
        KilomolePerHour = 'KilomolePerHour'
        """
            
        """
        

class MolarFlowDto:
    """
    A DTO representation of a MolarFlow

    Attributes:
        value (float): The value of the MolarFlow.
        unit (MolarFlowUnits): The specific unit that the MolarFlow value is representing.
    """

    def __init__(self, value: float, unit: MolarFlowUnits):
        """
        Create a new DTO representation of a MolarFlow

        Parameters:
            value (float): The value of the MolarFlow.
            unit (MolarFlowUnits): The specific unit that the MolarFlow value is representing.
        """
        self.value: float = value
        """
        The value of the MolarFlow
        """
        self.unit: MolarFlowUnits = unit
        """
        The specific unit that the MolarFlow value is representing
        """

    def to_json(self):
        """
        Get a MolarFlow DTO JSON object representing the current unit.

        :return: JSON object represents MolarFlow DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "MolePerSecond"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of MolarFlow DTO from a json representation.

        :param data: The MolarFlow DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "MolePerSecond"}
        :return: A new instance of MolarFlowDto.
        :rtype: MolarFlowDto
        """
        return MolarFlowDto(value=data["value"], unit=MolarFlowUnits(data["unit"]))


class MolarFlow(AbstractMeasure):
    """
    Molar flow is the ratio of the amount of substance change to the time during which the change occurred (value of amount of substance changes per unit time).

    Args:
        value (float): The value.
        from_unit (MolarFlowUnits): The MolarFlow unit to create from, The default unit is MolePerSecond
    """
    def __init__(self, value: float, from_unit: MolarFlowUnits = MolarFlowUnits.MolePerSecond):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__moles_per_second = None
        
        self.__moles_per_minute = None
        
        self.__moles_per_hour = None
        
        self.__pound_moles_per_second = None
        
        self.__pound_moles_per_minute = None
        
        self.__pound_moles_per_hour = None
        
        self.__kilomoles_per_second = None
        
        self.__kilomoles_per_minute = None
        
        self.__kilomoles_per_hour = None
        

    def convert(self, unit: MolarFlowUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: MolarFlowUnits = MolarFlowUnits.MolePerSecond) -> MolarFlowDto:
        """
        Get a new instance of MolarFlow DTO representing the current unit.

        :param hold_in_unit: The specific MolarFlow unit to store the MolarFlow value in the DTO representation.
        :type hold_in_unit: MolarFlowUnits
        :return: A new instance of MolarFlowDto.
        :rtype: MolarFlowDto
        """
        return MolarFlowDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: MolarFlowUnits = MolarFlowUnits.MolePerSecond):
        """
        Get a MolarFlow DTO JSON object representing the current unit.

        :param hold_in_unit: The specific MolarFlow unit to store the MolarFlow value in the DTO representation.
        :type hold_in_unit: MolarFlowUnits
        :return: JSON object represents MolarFlow DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "MolePerSecond"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(molar_flow_dto: MolarFlowDto):
        """
        Obtain a new instance of MolarFlow from a DTO unit object.

        :param molar_flow_dto: The MolarFlow DTO representation.
        :type molar_flow_dto: MolarFlowDto
        :return: A new instance of MolarFlow.
        :rtype: MolarFlow
        """
        return MolarFlow(molar_flow_dto.value, molar_flow_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of MolarFlow from a DTO unit json representation.

        :param data: The MolarFlow DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "MolePerSecond"}
        :return: A new instance of MolarFlow.
        :rtype: MolarFlow
        """
        return MolarFlow.from_dto(MolarFlowDto.from_json(data))

    def __convert_from_base(self, from_unit: MolarFlowUnits) -> float:
        value = self._value
        
        if from_unit == MolarFlowUnits.MolePerSecond:
            return (value)
        
        if from_unit == MolarFlowUnits.MolePerMinute:
            return (value * 60)
        
        if from_unit == MolarFlowUnits.MolePerHour:
            return (value * 3600)
        
        if from_unit == MolarFlowUnits.PoundMolePerSecond:
            return (value / 453.59237)
        
        if from_unit == MolarFlowUnits.PoundMolePerMinute:
            return ((value / 453.59237) * 60)
        
        if from_unit == MolarFlowUnits.PoundMolePerHour:
            return ((value / 453.59237) * 3600)
        
        if from_unit == MolarFlowUnits.KilomolePerSecond:
            return ((value) / 1000.0)
        
        if from_unit == MolarFlowUnits.KilomolePerMinute:
            return ((value * 60) / 1000.0)
        
        if from_unit == MolarFlowUnits.KilomolePerHour:
            return ((value * 3600) / 1000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: MolarFlowUnits) -> float:
        
        if to_unit == MolarFlowUnits.MolePerSecond:
            return (value)
        
        if to_unit == MolarFlowUnits.MolePerMinute:
            return (value / 60)
        
        if to_unit == MolarFlowUnits.MolePerHour:
            return (value / 3600)
        
        if to_unit == MolarFlowUnits.PoundMolePerSecond:
            return (value * 453.59237)
        
        if to_unit == MolarFlowUnits.PoundMolePerMinute:
            return ((value * 453.59237) / 60)
        
        if to_unit == MolarFlowUnits.PoundMolePerHour:
            return ((value * 453.59237) / 3600)
        
        if to_unit == MolarFlowUnits.KilomolePerSecond:
            return ((value) * 1000.0)
        
        if to_unit == MolarFlowUnits.KilomolePerMinute:
            return ((value / 60) * 1000.0)
        
        if to_unit == MolarFlowUnits.KilomolePerHour:
            return ((value / 3600) * 1000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_moles_per_second(moles_per_second: float):
        """
        Create a new instance of MolarFlow from a value in moles_per_second.

        

        :param meters: The MolarFlow value in moles_per_second.
        :type moles_per_second: float
        :return: A new instance of MolarFlow.
        :rtype: MolarFlow
        """
        return MolarFlow(moles_per_second, MolarFlowUnits.MolePerSecond)

    
    @staticmethod
    def from_moles_per_minute(moles_per_minute: float):
        """
        Create a new instance of MolarFlow from a value in moles_per_minute.

        

        :param meters: The MolarFlow value in moles_per_minute.
        :type moles_per_minute: float
        :return: A new instance of MolarFlow.
        :rtype: MolarFlow
        """
        return MolarFlow(moles_per_minute, MolarFlowUnits.MolePerMinute)

    
    @staticmethod
    def from_moles_per_hour(moles_per_hour: float):
        """
        Create a new instance of MolarFlow from a value in moles_per_hour.

        

        :param meters: The MolarFlow value in moles_per_hour.
        :type moles_per_hour: float
        :return: A new instance of MolarFlow.
        :rtype: MolarFlow
        """
        return MolarFlow(moles_per_hour, MolarFlowUnits.MolePerHour)

    
    @staticmethod
    def from_pound_moles_per_second(pound_moles_per_second: float):
        """
        Create a new instance of MolarFlow from a value in pound_moles_per_second.

        

        :param meters: The MolarFlow value in pound_moles_per_second.
        :type pound_moles_per_second: float
        :return: A new instance of MolarFlow.
        :rtype: MolarFlow
        """
        return MolarFlow(pound_moles_per_second, MolarFlowUnits.PoundMolePerSecond)

    
    @staticmethod
    def from_pound_moles_per_minute(pound_moles_per_minute: float):
        """
        Create a new instance of MolarFlow from a value in pound_moles_per_minute.

        

        :param meters: The MolarFlow value in pound_moles_per_minute.
        :type pound_moles_per_minute: float
        :return: A new instance of MolarFlow.
        :rtype: MolarFlow
        """
        return MolarFlow(pound_moles_per_minute, MolarFlowUnits.PoundMolePerMinute)

    
    @staticmethod
    def from_pound_moles_per_hour(pound_moles_per_hour: float):
        """
        Create a new instance of MolarFlow from a value in pound_moles_per_hour.

        

        :param meters: The MolarFlow value in pound_moles_per_hour.
        :type pound_moles_per_hour: float
        :return: A new instance of MolarFlow.
        :rtype: MolarFlow
        """
        return MolarFlow(pound_moles_per_hour, MolarFlowUnits.PoundMolePerHour)

    
    @staticmethod
    def from_kilomoles_per_second(kilomoles_per_second: float):
        """
        Create a new instance of MolarFlow from a value in kilomoles_per_second.

        

        :param meters: The MolarFlow value in kilomoles_per_second.
        :type kilomoles_per_second: float
        :return: A new instance of MolarFlow.
        :rtype: MolarFlow
        """
        return MolarFlow(kilomoles_per_second, MolarFlowUnits.KilomolePerSecond)

    
    @staticmethod
    def from_kilomoles_per_minute(kilomoles_per_minute: float):
        """
        Create a new instance of MolarFlow from a value in kilomoles_per_minute.

        

        :param meters: The MolarFlow value in kilomoles_per_minute.
        :type kilomoles_per_minute: float
        :return: A new instance of MolarFlow.
        :rtype: MolarFlow
        """
        return MolarFlow(kilomoles_per_minute, MolarFlowUnits.KilomolePerMinute)

    
    @staticmethod
    def from_kilomoles_per_hour(kilomoles_per_hour: float):
        """
        Create a new instance of MolarFlow from a value in kilomoles_per_hour.

        

        :param meters: The MolarFlow value in kilomoles_per_hour.
        :type kilomoles_per_hour: float
        :return: A new instance of MolarFlow.
        :rtype: MolarFlow
        """
        return MolarFlow(kilomoles_per_hour, MolarFlowUnits.KilomolePerHour)

    
    @property
    def moles_per_second(self) -> float:
        """
        
        """
        if self.__moles_per_second != None:
            return self.__moles_per_second
        self.__moles_per_second = self.__convert_from_base(MolarFlowUnits.MolePerSecond)
        return self.__moles_per_second

    
    @property
    def moles_per_minute(self) -> float:
        """
        
        """
        if self.__moles_per_minute != None:
            return self.__moles_per_minute
        self.__moles_per_minute = self.__convert_from_base(MolarFlowUnits.MolePerMinute)
        return self.__moles_per_minute

    
    @property
    def moles_per_hour(self) -> float:
        """
        
        """
        if self.__moles_per_hour != None:
            return self.__moles_per_hour
        self.__moles_per_hour = self.__convert_from_base(MolarFlowUnits.MolePerHour)
        return self.__moles_per_hour

    
    @property
    def pound_moles_per_second(self) -> float:
        """
        
        """
        if self.__pound_moles_per_second != None:
            return self.__pound_moles_per_second
        self.__pound_moles_per_second = self.__convert_from_base(MolarFlowUnits.PoundMolePerSecond)
        return self.__pound_moles_per_second

    
    @property
    def pound_moles_per_minute(self) -> float:
        """
        
        """
        if self.__pound_moles_per_minute != None:
            return self.__pound_moles_per_minute
        self.__pound_moles_per_minute = self.__convert_from_base(MolarFlowUnits.PoundMolePerMinute)
        return self.__pound_moles_per_minute

    
    @property
    def pound_moles_per_hour(self) -> float:
        """
        
        """
        if self.__pound_moles_per_hour != None:
            return self.__pound_moles_per_hour
        self.__pound_moles_per_hour = self.__convert_from_base(MolarFlowUnits.PoundMolePerHour)
        return self.__pound_moles_per_hour

    
    @property
    def kilomoles_per_second(self) -> float:
        """
        
        """
        if self.__kilomoles_per_second != None:
            return self.__kilomoles_per_second
        self.__kilomoles_per_second = self.__convert_from_base(MolarFlowUnits.KilomolePerSecond)
        return self.__kilomoles_per_second

    
    @property
    def kilomoles_per_minute(self) -> float:
        """
        
        """
        if self.__kilomoles_per_minute != None:
            return self.__kilomoles_per_minute
        self.__kilomoles_per_minute = self.__convert_from_base(MolarFlowUnits.KilomolePerMinute)
        return self.__kilomoles_per_minute

    
    @property
    def kilomoles_per_hour(self) -> float:
        """
        
        """
        if self.__kilomoles_per_hour != None:
            return self.__kilomoles_per_hour
        self.__kilomoles_per_hour = self.__convert_from_base(MolarFlowUnits.KilomolePerHour)
        return self.__kilomoles_per_hour

    
    def to_string(self, unit: MolarFlowUnits = MolarFlowUnits.MolePerSecond, fractional_digits: int = None) -> str:
        """
        Format the MolarFlow to a string.
        
        Note: the default format for MolarFlow is MolePerSecond.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the MolarFlow. Default is 'MolePerSecond'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == MolarFlowUnits.MolePerSecond:
            return f"""{super()._truncate_fraction_digits(self.moles_per_second, fractional_digits)} mol/s"""
        
        if unit == MolarFlowUnits.MolePerMinute:
            return f"""{super()._truncate_fraction_digits(self.moles_per_minute, fractional_digits)} mol/min"""
        
        if unit == MolarFlowUnits.MolePerHour:
            return f"""{super()._truncate_fraction_digits(self.moles_per_hour, fractional_digits)} kmol/h"""
        
        if unit == MolarFlowUnits.PoundMolePerSecond:
            return f"""{super()._truncate_fraction_digits(self.pound_moles_per_second, fractional_digits)} lbmol/s"""
        
        if unit == MolarFlowUnits.PoundMolePerMinute:
            return f"""{super()._truncate_fraction_digits(self.pound_moles_per_minute, fractional_digits)} lbmol/min"""
        
        if unit == MolarFlowUnits.PoundMolePerHour:
            return f"""{super()._truncate_fraction_digits(self.pound_moles_per_hour, fractional_digits)} lbmol/h"""
        
        if unit == MolarFlowUnits.KilomolePerSecond:
            return f"""{super()._truncate_fraction_digits(self.kilomoles_per_second, fractional_digits)} kmol/s"""
        
        if unit == MolarFlowUnits.KilomolePerMinute:
            return f"""{super()._truncate_fraction_digits(self.kilomoles_per_minute, fractional_digits)} kmol/min"""
        
        if unit == MolarFlowUnits.KilomolePerHour:
            return f"""{super()._truncate_fraction_digits(self.kilomoles_per_hour, fractional_digits)} kkmol/h"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: MolarFlowUnits = MolarFlowUnits.MolePerSecond) -> str:
        """
        Get MolarFlow unit abbreviation.
        Note! the default abbreviation for MolarFlow is MolePerSecond.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == MolarFlowUnits.MolePerSecond:
            return """mol/s"""
        
        if unit_abbreviation == MolarFlowUnits.MolePerMinute:
            return """mol/min"""
        
        if unit_abbreviation == MolarFlowUnits.MolePerHour:
            return """kmol/h"""
        
        if unit_abbreviation == MolarFlowUnits.PoundMolePerSecond:
            return """lbmol/s"""
        
        if unit_abbreviation == MolarFlowUnits.PoundMolePerMinute:
            return """lbmol/min"""
        
        if unit_abbreviation == MolarFlowUnits.PoundMolePerHour:
            return """lbmol/h"""
        
        if unit_abbreviation == MolarFlowUnits.KilomolePerSecond:
            return """kmol/s"""
        
        if unit_abbreviation == MolarFlowUnits.KilomolePerMinute:
            return """kmol/min"""
        
        if unit_abbreviation == MolarFlowUnits.KilomolePerHour:
            return """kkmol/h"""
        
from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class BrakeSpecificFuelConsumptionUnits(Enum):
        """
            BrakeSpecificFuelConsumptionUnits enumeration
        """
        
        GramPerKiloWattHour = 'GramPerKiloWattHour'
        """
            
        """
        
        KilogramPerJoule = 'KilogramPerJoule'
        """
            
        """
        
        PoundPerMechanicalHorsepowerHour = 'PoundPerMechanicalHorsepowerHour'
        """
            The pound per horse power hour uses mechanical horse power and the imperial pound
        """
        

class BrakeSpecificFuelConsumptionDto:
    """
    A DTO representation of a BrakeSpecificFuelConsumption

    Attributes:
        value (float): The value of the BrakeSpecificFuelConsumption.
        unit (BrakeSpecificFuelConsumptionUnits): The specific unit that the BrakeSpecificFuelConsumption value is representing.
    """

    def __init__(self, value: float, unit: BrakeSpecificFuelConsumptionUnits):
        """
        Create a new DTO representation of a BrakeSpecificFuelConsumption

        Parameters:
            value (float): The value of the BrakeSpecificFuelConsumption.
            unit (BrakeSpecificFuelConsumptionUnits): The specific unit that the BrakeSpecificFuelConsumption value is representing.
        """
        self.value: float = value
        """
        The value of the BrakeSpecificFuelConsumption
        """
        self.unit: BrakeSpecificFuelConsumptionUnits = unit
        """
        The specific unit that the BrakeSpecificFuelConsumption value is representing
        """

    def to_json(self):
        """
        Get a BrakeSpecificFuelConsumption DTO JSON object representing the current unit.

        :return: JSON object represents BrakeSpecificFuelConsumption DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "KilogramPerJoule"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of BrakeSpecificFuelConsumption DTO from a json representation.

        :param data: The BrakeSpecificFuelConsumption DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "KilogramPerJoule"}
        :return: A new instance of BrakeSpecificFuelConsumptionDto.
        :rtype: BrakeSpecificFuelConsumptionDto
        """
        return BrakeSpecificFuelConsumptionDto(value=data["value"], unit=BrakeSpecificFuelConsumptionUnits(data["unit"]))


class BrakeSpecificFuelConsumption(AbstractMeasure):
    """
    Brake specific fuel consumption (BSFC) is a measure of the fuel efficiency of any prime mover that burns fuel and produces rotational, or shaft, power. It is typically used for comparing the efficiency of internal combustion engines with a shaft output.

    Args:
        value (float): The value.
        from_unit (BrakeSpecificFuelConsumptionUnits): The BrakeSpecificFuelConsumption unit to create from, The default unit is KilogramPerJoule
    """
    def __init__(self, value: float, from_unit: BrakeSpecificFuelConsumptionUnits = BrakeSpecificFuelConsumptionUnits.KilogramPerJoule):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__grams_per_kilo_watt_hour = None
        
        self.__kilograms_per_joule = None
        
        self.__pounds_per_mechanical_horsepower_hour = None
        

    def convert(self, unit: BrakeSpecificFuelConsumptionUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: BrakeSpecificFuelConsumptionUnits = BrakeSpecificFuelConsumptionUnits.KilogramPerJoule) -> BrakeSpecificFuelConsumptionDto:
        """
        Get a new instance of BrakeSpecificFuelConsumption DTO representing the current unit.

        :param hold_in_unit: The specific BrakeSpecificFuelConsumption unit to store the BrakeSpecificFuelConsumption value in the DTO representation.
        :type hold_in_unit: BrakeSpecificFuelConsumptionUnits
        :return: A new instance of BrakeSpecificFuelConsumptionDto.
        :rtype: BrakeSpecificFuelConsumptionDto
        """
        return BrakeSpecificFuelConsumptionDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: BrakeSpecificFuelConsumptionUnits = BrakeSpecificFuelConsumptionUnits.KilogramPerJoule):
        """
        Get a BrakeSpecificFuelConsumption DTO JSON object representing the current unit.

        :param hold_in_unit: The specific BrakeSpecificFuelConsumption unit to store the BrakeSpecificFuelConsumption value in the DTO representation.
        :type hold_in_unit: BrakeSpecificFuelConsumptionUnits
        :return: JSON object represents BrakeSpecificFuelConsumption DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "KilogramPerJoule"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(brake_specific_fuel_consumption_dto: BrakeSpecificFuelConsumptionDto):
        """
        Obtain a new instance of BrakeSpecificFuelConsumption from a DTO unit object.

        :param brake_specific_fuel_consumption_dto: The BrakeSpecificFuelConsumption DTO representation.
        :type brake_specific_fuel_consumption_dto: BrakeSpecificFuelConsumptionDto
        :return: A new instance of BrakeSpecificFuelConsumption.
        :rtype: BrakeSpecificFuelConsumption
        """
        return BrakeSpecificFuelConsumption(brake_specific_fuel_consumption_dto.value, brake_specific_fuel_consumption_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of BrakeSpecificFuelConsumption from a DTO unit json representation.

        :param data: The BrakeSpecificFuelConsumption DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "KilogramPerJoule"}
        :return: A new instance of BrakeSpecificFuelConsumption.
        :rtype: BrakeSpecificFuelConsumption
        """
        return BrakeSpecificFuelConsumption.from_dto(BrakeSpecificFuelConsumptionDto.from_json(data))

    def __convert_from_base(self, from_unit: BrakeSpecificFuelConsumptionUnits) -> float:
        value = self._value
        
        if from_unit == BrakeSpecificFuelConsumptionUnits.GramPerKiloWattHour:
            return (value * 3.6e9)
        
        if from_unit == BrakeSpecificFuelConsumptionUnits.KilogramPerJoule:
            return (value)
        
        if from_unit == BrakeSpecificFuelConsumptionUnits.PoundPerMechanicalHorsepowerHour:
            return (value / 1.689659410672e-7)
        
        return None


    def __convert_to_base(self, value: float, to_unit: BrakeSpecificFuelConsumptionUnits) -> float:
        
        if to_unit == BrakeSpecificFuelConsumptionUnits.GramPerKiloWattHour:
            return (value / 3.6e9)
        
        if to_unit == BrakeSpecificFuelConsumptionUnits.KilogramPerJoule:
            return (value)
        
        if to_unit == BrakeSpecificFuelConsumptionUnits.PoundPerMechanicalHorsepowerHour:
            return (value * 1.689659410672e-7)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_grams_per_kilo_watt_hour(grams_per_kilo_watt_hour: float):
        """
        Create a new instance of BrakeSpecificFuelConsumption from a value in grams_per_kilo_watt_hour.

        

        :param meters: The BrakeSpecificFuelConsumption value in grams_per_kilo_watt_hour.
        :type grams_per_kilo_watt_hour: float
        :return: A new instance of BrakeSpecificFuelConsumption.
        :rtype: BrakeSpecificFuelConsumption
        """
        return BrakeSpecificFuelConsumption(grams_per_kilo_watt_hour, BrakeSpecificFuelConsumptionUnits.GramPerKiloWattHour)

    
    @staticmethod
    def from_kilograms_per_joule(kilograms_per_joule: float):
        """
        Create a new instance of BrakeSpecificFuelConsumption from a value in kilograms_per_joule.

        

        :param meters: The BrakeSpecificFuelConsumption value in kilograms_per_joule.
        :type kilograms_per_joule: float
        :return: A new instance of BrakeSpecificFuelConsumption.
        :rtype: BrakeSpecificFuelConsumption
        """
        return BrakeSpecificFuelConsumption(kilograms_per_joule, BrakeSpecificFuelConsumptionUnits.KilogramPerJoule)

    
    @staticmethod
    def from_pounds_per_mechanical_horsepower_hour(pounds_per_mechanical_horsepower_hour: float):
        """
        Create a new instance of BrakeSpecificFuelConsumption from a value in pounds_per_mechanical_horsepower_hour.

        The pound per horse power hour uses mechanical horse power and the imperial pound

        :param meters: The BrakeSpecificFuelConsumption value in pounds_per_mechanical_horsepower_hour.
        :type pounds_per_mechanical_horsepower_hour: float
        :return: A new instance of BrakeSpecificFuelConsumption.
        :rtype: BrakeSpecificFuelConsumption
        """
        return BrakeSpecificFuelConsumption(pounds_per_mechanical_horsepower_hour, BrakeSpecificFuelConsumptionUnits.PoundPerMechanicalHorsepowerHour)

    
    @property
    def grams_per_kilo_watt_hour(self) -> float:
        """
        
        """
        if self.__grams_per_kilo_watt_hour != None:
            return self.__grams_per_kilo_watt_hour
        self.__grams_per_kilo_watt_hour = self.__convert_from_base(BrakeSpecificFuelConsumptionUnits.GramPerKiloWattHour)
        return self.__grams_per_kilo_watt_hour

    
    @property
    def kilograms_per_joule(self) -> float:
        """
        
        """
        if self.__kilograms_per_joule != None:
            return self.__kilograms_per_joule
        self.__kilograms_per_joule = self.__convert_from_base(BrakeSpecificFuelConsumptionUnits.KilogramPerJoule)
        return self.__kilograms_per_joule

    
    @property
    def pounds_per_mechanical_horsepower_hour(self) -> float:
        """
        The pound per horse power hour uses mechanical horse power and the imperial pound
        """
        if self.__pounds_per_mechanical_horsepower_hour != None:
            return self.__pounds_per_mechanical_horsepower_hour
        self.__pounds_per_mechanical_horsepower_hour = self.__convert_from_base(BrakeSpecificFuelConsumptionUnits.PoundPerMechanicalHorsepowerHour)
        return self.__pounds_per_mechanical_horsepower_hour

    
    def to_string(self, unit: BrakeSpecificFuelConsumptionUnits = BrakeSpecificFuelConsumptionUnits.KilogramPerJoule, fractional_digits: int = None) -> str:
        """
        Format the BrakeSpecificFuelConsumption to a string.
        
        Note: the default format for BrakeSpecificFuelConsumption is KilogramPerJoule.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the BrakeSpecificFuelConsumption. Default is 'KilogramPerJoule'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == BrakeSpecificFuelConsumptionUnits.GramPerKiloWattHour:
            return f"""{super()._truncate_fraction_digits(self.grams_per_kilo_watt_hour, fractional_digits)} g/kWh"""
        
        if unit == BrakeSpecificFuelConsumptionUnits.KilogramPerJoule:
            return f"""{super()._truncate_fraction_digits(self.kilograms_per_joule, fractional_digits)} kg/J"""
        
        if unit == BrakeSpecificFuelConsumptionUnits.PoundPerMechanicalHorsepowerHour:
            return f"""{super()._truncate_fraction_digits(self.pounds_per_mechanical_horsepower_hour, fractional_digits)} lb/hph"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: BrakeSpecificFuelConsumptionUnits = BrakeSpecificFuelConsumptionUnits.KilogramPerJoule) -> str:
        """
        Get BrakeSpecificFuelConsumption unit abbreviation.
        Note! the default abbreviation for BrakeSpecificFuelConsumption is KilogramPerJoule.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == BrakeSpecificFuelConsumptionUnits.GramPerKiloWattHour:
            return """g/kWh"""
        
        if unit_abbreviation == BrakeSpecificFuelConsumptionUnits.KilogramPerJoule:
            return """kg/J"""
        
        if unit_abbreviation == BrakeSpecificFuelConsumptionUnits.PoundPerMechanicalHorsepowerHour:
            return """lb/hph"""
        
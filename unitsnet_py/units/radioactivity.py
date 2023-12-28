from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class RadioactivityUnits(Enum):
        """
            RadioactivityUnits enumeration
        """
        
        Becquerel = 'becquerel'
        """
            Activity of a quantity of radioactive material in which one nucleus decays per second.
        """
        
        Curie = 'curie'
        """
            
        """
        
        Rutherford = 'rutherford'
        """
            Activity of a quantity of radioactive material in which one million nuclei decay per second.
        """
        
        Picobecquerel = 'picobecquerel'
        """
            
        """
        
        Nanobecquerel = 'nanobecquerel'
        """
            
        """
        
        Microbecquerel = 'microbecquerel'
        """
            
        """
        
        Millibecquerel = 'millibecquerel'
        """
            
        """
        
        Kilobecquerel = 'kilobecquerel'
        """
            
        """
        
        Megabecquerel = 'megabecquerel'
        """
            
        """
        
        Gigabecquerel = 'gigabecquerel'
        """
            
        """
        
        Terabecquerel = 'terabecquerel'
        """
            
        """
        
        Petabecquerel = 'petabecquerel'
        """
            
        """
        
        Exabecquerel = 'exabecquerel'
        """
            
        """
        
        Picocurie = 'picocurie'
        """
            
        """
        
        Nanocurie = 'nanocurie'
        """
            
        """
        
        Microcurie = 'microcurie'
        """
            
        """
        
        Millicurie = 'millicurie'
        """
            
        """
        
        Kilocurie = 'kilocurie'
        """
            
        """
        
        Megacurie = 'megacurie'
        """
            
        """
        
        Gigacurie = 'gigacurie'
        """
            
        """
        
        Teracurie = 'teracurie'
        """
            
        """
        
        Picorutherford = 'picorutherford'
        """
            
        """
        
        Nanorutherford = 'nanorutherford'
        """
            
        """
        
        Microrutherford = 'microrutherford'
        """
            
        """
        
        Millirutherford = 'millirutherford'
        """
            
        """
        
        Kilorutherford = 'kilorutherford'
        """
            
        """
        
        Megarutherford = 'megarutherford'
        """
            
        """
        
        Gigarutherford = 'gigarutherford'
        """
            
        """
        
        Terarutherford = 'terarutherford'
        """
            
        """
        

class Radioactivity(AbstractMeasure):
    """
    Amount of ionizing radiation released when an element spontaneously emits energy as a result of the radioactive decay of an unstable atom per unit time.

    Args:
        value (float): The value.
        from_unit (RadioactivityUnits): The Radioactivity unit to create from, The default unit is Becquerel
    """
    def __init__(self, value: float, from_unit: RadioactivityUnits = RadioactivityUnits.Becquerel):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__becquerels = None
        
        self.__curies = None
        
        self.__rutherfords = None
        
        self.__picobecquerels = None
        
        self.__nanobecquerels = None
        
        self.__microbecquerels = None
        
        self.__millibecquerels = None
        
        self.__kilobecquerels = None
        
        self.__megabecquerels = None
        
        self.__gigabecquerels = None
        
        self.__terabecquerels = None
        
        self.__petabecquerels = None
        
        self.__exabecquerels = None
        
        self.__picocuries = None
        
        self.__nanocuries = None
        
        self.__microcuries = None
        
        self.__millicuries = None
        
        self.__kilocuries = None
        
        self.__megacuries = None
        
        self.__gigacuries = None
        
        self.__teracuries = None
        
        self.__picorutherfords = None
        
        self.__nanorutherfords = None
        
        self.__microrutherfords = None
        
        self.__millirutherfords = None
        
        self.__kilorutherfords = None
        
        self.__megarutherfords = None
        
        self.__gigarutherfords = None
        
        self.__terarutherfords = None
        

    def convert(self, unit: RadioactivityUnits) -> float:
        return self.__convert_from_base(unit)

    def __convert_from_base(self, from_unit: RadioactivityUnits) -> float:
        value = self._value
        
        if from_unit == RadioactivityUnits.Becquerel:
            return (value)
        
        if from_unit == RadioactivityUnits.Curie:
            return (value / 3.7e10)
        
        if from_unit == RadioactivityUnits.Rutherford:
            return (value / 1e6)
        
        if from_unit == RadioactivityUnits.Picobecquerel:
            return ((value) / 1e-12)
        
        if from_unit == RadioactivityUnits.Nanobecquerel:
            return ((value) / 1e-09)
        
        if from_unit == RadioactivityUnits.Microbecquerel:
            return ((value) / 1e-06)
        
        if from_unit == RadioactivityUnits.Millibecquerel:
            return ((value) / 0.001)
        
        if from_unit == RadioactivityUnits.Kilobecquerel:
            return ((value) / 1000.0)
        
        if from_unit == RadioactivityUnits.Megabecquerel:
            return ((value) / 1000000.0)
        
        if from_unit == RadioactivityUnits.Gigabecquerel:
            return ((value) / 1000000000.0)
        
        if from_unit == RadioactivityUnits.Terabecquerel:
            return ((value) / 1000000000000.0)
        
        if from_unit == RadioactivityUnits.Petabecquerel:
            return ((value) / 1000000000000000.0)
        
        if from_unit == RadioactivityUnits.Exabecquerel:
            return ((value) / 1e+18)
        
        if from_unit == RadioactivityUnits.Picocurie:
            return ((value / 3.7e10) / 1e-12)
        
        if from_unit == RadioactivityUnits.Nanocurie:
            return ((value / 3.7e10) / 1e-09)
        
        if from_unit == RadioactivityUnits.Microcurie:
            return ((value / 3.7e10) / 1e-06)
        
        if from_unit == RadioactivityUnits.Millicurie:
            return ((value / 3.7e10) / 0.001)
        
        if from_unit == RadioactivityUnits.Kilocurie:
            return ((value / 3.7e10) / 1000.0)
        
        if from_unit == RadioactivityUnits.Megacurie:
            return ((value / 3.7e10) / 1000000.0)
        
        if from_unit == RadioactivityUnits.Gigacurie:
            return ((value / 3.7e10) / 1000000000.0)
        
        if from_unit == RadioactivityUnits.Teracurie:
            return ((value / 3.7e10) / 1000000000000.0)
        
        if from_unit == RadioactivityUnits.Picorutherford:
            return ((value / 1e6) / 1e-12)
        
        if from_unit == RadioactivityUnits.Nanorutherford:
            return ((value / 1e6) / 1e-09)
        
        if from_unit == RadioactivityUnits.Microrutherford:
            return ((value / 1e6) / 1e-06)
        
        if from_unit == RadioactivityUnits.Millirutherford:
            return ((value / 1e6) / 0.001)
        
        if from_unit == RadioactivityUnits.Kilorutherford:
            return ((value / 1e6) / 1000.0)
        
        if from_unit == RadioactivityUnits.Megarutherford:
            return ((value / 1e6) / 1000000.0)
        
        if from_unit == RadioactivityUnits.Gigarutherford:
            return ((value / 1e6) / 1000000000.0)
        
        if from_unit == RadioactivityUnits.Terarutherford:
            return ((value / 1e6) / 1000000000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: RadioactivityUnits) -> float:
        
        if to_unit == RadioactivityUnits.Becquerel:
            return (value)
        
        if to_unit == RadioactivityUnits.Curie:
            return (value * 3.7e10)
        
        if to_unit == RadioactivityUnits.Rutherford:
            return (value * 1e6)
        
        if to_unit == RadioactivityUnits.Picobecquerel:
            return ((value) * 1e-12)
        
        if to_unit == RadioactivityUnits.Nanobecquerel:
            return ((value) * 1e-09)
        
        if to_unit == RadioactivityUnits.Microbecquerel:
            return ((value) * 1e-06)
        
        if to_unit == RadioactivityUnits.Millibecquerel:
            return ((value) * 0.001)
        
        if to_unit == RadioactivityUnits.Kilobecquerel:
            return ((value) * 1000.0)
        
        if to_unit == RadioactivityUnits.Megabecquerel:
            return ((value) * 1000000.0)
        
        if to_unit == RadioactivityUnits.Gigabecquerel:
            return ((value) * 1000000000.0)
        
        if to_unit == RadioactivityUnits.Terabecquerel:
            return ((value) * 1000000000000.0)
        
        if to_unit == RadioactivityUnits.Petabecquerel:
            return ((value) * 1000000000000000.0)
        
        if to_unit == RadioactivityUnits.Exabecquerel:
            return ((value) * 1e+18)
        
        if to_unit == RadioactivityUnits.Picocurie:
            return ((value * 3.7e10) * 1e-12)
        
        if to_unit == RadioactivityUnits.Nanocurie:
            return ((value * 3.7e10) * 1e-09)
        
        if to_unit == RadioactivityUnits.Microcurie:
            return ((value * 3.7e10) * 1e-06)
        
        if to_unit == RadioactivityUnits.Millicurie:
            return ((value * 3.7e10) * 0.001)
        
        if to_unit == RadioactivityUnits.Kilocurie:
            return ((value * 3.7e10) * 1000.0)
        
        if to_unit == RadioactivityUnits.Megacurie:
            return ((value * 3.7e10) * 1000000.0)
        
        if to_unit == RadioactivityUnits.Gigacurie:
            return ((value * 3.7e10) * 1000000000.0)
        
        if to_unit == RadioactivityUnits.Teracurie:
            return ((value * 3.7e10) * 1000000000000.0)
        
        if to_unit == RadioactivityUnits.Picorutherford:
            return ((value * 1e6) * 1e-12)
        
        if to_unit == RadioactivityUnits.Nanorutherford:
            return ((value * 1e6) * 1e-09)
        
        if to_unit == RadioactivityUnits.Microrutherford:
            return ((value * 1e6) * 1e-06)
        
        if to_unit == RadioactivityUnits.Millirutherford:
            return ((value * 1e6) * 0.001)
        
        if to_unit == RadioactivityUnits.Kilorutherford:
            return ((value * 1e6) * 1000.0)
        
        if to_unit == RadioactivityUnits.Megarutherford:
            return ((value * 1e6) * 1000000.0)
        
        if to_unit == RadioactivityUnits.Gigarutherford:
            return ((value * 1e6) * 1000000000.0)
        
        if to_unit == RadioactivityUnits.Terarutherford:
            return ((value * 1e6) * 1000000000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_becquerels(becquerels: float):
        """
        Create a new instance of Radioactivity from a value in becquerels.

        Activity of a quantity of radioactive material in which one nucleus decays per second.

        :param meters: The Radioactivity value in becquerels.
        :type becquerels: float
        :return: A new instance of Radioactivity.
        :rtype: Radioactivity
        """
        return Radioactivity(becquerels, RadioactivityUnits.Becquerel)

    
    @staticmethod
    def from_curies(curies: float):
        """
        Create a new instance of Radioactivity from a value in curies.

        

        :param meters: The Radioactivity value in curies.
        :type curies: float
        :return: A new instance of Radioactivity.
        :rtype: Radioactivity
        """
        return Radioactivity(curies, RadioactivityUnits.Curie)

    
    @staticmethod
    def from_rutherfords(rutherfords: float):
        """
        Create a new instance of Radioactivity from a value in rutherfords.

        Activity of a quantity of radioactive material in which one million nuclei decay per second.

        :param meters: The Radioactivity value in rutherfords.
        :type rutherfords: float
        :return: A new instance of Radioactivity.
        :rtype: Radioactivity
        """
        return Radioactivity(rutherfords, RadioactivityUnits.Rutherford)

    
    @staticmethod
    def from_picobecquerels(picobecquerels: float):
        """
        Create a new instance of Radioactivity from a value in picobecquerels.

        

        :param meters: The Radioactivity value in picobecquerels.
        :type picobecquerels: float
        :return: A new instance of Radioactivity.
        :rtype: Radioactivity
        """
        return Radioactivity(picobecquerels, RadioactivityUnits.Picobecquerel)

    
    @staticmethod
    def from_nanobecquerels(nanobecquerels: float):
        """
        Create a new instance of Radioactivity from a value in nanobecquerels.

        

        :param meters: The Radioactivity value in nanobecquerels.
        :type nanobecquerels: float
        :return: A new instance of Radioactivity.
        :rtype: Radioactivity
        """
        return Radioactivity(nanobecquerels, RadioactivityUnits.Nanobecquerel)

    
    @staticmethod
    def from_microbecquerels(microbecquerels: float):
        """
        Create a new instance of Radioactivity from a value in microbecquerels.

        

        :param meters: The Radioactivity value in microbecquerels.
        :type microbecquerels: float
        :return: A new instance of Radioactivity.
        :rtype: Radioactivity
        """
        return Radioactivity(microbecquerels, RadioactivityUnits.Microbecquerel)

    
    @staticmethod
    def from_millibecquerels(millibecquerels: float):
        """
        Create a new instance of Radioactivity from a value in millibecquerels.

        

        :param meters: The Radioactivity value in millibecquerels.
        :type millibecquerels: float
        :return: A new instance of Radioactivity.
        :rtype: Radioactivity
        """
        return Radioactivity(millibecquerels, RadioactivityUnits.Millibecquerel)

    
    @staticmethod
    def from_kilobecquerels(kilobecquerels: float):
        """
        Create a new instance of Radioactivity from a value in kilobecquerels.

        

        :param meters: The Radioactivity value in kilobecquerels.
        :type kilobecquerels: float
        :return: A new instance of Radioactivity.
        :rtype: Radioactivity
        """
        return Radioactivity(kilobecquerels, RadioactivityUnits.Kilobecquerel)

    
    @staticmethod
    def from_megabecquerels(megabecquerels: float):
        """
        Create a new instance of Radioactivity from a value in megabecquerels.

        

        :param meters: The Radioactivity value in megabecquerels.
        :type megabecquerels: float
        :return: A new instance of Radioactivity.
        :rtype: Radioactivity
        """
        return Radioactivity(megabecquerels, RadioactivityUnits.Megabecquerel)

    
    @staticmethod
    def from_gigabecquerels(gigabecquerels: float):
        """
        Create a new instance of Radioactivity from a value in gigabecquerels.

        

        :param meters: The Radioactivity value in gigabecquerels.
        :type gigabecquerels: float
        :return: A new instance of Radioactivity.
        :rtype: Radioactivity
        """
        return Radioactivity(gigabecquerels, RadioactivityUnits.Gigabecquerel)

    
    @staticmethod
    def from_terabecquerels(terabecquerels: float):
        """
        Create a new instance of Radioactivity from a value in terabecquerels.

        

        :param meters: The Radioactivity value in terabecquerels.
        :type terabecquerels: float
        :return: A new instance of Radioactivity.
        :rtype: Radioactivity
        """
        return Radioactivity(terabecquerels, RadioactivityUnits.Terabecquerel)

    
    @staticmethod
    def from_petabecquerels(petabecquerels: float):
        """
        Create a new instance of Radioactivity from a value in petabecquerels.

        

        :param meters: The Radioactivity value in petabecquerels.
        :type petabecquerels: float
        :return: A new instance of Radioactivity.
        :rtype: Radioactivity
        """
        return Radioactivity(petabecquerels, RadioactivityUnits.Petabecquerel)

    
    @staticmethod
    def from_exabecquerels(exabecquerels: float):
        """
        Create a new instance of Radioactivity from a value in exabecquerels.

        

        :param meters: The Radioactivity value in exabecquerels.
        :type exabecquerels: float
        :return: A new instance of Radioactivity.
        :rtype: Radioactivity
        """
        return Radioactivity(exabecquerels, RadioactivityUnits.Exabecquerel)

    
    @staticmethod
    def from_picocuries(picocuries: float):
        """
        Create a new instance of Radioactivity from a value in picocuries.

        

        :param meters: The Radioactivity value in picocuries.
        :type picocuries: float
        :return: A new instance of Radioactivity.
        :rtype: Radioactivity
        """
        return Radioactivity(picocuries, RadioactivityUnits.Picocurie)

    
    @staticmethod
    def from_nanocuries(nanocuries: float):
        """
        Create a new instance of Radioactivity from a value in nanocuries.

        

        :param meters: The Radioactivity value in nanocuries.
        :type nanocuries: float
        :return: A new instance of Radioactivity.
        :rtype: Radioactivity
        """
        return Radioactivity(nanocuries, RadioactivityUnits.Nanocurie)

    
    @staticmethod
    def from_microcuries(microcuries: float):
        """
        Create a new instance of Radioactivity from a value in microcuries.

        

        :param meters: The Radioactivity value in microcuries.
        :type microcuries: float
        :return: A new instance of Radioactivity.
        :rtype: Radioactivity
        """
        return Radioactivity(microcuries, RadioactivityUnits.Microcurie)

    
    @staticmethod
    def from_millicuries(millicuries: float):
        """
        Create a new instance of Radioactivity from a value in millicuries.

        

        :param meters: The Radioactivity value in millicuries.
        :type millicuries: float
        :return: A new instance of Radioactivity.
        :rtype: Radioactivity
        """
        return Radioactivity(millicuries, RadioactivityUnits.Millicurie)

    
    @staticmethod
    def from_kilocuries(kilocuries: float):
        """
        Create a new instance of Radioactivity from a value in kilocuries.

        

        :param meters: The Radioactivity value in kilocuries.
        :type kilocuries: float
        :return: A new instance of Radioactivity.
        :rtype: Radioactivity
        """
        return Radioactivity(kilocuries, RadioactivityUnits.Kilocurie)

    
    @staticmethod
    def from_megacuries(megacuries: float):
        """
        Create a new instance of Radioactivity from a value in megacuries.

        

        :param meters: The Radioactivity value in megacuries.
        :type megacuries: float
        :return: A new instance of Radioactivity.
        :rtype: Radioactivity
        """
        return Radioactivity(megacuries, RadioactivityUnits.Megacurie)

    
    @staticmethod
    def from_gigacuries(gigacuries: float):
        """
        Create a new instance of Radioactivity from a value in gigacuries.

        

        :param meters: The Radioactivity value in gigacuries.
        :type gigacuries: float
        :return: A new instance of Radioactivity.
        :rtype: Radioactivity
        """
        return Radioactivity(gigacuries, RadioactivityUnits.Gigacurie)

    
    @staticmethod
    def from_teracuries(teracuries: float):
        """
        Create a new instance of Radioactivity from a value in teracuries.

        

        :param meters: The Radioactivity value in teracuries.
        :type teracuries: float
        :return: A new instance of Radioactivity.
        :rtype: Radioactivity
        """
        return Radioactivity(teracuries, RadioactivityUnits.Teracurie)

    
    @staticmethod
    def from_picorutherfords(picorutherfords: float):
        """
        Create a new instance of Radioactivity from a value in picorutherfords.

        

        :param meters: The Radioactivity value in picorutherfords.
        :type picorutherfords: float
        :return: A new instance of Radioactivity.
        :rtype: Radioactivity
        """
        return Radioactivity(picorutherfords, RadioactivityUnits.Picorutherford)

    
    @staticmethod
    def from_nanorutherfords(nanorutherfords: float):
        """
        Create a new instance of Radioactivity from a value in nanorutherfords.

        

        :param meters: The Radioactivity value in nanorutherfords.
        :type nanorutherfords: float
        :return: A new instance of Radioactivity.
        :rtype: Radioactivity
        """
        return Radioactivity(nanorutherfords, RadioactivityUnits.Nanorutherford)

    
    @staticmethod
    def from_microrutherfords(microrutherfords: float):
        """
        Create a new instance of Radioactivity from a value in microrutherfords.

        

        :param meters: The Radioactivity value in microrutherfords.
        :type microrutherfords: float
        :return: A new instance of Radioactivity.
        :rtype: Radioactivity
        """
        return Radioactivity(microrutherfords, RadioactivityUnits.Microrutherford)

    
    @staticmethod
    def from_millirutherfords(millirutherfords: float):
        """
        Create a new instance of Radioactivity from a value in millirutherfords.

        

        :param meters: The Radioactivity value in millirutherfords.
        :type millirutherfords: float
        :return: A new instance of Radioactivity.
        :rtype: Radioactivity
        """
        return Radioactivity(millirutherfords, RadioactivityUnits.Millirutherford)

    
    @staticmethod
    def from_kilorutherfords(kilorutherfords: float):
        """
        Create a new instance of Radioactivity from a value in kilorutherfords.

        

        :param meters: The Radioactivity value in kilorutherfords.
        :type kilorutherfords: float
        :return: A new instance of Radioactivity.
        :rtype: Radioactivity
        """
        return Radioactivity(kilorutherfords, RadioactivityUnits.Kilorutherford)

    
    @staticmethod
    def from_megarutherfords(megarutherfords: float):
        """
        Create a new instance of Radioactivity from a value in megarutherfords.

        

        :param meters: The Radioactivity value in megarutherfords.
        :type megarutherfords: float
        :return: A new instance of Radioactivity.
        :rtype: Radioactivity
        """
        return Radioactivity(megarutherfords, RadioactivityUnits.Megarutherford)

    
    @staticmethod
    def from_gigarutherfords(gigarutherfords: float):
        """
        Create a new instance of Radioactivity from a value in gigarutherfords.

        

        :param meters: The Radioactivity value in gigarutherfords.
        :type gigarutherfords: float
        :return: A new instance of Radioactivity.
        :rtype: Radioactivity
        """
        return Radioactivity(gigarutherfords, RadioactivityUnits.Gigarutherford)

    
    @staticmethod
    def from_terarutherfords(terarutherfords: float):
        """
        Create a new instance of Radioactivity from a value in terarutherfords.

        

        :param meters: The Radioactivity value in terarutherfords.
        :type terarutherfords: float
        :return: A new instance of Radioactivity.
        :rtype: Radioactivity
        """
        return Radioactivity(terarutherfords, RadioactivityUnits.Terarutherford)

    
    @property
    def becquerels(self) -> float:
        """
        Activity of a quantity of radioactive material in which one nucleus decays per second.
        """
        if self.__becquerels != None:
            return self.__becquerels
        self.__becquerels = self.__convert_from_base(RadioactivityUnits.Becquerel)
        return self.__becquerels

    
    @property
    def curies(self) -> float:
        """
        
        """
        if self.__curies != None:
            return self.__curies
        self.__curies = self.__convert_from_base(RadioactivityUnits.Curie)
        return self.__curies

    
    @property
    def rutherfords(self) -> float:
        """
        Activity of a quantity of radioactive material in which one million nuclei decay per second.
        """
        if self.__rutherfords != None:
            return self.__rutherfords
        self.__rutherfords = self.__convert_from_base(RadioactivityUnits.Rutherford)
        return self.__rutherfords

    
    @property
    def picobecquerels(self) -> float:
        """
        
        """
        if self.__picobecquerels != None:
            return self.__picobecquerels
        self.__picobecquerels = self.__convert_from_base(RadioactivityUnits.Picobecquerel)
        return self.__picobecquerels

    
    @property
    def nanobecquerels(self) -> float:
        """
        
        """
        if self.__nanobecquerels != None:
            return self.__nanobecquerels
        self.__nanobecquerels = self.__convert_from_base(RadioactivityUnits.Nanobecquerel)
        return self.__nanobecquerels

    
    @property
    def microbecquerels(self) -> float:
        """
        
        """
        if self.__microbecquerels != None:
            return self.__microbecquerels
        self.__microbecquerels = self.__convert_from_base(RadioactivityUnits.Microbecquerel)
        return self.__microbecquerels

    
    @property
    def millibecquerels(self) -> float:
        """
        
        """
        if self.__millibecquerels != None:
            return self.__millibecquerels
        self.__millibecquerels = self.__convert_from_base(RadioactivityUnits.Millibecquerel)
        return self.__millibecquerels

    
    @property
    def kilobecquerels(self) -> float:
        """
        
        """
        if self.__kilobecquerels != None:
            return self.__kilobecquerels
        self.__kilobecquerels = self.__convert_from_base(RadioactivityUnits.Kilobecquerel)
        return self.__kilobecquerels

    
    @property
    def megabecquerels(self) -> float:
        """
        
        """
        if self.__megabecquerels != None:
            return self.__megabecquerels
        self.__megabecquerels = self.__convert_from_base(RadioactivityUnits.Megabecquerel)
        return self.__megabecquerels

    
    @property
    def gigabecquerels(self) -> float:
        """
        
        """
        if self.__gigabecquerels != None:
            return self.__gigabecquerels
        self.__gigabecquerels = self.__convert_from_base(RadioactivityUnits.Gigabecquerel)
        return self.__gigabecquerels

    
    @property
    def terabecquerels(self) -> float:
        """
        
        """
        if self.__terabecquerels != None:
            return self.__terabecquerels
        self.__terabecquerels = self.__convert_from_base(RadioactivityUnits.Terabecquerel)
        return self.__terabecquerels

    
    @property
    def petabecquerels(self) -> float:
        """
        
        """
        if self.__petabecquerels != None:
            return self.__petabecquerels
        self.__petabecquerels = self.__convert_from_base(RadioactivityUnits.Petabecquerel)
        return self.__petabecquerels

    
    @property
    def exabecquerels(self) -> float:
        """
        
        """
        if self.__exabecquerels != None:
            return self.__exabecquerels
        self.__exabecquerels = self.__convert_from_base(RadioactivityUnits.Exabecquerel)
        return self.__exabecquerels

    
    @property
    def picocuries(self) -> float:
        """
        
        """
        if self.__picocuries != None:
            return self.__picocuries
        self.__picocuries = self.__convert_from_base(RadioactivityUnits.Picocurie)
        return self.__picocuries

    
    @property
    def nanocuries(self) -> float:
        """
        
        """
        if self.__nanocuries != None:
            return self.__nanocuries
        self.__nanocuries = self.__convert_from_base(RadioactivityUnits.Nanocurie)
        return self.__nanocuries

    
    @property
    def microcuries(self) -> float:
        """
        
        """
        if self.__microcuries != None:
            return self.__microcuries
        self.__microcuries = self.__convert_from_base(RadioactivityUnits.Microcurie)
        return self.__microcuries

    
    @property
    def millicuries(self) -> float:
        """
        
        """
        if self.__millicuries != None:
            return self.__millicuries
        self.__millicuries = self.__convert_from_base(RadioactivityUnits.Millicurie)
        return self.__millicuries

    
    @property
    def kilocuries(self) -> float:
        """
        
        """
        if self.__kilocuries != None:
            return self.__kilocuries
        self.__kilocuries = self.__convert_from_base(RadioactivityUnits.Kilocurie)
        return self.__kilocuries

    
    @property
    def megacuries(self) -> float:
        """
        
        """
        if self.__megacuries != None:
            return self.__megacuries
        self.__megacuries = self.__convert_from_base(RadioactivityUnits.Megacurie)
        return self.__megacuries

    
    @property
    def gigacuries(self) -> float:
        """
        
        """
        if self.__gigacuries != None:
            return self.__gigacuries
        self.__gigacuries = self.__convert_from_base(RadioactivityUnits.Gigacurie)
        return self.__gigacuries

    
    @property
    def teracuries(self) -> float:
        """
        
        """
        if self.__teracuries != None:
            return self.__teracuries
        self.__teracuries = self.__convert_from_base(RadioactivityUnits.Teracurie)
        return self.__teracuries

    
    @property
    def picorutherfords(self) -> float:
        """
        
        """
        if self.__picorutherfords != None:
            return self.__picorutherfords
        self.__picorutherfords = self.__convert_from_base(RadioactivityUnits.Picorutherford)
        return self.__picorutherfords

    
    @property
    def nanorutherfords(self) -> float:
        """
        
        """
        if self.__nanorutherfords != None:
            return self.__nanorutherfords
        self.__nanorutherfords = self.__convert_from_base(RadioactivityUnits.Nanorutherford)
        return self.__nanorutherfords

    
    @property
    def microrutherfords(self) -> float:
        """
        
        """
        if self.__microrutherfords != None:
            return self.__microrutherfords
        self.__microrutherfords = self.__convert_from_base(RadioactivityUnits.Microrutherford)
        return self.__microrutherfords

    
    @property
    def millirutherfords(self) -> float:
        """
        
        """
        if self.__millirutherfords != None:
            return self.__millirutherfords
        self.__millirutherfords = self.__convert_from_base(RadioactivityUnits.Millirutherford)
        return self.__millirutherfords

    
    @property
    def kilorutherfords(self) -> float:
        """
        
        """
        if self.__kilorutherfords != None:
            return self.__kilorutherfords
        self.__kilorutherfords = self.__convert_from_base(RadioactivityUnits.Kilorutherford)
        return self.__kilorutherfords

    
    @property
    def megarutherfords(self) -> float:
        """
        
        """
        if self.__megarutherfords != None:
            return self.__megarutherfords
        self.__megarutherfords = self.__convert_from_base(RadioactivityUnits.Megarutherford)
        return self.__megarutherfords

    
    @property
    def gigarutherfords(self) -> float:
        """
        
        """
        if self.__gigarutherfords != None:
            return self.__gigarutherfords
        self.__gigarutherfords = self.__convert_from_base(RadioactivityUnits.Gigarutherford)
        return self.__gigarutherfords

    
    @property
    def terarutherfords(self) -> float:
        """
        
        """
        if self.__terarutherfords != None:
            return self.__terarutherfords
        self.__terarutherfords = self.__convert_from_base(RadioactivityUnits.Terarutherford)
        return self.__terarutherfords

    
    def to_string(self, unit: RadioactivityUnits = RadioactivityUnits.Becquerel) -> str:
        """
        Format the Radioactivity to string.
        Note! the default format for Radioactivity is Becquerel.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == RadioactivityUnits.Becquerel:
            return f"""{self.becquerels} Bq"""
        
        if unit == RadioactivityUnits.Curie:
            return f"""{self.curies} Ci"""
        
        if unit == RadioactivityUnits.Rutherford:
            return f"""{self.rutherfords} Rd"""
        
        if unit == RadioactivityUnits.Picobecquerel:
            return f"""{self.picobecquerels} pBq"""
        
        if unit == RadioactivityUnits.Nanobecquerel:
            return f"""{self.nanobecquerels} nBq"""
        
        if unit == RadioactivityUnits.Microbecquerel:
            return f"""{self.microbecquerels} μBq"""
        
        if unit == RadioactivityUnits.Millibecquerel:
            return f"""{self.millibecquerels} mBq"""
        
        if unit == RadioactivityUnits.Kilobecquerel:
            return f"""{self.kilobecquerels} kBq"""
        
        if unit == RadioactivityUnits.Megabecquerel:
            return f"""{self.megabecquerels} MBq"""
        
        if unit == RadioactivityUnits.Gigabecquerel:
            return f"""{self.gigabecquerels} GBq"""
        
        if unit == RadioactivityUnits.Terabecquerel:
            return f"""{self.terabecquerels} TBq"""
        
        if unit == RadioactivityUnits.Petabecquerel:
            return f"""{self.petabecquerels} PBq"""
        
        if unit == RadioactivityUnits.Exabecquerel:
            return f"""{self.exabecquerels} EBq"""
        
        if unit == RadioactivityUnits.Picocurie:
            return f"""{self.picocuries} pCi"""
        
        if unit == RadioactivityUnits.Nanocurie:
            return f"""{self.nanocuries} nCi"""
        
        if unit == RadioactivityUnits.Microcurie:
            return f"""{self.microcuries} μCi"""
        
        if unit == RadioactivityUnits.Millicurie:
            return f"""{self.millicuries} mCi"""
        
        if unit == RadioactivityUnits.Kilocurie:
            return f"""{self.kilocuries} kCi"""
        
        if unit == RadioactivityUnits.Megacurie:
            return f"""{self.megacuries} MCi"""
        
        if unit == RadioactivityUnits.Gigacurie:
            return f"""{self.gigacuries} GCi"""
        
        if unit == RadioactivityUnits.Teracurie:
            return f"""{self.teracuries} TCi"""
        
        if unit == RadioactivityUnits.Picorutherford:
            return f"""{self.picorutherfords} pRd"""
        
        if unit == RadioactivityUnits.Nanorutherford:
            return f"""{self.nanorutherfords} nRd"""
        
        if unit == RadioactivityUnits.Microrutherford:
            return f"""{self.microrutherfords} μRd"""
        
        if unit == RadioactivityUnits.Millirutherford:
            return f"""{self.millirutherfords} mRd"""
        
        if unit == RadioactivityUnits.Kilorutherford:
            return f"""{self.kilorutherfords} kRd"""
        
        if unit == RadioactivityUnits.Megarutherford:
            return f"""{self.megarutherfords} MRd"""
        
        if unit == RadioactivityUnits.Gigarutherford:
            return f"""{self.gigarutherfords} GRd"""
        
        if unit == RadioactivityUnits.Terarutherford:
            return f"""{self.terarutherfords} TRd"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: RadioactivityUnits = RadioactivityUnits.Becquerel) -> str:
        """
        Get Radioactivity unit abbreviation.
        Note! the default abbreviation for Radioactivity is Becquerel.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == RadioactivityUnits.Becquerel:
            return """Bq"""
        
        if unit_abbreviation == RadioactivityUnits.Curie:
            return """Ci"""
        
        if unit_abbreviation == RadioactivityUnits.Rutherford:
            return """Rd"""
        
        if unit_abbreviation == RadioactivityUnits.Picobecquerel:
            return """pBq"""
        
        if unit_abbreviation == RadioactivityUnits.Nanobecquerel:
            return """nBq"""
        
        if unit_abbreviation == RadioactivityUnits.Microbecquerel:
            return """μBq"""
        
        if unit_abbreviation == RadioactivityUnits.Millibecquerel:
            return """mBq"""
        
        if unit_abbreviation == RadioactivityUnits.Kilobecquerel:
            return """kBq"""
        
        if unit_abbreviation == RadioactivityUnits.Megabecquerel:
            return """MBq"""
        
        if unit_abbreviation == RadioactivityUnits.Gigabecquerel:
            return """GBq"""
        
        if unit_abbreviation == RadioactivityUnits.Terabecquerel:
            return """TBq"""
        
        if unit_abbreviation == RadioactivityUnits.Petabecquerel:
            return """PBq"""
        
        if unit_abbreviation == RadioactivityUnits.Exabecquerel:
            return """EBq"""
        
        if unit_abbreviation == RadioactivityUnits.Picocurie:
            return """pCi"""
        
        if unit_abbreviation == RadioactivityUnits.Nanocurie:
            return """nCi"""
        
        if unit_abbreviation == RadioactivityUnits.Microcurie:
            return """μCi"""
        
        if unit_abbreviation == RadioactivityUnits.Millicurie:
            return """mCi"""
        
        if unit_abbreviation == RadioactivityUnits.Kilocurie:
            return """kCi"""
        
        if unit_abbreviation == RadioactivityUnits.Megacurie:
            return """MCi"""
        
        if unit_abbreviation == RadioactivityUnits.Gigacurie:
            return """GCi"""
        
        if unit_abbreviation == RadioactivityUnits.Teracurie:
            return """TCi"""
        
        if unit_abbreviation == RadioactivityUnits.Picorutherford:
            return """pRd"""
        
        if unit_abbreviation == RadioactivityUnits.Nanorutherford:
            return """nRd"""
        
        if unit_abbreviation == RadioactivityUnits.Microrutherford:
            return """μRd"""
        
        if unit_abbreviation == RadioactivityUnits.Millirutherford:
            return """mRd"""
        
        if unit_abbreviation == RadioactivityUnits.Kilorutherford:
            return """kRd"""
        
        if unit_abbreviation == RadioactivityUnits.Megarutherford:
            return """MRd"""
        
        if unit_abbreviation == RadioactivityUnits.Gigarutherford:
            return """GRd"""
        
        if unit_abbreviation == RadioactivityUnits.Terarutherford:
            return """TRd"""
        
from dataclasses import dataclass

from core.enums.humidity_unit import HumidityUnit
from core.enums.length_unit import LengthUnit
from core.enums.luminosity_unit import LuminosityUnit
from core.enums.temperature_unit import TemperatureUnit
from core.enums.weight_unit import WeightUnit


@dataclass
class Units:
    weight: WeightUnit
    length: LengthUnit
    temperature: TemperatureUnit
    humidity: HumidityUnit
    luminosity: LuminosityUnit

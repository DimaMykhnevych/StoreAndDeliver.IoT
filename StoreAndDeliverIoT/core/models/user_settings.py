from dataclasses import dataclass
from core.constants.language import Language
from core.enums.temperature_unit import TemperatureUnit


@dataclass
class UserSettings:
    language: Language = Language.en
    temperature_unit: TemperatureUnit = TemperatureUnit.FAHRENHEIT

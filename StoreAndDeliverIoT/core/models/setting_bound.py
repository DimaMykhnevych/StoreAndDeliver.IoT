from dataclasses import dataclass


@dataclass
class SettingBound:
    setting: str
    minValue: float
    maxValue: float

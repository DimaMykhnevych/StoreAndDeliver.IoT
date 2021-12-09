from dataclasses import dataclass
from typing import List
from core.models.cargo_request import CargoRequest
from core.models.setting_bound import SettingBound


@dataclass
class Request:
    cargoRequests: List[CargoRequest]
    settingsBound: List[SettingBound]

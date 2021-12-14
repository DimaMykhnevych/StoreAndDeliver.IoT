from dataclasses import dataclass
from core.enums.request_type import RequestType


@dataclass
class AddSnapshot:
    temperature: float
    humidity: float
    luminosity: float
    requestType: RequestType

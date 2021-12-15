from dataclasses import dataclass
from core.constants.language import Language
from core.enums.request_status import RequestStatus
from core.enums.request_type import RequestType
from core.models.units import Units


@dataclass
class GetRequest:
    requestType: RequestType
    units: Units
    currentLanguage: Language
    status: RequestStatus

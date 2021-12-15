from enum import Enum


class RequestStatus(Enum):
    PENDING = 0
    IN_PROGRESS = 1
    REJECTED = 2
    COMPLETED = 3

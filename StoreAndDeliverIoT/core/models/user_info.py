from dataclasses import dataclass


@dataclass
class UserInfo:
    userId: str
    userName: str
    role: str
    registryDate: str
    email: str

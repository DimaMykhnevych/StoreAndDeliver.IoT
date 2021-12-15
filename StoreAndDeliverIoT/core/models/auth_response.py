from dataclasses import dataclass


@dataclass
class AuthResponse:
    token: str
    user_info = {}
    login_error_code: int
    is_authorized: bool = False

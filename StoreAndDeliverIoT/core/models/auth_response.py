from dataclasses import dataclass


@dataclass
class AuthResponse:
    is_authorized: bool
    token: str
    user_info = {}
    login_error_code: int

import requests
import json
from collections import namedtuple
from core.constants.settings import AppSettings
from core.models.auth_response import AuthResponse


class AuthService:
    @staticmethod
    def login(username, password):
        url = f"{AppSettings.api_host}/auth/token"
        data = {
            'username': username,
            'password': password
        }
        r = requests.post(url=url, json=data)
        x = json.loads(r.text, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
        AuthResponse.is_authorized = x.isAuthorized
        AuthResponse.token = x.token
        AuthResponse.user_info = x.userInfo
        AuthResponse.login_error_code = x.loginErrorCode

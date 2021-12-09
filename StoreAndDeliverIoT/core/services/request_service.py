import json
from pprint import pprint

import requests
from core.constants.settings import AppSettings
from core.models.auth_response import AuthResponse
from core.models.cargo_request import CargoRequest
from core.models.request import Request
from core.models.setting_bound import SettingBound


class RequestService:
    @staticmethod
    def get_active_requests():
        url = f"{AppSettings.api_host}/cargoSession/carrierSessionRequests"
        data = {
            "requestType": 1,
            "units": {
                "weight": 0,
                "length": 0,
                "temperature": 0,
                "humidity": 0,
                "luminosity": 0
            },
            "currentLanguage": "en",
            "status": 0
        }
        headers = {'Authorization': f'Bearer {AuthResponse.token}'}
        r = requests.post(url=url, json=data, headers=headers)
        data = json.loads(r.text)
        Request.cargoRequests = list()
        for r in data['cargoRequests']:
            cr = CargoRequest(
                id=r['id'],
                cargo=r['cargo']
            )
            Request.cargoRequests.append(cr)
        Request.settingsBound = list()
        for s in data['settingsBound']:
            sb = SettingBound(
                setting=s['setting'],
                minValue=s['minValue'],
                maxValue=s['maxValue']
            )
            Request.settingsBound.append(sb)

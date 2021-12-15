import json

import requests
from core.constants.settings import AppSettings
from core.models.auth_response import AuthResponse
from core.models.cargo import Cargo
from core.models.cargo_request import CargoRequest
from core.models.get_request import GetRequest
from core.models.request import Request
from core.models.setting_bound import SettingBound


class RequestService:
    @staticmethod
    def get_active_requests(get_request: GetRequest):
        url = f"{AppSettings.api_host}/cargoSession/carrierSessionRequests"
        data = {
            "requestType": get_request.requestType.value,
            "units": {
                "weight": get_request.units.weight.value,
                "length": get_request.units.length.value,
                "temperature": get_request.units.temperature.value,
                "humidity": get_request.units.humidity.value,
                "luminosity": get_request.units.luminosity.value
            },
            "currentLanguage": get_request.currentLanguage,
            "status": get_request.status.value
        }
        headers = {'Authorization': f'Bearer {AuthResponse.token}'}
        r = requests.post(url=url, json=data, headers=headers)
        data = json.loads(r.text)
        Request.cargoRequests = list()
        for r in data['cargoRequests']:
            cargo = Cargo(
                id=r['cargo']['id'],
                description=r['cargo']['description'],
                amount=r['cargo']['amount'],
                weight=r['cargo']['weight'],
                length=r['cargo']['length'],
                width=r['cargo']['width'],
                height=r['cargo']['height'],
            )
            cr = CargoRequest(
                id=r['id'],
                cargo=cargo
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

import requests
from core.constants.settings import AppSettings
from core.models.add_snapshot import AddSnapshot
from core.models.auth_response import AuthResponse


class IndicatorsApiService:
    @staticmethod
    def add_cargo_snapshot(snapshot: AddSnapshot):
        url = f"{AppSettings.api_host}/CargoSnapshot/addCurrentCarrierSessionSnapshots"
        data = {
            'temperature': snapshot.temperature,
            'humidity': snapshot.humidity,
            'luminosity': snapshot.luminosity,
            'requestType': snapshot.requestType.value
        }
        headers = {'Authorization': f'Bearer {AuthResponse.token}'}
        res = requests.post(url=url, json=data, headers=headers)
        print(res)

    @staticmethod
    def send_motion_detected_email(language: str):
        url = f"{AppSettings.api_host}/CargoSnapshot/sendMotionDetectedEmail/{language}"
        headers = {'Authorization': f'Bearer {AuthResponse.token}'}
        requests.post(url=url, json={}, headers=headers)

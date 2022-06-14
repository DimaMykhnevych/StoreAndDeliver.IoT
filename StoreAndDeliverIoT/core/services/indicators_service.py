from threading import Thread
import RPi.GPIO as GPIO
import Adafruit_DHT
import time
import random
from core.models.add_snapshot import AddSnapshot
from core.services.indicators_api_service import IndicatorsApiService
from core.models.user_settings import UserSettings


class IndicatorsService:
    def __init__(self, on_indicators_recorded_callback, get_request_type, push_button_callback):
        self.on_indicators_recorded = on_indicators_recorded_callback
        self.get_current_request_type = get_request_type
        # humidity and temperature
        self.DHT_SENSOR = Adafruit_DHT.DHT11
        self.DHT_PIN = 4
        self.indicators_disabled = False
        self.indicators_loop_thread = Thread()
        # luminosity
        GPIO.setmode(GPIO.BCM)
        self.LIGHT_PIN = 13
        GPIO.setup(self.LIGHT_PIN, GPIO.IN)
        time.sleep(0.5)
        # security mode
        self.PIR_PIN = 22
        GPIO.setup(self.PIR_PIN, GPIO.IN)
        self.security_mode_loop_thread = Thread()
        self.security_mode_disabled = False
        # push button
        GPIO.setwarnings(False)
        self.BUTTON_PIN = 15
        GPIO.setup(self.BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(self.BUTTON_PIN, GPIO.RISING, callback=push_button_callback)
        

    def start_indicators(self):
        self.indicators_loop_thread = Thread(target=self.start_indicators_loop,
                                             args=(lambda: self.indicators_disabled,))
        self.indicators_loop_thread.start()

    def stop_indicators(self):
        self.indicators_disabled = True
        self.indicators_loop_thread.join()

    def enable_security_mode(self):
        self.security_mode_loop_thread = Thread(target=self.start_security_mode_loop,
                                                args=(lambda: self.security_mode_disabled,))
        self.security_mode_loop_thread.start()

    def disable_security_mode(self):
        self.security_mode_disabled = True
        self.security_mode_loop_thread.join()

    def start_security_mode_loop(self, stop):
        self.security_mode_disabled = False
        while True:
            time.sleep(10)
            input_state = GPIO.input(self.PIR_PIN)
            if input_state:
                print("Motion detected")
                IndicatorsApiService.send_motion_detected_email(UserSettings.language)
                print("Motion detected email was send successfully")
            else:
                print("Motion wasn't detected")
            if stop():
                break

    def start_indicators_loop(self, stop):
        self.indicators_disabled = False
        while True:
            humidity, temperature = Adafruit_DHT.read(self.DHT_SENSOR, self.DHT_PIN)
            if humidity is not None and temperature is not None:
                print("Temp={0:0.01f}C Humidity={1:0.1f}%".format(temperature, humidity))
                current_luminosity = self.get_luminosity(GPIO.input(self.LIGHT_PIN))
                print("Luminosity={0:0.01f}Lux".format(current_luminosity))
                current_request_type = self.get_current_request_type()
                add_snapshot = AddSnapshot(temperature=temperature, humidity=humidity, luminosity=current_luminosity,
                                           requestType=current_request_type)
                IndicatorsApiService.add_cargo_snapshot(add_snapshot)
                print("Snapshot was saved successfully")
                self.on_indicators_recorded(add_snapshot)
            time.sleep(10)
            if stop():
                break

    def get_luminosity(self, is_dark):
        if is_dark:
            return random.randint(1, 100)
        return random.randint(100, 1000)

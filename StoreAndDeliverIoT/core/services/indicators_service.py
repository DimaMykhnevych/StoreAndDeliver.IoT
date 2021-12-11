from threading import Thread

import Adafruit_DHT
import time


class IndicatorsService:
    def __init__(self):
        self.DHT_SENSOR = Adafruit_DHT.DHT11
        self.DHT_PIN = 4
        self.indicators_enabled = True
        self.indicators_loop_thread = Thread()
    
    def start_indicators(self):
        self.indicators_loop_thread = Thread(target=self.start_indicators)
        self.indicators_loop_thread.start()
    
    def stop_indicators(self):
        self.indicators_loop_thread

    def start_indicators_loop(self):
        while self.indicators_enabled:
            humidity, temperature = Adafruit_DHT.read(self.DHT_SENSOR, self.DHT_PIN)
            if humidity is not None and temperature is not None:
                print("Temp={0:0.01f}C Humidity={1:0.1f}%".format(temperature, humidity))
            else:
                print("FAILURE")
            time.sleep(10)

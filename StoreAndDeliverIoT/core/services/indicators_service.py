from threading import Thread
import RPi.GPIO as GPIO
import Adafruit_DHT
import time
import random


class IndicatorsService:
    def __init__(self):
        #humidity and temperature
        self.DHT_SENSOR = Adafruit_DHT.DHT11
        self.DHT_PIN = 4
        self.indicators_disabled = False
        self.indicators_loop_thread = Thread()
        #luminosity
        GPIO.setmode(GPIO.BCM)
        self.LIGHT_PIN = 13
        GPIO.setup(self.LIGHT_PIN, GPIO.IN)
        time.sleep(0.5)
        #security mode
        self.PIR_PIN = 22
        GPIO.setup(self.PIR_PIN, GPIO.IN)
        self.security_mode_loop_thread = Thread()
        self.security_mode_disabled = False
    
    def start_indicators(self):
        self.indicators_loop_thread = Thread(target=self.start_indicators_loop, args =(lambda : self.indicators_disabled, ))
        self.indicators_loop_thread.start()
    
    def stop_indicators(self):
        self.indicators_disabled = True
        self.indicators_loop_thread.join()
        
    def enable_security_mode(self):
        self.security_mode_loop_thread = Thread(target=self.start_security_mode_loop, args =(lambda : self.security_mode_disabled, ))
        self.security_mode_loop_thread.start()
        
    def disable_security_mode(self):
        self.security_mode_disabled = True
        self.security_mode_loop_thread.join()
        
    def start_security_mode_loop(self, stop):
        self.security_mode_disabled = False
        while True: 
          time.sleep(10) 
          input_state = GPIO.input(self.PIR_PIN) 
          if input_state == True:    
            print("Motion detected")
          else:
            print("Motion wasn't detected")
          if stop():
            break

    def start_indicators_loop(self, stop):
        count = 0
        self.indicators_disabled = False
        while True:
            humidity, temperature = Adafruit_DHT.read(self.DHT_SENSOR, self.DHT_PIN)
            if humidity is not None and temperature is not None:
                print("Temp={0:0.01f}C Humidity={1:0.1f}%".format(temperature, humidity))
                print("Luminosity={0:0.01f}Lux".format(self.get_luminosity(GPIO.input(self.LIGHT_PIN))))
            time.sleep(5)
            if stop():
                break
            
    def get_luminosity(self, is_dark):
        if is_dark:
            return random.randint(1, 100)
        return random.randint(100, 1000)


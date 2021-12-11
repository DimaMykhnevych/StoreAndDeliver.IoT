from guizero import Text, ListBox, Box, PushButton

from core.constants.indicators_settings import IndicatorsSettings
from core.models.request import Request
from core.services.request_service import RequestService
from core.services.indicators_service import IndicatorsService


class MainWindow:
    width = 700
    height = 500

    def __init__(self, window):
        self.window = window
        self.center_main_window()
        Text(window, text="Current active cargo requests", color="blue", size=14)
        self.listbox = ListBox(window, items=[])
        Text(window, text="Required Indicators Settings", color="blue", size=14)
        self.humidity_text = Text(window, text="")
        self.humidity_text.visible = False
        self.luminosity_text = Text(window, text="")
        self.luminosity_text.visible = False
        self.temperature_text = Text(window, text="")
        self.temperature_text.visible = False
        self.start_button = PushButton(window, text="Start", command=self.on_start_indicators)
        self.stop_button = PushButton(window, text="Stop", command=self.on_stop_indicators)
        self.enable_security_mode = PushButton(window, text="Enable security mode", command=self.on_enable_security_mode)
        self.disable_security_mode = PushButton(window, text="Disable security mode", command=self.on_disable_security_mode)
        self.indicators_service = IndicatorsService()
        
    def on_enable_security_mode(self):
        self.indicators_service.enable_security_mode()
        
    def on_disable_security_mode(self):
        self.indicators_service.disable_security_mode()
        
    def on_start_indicators(self):
        self.indicators_service.start_indicators()
        
    def on_stop_indicators(self):
        self.indicators_service.stop_indicators()

    def center_main_window(self):
        screen_width = self.window.tk.winfo_screenwidth()
        screen_height = self.window.tk.winfo_screenheight()
        x = (screen_width / 2) - (self.width / 2)
        y = (screen_height / 2) - (self.height / 2)
        self.window.tk.geometry('%dx%d+%d+%d' % (self.width, self.height, x, y))

    def get_requests(self):
        RequestService.get_active_requests()
        for cr in Request.cargoRequests:
            self.listbox.append(cr.cargo.description)
        for setting in Request.settingsBound:
            if setting.setting == IndicatorsSettings.temperature:
                self.temperature_text.visible = True
                self.temperature_text.value = f"Temperature: {setting.minValue}°C ...  {setting.maxValue}°C"
            elif setting.setting == IndicatorsSettings.humidity:
                self.humidity_text.visible = True
                self.humidity_text.value = f"Humidity: {setting.minValue}°C ...  {setting.maxValue}°C"
            elif setting.setting == IndicatorsSettings.luminosity:
                self.luminosity_text.visible = True
                self.luminosity_text.value = f"Luminosity: {setting.minValue}°C ...  {setting.maxValue}°C"

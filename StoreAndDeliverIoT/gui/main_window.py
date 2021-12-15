from guizero import Text, ListBox, PushButton, ButtonGroup, MenuBar

from core.constants.indicators_settings import IndicatorsSettings
from core.constants.language import Language
from core.enums.humidity_unit import HumidityUnit
from core.enums.length_unit import LengthUnit
from core.enums.luminosity_unit import LuminosityUnit
from core.enums.request_status import RequestStatus
from core.enums.request_type import RequestType
from core.enums.temperature_unit import TemperatureUnit
from core.enums.weight_unit import WeightUnit
from core.models.add_snapshot import AddSnapshot
from core.models.get_request import GetRequest
from core.models.request import Request
from core.models.units import Units
from core.services.custom_translate_service import _
from core.services.indicators_api_service import IndicatorsApiService
from core.services.request_service import RequestService
from core.services.indicators_service import IndicatorsService


class MainWindow:
    width = 700
    height = 500
    website_link = "https://dimamykhnevych.github.io/StoreAndDeliver.UI/home"

    def __init__(self, window):
        self.menu_bar = MenuBar(window,
                                toplevel=[_("about")],
                                options=[
                                    [["Program", self.on_program_about_click],
                                     ["Developers", self.on_developers_about_click]]
                                ])
        self.window = window
        self.window.bg = (240, 240, 218)
        self.selected_request_type = RequestType.DELIVER
        self.indicators_service = IndicatorsService()
        self.center_main_window()
        Text(window, text="Current active cargo requests", color="blue", size=14)
        self.request_type_choice = ButtonGroup(window,
                                               options=[["Store", RequestType.STORE.name],
                                                        ["Deliver", RequestType.DELIVER.name]],
                                               selected=self.selected_request_type.name,
                                               horizontal="True",
                                               command=self.on_request_type_changed)
        self.loading_text = Text(window, text="Loading...", color="blue")
        self.loading_text.visible = False
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
        self.enable_security_mode = PushButton(window,
                                               text="Enable security mode",
                                               command=self.on_enable_security_mode)
        self.disable_security_mode = PushButton(window,
                                                text="Disable security mode",
                                                command=self.on_disable_security_mode)
        self.hide_security_mode_actions()

    def on_program_about_click(self):
        self.window.info("About program", "StoreAndDeliver IoT program to track environmental conditions of stored "
                                          f"and delivered cargo.\nLink to website: {self.website_link}")

    def on_developers_about_click(self):
        self.window.info("About developers", "Program was developed by Dmytro Mykhnevych, "
                                             "student of Kharkiv National University of Radio Electronics\n"
                                             "Email: dmytro.mykhnevych@nure.ua")

    def hide_security_mode_actions(self):
        self.enable_security_mode.visible = False
        self.disable_security_mode.visible = False

    def show_security_mode_actions(self):
        self.enable_security_mode.visible = True
        self.disable_security_mode.visible = True

    def on_request_type_changed(self):
        string_request_type_option = self.request_type_choice.value
        self.selected_request_type = RequestType.DELIVER
        self.hide_security_mode_actions()
        if string_request_type_option == RequestType.STORE.name:
            self.selected_request_type = RequestType.STORE
            self.show_security_mode_actions()
        self.listbox.clear()
        self.get_requests()

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
        get_request = GetRequest(
            requestType=self.selected_request_type,
            units=Units(
                weight=WeightUnit.KILOGRAMS,
                length=LengthUnit.METERS,
                temperature=TemperatureUnit.CELSIUS,
                humidity=HumidityUnit.PERCENTAGE,
                luminosity=LuminosityUnit.LUX
            ),
            currentLanguage=Language.en,
            status=RequestStatus.IN_PROGRESS
        )
        self.loading_text.visible = True
        RequestService.get_active_requests(get_request)
        self.loading_text.visible = False
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

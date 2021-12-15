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
from core.models.auth_response import AuthResponse
from core.models.get_request import GetRequest
from core.models.request import Request
from core.models.units import Units
from core.models.user_settings import UserSettings
from core.services.custom_translate_service import _, get_temperature_unit_symbol
from core.services.indicators_api_service import IndicatorsApiService
from core.services.request_service import RequestService
from core.services.indicators_service import IndicatorsService


class MainWindow:
    width = 700
    height = 500
    website_link = "https://dimamykhnevych.github.io/StoreAndDeliver.UI/home"

    def __init__(self, window):
        self.menu_bar = MenuBar(window,
                                toplevel=[_('about'), _('language'), _('temperature')],
                                options=[
                                    [[_('program'), self.on_program_about_click],
                                     [_('developers'), self.on_developers_about_click]],
                                    [[_('english'), lambda: self.on_language_change(Language.en)],
                                     [_('ukrainian'), lambda: self.on_language_change(Language.ua)],
                                     [_('russian'), lambda: self.on_language_change(Language.ru)]],
                                    [[_('celsius'), lambda: self.on_temperature_unit_click(TemperatureUnit.CELSIUS)],
                                     [_('fahrenheit'),
                                      lambda: self.on_temperature_unit_click(TemperatureUnit.FAHRENHEIT)],
                                     [_('kelvin'), lambda: self.on_temperature_unit_click(TemperatureUnit.KELVIN)]]
                                ])
        self.window = window
        self.window.bg = (240, 240, 218)
        self.selected_request_type = RequestType.DELIVER
        self.indicators_service = IndicatorsService()
        self.center_main_window()
        self.main_header = Text(window, text=_('current_active_requests'), color="blue", size=14)
        self.request_type_choice = ButtonGroup(window,
                                               options=[[_('store'), RequestType.STORE.name],
                                                        [_('deliver'), RequestType.DELIVER.name]],
                                               selected=self.selected_request_type.name,
                                               horizontal="True",
                                               command=self.on_request_type_changed)
        self.loading_text = Text(window, text=_("loading"), color="blue")
        self.loading_text.visible = False
        self.listbox = ListBox(window, items=[])
        self.required_settings_header = Text(window, text=_('required_settings'), color="blue", size=14)
        self.humidity_text = Text(window, text="")
        self.humidity_text.visible = False
        self.luminosity_text = Text(window, text="")
        self.luminosity_text.visible = False
        self.temperature_text = Text(window, text="")
        self.temperature_text.visible = False
        self.start_button = PushButton(window, text=_('start'), command=self.on_start_indicators)
        self.stop_button = PushButton(window, text=_('stop'), command=self.on_stop_indicators)
        self.enable_security_mode = PushButton(window,
                                               text=_('enable_security_mode'),
                                               command=self.on_enable_security_mode)
        self.disable_security_mode = PushButton(window,
                                                text=_('disable_security_mode'),
                                                command=self.on_disable_security_mode)
        self.hide_security_mode_actions()

    def on_language_change(self, language):
        UserSettings.language = language
        UserSettings.temperature_unit = TemperatureUnit.CELSIUS
        if language == Language.en:
            UserSettings.temperature_unit = TemperatureUnit.FAHRENHEIT
        self.update_view()

    def on_temperature_unit_click(self, temperature_unit):
        UserSettings.temperature_unit = temperature_unit
        self.update_request_list()

    def on_program_about_click(self):
        self.window.info(_('about_program'), f"{_('about_program_description')}{self.website_link}")

    def on_developers_about_click(self):
        self.window.info(_('about_developers'), _('about_developers_description'))

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
        self.update_request_list()

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
        self.update_view(False)
        get_request = GetRequest(
            requestType=self.selected_request_type,
            units=Units(
                weight=WeightUnit.KILOGRAMS,
                length=LengthUnit.METERS,
                temperature=UserSettings.temperature_unit,
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
                self.temperature_text.value = f"{_('temperature')}: {setting.minValue}" \
                                              f"{get_temperature_unit_symbol()} ... " \
                                              f"{setting.maxValue}{get_temperature_unit_symbol()}"
            elif setting.setting == IndicatorsSettings.humidity:
                self.humidity_text.visible = True
                self.humidity_text.value = f"{_('humidity')}: {setting.minValue}% ... {setting.maxValue}%"
            elif setting.setting == IndicatorsSettings.luminosity:
                self.luminosity_text.visible = True
                self.luminosity_text.value = f"{_('luminosity')}: {setting.minValue}lx ... {setting.maxValue}lx"

    def update_request_list(self):
        self.listbox.clear()
        self.get_requests()

    def update_view(self, need_to_update_requests=True):
        self.menu_bar = MenuBar(self.window,
                                toplevel=[_('about'), _('language'), _('temperature')],
                                options=[
                                    [[_('program'), self.on_program_about_click],
                                     [_('developers'), self.on_developers_about_click]],
                                    [[_('english'), lambda: self.on_language_change(Language.en)],
                                     [_('ukrainian'), lambda: self.on_language_change(Language.ua)],
                                     [_('russian'), lambda: self.on_language_change(Language.ru)]],
                                    [[_('celsius'), lambda: self.on_temperature_unit_click(TemperatureUnit.CELSIUS)],
                                     [_('fahrenheit'),
                                      lambda: self.on_temperature_unit_click(TemperatureUnit.FAHRENHEIT)],
                                     [_('kelvin'), lambda: self.on_temperature_unit_click(TemperatureUnit.KELVIN)]]
                                ])
        self.main_header.value = _('current_active_requests')
        self.request_type_choice.remove(RequestType.STORE.name)
        self.request_type_choice.remove(RequestType.DELIVER.name)
        self.request_type_choice.append([_('store'), RequestType.STORE.name])
        self.request_type_choice.append([_('deliver'), RequestType.DELIVER.name])
        self.required_settings_header.value = _('required_settings')
        self.start_button.text = _('start')
        self.stop_button.text = _('stop')
        self.enable_security_mode.text = _('enable_security_mode')
        self.disable_security_mode.text = _('disable_security_mode')
        if need_to_update_requests:
            self.update_request_list()

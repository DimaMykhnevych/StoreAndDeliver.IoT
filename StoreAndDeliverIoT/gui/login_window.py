import sys
from threading import Thread
from guizero import App, Text, TextBox, PushButton, Window, MenuBar

from core.constants.Roles import Roles
from core.constants.language import Language
from core.enums.temperature_unit import TemperatureUnit
from core.models.auth_response import AuthResponse
from core.models.user_settings import UserSettings
from core.services.auth_service import AuthService
from core.services.custom_translate_service import _
from gui.main_window import MainWindow


class LoginWindow:
    width = 340
    height = 120
    app = App(title=_('login'), width=width, height=height, layout="grid")
    username_text = Text(app, text=_('username'), grid=[0, 0], align="left")
    username_text_box = TextBox(app, width=30, grid=[1, 0])
    password_text = Text(app, text=_('password'), grid=[0, 1], align="left")
    password_text_box = TextBox(app, width=30, grid=[1, 1], hide_text=True)
    error_text = Text(app, text="", grid=[1, 2], align="left", color="red")
    loading_text = Text(app, text="", grid=[0, 2], align="left", color="blue")

    def __init__(self):
        self.mainWindow = MainWindow(Window(self.app, title=_('dashboard')))
        self.menu_bar = MenuBar(self.app,
                                toplevel=[_('language')],
                                options=[
                                    [[_('english'), lambda: self.on_language_change(Language.en)],
                                     [_('ukrainian'), lambda: self.on_language_change(Language.ua)],
                                     [_('russian'), lambda: self.on_language_change(Language.ru)]],
                                ])
        self.mainWindow.window.hide()
        self.login_btn = PushButton(self.app, command=self.on_login_click, text=_('log_in'), grid=[0, 3])
        self.mainWindow.window.when_closed = self.app.destroy
        self.center_login_window()
        self.app.display()

    def on_language_change(self, language):
        UserSettings.language = language
        UserSettings.temperature_unit = TemperatureUnit.CELSIUS
        if language == Language.en:
            UserSettings.temperature_unit = TemperatureUnit.FAHRENHEIT
        self.update_view()

    def update_view(self):
        self.app.title = _('login')
        self.mainWindow.window.title = _('dashboard')
        self.username_text.value = _('username')
        self.password_text.value = _('password')
        self.login_btn.text = _('log_in')
        self.menu_bar = MenuBar(self.app,
                                toplevel=[_('language')],
                                options=[
                                    [[_('english'), lambda: self.on_language_change(Language.en)],
                                     [_('ukrainian'), lambda: self.on_language_change(Language.ua)],
                                     [_('russian'), lambda: self.on_language_change(Language.ru)]],
                                ])

    def on_login_click(self):
        username = self.username_text_box.value
        password = self.password_text_box.value
        if username != "" and password != "":
            self.loading_text.value = _("loading")
            self.error_text.clear()
            self.login_btn.disable()
            thread = Thread(target=self.authorize)
            thread.start()

    def authorize(self):
        username = self.username_text_box.value
        password = self.password_text_box.value
        if username != "" and password != "":
            AuthService.login(username, password)
            self.validate_response()

    def validate_response(self):
        self.loading_text.clear()
        if AuthResponse.is_authorized and AuthResponse.user_info.role == Roles.carrier:
            self.error_text.clear()
            self.app.hide()
            self.mainWindow.window.show()
            self.mainWindow.get_requests()
        elif AuthResponse.is_authorized and AuthResponse.user_info.role != Roles.carrier:
            self.error_text.value = _('access_denied')
        else:
            if AuthResponse.login_error_code == 0:
                self.error_text.value = _('invalid_credentials')
            elif AuthResponse.login_error_code == 1:
                self.error_text.value = _('email_confirmation_required')
        self.login_btn.enable()
        sys.exit()

    def center_login_window(self):
        screen_width = self.app.tk.winfo_screenwidth()
        screen_height = self.app.tk.winfo_screenheight()
        x = (screen_width / 2) - (self.width / 2)
        y = (screen_height / 2) - (self.height / 2)
        self.app.tk.geometry('%dx%d+%d+%d' % (self.width, self.height, x, y))

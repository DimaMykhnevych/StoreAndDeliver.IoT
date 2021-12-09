import sys
from threading import Thread
from guizero import App, Text, TextBox, PushButton, Window
from core.models.auth_response import AuthResponse
from core.services.auth_service import AuthService
from gui.main_window import MainWindow


class LoginWindow:
    width = 340
    height = 120
    app = App(title="Login", width=width, height=height, layout="grid")
    username_text = Text(app, text="Username: ", grid=[0, 0], align="left")
    username_text_box = TextBox(app, width=30, grid=[1, 0])
    password_text = Text(app, text="Password: ", grid=[0, 1], align="left")
    password_text_box = TextBox(app, width=30, grid=[1, 1], hide_text=True)
    error_text = Text(app, text="", grid=[1, 2], align="left", color="red")
    loading_text = Text(app, text="", grid=[0, 2], align="left", color="blue")

    def __init__(self):
        self.mainWindow = MainWindow(Window(self.app, title="Dashboard"))
        self.center_login_window()
        self.mainWindow.window.hide()
        self.login_btn = PushButton(self.app, command=self.on_login_click, text="Log In", grid=[0, 3])
        self.mainWindow.window.when_closed = self.app.destroy
        self.app.display()

    def on_login_click(self):
        username = self.username_text_box.value
        password = self.password_text_box.value
        if username != "" and password != "":
            self.loading_text.value = "Loading..."
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
        if AuthResponse.is_authorized:
            self.error_text.clear()
            self.app.hide()
            self.mainWindow.window.show()
            MainWindow.get_requests()
        else:
            if AuthResponse.login_error_code == 0:
                self.error_text.value = "Username or password is invalid"
            elif AuthResponse.login_error_code == 1:
                self.error_text.value = "You need to confirm your email"
        self.login_btn.enable()
        sys.exit()

    def center_login_window(self):
        screen_width = self.app.tk.winfo_screenwidth()
        screen_height = self.app.tk.winfo_screenheight()
        x = (screen_width / 2) - (self.width / 2)
        y = (screen_height / 2) - (self.height / 2)
        self.app.tk.geometry('%dx%d+%d+%d' % (self.width, self.height, x, y))

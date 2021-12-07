from guizero import App, Text, TextBox, PushButton


class LoginWindow:
    width = 300
    height = 200
    app = App(title="Login", width=width, height=height, layout="grid")
    username_text = Text(app, text="Username: ", grid=[0, 0], align="left")
    username_text_box = TextBox(app, width=30, grid=[1, 0])
    password_text = Text(app, text="Password: ", grid=[0, 1], align="left")
    password_text_box = TextBox(app, width=30, grid=[1, 1], hide_text=True)

    def __init__(self):
        self.center_window()
        self.update_text = PushButton(self.app, text="Log In", grid=[1, 2])
        self.app.display()

    def hide_it(self):
        self.app.hide()

    def center_window(self):
        screen_width = self.app.tk.winfo_screenwidth()
        screen_height = self.app.tk.winfo_screenheight()
        x = (screen_width / 2) - (self.width / 2)
        y = (screen_height / 2) - (self.height / 2)
        self.app.tk.geometry('%dx%d+%d+%d' % (self.width, self.height, x, y))

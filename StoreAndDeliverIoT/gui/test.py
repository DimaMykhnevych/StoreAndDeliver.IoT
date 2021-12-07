from guizero import App, Text, TextBox, PushButton, Slider


class Gui:
    app = App(title="Hello world")
    welcome_message = Text(app, text="Welcome to my app",
                           size=40,
                           font="Times New Roman",
                           color="lightblue")
    my_name = TextBox(app, width=40)

    def __init__(self):
        self.update_text = PushButton(self.app, command=self.show_name, text="Display my name")
        text_size = Slider(self.app, command=self.change_text_size, start=10, end=80)
        self.show_window()

    def show_window(self):
        self.app.display()

    def show_name(self):
        self.welcome_message.value = self.my_name.value

    def change_text_size(self, value):
        self.welcome_message.size = value


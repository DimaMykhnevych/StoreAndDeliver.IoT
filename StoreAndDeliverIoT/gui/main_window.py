from guizero import Text


class MainWindow:
    width = 600
    height = 400

    def __init__(self, window):
        self.window = window
        self.center_main_window()
        Text(window, text="This text will show up in the second window")

    def center_main_window(self):
        screen_width = self.window.tk.winfo_screenwidth()
        screen_height = self.window.tk.winfo_screenheight()
        x = (screen_width / 2) - (self.width / 2)
        y = (screen_height / 2) - (self.height / 2)
        self.window.tk.geometry('%dx%d+%d+%d' % (self.width, self.height, x, y))

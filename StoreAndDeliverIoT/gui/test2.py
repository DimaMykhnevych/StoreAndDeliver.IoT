from guizero import App, Combo, Text, CheckBox, ButtonGroup, PushButton, info


class Gui2:
    app = App(title="My second GUI app", width=300, height=200, layout="grid")
    film_choice = Combo(app, options=["Star Wars", "Frozen", "Lion King"], grid=[1, 0], align="left")
    film_description = Text(app, text="Which film?", grid=[0, 0], align="left")
    vip_seat = CheckBox(app, text="VIP seat?", grid=[1, 1], align="left")
    row_choice = ButtonGroup(app, options=[["Front", "F"], ["Middle", "M"], ["Back", "B"]],
                             selected="M", horizontal=True, grid=[1, 2], align="left")

    def __init__(self):
        self.book_seats = PushButton(self.app, command=self.do_booking, text="Book seat", grid=[1, 3], align="left")
        self.app.display()

    def do_booking(self):
        info("Booking", "Thank you for booking")
        print(self.film_choice.value)
        print(self.vip_seat.value)
        print(self.row_choice.value)

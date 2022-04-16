from turtle import Screen, Turtle


class Scr(Screen):
    def __init__(self):
        super().__init__()
        self.Scr = Turtle.Screen()

    def question(self):
        self.textinput(title="Guess the state", prompt="What's another state's name?")

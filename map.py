from turtle import Turtle, Screen


class Map(Turtle):
    def __init__(self):
        super().__init__()
        self.screen = Screen()
        image = "blank_states_img.gif"
        self.screen.addshape(image)
        self.shape(image)

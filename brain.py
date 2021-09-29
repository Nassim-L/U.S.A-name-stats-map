import pandas
from turtle import Turtle, Screen
import turtle
import time

name_show_in_the_map = []
name_left = []


class Brain(Turtle):
    def __init__(self):
        super().__init__()
        self.screen = Screen()
        self.ht()
        self.data = pandas.read_csv('50_states.csv')
        self.states = self.data.state.tolist()
        self.x = self.data.x.tolist()
        self.y = self.data.y.tolist()
        self.scoreboard = Turtle()
        self.score = 0
        self.xx = 0
        self.answer_state = ""
        self.game = True
        self.loop()

    def loop(self):
        self.xx = len(name_show_in_the_map)
        while self.xx < 50:
            self.get_answer()
            if self.answer_state == "show":
                self.show()

            elif self.answer_state == "stop":
                turtle.bye()

    def get_answer(self):
        self.answer_state = self.screen.textinput(title='Guess The State', prompt="What's another state name?.")
        self.show_name_in_the_map()

    def show_name_in_the_map(self):
        if self.answer_state.title() in self.states:
            index = self.states.index(self.answer_state.title())
            pos = (self.x[index], self.y[index])
            self.ht()
            self.pu()
            self.goto(pos)
            self.write(f'{self.answer_state.title()}', align="center", font=("courier", 10, "normal"))
            if self.answer_state.title() not in name_show_in_the_map:
                name_show_in_the_map.append(self.answer_state.title())
                self.inc_score()
                self.showscore()

            self.get_answer()

        elif self.answer_state == "stop":
            pass

        elif self.answer_state == "show":
            pass

        else:
            self.goto(0, 0)
            b = Turtle()
            b.ht()
            b.write('Wrong state name', align="center", font=("courier", 40, "normal"))
            time.sleep(1)
            b.clear()
            self.get_answer()

    def inc_score(self):
        self.score += 1

    def showscore(self):
        scoret = self.scoreboard
        scoret.ht()
        scoret.pu()
        scoret.goto(250, 230)
        scoret.clear()
        scoret.write(f'{self.score}/50', align="center", font=("courier", 40, "normal"))

    def show(self):

        for states in self.states:
            if states not in name_left:
                name_left.append(states)

        print(pandas.DataFrame(name_left))

from turtle import Turtle
import time

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-250, 265)
        self.hideturtle()

    def display_level(self, level):
        self.write(f"Level: {level}", font=FONT)
        time.sleep(2)
        self.clear()

    def game_over(self, level):
        self.write(f"GAME OVER, Level: {level}", font=FONT)


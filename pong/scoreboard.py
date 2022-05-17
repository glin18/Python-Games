from turtle import Turtle
import time

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.hideturtle()
        self.penup()
        self.goto(-20, 270)
        self.color("white")

    def right_score(self):
        self.r_score += 1
        self.write(f"{self.l_score} : {self.r_score}", font=("Arial", 20, "bold"))
        if self.r_score == 5:
            time.sleep(1)
            self.clear()
            self.write("GAME OVER RIGHT WINS", font=("Arial", 20, "bold"))

    def left_score(self):
        self.l_score += 1
        self.write(f"{self.l_score} : {self.r_score}", font=("Arial", 20, "bold"))
        if self.l_score == 5:
            time.sleep(1)
            self.clear()
            self.write("GAME OVER LEFT WINS", font=("Arial", 20, "bold"))




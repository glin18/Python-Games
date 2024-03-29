from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.shapesize(stretch_wid=2, stretch_len=1)
        self.setheading(90)
        self.random_car()

    def move(self, level):
        new_x = self.xcor() - STARTING_MOVE_DISTANCE - MOVE_INCREMENT*level
        self.goto(new_x, self.ycor())

    def random_car(self):
        y_cor = random.randint(-250, 250)
        x_cor = 299
        self.color(random.choice(COLORS))
        self.goto(x_cor, y_cor)



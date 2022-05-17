from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.goto(0, -275)
        self.setheading(90)

    def up(self):
        new_y = self.ycor() + 10
        self.goto(self.xcor(), new_y)

    def return_starting(self):
        self.goto(0, -275)

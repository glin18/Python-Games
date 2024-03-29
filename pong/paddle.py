from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)

    def go_up(self):
        new_y = self.ycor() + 60
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 60
        self.goto(self.xcor(), new_y)


from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.x_move = 1
        self.y_move = 1.4

    def move(self):
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(new_x, new_y)

    def check_collision(self):
        if self.ycor() >= 299 or self.ycor() <= -299:
            self.y_move = self.y_move * -1

    def check_bounce(self, paddle):
        if self.distance(paddle) < 90 and (self.xcor() == 340 or self.xcor() == -340):
            self.x_move = self.x_move * -1

    def right_lose(self):
        if self.xcor() >= 399:
            self.goto(0, 0)
            return True
        return False

    def left_lose(self):
        if self.xcor() <= -399:
            self.goto(0, 0)
            return True
        return False




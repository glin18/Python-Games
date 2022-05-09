from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.color("white")
        self.score_update()

    def score_increase(self):
        self.score += 1
        self.score_update()

    def score_update(self):
        self.clear()
        style = ('Courier', 30, 'italic')
        self.write(f'Score: {self.score} ', font=style, align='center')

    def game_end(self):
        self.clear()
        style = ('Courier', 30, 'italic')
        self.goto(0, 0)
        self.write(f"GAME OVER, Final Score: {self.score}", font=style, align='center')
from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
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
        self.write(f'Score: {self.score} , High Score: {self.high_score} ', font=style, align='center')

    # def game_end(self):
    #     self.clear()
    #     style = ('Courier', 30, 'italic')
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER, Final Score: {self.score}", font=style, align='center')

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.score_update()

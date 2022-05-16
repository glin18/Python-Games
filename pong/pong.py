import turtle as t
from paddle import Paddle

screen = t.Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

paddle = Paddle()
paddle.goto(350, 0)

paddle2 = Paddle()
paddle2.goto(-350, 0)


screen.listen()
screen.onkey(paddle.go_up, "Up")
screen.onkey(paddle.go_down, "Down")
screen.onkey(paddle2.go_up, "w")
screen.onkey(paddle2.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()

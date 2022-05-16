import turtle as t
from paddle import Paddle
from ball import Ball
import time

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

ball = Ball()


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.0001)
    ball.check_collision()
    ball.check_bounce(paddle)
    ball.check_bounce(paddle2)
    ball.move()



screen.exitonclick()

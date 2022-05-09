import turtle as t
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
# turn off tracer
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

game_is_on = True

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")
screen.onkey(snake.left, "a")
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    if snake.segments[0].distance(food) < 15:
        food.refresh()
        score.score_increase()
        snake.extend()

    if snake.segments[0].xcor() > 299 or snake.segments[0].xcor() < -299 or snake.segments[0].ycor() > 299 \
            or snake.segments[0].ycor() < -299:
        game_is_on = False
        score.game_end()

    for segment in snake.segments[1:]:
        if segment.distance(snake.segments[0]) < 10:
            game_is_on = False
            score.game_end()

screen.exitonclick()

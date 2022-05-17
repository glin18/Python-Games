import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing")

player = Player()
car = CarManager()
car_list = [car]
score = Scoreboard()

screen.listen()
screen.onkey(player.up, 'Up')

game_is_on = True
n = 0
level = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if n % 6 == 0:
        new_car = CarManager()
        car_list.append(new_car)
    for vehicle in car_list:
        vehicle.move(level)
        if player.distance(vehicle) < 15:
            game_is_on = False

    n += 1
    if player.ycor() >= 290:
        level += 1
        player.return_starting()
        score.display_level(level)
        n += 1

screen.exitonclick()

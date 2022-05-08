import turtle as t
import random

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

turtleOne = t.Turtle()
turtleTwo = t.Turtle()
turtleThree = t.Turtle()
turtleFour = t.Turtle()
turtleFive = t.Turtle()
turtleSix = t.Turtle()

screen = t.Screen()
screen.setup(width=500, height=400)

turtles = [turtleOne, turtleTwo, turtleThree, turtleFour, turtleFive, turtleSix]
y_coord = -125
i = 0

for turtle in turtles:
    turtle.shape("turtle")
    turtle.color(colors[i])
    turtle.penup()
    turtle.goto(x=-230, y=y_coord)
    y_coord += 50
    i += 1

is_race_on = False
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        turtle.forward(random.randint(1, 10))
        if turtle.position()[0] > 240:
            is_race_on = False
            index = turtles.index(turtle)
            text = t.Turtle()
            text.penup()
            text.hideturtle()
            text.setpos(-220, 0)
            if user_bet.lower() == colors[index]:
                text.write(f"You win! The winner is {colors[index]}", font=("Lemon", 30, "normal"))
            else:
                text.write(f"You lose! The winner is {colors[index]}", font=("Lemon", 30, "normal"))
            
screen.exitonclick()

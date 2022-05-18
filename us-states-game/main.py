import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US States Game")

screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

data = pd.read_csv("50_states.csv")
states = data["state"]
game_is_on = True
n = 0
correct_answers = []
missed_answers = []

while game_is_on:
    answer_state = screen.textinput(title=f"Guess the State. {n}/50", prompt="What's another state's name?")
    answer_state = answer_state.lower().capitalize()
    if answer_state in states.to_list():
        row = data[data["state"] == answer_state]
        x = int(row["x"])
        y = int(row["y"])
        state = turtle.Turtle()
        state.penup()
        state.hideturtle()
        state.goto(x, y)
        state.write(f"{answer_state}")
        correct_answers.append(answer_state)
        n += 1
        if n == 50:
            game_is_on = False
    if answer_state == "Exit":
        game_is_on = False
        for state in states.to_list():
            if state not in correct_answers:
                missed_answers.append(state)
missed_answers = pd.DataFrame(missed_answers)
print(missed_answers)
missed_answers.to_csv("states_to_learn.csv")
screen.exitonclick()

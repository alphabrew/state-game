import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

guessed_states = []

while len(guessed_states)<50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 identified", prompt="Enter state State").title()

    data = pd.read_csv("50_states.csv")
    all_states = data.state.tolist()

    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        row= data[data.state==answer_state]
        t.goto(int(row.x), int(row.y))
        t.write(row.state.item())
        guessed_states.append(row.state.item())

screen.exitonclick()

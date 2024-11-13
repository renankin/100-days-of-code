import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("Name the States")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50"
                                          f" States Correct",
                                    prompt="What's another state's "
                                           "name?").title()

    if answer_state == "Exit":
        # Save states which have not been guessed into csv file
        remaining_states = []
        for state in all_states:
            if state not in guessed_states:
                remaining_states.append(state)
        df = pd.DataFrame(remaining_states)
        df.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)

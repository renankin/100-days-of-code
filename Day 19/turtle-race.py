from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet",
                            prompt="Which turtle will win the race? Enter a "
                                   "color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = -100
all_turtles = []

for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_pos)
    y_pos += 40
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True
else:
    is_race_on = False

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the "
                      f"winner.")
        random_dist = random.randint(0, 10)
        turtle.forward(random_dist)

screen.exitonclick()

import random
import turtle
from turtle import Turtle, Screen


is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color(vibgyor): ")
colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
y_position = [-90, -60, -30, 0, 30, 60, 90]
all_turtles = []

for turtle_index in range(0, 7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x = -230, y=y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for t in all_turtles:
        if t.xcor() > 210:
            is_race_on = False
            winner = t.pencolor()
            if winner == user_bet:
                print(f"You won the bet. The {winner} turtle is the winner!!")
            else:
                print(f"You lost the bet. The {winner} turtle is the winner!!")

        random_distance = random.randint(0, 10)
        t.forward(random_distance)


screen.exitonclick()
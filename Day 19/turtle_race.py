from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=600, height=600)
user_bet = screen.textinput(title="Make your bet", prompt="Which color will win").lower()
print(user_bet)
colors = ["red", "green", "blue", "yellow", "orange"]
y_position = [-200, -100, 0, 100, 200]
all_turtles = []

for i in range(0,5):
    a = Turtle()
    a.shape("turtle")
    a.color(colors[i])
    a.penup()
    a.goto(-290, y_position[i])
    a.speed(random.randint(10,50))
    all_turtles.append(a)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You Won! {winning_color} You guessed it right ")
            else:
                print(f"You Lose! {winning_color} won the race You guessed it wrong ")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()

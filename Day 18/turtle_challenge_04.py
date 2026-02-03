# Random Walk

from turtle import Turtle, Screen
import random

timmy = Turtle()
screen = Screen()

# screen.setworldcoordinates(-300, -300, 300, 300)
angles = [0,90,180,270]
timmy.pensize(10)
timmy.shape("circle")
timmy.shapesize(0.5, 0.5)
timmy.speed("fastest")

for i in range(30):

    timmy.color(random.random(), random.random(), random.random())
    timmy.left(random.choice(angles))
    timmy.forward(20)


screen.exitonclick()

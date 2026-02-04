# Making a Spirograph

from turtle import Turtle, Screen
import random

timmy = Turtle()
screen = Screen()

timmy.speed("fastest")

for i in range(72):
    timmy.color((random.random(), random.random(), random.random()))
    timmy.circle(100)
    timmy.left(5)

screen.exitonclick()

# Creating a Painting

from turtle import Turtle, Screen
import random

timmy = Turtle()
screen = Screen()

timmy.shape("circle")
timmy.shapesize(0.5,0.5)
timmy.speed("fastest")

for j in range(30):
    for i in range(30):
        timmy.color((random.random(), random.random(), random.random()))
        timmy.dot(10)
        timmy.penup()
        timmy.forward(20)
        timmy.pendown()

    timmy.penup()
    timmy.left(90)
    timmy.forward(20)
    timmy.left(90)
    timmy.forward(600)
    timmy.right(180)

screen.exitonclick()

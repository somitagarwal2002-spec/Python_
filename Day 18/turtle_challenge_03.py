# Drawing Different Shapes

from turtle import Turtle, Screen 
import random

timmy = Turtle()

for n in range(3, 11):
    angle = 180 - (180 * (n - 2)) / n
    timmy.color(random.random(), random.random(), random.random())
    for i in range(n):
        timmy.forward(100)
        timmy.right(angle)

screen = Screen()   
screen.exitonclick()

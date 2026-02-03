# Drawing a Square

from turtle import Turtle, Screen

timmy = Turtle()

for i in range(4):
    timmy.forward(100)
    timmy.right(90)


screen = Screen()
screen.exitonclick()

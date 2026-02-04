# Etch A Sketch Program

from turtle import Turtle, Screen

def move():
    timmy.forward(10)

def back():
    timmy.backward(10)

def clockwise():
    new_heading = timmy.heading() + 10
    timmy.setheading(new_heading)

def anticlockwise():
    new_heading = timmy.heading() - 10
    timmy.setheading(new_heading)

def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()

timmy = Turtle()
screen = Screen()

screen.listen()
screen.onkey(move, "w")
screen.onkey(back,"s")
screen.onkey(clockwise,"a")
screen.onkey(anticlockwise,"d")
screen.onkey(clear, "space")

screen.exitonclick()

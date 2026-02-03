#  Method 1: Importing the whole module
import turtle

timmy = turtle.Turtle()

# Method 2: from import

from turtle import Turtle, Screen

timmy2 = Turtle()
screen = Screen()
screen.exitonclick()

# Method 3: Importing all classes and functions of a module
# It becomes confusing if there are many modules like we chosing 
# methods from which module

from turtle import *

timmy3 = Turtle()
screen2 = Screen()
screen2.exitonclick()

# Method 4: Importing with an alias
# instead of while writing "turtle" we can write "t" where required

import turtle as t

timmy4 = t.Turtle()
screen3 = t.Screen()
screen3.exitonclick()




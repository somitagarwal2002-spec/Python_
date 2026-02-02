# import turtle

# timmy = turtle.Turtle() 


# yha pe humne Turtle() bulayi hai na kyuki iska first alphabet capital 
# hai jo show kr rha hai ki ye ek class hai

# itna import krne se acha hum ye bhi likh skte hai

from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
# object and method
timmy.shape("turtle") # jo screen pr point aayega uska shape
timmy.color("red") # changes color of the shape i.e turtle here
timmy.forward(100) # moves 100 pxl

my_screen = Screen()
# object and attributes
print(my_screen.canvheight)
print(my_screen.canvwidth)

my_screen.exitonclick()
# jo screen hogi wo tb tk nhi jaegi jb tk hum uspe click na kare


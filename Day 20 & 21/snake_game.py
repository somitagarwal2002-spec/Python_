from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import random
import time

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
food =Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detecting collision with food

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # Detecting collision with wall

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Detecting collision with tail

    for segment in snake.segments:
        if segment == snake.head:
            pass

    # upr ye teen likhne se acha hum iss code ko aise bhi likh skte the
    # for segment in snake.segments[1:]:
    # iss line se hume if statement likhne ki zarurat hi nhi padti

        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
        
screen.exitonclick()

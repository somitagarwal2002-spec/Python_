from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

r_paddle = Paddle((350, 0))
l_paddle = Paddle(( -350, 0))
screen = Screen()
ball = Ball()
score = Scoreboard()

screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Ping Pong Game")
screen.listen()
screen.tracer(0) # jo beech mein pehle aa rha tha paddle uska animation hatane ke liye

screen.onkey(r_paddle.up , "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update() # jb tracer apni shi jagah pahuch gya to usko wapas show krne ke liye 
    ball.move()

    # Detecting collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()

    # Detecting collision with r_paddle and l_paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_paddle()

    # Detecting if the ball is out of bound for r_paddle
    if ball.xcor() > 400:
        ball.reset_position()
        score.l_point()

    # Detecting if the ball is out of bound for l_paddle
    if ball.xcor() < -400:
        ball.reset_position()
        score.r_point()

screen.exitonclick()

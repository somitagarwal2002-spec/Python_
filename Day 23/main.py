from turtle import Turtle, Screen
from blocks import Blocks
from player import Player
from scoreboard import Scoreboard
import time

block_manager = Blocks()
player = Player()
score = Scoreboard()

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

t = Turtle()

screen.listen()
screen.onkey(player.up , "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    block_manager.create_block()
    block_manager.move_block()

    # Detecting collision with the block

    for block in block_manager.all_blocks:
        if block.distance(player) < 20:
            game_is_on = False
            score.game_over()

    # Detecting successfully crossed 

    if player.is_at_finish_line():
        block_manager.level_up()
        score.increase_level()

screen.exitonclick()

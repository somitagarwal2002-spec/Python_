from turtle import Turtle, Screen
import random
import time

screen = Screen()
screen.bgcolor("black")
screen.screensize(canvheight=500, canvwidth=300)
screen.bgcolor("black")

COLOR = ["red", "green", "blue", "yellow", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class Blocks(Turtle):
    def __init__(self):
        super().__init__()
        self.all_blocks = []
        self.block_speed = STARTING_MOVE_DISTANCE

    def create_block(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_block = Turtle("square")
            new_block.shapesize(stretch_wid=1, stretch_len=2)
            new_block.color(random.choice(COLOR))
            new_block.penup()
            random_y = random.randint(-250, 250)
            new_block.goto(300, random_y)
            self.all_blocks.append(new_block)

    def move_block(self):
        for block in self.all_blocks:
            block.backward(self.block_speed)
        
    def level_up(self):
        self.block_speed += MOVE_INCREMENT




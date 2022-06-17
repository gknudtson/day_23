from turtle import Turtle
from random import choice, randint
import screen_config
import scoreboard
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = -5
MOVE_INCREMENT = 10
shape_stretch_x = 2
shape_stretch_y = 1
car_length = shape_stretch_x * 20
car_height = shape_stretch_y * 20
ycor_range = screen_config.SCREEN_HEIGHT/2 - car_height * 2
random_ycor = randint(-ycor_range, ycor_range)


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('square')
        self.setheading(180)
        self.level = 1
        self.goto(x=screen_config.SCREEN_WIDTH/2, y=random_ycor)
        self.shapesize(shape_stretch_y, shape_stretch_x)
        self.color(choice(COLORS))
        self.speed_increase = MOVE_INCREMENT * self.level

    def car_move(self):
        self.forward(STARTING_MOVE_DISTANCE + self.speed_increase)

    def car_level(self):
        self.level += 1

    def car_reset(self):
        if self.xcor() <= -(screen_config.SCREEN_WIDTH/2):
            self.goto(x=screen_config.SCREEN_WIDTH / 2, y=random_ycor)
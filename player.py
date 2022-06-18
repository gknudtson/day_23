from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
shape_stretch_x = 1
shape_stretch_y = 1
player_length = shape_stretch_x * 20
player_height = shape_stretch_y * 20


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.shapesize(shape_stretch_y, shape_stretch_x)
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def player_up(self):
        self.forward(MOVE_DISTANCE)

    def player_reset(self):
        self.goto(STARTING_POSITION)

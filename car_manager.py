from turtle import Turtle
from random import choice, randint
import screen_config

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 3
MOVE_INCREMENT = 7
shape_stretch_x = 2
shape_stretch_y = 1
car_length = shape_stretch_x * 20
car_height = shape_stretch_y * 20
ycor_range = screen_config.SCREEN_HEIGHT / 2 - car_height * 2
level = 1


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.car_list = []
        self.hideturtle()
        self.penup()
        self.goto(x=screen_config.SCREEN_WIDTH / 2, y=0)

    def make_car(self):
        random_chance = randint(0, 110 - level * 10)
        if random_chance <= 20:
            random_ycor = randint(-ycor_range, ycor_range)
            new_car = Turtle()
            new_car.speed(0)
            new_car.penup()
            new_car.shape('square')
            new_car.setheading(180)
            new_car.goto(x=screen_config.SCREEN_WIDTH / 2, y=random_ycor)
            new_car.shapesize(shape_stretch_y, shape_stretch_x)
            new_car.color(choice(COLORS))
            self.car_list.append(new_car)

    def car_move(self):
        speed_increase = MOVE_INCREMENT * level
        for car in self.car_list:
            car.forward(STARTING_MOVE_DISTANCE + speed_increase)

    def car_delete(self):
        for i in self.car_list:
            if i.xcor() < -screen_config.SCREEN_WIDTH / 2:
                i.hideturtle()
                self.car_list.remove(i)

    @staticmethod
    def car_level():
        global level
        level += 1

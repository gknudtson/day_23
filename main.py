import time
import screen_config
from turtle import Screen
import player
from car_manager import CarManager
from scoreboard import Scoreboard

# Screen Setup
screen = Screen()
screen.setup(width=screen_config.SCREEN_WIDTH, height=screen_config.SCREEN_HEIGHT)
screen.tracer(0)
screen.listen()
# Level Tracker
score = Scoreboard()
# Player
player_1 = player.Player()
screen.onkeypress(player_1.player_up, 'w')
# CarManager
car_list = []
for car in range(10):
    cars = CarManager()
    car_list.append(car)
# Game Loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.car_move()
    car.car_reset()
    if player_1.ycor() >= player.FINISH_LINE_Y:
        player_1.player_reset()
        score.add_score()
        car.car_level()

# TODO implement car collision game over logic, generate multiple cars, generate car reset logic, recheck scoring logic

import time
import car_manager
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
car = CarManager()
# Game Loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    # make, move, and delete cars once off-screen
    car.make_car()
    car.car_move()
    car.car_delete()
    # check if player has crossed finish line increases level along with difficulty and resets player to start
    if player_1.ycor() >= player.FINISH_LINE_Y:
        player_1.player_reset()
        score.add_score()
        car.car_level()
    # detect collision
    for i in car.car_list:
        bottom = i.ycor() - car_manager.car_height / 2
        top = i.ycor() + car_manager.car_height / 2
        left = i.xcor() - car_manager.car_length / 2
        right = i.xcor() + car_manager.car_length / 2
        if left < player_1.xcor() < right and bottom < player_1.ycor() < top:
            score.game_over()
            game_is_on = False

screen.exitonclick()

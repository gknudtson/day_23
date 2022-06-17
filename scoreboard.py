from turtle import Turtle
import screen_config

FONT = ("Courier", 24, "bold")
ALIGN = 'left'
font_size = 24
score_x = -(screen_config.SCREEN_WIDTH / 2) + font_size
score = 1
score_y = (screen_config.SCREEN_HEIGHT / 2) - font_size * 2


class Scoreboard(Turtle):
    def __init__(self):
        self.score = 0
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('black')
        self.setposition(score_x, score_y)
        self.write(f'Level: {score}', move=False, align=ALIGN, font=FONT)

    def add_score(self):
        global score
        score += 1
        self.clear()
        self.write(f'Level: {score}', move=False, align=ALIGN, font=FONT)

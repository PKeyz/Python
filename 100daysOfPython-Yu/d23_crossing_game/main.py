import time
from turtle import Screen
import player
import car_manager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)
player = player.Player()

screen.listen()
#player control buttons
screen.onkeypress(player.move_up, "w")
screen.onkeypress(player.move_up, "W")
screen.onkeypress(player.move_up, "Up")

car = car_manager.CarManager()
#game
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()


screen.exitonclick()

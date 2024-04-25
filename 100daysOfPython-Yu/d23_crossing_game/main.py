import time
from turtle import Screen
import player
import car_manager
import scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)
player = player.Player()
car = car_manager.CarManager()
scoreboard = scoreboard.Scoreboard()

screen.listen()
#player control buttons
screen.onkeypress(player.move_up, "w")
screen.onkeypress(player.move_up, "W")
screen.onkeypress(player.move_up, "Up")

#game
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move_left()
    car.vanish()

    if player.ycor() >= 290:
        scoreboard.increment_score()
        scoreboard.display()
        player.reset_pos()
        car.increase_cars_chance()
        car.increase_cars_speed()

screen.exitonclick()

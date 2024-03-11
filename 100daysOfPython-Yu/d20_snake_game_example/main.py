from turtle import Screen
import snake
import random
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game Example')
screen.tracer(0)

snake = snake.Snake()

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


screen.exitonclick()

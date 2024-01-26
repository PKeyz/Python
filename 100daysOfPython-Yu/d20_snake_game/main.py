import turtle
import functions

#TODO 0. init snake game

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')

snake = turtle.Turtle('square')
snake.color('white')
snake.penup()
snake.shapesize(1, 3)

is_running = True
while is_running:
    snake.forward(1)






















screen.exitonclick()


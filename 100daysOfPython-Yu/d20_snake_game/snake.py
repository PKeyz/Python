import turtle

SIZE = 20
COLOR = 'green'
SHAPE = 'square'


# TODO 1. create snake body
# a)define 1 unit of body
# b)start game with 3 units
def create_one_snake(x: int, y: int):
    snake = turtle.Turtle(SHAPE)
    snake.color('black')
    snake.penup()
    snake.setposition(x, y)
    snake.color(COLOR)
    return snake

class Snake:
    def __init__(self):
        pass

    # TODO 2. move the snake
    def move_left(NONE):
        turtle.setheading(180)
        turtle.forward(20)

    def move_right(NONE):
        turtle.setheading(0)
        turtle.forward(20)

    def move_up(NONE):
        turtle.setheading(90)
        turtle.forward(20)

    def move_down(NONE):
        turtle.setheading(270)
        turtle.forward(20)



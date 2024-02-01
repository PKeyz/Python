import turtle
import random


# TODO 1. create snake body
# a)define 1 unit of body
# b)start game with 3 units

def create_one_snake(x: int, y: int, color: str):
    snake = turtle.Turtle('square')
    snake.color('black')
    snake.penup()
    snake.setposition(x, y)
    snake.color(color)
    return snake


# TODO 2. move the snake
def move_left():
    turtle.left(90)


def move_right():
    turtle.right(90)


# TODO 3. create snake food
# TODO 4. detect collision with food
# TODO 5. create a scoreboard
# TODO 6. detect collision with wall
# TODO 7. detect collision with tail


def define_rand_coordinate():
    """
    defines a random position on the 600*600 screen
    """
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    coordinate = (x, y)
    return coordinate


# def new_food_pos():
#     new_position = ()
#     is_used = True
#     while is_used:
#         temp_coordinate = define_rand_coordinate()
#         if temp_coordinate !=  coordinates of snake turtles
#             new_position = temp_coordinate
#             is_used = False
#             return new_position
#         else:
#             continue

def create_food(new_food_pos):
    x = new_food_pos()[0]
    y = new_food_pos()[1]
    create_one_snake(x, y, 'blue')

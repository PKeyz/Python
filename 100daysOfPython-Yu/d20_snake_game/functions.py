import turtle
import random

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
    coordinate = [x, y]
    return coordinate


def create_food():
    new_food_pos = define_rand_coordinate()
    x = new_food_pos[0]
    y = new_food_pos[1]
    create_one_snake(x, y, 'blue')


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


def left():
    turtle.left(90)


def right():
    turtle.right(90)

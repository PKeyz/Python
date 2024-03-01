import turtle
import random
import functions as f

FOOD_COLOR = 'red'
SHAPE = 'circle'


class Food:
    def __init__(self):
        pass

    def create_food(self):
        food = turtle.Turtle()
        food.shape(SHAPE)
        food.color(FOOD_COLOR)
        food_coordinate = f.define_rand_coordinate()
        x = food_coordinate[0]
        y = food_coordinate[1]
        food.setposition(x, y)
        return food

import turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.y_move = 0
        self.x_move = 0
        self.speed = 0
        self.amount_cars_chance = 1

    def create_car(self):
        random_chance = random.randint(self.amount_cars_chance, 10)
        if random_chance == 10:
            new_car = turtle.Turtle('square')
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.color(COLORS[random.randint(0, 5)])
            new_car.speed(STARTING_MOVE_DISTANCE)
            self.speed = STARTING_MOVE_DISTANCE
            new_car.goto(280, random.randint(-250, 250))
            new_car.setheading(180)
            new_car.y_move = self.ycor()
            new_car.x_move = 280
            self.all_cars.append(new_car)

    def move_left(self):
        for car in self.all_cars:
            car.forward(STARTING_MOVE_DISTANCE)

    def increase_cars_chance(self):
        self.amount_cars_chance += 0.3

    def increase_cars_speed(self):
        self.speed += MOVE_INCREMENT

    def vanish(self):
        for car in self.all_cars:
            if car.xcor() <= (-300):
                car.reset()

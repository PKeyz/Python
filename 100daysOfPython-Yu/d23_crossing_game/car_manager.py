import turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shapesize(1, 2)
        self.penup()
        self.color(COLORS[random.randint(0, 5)])
        self.speed(STARTING_MOVE_DISTANCE)
        self.goto(280, random.randint(-280, 280))
        self.setheading(180)
        self.shape('square')
        self.y_move = self.ycor()
        self.x_move = 280
        self.screen.ontimer(self.move_left, 5)


    def move_left(self):
        new_x = self.xcor() - self.speed()
        self.goto(new_x, self.ycor())
        if self.xcor() <= -320:
            self.reset()


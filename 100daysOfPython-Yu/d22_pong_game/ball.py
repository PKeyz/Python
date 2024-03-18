import turtle
import random


STARTING_POSITION_1 = (0, 300)
STARTING_POSITION_2 = (0, -300)
SPEED = "fastest"
HEADING_UP = 90
HEADING_DOWN = 270
HEADING_LEFT = 180
HEADING_RIGHT = 0


class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(0.7)
        self.penup()
        self.color('white')
        self.speed(SPEED)
        self.random_start_direction()

    def random_start_direction(self):
        """
        return a random vector to start the pong game with
        """
        y = random.randint(0, 1)
        if y == 0:
            self.goto(STARTING_POSITION_1)
            self.setheading(HEADING_DOWN)
        else:
            self.goto(STARTING_POSITION_2)
            self.setheading(HEADING_UP)

        direction = random.randint(1, 179)
        if direction <= 90:
            self.left(direction)
        elif direction > 90:
            self.right(direction - 90)

    def ball_move(self):
        """
        define continuous ball movement
        """
        self.forward(40)

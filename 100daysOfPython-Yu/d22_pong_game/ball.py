import turtle
import random
import math

# Define constants
TOP_EDGE = 280
BOTTOM_EDGE = -280

STARTING_POSITION_1 = (0, 300)
STARTING_POSITION_2 = (0, -300)
SPEED = "slowest"
HEADING_UP = 90
HEADING_DOWN = 270
HEADING_LEFT = 180
HEADING_RIGHT = 0

TOP_EDGE_ANGLE = 0
BOTTOM_EDGE_ANGLE = 180
LEFT_EDGE_ANGLE = 90
RIGHT_EDGE_ANGLE = -90


class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(1)
        self.penup()
        self.color('white')
        self.speed(SPEED)
        self.goto(0, 0)
        self.random_direction()
        # self.x_move = 10
        # self.y_move = 10
        # self.forward(10)

    def random_direction(self):
        """
        return a random vector to start the pong game with
        """
        self.setheading(random.randint(0, 359))

    def check_bounce(self):
        y = self.ycor()
        if y >= TOP_EDGE or y <= BOTTOM_EDGE:
            self.bounce()

    def bounce(self):
        self.y_move *= -1

    def ball_move(self):
        """
        define continuous ball movement
        """
        self.forward(10)

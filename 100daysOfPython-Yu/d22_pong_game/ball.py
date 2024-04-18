import turtle
import random
import math

# Define constants
TOP_EDGE = 290
BOTTOM_EDGE = -290
LEFT_EDGE = -385
RIGHT_EDGE = 385


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


        def random_direction(self):
            """
                        return a random vector to start the pong game with
                        """
            self.setheading(random.randint(0, 359))

        def check_bounce(self):
            y = self.ycor()
            x = self.xcor()
            if y >= TOP_EDGE or y <= BOTTOM_EDGE:
                self.bounce()


        def bounce(self):
            self.setheading(self.heading() * (-1))

        def ball_move(self):
            """
                                define continuous ball movement
                                """
            self.forward(10)

        # elif (x - 10) == LEFT_EDGE or (x + 10) == RIGHT_EDGE:




















import turtle

STARTING_POSITION_1 = (-575, 0)
STARTING_POSITION_2 = (570, 0)
SPEED = 200
HEADING_UP = 90
HEADING_DOWN = 270


class Racket(turtle.Turtle):
    """
    position left of right to create racket 1( left ) and 2 ( right )
    """

    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.shapesize(1, 4)
        self.penup()
        self.color('white')
        self.speed(SPEED)

        if position == 'left':
            self.goto(STARTING_POSITION_1)
            self.setheading(HEADING_UP)
        elif position == 'right':
            self.goto(STARTING_POSITION_2)
            self.setheading(HEADING_UP)

    def move_up(self):
        self.setheading(HEADING_UP)
        self.forward(10)

    def move_down(self):
        self.setheading(HEADING_DOWN)
        self.forward(10)

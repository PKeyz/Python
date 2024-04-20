import turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
SPEED = 'fastest'


class Player(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(STARTING_POSITION)
        self.shape('turtle')
        self.shapesize(1)
        self.color('green')
        self.speed(SPEED)
        self.setheading(90)
        self.score = 0

    def move_up(self):
        old_y = self.ycor()
        self.goto(0, old_y + MOVE_DISTANCE)

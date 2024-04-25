import turtle

MOVEMENT = False
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(-270, 270)

    def display(self):
        self.clear()
        self.write(f"Score: {self.score}", MOVEMENT, ALIGNMENT, FONT)

    def increment_score(self):
        self.score += 0.3

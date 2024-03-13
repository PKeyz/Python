from turtle import Turtle

MOVEMENT = False
ALIGNMENT = "center"
FONT = ("Courier", 15, "bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(0, 270)

    def display(self):
        self.clear()
        self.write(f"Score: {self.score}", MOVEMENT, ALIGNMENT, FONT)

    def increase_score(self):
        self.score += 1

    def print_game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", MOVEMENT, ALIGNMENT, FONT)
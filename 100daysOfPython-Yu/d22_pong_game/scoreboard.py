import turtle

DASHES = 50
DASH_STEPS_VISIBLE = 9
DASH_STEPS_INVISIBLE = 16
DASH_PENSIZE = 5
MOVEMENT = False
ALIGNMENT = "center"
FONT = ("Courier", 15, "bold")


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score_1 = 0
        self.score_2 = 0
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(0, 300)

    def dashed_line(self):
        self.setheading(270)
        self.speed('fastest')
        self.pensize(DASH_PENSIZE)
        x = 0
        while x < DASHES:
            self.pendown()
            self.forward(DASH_STEPS_VISIBLE)
            self.penup()
            self.forward(DASH_STEPS_INVISIBLE)
            x += 1
    def display(self):
        self.clear()
        self.write(f"{self.score_1} : {self.score_2}", MOVEMENT, ALIGNMENT, FONT)

    def increase_score(self,player_num):
        if player_num == 1:
            self.score_1 += 1
        elif player_num == 2:
            self.score_2 += 1

    def print_game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", MOVEMENT, ALIGNMENT, FONT)

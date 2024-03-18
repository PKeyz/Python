import time
from turtle import Turtle, Screen
import racket
import scoreboard
import ball

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("My Pong Game")
screen.tracer(0)

# create classes here
scoreboard = scoreboard.Scoreboard()
racket_1 = racket.Racket('left')
racket_2 = racket.Racket('right')
ball = ball.Ball()


screen.listen()
# screen.onkey(fun, "key")
screen.onkeypress(racket_1.move_up, "w")
screen.onkeypress(racket_1.move_down, "s")
screen.onkeypress(racket_2.move_up, "Up")
screen.onkeypress(racket_2.move_down, "Down")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    # scoreboard.dashed_line()
    # scoreboard.display()
    ball.ball_move()

    pass

screen.exitonclick()

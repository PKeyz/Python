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
racket_l = racket.Racket('left')
racket_r = racket.Racket('right')
ball = ball.Ball()


screen.listen()
# screen.onkey(fun, "key")
screen.onkeypress(racket_l.move_up, "w")
screen.onkeypress(racket_l.move_down, "s")
screen.onkeypress(racket_r.move_up, "Up")
screen.onkeypress(racket_r.move_down, "Down")

ball.random_direction()

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    # scoreboard.dashed_line()
    # scoreboard.display()
    ball.ball_move()

    if ball.distance(racket_l.pos())< 20 or ball.distance(racket_r.pos())< 20:
        ball.bounce()








screen.exitonclick()

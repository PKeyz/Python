from turtle import Screen
from snake import Snake
from food import Food
import scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game Example')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = scoreboard.Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        scoreboard.display()

    # detect collision with wall
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        scoreboard.print_game_over()
        is_game_on = False
    """
    # Detect collision with tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.print_game_over()
            is_game_on = False
    # if head collides with any segment in tail :
    # trigger scoreboard.game_over
    """

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.print_game_over()
            is_game_on = False

screen.exitonclick()

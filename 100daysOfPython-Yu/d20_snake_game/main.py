import turtle
import time
import functions as f
import snake as sn
import food as fo

# TODO 0. init snake game

GAME_WIDTH = 600
GAME_HEIGHT = 600
SCREEN_BG_COLOR = 'black'
SCREEN_TITLE = 'My Snake Game'

screen = turtle.Screen()
screen.setup(width=GAME_WIDTH, height=GAME_HEIGHT)
screen.bgcolor(SCREEN_BG_COLOR)
screen.title(SCREEN_TITLE)

snake_lst = []

# initial snake at game start
starting_positions = [(0, 0), (-20, 0), (-40, 0)]

SHAPE = 'square'

i = 0
j = 1
for x in range(3):
    snake = (sn.create_one_snake(starting_positions[x][i], starting_positions[x][j]))
    snake_lst.append(snake)

is_running = True
while is_running:
    screen.update()
    time.sleep(.5)

    for snake in snake_lst:
        old_x: int
        old_y: int

        turtle.listen()

        turtle.onkey(sn.Snake.move_left, 'Left')
        turtle.onkey(sn.Snake.move_right, 'Right')
        turtle.onkey(sn.Snake.move_up, 'Up')
        turtle.onkey(sn.Snake.move_down, 'Down')

        snake.forward(20)

        if snake_lst[0]:
            turtle.listen()

            snake.onkey(sn.Snake.move_up(), 'Up')
            old_x = snake.xcor()
            old_y = snake.ycor()

        elif not snake_lst[0]:
            current_x = snake.xcor()
            current_y = snake.ycor()

            snake.setposition(old_x, old_y)

            old_x = current_x
            old_y = current_y

turtle.mainloop()
screen.exitonclick()

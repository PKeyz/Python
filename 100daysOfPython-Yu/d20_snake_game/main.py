import turtle
import functions as f

# TODO 0. init snake game

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')

snake_lst = []

# initial snake at game start
starting_positions = [(0, 0), (-20, 0), (-40, 0)]

# food example
# f.create_one_snake(0, 70, 'blue')

i = 0
j = 1
for x in range(3):

    snake = f.create_one_snake(starting_positions[x][i], starting_positions[x][j], 'red')
    snake_lst.append(snake)

is_running = True
while is_running:
    # snake = f.create_food()

    for snake in snake_lst:
        snake.forward(5)

screen.exitonclick()

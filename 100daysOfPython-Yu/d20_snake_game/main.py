import turtle
import time
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
    screen.update()
    time.sleep(.5)

    for snake in snake_lst:
        turtle.listen()

        snake_index = snake_lst.index(snake)
        old_position = snake.pos()

        turtle.onkey(f.left, "a")
        turtle.onkey(f.right, "d")


        snake.forward(20)

        new_position = snake.pos()
        starting_positions[snake_index] = new_position
        #print(starting_positions)

    if snake.pos()[0] > 300 or snake.pos()[1] > 300:
        print('Game Over')
        is_running = False
    elif snake.pos() in starting_positions:
        print('Game Over')
        is_running = False
turtle.mainloop()
screen.exitonclick()

import turtle
import functions

#TODO 0. init snake game

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')

snake_lst = []

# snake_lst.append(functions.create_one_snake(0, 0, 'red'))
# snake_lst.append(functions.create_one_snake(-20, 0, 'red'))
# snake_lst.append(functions.create_one_snake(-40, 0, 'red'))
starting_positions = [(0, 0), (-20, 0), (-40, 0)]

#food example
functions.create_one_snake(0, 70, 'blue')

i = 0
j = 1
for x in range(3):
    snake = functions.create_one_snake(starting_positions[x][i], starting_positions[x][j], 'red')
    snake_lst.append(snake)

print(snake_lst)
is_running = True
while is_running:
    for snake in snake_lst:
        snake.forward(100)
    is_running = False




















screen.exitonclick()


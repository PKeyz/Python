import turtle
import functions

#TODO 0. init snake game

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')
screen.title('My Snake Game')

snake_lst = []
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
# snake_lst.append(functions.create_one_snake(0, 0, 'red'))
# snake_lst.append(functions.create_one_snake(-20, 0, 'red'))
# snake_lst.append(functions.create_one_snake(-40, 0, 'red'))
functions.create_one_snake(-50, 70, 'blue')

i = 0
j = 0
for x in range(3):
    snake_lst.append(functions.create_one_snake(starting_positions[i][j], starting_positions[i][j], 'red'))
    i += 1
    j += 1

# is_running = True
# while is_running:
#     for snake in snake_lst:
#         snake.forward(1)






















screen.exitonclick()


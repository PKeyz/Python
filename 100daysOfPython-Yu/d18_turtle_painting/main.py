import turtle
import random

phil_turtle = turtle.Turtle()
phil_turtle.shape('classic')
phil_turtle.color('red2')

# # turtle square
# for x in range(4):
#     phil_turtle.forward(100)
#     phil_turtle.right(90)

# # draw dashed line: line 10 gap 10 repeat 50 times
# for x in range(15):
#     phil_turtle.forward(10)
#     phil_turtle.penup()
#     phil_turtle.forward(10)
#     phil_turtle.pendown()

# Draw triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, decagon in sequence
# from the same starting position
# changing to a random color for each row

counter = 0
distance = 100
shapes = [
    {'shape': 'triangle',
     'sides': 3,
     'angles': 120},
    {'shape': 'square',
     'sides': 4,
     'angles': 90},
    {'shape': 'pentagon',
     'sides': 5,
     'angles': 72},
    {'shape': 'hexagon',
     'sides': 6,
     'angles': 60},
    {'shape': 'heptagon',
     'sides': 7,
     'angles': 51 + 3/7},
    {'shape': 'octagon',
     'sides': 8,
     'angles': 45},
    {'shape': 'nonagon',
     'sides': 9,
     'angles': 40},
    {'shape': 'decagon',
     'sides': 10,
     'angles': 36}
]
color = f'#{random.randrange(256**3):06x}'

while counter < 8:
    color = f'#{random.randrange(256 ** 3):06x}'
    phil_turtle.color(color)

    for y in range(shapes[counter].get('sides')):
        phil_turtle.forward(distance)
        phil_turtle.right(shapes[counter].get('angles'))
    counter += 1




# must be at the end of the code to visualize, else returns empty screen
screen = turtle.Screen()
screen.exitonclick()
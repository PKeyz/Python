import turtle

phil_turtle = turtle.Turtle()
phil_turtle.shape('classic')
phil_turtle.color('red2')

# turtle square
for x in range(4):
    phil_turtle.forward(100)
    phil_turtle.right(90)


# must be at the end of the code to visualize, else returns empty screen
screen = turtle.Screen()
screen.exitonclick()
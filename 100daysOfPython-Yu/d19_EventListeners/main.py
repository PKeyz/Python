import turtle

phil_turtle = turtle.Turtle()
# keep last to visualize the actions propertly
screen = turtle.Screen()


def move_forward():
    phil_turtle.speed(5)
    phil_turtle.forward(10)

def move_backwards():
    phil_turtle.speed(5)
    phil_turtle.backward(10)

def move_left():
    newheading = phil_turtle.heading() + 10
    phil_turtle.setheading(newheading)

def move_right():
    newheading = phil_turtle.heading() - 10
    phil_turtle.setheading(newheading)

def clear_screen():
    turtle.resetscreen()

screen.listen()
screen.onkeypress(move_forward, 'w')
screen.onkeypress(move_backwards, "s")
screen.onkeypress(move_left, "a")
screen.onkeypress(move_right, "d")
screen.onkeypress(clear_screen, "c")

screen.exitonclick()


# WASD buttons for movement in according directions -> drawing lines in this direction while holding key pressed
#     clear screen via "C" button
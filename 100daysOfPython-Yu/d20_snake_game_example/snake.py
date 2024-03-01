import turtle


class Snake:
    snake_shape: str
    snake_color: str
    xcord: int
    ycord: int
    snake_lst: []
    starting_positions: []

    def __init__(self):
        snake = turtle.Turtle(self.snake_shape)
        snake_shape: str = 'square'
        snake_color: str = 'white'
        starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        snake_lst = []

        i = 0
        j = 1
        for x in range(3):
            snake = turtle.Turtle(snake_shape)
            snake.color('black')
            snake.penup()
            snake.setposition(starting_positions[x][i], starting_positions[x][j])
            snake.color(snake_color)
            snake_lst.append(snake)

    def move(self):
        distance = 20
        self.snake_lst: []
        self.starting_positions: []

        is_running = True
        while is_running:
            # screen.update()
            # time.sleep(.5)

            for snake in self.snake_lst:
                snake_index = self.snake_lst.index(snake)
                old_position = snake.pos()

                snake.forward(20)

                new_position = snake.pos()
                self.starting_positions[snake_index] = new_position

    # def
    #     for snake in snake_lst:
    #         turtle.listen()
    #
    #         snake_index = snake_lst.index(snake)
    #         old_position = snake.pos()
    #
    #         turtle.onkey(f.left, "a")
    #         turtle.onkey(f.right, "d")
    #
    #         snake.forward(20)
    #
    #         new_position = snake.pos()
    #         starting_positions[snake_index] = new_position

import turtle
import pandas

screen = turtle.Screen()

text = turtle.Turtle()
text.hideturtle()


class PopUp(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.retry = 0
        self.correct_answers = 0
        self.state_data = self.read_csv_to_dict()
        self.correct_answers_list = []

    def read_csv_to_dict(self):

        """reading the csv file and converting it to a readeable format; returning a dict with states==key: x and y
        == value"""
        states_data = pandas.read_csv('50_states.csv')

        states_data_dict = states_data.to_dict()

        # Refactored dictionary
        refactored_state_data = {}

        # Iterate over the 'state' column and construct the refactored dictionary
        for i in range(len(states_data_dict['state'])):
            state_name = states_data_dict['state'][i]  # Get the state name
            x_value = states_data_dict['x'][i]  # Get the corresponding x value
            y_value = states_data_dict['y'][i]  # Get the corresponding y value
            refactored_state_data[state_name] = {'x': x_value, 'y': y_value}

        # Print the refactored dictionary
        return refactored_state_data

    def count_correct(self, state: str):
        """counting correct answers and returning a single integer"""
        state = state
        self.correct_answers_list.append(state)
        self.correct_answers += 1

    def user_input(self):
        """returns user input"""
        answer = screen.textinput(f"{self.correct_answers}/50 States correct!", "What's another state name?").title()
        return answer

    def evaluate_answer(self, answer: str):
        """evaluates the answer and returns True if the answer is in the dictionary, False otherwise"""
        if answer in self.state_data:
            self.count_correct(answer)
            return True

        elif answer not in self.state_data and answer != 'Exit':
            print("State not in the US! Try again!")
            self.retry += 1
            return False

    def return_coordinates(self, state: str):
        """returns coordinates of the state, if key available in read_csv_to_dict()"""
        coordinates = self.state_data[state]
        return coordinates

    def print_coordinates(self, coordinates):
        """prints the state name on the map at the corresponding x and y coordinates"""
        text.goto(coordinates['x'], coordinates['y'])
        text.write(f'{self.correct_answers_list[-1]}', align='center', font=('Arial', 8, 'normal'))

    def terminate_game(self):
        """finish the game after 3 wrong inputs from the user and return False to the main loop"""
        if self.retry == 3:
            termination = screen.textinput(f"To many mistakes,\ngame terminated!",
                                      f"{self.correct_answers}/50 States correct!\n{self.retry} states wrong! Try again")
            return termination

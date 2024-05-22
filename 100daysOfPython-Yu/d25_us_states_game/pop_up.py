import turtle
import pandas

screen = turtle.Screen()

text = turtle.Turtle()


class PopUp:
    def __init__(self):
        super().__init__()
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

    # def show_window(self):
    #     """create a pop-up window in the screen to input answers of the user"""
    #     #input var for correct states from dict
    #     answer = screen.textinput(f"{self.correct_answers}/50 States correct!", "What's another state name?").title()
    #
    #     return answer

    def evaluate_answer(self):
        answer = screen.textinput(f"{self.correct_answers}/50 States correct!", "What's another state name?").title()
        if answer in self.read_csv_to_dict():
            self.count_correct(answer)
            return answer

        else:
            print("State not in the US! Try again!")
            # self.retry += 1
            # if self.retry == 3:
            #     print('To many mistakes, game terminated!')

    def return_coordinates(self, state: str):
        """returns coordinates of the state, if key available in read_csv_to_dict()"""
        state_dict = self.read_csv_to_dict()
        coordinates = state_dict[state]
        return coordinates

import turtle
import pandas

screen = turtle.Screen()

class PopUp:
    def __init__(self):
        super().__init__()
        self.show_window()

    def read_csv_to_dict(self):
        """reading the csv file and converting it to a readeable format; returning a dict/list #find out what is better"""
        """reading the csv file and converting it to a readeable format; returning a dict/list #find out what is better"""
        states_data = pandas.read_csv('50_states.csv')

        states_data_dict = states_data.to_dict()
        # print(states_data_dict)

        # Refactored dictionary
        refactored_state_data = {}

        # Iterate over the 'state' column and construct the refactored dictionary
        for i in range(len(states_data_dict['state'])):
            state_name = states_data_dict['state'][i]  # Get the state name
            x_value = states_data_dict['x'][i]  # Get the corresponding x value
            y_value = states_data_dict['y'][i]  # Get the corresponding y value
            refactored_state_data[state_name] = {'x': x_value, 'y': y_value}

        # Print the refactored dictionary
        print(refactored_state_data)


    def check_correctness(self):
        """check if user input fits the states in the states dict/list"""
    def count_correct(self):
        """counting correct answers and returning a single int"""
    def show_window(self):
        """create a pop-up window in the screen to input answers of the user"""
        #input var for correct states from csv|| dict|| list
        answer = screen.textinput(f"2/50 States correct!", "What's another state name?")
        if answer is None or answer.lower().startswith('n'):
            print("Goodbye!")
            screen.clear()
            screen.bye()
        else:
            print("Start!")

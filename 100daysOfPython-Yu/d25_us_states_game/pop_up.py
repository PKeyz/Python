import turtle

screen = turtle.Screen()

class PopUp:
    def __init__(self):
        super().__init__()
        self.show_window()

    def read_csv(self):
        """reading the csv file and converting it to a readeable format; returning a dict/list #find out what is better"""

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

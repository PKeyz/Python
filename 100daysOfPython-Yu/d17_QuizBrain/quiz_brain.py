# TODO 4. asking the questions
# TODO 5. checking if the answer was correct
# TODO 6. checking if we're at the end of the quiz

# create class QuizBrain
# Write an __init__() method

class QuizBrain:
    def __init__(self, q_list: list):
        self.question_number: int = 0
        self.question_list: list = q_list

    # TODO 7. retrieve item at current question_number from question_list.
    # use input() to show the user the Question text and ask for user's answer.
    def next_question(self):
        user_answer = bool(
            input(f'Q.{self.question_number + 1}: {self.question_list[self.question_number].text} (True/False): '))
        self.question_number += 1
        return user_answer

# TODO 3. with custom names -> generate custom Obj. QUESTION with different text/answer
# TODO 4. append Obj. QUESTION to question_bank[]


import data
import question_model

# new_question = question_model.Question()
question_bank = []
question_counter: int = 0


def generate_question_objects(text, answer):
    global question_counter
    for _ in data.question_data:
        question_object = question_model.Question(text, answer)
        question_bank.append(question_object)
        question_counter += 1


generate_question_objects(data.question_data[question_counter].get('text'),
                          data.question_data[question_counter].get('answer'))

for question in question_bank:
    counter = 0
    print(question_bank[counter].text)
    print(question_bank[counter].answer)
    counter += 1

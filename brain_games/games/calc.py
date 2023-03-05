import random


TASK = 'What is the result of the expression?'


def calc():
    random_number_one = random.randint(1, 10)
    random_number_two = random.randint(1, 10)
    operators = ['+', '-', '*']
    random_operator = random.choice(operators)
    question = f'{random_number_one} {random_operator} {random_number_two}'
    correct_answer = str(eval(f'{random_number_one} {random_operator} {random_number_two}'))
    return question, correct_answer

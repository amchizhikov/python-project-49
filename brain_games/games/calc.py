import random


TASK = 'What is the result of the expression?'


def task():
    random_number_one = random.randint(1, 10)
    random_number_two = random.randint(1, 10)
    operators = ['+', '-', '*']
    random_operator = random.choice(operators)
    result = eval(f'{random_number_one} {random_operator} {random_number_two}')
    question = f'{random_number_one} {random_operator} {random_number_two}'
    correct_answer = str(result)
    return question, correct_answer
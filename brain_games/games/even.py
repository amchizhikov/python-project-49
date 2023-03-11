import random


TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(question):
    dict = {True: 'yes', False: 'no'}
    if question % 2 == 0:
        return dict[True]
    else:
        return dict[False]


def task():
    RANDOM_NUMBER = random.randint(1, 100)
    question = RANDOM_NUMBER
    correct_answer = str(is_even(question))
    return question, correct_answer

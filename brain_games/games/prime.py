import random


TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(question):
    dividers = []
    dict = {True: 'yes', False: 'no'}
    for n in range(1, question + 1):
        if question % n == 0:
            dividers.append(n)
    if len(dividers) == 2:
        return dict[True]
    else:
        return dict[False]


def task():
    RANDOM_NUMBER = random.randint(2, 100)
    question = RANDOM_NUMBER
    correct_answer = str(is_prime(question))
    return question, correct_answer

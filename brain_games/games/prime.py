import random


TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(question):
    dividers = []
    for n in range(1, question + 1):
        if question % n == 0:
            dividers.append(n)
    if len(dividers) == 2:
        return 'yes'
    else:
        return 'no'


def task():
    question = random.randint(2, 100)
    correct_answer = str(is_prime(question))
    return question, correct_answer

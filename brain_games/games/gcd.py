import random
from math import gcd


TASK = 'Find the greatest common divisor of given numbers.'


def task():
    RANDOM_ONE = random.randint(1, 100)
    RANDOM_TWO = random.randint(1, 100)
    random_number_one, random_number_two = (
        RANDOM_ONE,
        RANDOM_TWO)
    question = f'{random_number_one} {random_number_two}'
    correct_answer = str(gcd(random_number_one, random_number_two))
    return question, correct_answer

import random


TASK = 'Find the greatest common divisor of given numbers.'


def gcd():
    random_number_one = random.randint(1, 10)
    random_number_two = random.randint(1, 10)
    while random_number_one != 0 and random_number_two != 0:
        if random_number_one > random_number_two:
            random_number_one = random_number_one % random_number_two
        else:
            random_number_two = random_number_two % random_number_one
    result = random_number_one + random_number_two
    question = f'{random_number_one} {random_number_two}'
    correct_answer = str(result)
    return question, correct_answer

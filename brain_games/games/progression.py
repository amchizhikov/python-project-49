import random


TASK = 'What number is missing in the progression?'


def task():
    START = random.randint(1, 5)
    STOP = random.randint(30, 100)
    STEP = random.randint(1, 5)
    random_number_one, random_number_two, random_number_three = (
        START,
        STOP,
        STEP)
    progression = list(range(
        random_number_one,
        random_number_two,
        random_number_three))[:10]
    missing_index = random.randint(0, len(progression) - 1)
    result = progression[missing_index]
    progression[missing_index] = '..'
    progression_for_game = ' '.join(map(str, progression))
    question = progression_for_game
    correct_answer = str(result)
    return question, correct_answer

import random
import operator


TASK = 'What is the result of the expression?'


def task():
    RANDOM_ONE = random.randint(1, 10)
    RANDOM_TWO = random.randint(1, 10)
    random_number_one, random_number_two = (
        RANDOM_ONE,
        RANDOM_TWO)
    operators = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
    }
    random_operator = random.choice(list(operators))
    question = f'{random_number_one} {random_operator} {random_number_two}'
    correct_answer = str(
        operators.get(random_operator)(random_number_one, random_number_two))
    return question, correct_answer

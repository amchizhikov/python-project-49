import prompt
from brain_games.cli import welcome_user


def round_engine(question, correct_answer):
    print(f'Question: {question}')
    answer = prompt.string('Your answer: ')
    if answer.upper() == correct_answer.upper():
        print('Correct!')
        return True
    print(f'''{answer} is wrong answer ;(.
        \rCorrect answer was {correct_answer}.''')
    return False


def game_engine(game):
    name = welcome_user()
    print(game.TASK)
    i = 0
    TRY = 3
    while i < TRY:
        question, correct_answer = game.task()
        if round_engine(question, correct_answer):
            i += 1
        else:
            print(f"Let's try again, {name}!")
            break
    if i == 3:
        print(f'Congratulations, {name}!')

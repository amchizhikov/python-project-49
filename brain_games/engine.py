import prompt
from brain_games.cli import welcome_user


def round_engine(question, correct_answer):
    print(f'Questions: {question}')
    answer = prompt.string('Your answer: ')
    if answer == correct_answer:
        print('Correct!')
        return True
    else:
        print(f'''{answer} is wrong answer ;(.
            \rCorrect answer was {correct_answer}.''')
        return False


def game_engine(game):
    name = welcome_user()
    print(game.TASK)
    i = 0
    while i < 3:
        question, correct_answer = game.task()
        if round_engine(question, correct_answer):
            i += 1
        else:
            print(f"Let's try again, {name}!")
            break
    if i == 3:
        print(f'Congratulations, {name}!')

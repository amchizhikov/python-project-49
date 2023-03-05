#!/usr/bin/env python3
import random


def progression():
    print('Welcome to the Brain Games!')
    name = input('May I have your name? ')
    print(f'Hello, {name}!')
    print('What number is missing in the progression?')
    i = 0
    while i < 3:
        random_number_one = random.randint(1, 5)
        random_number_two = random.randint(30, 100)
        random_number_three = random.randint(1, 5)
        progression = list(range(
            random_number_one,
            random_number_two,
            random_number_three))[:10]
        missing_index = random.randint(0, len(progression) - 1)
        result = progression[missing_index]
        progression[missing_index] = '..'
        progression_for_game = ' '.join(map(str, progression))
        print(f'Questions: {progression_for_game}')
        answer = int(input('Your answer: '))
        if answer == result:
            print('Correct!')
        else:
            print(f'''{answer} is wrong answer ;(. Correct answer was {result}.
            \rLet's try again, {name}!''')
            break
        i += 1
    if i == 3:
        print(f'Congratulations, {name}!')


def main():
    progression()


if __name__ == '__main__':
    main()

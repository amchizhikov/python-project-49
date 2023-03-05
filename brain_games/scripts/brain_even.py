#!/usr/bin/env python3
from random import randint


def is_even():
    print('Welcome to the Brain Games!')
    name = input('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no"')
    i = 0
    while i < 3:
        random_number = randint(1, 100)
        if random_number % 2 == 0:
            result = 'yes'
        else:
            result = 'no'
        print(f'Questions: {random_number}')
        answer = input('Your answer: ')
        if answer == result:
            print('Correct!')
        else:
            print(f"""{answer} is wrong answer ;(. Correct answer was {result}.
            \rLet's try again, {name}!""")
            break
        i += 1
    if i == 3:
        print(f'Congratulations, {name}!')


def main():
    is_even()


if __name__ == '__main__':
    main()

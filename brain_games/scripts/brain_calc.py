#!/usr/bin/env python3
import random


def calc():
    print('Welcome to the Brain Games!')
    name = input('May I have your name? ')
    print(f'Hello, {name}!')
    print('What is the result of the expression?')
    i = 0
    operators = ['+', '-', '*']
    while i < 3:
        random_number_one = random.randint(1, 10)
        random_number_two = random.randint(1, 10)
        random_operator = random.choice(operators)
        print(f'Questions: {random_number_one} {random_operator} {random_number_two}')
        result = eval(f'{random_number_one} {random_operator} {random_number_two}')
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
    calc()

if __name__ == '__main__':
    main()

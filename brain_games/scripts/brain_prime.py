#!/usr/bin/env python3
import random


def is_prime():
    print('Welcome to the Brain Games!')
    name = input('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    i = 0
    while i < 3:
        random_number_one = random.randint(2, 100)
        print(f'Questions: {random_number_one}')
        dividers = []
        for n in range(1, random_number_one + 1):
            if random_number_one % n == 0:
                dividers.append(n)
        if len(dividers) == 2:
            result = 'yes'
        else:
            result = 'no'
        answer = (input('Your answer: '))
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
    is_prime()


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
import random


def gcd():
    print('Welcome to the Brain Games!')
    name = input('May I have your name? ')
    print(f'Hello, {name}!')
    print('Find the greatest common divisor of given numbers.')
    i = 0
    while i < 3:
        random_number_one = random.randint(1, 10)
        random_number_two = random.randint(1, 10)
        print(f'Questions: {random_number_one} {random_number_two}')
        while random_number_one != 0 and random_number_two != 0:
            if random_number_one > random_number_two:
                random_number_one = random_number_one % random_number_two
            else:
                random_number_two = random_number_two % random_number_one
        result = random_number_one + random_number_two
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
    gcd()


if __name__ == '__main__':
    main()

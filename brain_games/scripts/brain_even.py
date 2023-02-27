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
        print(f'Questions: {random_number}')
        answer = input('Your answer: ')
        if random_number % 2 == 0 and answer == 'yes':
            print('Correct!')
        elif random_number % 2 != 0 and answer == 'no':
            print('Correct!')
        elif random_number % 2 != 0 and answer == 'yes':
            print(f"""'yes' is wrong answer ;(. Correct answer was 'no'.
            \rLet's try again, {name}!""")
            break
        elif random_number % 2 == 0 and answer == 'no':
            print(f"""'no' is wrong answer ;(. Correct answer was 'yes'.
            \rLet's try again, {name}!""")
            break
        else:
            print(f"""{answer} is wrong answer ;(. Correct answer
            \rwas 'yes' or 'no'. Let's try again, {name}!""")
            break
        i += 1
    if i == 3:
        print(f'Congratulations, {name}!')


def main():
    is_even()


if __name__ == '__main__':
    main()

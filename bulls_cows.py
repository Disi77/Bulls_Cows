from random import randrange
from time import time


def generate_number():
    number = ''
    while len(number) < 4:
        new_digit = str(randrange(0, 10))
        if new_digit not in number:
            number += new_digit
    return number


def user_guess():
    while True:
        guess = input('>>>')
        print()
        if guess.isdigit() and len(guess) == 4:
            return guess
        else:
            print('Invalid input, try again >>>')


def evaluation(guess, secret_num):
    bulls = 0  # correct number and correct position
    cows = 0  # correct number and INcorrect position
    help_num = ''
    for index, digit in enumerate(guess):
        if digit == secret_num[index] and digit not in help_num:
            bulls += 1
            help_num += digit
    for index, digit in enumerate(guess):
        if digit in secret_num and digit not in help_num:
            cows += 1
            help_num += digit
    return bulls, cows


def time_conversion(time):
    if time < 60:
        sec = round(time)
        return '{} sec'.format(sec)
    if time < 60*60:
        min, sec = divmod(time, 60)
        sec = round(sec)
        return '{} min {} sec'.format(int(min), sec)
    else:
        hod, rest = divmod(time, 60*60)
        min, sec = divmod(rest, 60)
        sec = round(sec)
        return '{} hod {} min {} sec'.format(int(hod), int(min), sec)


def main():
    print(''' Hi there !!!
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
Enter a number.
    ''')
    secret_num = generate_number()
    print('SECRET NUMBER: ', secret_num)
    count_try = 0
    while True:
        guess = user_guess()
        if count_try == 0:
            start = time()
        bulls, cows = evaluation(guess, secret_num)
        print('{} bull{}, {} cow{}'.format(bulls,
                                           's' if bulls > 1 else '',
                                           cows,
                                           's' if cows > 1 else ''))
        count_try += 1
        if bulls == 4:
            end = time()
            user_time = time_conversion(end - start)
            print(user_time)
            print('Correct, you\'ve guessed the right number in {} guesses!'.format(count_try))
            break


main()

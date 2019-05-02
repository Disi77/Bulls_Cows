from random import randrange
from time import time
from operator import itemgetter


def generate_number():
    '''
    Generates a four-digit number, each digit is unique
    Returns this number as string
    '''
    number = ''
    while len(number) < 4:
        new_digit = str(randrange(0, 10))
        if new_digit not in number:
            number += new_digit
    return number


def user_guess():
    '''
    User guess. Valid is only four-digit number,
    but user can use each digit more times.
    '''
    while True:
        guess = input('>>>')
        print()
        if guess.isdigit() and len(guess) == 4:
            return guess
        else:
            print('Invalid input, try again >>>')


def evaluation(guess, secret_num):
    '''
    Evaluation of user guess.
    Bulls = correct number and correct position
    Cows = correct number and INcorrect position
    '''
    bulls = 0
    cows = 0
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
    '''
    Conversion time from sec to hour/min/sec
    '''
    if time < 60:
        sec = round(time)
        return '{} sec'.format(sec)
    if time < 60*60:
        min, sec = divmod(time, 60)
        sec = round(sec)
        return '{} min {} sec'.format(int(min), sec)
    else:
        hour, rest = divmod(time, 60*60)
        min, sec = divmod(rest, 60)
        sec = round(sec)
        return '{} h {} min {} sec'.format(int(hour), int(min), sec)


def statistics(user_time, count_try):
    while True:
        save = input('Do you want save your results? Yes/No ')
        if save.lower() in ['y', 'yes']:
            name = input('Enter your name, max 10 letters ')
            if len(name) > 10:
                name = name[:10]
            result = (name, user_time, count_try)
            write_stat_to_file(result)
            break
        elif save.lower() in ['n', 'no']:
            break
    print_TOP10()


def print_TOP10():
    filename = 'bulls_cows_stat.txt'
    with open(filename) as file:
        results = eval(file.read())
    temp_text = '| {:^2} | {:^10} | {:^15} | {:^10} |'
    temp_line = '=' * 50
    print(temp_line)
    print(temp_text.format('', 'Name', 'Time', 'Tips'))
    print(temp_line)
    for row in range(min(10, len(results))):
        print(temp_text.format(row+1, *results[row]))
    print(temp_line)


def write_stat_to_file(result):
    filename = 'bulls_cows_stat.txt'
    with open(filename) as file:
        results = eval(file.read())
    results.append(result)
    results.sort(key=itemgetter(2))
    with open(filename, 'w') as file:
        file.write(str(results))


def main():
    print(''' Hi there !!!
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
Enter a number.
    ''')
    secret_num = generate_number()
    # print('SECRET NUMBER: ', secret_num)
    count_try = 0
    while True:
        guess = user_guess()
        if count_try == 0:
            start = time()
        bulls, cows = evaluation(guess, secret_num)
        print('{} bull{}, {} cow{}'.format(bulls, 's' if bulls > 1 else '',
                                           cows, 's' if cows > 1 else ''))
        print()
        count_try += 1
        if bulls == 4:
            end = time()
            user_time = time_conversion(end - start)
            print(user_time)
            print('Correct, you\'ve guessed the right number in {} guesses!'.format(count_try))
            statistics(user_time, count_try)
            break


main()

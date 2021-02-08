from sys import argv
from random import randint


def gather_guess(min, max):
    return input(f'Guess a number between {min} and {max}: ')


def evaluate_guess(guess, solution, min, max):
    try:
        int_guess = int(guess)
        if min <= int_guess <= max:
            if int_guess == solution:
                return 'Congratulations, you got it!'
        else:
            return (f'Please enter a number between {min} and {max}!')
    except ValueError:
        return 'Please enter a number in the integer format!'


if __name__ == '__main__':
    # game setup
    try:
        game_min = int(argv[1])
        game_max = int(argv[2])
        solution = randint(game_min, game_max)
    except (IndexError, ValueError) as err:
        raise Exception(f'{err}, please run the script with two integer numbers as command line arguments ' +
                        'to set a minimum (1st number) and a maximum (2nd number) for the guessing game.')

    # guessing game
    while True:
        guess = gather_guess(game_min, game_max)
        result = evaluate_guess(guess, solution, game_min, game_max)
        if result is not None:
            print(result)
        if result == 'Congratulations, you got it!':
            break

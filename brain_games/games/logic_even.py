from random import randint
from brain_games.common_logic import solve, win, convert_bool
from brain_games.constants import RANGE_START, RANGE_STOP_MAX


def is_even(x):
    return x % 2 == 0


def game_even():
    for _ in range(3):
        given_number = randint(RANGE_START, RANGE_STOP_MAX)
        print(f'Question: {given_number}')
        answer = input('Your answer: ')
        result = solve(convert_bool(is_even(given_number)), answer)
        if result is False:
            break
    if result is True:
        win()

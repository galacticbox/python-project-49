from random import randint
from brain_games.common_logic import solve, win, convert_bool
from brain_games.constants import RANGE_START, RANGE_STOP_MAX


def is_prime(x):
    lis = [i for i in range(1, x + 1) if x % i == 0]
    return len(lis) == 2


def game_prime():
    for _ in range(3):
        given_number = randint(RANGE_START, RANGE_STOP_MAX)
        print(f'Question: {given_number}')
        answer = input('Your answer: ')
        result = solve(convert_bool(is_prime(given_number)), answer)
        if result is False:
            break
    if result is True:
        win()

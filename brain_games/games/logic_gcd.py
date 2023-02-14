from random import randint
from math import gcd
from brain_games.common_logic import solve, win
from brain_games.constants import RANGE_START, RANGE_STOP_MAX


def game_gcd():
    for _ in range(3):
        number_1 = randint(RANGE_START, RANGE_STOP_MAX)
        number_2 = randint(RANGE_START, RANGE_STOP_MAX)
        print(f'Question: {number_1} {number_2}')
        answer = int(input('Your answer: '))
        result = solve(gcd(number_1, number_2), answer)
        if result is False:
            break
    if result is True:
        win()

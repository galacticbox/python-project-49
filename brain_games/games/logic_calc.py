from random import randint, choice
from brain_games.common_logic import solve, win
from brain_games.constants import CALC_SIGN, RANGE_STOP, RANGE_START


def calculate(x, y, z):
    if z == '+':
        return x + y
    elif z == '-':
        return x - y
    elif z == '*':
        return x * y


def game_calc():
    for _ in range(3):
        number_1 = randint(RANGE_START, RANGE_STOP)
        number_2 = randint(RANGE_START, RANGE_STOP)
        calc = choice(CALC_SIGN)
        print(f'Question: {number_1} {calc} {number_2}')
        answer = int(input('Your answer: '))
        result = solve(calculate(number_1, number_2, calc), answer)
        if not result:
            break
    if result:
        win()

from random import randint, choice
from brain_games.constants import CALC_SIGN, RANGE_STOP, RANGE_START

GAME_RULES = 'What is the result of the expression?'


def calculate(x, y, z):
    if z == '+':
        return x + y
    elif z == '-':
        return x - y
    elif z == '*':
        return x * y


def game_calc():
    number_1 = randint(RANGE_START, RANGE_STOP)
    number_2 = randint(RANGE_START, RANGE_STOP)
    calc = choice(CALC_SIGN)
    question = f'{number_1} {calc} {number_2}'
    correct_answer = calculate(number_1, number_2, calc)
    return question, correct_answer

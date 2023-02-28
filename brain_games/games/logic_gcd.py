from random import randint
from math import gcd
from brain_games.constants import RANGE_START, RANGE_STOP_MAX

GAME_RULES = 'Find the greatest common divisor of given numbers.'


def game_gcd():
    number_1 = randint(RANGE_START, RANGE_STOP_MAX)
    number_2 = randint(RANGE_START, RANGE_STOP_MAX)
    question = f'{number_1} {number_2}'
    correct_answer = gcd(number_1, number_2)
    return question, correct_answer

from random import randint
from brain_games.constants import RANGE_START, RANGE_STOP_MAX

GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def game_even():
    given_number = randint(RANGE_START, RANGE_STOP_MAX)
    return given_number, given_number % 2 == 0 and "yes" or 'no'

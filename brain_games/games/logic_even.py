from random import randint
from brain_games.common_logic import convert_bool
from brain_games.constants import RANGE_START, RANGE_STOP_MAX

game_rules = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(x):
    return x % 2 == 0


def game_even():
    given_number = randint(RANGE_START, RANGE_STOP_MAX)
    correct_answer = convert_bool(is_even(given_number))
    return given_number, correct_answer

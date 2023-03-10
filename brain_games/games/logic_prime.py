from random import randint
from brain_games.constants import RANGE_START, RANGE_STOP_MAX

GAME_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(x):
    lis = [i for i in range(1, x + 1) if x % i == 0]
    return len(lis) == 2


def game_prime():
    given_number = randint(RANGE_START, RANGE_STOP_MAX)
    correct_answer = is_prime(given_number)
    return given_number, correct_answer and 'yes' or 'no'

from random import randint
from math import gcd
from brain_games.common_logic import answering, winning


def is_gcd(x, y):
    return gcd(x, y)


def game_gcd():
    for _ in range(3):
        number_1 = randint(1, 100)
        number_2 = randint(1, 100)
        print(f'Question: {number_1} {number_2}')
        answer = int(input('Your answer: '))
        result = answering(is_gcd(number_1, number_2), answer)
        if result is False:
            break
    if result is True:
        winning()

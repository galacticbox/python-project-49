from random import randint, choice
from brain_games.common_logic import answering, winning

calc_sign = ['+', '-', '*']


def is_calc(x, y, z):
    if z == '+':
        return x + y
    elif z == '-':
        return x - y
    elif z == '*':
        return x * y


def game_calc():
    for _ in range(3):
        number_1 = randint(1, 20)
        number_2 = randint(1, 20)
        calc = choice(calc_sign)
        print(f'Question: {number_1} {calc} {number_2}')
        answer = int(input('Your answer: '))
        result = answering(is_calc(number_1, number_2, calc), answer)
        if result is False:
            break
    if result is True:
        winning()

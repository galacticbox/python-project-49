from random import randint
from brain_games.common_logic import answering, winning

yes = 'yes'
no = 'no'


def is_even(x):
    if x % 2 == 0:
        return yes
    else:
        return no


def game_even():
    for _ in range(3):
        given_number = randint(1, 100)
        print(f'Question: {given_number}')
        answer = input('Your answer: ')
        result = answering(is_even(given_number), answer)
        if result is False:
            break
    if result is True:
        winning()

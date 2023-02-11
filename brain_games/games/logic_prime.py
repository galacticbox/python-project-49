from random import randint
from brain_games.common_logic import answering, winning

yes = 'yes'
no = 'no'


def is_prime(x):
    count = 0
    for i in range(1, x + 1):
        if x % i == 0:
            count += 1
    if count == 2:
        return yes
    else:
        return no


def game_prime():
    for _ in range(3):
        given_number = randint(2, 100)
        print(f'Question: {given_number}')
        answer = input('Your answer: ')
        result = answering(is_prime(given_number), answer)
        if result is False:
            break
    if result is True:
        winning()

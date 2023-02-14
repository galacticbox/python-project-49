from random import randint
from brain_games.common_logic import solve, win


def make_progression():
    step = randint(2, 5)
    start = randint(1, 10)
    stop = randint(40, 70)
    lis = [i for i in range(start, stop, step)]
    return lis


def make_missing_number(lis):
    missing_num_index = randint(1, len(lis) - 1)
    answer_num = lis.pop(missing_num_index)
    lis.insert(missing_num_index, '..')
    return answer_num, lis


def game_prog():
    for _ in range(3):
        answer_num, lis = make_missing_number(make_progression())
        print('Question:', *lis, sep=' ')
        answer = int(input('Your answer: '))
        result = solve(answer_num, answer)
        if result is False:
            break
    if result is True:
        win()

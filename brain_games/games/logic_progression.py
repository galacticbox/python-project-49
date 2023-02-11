from random import randint
from brain_games.common_logic import answering, winning


def game_prog():
    for _ in range(3):
        step = randint(2, 5)
        start = randint(1, 10)
        stop = randint(40, 70)
        lis = [i for i in range(start, stop, step)]
        missing_num_index = randint(1, len(lis) - 1)
        answer_num = lis.pop(missing_num_index)
        lis.insert(missing_num_index, '..')
        print('Question:', *lis, sep=' ')
        answer = int(input('Your answer: '))
        result = answering(answer_num, answer)
        if result is False:
            break
    if result is True:
        winning()

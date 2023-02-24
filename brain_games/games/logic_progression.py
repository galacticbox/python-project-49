from random import randint


game_rules = 'What number is missing in the progression?'


def game_prog():
    step = randint(2, 5)
    start = randint(1, 10)
    stop = randint(40, 70)
    question = [i for i in range(start, stop, step)]
    missing_num_index = randint(1, len(question) - 1)
    correct_answer = question.pop(missing_num_index)
    question.insert(missing_num_index, '..')
    return question, str(correct_answer)

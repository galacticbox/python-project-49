import prompt
from brain_games.constants import YES, NO, TRIES


def convert_bool(x):
    if x is True:
        return YES
    elif x is False:
        return NO


def solve(real_ans, user_ans, name):
    if real_ans == user_ans:
        print('Correct!')
        return True
    print(f'"{user_ans}" is wrong answer ;(. Correct answer was "{real_ans}"')
    print(f"Let's try again, {name}!")
    return False


def game(game_rules, game_question):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game_rules)
    for _ in range(TRIES):
        x, y = game_question()
        print('Question:', x)
        answer = input('Your answer: ')
        result = solve(y, answer, name)
        if result is False:
            break
    if result is True:
        print(f'Congratulations, {name}!')

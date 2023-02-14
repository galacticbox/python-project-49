import prompt
from brain_games.constants import YES, NO


def welcome_user():
    global name
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def convert_bool(x):
    if x is True:
        return YES
    elif x is False:
        return NO


def win():
    print(f'Congratulations, {name}!')


def solve(real_ans, user_ans):
    if real_ans == user_ans:
        print('Correct!')
        return True
    print(f'"{user_ans}" is wrong answer ;(. Correct answer was "{real_ans}"')
    print(f"Let's try again, {name}!")
    return False

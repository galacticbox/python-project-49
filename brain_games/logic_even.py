import prompt
from random import randint

yes = 'yes'
no = 'no'
name = ''

def welcome_user():
    global name
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def is_even(x):
    if x % 2 == 0:
        return yes
    else:
        return no


def game_even():
    global name
    print('Answer "yes" if the number is even, otherwise answer "no".')
    result = True
    for _ in range(3):
        given_number = randint(1, 100)
        print(f'Question: {given_number}')
        answer = input('Your answer: ')
        if is_even(given_number) == answer:
            print('Correct!')
        else:
            print(f'"{answer}" is wrong answer ;(. Correct answer was "{is_even(given_number)}"')
            print(f"Let's try again, {name}")
            result = False
            break
        
    if result == True:
        print(f'Congratulations, {name}!')
    pass


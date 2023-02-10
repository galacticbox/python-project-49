import prompt


def welcome_user():
    global name
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def winning():
    print(f'Congratulations, {name}!')


def answering(computer, user):
    if computer == user:
        print('Correct!')
        return True
    else:
        print(f'"{user}" is wrong answer ;(. Correct answer was "{computer}"')
        print(f"Let's try again, {name}")
        return False

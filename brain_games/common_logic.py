import prompt
from brain_games.constants import TRIES


def solve(real_ans, user_ans, name):
    if real_ans.lower() == user_ans.lower():
        print('Correct!')
        return True
    print(f'"{user_ans}" is wrong answer ;(. Correct answer was "{real_ans}"')
    print(f"Let's try again, {name}!")
    return False


def game(GAME_RULES, game_logic):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(GAME_RULES)
    for _ in range(TRIES):
        game_question, game_answer = game_logic()
        print('Question:', game_question)
        answer = prompt.string('Your answer: ')
        result = solve(str(game_answer), answer, name)
        if not result:
            return
    print(f'Congratulations, {name}!')

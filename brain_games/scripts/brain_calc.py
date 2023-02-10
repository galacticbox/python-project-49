#!/usr/bin/env python3
from brain_games.games.logic_calc import game_calc
from brain_games.common_logic import welcome_user


def main():
    welcome_user()
    print('What is the result of the expression?')
    game_calc()
    pass


if __name__ == '__main__':
    main()

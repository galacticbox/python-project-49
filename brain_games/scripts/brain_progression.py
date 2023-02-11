#!/usr/bin/env python3
from brain_games.games.logic_progression import game_prog
from brain_games.common_logic import welcome_user


def main():
    welcome_user()
    print('What number is missing in the progression?')
    game_prog()
    pass


if __name__ == '__main__':
    main()

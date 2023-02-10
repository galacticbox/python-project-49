#!/usr/bin/env python3
from brain_games.games.logic_even import game_even
from brain_games.common_logic import welcome_user


def main():
    welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    game_even()
    pass


if __name__ == '__main__':
    main()

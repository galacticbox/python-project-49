#!/usr/bin/env python3
from brain_games.games.logic_gcd import game_gcd
from brain_games.common_logic import welcome_user


def main():
    welcome_user()
    print('Find the greatest common divisor of given numbers.')
    game_gcd()
    pass


if __name__ == '__main__':
    main()

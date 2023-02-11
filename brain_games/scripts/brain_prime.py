#!/usr/bin/env python3
from brain_games.games.logic_prime import game_prime
from brain_games.common_logic import welcome_user


def main():
    welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    game_prime()
    pass


if __name__ == '__main__':
    main()

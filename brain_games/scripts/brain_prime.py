#!/usr/bin/env python3
from brain_games.games.logic_prime import GAME_RULES, game_prime
from brain_games.common_logic import game


def main():
    game(GAME_RULES, game_prime)
    pass


if __name__ == '__main__':
    main()

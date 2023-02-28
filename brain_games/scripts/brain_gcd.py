#!/usr/bin/env python3
from brain_games.games.logic_gcd import GAME_RULES, game_gcd
from brain_games.common_logic import game


def main():
    game(GAME_RULES, game_gcd)
    pass


if __name__ == '__main__':
    main()

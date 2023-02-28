#!/usr/bin/env python3
from brain_games.games.logic_even import GAME_RULES, game_even
from brain_games.common_logic import game


def main():
    game(GAME_RULES, game_even)
    pass


if __name__ == '__main__':
    main()

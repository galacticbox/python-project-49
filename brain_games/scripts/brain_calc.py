#!/usr/bin/env python3
from brain_games.games.logic_calc import game_calc, GAME_RULES
from brain_games.common_logic import game


def main():
    game(GAME_RULES, game_calc)
    pass


if __name__ == '__main__':
    main()

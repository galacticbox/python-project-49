#!/usr/bin/env python3
from brain_games.games.logic_progression import GAME_RULES, game_prog
from brain_games.common_logic import game


def main():
    game(GAME_RULES, game_prog)
    pass


if __name__ == '__main__':
    main()

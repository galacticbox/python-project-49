#!/usr/bin/env python3
from brain_games.games.logic_progression import game_rules, game_prog
from brain_games.common_logic import game


def main():
    game(game_rules, game_prog)
    pass


if __name__ == '__main__':
    main()

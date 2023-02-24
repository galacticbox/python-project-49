#!/usr/bin/env python3
from brain_games.games.logic_even import game_rules, game_even
from brain_games.common_logic import game


def main():
    game(game_rules, game_even)
    pass


if __name__ == '__main__':
    main()

from src.dataclasses import GameMap


class UI(object):
    def __init__(self):
        raise NotImplementedError

    def print_map(self, game_map: GameMap) -> None:
        raise NotImplementedError

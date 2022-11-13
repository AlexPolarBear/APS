from src.dataclasses import GameMap


class UI(object):
    def __init__(self):
        pass

    def print_map(self, game_map: GameMap) -> None:
        print('This is a map ;)', game_map)

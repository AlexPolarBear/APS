from src.dataclasses import Command, GameMap


class Model(object):
    def process_command(self, command: Command) -> GameMap:
        raise NotImplementedError

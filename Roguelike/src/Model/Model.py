from src.dataclasses import Command, GameMap


class Model(object):
    def process_command(self, command: Command) -> GameMap:
        return GameMap(command.button.key)

    @classmethod
    def from_save(cls, save_path: str) -> 'Model':
        model = cls()
        # TODO: Load the save file
        return model

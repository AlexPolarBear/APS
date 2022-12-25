from src.GameClient.Command import Command
from src.Model.Map.Map import Direction


class MoveRightCommand(Command):
    """Command for moving player to the right."""
    def execute(self):
        self._model.move(Direction.RIGHT)

from src.GameClient.Command import Command
from src.Model.Map.MapController import Direction


class MoveLeftCommand(Command):
    """Command for moving player to the left."""
    def execute(self):
        self._model.move(Direction.LEFT)

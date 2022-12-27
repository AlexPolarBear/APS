from src.GameClient.Command import Command
from src.Model.Map.MapController import Direction


class MoveRightCommand(Command):
    """Command for moving player to the right."""
    def execute(self):
        self._model.move(Direction.RIGHT)

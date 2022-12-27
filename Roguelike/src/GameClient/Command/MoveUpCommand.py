from src.GameClient.Command import Command
from src.Model.Map.MapController import Direction


class MoveUpCommand(Command):
    """Command for moving player up."""
    def execute(self):
        self._model.move(Direction.UP)

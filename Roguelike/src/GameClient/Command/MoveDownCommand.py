from src.GameClient.Command import Command
from src.Model.Map.Map import Direction


class MoveDownCommand(Command):
    """Command for moving player down."""
    def execute(self):
        self._model.move(Direction.DOWN)

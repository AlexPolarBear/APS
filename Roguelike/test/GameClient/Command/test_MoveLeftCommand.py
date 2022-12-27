from src import Model
from src.GameClient.Command import MoveLeftCommand
from src.Model.Map.MapController import Direction


class ModelMoveLeftMock(Model):
    def __init__(self):
        pass

    def move(self, direction: Direction):
        assert direction == Direction.LEFT


def test_move_down_command():
    command = MoveLeftCommand(ModelMoveLeftMock())
    command.execute()

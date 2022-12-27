from src import Model
from src.GameClient.Command import MoveRightCommand
from src.Model.Map.MapController import Direction


class ModelMoveRightMock(Model):
    def __init__(self):
        pass

    def move(self, direction: Direction):
        assert direction == Direction.RIGHT


def test_move_down_command():
    command = MoveRightCommand(ModelMoveRightMock())
    command.execute()

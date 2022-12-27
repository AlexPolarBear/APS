from src import Model
from src.GameClient.Command import MoveUpCommand
from src.Model.Map.Map import Direction


class ModelMoveUpMock(Model):
    def __init__(self):
        pass

    def move(self, direction: Direction):
        assert direction == Direction.UP


def test_move_down_command():
    command = MoveUpCommand(ModelMoveUpMock())
    command.execute()

from src import Model
from src.GameClient.Command import MoveDownCommand
from src.Model.Map.Map import Direction


class ModelMoveDownMock(Model):
    def __init__(self):
        pass

    def move(self, direction: Direction):
        assert direction == Direction.DOWN


def test_move_down_command():
    command = MoveDownCommand(ModelMoveDownMock())
    command.execute()

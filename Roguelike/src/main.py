from src import Model, GameClient
from src.Model.Map import Direction
import argparse


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--save', default=None, type=str, help='The save file to load.')
    args = parser.parse_args()

    if args.save is None:
        model = Model()
    else:
        model = Model.from_save(args.save)
    model.world_map._print_map()
    model.move(Direction.RIGHT)
    print('---------')
    model.world_map._print_map()
    #game_client = GameClient(model)
    #game_client.play()
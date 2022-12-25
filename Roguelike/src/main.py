from src import Model, GameClient
from src.Model.Map.Map import Direction
import argparse


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--save', default=None, type=str, help='The save file to load.')
    args = parser.parse_args()

    if args.save is None:
        model = Model()
    else:
        model = Model.from_save(args.save)
    game_client = GameClient(model)
    game_client.play()

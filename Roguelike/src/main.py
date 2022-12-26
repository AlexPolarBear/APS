import argparse

from src import Model, GameClient
from src.GameClient.InputProvider import KeyboardInputProvider


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--save', default=None, type=str, help='The save file to load.')
    args = parser.parse_args()

    if args.save is None:
        model = Model()
    else:
        model = Model.from_save(args.save)

    keyboard_input_provider = KeyboardInputProvider(
        keys_to_track={'w', 'a', 's', 'd', 'up', 'left', 'down', 'right', 'tab', 'space', 'shift', 'esc'},
        key_mapping={'w': 'up', 'a': 'left', 's': 'down', 'd': 'right'},
    )
    game_client = GameClient(model, keyboard_input_provider)
    game_client.play()

from src import Model, Controller
import argparse
from src.Model.Map import Direction


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--save', default=None, type=str, help='The save file to load.')
    args = parser.parse_args()

    if args.save is None:
       model = Model()
      #  model.get_map().print_map()
      #  model.get_map().move(Direction.RIGHT, model._user_hero)
      #  model.get_map().print_map()
    else:
       model = Model.from_save(args.save)
    return # TODO
    controller = Controller(model)
    controller.run()

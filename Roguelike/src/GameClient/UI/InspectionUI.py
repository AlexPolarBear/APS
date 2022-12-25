from typing import Optional

from src import Model
from src.GameClient.UI import UI

from src.Model.Map.Map import GridCell


class InspectionUI(UI):
    """
    UI specialization for the enemy inspection view.
    Renders game state for user in the enemy inspection view.

    Parameters
    ----------
    width : int
        Width of the UI.
    height : int
        Height of the UI.

    Attributes
    ----------
    width : int
        Width of the UI.
    height : int
        Height of the UI.
    """
    def __init__(self, width: int, height: int):
        super(InspectionUI, self).__init__(width, height)

    def print(
            self, model: Model, erase_before: bool = True, selected_enemy_index: Optional[int] = None, **kwargs,
    ) -> None:
        """
        Render the world map to user, highlight currently selected enemy and print enemy's details.

        Parameters
        ----------
        model : Model
            Model instance which contains the world map.
        erase_before : bool
            If True, erase previous UI frame before rendering new one.
        selected_enemy_index : Optional[int]
            Index of currently selected enemy for the inspection.
        kwargs : dict
            Additional keyword arguments for rendering customization.
        """
        if erase_before:
            self.erase()

        print('#' * self.width * 2)

        enemy_coordinates_list = []
        world_map = model.world_map.get_map()
        for i, row in enumerate(world_map):
            for j, cell in enumerate(row):
                if cell == GridCell.EMPTY:
                    print('.', end=' ')
                elif cell == GridCell.WALL:
                    print('█', end=' ')
                elif cell == GridCell.USER_POSITION:
                    print('@', end=' ')
                elif cell == GridCell.ITEM:
                    print('0', end=' ')
                elif cell == GridCell.AGGRESSIVE_ENEMY:
                    enemy_coordinates_list.append((i, j))
                    if selected_enemy_index == len(enemy_coordinates_list) - 1:
                        print('\033[31ma\033[0m', end=' ')
                    else:
                        print('a', end=' ')
                elif cell == GridCell.NEUTRAL_ENEMY:
                    enemy_coordinates_list.append((i, j))
                    if selected_enemy_index == len(enemy_coordinates_list) - 1:
                        print('\033[31mn\033[0m', end=' ')
                    else:
                        print('n', end=' ')
                elif cell == GridCell.COWARD_ENEMY:
                    enemy_coordinates_list.append((i, j))
                    if selected_enemy_index == len(enemy_coordinates_list) - 1:
                        print('\033[31mc\033[0m', end=' ')
                    else:
                        print('c', end=' ')
                elif cell == GridCell.CONFUSED_ENEMY:
                    enemy_coordinates_list.append((i, j))
                    if selected_enemy_index == len(enemy_coordinates_list) - 1:
                        print('\033[31m*\033[0m', end=' ')
                    else:
                        print('*', end=' ')
            print()

        print('=' * self.width * 2)

        enemy_info = model.world_map.get_enemy_info(enemy_coordinates_list[selected_enemy_index])
        name = enemy_info['name']
        name = name[0].upper() + name[1:]

        print(
            f'{name}:',
            'HP:', enemy_info['health'],
            'AP:', enemy_info['attack'],
        )
        print('#' * self.width * 2)

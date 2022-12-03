from src import Model
from src.GameClient.UI import UI

from src.Model.Map import GridCell


class MapUI(UI):
    """
    UI specialization for the map view.
    Renders game state for user in the map view.

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
        super(MapUI, self).__init__(width, height)

    def print(self, model: Model, erase_before: bool = True, **kwargs) -> None:
        """
        Render the world map to user.

        Parameters
        ----------
        model : Model
            Model instance which contains the world map.
        erase_before : bool
            If True, erase previous UI frame before rendering new one.
        kwargs : dict
            Additional keyword arguments for rendering customization.
        """
        if erase_before:
            self.erase()

        print('#' * self.width * 2)

        world_map = model.world_map.get_map()
        for row in world_map:
            for cell in row:
                if cell == GridCell.EMPTY:
                    print('.', end=' ')
                elif cell == GridCell.WALL:
                    print('█', end=' ')
                elif cell == GridCell.USER_POSITION:
                    print('@', end=' ')
                elif cell == GridCell.ITEM:
                    print('0', end=' ')
                elif cell == GridCell.AGGRESSIVE_ENEMY:
                    print('a', end=' ')
                elif cell == GridCell.NEUTRAL_ENEMY:
                    print('n', end=' ')
                elif cell == GridCell.COWARD_ENEMY:
                    print('c', end=' ')
                elif cell == GridCell.CONFUSED_ENEMY:
                    print('*', end=' ')
            print()

        print('HP: ', model.user_hero.health_point, 'AP: ', model.user_hero.attack_point)
        print('#' * self.width * 2)

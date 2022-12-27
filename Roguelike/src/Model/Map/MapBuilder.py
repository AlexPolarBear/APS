from src.Model.Map.Map import MapData


class MapBuilder(object):
    """Class for building the world map."""

    def generate_map(self) -> MapData:
        """Generate the map data."""
        self._generate_walls()
        coordinates_to_items = self._generate_items()
        mold_prototype = self._generate_mold_prototype()
        coordinates_to_enemies = self._generate_enemies()
        self._map[self._start_position[0]][self._start_position[1]] = GridCell.USER_POSITION
        return MapData(coordinates_to_items, mold_prototype, coordinates_to_enemies)

    def _generate_walls(self):
        """Generate walls on the world map."""
        raise NotImplementedError

    def _generate_items(self):
        """Arrange items on the map."""
        raise NotImplementedError

    def _generate_enemies(self):
        """Arrange enemies on the map."""
        raise NotImplementedError

    def _generate_mold_prototype(self):
        """Create mold prototype"""
        raise NotImplementedError

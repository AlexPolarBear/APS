class MapBuilder(object):
    """Class for building the world map."""

    def generate_walls(self):
        """Generate walls on the world map."""
        raise NotImplementedError

    def generate_items(self):
        """Arrange items on the map."""
        raise NotImplementedError

    def generate_enemies(self):
        """Arrange enemies on the map."""
        raise NotImplementedError
from src.core.common import Size
from src.world.map import Map


class Home(Map):
    """
    Home background.
    """

    def __init__(self):
        super().__init__(Size(5, 5))

    def _init_wall(self):
        ground_layer = self.get_layer("ground")

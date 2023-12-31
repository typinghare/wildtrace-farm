"""
Farm map module.
"""

from typing import List, Dict, Tuple

from pygame import Surface, Rect

from src.core.common import Size, CoordinateSet, Grid
from src.core.context import Context
from src.core.display import GridLayer
from src.world.data.frames import Frames
from src.world.data.renderers import Renderers
from src.world.data.tiles import Tiles
from src.world.map import Map
from src.world.util import flip_coin, randomly_pick


class FarmMap(Map):
    """
    Farm map.
    """

    def __init__(self):
        super().__init__(Size(25, 15))

        # Layers
        self.water: GridLayer = self.get_layer("water")
        self.ground: GridLayer = self.get_layer("ground")
        self.floor: GridLayer = self.get_layer("floor")
        self.crop: GridLayer = self.get_layer("crop")
        self.furniture_bottom: GridLayer = self.get_layer("furniture_bottom")

        # Crop grid
        self.crop_grid: Grid = Grid(self.size)

        # Coordinate sets
        self.coordinate_set_map: Dict[str, CoordinateSet] = {}

        self.invisible_block_grid = Grid(self.size, False)

        # house rect
        self.house_rect: Rect = Rect(16, 2, 6, 4)

        self._init_water()
        self._init_grass()
        self._init_tilled_dirt()
        self._init_chest()
        self._init_house()
        self._init_trees()
        self._init_ground_decorations()

    def get_door_coordinate(self) -> Tuple[int, int]:
        """
        Returns the coordinate of the house door.
        """
        return self.house_rect.midbottom

    def _init_water(self) -> None:
        """
        Initializes water.
        """
        self.coordinate_set_map["water"] = water_set = CoordinateSet()

        for col in range(self.size.width):
            water_set.add((col, 0))
            water_set.add((col, 1))
            water_set.add((col, self.size.height - 1))
            water_set.add((col, self.size.height - 2))

            self.invisible_block_grid.set((col, 0), True)
            self.invisible_block_grid.set((col, self.size.height - 1), True)

        for row in range(self.size.height):
            water_set.add((0, row))
            water_set.add((1, row))
            water_set.add((self.size.width - 1, row))
            water_set.add((self.size.width - 2, row))

            self.invisible_block_grid.set((0, row), True)
            self.invisible_block_grid.set((self.size.width - 1, row), True)

        for row in range(2, 5):
            for col in range(2, 5):
                water_set.add((row, col))

        # Update cells
        for coordinate in water_set.all():
            self.water.update_cell(coordinate, Tiles.Water0)

    def _init_grass(self) -> None:
        """
        Initializes grass.
        """
        self.coordinate_set_map["grass"] = grass_set = CoordinateSet()

        for row in range(1, self.size.height - 1):
            for col in range(1, self.size.width - 1):
                grass_set.add((col, row))

        # Top-left corner
        for row in range(1, 4):
            for col in range(1, 3):
                grass_set.remove((col, row))

        Renderers.Grass.render(self.ground, grass_set)

        # Initialize decorative coordinate set
        decorative_set = self.coordinate_set_map["decorative"] = CoordinateSet()
        for coordinate in grass_set.all():
            decorative_set.add(coordinate)
        for row in range(1, self.size.height - 2):
            for col in range(10, self.size.width - 1):
                decorative_set.remove((col, row))
        for col in range(1, self.size.width):
            decorative_set.remove((col, self.size.height - 2))
            decorative_set.remove((col, self.size.height - 3))
        for row in range(1, self.size.height - 2):
            decorative_set.remove((1, row))
        for row in range(1, 3):
            decorative_set.remove((3, row))

    def _init_chest(self) -> None:
        """
        Initializes a chest.
        """
        self.furniture_bottom.update_cell((15, 6), Tiles.ChestFront0)

    def _init_tilled_dirt(self) -> None:
        """
        Initializes tilled dirt.
        """
        self.coordinate_set_map["tilled_dirt"] = tilled_dirt_set = CoordinateSet()

        rect = Rect(11, 8, 12, 5)

        for row in range(rect.top, rect.bottom):
            for col in range(rect.left, rect.right):
                tilled_dirt_set.add((col, row))

        Renderers.TilledDirt.render(self.floor, tilled_dirt_set)

    def _init_house(self) -> None:
        """
        Initializes house.
        """
        rect = self.house_rect
        mid_row = rect.midleft[1]

        def render_row(_row: int, tile_list: List[Surface]) -> None:
            self.furniture_bottom.update_cell((rect.left, _row), tile_list[0])
            self.furniture_bottom.update_cell((rect.right - 1, _row), tile_list[2])
            for _col in range(rect.left + 1, rect.right - 1):
                self.furniture_bottom.update_cell((_col, _row), tile_list[1])

        # Roof
        render_row(rect.top, [Tiles.Roof0, Tiles.Roof1, Tiles.Roof2])
        render_row(mid_row, [Tiles.Roof6, Tiles.Roof7, Tiles.Roof8])
        render_row(rect.bottom, [Tiles.Roof12, Tiles.Roof13, Tiles.Roof14])
        for row in range(rect.top + 1, mid_row):
            render_row(row, [Tiles.Roof3, Tiles.Roof4, Tiles.Roof5])
        for row in range(mid_row + 1, rect.bottom):
            render_row(row, [Tiles.Roof9, Tiles.Roof10, Tiles.Roof11])

        # Last row
        for col in range(rect.left + 1, rect.right - 1):
            self.floor.update_cell((col, rect.bottom), Tiles.WoodenHouse11)
        self.floor.update_cell((rect.left, rect.bottom), Tiles.WoodenHouse3)
        self.floor.update_cell((rect.right - 1, rect.bottom), Tiles.WoodenHouse9)

        # Door
        door_coordinate = self.get_door_coordinate()
        self.floor.update_cell(door_coordinate, None)
        self.ground.update_cell(door_coordinate, Tiles.Door5)

    def _init_trees(self) -> None:
        """
        Initializes trees.
        """
        tree_tiles: List[Surface] = [Tiles.Tree0, Tiles.Tree1, Tiles.Stump0, Tiles.Stump1]
        decoration_set = self.coordinate_set_map["decorative"]
        for coordinate in decoration_set.all():
            if flip_coin(0.90):
                continue

            self.floor.update_cell(coordinate, randomly_pick(tree_tiles))

    def _init_ground_decorations(self) -> None:
        """
        Initializes ground decorations.
        """
        ground_decoration_tiles: List[Surface] = [
            Tiles.Stone0,
            Tiles.Stone1,
            Tiles.Stone2,
            Tiles.Stone3,
            Tiles.Bush0,
            Tiles.Bush1,
            Tiles.Bush2,
            Tiles.Bush3,
        ]
        decoration_set = self.coordinate_set_map["decorative"]
        for coordinate in decoration_set.all():
            if flip_coin(0.80):
                continue

            self.floor.update_cell(coordinate, randomly_pick(ground_decoration_tiles))

    def load(self, context: Context) -> None:
        # Water animation
        frames: List[Surface] = Frames.Water.list

        def update_water(index: int):
            for coordinate in self.coordinate_set_map["water"].all():
                self.water.update_cell(coordinate, frames[index])

        update_water(0)
        context.game.loop_manager.loop(2, len(frames), update_water)

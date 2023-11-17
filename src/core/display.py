"""
Display module.
"""
from typing import List, Dict, Tuple

import pygame
from pygame import Surface, Vector2

from src.core import Size


class Layer:
    """
    An abstract layer.
    """

    def __init__(self, name: str, size: Size):
        # The name of this layer
        self.name = name

        # The size of this layer
        self.size: Size = size

        # The surface of this layer; by default, the surface is transparent
        self.surface: Surface = Surface(size.toTuple(), pygame.SRCALPHA)

        # The offset of the surface
        self.offset: Vector2 = Vector2(0, 0)

    def render(self) -> None:
        """
        Renders this layer.
        """

    def blit(self, surface: Surface, offset: Tuple[float, float]) -> None:
        """
        Blits a surface on this layer.
        """
        self.surface.blit(surface, offset)

    def clear(self) -> None:
        """
        Clears the surface.
        """
        self.surface = Surface(self.size.toTuple(), pygame.SRCALPHA)

    def display(self, screen: Surface) -> None:
        """
        Draws the surface on the screen.
        :param screen: The screen to draw.
        """
        screen.blit(self.surface, (self.offset.x, self.offset.y))


class GridLayer(Layer):
    """
    Grid layer.
    """

    class Cell:
        """
        Grid cell.
        """

        def __init__(self):
            # The surface of this cell
            self._surface: Surface | None = None

            # Whether the surface of this cell is updated
            self.updated = False

        def set_surface(self, surface: Surface):
            """
            Sets a surface for this cell.
            :param surface: The surface of this cell.
            """
            self._surface = surface
            self.updated = True

        def clear_surface(self):
            """
            Clears the surface.
            """
            self._surface = None
            self.updated = True

        def get_surface(self) -> Surface:
            """
            Returns the surface.
            """
            return self._surface

    def __init__(self, name: str, grid_size: Size, cell_size: Size):
        super().__init__(
            name, Size(grid_size.width * cell_size.width, grid_size.height * cell_size.height)
        )

        # Grid size
        self.grid_size: Size = grid_size

        # The size of each cell
        self.cell_size: Size = cell_size

        # Grid; it is a list of cells
        self.grid: List[GridLayer.Cell] = []
        for i in range(grid_size.width * grid_size.height):
            self.grid.append(GridLayer.Cell())

    def get_cell(self, pos: Tuple[int, int]) -> "GridLayer.Cell":
        """
        Retrieves a cell at the specified position.
        :return: The cell located at the specified position in the grid.
        """
        index = pos[0] * int(self.grid_size.width) + pos[1]
        return self.grid[index]

    def render(self):
        """
        Renders this grid layer.
        """
        # self.surface.fill("green")
        for row in range(self.grid_size.height):
            for col in range(self.grid_size.width):
                cell = self.get_cell((row, col))
                if not cell.updated:
                    continue

                # Redraw the cell on the layer surface
                pos = (
                    col * self.cell_size.width,
                    row * self.cell_size.height,
                )
                surface = cell.get_surface()
                self.surface.blit(surface, pos)


class Display:
    """
    Game display.
    """

    def __init__(self):
        # Screen
        self.screen: Surface = pygame.display.set_mode((800, 600))

        # Layer stack
        self.layer_stack: List[Layer.__subclasses__] = []

        # A map from layer names to layers
        self._by_name: Dict[str, Layer.__subclasses__] = {}

    def _init(self):
        """
        Initializes the builtin layers.
        """
        self.add_layer(GridLayer("ground", Size(40, 30), Size(32, 32)))
        self.add_layer(Layer("character", Size(self.screen.get_width(), self.screen.get_height())))

    def add_layer(self, layer: Layer.__subclasses__):
        """
        Adds a layer to the layer stack.
        :param layer: The layer to add.
        """
        self.layer_stack.append(layer)
        self._by_name[layer.name] = layer

    def get_layer(self, name: str) -> Layer.__subclasses__:
        """
        Retrieves a layer by its name.
        :param name: The name of the layer to retrieve.
        :return: The layer.
        """
        return self._by_name[name]

    @property
    def center(self) -> Tuple[int, int]:
        """
        Returns the center
        """
        return self.screen.get_width() // 2, self.screen.get_height() // 2

    def render(self):
        """
        Renders the screen by drawing layers from bottom to top, ensuring that each subsequent
        layer covers the previous ones.
        """
        for layer in self.layer_stack:
            layer.render()
            layer.display(self.screen)

        pygame.display.flip()

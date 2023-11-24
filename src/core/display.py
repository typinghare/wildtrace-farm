"""
Display module.
"""
from typing import List, Dict, Tuple, Optional

import pygame
from pygame import Surface, Vector2, Rect

from src.core.common import Size, Grid


class Layer:
    """
    A layer.
    """

    def __init__(self, size: Size):
        # The size of this layer
        self.size: Size = size

        # The surface of this layer; by default, the surface is transparent
        self.surface: Surface = Surface(size.toTuple(), pygame.SRCALPHA)

        # The offset when this layer is displayed on the screen
        self.offset: Vector2 = Vector2(0, 0)

        # Rectangle to crop
        self.rect: Optional[Rect] = None

    def render(self) -> None:
        """
        Renders this layer.
        """

    def blit(self, surface: Surface, offset: Vector2 = Vector2(0, 0)) -> None:
        """
        Blits a surface on this layer.
        :param: surface The surface to blit on this layer.
        :param: offset The offset of the surface.
        """
        self.surface.blit(surface, offset)

    def clear(self, flag: int = pygame.SRCALPHA) -> None:
        """
        Clears the surface.
        :param flag An extra parameter for initializing the surface.
        """
        self.surface = Surface(self.size.toTuple(), flag)

    def display(self, screen: Surface) -> None:
        """
        Blits the surface on the screen.
        :param screen: The screen to blit.
        """
        self.render()
        screen.blit(self.surface, self.offset)


class GridLayer(Layer):
    """
    Grid layer.
    """

    class Cell:
        """
        Grid cell.
        """

        def __init__(self, coordinate: Tuple[int, int]):
            # The coordinate of this cell
            self.coordinate = coordinate

            # The surface of this cell
            self.surface: Surface | None = None

    def __init__(self, grid_size: Size, cell_size: Size):
        super().__init__(grid_size * cell_size)

        # Grid size
        self.grid_size: Size = grid_size

        # The size of each cell
        self.cell_size: Size = cell_size

        # Grid
        self.grid: Grid = Grid(grid_size)
        for row in range(grid_size.height):
            for col in range(grid_size.width):
                coordinate = (col, row)
                index = self.grid.get_index(coordinate)
                self.grid[index] = GridLayer.Cell(coordinate)

        # Updated cells' indices
        self.updated_indices: List[int] = []

    def get_cell(self, coordinate: Tuple[int, int]) -> "GridLayer.Cell":
        """
        Retrieves a cell at a specified position.
        :param coordinate The coordinate of the cell.
        :return: The cell located at the specified position in the grid.
        """
        return self.grid.get(coordinate)

    def update_cell(self, coordinate: Tuple[int, int], surface: Surface | None) -> None:
        """
        Updates a cell at a specified position.
        :return: The cell located at the specified position in the grid.
        """
        index: int = self.grid.get_index(coordinate)
        cell: GridLayer.Cell = self.grid[index]
        cell.surface = surface

        self.updated_indices.append(index)

    def render_all(self):
        """
        Renders all cells in this layer; clears the updated indices.
        :return:
        """
        self._render_indices(list(range(len(self.grid))))
        self.updated_indices = []

    def render(self):
        """
        Renders this layer; blit the updated cells on the surface.
        """
        self._render_indices(self.updated_indices)
        self.updated_indices = []

    def _render_indices(self, indices: List[int]):
        """
        Renders cells of given indices.
        """
        for index in indices:
            cell: GridLayer.Cell = self.grid[index]
            dest = (
                cell.coordinate[0] * self.cell_size.width,
                cell.coordinate[1] * self.cell_size.height,
            )
            surface = cell.surface
            if surface is not None:
                self.surface.blit(surface, dest)

    def clone(self) -> "GridLayer":
        """
        Returns a deep copy of this grid layer.
        """
        grid_layer = GridLayer(self.grid_size, self.cell_size)
        for index in range(len(self.grid)):
            grid_layer.grid[index].surface = self.grid[index].surface

        return grid_layer


class Display:
    """
    Game display.
    """

    def __init__(self, window_size: Size, background: str):
        # Size
        self.size = window_size

        # Screen
        self.screen: Surface = pygame.display.set_mode(window_size.toTuple())

        # default background
        self.background = background

        # Static layer
        self.static_layer: Layer = Layer(window_size)

        # Layer stack
        self.layer_stack: List[Layer] = []

        # A map from layer names to layers
        self._by_name: Dict[str, Layer] = {}

    def unshift_layer(self, name: str, layer: Layer):
        """
        Unshifts a layer to the layer stack.
        :param name: The name of the layer to add.
        :param layer: The layer to unshift.
        """
        self.layer_stack.insert(0, layer)
        self._by_name[name] = layer

    def append_layer(self, name: str, layer: Layer) -> None:
        """
        Adds a layer to the layer stack.
        :param name: The name of the layer to add.
        :param layer: The layer to add.
        """
        self.layer_stack.append(layer)
        self._by_name[name] = layer

    def set_layer(self, name: str, layer: Layer) -> None:
        """
        Sets a layer.
        :param name: The name of the layer.
        :param layer: The layer to set.
        """
        original_layer = self._by_name[name]
        self._by_name[name] = layer

        for i in range(len(self.layer_stack)):
            if original_layer == self.layer_stack[i]:
                self.layer_stack[i] = layer
                break

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
        Returns the center fo the screen.
        """
        return self.screen.get_width() // 2, self.screen.get_height() // 2

    def render(self):
        """
        Renders the screen by drawing layers from bottom to top, ensuring that each subsequent
        layer covers the previous ones.
        """
        self.screen.fill(self.background)

        for layer in self.layer_stack:
            layer.display(self.screen)

    @staticmethod
    def flip() -> None:
        """
        Flips the display.
        """
        pygame.display.flip()

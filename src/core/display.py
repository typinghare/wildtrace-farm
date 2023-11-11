"""Display module"""
from typing import Tuple, List

import pygame
from pygame import Surface


class Display:
    """Display."""

    def __init__(self, cell_size: Tuple[int, int], grid_size: Tuple[int, int], scale_factor: int):
        # The size of each cell
        self.cell_size = cell_size

        # The size of the grid
        self.grid_size = grid_size

        # The scale factor
        self.scale_factor = scale_factor

        # The pygame screen object
        width = cell_size[0] * grid_size[0] * scale_factor
        height = cell_size[1] * grid_size[1] * scale_factor
        self.screen = self.screen = pygame.display.set_mode((width, height))

        # The grid of cells
        self.grid = []
        for row in range(grid_size[1]):
            cell_row = []
            self.grid.append(cell_row)
            for col in range(grid_size[0]):
                cell_row.append(Cell((row, col), self))

    def render(self):
        """
        Renders this display.
        """
        pygame.display.flip()

        for row in self.grid:
            for cell in row:
                cell.draw(self)


class Cell:
    """Grid cell."""

    def __init__(self, pos: Tuple[int, int], display: Display):
        # The position (row, col) of this cell
        self.pos = pos

        # The coordinate of this cell
        self.pos: Tuple[int, int] = (
            display.cell_size[0] * pos[1] * display.scale_factor,
            display.cell_size[1] * pos[0] * display.scale_factor,
        )

        # Surface stack
        self.surface_stack: List[Surface] = []

        # Whether this cell is updated
        self.updated = False

    def cover(self, surface: Surface):
        """
        Clears surface stack, and adds the given surface on the surface stack.
        :param surface: The surface to add.
        """
        self.surface_stack = [surface]
        self.updated = True

    def add(self, surface: Surface):
        """
        Adds a surface; appends the given surface to the surface stack.
        :param surface: The surface to add.
        """
        self.surface_stack.append(surface)
        self.updated = True

    def draw(self, display: Display):
        """
        Draws the cell on the display.
        :param display: The display where the image to draw on.
        """
        if not self.updated:
            return

        for surface in self.surface_stack:
            display.screen.blit(surface, self.pos)

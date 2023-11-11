"""Display module"""
from typing import Tuple

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
        self.screen = self.screen = pygame.display.set_mode(
            (cell_size[0] * grid_size[0] * scale_factor, cell_size[1] * grid_size[1] * scale_factor)
        )

        # The grid of cells
        self.grid = []
        for row in range(grid_size[1]):
            cell_row = []
            self.grid.append(cell_row)
            for col in range(grid_size[0]):
                cell_row.append(Cell(row, col, self))

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

    def __init__(self, row: int, col: int, display: Display):
        # The row of this cell
        self.row: int = row

        # The column of this cell
        self.col: int = col

        # The coordinate of this cell
        self.pos: Tuple[int, int] = (
            display.cell_size[0] * col * display.scale_factor,
            display.cell_size[1] * row * display.scale_factor,
        )

        # The image this cell displays
        self.image: Surface | None = None

    def set_image(self, image: Surface | None):
        """
        Sets the image.
        :param image: The image to set.
        """
        self.image = image

    def draw(self, display: Display):
        """
        Draws the image on the display.
        :param display: The display where the image to draw on.
        """
        if self.image is not None:
            display.screen.blit(self.image, self.pos)

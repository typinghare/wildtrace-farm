"""Display module"""
from typing import Tuple, List

import pygame
from pygame import Surface

from src.core.animation import Animation


class Display:
    """
    Game display. The whole screen is evenly divided into a two-dimensional grid of cells.
    """

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
        for row in self.grid:
            for cell in row:
                cell.draw(self)

        pygame.display.flip()

    def get_grid(self, row: int, col: int):
        """
        Returns a grid at a given position (row, col).
        """
        return self.grid[row][col]

    class Iterator:
        """
        Square iterator.
        """

        def __init__(
            self, display: "Display", row_range: Tuple[int, int], col_range: Tuple[int, int]
        ):
            self.display = display
            self.row_range = row_range
            self.col_range = col_range
            self.current: List[int, int] = [row_range[0], col_range[0]]

        def __iter__(self):
            return self

        def __next__(self) -> "Cell":
            (row, col) = self.current

            if self.current[0] == self.row_range[1]:
                # signals the end of iteration
                raise StopIteration

            self.current[1] += 1
            if self.current[1] == self.col_range[1]:
                # Go to the next row
                self.current[0] += 1
                self.current[1] = self.col_range[0]

            return self.display.get_grid(row, col)

    def get_iterator(self, row: Tuple[int, int] | int, col: Tuple[int, int] | int) -> Iterator:
        """
        Returns an interator.
        :param row: A row or a range of rows.
        :param col: A column or a range of columns.
        """
        row_range = (row, row + 1) if isinstance(row, int) else row
        col_range = (col, col + 1) if isinstance(col, int) else col

        return Display.Iterator(self, row_range, col_range)


class Cell:
    """
    Grid cell.
    """

    def __init__(self, pos: Tuple[int, int], display: Display):
        # The position (row, col) of this cell
        self.pos = pos

        # The coordinate of this cell
        self.pos: Tuple[int, int] = (
            display.cell_size[0] * pos[1] * display.scale_factor,
            display.cell_size[1] * pos[0] * display.scale_factor,
        )

        # displayable stack
        self.displayable_stack: List[Surface | Animation] = []

        # Whether this cell is updated
        self.updated = False

    def clear(self):
        """
        Clears the displayable stack.
        """
        self.displayable_stack = []
        self.updated = True

    def add(self, displayable: Surface | Animation):
        """
        Adds a surface or animation; appends the given element to the stack.
        :param displayable: The surface to add.
        """
        self.displayable_stack.append(displayable)
        self.updated = True

    def draw(self, display: Display):
        """
        Draws the cell on the display.
        :param display: The display where the image to draw on.
        """
        if not self.updated:
            return

        has_animation = False
        for displayable in self.displayable_stack:
            if isinstance(displayable, Surface):
                display.screen.blit(displayable, self.pos)
            else:
                has_animation = True
                display.screen.blit(displayable.get_current_frame(), self.pos)

        if not has_animation:
            self.updated = False

"""
Grid module.
"""

from typing import Tuple, List, Any, TypeVar, Generic

from .size import Size

T = TypeVar("T")


class Grid(Generic[T]):
    """
    General grid.
    """

    def __init__(self, size: Size, default_cell: T | None = None):
        # The size of this grid
        self.size = size

        # Cells
        self._cells: List[T | None] = [None] * size.width * size.height

        # Fill
        if default_cell is not None:
            self.fill(default_cell)

    def get_index(self, coordinate: Tuple[int, int]) -> T | None:
        """
        Gets the index of a coordinate (x = col, y = row).
        :param coordinate: The coordinate to get the index of.
        """
        return coordinate[1] * self.size.width + coordinate[0]

    def get(self, coordinate: Tuple[int, int]) -> T | None:
        """
        Retrieves a cell.
        :param coordinate: The coordinate of the cell to retrieve.
        :return: The cell at the specified coordinate (or index).
        """
        return self._cells[self.get_index(coordinate)]

    def set(self, coordinate: Tuple[int, int], cell: T | None) -> None:
        """
        Sets a cell.
        :param coordinate: The coordinate of the cell to set.
        :param cell: The cell to set.
        """
        self._cells[self.get_index(coordinate)] = cell

    def fill(self, cell: Any) -> None:
        """
        Fills all cells with a given value.
        :param cell: The value of fill.
        """
        for i in range(0, len(self._cells)):
            self._cells[i] = cell

    def __getitem__(self, index: int) -> T | None:
        """
        Retrieves a cell of a specified index.
        :param index: The index of the cell to retrieve.
        """
        return self._cells[index]

    def __setitem__(self, index: int, cell: Any) -> None:
        """
        Sets the value of a cell.
        :param index: The index of the cell.
        :param cell: The cell to set.
        """
        self._cells[index] = cell

    def __len__(self) -> int:
        """
        Returns the size of cells.
        """
        return len(self._cells)

    def get_iterator(
        self, row_range: Tuple[int, int], col_range: Tuple[int, int]
    ) -> "Grid.Iterator":
        """
        Returns an iterator.
        :param row_range: The range of row.
        :param col_range: The range of column.
        """
        return self.Iterator(self, row_range, col_range)

    class Iterator:
        """
        Grid iterator.
        """

        def __init__(self, grid: "Grid[T]", row_range: Tuple[int, int], col_range: Tuple[int, int]):
            self.grid = grid
            self.row_start, self.row_end = row_range
            self.col_start, self.col_end = col_range
            self.current_row = self.row_start
            self.current_col = self.col_start

        def __iter__(self):
            return self

        def __next__(self) -> T | None:
            if self.current_row >= self.row_end:
                raise StopIteration

            cell = self.grid.get((self.current_col, self.current_row))
            self.current_col += 1

            if self.current_col >= self.col_end:
                self.current_col = self.col_start
                self.current_row += 1

            return cell

"""
Common module.
"""
from typing import Tuple, List, Any

from pygame import Rect, Vector2


class Size:
    """
    A size where width and height are constant integers.
    """

    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height

    @property
    def width(self):
        """
        Returns the width of this size.
        """
        return self._width

    @property
    def height(self):
        """
        Returns the height of this size.
        """
        return self._height

    def toTuple(self) -> Tuple[int, int]:
        """
        Converts this size to a tuple.
        """
        return self._width, self._height

    def __mul__(self, other: "Size"):
        """
        Multiplies two sizes.
        :param other: The other size to multiply.
        :return: A new size.
        """
        return Size(self._width * other._width, self._height * other._height)


class ListWrapper:
    def __init__(self, list_to_wrap: List[Any]):
        self.list = list_to_wrap


class Grid:
    """
    General grid.
    """

    def __init__(self, size: Size):
        # The size of this grid
        self.size = size

        # Cells
        self._cells: List[Any] = [None] * size.width * size.height

    def get_index(self, coordinate: Tuple[int, int]) -> Any:
        """
        Gets the index of a coordinate (x = col, y = row).
        :param coordinate: The coordinate to get the index of.
        """
        return coordinate[1] * self.size.width + coordinate[0]

    def get(self, coordinate: Tuple[int, int]) -> Any:
        """
        Retrieves a cell.
        :param coordinate: The coordinate of the cell to retrieve.
        :return: The cell at the specified coordinate (or index).
        """
        return self._cells[self.get_index(coordinate)]

    def set(self, coordinate: Tuple[int, int], cell: Any) -> None:
        """
        Sets a cell.
        :param coordinate: The coordinate of the cell to set.
        :param cell: The cell to set.
        """
        self._cells[self.get_index(coordinate)] = cell

    def __getitem__(self, index: int) -> Any:
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


class CoordinateSet:
    """
    Coordinate set allows adding and checking, but does not allow remove.
    """

    def __init__(self):
        self._coordinate_set: set = set()

    @staticmethod
    def from_rect(rect: Rect) -> "CoordinateSet":
        """
        Converts a rectangle to a coordinate set.
        """
        coordinate_set = CoordinateSet()
        for row in range(rect.y, rect.y + rect.height):
            for col in range(rect.x, rect.x + rect.width):
                coordinate_set.add((col, row))

        return coordinate_set

    def add(self, coordinate: Tuple[int, int]) -> None:
        """
        Adds a coordinate
        :param coordinate: The coordinate to add.
        """
        self._coordinate_set.add(coordinate)

    def has(self, coordinate: Tuple[int, int]) -> bool:
        """
        Checks whether a given coordinate is in the set.
        :param coordinate: The coordinate to check.
        """
        return coordinate in self._coordinate_set

    def all(self) -> set:
        """
        Returns all coordinates.
        """
        return self._coordinate_set

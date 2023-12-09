from typing import Tuple, Set

from pygame import Rect


class CoordinateSet:
    """
    Coordinate set allows adding and checking and removing coordinates.
    """

    def __init__(self):
        self._coordinate_set: Set[Tuple[int, int]] = set()

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

    def remove(self, coordinate: Tuple[int, int]) -> None:
        """
        Removes a coordinate
        """
        if coordinate in self._coordinate_set:
            self._coordinate_set.remove(coordinate)

    def all(self) -> Set[Tuple[int, int]]:
        """
        Returns all coordinates.
        """
        return self._coordinate_set

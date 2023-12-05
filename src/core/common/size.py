"""
Size module.
"""
from typing import Tuple


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
        Converts this size object to a tuple.
        """
        return self._width, self._height

    def __mul__(self, other: "Size"):
        """
        Multiplies two sizes.
        :param other: The other size to multiply.
        :return: A new size.
        """
        return Size(self._width * other._width, self._height * other._height)

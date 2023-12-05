"""
List wrapper.
"""

from typing import List, Any


class ListWrapper:
    """
    List wrapper. (In python, lists cannot be hashed. But why?)
    """

    def __init__(self, list_to_wrap: List[Any]):
        self.list = list_to_wrap

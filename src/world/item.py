from pygame import Surface


class Item:
    """
    Represents a static type of item in the game.
    """

    def __init__(self, name: str, image: Surface, max_stack: int = 1):
        # Name
        self.name: str = name

        # Image
        self.image: Surface = image

        # Max stack
        self.max_stack: int = max_stack


class GameItem:
    """
    Represents an instance of an item during gameplay.
    """

    def __init__(self, item: Item):
        # Item
        self.item: Item = item

        # Stack number
        self.stack: int = 1

    @property
    def image(self) -> Surface:
        """
        Returns the item's image.
        """
        return self.item.image

    def increase_stack(self, increment: int = 1) -> bool:
        """
        Increases the stack number.
        :param increment: The number to increase.
        :return: True if the stack number is legal after the process; false otherwise.
        """
        stack = self.stack + increment
        if stack <= self.item.max_stack:
            self.stack = stack
            return True
        else:
            return False

    def decrease_stack(self, decrement: int = 1) -> bool:
        """
        Decreases the stack number.
        :param decrement: The number to decrease.
        :return: True if the stack number is legal after the process; false otherwise.
        """
        stack = self.stack - decrement
        if stack >= 0:
            self.stack = stack
            return True
        else:
            return False

    def stack_to_full(self, increment: int) -> int:
        """
        Stacks items to the maximum stack.
        :param increment: The number to increase.
        :return: The remaining number of items.
        """
        space: int = self.item.max_stack - self.stack
        if space >= increment:
            self.stack += increment
            return 0
        else:
            self.stack = self.item.max_stack
            return increment - space

    def is_full(self) -> bool:
        """
        Checks whether the item is full.
        """
        return self.stack == self.item.max_stack

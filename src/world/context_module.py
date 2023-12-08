"""
Context module module.
"""
from src.core.context import Context


class ContextModule:
    """
    General context module.
    """

    def __init__(self, context: Context):
        # Game context
        self.context = context

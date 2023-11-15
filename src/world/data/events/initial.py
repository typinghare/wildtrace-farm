"""
Initialize functions.
"""
from src.core.context import Context
from src.world.data.tiles import Tiles
from src.world.data.frames import Frames


def fill_screen_with_grass(context: Context):
    """
    Fills the whole screen with grass tiles.
    """
    # display = context.game.display
    # (width, height) = display.grid_size
    #
    # display.get_grid(0, 0).add(Tiles.GrassSquare0)
    # display.get_grid(0, width - 1).add(Tiles.GrassSquare2)
    # display.get_grid(height - 1, 0).add(Tiles.GrassSquare6)
    # display.get_grid(height - 1, width - 1).add(Tiles.GrassSquare8)
    #
    # # First row
    # for cell in display.get_iterator(0, (1, width - 1)):
    #     cell.add(Tiles.GrassSquare1)
    #
    # # Last row
    # for cell in display.get_iterator(height - 1, (1, width - 1)):
    #     cell.add(Tiles.GrassSquare7)
    #
    # # First column
    # for cell in display.get_iterator((1, height - 1), 0):
    #     cell.add(Tiles.GrassSquare3)
    #
    # # Last column
    # for cell in display.get_iterator((1, height - 1), width - 1):
    #     cell.add(Tiles.GrassSquare5)
    #
    # # Center
    # for cell in display.get_iterator((1, height - 1), (1, width - 1)):
    #     cell.add(Tiles.GrassSquare4)


def init_water(context: Context):
    """
    Initializes water.
    """
    # display = context.game.display
    # animation_manager = context.game.animation_manager
    #
    # for cell in display.get_iterator((5, 10), (5, 10)):
    #     water_animation = animation_manager.register(Frames.Water, 2)
    #     water_animation.resume()
    #     cell.add(water_animation)

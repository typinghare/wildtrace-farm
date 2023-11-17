"""
Initialize functions.
"""
from src.core import Size
from src.core.context import Context
from src.core.display import Layer, GridLayer
from src.world.data.frames import Frames
from src.world.debug import Debug


def init_layer(context: Context) -> None:
    """
    Initializes layers.
    """
    display = context.game.display
    ground_layer = GridLayer("ground", Size(40, 30), Size(32, 32))
    character_layer = Layer(
        "character", Size(display.screen.get_width(), display.screen.get_height())
    )
    debug_layer = Layer("debug", Size(display.screen.get_width(), display.screen.get_height()))

    display.add_layer(ground_layer)
    display.add_layer(character_layer)
    display.add_layer(debug_layer)


def init_debug(context: Context) -> None:
    """
    Initializes debug tool.
    """
    # Adds debug tool to context.
    context.set("debug", Debug(context))


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
    display = context.game.display
    ground_layer: GridLayer = display.get_layer("ground")

    # Animation
    frames = Frames.Water

    def update_water(index: int):
        for row in range(0, ground_layer.grid_size.height):
            for col in range(0, ground_layer.grid_size.width):
                ground_layer.get_cell((row, col)).set_surface(frames[index])

    loop_manager = context.game.loop_manager
    loop_manager.register(2, len(frames), update_water)

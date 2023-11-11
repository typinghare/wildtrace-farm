from src.core.context import Context
from src.world.data.tiles import Tiles

def fill_screen_with_grass(context: Context):
    """
    Fills the whole screen with grass tiles.
    """
    display = context.game.display
    (width, height) = display.grid_size

    display.grid[0][0].add(Tiles.GrassSquare0)
    display.grid[0][width - 1].add(Tiles.GrassSquare2)
    display.grid[height - 1][0].add(Tiles.GrassSquare6)
    display.grid[height - 1][width - 1].add(Tiles.GrassSquare8)

    # First row
    for col in range(1, width - 1):
        display.grid[0][col].add(Tiles.GrassSquare1)

    # Last row
    for col in range(1, width - 1):
        display.grid[height - 1][col].add(Tiles.GrassSquare7)

    # First column
    for row in range(1, height - 1):
        display.grid[row][0].add(Tiles.GrassSquare3)

    # Last column
    for row in range(1, height - 1):
        display.grid[row][width - 1].add(Tiles.GrassSquare5)

    # Center
    for row in range(1, height - 1):
        for col in range(1, width - 1):
            display.grid[row][col].add(Tiles.GrassSquare4)

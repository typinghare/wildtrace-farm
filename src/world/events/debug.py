"""
Initialized events.
"""
from src.core.context import Context
from src.core.display import Layer
from src.world.debug import Debug


def init_debug(context: Context) -> None:
    """
    Initializes the debug tool.
    """
    context["debug"] = Debug.INSTANCE = Debug(context)

    # debug layer
    display = context.display
    display.append_layer("debug", Layer(display.size))


def update_debug(context: Context) -> None:
    """
    Updates debug.
    """
    debug: Debug = context["debug"]
    debug.print_all()

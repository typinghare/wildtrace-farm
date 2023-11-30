"""
Data window related events.
"""
from src.core.context import Context
from src.world.data_window import DataWindow


def init_data_window(context: Context) -> None:
    """
    Initializes data window.
    """
    context["data_window"] = DataWindow(context)


def update_data_window(context: Context) -> None:
    """
    Updates data window.
    """
    data_window: DataWindow = context["data_window"]
    data_window.update()

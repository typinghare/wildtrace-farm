from src.core.context import Context
from src.world.curtain import Curtain


def init_curtain(context: Context) -> None:
    """
    Initializes curtain.
    """
    context["curtain"] = Curtain(context)


def update_curtain(context: Context) -> None:
    """
    Updates the curtain.
    """
    curtain: Curtain = context["curtain"]
    curtain.update()

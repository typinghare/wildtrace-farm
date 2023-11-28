from src.core.context import Context
from src.core.display import Layer
from src.world.message_box import MessageBox


def init_message_box(context: Context) -> None:
    """
    Initializes message box.
    """
    message_box = context["message_box"] = MessageBox(context)
    message_box.play("Hello world! You mom died yesterday!")


def update_message_box(context: Context) -> None:
    """
    Updates message box.
    """
    message_box: MessageBox = context["message_box"]
    message_box.update()

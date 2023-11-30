"""
Game related functions.
"""
from src.core.context import Context
from src.world.message_box import MessageBox


def init_flags(context: Context) -> None:
    """
    Initializes flags.
    """
    # context["flag.enter_game"] = False
    # context["flag.been_to_farm"] = False

    context["flag.enter_game"] = True
    context["flag.been_to_farm"] = True


def before_all(context: Context) -> None:
    """
    Called before all updates.
    """

    if not context["flag.enter_game"]:
        enter_game(context)


def enter_game(context: Context) -> None:
    """
    Called when the player first enters the game.
    """
    context["flag.enter_game"] = True

    message_box: MessageBox = context["message_box"]

    def second() -> None:
        message_box.play(
            "Press number keys [0] to [9] to change the selected items.\n"
            "Press [J] to use an item.\n",
            third,
        )

    message_box.play(
        "Welcome to play Wildtrace Farm!\n"
        "Press [W] to move upward;\n"
        "Press [S] to move downward;\n"
        "Press [A] to move leftward;\n"
        "Press [D] to move rightward.\n",
        second,
    )

    def third() -> None:
        message_box.play("When you want to sleep, get close to the bed and press [J].\n")


def first_time_to_farm(context: Context) -> None:
    """
    Called when the player first arrives at the farm.
    """
    context["flag.been_to_farm"] = True

    message_box: MessageBox = context["message_box"]
    message_box.play(
        "You are now at the farm. You can sow seeds on plowed land.\n"
        "Press 3 or 4 to select seeds.\n"
        "Press J on the plowed land to sow seeds!"
    )

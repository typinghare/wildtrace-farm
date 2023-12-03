"""
Game related functions.
"""
from src.core.common import Size
from src.core.context import Context
from src.world.context_getters import get_character
from src.world.data.registries import Registries
from src.world.item.chest import Chest
from src.world.item.crop_item import CropItem
from src.world.message_box import MessageBox


def init_flags(context: Context) -> None:
    """
    Initializes flags.
    """
    is_debug = context.settings.debug

    context["flag.enter_game"] = is_debug
    context["flag.been_to_farm"] = is_debug
    context["flag.first_open_chest"] = not is_debug
    context["flag.first_time_to_harvest"] = not is_debug


def before_all(context: Context) -> None:
    """
    Called before all updates.
    """

    if not context["flag.enter_game"]:
        enter_game(context)

    # Chests
    context["shipping_chest"] = Chest(Size(10, 3))
    context["home_chest"] = Chest(Size(10, 3))

    # Item-crop mapping
    crop_item_mapping = context["crop_item_mapping"] = {}
    for ref in Registries.CropItem.get_ref_list():
        crop_item: CropItem = ref.res
        crop_item_mapping[crop_item.item] = crop_item.crop

    # shipping_chest: Chest = context["shipping_chest"]
    # shipping_chest.stack_item(Items.BeetProduct, 2)
    # shipping_chest.stack_item(Items.WheatProduct, 3)


def enter_game(context: Context) -> None:
    """
    Called when the player first enters the game.
    """
    context["flag.enter_game"] = True

    message_box: MessageBox = context["message_box"]

    def third() -> None:
        message_box.play(
            "When you want to sleep, get close to the bed and press [J].\n"
            "Your crops will grow overnight!",
        )

    def second() -> None:
        message_box.play(
            "Press number keys [0] to [9] to select items.\n"
            "Press [J] to use an item, open a door or a chest.\n",
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


def first_time_to_farm(context: Context) -> None:
    """
    Called when the player first arrives at the farm.
    """
    context["flag.been_to_farm"] = True

    message_box: MessageBox = context["message_box"]

    def second() -> None:
        message_box.play(
            "Remember to water your crops.\nMaking them happy will boost their growth."
        )

    message_box.play(
        "You are now at the farm. You can sow seeds on plowed land.\n"
        "Press [3] or [4] to select seeds.\n"
        "Press [J] on the plowed land to sow seeds!",
        second,
    )

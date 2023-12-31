"""
Item resource modules.
"""
from src.registry import RegistryUtil, Tag
from src.world.data.registries import Registries
from src.world.data.tiles import Tiles
from src.world.item.item import Item


def register(path: str, item: Item) -> Item:
    """
    Register an item.
    :param path: The path of the item.
    :param item: The Item to register.
    :return: The item.
    """
    return Registries.Item.register(RegistryUtil.createLoc(path), item)


class Items:
    """
    Item resources.
    """

    # Tools
    WateringCan = register("tool/watering_can", Item("Watering Can", Tiles.ToolWateringCan))
    Hoe = register("tool/hoe", Item("Hoe", Tiles.ToolHoe))

    # Seeds
    WheatSeeds = register("seeds/wheat", Item("Wheat Seeds", Tiles.WheatSeeds, 64))
    BeetSeeds = register("seeds/beet", Item("Beet Seeds", Tiles.BeetSeeds, 64))
    CarrotSeeds = register("seeds/carrot", Item("Carrot Seeds", Tiles.CarrotSeeds, 64))
    CauliflowerSeeds = register(
        "seeds/cauliflower", Item("Cauliflower Seeds", Tiles.CauliflowerSeeds, 64)
    )
    EggplantSeeds = register("seeds/eggplant", Item("Eggplant Seeds", Tiles.EggplantSeeds, 64))
    PumpkinSeeds = register("seeds/pumpkin", Item("Pumpkin Seeds", Tiles.PumpkinSeeds, 64))

    # Product
    WheatProduct = register("product/wheat", Item("Wheat", Tiles.WheatProduct, 64))
    BeetProduct = register("product/beet", Item("Beet", Tiles.BeetProduct, 64))
    CarrotProduct = register("product/carrot", Item("Carrot", Tiles.CarrotProduct, 64))
    CauliflowerProduct = register(
        "product/cauliflower", Item("Cauliflower", Tiles.CauliflowerProduct, 64)
    )
    EggplantProduct = register("product/eggplant", Item("Eggplant", Tiles.EggplantProduct, 64))
    PumpkinProduct = register("product/pumpkin", Item("Pumpkin", Tiles.PumpkinProduct, 64))


class ItemTags:
    """
    Item tags.
    """

    TOOL = Tag("TOOL")
    SEEDS = Tag("SEEDS")


# tool tag
tool_items = [Items.WateringCan, Items.Hoe]
for tool_item in tool_items:
    ref = Registries.Item.get_ref_by_res(tool_item)
    ref.bind_tag(ItemTags.TOOL)

# seeds tag
seeds_items = [
    Items.WheatSeeds,
    Items.BeetSeeds,
    Items.CarrotSeeds,
    Items.CauliflowerSeeds,
    Items.EggplantSeeds,
    Items.PumpkinSeeds,
]
for seeds_item in seeds_items:
    ref = Registries.Item.get_ref_by_res(seeds_item)
    ref.bind_tag(ItemTags.SEEDS)

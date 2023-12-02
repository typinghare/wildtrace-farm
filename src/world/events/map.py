"""
Map crafting events.
"""
from src.core.constant import Direction
from src.core.context import Context
from src.world.character import Character
from src.world.data.maps import Maps
from src.world.scene_manager import SceneManager


def init_map(context: Context) -> None:
    """
    Initializes scene manager.
    """
    scene_manger = context["scene_manager"] = SceneManager(context)

    def init_character_position():
        character: Character = context["character"]
        character.teleport((2, 4))
        character.facing = Direction.RIGHT

    scene_manger.change_map(Maps.Home, init_character_position)


def update_map(context: Context) -> None:
    """
    Updates the scene.
    """
    scene_manager: SceneManager = context["scene_manager"]
    scene_manager.update_scene()

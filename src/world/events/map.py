"""
Map crafting events.
"""
from pygame import Vector2

from src.core.context import Context
from src.world.data.maps import Maps
from src.world.scene_manager import SceneManager


def init_map(context: Context) -> None:
    """
    Initializes scene manager.
    """
    scene_manger = context["scene_manager"] = SceneManager(context)
    scene_manger.load_map(Maps.Home)
    # scene_manger.load_map(Maps.Farm)


def update_map(context: Context) -> None:
    """
    Updates the scene.
    """
    scene_manager: SceneManager = context["scene_manager"]
    scene_manager.update_scene()

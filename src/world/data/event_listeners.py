"""
Event listener source module.
"""
from typing import Callable, cast

from src.registry import RegistryUtil
from src.core.context import Context
from src.core.event import EventListener
from src.core.event_types import EventTypes
from src.world.data.registries import Registries
from src.world.data.events import fill_screen_with_grass, init_water


def register(
    path: str, event_type: int, callback: Callable[[Context | None], None]
) -> EventListener:
    """
    Registers an event listener.
    :param path:
    :param event_type:
    :param callback:
    :return: The event listener.
    """
    return cast(
        EventListener,
        Registries.EventListener.register(
            RegistryUtil.createLoc(path), EventListener(event_type, callback)
        ),
    )


class EventListeners:
    """
    Event listener resources.
    """

    FillScreenWithGrass = register(
        "fill_screen_with_grass", EventTypes.ON_START, fill_screen_with_grass
    )

    InitWater = register("init_water", EventTypes.ON_START, init_water)

import pygame
from pygame import Vector2

from src.core.context import Context
from src.core.display import Layer
from src.world.data.tiles import Tiles


class Tool:
    # The number of tool
    NUMBER = 2

    Hoe = 0
    WateringCan = 1


def init_tool(context: Context) -> None:
    """
    Initializes tool.
    """
    # layer
    context.display.set_layer("tool", Layer(context.display.size))

    context["current_tool"] = Tool.Hoe
    context["tool_buffer"] = None
    render_tool_layer(context, Tool.Hoe)


def update_tool(context: Context) -> None:
    """
    Updates tool.
    """
    tool_buffer: int = context["tool_buffer"]

    if tool_buffer is not None:
        context["current_tool"] = tool_buffer
        context["tool_buffer"] = None

        render_tool_layer(context, tool_buffer)


def tool_key_up(context: Context) -> None:
    """
    Tool key up.
    """
    key = context.event_data.get("key")
    if key == pygame.K_t:
        tool: int = context["current_tool"]
        context["tool_buffer"] = (tool + 1) % Tool.NUMBER


def render_tool_layer(context: Context, tool: int) -> None:
    """
    Renders the tool layer with the given tool.
    """
    tool_layer: Layer = context.display.get_layer("tool")
    cell_size = context.settings.display_cell_size
    offset = Vector2(cell_size.width // 2, cell_size.height // 2)

    tool_layer.clear()

    if tool == Tool.Hoe:
        tool_layer.blit(Tiles.ToolHoe, offset)
    elif tool == Tool.WateringCan:
        tool_layer.blit(Tiles.ToolWaterCan, offset)

"""
Data window module
"""
from pygame import Vector2, Surface

from src.core.common import Size
from src.core.context import Context
from src.core.display import Layer
from src.world.util import get_font


class Time:
    """
    Time.
    """

    def __init__(self, hour: int, minute: int):
        # Hour (0 ~ 23)
        self.hour: int = hour

        # Minute (0 ~ 60)
        self.minute: int = minute

    def __repr__(self):
        """
        Returns this time in the form of "HH:mm XM"
        """
        suffix = "AM" if self.hour < 12 else "PM"
        hour = str(self.hour)
        minute = str(self.minute)

        if self.hour <= 9:
            hour = "0" + hour

        if self.minute <= 9:
            minute = "0" + minute

        return f"{hour}:{minute} {suffix}"


class DataWindow:
    """
    Data window.
    """

    def __init__(self, context: Context):
        # Game context
        self.context = context

        # Day
        self.day: int = 1

        # Time
        self.time: Time = Time(6, 0)

        # Money
        self.money: int = 0

        # Layer
        self.layer = Layer(Size(150, 130))

        # Init
        self._init_layer()

    def _init_layer(self) -> None:
        """
        Initializes layer.
        """
        self.context.display.set_layer("data_window", self.layer)

        screen_size = self.context.display.size
        size = self.layer.size
        self.layer.offset = Vector2(
            screen_size.width - size.width, (screen_size.height - size.height) * 0.1
        )

        self.layer.surface.fill("#c38e70")

    def update(self) -> None:
        """
        Updates the layer
        """
        # Day 1
        # 15:50 AM
        # $ 000000

        text_font = get_font(35)

        # Day
        day_surface = Surface((130, 30))
        day_surface.fill("white")
        day_text = text_font.render(f"Day    {self.day}", False, "black")
        day_surface.blit(day_text, (10, 3))
        self.layer.blit(day_surface, Vector2(10, 10))

        # Time
        time_surface = Surface((130, 30))
        time_surface.fill("white")
        time_text = text_font.render(str(self.time), False, "black")
        time_surface.blit(time_text, (10, 3))
        self.layer.blit(time_surface, Vector2(10, 50))

        # Money
        money_surface = Surface((130, 30))
        money_surface.fill("white")
        money_text = text_font.render("$      0", False, "black")
        money_surface.blit(money_text, (10, 3))
        self.layer.blit(money_surface, Vector2(10, 90))

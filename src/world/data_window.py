"""
Data window module
"""
from pygame import Vector2, Surface

from src.core.common import Size
from src.core.context import Context
from src.core.display import Layer
from src.core.loop import Loop
from src.world.context_module import ContextModule
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

    def increase_minute(self, increment: int) -> None:
        """
        Increases minutes
        """
        self.minute += increment
        while self.minute >= 60:
            self.hour += 1
            self.minute -= 60

        self.hour %= 24


class DataWindow(ContextModule):
    """
    Data window.
    """

    def __init__(self, context: Context):
        super().__init__(context)

        # Day
        self.day: int = 1

        # Time
        self.time: Time = Time(6, 0)

        # Money
        self.money: int = 0

        # Layer
        self.layer = Layer(Size(170, 130))

        # Time elapse loop
        self.time_elapse_loop: Loop | None = None

        # Init
        self._init_layer()
        self._init_time_elapse()

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

    def _init_time_elapse(self) -> None:
        """
        Initializes time elapse. Increase 10 minutes in game every 5 seconds in real life.
        """
        loop_manager = self.context.loop_manager
        count_per_period: int = 5

        def time_elapse(index: int) -> None:
            if index != count_per_period - 1:
                return

            self.time.increase_minute(10)
            if self.time.hour == 0:
                # Next day
                pass

        self.time_elapse_loop = loop_manager.loop(1, count_per_period, time_elapse)

    def update(self) -> None:
        """
        Updates the layer
        """
        # Day 1
        # 15:50 AM
        # $ 000000

        text_font = get_font(24, "manaspace/manaspc.ttf")

        # Day
        day_surface = Surface((150, 30))
        day_surface.fill("white")
        day_text = text_font.render(f"Day{str(self.day).rjust(5)}", False, "blue")
        self.layer.blit(day_surface, Vector2(10, 10))
        self.layer.blit(day_text, Vector2(20, 16))

        # Time
        time_surface = Surface((150, 30))
        time_surface.fill("white")
        time_text = text_font.render(str(self.time), False, "pink")
        self.layer.blit(day_surface, Vector2(10, 50))
        self.layer.blit(time_text, Vector2(20, 56))

        # Money
        money_surface = Surface((150, 30))
        money_surface.fill("white")
        money_text = text_font.render(f"${str(self.money).rjust(7)}", False, "orange")
        self.layer.blit(money_surface, Vector2(10, 90))
        self.layer.blit(money_text, Vector2(20, 96))

    def reset_time(self) -> None:
        """
        Resets the time.
        """
        self.time = Time(6, 0)
        self.time_elapse_loop.reset()

"""
Loop module.
"""
from typing import Callable, List


class Loop:
    """
    A frame-based loop that triggers a callback at specified intervals.
    """

    def __init__(self, fps: int, count_per_period: int, callback: Callable[[int], None]):
        # Frame per second, or count per second
        self.fps = fps

        # Number of counts per period
        self.count_per_period = count_per_period

        # Callback function to be triggered
        self.callback = callback

        # Time in milliseconds for one count
        self.each_count_time = 1000 / fps

        # Time elapsed since the last update
        self.elapsed_time: float = 0

        # Current count
        self.current_count: int = 0

    def update(self, dt: float) -> None:
        """
        Update the frame-based loop. The callback is triggered at each count.
        :param dt: The delta time.
        """
        self.elapsed_time += dt

        if self.elapsed_time > (self.current_count + 1) * self.each_count_time:
            self.current_count += 1
            if self.current_count >= self.count_per_period:
                self.elapsed_time = 0
                self.current_count = 0

            self.callback(self.current_count)


class LoopManager:
    """
    Loop manager.
    """

    def __init__(self):
        # List of loops
        self.loop_list: List[Loop] = []

    def register(self, fps: int, count_per_period: int, callback: Callable[[int], None]) -> Loop:
        """
        Registers a loop.
        :param fps: Frame per second, or count per second.
        :param count_per_period: Number of counts per period.
        :param callback: Callback function to be triggered.
        :return: The loop registered.
        """
        loop = Loop(fps, count_per_period, callback)
        self.loop_list.append(loop)

        return loop

    def update(self, dt: float) -> None:
        """
        Updates all loops.
        """
        for loop in self.loop_list:
            loop.update(dt)
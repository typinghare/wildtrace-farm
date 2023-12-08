"""
Loop module.
"""
from typing import Callable, List

from src.core.common import CallbackNode


class Loop:
    """
    A frame-based loop that triggers a callback at specified intervals.
    """

    def __init__(self, fps: float, count_per_period: int, callback: Callable[[int], None]):
        # Frame per second, or count per second
        self.fps: float = fps

        # Number of counts per period
        self.count_per_period: int = count_per_period

        # Callback function to be triggered
        self.callback: Callable[[int], None] = callback

        # Time in milliseconds for one count
        self.each_count_time: float = 1000 / fps

        # Time elapsed since the last update
        self.elapsed_time: float = 0

        # Current count
        self.current_count: int = -1

        # Whether it is paused
        self.paused: bool = False

    def update(self, dt: float) -> None:
        """
        Update the frame-based loop. The callback is triggered at each count.
        :param dt: The delta time.
        """
        self.elapsed_time += dt

        if self.elapsed_time < (self.current_count + 1) * self.each_count_time:
            return

        self.current_count += 1
        if self.current_count >= self.count_per_period:
            self.reset()

        self.callback(self.current_count)

    def reset(self) -> None:
        """
        Resets this loop.
        """
        self.elapsed_time = 0
        self.current_count = 0


class LoopManager:
    """
    Loop manager.
    """

    def __init__(self):
        # A list of loops
        self._loops: List[Loop] = []

    def loop(self, fps: float, count_per_period: int, callback: Callable[[int], None]) -> Loop:
        """
        Registers a loop.
        :param fps: Frame per second, or count per second.
        :param count_per_period: Number of counts per period.
        :param callback: Callback function to be called.
        :return: The loop registered.
        """
        loop = Loop(fps, count_per_period, callback)
        self._loops.append(loop)

        return loop

    def once(self, fps: float, count_per_period: int, callback: Callable[[int], None]) -> Loop:
        """
        Registers a loop that will be deleted after one period.
        :param fps: Frames per second, or counts per second.
        :param count_per_period: Number of counts per period.
        :param callback: Callback function to be called when indices change.
        :return: The once loop registered.
        """

        def fn(index: int) -> None:
            callback(index)
            if index == count_per_period - 1:
                self._loops.remove(loop)

        loop = Loop(fps, count_per_period, fn)
        self._loops.append(loop)

        return loop

    def delay(self, delay_ms: int, callback: Callable[[], None]) -> Loop:
        """
        Schedules a callback function to be executed after a specified delay.
        :param delay_ms: The delay time in milliseconds.
        :param callback: The function to be called after the delay.
        :return: The registered loop.
        """

        def delay_fn(index: int) -> None:
            if index == 1:
                callback()
                self._loops.remove(loop)

        loop = self.loop(1000 / delay_ms, 2, delay_fn)
        self._loops.append(loop)

        return loop

    def delay_methodical(self, delay_ms: int) -> CallbackNode:
        """
        Schedules a callback function to be executed after a specified delay.
        :param delay_ms: The delay time in milliseconds.
        :return: The callback node.
        """
        callback_node = CallbackNode()

        def delay_fn(index: int) -> None:
            if index == 1:
                callback_node.invoke()
                self._loops.remove(loop)

        loop = self.loop(1000 / delay_ms, 2, delay_fn)
        self._loops.append(loop)

        return callback_node

    def remove(self, loop: Loop) -> None:
        """
        Removes a loop from the list if it exists.
        :param loop: The loop to remove.
        """
        if loop in self._loops:
            self._loops.remove(loop)

    def update(self, dt: float) -> None:
        """
        Updates all loops.
        """
        for loop in self._loops:
            if loop.paused:
                continue

            loop.update(dt)

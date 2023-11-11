"""
Animation module.
"""
from typing import List

from pygame import Surface


class Animation:
    """
    Game animation.
    """

    def __init__(self, frames: List[Surface], fps: int, game_fps: int):
        # Surface sequences
        self.frames: List[Surface] = frames

        # Game FPS
        self.game_fps: int = game_fps

        # Animation FPS
        self.fps: int = fps

        # Interval game frames between two animation frames
        self.frame_interval: int = game_fps // fps + 1

        # Whether the animation is running
        self.is_running: bool = False

        # Frame counter
        self.frame_counter: int = 0

        # Current frame index
        self.current_frame_index: int = 0

    def get_current_frame(self) -> Surface:
        """
        Returns the current frame.
        """
        return self.frames[self.current_frame_index]

    def update_frame_counter(self):
        """
        Updates the frame counter; updates the current frame index based on the frame counter.
        """
        self.frame_counter += 1
        self.current_frame_index = self.frame_counter // self.frame_interval

        if self.current_frame_index == len(self.frames):
            self.restore()

    def resume(self):
        """
        Resumes the animation.
        """
        self.is_running = True

    def pause(self):
        """
        Pauses the animation.
        """
        self.is_running = False

    def restore(self):
        """
        Restores to the initial frame.
        """
        self.frame_counter = 0
        self.current_frame_index = 0


class AnimationManager:
    """
    Animation manager.
    """

    def __init__(self, game_fps: int):
        # Game FPS
        self.game_fps = game_fps

        # List of animations
        self.animation_list: List[Animation] = []

        # Frame counters
        self.frame_counter = 0

    def register(self, frames: List[Surface], fps: int) -> Animation:
        """
        Registers an animation.
        :param frames: A sequence of frames.
        :param fps: The FPS of the animation.
        :return: The animation.
        """
        animation = Animation(frames, fps, self.game_fps)
        self.animation_list.append(animation)

        return animation

    def update_frame(self):
        """
        Updates the frame indices in all animations that are running.
        """
        for animation in self.animation_list:
            if not animation.is_running:
                continue

            animation.update_frame_counter()

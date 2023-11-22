"""
Character module.
"""
from typing import List

from pygame import Vector2, Surface

from src.core.constant import Direction
from src.core.context import Context
from src.core.display import Layer
from src.world.data.frames import Frames


class Character:
    """
    Main character in the game.
    """

    def __init__(self, context: Context):
        # Game context
        self.context: Context = context

        # Animation frames list
        self.frames_list: list[List[Surface]] = [
            Frames.CharacterIdleUp.list,
            Frames.CharacterIdleRight.list,
            Frames.CharacterIdleDown.list,
            Frames.CharacterIdleLeft.list,
            Frames.CharacterMoveUp.list,
            Frames.CharacterMoveRight.list,
            Frames.CharacterMoveDown.list,
            Frames.CharacterMoveLeft.list,
        ]

        # Current facing direction
        self.facing: int = Direction.DOWN

        # Current frames
        self.current_frames: List[Surface] = self.frames_list[self.facing]

        # velocity vector
        self.velocity: Vector2 = Vector2(0, 0)

    def init_animation(self) -> None:
        display = self.context.game.display
        character_layer: Layer = display.get_layer("character")
        character_size = self.context.settings.character_size
        center_coordinate = (
            display.center[0] - character_size.width // 2,
            display.center[1] - character_size.height // 2,
        )
        character_layer.offset = center_coordinate
        character_default_fps = self.context.settings.character_animation_fps

        def update_image(index: int):
            character_layer.clear()
            character_layer.blit(self.current_frames[index])

        loop_manager = self.context.game.loop_manager
        loop_manager.register(character_default_fps, len(self.current_frames), update_image)

    def move(self, direction: int) -> None:
        """
        Starts the displacement on a specified direction.
        :param direction: The specified direction.
        """
        self.facing = direction
        self.current_frames = self.frames_list[direction + 4]

        if direction == Direction.UP:
            self.velocity.y -= 1
        elif direction == Direction.RIGHT:
            self.velocity.x += 1
        elif direction == Direction.DOWN:
            self.velocity.y += 1
        elif direction == Direction.LEFT:
            self.velocity.x -= 1

    def stop(self, direction: int) -> None:
        """
        Stops the displacement on a specified direction.
        :param direction: The specified direction.
        """
        if direction == Direction.UP:
            self.velocity.y += 1
        elif direction == Direction.RIGHT:
            self.velocity.x -= 1
        elif direction == Direction.DOWN:
            self.velocity.y -= 1
        elif direction == Direction.LEFT:
            self.velocity.x += 1

        if self.velocity.magnitude() == 0:
            self.current_frames = self.frames_list[direction]

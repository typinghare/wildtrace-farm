"""
Character module.
"""
from typing import List, Tuple

from pygame import Vector2, Surface

from src.core.common import Size
from src.core.constant import Direction
from src.core.context import Context
from src.core.display import Layer, GridLayer
from src.world.camera import Camera
from src.world.data.frames import Frames
from src.world.debug import Debug
from src.world.map import MapController


class Character:
    """
    Main character in the game.
    """

    def __init__(self, context: Context):
        # Game context
        self.context: Context = context

        # Character size
        self.size: Size = context.settings.character_size

        # Animation frames list
        self.frames_list: List[List[Surface]] = [
            Frames.CharacterIdleUp.list,
            Frames.CharacterIdleRight.list,
            Frames.CharacterIdleDown.list,
            Frames.CharacterIdleLeft.list,
            Frames.CharacterMoveUp.list,
            Frames.CharacterMoveRight.list,
            Frames.CharacterMoveDown.list,
            Frames.CharacterMoveLeft.list,
        ]

        # Current frames
        self.current_frames: List[Surface] = self.frames_list[Direction.DOWN]

        # A list to stores the key-pressing status of each direction
        self.key_status = [False] * 4

        # A list to stores the movement status of each direction
        self.movement_status = [False] * 4

        # Current facing direction
        self.facing: int = Direction.DOWN

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
        self.key_status[direction] = True
        opposite = Direction.opposite_of(direction)
        if not self.key_status[opposite]:
            self.facing = direction
            self.movement_status[direction] = True

        self._update_after_key_status_change()

    def stop(self, direction: int) -> None:
        """
        Stops the displacement on a specified direction.
        :param direction: The specified direction.
        """
        self.key_status[direction] = False
        self.movement_status[direction] = False
        opposite = Direction.opposite_of(direction)
        if self.key_status[opposite]:
            # Begin to move towards the opposite direction
            self.facing = opposite
            self.movement_status[opposite] = True

        self._update_after_key_status_change()

    def _update_after_key_status_change(self) -> None:
        """
        Updates after key status changes.
        """
        # Check if it is idle
        is_idle = True
        direction_count = 0
        for direction in range(0, 4):
            if self.movement_status[direction]:
                is_idle = False
                direction_count += 1

        # correct facing if direction count is 1
        if direction_count == 1:
            curr_direction = Direction.UP
            for direction in range(1, 4):
                if self.movement_status[direction]:
                    curr_direction = direction
                    break
            self.facing = curr_direction

        if is_idle:
            self.current_frames = self.frames_list[self.facing]
        else:
            self.current_frames = self.frames_list[self.facing + 4]

    def get_unit_velocity(self) -> Vector2:
        """
        Returns the velocity unit vector.
        """
        x, y = 0, 0
        if self.movement_status[Direction.UP]:
            y -= 1
        elif self.movement_status[Direction.DOWN]:
            y += 1
        if self.movement_status[Direction.RIGHT]:
            x += 1
        elif self.movement_status[Direction.LEFT]:
            x -= 1

        velocity = Vector2(x, y)
        if velocity.magnitude() > 0:
            velocity = velocity.normalize()

        return velocity

    def update(self) -> None:
        """
        Updates this character.
        """
        dt = self.context.dt
        velocity = self.get_unit_velocity()
        displacement = Vector2(velocity.x * dt * 0.2, velocity.y * dt * 0.2)

        # Camera moves
        camera: Camera = self.context["camera"]
        camera.move(displacement)

        # Check collision
        virtual_center: Tuple[int, int] = camera.get_virtual_center()
        map_controller: MapController = self.context["map_controller"]
        map_offset = map_controller.offset
        character_center = (virtual_center[0] - map_offset.x, virtual_center[1] - map_offset.y)

        # Find which cell the character center is in
        cell_size = self.context.settings.display_cell_size
        row: int = character_center[0] // cell_size.width
        col: int = character_center[1] // cell_size.height
        coordinate = (row, col)
        Debug.INSTANCE.get_module("character_center").print(coordinate)

        self._update_character_layer()

    def _update_character_layer(self) -> None:
        """
        Updates character layer.
        """
        camera: Camera = self.context["camera"]
        virtual_center: Tuple[int, int] = camera.get_virtual_center()
        character_layer: GridLayer = self.context.display.get_layer("character")
        character_layer.offset = Vector2(
            virtual_center[0] - self.size.width // 2,
            virtual_center[1] - self.size.height // 2,
        )

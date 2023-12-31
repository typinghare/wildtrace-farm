"""
Character module.
"""
from typing import List, Tuple

from pygame import Vector2, Surface, Rect

from src.core.common import Size
from src.core.constant import Direction
from src.core.context import Context
from src.core.display import Layer, GridLayer
from src.core.loop import Loop
from src.world.camera import Camera
from src.world.context_module import ContextModule
from src.world.data.frames import Frames
from src.world.debug import Debug
from src.world.map import MapController
from src.world.scene_manager import SceneManager


class Character(ContextModule):
    """
    Main character in the game.
    """

    class Action:
        """
        Character actions.
        """

        Idle = 0
        Move = 1
        Water = 2
        Hoe = 3

    def __init__(self, context: Context):
        super().__init__(context)

        # Character size (surface)
        self.size: Size = context.settings.character_size

        # Character collision box size
        self.collision_box_size: Size = Size(16, 32)

        # Cell size
        self.cell_size = self.context.settings.display_cell_size

        # Animation frames list
        self.frames_list: List[List[Surface]] = [
            # Idle
            Frames.CharacterIdleUp.list,
            Frames.CharacterIdleRight.list,
            Frames.CharacterIdleDown.list,
            Frames.CharacterIdleLeft.list,
            # Move
            Frames.CharacterMoveUp.list,
            Frames.CharacterMoveRight.list,
            Frames.CharacterMoveDown.list,
            Frames.CharacterMoveLeft.list,
            # Water
            Frames.CharacterWaterUp.list,
            Frames.CharacterWaterRight.list,
            Frames.CharacterWaterDown.list,
            Frames.CharacterWaterLeft.list,
            # Hoe
        ]

        # Character action
        self.action: int = Character.Action.Idle

        # A list to stores the key-pressing status of each direction
        self.key_status = [False] * 4

        # A list to stores the movement status of each direction
        self.movement_status = [False] * 4

        # Current facing direction
        self.facing: int = Direction.DOWN

        # Character layer
        self.layer: Layer = Layer(self.context.settings.character_size)

        # Character cannot move when it is frozen
        self.frozen: bool = False

        # Animation loop
        self.loop: Loop | None = None

        # Previous frames
        self.previous_frames: List[Surface] = self.frames_list[0]

        # init
        self._init_layer()
        self._init_animation()

    def _init_layer(self) -> None:
        """
        Initializes layer.
        """
        self.context.display.set_layer("character", self.layer)

    def _init_animation(self) -> None:
        display = self.context.game.display
        character_layer: Layer = display.get_layer("character")
        character_size = self.context.settings.character_size
        center_coordinate = (
            display.center[0] - character_size.width // 2,
            display.center[1] - character_size.height // 2,
        )
        character_layer.offset = center_coordinate
        default_fps = self.context.settings.character_animation_fps

        self.previous_frames = self.get_current_frame_list()

        def update_image(index: int) -> None:
            if self.frozen:
                return

            character_layer.clear()

            current_frames = self.get_current_frame_list()
            if current_frames == self.previous_frames:
                character_layer.blit(current_frames[index])
            else:
                self.loop.reset()
                self.previous_frames = current_frames
                character_layer.blit(current_frames[0])

        self.loop = self.context.loop_manager.loop(default_fps, 8, update_image)

    def get_current_frame_list(self) -> List[Surface]:
        """
        Returns the frame list based on character's current action and facing.
        """
        return self.frames_list[self.action * 4 + self.facing]

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

    def stop_all(self) -> None:
        """
        Stops character's movement on all directions.
        """
        for direction in range(0, 4):
            self.key_status[direction] = False
            self.movement_status[direction] = False

    def teleport(self, coordinate: Tuple[int, int]) -> None:
        """
        Teleports the character to a certain coordinate.
        NOTE: It will cause a bug if the coordinate is blocked.
        """
        # Get the center (pixel) of the coordinate
        center = (
            coordinate[0] * self.cell_size.width,
            coordinate[1] * self.cell_size.height,
        )

        camera: Camera = self.context["camera"]
        screen_size = self.context.display.size
        map_offset = self._get_map_offset()
        # [MATH] virtual_center = (camera.offset + screen.size) / 2
        # camera.offset = virtual_center * 2 - screen.size
        camera.offset = Vector2(
            (map_offset.x + center[0]) * 2 - screen_size.width + self.size.width // 2,
            (map_offset.y + center[1]) * 2 - screen_size.height + self.size.height // 2,
        )

    def _update_after_key_status_change(self) -> None:
        """
        Updates after key status changes.
        """
        # Check if it is idle
        direction_count = 0  # The number of direction the character is moving towards
        for direction in range(0, 4):
            if self.movement_status[direction]:
                direction_count += 1

        # The character is idle if the direction count is 0
        is_idle = direction_count == 0

        # correct facing if direction count is 1
        if direction_count == 1:
            curr_direction = Direction.UP
            for direction in range(1, 4):
                if self.movement_status[direction]:
                    curr_direction = direction
                    break
            self.facing = curr_direction

        if is_idle:
            self.action = Character.Action.Idle
        else:
            self.action = Character.Action.Move

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
        if self.frozen:
            return

        if self.action < Character.Action.Move:
            self._update_after_key_status_change()

        self._update_camera()
        self._update_character_layer()
        # Debug.get_module("coordinate").print(self.get_coordinate())

    def get_current_center(self) -> Tuple[int, int]:
        camera: Camera = self.context["camera"]
        virtual_center: Tuple[int, int] = camera.get_virtual_center()
        map_offset = self._get_map_offset()
        return virtual_center[0] - map_offset.x, virtual_center[1] - map_offset.y

    def get_coordinate(self) -> Tuple[int, int]:
        """
        Returns character's current coordinate.
        """
        current_center = self.get_current_center()

        return (
            int(current_center[0] // self.cell_size.width),
            int(current_center[1] // self.cell_size.height),
        )

    def get_front_coordinate(self) -> Tuple[int, int]:
        """
        Returns the front coordinate.
        """
        coordinate = self.get_coordinate()

        if self.facing == Direction.UP:
            return coordinate[0], coordinate[1] - 1
        if self.facing == Direction.RIGHT:
            return coordinate[0] + 1, coordinate[1]
        if self.facing == Direction.DOWN:
            return coordinate[0], coordinate[1] + 1
        if self.facing == Direction.LEFT:
            return coordinate[0] - 1, coordinate[1]

    def _update_camera(self) -> None:
        """
        Updates camera.
        """

        dt = self.context.dt
        velocity = self.get_unit_velocity()
        displacement = Vector2(velocity.x * dt * 0.2, velocity.y * dt * 0.2)

        # Get the character center
        camera: Camera = self.context["camera"]
        scene_manager: SceneManager = self.context["scene_manager"]
        map_controller: MapController = scene_manager.controller
        current_center = self.get_current_center()
        next_center = Vector2(
            current_center[0] + displacement.x, current_center[1] + displacement.y
        )

        # Find which cell the character center will be in
        col: int = int(next_center.x // self.cell_size.width)
        row: int = int(next_center.y // self.cell_size.height)
        character_rect = Rect(
            next_center.x - self.collision_box_size.width // 2,
            next_center.y - self.collision_box_size.height // 2,
            self.collision_box_size.width,
            self.collision_box_size.height,
        )

        up_coordinate = (col, row - 1)
        right_coordinate = (col + 1, row)
        down_coordinate = (col, row + 1)
        left_coordinate = (col - 1, row)
        up_rect = self.get_rect(up_coordinate)
        right_rect = self.get_rect(right_coordinate)
        down_rect = self.get_rect(down_coordinate)
        left_rect = self.get_rect(left_coordinate)

        def is_collide(coordinate: Tuple[int, int], rect: Rect):
            return (
                rect is not None
                and map_controller.is_block(coordinate)
                and character_rect.colliderect(rect)
            )

        if is_collide(up_coordinate, up_rect):
            next_center.y = up_rect.bottom + self.collision_box_size.height // 2
        if is_collide(right_coordinate, right_rect):
            next_center.x = right_rect.left - self.collision_box_size.width // 2
        if is_collide(down_coordinate, down_rect):
            next_center.y = down_rect.top - self.collision_box_size.height // 2
        if is_collide(left_coordinate, left_rect):
            next_center.x = left_rect.right + self.collision_box_size.width // 2

        real_displacement = Vector2(
            next_center.x - current_center[0], next_center.y - current_center[1]
        )
        camera.move(real_displacement)

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

    def get_rect(self, coordinate: Tuple[int, int]) -> Rect | None:
        """
        Returns the rectangle instance of the cell at a given coordinate.
        :return None if the coordinate is not valid.
        """
        if coordinate[0] < 0 or coordinate[1] < 0:
            return None

        return Rect(
            coordinate[0] * self.cell_size.width,
            coordinate[1] * self.cell_size.height,
            self.cell_size.width,
            self.cell_size.height,
        )

    def _get_map_offset(self) -> Vector2:
        """
        Gets map offset.
        """
        scene_manager: SceneManager = self.context["scene_manager"]
        map_controller: MapController = scene_manager.controller
        return map_controller.offset

    def set_action(self, action: int) -> None:
        """
        Sets this character's action.
        :param action: The action to set.
        """
        self.action = action

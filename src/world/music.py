from pygame import mixer

from src.core.context import Context
from src.core.loop import Loop
from src.world.context_module import ContextModule


class Music(ContextModule):
    def __init__(self, context: Context):
        super().__init__(context)

        # Current music path
        self.current_music: str | None = None

        # Music loop
        self.loop: Loop | None = None

        # Music fade fps
        self.fade_fps = 20

    @staticmethod
    def set_volume(volume: float) -> None:
        """
        Sets the volume of the current music.
        :param volume: The volume of the music.
        """
        mixer.music.set_volume(volume)

    @staticmethod
    def get_volume() -> float:
        """
        Gets the volume of the current music.
        """
        return mixer.music.get_volume()

    def play(self, music: str, volume=1.0) -> None:
        """
        Plays a music.
        :param music The path of the music file.
        :param volume: The volume of the music.
        """
        self.current_music = music
        mixer.music.load(music)
        mixer.music.set_volume(volume)
        mixer.music.play(-1)

    def fade_in(self, music: str, max_volume: float = 1.0, fade_time: int = 500) -> None:
        """
        Plays a music with fading in.
        :param music The path of the music file.
        :param max_volume: The maximum volume of the music.
        :param fade_time: The number of milliseconds to fade in the music.
        """
        self.play(music, 0)
        count = round(fade_time / self.fade_fps)

        def fade_in(index: int) -> None:
            volume = max_volume * (1 - (count - index) / count)
            Music.set_volume(volume)

            if index == count - 1:
                Music.set_volume(max_volume)

        self.loop = self.context.loop_manager.once(self.fade_fps, count, fade_in)

    def fade_out(self, fade_time: int = 500) -> None:
        """
        Stops the music with fading out.
        :param fade_time: The number of milliseconds to fade out the music.
        """
        count = round(fade_time / self.fade_fps)
        max_volume = Music.get_volume()

        def fade_out(index: int) -> None:
            volume = (count - index) / count * max_volume
            Music.set_volume(volume)

            if index == count - 1:
                self.stop()

        self.loop = self.context.loop_manager.once(self.fade_fps, count, fade_out)

    def stop(self) -> None:
        """
        Stops the current music.
        """
        self.set_volume(0)
        self.current_music = None

    def is_playing(self) -> None:
        """
        Checks whether the music is playing.
        """
        return self.current_music is not None

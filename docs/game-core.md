# Game Core

## Game Context

Game context includes everything of the game, and allows developers to store extra data.

~~~python
from src.core.game import Game
from src.core.context import Context

context = Context(Game())

# You can use context as if using a dictionary
context["user_level"] = 5
user_level = context["user_level"]

# You can access to game, settings, display, and many core instances via context
game = context.game
settings = context.settings
display = context.display
event_manager = context.event_manager
loop_manager = context.loop_manager

# You can access to the event data of the current processing event
event_data = context.event_data
~~~

## Game Settings

The class `src.core.settings.Settings` is a singleton object. It always returns the same instance every time you instantiate it.

~~~python
from src.core.settings import Settings

settings = Settings()
~~~

## Game Display

## Game Loop

Game loop module allows developers to create sub-loops, such as animations, timer, and so on. All sub-loops are refresh rate independent, as they update their inner elapsed time with a given delta time at each frame. Developers can create a loop using `context.loop_manager`:

~~~python
from src.core.game import Game
from src.core.context import Context

context = Context(Game())

fps = 5
counter_per_period = 10


def callback(index):
    # Update animation frames or something else here
    pass


# Register a loop using the loop manager
loop = context.loop_manager.loop(fps, counter_per_period, callback)

# Remove the loop from the loop manager
context.loop_manager.remove(loop)
~~~
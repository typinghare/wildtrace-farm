# Wildtrace Farm (野迹农场)

## Foreword

I have been dreaming of creating a game. However, I am obviously not a good self-learner, and I haven't made any complete graphical games. This time, I have to make one without any choice since it is an essential assignment for my college class.

Since I only have two weeks to accomplish it, I decided to make a simple idle game. I am inclined to make a farming game since my parents grew up as peasants, and while making the game I can acquire a little agricultural knowledge and talk with them in the future. There is an online game called QQ Farm, which was popular among the Chinese population ranging from six to 80s. Take inspiration from it and one of my favorite games—Stardew Valley—I designed the Wildtrace Farm.

I determined to make a complete program instead of a just-runnable one. That means I must focus much on advanced skills such as game development principles, frameworks, design patterns, and so on. Also, I will write complete documentation as professionally as I can.

## Get Started

To run Wildtrace Farm, you should install the following programs as prerequisites:

* Python `v3.11.5+`
* Pygame `v2.5.2+`

Start the game with the following command:

~~~shell
Python3 ./src/wildtrace-farm.py
~~~

### Gameplay

## Development

Wildtrace Farm is a charming and visually captivating pixel-style game, brought to life through the creative utilization of the Python-based game development library, [PyGame](https://www.pygame.org/docs/). This game transports players to a picturesque world where they can immerse themselves in the intricacies of farm life while enjoying the nostalgic aesthetics of pixel art.

The heart and soul of the game's design are encapsulated in the meticulously crafted tile set sourced from [Sprout Lands](https://cupnooble.itch.io/sprout-lands-asset-pack). This tile set breathes life into Wildtrace Farm, serving as the canvas upon which players cultivate their virtual agricultural dreams. The whimsical and detailed graphics of Sprout Lands seamlessly blend with the pixel style, ensuring an immersive and enchanting gaming experience.

Behind the scenes, the code that powers Wildtrace Farm is not just functional but also impeccably organized. It adheres to a high standard of code formatting using [Black](https://black.readthedocs.io/en/stable/), ensuring that the development process remains clean and maintainable. Additionally, the code is subjected to rigorous analysis and linting by [Pylint](https://pylint.readthedocs.io/en/stable/), guaranteeing that it not only looks good but is also optimized for performance and free of potential errors.

Regarding coding, I have meticulously organized the code into distinct sections, each thoughtfully accompanied by its dedicated documentation:

* [Game Resource Management](./docs/resource-management.md)
* [Game Lifecycle](./docs/game-lifecyle.md)

### Reference

* [Understanding framerate independence and delta time](https://www.youtube.com/watch?v=rWtfClpWSb8)
* [Stardew Valley Game Clone with Python and Pygame – Full Course](https://www.youtube.com/watch?v=R9apl6B_ZgI)
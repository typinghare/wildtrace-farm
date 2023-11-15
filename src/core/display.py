"""
Display module.
"""
from typing import List, Dict

import pygame
from pygame import Surface


class Layer:
    """
    A layer.
    """

    def __init__(self, name: str):
        # The name of this layer
        self.name = name

    def render(self, screen: Surface):
        """
        Renders this layer on the screen.
        :param screen The screen to render on.
        """
        pass


class Display:
    """
    Game display.
    """

    def __init__(self):
        # Screen
        self.screen: Surface = pygame.display.set_mode((800, 600))

        # Layer stack
        self.layer_stack: List[Layer] = []

        # A map from layer names to layers
        self._by_name: Dict[str, Layer] = {}

        self._init()

    def _init(self):
        """
        Initializes the builtin layers.
        """
        self.add_layer(Layer("water"))

    def add_layer(self, layer: Layer):
        """
        Adds a layer to the layer stack.
        :param layer: The layer to add.
        """
        self.layer_stack.append(layer)
        self._by_name[layer.name] = layer

    def get_layer(self, name: str) -> Layer:
        """
        Retrieves a layer by its name.
        :param name: The name of the layer to retrieve.
        :return: The layer.
        """
        return self._by_name[name]

    def render(self):
        """
        Renders the screen by drawing layers from bottom to top, ensuring that each subsequent
        layer covers the previous ones.
        """
        for layer in self.layer_stack:
            layer.render(self.screen)

        pygame.display.flip()

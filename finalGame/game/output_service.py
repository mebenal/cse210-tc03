import sys
import math
from game import constants
from asciimatics.widgets import Frame

class OutputService:
    """Outputs the game state. The responsibility of the class of objects is to draw the game state on the terminal. 
    
    Stereotype: 
        Service Provider

    Attributes:
        _screen (Screen): An Asciimatics screen.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            screen (Screen): An Asciimatics Screen.
        """
        
    def draw_layer(self, layer):
        """Renders the given actor's text on the screen.

        Args:
            actor (Actor): The actor to render.
        """ 
        layer.draw(filter='')

    def draw_layers(self, layers, drawOrder):
        """Renders the given list of actors on the screen.

        Args:
            actors (list): The actors to render.
        """ 
        for name in drawOrder:
            self.draw_layer(layers[name])
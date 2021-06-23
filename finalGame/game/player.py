from game import constants
import arcade

class Player(arcade.Sprite):
  """
  """

  def __init__(self, sprite):
    """The class constructor."""
    super().__init__()
    self.__dict__ = sprite.__dict__.copy()
    self._set_scale(constants.CHARACTER_SCALING)

  
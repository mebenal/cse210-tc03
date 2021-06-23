from game import constants
import arcade

class Enemy(arcade.Sprite):
  def __init__(self, sprite):
    """The class constructor."""
    super().__init__()
    self.__dict__ = sprite.__dict__.copy()
    self._set_scale(constants.CHARACTER_SCALING)

  def fight_or_flight(self, player, enemy):
    arcade.Sprite.get_distance_between_sprites(player, enemy)
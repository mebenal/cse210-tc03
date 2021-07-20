import arcade

from game import constants
from game.action import Action
from game.type_cast import Cast
from game.director_game import DirectorGame


class ActionHandleViewport(Action):
  """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
  Stereotype:
    Controller
  """
  def __init__(self):
    self._size = {}

  def execute(self, director:DirectorGame, cast:Cast, frame_count:int):
    """Executes the action using the given actors.

    Args:
      cast (dict): The game actors {key: tag, value: list}.
    """
    self._size = cast['map'].get_map_size()

    for (k,v) in self._size.items():
      self._size[k] = v * 16 * constants.TILE_SCALING

    left_side = self._limit_x_axis(cast['player'].left -  int(constants.SCREEN_WIDTH / 2))
    bottom_side = self._limit_y_axis(cast['player'].bottom -  int(constants.SCREEN_HEIGHT / 2))
           
    # Do the scrolling
    arcade.set_viewport( left_side,
                         left_side + constants.SCREEN_WIDTH,
                         bottom_side,
                         bottom_side + constants.SCREEN_HEIGHT )
      
  def _limit_x_axis(self, num:int) -> int:
    return max(min(num, self._size['width'] - constants.SCREEN_WIDTH), 0)

  def _limit_y_axis(self, num:int) -> int:
    return max(min(num, self._size['height'] - constants.SCREEN_HEIGHT), 0)

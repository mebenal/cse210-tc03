from game import constants
from game.constants import Cast
from game.action import Action

import arcade

class HandleCollisionsAction(Action):
  """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
  Stereotype:
    Controller
  """
  def __init__(self):
    return

  def execute(self, cast:Cast, frame_count:int):
    """Executes the action using the given actors.

    Args:
      cast (dict): The game actors {key: tag, value: list}.
    """
    for engine in cast['physics_engines']:
      engine.update()

    for projectile in cast['projectiles']:
      if projectile.has_traveled_distance():
        projectile.kill()
      else:
        collision = arcade.check_for_collision_with_list(projectile, cast['map'].get_layer('collision'))
        if len(collision) > 0:
          projectile.kill()
        collision = arcade.check_for_collision_with_list(projectile, cast['map'].get_layer(projectile.get_target()))
        if len(collision) > 0:
          projectile.kill(collision[0])

    cast['map'].get_layer('collision').update_animation()
    cast['map'].get_layer('background').update_animation()
      
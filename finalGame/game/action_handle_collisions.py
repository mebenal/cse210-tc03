
import arcade
from arcade.sprite import AnimatedTimeBasedSprite, Sprite

from game import constants
from game.action import Action
from game.type_game_cast import GameCast
from game.director_game import DirectorGame

class ActionHandleCollisions(Action):
  """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
  Stereotype:
    Controller
  """
  def __init__(self):
    return

  def execute(self, director:DirectorGame, cast:GameCast, frame_count:int):
    """Executes the action using the given actors.

    Args:
      cast (dict): The game actors {key: tag, value: list}.
    """

    for engine in cast['physics_engines']:
      collisions = engine.update()
      if len(collisions) > 0 and (collisions[0].properties['id'] == '245' or collisions[0].properties['id'] == '266'):
        director.load_next_map()

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

    for sprite in cast['map'].get_layer('collision'):
      if isinstance(sprite, AnimatedTimeBasedSprite):
        sprite.update_animation()
    for sprite in cast['map'].get_layer('background'):
      if isinstance(sprite, AnimatedTimeBasedSprite):
        sprite.update_animation()
      
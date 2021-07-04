from game import constants
from game.action import Action
import arcade

class HandleCollisionsAction(Action):
  """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
  Stereotype:
    Controller
  """
  def __init__(self):
    return

  def execute(self, cast, frame_count):
    """Executes the action using the given actors.

    Args:
      cast (dict): The game actors {key: tag, value: list}.
    """
    for engine in cast['physics_engines']:
      engine.update()

    cast['map'].get_layer('collision').update_animation()
    cast['map'].get_layer('background').update_animation()
      
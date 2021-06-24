from game import constants
from game.action import Action
from game.enemy import Enemy
import arcade


class MoveEnemyAction(Action):
  """A code template for controlling actors. The responsibility of this
  class of objects is translate user input into some kind of intent.
    
  Stereotype:
    Controller

  Attributes:
    _input_service (InputService): An instance of InputService.
  """

  def __init__(self):
    """The class constructor.
        

    Args:
      input_service (InputService): An instance of InputService.
    """

  def execute(self, cast):
    """Executes the action using the given actors.

    Args:
      cast (dict): The game actors {key: tag, value: list}.
    """
    for enemy in cast['enemies']:

      if arcade.get_distance_between_sprites(cast['player'], enemy) > 100:
        enemy.set_move_behavior(0)
      else:
        enemy.set_move_behavior(1)

    cast['enemies'].update()

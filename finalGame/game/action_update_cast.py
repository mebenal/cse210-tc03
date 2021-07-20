from game import constants
from game.action import Action
from game.type_cast import Cast
from game.director_game import DirectorGame


class ActionUpdateCast(Action):
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
    return

  def execute(self, director:DirectorGame, cast:Cast, frame_count:int):
    """Executes the action using the given actors.

    Args:
      cast (dict): The game actors {key: tag, value: list}.
   """
    cast['player'].update(cast['sound'])
    for enemy in cast['enemies']:
      enemy.update(cast['sound'])
    cast['player'].update_animation()
    for enemy in cast['enemies']:
      enemy.update_animation()
    cast['projectiles'].update()
    cast['ui'][1].update(cast)
    cast['sound'].update()

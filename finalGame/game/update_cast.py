from game import constants
from game.action import Action

class UpdateCast(Action):
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

  def execute(self, cast, frame_count):
    """Executes the action using the given actors.

    Args:
      cast (dict): The game actors {key: tag, value: list}.
   """
    cast['player'].update()
    cast['enemies'].update()
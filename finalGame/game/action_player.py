from game import constants
from game.action import Action
from game.type_cast import Cast
from game.director_game import DirectorGame
from game.input_service import InputService


class ActionPlayer(Action):
  """A code template for controlling actors. The responsibility of this
  class of objects is translate user input into some kind of intent.
    
  Stereotype:
    Controller

  Attributes:
    _input_service (InputService): An instance of InputService.
  """

  def __init__(self, input_service:InputService):
    """The class constructor.
        
    Args:
      input_service (InputService): An instance of InputService.
    """
    self._input_service = input_service

  def execute(self, director:DirectorGame, cast:Cast, frame_count:int):
    """Executes the action using the given actors.

    Args:
      cast (dict): The game actors {key: tag, value: list}.
   """
    player = cast['player']
    self._input_service.set_direction(player)
    self._input_service.update_options(player)

from game.type_start_menu_cast import StartMenuCast
from game.director_start_menu import DirectorStartMenu
from game.action import Action


class ActionStartMenu(Action):
  """A code template for a thing done in a game. The responsibility of 
  this class of objects is to interact with actors to change the state of the game. 
    
  Stereotype:
    Controller

  Attributes:
    _tag (string): The action tag (input, update or output).
  """

  def execute(self, director:DirectorStartMenu, cast:StartMenuCast, frame_count:int):
    """Executes the action using the given actors.

    Args:
      cast (dict): The game actors {key: tag, value: list}.
    """
    if cast['player'].get_exit_start_menu():
      director.window.show_view(cast['views'][1])
    cast['ui'][0].update(cast)
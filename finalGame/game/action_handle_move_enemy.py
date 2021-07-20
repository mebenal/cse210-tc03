import arcade

from game import constants
from game.action import Action
from game.type_cast import Cast
from game.director_game import DirectorGame


class ActionHandleMoveEnemy(Action):
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

  def execute(self, director:DirectorGame, cast:Cast, frame_count:int):
    """Executes the action using the given actors.

    Args:
      cast (dict): The game actors {key: tag, value: list}.
    """
    for enemy in cast['enemies']:
      distance = arcade.get_distance_between_sprites(cast['player'], enemy)
      enemy.set_distance_to_player(distance)
      if distance < constants.ENEMY_SIGHT or (enemy.get_health() < enemy.get_max_health()):
        weapon = enemy.get_item_of_slot('weapon')
        melee = True
        if weapon != None:
          melee = weapon.get_type() == 'melee'
        if (melee and distance > 10) or distance > 250:
          enemy.set_move_behavior(1)
        elif not melee and distance < 200:
          enemy.set_move_behavior(2)
        else:
          enemy.set_move_behavior(-1)
      else:
        enemy.set_move_behavior(0)
      
      enemy.update_movement(frame_count, cast['map'].get_layer('collision'), cast['player'].position)
      

    
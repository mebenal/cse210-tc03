from game import constants
from game.constants import Cast
from game.action import Action
from game.projectile import Projectile

import arcade
import math

class HandleAttackAction(Action):
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
    player = cast['player']
    mouse = cast['mouse']
    
    if player.get_attack() and player.can_attack():
      weapon = player.get_item_of_type('weapon')
      if weapon == None or weapon.get_type() == 'melee':
        nearest = arcade.get_closest_sprite(player, cast['enemies'])
        if weapon and weapon.get_range() >= nearest[1]:
          nearest[0].take_damage(weapon.get_damage())
        elif 50 >= nearest[1]:
          nearest[0].take_damage(15)
      elif weapon.get_type() == 'ranged':
        angle = math.atan2(mouse['y_pos'], mouse['x_pos'])
        change_x = constants.PROJECTILE_SPEED * math.cos(angle)
        change_y = constants.PROJECTILE_SPEED * math.sin(angle)
        cast['projectiles'].append(Projectile(player.position[0], player.position[1], 'enemy', weapon.get_damage(), change_x, change_y, weapon.get_range(), angle))
      player.reset_item_attack_cooldown()

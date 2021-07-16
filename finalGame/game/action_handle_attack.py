import math

import arcade
from arcade import SpriteList

from game import constants
from game.action import Action
from game.actor import Actor
from game.constants import Cast
from game.director_game import DirectorGame
from game.item import Item
from game.projectile import Projectile


class ActionHandleAttack(Action):
  """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
  Stereotype:
    Controller
  """
  def __init__(self):
    return

  def execute(self, director:DirectorGame, cast:Cast, frame_count:int):
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
        self.create_projectile(cast['projectiles'], player, weapon, [mouse['y_pos'], mouse['x_pos']], 'enemy')
      player.reset_item_attack_cooldown()
    
    for enemy in cast['enemies']:
      distance = enemy.get_distance_to_player()
      if distance < constants.ENEMY_SIGHT and enemy.can_attack():
        weapon = enemy.get_item_of_type('weapon')
        if weapon == None or weapon.get_type() == 'melee':
          if weapon and weapon.get_range() >= distance:
            player.take_damage(weapon.get_damage())
          elif 50 >= distance:
            player.take_damage(15)
        elif weapon.get_type() == 'ranged':
          position_to_attack = [player.position[1] - enemy.position[1], player.position[0] - enemy.position[0]]
          self.create_projectile(cast['projectiles'], enemy, weapon, position_to_attack, 'player')
        enemy.reset_item_attack_cooldown()

  def create_projectile(self, projectiles:SpriteList, sprite:Actor, weapon:Item, point:list[float,float], toAttack:str):
    angle = math.atan2(point[0],point[1])
    change_x = constants.PROJECTILE_SPEED * math.cos(angle)
    change_y = constants.PROJECTILE_SPEED * math.sin(angle)
    projectiles.append(Projectile(sprite.position[0], sprite.position[1], toAttack, weapon.get_damage(), change_x, change_y, weapon.get_range(), angle))

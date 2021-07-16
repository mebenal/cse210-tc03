import arcade
from arcade import Sprite, SpriteList

from game import constants
from game.action import Action
from game.type_game_cast import GameCast
from game.director_game import DirectorGame
from game.item import Item


class ActionHandleItems(Action):
  """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
  Stereotype:
    Controller
  """
  def __init__(self):
    self._size = {}

  def execute(self, director:DirectorGame, cast:GameCast, frame_count:int):
    """Executes the action using the given actors.

    Args:
      cast (dict): The game actors {key: tag, value: list}.
    """
    player = cast['player']
    items = cast['items']
  
    item_collisions = arcade.check_for_collision_with_list(player, cast['map'].get_layer('item'))
    if player.get_item_switch() and len(item_collisions) != 0 and player.can_switch_item():
      switch_dict = self.get_possible_switch(player, item_collisions[0])
      self.switch_item(player, items, switch_dict)
      player.reset_item_switch_cooldown()
    elif player.get_item_drop() and player.can_switch_item():
      self.drop_item(player, items)
      player.reset_item_switch_cooldown()


    for enemy in cast['enemies']:
      item_collisions = arcade.check_for_collision_with_list(enemy, cast['map'].get_layer('item'))
      if len(item_collisions) != 0 and enemy.can_switch_item():
        switch_dict = self.get_possible_switch(enemy, item_collisions[0])
        switch = False
        if switch_dict['sprite_item'] == None:
          switch = True
        elif switch_dict['sprite_item'].get_damage() < switch_dict['ground_item'].get_damage():
          switch = True
        if switch:
          self.switch_item(enemy, items, switch_dict)
          enemy.reset_item_switch_cooldown()

  def switch_item(self, sprite:Sprite, item_layer:SpriteList, switch_dict:dict[str:Item,str:Item]):
    if switch_dict['sprite_item'] != None:
      switch_dict['sprite_item'].position = switch_dict['ground_item'].position
      item_layer.append(switch_dict['sprite_item'])
    sprite.remove_item(switch_dict['sprite_item'])
    item_layer.remove(switch_dict['ground_item'])
    sprite.add_item(switch_dict['ground_item'])

  def get_possible_switch(self, sprite:Sprite, item:Item) -> dict:
    possible_switch = sprite.get_item_of_type(item.get_slot())
    return { "sprite_item" : possible_switch,
             "ground_item" : item }

  def drop_item(self, sprite:Sprite, item_layer:SpriteList):
    possible_drop = sprite.get_item_of_type('weapon')
    if possible_drop != None:
      possible_drop.position = sprite.position
      sprite.remove_item(possible_drop)
      item_layer.append(possible_drop)

from game.library_sound import LibrarySound
from game.actor_walking_animated import ActorWalkingAnimated
from game import constants
from game.actor import Actor

from arcade import Sprite

class Player(ActorWalkingAnimated):
  """
  """

  def __init__(self, sprite:Sprite):
    """The class constructor."""
    super().__init__(sprite)
    self._set_scale(constants.CHARACTER_SCALING)
    self._item_switch_held = None
    self._item_drop_held = None
    self._attack_held = None
    self._use_health_held = None

  def set_item_switch(self, key_pressed:bool):
    self._item_switch_held = key_pressed

  def get_item_switch(self) -> bool:
    return self._item_switch_held
  
  def set_item_drop(self, key_pressed:bool):
    self._item_drop_held = key_pressed

  def get_item_drop(self) -> bool:
    return self._item_drop_held

  def set_attack(self, key_pressed:bool):
    self._attack_held = key_pressed

  def get_attack(self) -> bool:
    return self._attack_held

  def set_use_health(self, key_pressed:bool):
    self._use_health_held = key_pressed
  
  def get_use_health(self) -> bool:
    return self._use_health_held

  def update(self, sound: LibrarySound):
    super().update(sound)
    if (self.change_x != 0 or self.change_y != 0) and sound.get_last_played('walking') > 10:
      sound.play_sound('walking')
 
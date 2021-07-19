from arcade import Sound
from pyglet.media.player import Player


class LibrarySound:
  def __init__(self):
    self._sounds =            { 'walking'          : Sound(r'./finalGame/game/SFX/walking.wav'         ),
                                'player_melee_hit' : Sound(r'./finalGame/game/SFX/player_melee_hit.ogg'),
                                'fist_hit'         : Sound(r'./finalGame/game/SFX/fist.ogg'            ),
                                'swing'            : Sound(r'./finalGame/game/SFX/swing.wav'           ),
                                'bow'              : Sound(r'./finalGame/game/SFX/bow.wav'             ),
                                'death'            : Sound(r'./finalGame/game/SFX/death.wav'           ),
                                'enemy_melee_hit'  : Sound(r'./finalGame/game/SFX/enemy_melee_hit.wav' )}
    self._sound_last_played = {}
    for i, (k, v) in enumerate(self._sounds.items()):
      self._sound_last_played[k] = 0

  def play_sound(self, sound:str):
    to_play = self._sounds.get(sound)
    if to_play:
      to_play.play()
      self._sound_last_played[sound] = 0

  def get_sound(self, sound:str) -> Sound:
    return self._sounds.get(sound)

  def get_last_played(self, sound:str) -> int:
    return self._sound_last_played.get(sound)

  def update(self):
    for i, (k, sound) in enumerate(self._sounds.items()):
      self._sound_last_played[k] += 1
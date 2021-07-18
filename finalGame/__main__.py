from game.load_animation_textures import LoadAnimationTextures
from game.type_script import Script
from game.type_scripts import Scripts
from typing import Iterable, List, TypedDict

import arcade
from arcade import PhysicsEngineSimple
from arcade.sprite_list import SpriteList

from game import constants
from game.type_casts import Casts
from game.action_draw import ActionDraw
from game.action_handle_attack import ActionHandleAttack
from game.action_handle_collisions import ActionHandleCollisions
from game.action_handle_items import ActionHandleItems
from game.action_handle_move_enemy import ActionHandleMoveEnemy
from game.action_handle_viewport import ActionHandleViewport
from game.action_player import ActionPlayer
from game.action_update_cast import ActionUpdateCast
from game.director_game import DirectorGame
from game.input_service import InputService
from game.map import Map
from game.output_service import OutputService
from game.type_game_cast import GameCast
from game.ui import UI


def main():
  # create the cast {key: tag, value: list}

  casts: Casts = {}
  game_cast: GameCast = {}

  game_cast['map'] = Map()
  game_cast['player'] = game_cast['map'].get_layer('player')[0]
  game_cast['enemies'] = game_cast['map'].get_layer('enemy')
  game_cast['items'] = game_cast['map'].get_layer('item')
  game_cast['projectiles'] = game_cast['map'].get_layer('projectile')
  game_cast['physics_engines'] = [PhysicsEngineSimple(game_cast['player'], game_cast['map'].get_layer('collision'))]
  game_cast['mouse'] = {'x_pos' : 0, 'y_pos' : 0}
  game_cast['ui'] = UI()
  game_cast['animation_textures'] = LoadAnimationTextures(game_cast['map'].get_tileset('actors'))
  
  casts['game_cast'] = game_cast


  input_service = InputService()
  
  scripts: Scripts = {}
  game_script: Script = {}

  game_script['input'] = [ActionPlayer(input_service)]
  game_script['update'] = [ActionHandleCollisions(), ActionHandleMoveEnemy(), ActionHandleViewport(), ActionHandleItems(), ActionHandleAttack(), ActionUpdateCast()]
  game_script['output'] = [ActionDraw(OutputService())]

  scripts['game_script'] = game_script

  window = arcade.Window(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)

  director_game = DirectorGame(window)
  director_game.setup(casts['game_cast'], scripts['game_script'], input_service)
  window.show_view(director_game)
  arcade.run()

if __name__ == "__main__":
  main()

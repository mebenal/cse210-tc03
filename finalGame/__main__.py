from game.ui_start_menu import UIStartMenu
from game.action_start_menu import ActionStartMenu
from game.director_start_menu import DirectorStartMenu
from game.library_items import LibraryItems
from game.library_sound import LibrarySound
from game.library_animation_textures import LibraryAnimationTextures
from game.type_script import Script
from game.type_scripts import Scripts
from game.type_cast import Cast

import arcade
from arcade import PhysicsEngineSimple
from arcade.sprite_list import SpriteList

from game import constants
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
from game.ui_game import UIGame


def main():
  # create the cast {key: tag, value: list} 

  cast: Cast = {}

  cast['map'] = Map()
  cast['player'] = cast['map'].get_layer('player')[0]
  cast['enemies'] = cast['map'].get_layer('enemy')
  cast['items'] = cast['map'].get_layer('item')
  cast['projectiles'] = cast['map'].get_layer('projectile')
  cast['physics_engines'] = [PhysicsEngineSimple(cast['player'], cast['map'].get_layer('collision'))]
  cast['mouse'] = {'x_pos' : 0, 'y_pos' : 0}
  cast['ui'] = [UIStartMenu(), UIGame()]
  cast['animation_textures'] = LibraryAnimationTextures(cast['map'].get_tileset('actors'))
  cast['sound'] = LibrarySound()
  cast['item_textures'] = LibraryItems(cast['map'].get_tileset('weapons'))


  


  input_service = InputService()
  
  scripts: Scripts = {}
  game_script: Script = {}
  start_menu_script: Script = {}

  game_script['input'] = [ActionPlayer(input_service)]
  game_script['update'] = [ActionHandleCollisions(), ActionHandleMoveEnemy(), ActionHandleViewport(), ActionHandleAttack(), ActionHandleItems(), ActionUpdateCast()]
  game_script['output'] = [ActionDraw(OutputService())]

  start_menu_script['input'] = [ActionPlayer(input_service)]
  start_menu_script['update'] = [ActionHandleViewport(), ActionStartMenu()]
  start_menu_script['output'] = [ActionDraw(OutputService())]

  scripts['game_script'] = game_script
  scripts['start_menu_script'] = start_menu_script

  window = arcade.Window(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)

  director_game = DirectorGame(window)
  director_game.setup(cast, scripts['game_script'], input_service)

  director_start_menu = DirectorStartMenu(window)
  director_start_menu.setup(cast, scripts['start_menu_script'], input_service)

  cast['views'] = [director_start_menu, director_game]

  window.show_view(director_start_menu)
  arcade.run()

if __name__ == "__main__":
  #import cProfile, pstats
  #profiler = cProfile.Profile()
  #profiler.enable()
  main()
  #profiler.disable()
  #stats = pstats.Stats(profiler).sort_stats('tottime')
  #astats.print_stats()
  

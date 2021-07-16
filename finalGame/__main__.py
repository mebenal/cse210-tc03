from typing import Iterable, List, TypedDict

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
from game.type_game_cast import GameCast
from game.ui import UI


def main():
  # create the cast {key: tag, value: list}
  cast: GameCast = {}
  cast['map'] = Map()
  cast['player'] = cast['map'].get_layer('player')[0]
  cast['enemies'] = cast['map'].get_layer('enemy')
  cast['items'] = cast['map'].get_layer('item')
  cast['projectiles'] = cast['map'].get_layer('projectile')
  cast['physics_engines'] = [PhysicsEngineSimple(cast['player'], cast['map'].get_layer('collision'))]
  cast['mouse'] = {'x_pos' : 0, 'y_pos' : 0}
  cast['ui'] = UI()

  input_service = InputService()
  
  script = {}
  script['input'] = [ActionPlayer(input_service)]
  script['update'] = [ActionHandleCollisions(), ActionHandleMoveEnemy(), ActionHandleViewport(), ActionHandleItems(), ActionHandleAttack(), ActionUpdateCast()]
  script['output'] = [ActionDraw(OutputService())]
  window = arcade.Window(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
  director = DirectorGame(window)
  director.setup(cast, script, input_service)
  window.show_view(director)
  arcade.run()

if __name__ == "__main__":
  main()

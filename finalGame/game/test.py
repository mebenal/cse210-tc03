import arcade
from game import constants

class Test(arcade.Window):
  def __init__(self, map):
    super().__init__(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
    self.physics_engine = None
    self.map = map
    self.player_list = None

    self.view_bottom = 0
    self.view_left = 0

  def setup(self):
    self.player_list = arcade.SpriteList()
    image_source = r"C:\Users\Michael\Downloads\char1.bmp"
    self.player_sprite = arcade.Sprite(image_source, constants.CHARACTER_SCALING)
    self.player_sprite.center_x = 128 * constants.TILE_SCALING
    self.player_sprite.center_y = 400 * constants.TILE_SCALING
    self.player_list.append(self.player_sprite)

    self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                     self.map.get_layers()['collision'])
        

  def on_draw(self):
    arcade.start_render()

    layers = self.map.get_layers()
        
    layers['background'].draw(filter="")
    layers['path'].draw(filter="")
    layers['collision'].draw(filter="")
    self.player_list.draw(filter="")
    layers['foreground'].draw(filter="")

  def on_key_press(self, key, modifiers):
    if key == arcade.key.UP or key == arcade.key.W:
      self.player_sprite.change_y = constants.PLAYER_MOVEMENT_SPEED
    elif key == arcade.key.DOWN or key == arcade.key.S:
      self.player_sprite.change_y = -constants.PLAYER_MOVEMENT_SPEED
    elif key == arcade.key.LEFT or key == arcade.key.A:
      self.player_sprite.change_x = -constants.PLAYER_MOVEMENT_SPEED
    elif key == arcade.key.RIGHT or key == arcade.key.D:
      self.player_sprite.change_x = constants.PLAYER_MOVEMENT_SPEED

  def on_key_release(self, key, modifiers):
    if key == arcade.key.UP or key == arcade.key.W:
      self.player_sprite.change_y = 0
    elif key == arcade.key.DOWN or key == arcade.key.S:
      self.player_sprite.change_y = 0
    elif key == arcade.key.LEFT or key == arcade.key.A:
      self.player_sprite.change_x = 0
    elif key == arcade.key.RIGHT or key == arcade.key.D:
      self.player_sprite.change_x = 0

  def on_update(self, delta_time):
    self.physics_engine.update()

    changed = False

    # Scroll left
    left_boundary = self.view_left + constants.LEFT_VIEWPORT_MARGIN
    if self.player_sprite.left < left_boundary:
      self.view_left -= left_boundary - self.player_sprite.left
      changed = True

    # Scroll right
    right_boundary = self.view_left + constants.SCREEN_WIDTH - constants.RIGHT_VIEWPORT_MARGIN
    if self.player_sprite.right > right_boundary:
      self.view_left += self.player_sprite.right - right_boundary
      changed = True

    # Scroll up
    top_boundary = self.view_bottom + constants.SCREEN_HEIGHT - constants.TOP_VIEWPORT_MARGIN
    if self.player_sprite.top > top_boundary:
      self.view_bottom += self.player_sprite.top - top_boundary
      changed = True

    # Scroll down
    bottom_boundary = self.view_bottom + constants.BOTTOM_VIEWPORT_MARGIN
    if self.player_sprite.bottom < bottom_boundary:
      self.view_bottom -= bottom_boundary - self.player_sprite.bottom
      changed = True

    if changed:
      # Only scroll to integers. Otherwise we end up with pixels that
      # don't line up on the screen
      self.view_bottom = int(self.view_bottom)
      self.view_left = int(self.view_left)

      # Do the scrolling
      arcade.set_viewport(self.view_left,
                          constants.SCREEN_WIDTH + self.view_left,
                          self.view_bottom,
                          constants.SCREEN_HEIGHT + self.view_bottom)
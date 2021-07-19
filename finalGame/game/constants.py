SCREEN_WIDTH = 1420
SCREEN_HEIGHT = 700
SCREEN_TITLE = 'Hero Man v0.0.1'
#1080
#1920
CHARACTER_SCALING = 3
ITEM_SCALING = 2
TILE_SCALING = 8
SPRITE_PIXEL_SIZE = 16
GRID_PIXEL_SIZE = (SPRITE_PIXEL_SIZE * TILE_SCALING)

PLAYER_MOVEMENT_SPEED = 5
ENEMY_MOVEMENT_SPEED = 2
PROJECTILE_SPEED = 20

ENEMY_SIGHT = 250

FACE_RIGHT = 1
FACE_LEFT = 2
FACE_UP = 3
FACE_DOWN = 4

TILE_LAYERS = ['background', 'path', 'collision', 'player', 'enemy', 'item', 'foreground']
DRAW_LAYERS = ['background', 'path', 'collision', 'player', 'enemy', 'item', 'projectile', 'weapons', 'foreground']

RECTANGLE_ORDER = ['player_weapon_cooldown', 'player_health_cooldown', 'player_health_outline', 'player_health_bar']

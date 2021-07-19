from arcade import sprite, tilemap
from arcade.texture import Texture
from pytiled_parser.objects import TileSet

class LibraryItems:
  def __init__(self, tileset:TileSet):
    self._items = []
    if not tileset:
      return
    for tile in tileset.tiles:
      filename = tilemap._get_image_source(tileset.tiles[tile], None, None)
      image_x, image_y, width, height = tilemap._get_image_info_from_tileset(tileset.tiles[tile])
      self._items.append(sprite.load_texture(filename, image_x, image_y,
                                             width, height))
    

  def get_item_by_id(self, id:int) -> Texture:
    if id < len(self._items) and id >= 0 and isinstance(id, int):
      return self._items[id]
    return None
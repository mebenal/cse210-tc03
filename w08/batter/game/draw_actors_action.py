from game.action import Action

# TODO: Define the DrawActorsAction class here


class DrawActorsAction(Action):
    def __init__(self, output_service):
        self._output_service = output_service

    def execute(self, cast):
        self._output_service.clear_screen()
        for member in cast.values():
            self._output_service.draw_actors(member)
        self._output_service.flush_buffer()
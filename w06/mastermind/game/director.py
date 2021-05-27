from game.roster import Roster
from game.console import Console
from game.player import Player
from game.code import Code
from game.hint import Hint

class Director:

  def __init__(self):
        

    self._roster = Roster()
    self._console = Console()
    self._code = Code()
    self._hint = Hint()
    self._keep_playing = True

  def start_game(self):


    self._prepare_game()
    while self._keep_playing:
      self._get_inputs()
      self._do_updates()
      self._do_outputs()


  def _prepare_game(self):


    for n in range(2):
      name = self._console.read(f"Enter a name for player {n + 1}: ")
      self._roster.add_player(Player(name))
      self._player = self._roster.get_current()
      self._hint.add_player_hint(self._player.get_name(), self._player.get_guess(), self._player.get_checked_guess())
        
    self._roster.next_player()
    self._player = self._roster.get_current() 
    self._console.write(self._hint.display_hint())
    self._hint.reset_hint()
    
  def _get_inputs(self):

        
        
    
    self._console.write(f"{self._player.get_name()}'s turn:")
    self._player.set_guess(str(self._console.read_number("What is your guess?: ")))
        
  def _do_updates(self):
        

        
    self._player.set_checked_guess(self._code.check_guess(self._player.get_guess()))
    for player in self._roster.get_players():
      self._hint.add_player_hint(player.get_name(), player.get_guess(), player.get_checked_guess())
    self._keep_playing = self._code.is_won(self._player.get_guess())



  def _do_outputs(self):


    self._console.write(self._hint.display_hint())
    if not self._keep_playing:
      self._console.write(f"{self._player.get_name()} won!")
    self._hint.reset_hint()

    self._roster.next_player()
    self._player = self._roster.get_current()
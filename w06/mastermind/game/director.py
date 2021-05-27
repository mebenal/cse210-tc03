from game.roster import Roster
from game.console import Console
from game.player import Player
from game.code import Code
from game.hint import Hint

class Director:

    def __init__(self):
        

        self._roster = Roster()
        self._console = Console()
        self._player = Player()
        self._code = None
        self._hint = Hint()
        self._keep_playing() = True

    def start_game(self):


        self._prepare_game()
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()


    def _prepare_game(self):


        for n in range(2):
            name = self._console.read(f"Enter a name for player {n + 1}: ")
            player = Player(name)
            self._roster.add_player(player)
            self.addPlayerHint(player.getName(), player.getGuess(), '0000')
        
        hint = self._hint.displayHint()
        self._console.write(hint)
    
    def _get_inputs(self):

        
        
        player = self._roster.getCurrent()
        self._console.write(f"{player.get_name()}'s turn:")
        guess = self._console.read_number("What is your guess?: ")
        check_guess = self._code.checkGuess(guess)
        self.addPlayerHint(player, guess, check_guess)


    
    def _do_updates(self):
        

        player = self._roster.get_current()
        


    def _do_outputs(self):



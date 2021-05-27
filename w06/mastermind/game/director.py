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
            self._player = self._roster.getCurrent()
            self._hint.addPlayerHint(self._player.getName(), self._player.getGuess(), '0000')
        
        self._roster.next_player()
        self._player = self._roster.getCurrent()
        hint = self._hint.displayHint()
        self._console.write(hint)
        self._hint.resetHint()
    
    def _get_inputs(self):

        
        
    
        self._console.write(f"{self._player.getName()}'s turn:")
        guess = self._console.read_number("What is your guess?: ")
        self._player.setGuess(str(guess))
        
        


    
    def _do_updates(self):
        

        
        self._player.setCheckedGuess(self._code.checkGuess(self._player.getGuess()))
        for i in self._roster.players:
            self._hint.addPlayerHint(i.getName(), i.getGuess(), i.getCheckedGuess())
        self._keep_playing = self._code.isWon(self._player.getGuess())



    def _do_outputs(self):


        self._console.write(self._hint.displayHint())
        if not self._keep_playing:
            self._console.write(f"{self._player.getName()} won!")
        self._hint.resetHint()

        self._roster.next_player()
        self._player = self._roster.getCurrent()



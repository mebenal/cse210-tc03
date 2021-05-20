from game.console import Console
from game.player import Player
from game.puzzle import Puzzle

class Director:
  """A code template for a person who directs the game. The responsibility of 
  this class of objects is to keep track of the points and control the 
  sequence of play.
  Attributes:
      keep_playing (boolean): Whether or not the player wants to keep playing
                              if they haven't lost.
      points (int): The total number of points earned.
      dealer (Dealer): An instance of the class of objects known as Dealer.
  """
  
  def __init__(self):
    """The class constructor.
    Args:
        self (Director): an instance of Director.
    """
    self.keep_playing = True
    self.console = Console()
    self.player = Player()
    self.puzzle = Puzzle()
  
  def start_game(self):
    """Starts the game loop to control the sequence of play.
    Args:
        self (Director): an instance of Director.
    """
    self.do_outputs()
    while self.keep_playing and not self.puzzle.isWon():
      guess = self.get_inputs()
      self.do_updates(guess)
      self.do_outputs()
  
  def get_inputs(self):
    """Gets the inputs at the beginning of each round of play. In this case,
    that means showing the current card and asking the user for hi or low.
    Args:
        self (Director): An instance of Director.
    """
    return self.console.read("Guess a letter [a-z]: ")
  
  def do_updates(self, guess):
    """Updates the important game information for each round of play. In 
    this case, that means updating the points and determining whether they
    lost the game.
    Args:
        self (Director): An instance of Director.
        answer (str): Whether the user choose hi or low.
    """
    isCorrect = self.puzzle.checkGuess(guess)
    self.player.updateLife(isCorrect)
    self.keep_playing = bool(self.player.getLife())

  
  def do_outputs(self):
    """Outputs the important game information for each round of play. In 
    this case, that means what the next card was, what their score is, and
    whether they want to keep playing if they haven't lost the game.
    Args:
        self (Director): An instance of Director.
    """
    self.console.write(self.puzzle.display_correct())
    self.console.write(self.player.displayParachute())
class Hint:

  def __init__(self):
    self.reset_hint()

  def _checked_guess_to_hint(self, checkedGuess):
    return str(checkedGuess).replace('0','*').replace('1','o').replace('2','x')

  def add_player_hint(self, playerName, playerGuess, checkedGuess):
    self._hint.insert(-1,f'Player {playerName}: {playerGuess}, {self._checked_guess_to_hint(checkedGuess)}')

  def reset_hint(self):
    self._hint = ["--------------------","--------------------"]

  def display_hint(self):
    return '\n'.join(self._hint)

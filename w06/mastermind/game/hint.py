class Hint:

  def __init__(self):
    self.resetHint()

  def _checkedGuessToHint(self, checkedGuess):
    return str(checkedGuess).replace('0','*').replace('1','o').replace('2','x')

  def addPlayerHint(self, playerName, playerGuess, checkedGuess):
    self.hint.insert(-1,f'Player {playerName}: {playerGuess}, {self._checkedGuessToHint(checkedGuess)}')

  def resetHint(self):
    self.hint = ["--------------------","--------------------"]

  def displayHint(self):
    return '\n'.join(self.hint)
import random

class Code:


    def __init__(self):
        self._code = str(random.randint(1000, 9999))
        

    def check_guess(self, guess):
        hint = ""
        for i in range(len(guess)):
            if guess[i] == self._code[i]:
                hint += "2"
            elif guess[i] in self._code:
                hint += "1"
            else:
                hint += "0"
            
        return hint

    def _multiple(self, hint, guess):
        if self.code.count() < guess.count():
            



        


bob = Code()

print(bob.check_guess("4594"))
print(bob._code)
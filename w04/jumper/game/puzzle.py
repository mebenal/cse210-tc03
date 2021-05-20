import random

words = ["consciousness", "cable", "lecture", "linear", "coincidence", "demonstration",
            "operation", "angel", "sickness", "compliance", "autonomy", "level", "practice"
            "cause", "inhibition", "broken", "battle", "modest", "safety", "teenager"]

class Puzzle:
    
    
    def __init__(self):
        self.chosen_word = words[random.randint(0, len(words))]
        self.correct_list = ["_"] * len(self.chosen_word)


    def checkGuess(self, letter):
        if letter in self.chosen_word:
            for i in range(len(self.chosen_word)):
                if self.chosen_word[i] == letter:
                    self.correct_list[i] = letter
            return True
        else:
            return False
    
    def display_correct(self):
        return " ".join(self.correct_list)

            
    
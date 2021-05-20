
parachutes = [
"""   
   X 
  /|\   
  / \ 
        
^^^^^^^  """,
"""
  \ / 
   0 
  /|\   
  / \ 
         
^^^^^^^ """,
""" 
 \   / 
  \ / 
   0 
  /|\   
  / \ 
         
^^^^^^^ """,
"""   
 /___\ 
 \   / 
  \ / 
   0 
  /|\   
  / \ 
         
^^^^^^^ """,
""" 
  ___  
 /___\ 
 \   / 
  \ / 
   0 
  /|\   
  / \ 
         
^^^^^^^ """]

class Player:

    def __init__(self):
        self.health = 4


    def updateLife(self, check):
        if not check:
            self.health -= 1
        
    def displayParachute(self): 
        return parachutes[self.health]

    def getLife(self):
        return self.health
        

    
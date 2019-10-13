from domino import Domino

class Board:
    "The Board State"
    
    def __init__(self):
        self.dominoes = []
        
    def add_domino(self, domino: Domino):
        "add a domino to the board"
        self.dominoes.append(domino)
        
    def show(self):
        for domino in self.dominoes:
            print(domino, sep="", end="")
                
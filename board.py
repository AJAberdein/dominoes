from domino import Domino

class Board:
    "The Board State"
    
    def __init__(self):
        self.dominoes = []
        
    def __repr__(self) -> str:
        "show the board state"
        return self.show()
        
    def add_domino(self, domino: Domino):
        "add a domino to the board"
        self.dominoes.append(domino)
        
    def show(self) -> str:
        board_str = ""
        for domino in self.dominoes:
            board_str += domino.show()
        return board_str
                
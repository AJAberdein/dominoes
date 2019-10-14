from domino import Domino

class Hand:
    "A hand of dominos instance"
    
    def __init__(self):
        self.dominoes = {}
        
    def __repr__(self) -> str:
        "show a player's hand"
        return self.show()
    
    def add_domino(self, domino: Domino):
        "add a domino to this hand"
#         self.dominoes.append({domino.id : domino})
        self.dominoes[domino.id] = domino 
        
    def remove_domino(self, domino_id: int):
        "remove a domino from this hand"
        del self.dominoes[domino_id]
    
    def show(self):
        hand_str = ""
        for domino in self.dominoes.values():
            hand_str += domino.show()
        return hand_str
        
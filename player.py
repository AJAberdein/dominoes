from domino import Domino
from hand import Hand

class Player:
    "A Player instance"
    
    def __init__(self, name: str):
        self.name = = name
        self.hand = Hand()
    
    def add_domino(self, domino: Domino):
        "add a domino to this player's hand"
        self.hand.add_domino({domino.id : domino})
        
    def remove_domino(self, domino_id: int):
        "remove a domino from this player's hand"
        self.hand.remove_domino({domino.id : domino})
        
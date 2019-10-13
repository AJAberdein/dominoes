class Hand:
    "A hand of dominos instance"
    
    def __init__(self):
        self.dominoes = [int, Domino]
    
    def add_domino(self, domino: Domino):
        "add a domino to this hand"
        self.dominoes.append({domino.id : domino})
        
    def remove_domino(self, domino_id: int):
        "remove a domino from this hand"
        del self.dominoes[domino_id]
        
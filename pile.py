import random
from domino import Domino

class Pile:
    "The Pile of Dominoes instance"
    
    def __init__(self):
        self.dominoes = {}
        self.initialize_starting_dominoes()
        
    def initialize_starting_dominoes(self):
        "creates a new Domino instance for every valid combination and attach them to the Pile"
        index = 0
        for i in range(7):
            for j in range(i+1):
                index +=1
                self.dominoes[index] = Domino(index, i, j) 
        
    def take_domino(self) -> Domino:
        "take a random domino from the pile and return it"
        id = random.choice(list(self.dominoes.keys()))
        domino = self.dominoes[id]
        del self.dominoes[id]
        return domino
        
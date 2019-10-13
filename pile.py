from domino import Domino

class Pile:
    "The Pile of Dominoes instance"
    
    def __init__(self):
        self.dominoes = [int, Domino]
        self.initialize_starting_dominoes()
        
    def initialize_starting_dominoes(self):
        index = 0
        for i in range(7):
            for j in range(i+1):
                index +=1
                self.dominoes.append({index : Domino(index, i, j) })      
        
            
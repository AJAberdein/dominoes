from player import Player
from pile import Pile

class Game:
    "The Game State"
    
    def start(self):
        "begin a new game of Dominoes"
        print("Welcome to Dominoes!", end="\n\n")
        self.pile = Pile()
        self.create_players()
        self.deal()
    
    def create_players(self):
        "creates 2 new players: Athur and Dutch"
        self.player_1 = Player('Arthur Morgan')
        self.player_2 = Player('Dutch')
        
    def deal(self):
        "deal 7 domninoes to each player, one at a time"
        for i in range(7):
            domino_1 = self.pile.take_domino()
            self.player_1.add_domino(domino_1)
            domino_2 = self.pile.take_domino()
            self.player_2.add_domino(domino_2)


game = Game()
game.start()
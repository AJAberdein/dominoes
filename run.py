from player import Player
from pile import Pile
from board import Board

import random

class Game:
    "The Board State"
    
    def start(self):
        "begin a new game of Dominoes"
        print("Welcome to Dominoes!", end="\n\n")
        self.pile = Pile()
        self.board = Board()
        self.create_players()
        self.deal()
        self.set_starting_tile()
    
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
        print('\n')

    def set_starting_tile(self):
        domino = self.pile.take_domino()
        self.board.add_domino(domino)
        print('BOARD:')
        print(self.board)
        
        


game = Game()
game.start()
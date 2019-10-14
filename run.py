from player import Player
from pile import Pile
from board import Board

import random
from pick import pick





class Game:
    "The Board State"
    
    def start(self):
        "begin a new game of Dominoes"
        print("Welcome to Dominoes!", end="\n\n")
        self.setup_game()
        
    def setup_game(self):
        self.pile = Pile()
        self.board = Board()
        self.create_players()
        self.deal()
        self.set_starting_tile()
        self.play()
    
    def create_players(self):
        "creates 2 new players: Athur and Dutch"
        self.players = [
            Player('Arthur Morgan'),
            Player('Dutch')
        ]
        
    def deal(self):
        "deal 7 domninoes to each player, one at a time"
        for i in range(7):
            domino_1 = self.pile.take_domino()
            self.players[0].add_domino(domino_1)
            domino_2 = self.pile.take_domino()
            self.players[1].add_domino(domino_2)
        print('\n')

    def set_starting_tile(self):
        domino = self.pile.take_domino()
        self.board.add_domino(domino)
        
    def play(self):
        self.game_end = False
        p = 0
        while(not self.game_end):
            self.turn(self.players[p])
            p = 1 if p == 0 else 0
        
    def turn(self, player):
        new_domino = self.pile.take_domino()
        player.add_domino(new_domino)
        domino, position = self.make_move(player)
        self.place_domino(player, domino, position)
        print(domino)
        
    def make_move(self, player):
        valid_moves = self.get_valid_moves(player.hand)
        move_display = list(map(lambda move : 'PLACE ' + (move["domino"]).show() +  ' ' + move["placement"], valid_moves)) 
        move, index = pick(move_display, self.get_selection_heading(player))
        player_move = valid_moves[index]
        return (player_move ['domino'], player_move ['placement'])
        
    def place_domino(self, player, domino, position):        
        player.remove_domino(domino.id)
        self.board.add_domino(domino, position)
        
    def get_selection_heading(self, player):
        player_details = str(player.name) + "'s Turn"
        board = "Board:\n" + str(self.board)
        hand = "\n\nHand\n" + str(player.hand)
        title = "\n\nSelect a valid move:\n" 
        return player_details + board + hand + title
        
    def get_valid_moves(self, hand):
        first = self.board.dominoes[0]
        last = self.board.dominoes[-1]
        moves = []
        for domino in hand.dominoes.values():
            if(domino.value_1 == first.value_1 or domino.value_2 == first.value_1):
                moves.append({"domino": domino, "placement": "LEFT"})   
            if(domino.value_1 == last.value_2 or domino.value_2 == last.value_2):
                moves.append({"domino": domino, "placement": "RIGHT"})   
        return moves
    

        
        

game = Game()
game.start()
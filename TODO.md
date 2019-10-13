


## To Do List:

# Classes

- Domino
- Hand
- Player
- Pile (generates dominoes)
- Board


# Running

on start:
 - create a new Pile (and assign it new 28 dominoes)
 - create a new Player
 - create a new empty hand for eahc player
 - each player draws from pile on by one (log to console (Arthur draws (domino), Dutch draws (domino)))
 - board draws starting tile and displays board

player turn:
 - player draws
 - show hand
 - IF valid tiles
 - Prompt pick tile and show valid tiles you can use
 	- IF avalable spots on board == 1
 		- place
 	- IF avalable spots on board == 2
 		-prompt: place LEFT or RIGHT
 - IF ! valid tiles
 	- players draws
 - IF pile.length == 0
 	- end turn
 - IF hand.length == 0
 	- PLAYER WINS (log('Domino!/nArthur Wins!'))

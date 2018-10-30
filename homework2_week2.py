#------------------------------------------------
# Homework 2 of course "Python for Research"
# HarvardX -  PH526xEdX, EdX
#------------------------------------------------

#Exercise 1
import numpy as np

def create_board():
    """creates 3 x3 numpy array"""
    board=np.zeros((3,3))
    return(board)

#Exercise 2
def place(board,player,position):
    """ Allows placement of player 1 or 2 on empty (corresponding to (0,0) position on board """
    if board[position]==0 and (player==1 or player==2):
        board[position]=player
    return(board)

#Exercise 3
def possibilities(board):
    """" Find all positions (as tuples), where numpy array board is 0, returns tuples as list """
    positions=np.array(np.where(board==0)).T #only arrays can be transposed, np.where returns tuple
    list_of_tuples=list(map(tuple,positions))
    return(list_of_tuples)


#Exercise 4
def random_place(board,player):
    """ places a marker for the current player (1 or 2) at random among all positions with value 0 in board """
    import random
    selection=possibilities(board)
    position=random.choice(selection)
    board=place(board,player,position)
    return(board)

#Exercise 5
board = create_board()
for j in range(3):
    for player in [1,2]:
        board=random_place(board,player)
print(board)

#Exercise 6
def row_win(board, player):
    for i in range(board.shape[0]):
        if (set(board[i,:]) == {player})==True:
            return(True)
    return(False)

row_win(board,1)

#Exercise 7
def col_win(board, player):
    for i in range(board.shape[0]):
        if (set(board[:,i]) == {player})==True:
            return(True)
    return(False)

#Exercise 8
def diag_win(board, player):
    for i in range(board.shape[1]):
        if (set(np.diagonal(board)) == {player})==True:
            return(True)
    return(False)

diag_win(board, 1)



#Exercise 9
def evaluate(board):
    winner = 0
    for player in [1, 2]:
        # Check if `row_win`, `col_win`, or `diag_win` apply.
		# If so, store `player` as `winner`.
        if (row_win(board, player)==True or col_win(board, player)==True or
         diag_win(board, player)==True):
            winner=player
            return(winner)
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner

evaluate(board)
board


player=[1,2]
results=player+[-1]
board=create_board()
results
player
for j in range(5): #better: while winner==0
    for i in player:
        board=random_place(board,i)
        if (evaluate(board) in results)==True:
            print([board,evaluate(board)])
            break




#Exercise 10
def play_game():
    player=[1,2]
    results=player+[-1]
    board=create_board()
    #for j in range(5):
    while(evaluate(board)==0):
        for i in player:
            board=random_place(board,i)
            if (evaluate(board) in results)==True:
                return(evaluate(board))


play_game()

#Exercise 11
import time as time
import matplotlib.pyplot as plt
start=time.time()
winners=[]
for i in range(1000):
    winners.append(play_game())
stop=time.time()
print(stop-start)


plt.hist(winners); #player one wins more often
plt.show(winners);

#Exercise 12
def play_strategic_game():
    board, winner = create_board(), 0
    board[1,1] = 1
    while winner == 0:
        for player in [2,1]:
            # use `random_place` to play a game, and store as `board`.
            board=random_place(board,player)
            # use `evaluate(board)`, and store as `winner`.
            winner=evaluate(board)
            if winner != 0:
                return(winner)
                break

play_strategic_game()

#Exercise 13
start=time.time()
winners=[]
for i in range(1000):
    winners.append(play_strategic_game())
stop=time.time()
print(stop-start)


plt.hist(winners); #player one wins more often
plt.show();

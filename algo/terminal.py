# Functional class that defines whether or not the board position is in the END state and a node is terminal.
# This is determined by a win, or tie if the board is filled

def winning_move(board, player):
    # checking vertical win possibility 
    for col in range(7):
        for row in range(3):
            if board[row][col] == player and board[row+1][col] == player and board[row+2][col] == player and board[row+3][col] == player:
                return True
            
    # checking horizontal win possibility
    for col in range(4):
        for row in range(6):
            if board[row][col] == player and board[row][col+1] == player and board[row][col+2] == player and board[row][col+3] == player:
                return True
            
    # checking sloped up 
    for col in range(4):
        for row in range(3):
            if board[row][col] == player and board[row+1][col+1] == player and board[row+2][col+2] == player and board[row+3][col+3] == player:
                return True
            
    # checking sloped down 
    for col in range(4):
        for row in range(3, 6): 
            if board[row][col] == player and board[row-1][col+1] == player and board[row-2][col+2] == player and board[row-3][col+3] == player:
                return True
            
   # if none are winning moves, return false
    return False


def is_terminal(board): 
    return winning_move(board, player)